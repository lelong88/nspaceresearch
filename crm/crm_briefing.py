#!/usr/bin/env python3
"""Daily CRM briefing: reads R2 bucket `crm`, generates briefing via LiteLLM, emails it."""

import json
import os
import sys
import urllib.request
from datetime import datetime

import boto3
from dotenv import load_dotenv

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(SCRIPT_DIR, ".env"))

sys.path.insert(0, SCRIPT_DIR)
from send_email import send_email

R2_BUCKET = "crm"
R2_ENDPOINT = os.getenv("R2_ENDPOINT", "https://8d8fff2b8b2d4f0328c8f0b438de5425.r2.cloudflarestorage.com")
R2_ACCESS_KEY = os.getenv("R2_ACCESS_KEY")
R2_SECRET_KEY = os.getenv("R2_SECRET_KEY")
LLM_BASE_URL = os.getenv("LLM_BASE_URL", "https://litellm.meomap.blog")
LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL", "kimi")
FROM_EMAIL = "support@nspace.is"
TO_EMAIL = "long@nspace.is"


def read_crm_data():
    r2 = boto3.client("s3", endpoint_url=R2_ENDPOINT, aws_access_key_id=R2_ACCESS_KEY,
                       aws_secret_access_key=R2_SECRET_KEY, region_name="auto")
    objects = r2.list_objects_v2(Bucket=R2_BUCKET).get("Contents", [])
    entries = []
    for obj in objects:
        body = r2.get_object(Bucket=R2_BUCKET, Key=obj["Key"])["Body"].read().decode()
        entries.append(f"--- {obj['Key']} ---\n{body}")
    return "\n\n".join(entries)


def load_system_prompt():
    with open(os.path.join(SCRIPT_DIR, "system_prompt.md")) as f:
        return f.read()


def generate_briefing(system_prompt, crm_data):
    today = datetime.now().strftime("%A, %Y-%m-%d")
    payload = json.dumps({
        "model": LLM_MODEL,
        "max_tokens": 2048,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Today is {today}.\n\nCRM Data:\n\n{crm_data}"},
        ],
    }).encode()
    req = urllib.request.Request(
        f"{LLM_BASE_URL}/v1/chat/completions",
        data=payload,
        headers={"Authorization": f"Bearer {LLM_API_KEY}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        result = json.loads(resp.read())
    return result["choices"][0]["message"]["content"]


def main():
    crm_data = read_crm_data()
    if not crm_data.strip():
        print("No CRM data found. Skipping briefing.")
        return
    briefing = generate_briefing(load_system_prompt(), crm_data)
    subject = f"CRM Daily Briefing — {datetime.now().strftime('%A %b %d')}"
    result = send_email(subject, briefing, FROM_EMAIL, TO_EMAIL)
    if not result["success"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
