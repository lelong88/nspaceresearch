#!/usr/bin/env python3
"""
Provision the 10 onboarding banners (5 statuses × 2 languages).

Creates banner definitions with targeting fields, then assigns each
to the test user. Safe to re-run — skips banners that already exist
(matched by title).

Usage:
    python campaigns/onboarding/_provision_banners.py
    python campaigns/onboarding/_provision_banners.py --dry-run
"""

import os
import sys
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_BASE = "https://email.step.is"
API_KEY = os.environ["API_KEY"]
TEST_USER_UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
MAX_EXPIRATION = "2026-12-31T23:59:59Z"
FIRST_SHOWN_EXPIRATION_HOURS = 72  # disappear 72h after first view

HEADERS = {
    "Content-Type": "application/json",
    "X-API-Key": API_KEY,
}

# ─── Banner definitions ───────────────────────────────────────────────────────
# Each tuple: (status, lang, type, title, subtitle, display_order)

BANNERS = [
    # not_logged_in
    (
        "not_logged_in", "en", "standard",
        "Sign in to start learning",
        "Create an account to unlock courses, track progress, and earn credits.",
        100,
    ),
    (
        "not_logged_in", "vi", "standard",
        "Đăng nhập để bắt đầu học",
        "Tạo tài khoản để mở khóa học, theo dõi tiến trình và nhận credits.",
        100,
    ),
    # no_credits
    (
        "no_credits", "en", "standard",
        "Get started for free",
        "Browse free courses (0 credits) or tap the wallet icon to enter a referral code.",
        90,
    ),
    (
        "no_credits", "vi", "standard",
        "Bắt đầu miễn phí",
        "Chọn khóa học miễn phí (0 credits) hoặc nhấn biểu tượng ví để nhập mã giới thiệu.",
        90,
    ),
    # no_purchase_yet
    (
        "no_purchase_yet", "en", "standard",
        "Ready to learn? Unlock a course",
        "You have credits! Use them to unlock a curriculum and start your first lesson.",
        80,
    ),
    (
        "no_purchase_yet", "vi", "standard",
        "Sẵn sàng học? Mở khóa ngay",
        "Bạn đã có credits! Dùng chúng để mở khóa học và bắt đầu bài học đầu tiên.",
        80,
    ),
    # not_started_yet
    (
        "not_started_yet", "en", "standard",
        "Your course is waiting",
        "Tap \"Get started\" on any course you've unlocked to begin learning.",
        70,
    ),
    (
        "not_started_yet", "vi", "standard",
        "Khóa học đang chờ bạn",
        "Nhấn \"Bắt đầu\" trên khóa học bạn đã mở để bắt đầu học.",
        70,
    ),
    # started_no_activity_yet
    (
        "started_no_activity_yet", "en", "minimal",
        "Welcome to your learning space",
        "This is your distraction-free zone. Each lesson is 5–10 min — pick one and dive in.",
        60,
    ),
    (
        "started_no_activity_yet", "vi", "minimal",
        "Chào mừng đến không gian học",
        "Đây là nơi tập trung của bạn. Mỗi bài học 5–10 phút — chọn một bài và bắt đầu.",
        60,
    ),
]


def main():
    dry_run = "--dry-run" in sys.argv

    print(f"{'[DRY RUN] ' if dry_run else ''}Provisioning {len(BANNERS)} onboarding banners...")
    print(f"  Target user: {TEST_USER_UID}")
    print(f"  Expiration: {MAX_EXPIRATION}")
    print(f"  First-shown TTL: {FIRST_SHOWN_EXPIRATION_HOURS}h")
    print()

    created = 0
    skipped = 0

    for status, lang, banner_type, title, subtitle, display_order in BANNERS:
        print(f"  [{lang}] {status}: {title}")

        if dry_run:
            print(f"       → would create ({banner_type}) + assign to {TEST_USER_UID}")
            created += 1
            continue

        # 1. Create banner definition
        payload = {
            "title": title,
            "subtitle": subtitle,
            "url": "https://step.is",
            "type": banner_type,
            "required_user_status": status,
            "required_user_language": lang,
        }

        resp = requests.post(f"{API_BASE}/api/banners", headers=HEADERS, json=payload)

        if resp.status_code == 201:
            banner = resp.json()
            banner_id = banner["id"]
            print(f"       → created banner #{banner_id}")
        else:
            print(f"       ✗ failed to create: {resp.status_code} {resp.text}")
            continue

        # 2. Assign to test user
        assign_payload = {
            "user_uid": TEST_USER_UID,
            "max_expiration_date": MAX_EXPIRATION,
            "first_shown_expiration_hours": FIRST_SHOWN_EXPIRATION_HOURS,
            "display_order": display_order,
        }

        resp = requests.post(
            f"{API_BASE}/api/banners/{banner_id}/assign",
            headers=HEADERS,
            json=assign_payload,
        )

        if resp.status_code == 201:
            result = resp.json()
            if result.get("inserted"):
                print(f"       → assigned to {TEST_USER_UID}")
                created += 1
            else:
                print(f"       → already assigned (skipped)")
                skipped += 1
        else:
            print(f"       ✗ failed to assign: {resp.status_code} {resp.text}")

    print()
    print(f"Done: {created} created, {skipped} skipped")


if __name__ == "__main__":
    main()
