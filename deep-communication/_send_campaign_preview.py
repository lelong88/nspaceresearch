"""
Send a preview of a campaign email to a single recipient.

Usage:
    python _send_campaign_preview.py                          # uses defaults below
    python _send_campaign_preview.py <campaign_slug> <lang>   # override campaign and locale
"""
import sys
from campaign_email import send_campaign_email

# ── Defaults (edit these or pass as CLI args) ────────────────
CAMPAIGN_SLUG = "introduce-nspace-users-to-step-app"
LANG = "vi"
SUBJECT = "Step — Ứng dụng học ngôn ngữ mới từ đội ngũ NSpace"
TO_EMAIL = "lelong88@gmail.com"

def main():
    slug = sys.argv[1] if len(sys.argv) > 1 else CAMPAIGN_SLUG
    lang = sys.argv[2] if len(sys.argv) > 2 else LANG

    result = send_campaign_email(
        campaign_slug=slug,
        subject=SUBJECT,
        to_email=TO_EMAIL,
        lang=lang,
        unsubscribe_url="#unsubscribe-preview",
    )

    if result["success"]:
        print(f"View in browser: {result['view_url']}")
    else:
        raise SystemExit(f"Failed: {result['message']}")

if __name__ == "__main__":
    main()
