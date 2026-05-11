"""Email the March 2026 VaR deep-dive report to the default recipient."""
import sys
from pathlib import Path

import markdown as md

# allow importing output/send_email.py
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from send_email import send_email  # noqa: E402

REPORT = Path(__file__).with_name("march-2026-var-deepdive.md")
md_text = REPORT.read_text(encoding="utf-8")

html_body = md.markdown(md_text, extensions=["tables", "fenced_code"])

# Light styling so tables render cleanly in mail clients
html = f"""<!doctype html>
<html><head><meta charset="utf-8">
<style>
  body {{ font-family: -apple-system, Segoe UI, Helvetica, Arial, sans-serif;
          font-size: 14px; color: #222; max-width: 920px; margin: 16px auto; padding: 0 12px; }}
  h1 {{ font-size: 22px; border-bottom: 2px solid #444; padding-bottom: 4px; }}
  h2 {{ font-size: 18px; margin-top: 28px; border-bottom: 1px solid #bbb; padding-bottom: 3px; }}
  h3 {{ font-size: 15px; margin-top: 20px; }}
  table {{ border-collapse: collapse; margin: 10px 0; font-size: 13px; }}
  th, td {{ border: 1px solid #ccc; padding: 6px 10px; text-align: left; }}
  th {{ background: #f0f3f7; }}
  td:has(+ td:nth-child(n)) {{ }}
  tr td:nth-child(n+2) {{ text-align: right; }}
  code {{ background: #f4f4f4; padding: 1px 4px; border-radius: 3px; }}
  blockquote {{ border-left: 3px solid #888; margin: 8px 0; padding: 4px 12px; color: #444; background:#fafafa; }}
</style></head>
<body>
{html_body}
</body></html>"""

subject = "VaR Deep-Dive — March 2026 (ILP26 launch month)"
result = send_email(subject, html, html=True)
sys.exit(0 if result["success"] else 1)
