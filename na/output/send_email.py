"""
Utility to send emails via AWS SES SMTP.

Usage:
    # As a module
    from output.send_email import send_email
    send_email("Subject", "Body text", to_email="someone@example.com")
    send_email("Subject", "<h1>HTML Body</h1>", html=True)

    # As a script
    python output/send_email.py "Test Subject" "Test body text"
    python output/send_email.py "Test Subject" "<h1>Hello</h1>" --html --to someone@example.com
"""

import smtplib
import os
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

SMTP_HOST = os.getenv("SES_SMTP_HOST", "email-smtp.us-west-2.amazonaws.com")
SMTP_PORT = int(os.getenv("SES_SMTP_PORT", "587"))
SMTP_USER = os.getenv("SES_SMTP_USER")
SMTP_PASSWORD = os.getenv("SES_SMTP_PASSWORD")
FROM_EMAIL = os.getenv("SES_FROM_EMAIL", "long@nspace.is")
DEFAULT_TO = os.getenv("SES_DEFAULT_TO_EMAIL", "phanthianhtien@gmail.com")


def send_email(subject: str, body: str, to_email: str = None, html: bool = False) -> dict:
    """
    Send an email via AWS SES SMTP.

    Args:
        subject: Email subject line
        body: Email body (plain text or HTML)
        to_email: Recipient email (defaults to phanthianhtien@gmail.com)
        html: If True, send body as HTML

    Returns:
        dict with 'success' bool and 'message' string
    """
    to_email = to_email or DEFAULT_TO

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = FROM_EMAIL
    msg["To"] = to_email

    content_type = "html" if html else "plain"
    msg.attach(MIMEText(body, content_type))

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(FROM_EMAIL, [to_email], msg.as_string())
        print(f"Email sent to {to_email}")
        return {"success": True, "message": f"Email sent to {to_email}"}
    except Exception as e:
        print(f"Failed to send email: {e}")
        return {"success": False, "message": str(e)}


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python output/send_email.py <subject> <body> [--html] [--to email@example.com]")
        sys.exit(1)

    subject = sys.argv[1]
    body = sys.argv[2]
    use_html = "--html" in sys.argv
    to = None
    if "--to" in sys.argv:
        to = sys.argv[sys.argv.index("--to") + 1]

    result = send_email(subject, body, to_email=to, html=use_html)
    sys.exit(0 if result["success"] else 1)
