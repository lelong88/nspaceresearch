"""
Bulk send a campaign to every subscriber in a list, with:
  - Confirmation prompt before live sends
  - Deduplication against email_campaign_send (never send duplicates, safe to resume)
  - Per-recipient R2 view_url tracked in the database
  - Configurable pacing (default 200ms between sends, ~5/sec — under SES default 14/s)

Usage (as a script):
    python send_bulk.py <campaign_slug> <list_id> <campaign_id> <lang> "<subject>" [options]

    Required positional args:
        campaign_slug  — directory name under campaigns/
        list_id        — email_list ID to send to
        campaign_id    — email_campaign ID (for dedup tracking)
        lang           — "en" or "vi"
        subject        — email subject line (quoted)

    Options:
        --from=<email>     override sender address (default: support@step.is)
        --delay-ms=<ms>    pacing between sends (default: 200)
        --limit=<n>        cap number of recipients (useful for testing)
        --dry-run          render only, don't send or record
        --yes              skip confirmation prompt (USE WITH CARE)

Usage (as a module):
    from send_bulk import send_bulk
    send_bulk(campaign_slug="...", list_id=1, campaign_id=1,
              subject="...", lang="vi", from_email="long@nspace.is")
"""

import os
import sys
import time
import socket
import subprocess
import urllib.parse
import urllib.request
import json
from dotenv import load_dotenv

from campaign_email import send_campaign_email, FROM_EMAIL as DEFAULT_FROM

load_dotenv()

# ── DNS workaround ───────────────────────────────────────────
# The dev box's local resolver returns NXDOMAIN for email.step.is. Resolve via
# Cloudflare (1.1.1.1) and pin the IPv4 result via a getaddrinfo override.
_DNS_OVERRIDES: dict[str, str] = {}

def _resolve_via_cloudflare(host: str) -> str | None:
    try:
        out = subprocess.check_output(
            ["nslookup", "-type=A", host, "1.1.1.1"],
            stderr=subprocess.DEVNULL,
            timeout=5,
        ).decode()
    except (subprocess.SubprocessError, FileNotFoundError):
        return None
    lines = out.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("Name:"):
            for next_line in lines[i + 1 :]:
                if next_line.startswith("Address:"):
                    addr = next_line.split(":", 1)[1].strip()
                    if "." in addr:
                        return addr
    return None

def _pin_host(host: str) -> None:
    try:
        if socket.getaddrinfo(host, None, socket.AF_INET):
            return
    except socket.gaierror:
        pass
    ip = _resolve_via_cloudflare(host)
    if ip:
        _DNS_OVERRIDES[host] = ip

_orig_getaddrinfo = socket.getaddrinfo
def _getaddrinfo(host, port, *args, **kwargs):
    if host in _DNS_OVERRIDES:
        return _orig_getaddrinfo(_DNS_OVERRIDES[host], port, *args, **kwargs)
    results = _orig_getaddrinfo(host, port, *args, **kwargs)
    v4 = [r for r in results if r[0] == socket.AF_INET]
    return v4 if v4 else results
socket.getaddrinfo = _getaddrinfo


# ── Constants ────────────────────────────────────────────────

API_BASE = "https://email.step.is/api"
UNSUBSCRIBE_BASE = "https://email.step.is/unsubscribe"
DEFAULT_DELAY_MS = 200
USER_AGENT = "step-email-bulk-sender/1.0"

_pin_host("email.step.is")


# ── API helpers ──────────────────────────────────────────────

def _auth_headers() -> dict[str, str]:
    key = os.getenv("API_KEY")
    if not key:
        raise SystemExit("API_KEY not set in environment")
    return {"X-API-Key": key, "User-Agent": USER_AGENT}


