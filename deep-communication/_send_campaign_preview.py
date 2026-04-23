"""Preview a campaign email: assemble header + body + footer, upload to R2, send.

Usage:
    python _send_campaign_preview.py

Edit the "Campaign config" section below to switch campaign/locale/recipient.
If a campaign wants to include the shared promo block, read campaigns/promo.html
and insert it between {body_rendered} and {footer_rendered}.
"""
import uuid
import os
import boto3
from dotenv import load_dotenv
from send_email import send_email

load_dotenv()

# ── R2 config ────────────────────────────────────────────────
R2_BUCKET = "emails"
R2_PUBLIC_BASE = "https://emails.step.is"

s3 = boto3.client(
    "s3",
    endpoint_url=os.getenv("R2_ENDPOINT_URL"),
    aws_access_key_id=os.getenv("R2_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("R2_SECRET_ACCESS_KEY"),
    region_name="auto",
)

# ── Campaign config ──────────────────────────────────────────
campaign_slug = "introduce-nspace-users-to-step-app"
lang = "vi"  # "en" or "vi"
subject = "Step — Ứng dụng học ngôn ngữ mới từ đội ngũ NSpace"
to_email = "lelong88@gmail.com"
from_email = "hello@step.is"

# ── Locale data ──────────────────────────────────────────────
TAGLINES = {
    "en": "Language courses built around content you'd actually enjoy",
    "vi": "Khóa học ngôn ngữ từ nội dung bạn thực sự thích",
}
WEBSITE_URLS = {
    "en": "https://step.is",
    "vi": "https://step.is/vi",
}

# ── Read templates ───────────────────────────────────────────
with open("campaigns/header.html") as f:
    header = f.read()
with open(f"campaigns/{campaign_slug}/body.html") as f:
    body = f.read()
with open("campaigns/footer.html") as f:
    footer = f.read()

# ── Render ───────────────────────────────────────────────────
header_rendered = header.replace("{{tagline}}", TAGLINES[lang])
body_rendered = body.replace("{{website_url}}", WEBSITE_URLS[lang])

# Generate R2 key upfront so view_url is known before upload
email_id = uuid.uuid4().hex
r2_key = f"{campaign_slug}/{email_id}.html"
view_url = f"{R2_PUBLIC_BASE}/{r2_key}"

footer_rendered = (
    footer
    .replace("{{unsubscribe_url}}", "#unsubscribe-preview")
    .replace("{{view_url}}", view_url)
)

full_html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{subject}</title>
</head>
<body style="margin:0;padding:0;background-color:#ffffff;">
{header_rendered}
{body_rendered}
{footer_rendered}
</body>
</html>"""

# ── Upload to R2 ─────────────────────────────────────────────
s3.put_object(
    Bucket=R2_BUCKET,
    Key=r2_key,
    Body=full_html.encode("utf-8"),
    ContentType="text/html; charset=utf-8",
)
print(f"Uploaded to: {view_url}")

# ── Send ─────────────────────────────────────────────────────
result = send_email(
    subject=subject,
    body=full_html,
    from_email=from_email,
    to_email=to_email,
    html=True,
)

if not result["success"]:
    raise SystemExit(f"Failed: {result['message']}")
