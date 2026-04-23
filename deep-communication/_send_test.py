"""Send a test email: render header + body + [promo] + footer, upload to R2, then send via SES."""
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

# ── Read shared templates ────────────────────────────────────
with open("campaigns/header.html") as f:
    header = f.read()
with open("campaigns/promo.html") as f:
    promo = f.read()
with open("campaigns/footer.html") as f:
    footer = f.read()

# ── Config ───────────────────────────────────────────────────
lang = "en"                # "en" or "vi"
include_promo = True       # set False to skip app download + social links

taglines = {
    "en": "Language courses built around content you'd actually enjoy",
    "vi": "Khóa học ngôn ngữ từ nội dung bạn thực sự thích",
}

website_urls = {
    "en": "https://step.is",
    "vi": "https://step.is/vi",
}

ZALO_LINK_HTML = ""  # kept for reference; no longer used in promo.html

# ── Test body ────────────────────────────────────────────────
body = f"""
<div style="margin:0;padding:0;background-color:#ffffff;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#ffffff;">
    <tr>
      <td align="center" style="padding:24px;">
        <table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0">
          <tr>
            <td style="padding:24px 0;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;">
              <h1 style="margin:0 0 16px;font-size:24px;font-weight:700;color:#1f2937;">
                Template Test Email
              </h1>
              <p style="margin:0 0 12px;font-size:15px;line-height:1.6;color:#4b5563;">
                Testing: lang={lang}, promo={include_promo}
              </p>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</div>
"""

# ── Render ───────────────────────────────────────────────────
header_rendered = header.replace("{{tagline}}", taglines[lang])

promo_rendered = ""
if include_promo:
    promo_rendered = promo.replace("{{website_url}}", website_urls[lang])

footer_rendered = footer.replace("{{unsubscribe_url}}", "#unsubscribe-test")

# Generate R2 key upfront so view_url is known before upload
campaign_slug = "test"
email_id = uuid.uuid4().hex
r2_key = f"{campaign_slug}/{email_id}.html"
view_url = f"{R2_PUBLIC_BASE}/{r2_key}"

footer_rendered = footer_rendered.replace("{{view_url}}", view_url)

full_html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Step — Template Test</title>
</head>
<body style="margin:0;padding:0;background-color:#ffffff;">
{header_rendered}
{body}
{promo_rendered}
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
    subject="Step — Template Test",
    body=full_html,
    from_email="hello@step.is",
    to_email="lelong88@gmail.com",
    html=True,
)

if not result["success"]:
    raise SystemExit(f"Failed: {result['message']}")