def _api_get(path: str) -> list | dict:
    req = urllib.request.Request(f"{API_BASE}{path}", headers=_auth_headers())
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def _api_post(path: str, body: dict) -> tuple[int, dict]:
    req = urllib.request.Request(
        f"{API_BASE}{path}",
        data=json.dumps(body).encode(),
        headers={**_auth_headers(), "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.status, json.load(resp)
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read().decode() or "{}")


def _fetch_subscribers(list_id: int) -> list[dict]:
    rows = _api_get(f"/lists/{list_id}/subscribers")
    return [r for r in rows if r.get("status") == "subscribed"]


def _fetch_already_sent(campaign_id: int) -> set[str]:
    """Return set of emails that already have a send record for this campaign."""
    rows = _api_get(f"/campaigns/{campaign_id}/sends")
    return {r["email"] for r in rows}


def _record_send(campaign_id: int, email: str, view_url: str) -> tuple[bool, bool]:
    """Record a send. Returns (ok, already_sent)."""
    status, body = _api_post(
        f"/campaigns/{campaign_id}/sends",
        {"email": email, "status": "sent", "view_url": view_url},
    )
    if status == 201:
        return True, False
    if status == 200 and body.get("already_sent"):
        return True, True
    return False, False


def _unsubscribe_url(email: str, list_id: int) -> str:
    return f"{UNSUBSCRIBE_BASE}?{urllib.parse.urlencode({'email': email, 'list_id': list_id})}"


# ── Guardrail ────────────────────────────────────────────────

def _confirm(summary: dict, auto_yes: bool) -> bool:
    """Show a summary and require typed confirmation before live sends."""
    print("=" * 60)
    print("BULK SEND CONFIRMATION")
    print("=" * 60)
    for k, v in summary.items():
        print(f"  {k:<16} {v}")
    print("=" * 60)

    if auto_yes:
        print("--yes flag set — skipping prompt")
        return True

    prompt = (
        f"\nAbout to send {summary['to send']} emails FROM '{summary['from']}'.\n"
        f"Type the FROM address to confirm: "
    )
    answer = input(prompt).strip()
    return answer == summary["from"]


# ── Main sender ──────────────────────────────────────────────

def send_bulk(
    campaign_slug: str,
    list_id: int,
    campaign_id: int,
    subject: str,
    lang: str = "en",
    from_email: str = DEFAULT_FROM,
    variables_fn=None,
    delay_ms: int = DEFAULT_DELAY_MS,
    dry_run: bool = False,
    limit: int | None = None,
    auto_yes: bool = False,
) -> dict:
    """
    Send a campaign to every subscribed recipient on a list.

    Dedup: checks email_campaign_send before each send; skips any (campaign_id, email)
    pair that already has a send record. Safe to resume — duplicates are never sent.
    """
    subscribers = _fetch_subscribers(list_id)
    already_sent = _fetch_already_sent(campaign_id)

    # Filter out already-sent recipients
    pending = [s for s in subscribers if s["email"] not in already_sent]
    skipped = len(subscribers) - len(pending)

    if limit:
        pending = pending[:limit]

    summary = {
        "campaign slug": campaign_slug,
        "campaign id": campaign_id,
        "list id": list_id,
        "from": from_email,
        "subject": subject,
        "lang": lang,
        "subscribed": len(subscribers),
        "already sent": skipped,
        "to send": len(pending),
        "pacing": f"{delay_ms}ms (~{1000/delay_ms:.1f}/sec)",
        "mode": "DRY RUN" if dry_run else "LIVE SEND",
    }

    # Guardrail: require confirmation for any live send
    if not dry_run and len(pending) > 0:
        if not _confirm(summary, auto_yes):
            print("\nAborted.")
            return {"sent": 0, "failed": 0, "skipped": skipped, "aborted": True}

    if len(pending) == 0:
        print("=" * 60)
        for k, v in summary.items():
            print(f"  {k:<16} {v}")
        print("=" * 60)
        print("Nothing to send (all recipients already sent or list empty).")
        return {"sent": 0, "failed": 0, "skipped": skipped, "aborted": False}

    print()

    sent = 0
    failed = 0
    errors: list[str] = []
    delay_s = delay_ms / 1000.0
    total = len(pending)

    for i, sub in enumerate(pending, start=1):
        email = sub["email"]
        extras = variables_fn(sub) if variables_fn else None
        unsub_url = _unsubscribe_url(email, list_id)
        progress = f"[{i}/{total}]"

        if dry_run:
            print(f"{progress} DRY: would send to {email}")
            sent += 1
        else:
            try:
                # Send (renders, uploads to R2, sends via SES)
                result = send_campaign_email(
                    campaign_slug=campaign_slug,
                    subject=subject,
                    to_email=email,
                    lang=lang,
                    variables=extras,
                    from_email=from_email,
                    unsubscribe_url=unsub_url,
                )
                if not result.get("success"):
                    failed += 1
                    msg = f"{email}: {result.get('message')}"
                    errors.append(msg)
                    print(f"{progress} ✗ {msg}")
                else:
                    # Record in DB (idempotent — ON CONFLICT DO NOTHING)
                    ok, _already = _record_send(campaign_id, email, result["view_url"])
                    if not ok:
                        failed += 1
                        errors.append(f"{email}: DB record failed")
                        print(f"{progress} ✗ {email}: sent but DB record failed")
                    else:
                        sent += 1
                        print(f"{progress} ✓ {email}")
            except Exception as e:
                failed += 1
                errors.append(f"{email}: {e}")
                print(f"{progress} ✗ {email}: {e}")

        if i < total:
            time.sleep(delay_s)

    print()
    print(f"Done. Sent: {sent}, Failed: {failed}, Skipped (already sent): {skipped}, Total subscribers: {len(subscribers)}")
    return {
        "sent": sent,
        "failed": failed,
        "skipped": skipped,
        "total": len(subscribers),
        "errors": errors,
        "aborted": False,
    }


# ── CLI ──────────────────────────────────────────────────────

def _parse_args(argv: list[str]) -> dict:
    if len(argv) < 6:
        print(__doc__)
        raise SystemExit(1)

    opts = {
        "campaign_slug": argv[1],
        "list_id": int(argv[2]),
        "campaign_id": int(argv[3]),
        "lang": argv[4],
        "subject": argv[5],
        "dry_run": "--dry-run" in argv,
        "auto_yes": "--yes" in argv,
        "from_email": DEFAULT_FROM,
        "delay_ms": DEFAULT_DELAY_MS,
        "limit": None,
    }
    for arg in argv[6:]:
        if arg.startswith("--from="):
            opts["from_email"] = arg.split("=", 1)[1]
        elif arg.startswith("--delay-ms="):
            opts["delay_ms"] = int(arg.split("=", 1)[1])
        elif arg.startswith("--limit="):
            opts["limit"] = int(arg.split("=", 1)[1])
    return opts


if __name__ == "__main__":
    opts = _parse_args(sys.argv)
    result = send_bulk(**opts)
    sys.exit(0 if not result.get("aborted") and result.get("failed", 0) == 0 else 1)
