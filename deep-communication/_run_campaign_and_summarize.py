#!/usr/bin/env python3
"""
Run a bulk campaign send and email a summary to the specified address.

Usage:
    python _run_campaign_and_summarize.py <campaign_slug> <list_id> <campaign_id> <lang> "<subject>" [options]

    Options:
        --from=<email>       override sender address (default: support@step.is)
        --notify=<email>     summary recipient (default: long@nspace.is)
        --delay-ms=<ms>      pacing between sends (default: 200)
        --limit=<n>          cap number of recipients
        --dry-run            render-only, no sends

Examples:
    # Run current campaign
    python _run_campaign_and_summarize.py introduce-nspace-users-to-step-app 2 1 vi \
        "Step — Ứng dụng học ngôn ngữ mới từ đội ngũ NSpace" --from=long@nspace.is

    # Future campaign with custom notify
    python _run_campaign_and_summarize.py welcome-back-users 5 3 en \
        "We missed you!" --notify=team@step.is

    # Dry run
    python _run_campaign_and_summarize.py my-campaign 2 4 vi "Subject" --dry-run --limit=5

This script is designed to be run interactively, by `at`, or by cron. It:
  1. Runs send_bulk (with --yes to skip confirmation)
  2. Queries the DB for final campaign stats
  3. Sends a plain-text summary email to the notify address
"""

import os
import sys
import datetime
import psycopg
from dotenv import load_dotenv

# Ensure we're in the right directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

load_dotenv()

from send_bulk import send_bulk, DEFAULT_DELAY_MS
from send_email import send_email
from campaign_email import FROM_EMAIL as DEFAULT_FROM

NOTIFY_DEFAULT = "long@nspace.is"


def get_db_stats(campaign_id: int) -> dict:
    """Query the DB for authoritative campaign send stats."""
    conn = psycopg.connect(os.environ["DATABASE_URL"])
    cur = conn.cursor()
    cur.execute(
        """SELECT
             COUNT(*) as total,
             COUNT(*) FILTER (WHERE status = 'sent') as sent,
             COUNT(*) FILTER (WHERE status = 'bounced') as bounced,
             MIN(sent_at) as first_sent,
             MAX(sent_at) as last_sent
           FROM email_campaign_send
           WHERE email_campaign_id = %s""",
        (campaign_id,),
    )
    row = cur.fetchone()
    cur.close()
    conn.close()
    return {
        "total_records": row[0],
        "sent": row[1],
        "bounced": row[2],
        "first_sent": row[3],
        "last_sent": row[4],
    }


def run_campaign_and_summarize(
    campaign_slug: str,
    list_id: int,
    campaign_id: int,
    lang: str,
    subject: str,
    from_email: str = DEFAULT_FROM,
    notify_email: str = NOTIFY_DEFAULT,
    delay_ms: int = DEFAULT_DELAY_MS,
    limit: int | None = None,
    dry_run: bool = False,
) -> dict:
    """
    Run a bulk campaign send and email a summary.

    Returns the send_bulk result dict augmented with db_stats.
    """
    print(f"[{datetime.datetime.utcnow().isoformat()}] Starting bulk send...")

    result = send_bulk(
        campaign_slug=campaign_slug,
        list_id=list_id,
        campaign_id=campaign_id,
        subject=subject,
        lang=lang,
        from_email=from_email,
        delay_ms=delay_ms,
        limit=limit,
        dry_run=dry_run,
        auto_yes=True,
    )

    print(f"[{datetime.datetime.utcnow().isoformat()}] Bulk send finished: {result}")

    # Get authoritative stats from DB
    stats = get_db_stats(campaign_id)

    # Build summary
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    summary_lines = [
        f"Campaign: {campaign_slug}",
        f"Campaign ID: {campaign_id}",
        f"List ID: {list_id}",
        f"From: {from_email}",
        f"Subject: {subject}",
        f"Language: {lang}",
        "",
        "── This Run ──",
        f"  Sent: {result['sent']}",
        f"  Skipped (already sent): {result['skipped']}",
        f"  Failed: {result['failed']}",
        f"  Total subscribers: {result['total']}",
        "",
        "── Overall (from DB) ──",
        f"  Total send records: {stats['total_records']}",
        f"  Delivered: {stats['sent']}",
        f"  Bounced: {stats['bounced']}",
        f"  First sent: {stats['first_sent']}",
        f"  Last sent: {stats['last_sent']}",
        "",
        f"Report generated: {now}",
    ]

    if result.get("errors"):
        summary_lines.append("")
        summary_lines.append("── Errors ──")
        for err in result["errors"][:50]:
            summary_lines.append(f"  • {err}")

    summary_text = "\n".join(summary_lines)
    print("\n" + summary_text)

    # Send summary email
    send_result = send_email(
        subject=f"[Campaign Summary] {campaign_slug} — {now}",
        body=summary_text,
        from_email="support@step.is",
        to_email=notify_email,
        html=False,
    )

    if send_result.get("success"):
        print(f"\n✓ Summary email sent to {notify_email}")
    else:
        print(f"\n✗ Failed to send summary email: {send_result.get('message')}")

    return {**result, "db_stats": stats}


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
        "from_email": DEFAULT_FROM,
        "notify_email": NOTIFY_DEFAULT,
        "delay_ms": DEFAULT_DELAY_MS,
        "limit": None,
        "dry_run": "--dry-run" in argv,
    }
    for arg in argv[6:]:
        if arg.startswith("--from="):
            opts["from_email"] = arg.split("=", 1)[1]
        elif arg.startswith("--notify="):
            opts["notify_email"] = arg.split("=", 1)[1]
        elif arg.startswith("--delay-ms="):
            opts["delay_ms"] = int(arg.split("=", 1)[1])
        elif arg.startswith("--limit="):
            opts["limit"] = int(arg.split("=", 1)[1])
    return opts


if __name__ == "__main__":
    opts = _parse_args(sys.argv)
    result = run_campaign_and_summarize(**opts)
    sys.exit(0 if not result.get("aborted") and result.get("failed", 0) == 0 else 1)
