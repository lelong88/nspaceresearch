"""Email the March 2026 VaR deep-dive PPTX to the default recipient as an attachment."""
import os
import smtplib
import sys
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

SMTP_HOST = os.getenv("SES_SMTP_HOST", "email-smtp.us-west-2.amazonaws.com")
SMTP_PORT = int(os.getenv("SES_SMTP_PORT", "587"))
SMTP_USER = os.getenv("SES_SMTP_USER")
SMTP_PASSWORD = os.getenv("SES_SMTP_PASSWORD")
FROM_EMAIL = os.getenv("SES_FROM_EMAIL", "long@nspace.is")
DEFAULT_TO = os.getenv("SES_DEFAULT_TO_EMAIL", "phanthianhtien@gmail.com")

PPTX = Path(__file__).with_name("march-2026-var-deepdive.pptx")
to_email = DEFAULT_TO

msg = MIMEMultipart()
msg["Subject"] = "VaR Deep-Dive — March 2026 (PPTX)"
msg["From"] = FROM_EMAIL
msg["To"] = to_email

body = """Hi,

Resending the March 2026 VaR deep-dive in PowerPoint format. 13 slides:

  1.  Title
  2.  Why a March-only deep-dive
  3.  Methodology (March-only VaR, payout coverage)
  4.  12-month trend — March sits within normal range
  5.  Population view — VaR bucket distribution (505 units)
  6.  Population — GTF / MBA Pro tier / P13 persistency
  7.  Deep-dive headline — Note column (calc gap vs. delay payment)
  8.  By Rank (col D)
  9.  By MBA Pro tier (col E)
 10.  By GTF (col F / H)
 11.  Cross-tabs — Rank × MBA Pro and Rank × GTF
 12.  Note × Rank cross-tab
 13.  Conclusions for Regional Office

Source data: slides/var-8th-draft (OCR'd).

Thanks,
Compensation & Risk team
"""
msg.attach(MIMEText(body, "plain"))

with open(PPTX, "rb") as fh:
    part = MIMEBase("application", "vnd.openxmlformats-officedocument.presentationml.presentation")
    part.set_payload(fh.read())
encoders.encode_base64(part)
part.add_header("Content-Disposition", f'attachment; filename="{PPTX.name}"')
msg.attach(part)

with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(SMTP_USER, SMTP_PASSWORD)
    server.sendmail(FROM_EMAIL, [to_email], msg.as_string())

print(f"Email sent to {to_email} with attachment {PPTX.name} ({PPTX.stat().st_size:,} bytes)")
