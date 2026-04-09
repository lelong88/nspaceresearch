"""
Utility to send emails via AWS SES SMTP.

Usage:
    # As a module
    from send_email import send_email
    send_email("Subject", "Body text", "from@example.com", "to@example.com")
    send_email("Subject", "<h1>HTML Body</h1>", "from@example.com", "to@example.com", html=True)

    # As a script
    python send_email.py from@example.com to@example.com "Test Subject" "Test body text"
    python send_email.py from@example.com to@example.com "Subject" "<h1>Hello</h1>" --html
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
def send_email(subject: str, body: str, from_email: str, to_email: str, html: bool = False) -> dict:
    """
    Send an email via AWS SES SMTP.

    Args:
        subject: Email subject line
        body: Email body (plain text or HTML)
        from_email: Sender email address
        to_email: Recipient email address
        html: If True, send body as HTML

    Returns:
        dict with 'success' bool and 'message' string
    """
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    content_type = "html" if html else "plain"
    msg.attach(MIMEText(body, content_type))

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(from_email, [to_email], msg.as_string())
        print(f"Email sent to {to_email}")
        return {"success": True, "message": f"Email sent to {to_email}"}
    except Exception as e:
        print(f"Failed to send email: {e}")
        return {"success": False, "message": str(e)}


if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python send_email.py <from> <to> <subject> <body> [--html]")
        sys.exit(1)

    from_addr = sys.argv[1]
    to_addr = sys.argv[2]
    subject = sys.argv[3]
    body = sys.argv[4]
    use_html = "--html" in sys.argv

    result = send_email(subject, body, from_email=from_addr, to_email=to_addr, html=use_html)
    sys.exit(0 if result["success"] else 1)
