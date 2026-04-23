"""
Reusable campaign email renderer and sender.

Handles: template loading, locale resolution, R2 upload ("View in browser"), and SES sending.

Usage:
    from campaign_email import render_email, upload_to_r2, send_campaign_email

    # Render only
    html = render_email("my-campaign", lang="vi", variables={"promo_code": "HELLO"})

    # Render + upload + send
    send_campaign_email(
        campaign_slug="my-campaign",
        lang="vi",
        subject="Hello!",
        to_email="user@example.com",
        variables={"promo_code": "HELLO"},
    )
"""

import os
import uuid
import boto3
from dotenv import load_dotenv
from send_email import send_email

load_dotenv()

# ── Constants ────────────────────────────────────────────────

CAMPAIGNS_DIR = "campaigns"
FROM_EMAIL = "support@step.is"

R2_BUCKET = "emails"
R2_PUBLIC_BASE = "https://emails.step.is"

TAGLINES = {
    "en": "Language courses built around content you'd actually enjoy",
    "vi": "Khóa học ngôn ngữ từ nội dung bạn thực sự thích",
}

WEBSITE_URLS = {
    "en": "https://step.is",
    "vi": "https://step.is/vi",
}

# ── R2 client (lazy init) ────────────────────────────────────

_s3 = None

def _get_s3():
    global _s3
    if _s3 is None:
        _s3 = boto3.client(
            "s3",
            endpoint_url=os.getenv("R2_ENDPOINT_URL"),
            aws_access_key_id=os.getenv("R2_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("R2_SECRET_ACCESS_KEY"),
            region_name="auto",
        )
    return _s3


# ── Template loading ─────────────────────────────────────────

def _read(path: str) -> str:
    with open(path) as f:
        return f.read()


def _load_templates(campaign_slug: str) -> tuple[str, str, str]:
    """Load header, campaign body, and footer templates."""
    header = _read(f"{CAMPAIGNS_DIR}/header.html")
    body = _read(f"{CAMPAIGNS_DIR}/{campaign_slug}/body.html")
    footer = _read(f"{CAMPAIGNS_DIR}/footer.html")
    return header, body, footer


# ── Rendering ────────────────────────────────────────────────

def render_email(
    campaign_slug: str,
    lang: str = "en",
    variables: dict[str, str] | None = None,
    unsubscribe_url: str = "#",
    view_url: str = "#",
) -> str:
    """
    Render a full email HTML from campaign templates.

    Args:
        campaign_slug: directory name under campaigns/
        lang: "en" or "vi" — controls tagline and website_url
        variables: extra {{key}} → value replacements for the body
        unsubscribe_url: per-recipient unsubscribe link
        view_url: public R2 link to this email

    Returns:
        Complete HTML string ready to send.
    """
    header, body, footer = _load_templates(campaign_slug)

    # Locale variables
    tagline = TAGLINES.get(lang, TAGLINES["en"])
    website_url = WEBSITE_URLS.get(lang, WEBSITE_URLS["en"])

    header = header.replace("{{tagline}}", tagline)
    body = body.replace("{{website_url}}", website_url)
    footer = (
        footer
        .replace("{{unsubscribe_url}}", unsubscribe_url)
        .replace("{{view_url}}", view_url)
    )

    # Custom variables
    if variables:
        for key, value in variables.items():
            placeholder = "{{" + key + "}}"
            body = body.replace(placeholder, value)

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin:0;padding:0;background-color:#ffffff;">
{header}
{body}
{footer}
</body>
</html>"""


# ── R2 upload ────────────────────────────────────────────────

def upload_to_r2(html: str, campaign_slug: str) -> str:
    """
    Upload rendered email HTML to R2 and return the public URL.

    The key is {campaign_slug}/{uuid}.html — unlisted but publicly accessible.
    """
    email_id = uuid.uuid4().hex
    key = f"{campaign_slug}/{email_id}.html"
    _get_s3().put_object(
        Bucket=R2_BUCKET,
        Key=key,
        Body=html.encode("utf-8"),
        ContentType="text/html; charset=utf-8",
    )
    return f"{R2_PUBLIC_BASE}/{key}"


# ── Send ─────────────────────────────────────────────────────

def send_campaign_email(
    campaign_slug: str,
    subject: str,
    to_email: str,
    lang: str = "en",
    variables: dict[str, str] | None = None,
    from_email: str = FROM_EMAIL,
    unsubscribe_url: str = "#",
) -> dict:
    """
    Render, upload to R2, and send a campaign email.

    The "View in browser" link is automatically set to the R2 URL.

    Returns:
        dict with 'success', 'message', and 'view_url' keys.
    """
    # First render with placeholder view_url to get the HTML structure
    # Then upload to get the real URL, re-render, and re-upload
    email_id = uuid.uuid4().hex
    key = f"{campaign_slug}/{email_id}.html"
    view_url = f"{R2_PUBLIC_BASE}/{key}"

    html = render_email(
        campaign_slug=campaign_slug,
        lang=lang,
        variables=variables,
        unsubscribe_url=unsubscribe_url,
        view_url=view_url,
    )

    # Upload to R2
    _get_s3().put_object(
        Bucket=R2_BUCKET,
        Key=key,
        Body=html.encode("utf-8"),
        ContentType="text/html; charset=utf-8",
    )

    # Send via SES
    result = send_email(
        subject=subject,
        body=html,
        from_email=from_email,
        to_email=to_email,
        html=True,
    )

    return {**result, "view_url": view_url}
