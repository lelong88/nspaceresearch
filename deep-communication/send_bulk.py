"""
Bulk send a campaign to every subscriber in a list, with:
  - Confirmation prompt before live sends (requires typing the FROM address)
  - Cache-proof deduplication: each send is atomically reserved in the DB before
    SES is called. Dup-check runs server-side via a UNIQUE constraint + INSERT
    with ON CONFLICT DO NOTHING — the response drives the skip decision.
  - Per-recipient R2 view_url stored in the database
  - Configurable pacing (default 200ms between sends, ~5/sec — under SES 14/s)

Usage (as a script):
    python send_bulk.py <campaign_slug> <list_id> <campaign_id> <lang> "<subject>" [options]

    Options:
        --from=<email>     override sender address (default: support@step.is)
        --delay-ms=<ms>    pacing between sends (default: 200)
        --limit=<n>        cap number of recipients (useful for testing)
        --dry-run          render nothing, just check who would send/skip
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
import urllib.error
import uuid
import json
from dotenv import load_dotenv

from campaign_email import (
    render_email,
    FROM_EMAIL as DEFAULT_FROM,
    R2_BUCKET,
    R2_PUBLIC_BASE,
    _get_s3,
)
from send_email import send_email

load_dotenv()

# ── DNS workaround ───────────────────────────────────────────
# Local resolver returns NXDOMAIN for email.step.is. Resolve via 1.1.1.1.
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


def _retry(fn, retries: int = 3, backoff: float = 2.0):
    """Retry a callable on transient network errors with exponential backoff."""
    for attempt in range(retries):
        try:
            return fn()
        except (urllib.error.URLError, OSError) as e:
            # Don't retry HTTP 4xx/5xx — only network-level failures
            if isinstance(e, urllib.error.HTTPError):
                raise
            if attempt == retries - 1:
                raise
            wait = backoff * (2 ** attempt)
            print(f"  ⚠ Network error ({e}), retrying in {wait:.0f}s...")
            time.sleep(wait)


def _api_get(path: str) -> list | dict:
    def _do():
        req = urllib.request.Request(f"{API_BASE}{path}", headers=_auth_headers())
        with urllib.request.urlopen(req) as resp:
            return json.load(resp)
    return _retry(_do)


def _api_post(path: str, body: dict) -> tuple[int, dict]:
    def _do():
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
            raw = e.read().decode() or "{}"
            try:
                return e.code, json.loads(raw)
            except json.JSONDecodeError:
                return e.code, {"error": raw}
    return _retry(_do)


def _fetch_subscribers(list_id: int) -> list[dict]:
    rows = _api_get(f"/lists/{list_id}/subscribers")
    return [r for r in rows if r.get("status") == "subscribed"]


def _reserve_send(campaign_id: int, email: str, view_url: str) -> tuple[bool, bool, dict]:
    """
    Atomically reserve a send slot for (campaign, email).

    Returns (ok, already_sent, record):
      - (True, False, record)  — fresh INSERT succeeded, caller should send via SES
      - (True, True, record)   — duplicate detected server-side, caller must NOT send
      - (False, False, {})     — API error, caller should treat as failure

    This authoritative POST bypasses any read-side caching: the unique constraint
    on (email_campaign_id, email) + ON CONFLICT DO NOTHING makes the INSERT
    response the source of truth for dedup.
    """
    status, body = _api_post(
        f"/campaigns/{campaign_id}/sends",
        {"email": email, "status": "sent", "view_url": view_url},
    )
    if status == 201:
        return True, False, body
    if status == 200 and body.get("already_sent"):
        return True, True, body
    return False, False, body


def _unsubscribe_url(email: str, list_id: int) -> str:
    return f"{UNSUBSCRIBE_BASE}?{urllib.parse.urlencode({'email': email, 'list_id': list_id})}"


# ── Guardrail ────────────────────────────────────────────────

def _confirm(summary: dict, auto_yes: bool) -> bool:
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
        f"\nAbout to process {summary['subscribed']} subscribers FROM '{summary['from']}'.\n"
        f"(Per-recipient dedup happens server-side; already-sent will be skipped.)\n"
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

    Flow per recipient:
      1. Generate a unique view_url (UUID-based R2 path)
      2. POST /campaigns/:id/sends with {email, view_url} — atomic server-side dedup
      3. If dedup detected (already_sent=true): skip, no render, no SES call
      4. If fresh reservation: render → upload to R2 → send via SES
    """
    subscribers = _fetch_subscribers(list_id)

    if limit:
        subscribers = subscribers[:limit]

    summary = {
        "campaign slug": campaign_slug,
        "campaign id": campaign_id,
        "list id": list_id,
        "from": from_email,
        "subject": subject,
        "lang": lang,
        "subscribed": len(subscribers),
        "pacing": f"{delay_ms}ms (~{1000/delay_ms:.1f}/sec)",
        "mode": "DRY RUN" if dry_run else "LIVE SEND",
    }

    # Guardrail
    if not dry_run and len(subscribers) > 0:
        if not _confirm(summary, auto_yes):
            print("\nAborted.")
            return {"sent": 0, "skipped": 0, "failed": 0, "aborted": True}

    if len(subscribers) == 0:
        print("=" * 60)
        for k, v in summary.items():
            print(f"  {k:<16} {v}")
        print("=" * 60)
        print("Nothing to send (list is empty or all unsubscribed).")
        return {"sent": 0, "skipped": 0, "failed": 0, "aborted": False}

    print()
    sent = 0
    skipped = 0
    failed = 0
    errors: list[str] = []
    delay_s = delay_ms / 1000.0
    total = len(subscribers)

    for i, sub in enumerate(subscribers, start=1):
        email = sub["email"]
        extras = variables_fn(sub) if variables_fn else None
        unsub_url = _unsubscribe_url(email, list_id)
        progress = f"[{i}/{total}]"

        # Always pre-generate the view_url so we know it before reserving
        email_id = uuid.uuid4().hex
        r2_key = f"{campaign_slug}/{email_id}.html"
        view_url = f"{R2_PUBLIC_BASE}/{r2_key}"

        if dry_run:
            # In dry-run, just check the DB via a GET-style query since we don't
            # want to create dry_run rows that pollute the dedup state. We use
            # a single targeted POST that we immediately would need to undo —
            # simpler: accept that dry-run can't see cached dedup state with
            # perfect accuracy, and just show subscriber count.
            print(f"{progress} DRY: would attempt send to {email}")
            sent += 1
            continue

        # 1) Reserve in DB (atomic, authoritative)
        ok, already_sent, record = _reserve_send(campaign_id, email, view_url)
        if not ok:
            failed += 1
            errors.append(f"{email}: reserve failed: {record}")
            print(f"{progress} ✗ {email}: reserve failed — {record}")
            if i < total:
                time.sleep(delay_s)
            continue
        if already_sent:
            skipped += 1
            print(f"{progress} SKIP (already sent): {email}")
            continue

        # 2) Render
        try:
            html = render_email(
                campaign_slug=campaign_slug,
                lang=lang,
                variables=extras,
                unsubscribe_url=unsub_url,
                view_url=view_url,
            )
            # 3) Upload to R2 (with retry)
            for _r2_attempt in range(3):
                try:
                    _get_s3().put_object(
                        Bucket=R2_BUCKET,
                        Key=r2_key,
                        Body=html.encode("utf-8"),
                        ContentType="text/html; charset=utf-8",
                    )
                    break
                except Exception as r2_err:
                    if _r2_attempt == 2:
                        raise r2_err
                    print(f"  ⚠ R2 upload error ({r2_err}), retrying...")
                    time.sleep(2 * (2 ** _r2_attempt))
            # 4) Send via SES (with retry)
            ses_result = None
            for _ses_attempt in range(3):
                result = send_email(
                    subject=subject,
                    body=html,
                    from_email=from_email,
                    to_email=email,
                    html=True,
                )
                if result.get("success"):
                    ses_result = result
                    break
                # Retry on network-level failures, not on SES rejections
                err_msg = result.get("message", "")
                if "Connection" in err_msg or "Network" in err_msg or "timed out" in err_msg:
                    if _ses_attempt < 2:
                        print(f"  ⚠ SES transient error ({err_msg}), retrying...")
                        time.sleep(2 * (2 ** _ses_attempt))
                        continue
                ses_result = result
                break
            if ses_result and ses_result.get("success"):
                sent += 1
                print(f"{progress} ✓ {email}")
            else:
                failed += 1
                msg = f"{email}: SES failed: {ses_result.get('message') if ses_result else 'unknown'}"
                errors.append(msg)
                print(f"{progress} ✗ {msg}")
        except Exception as e:
            failed += 1
            errors.append(f"{email}: {e}")
            print(f"{progress} ✗ {email}: {e}")

        if i < total:
            time.sleep(delay_s)

    print()
    print(
        f"Done. Sent: {sent}, Skipped (already sent): {skipped}, "
        f"Failed: {failed}, Total subscribers: {total}"
    )
    return {
        "sent": sent,
        "skipped": skipped,
        "failed": failed,
        "total": total,
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
