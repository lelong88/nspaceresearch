#!/usr/bin/env python3
"""
Update display_order column for all chapters in The Last Light of Alder House series
using the curriculum/setDisplayOrder endpoint.
"""
import sys, os, time, requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../..")
from firebase_token import get_firebase_id_token

API_BASE = "https://helloapi.step.is/curriculum"
UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"

CHAPTERS = [
    (1, "Qyh5uCNh47p2iDHl"),
    (2, "DLTIxoUd9wLgBzGm"),
    (3, "cww91BaiQsrQ4riz"),
    (4, "xY7ghNoIwXxQvB4Z"),
    (5, "VuixQt9nJIvhnFFX"),
    (6, "NIsuxRyoHIervuxZ"),
    (7, "ox5rW3r3R6UAlK8g"),
    (8, "8gvrHLAoVB0yFL7Y"),
    (9, "fkneO8n7qDydxXNf"),
    (10, "WBMT46gTnRWVUN97"),
    (11, "QfpgaSFOy4lnIDJN"),
    (12, "tVEmrVFJJhe2KQny"),
    (13, "wg1GOnVg6FkypqxF"),
    (14, "EaIVeq2HXLVQPaay"),
    (15, "ze2sDVM3dWsucZ2D"),
    (16, "o11aeKeiMSWq1QFQ"),
    (17, "4M8Oe56MdU62taUj"),
    (18, "CVXRWgaxq6eT2uOX"),
    (19, "euFxTmz1t3IvAXix"),
    (20, "tYMoMfLM6PrRgSVv"),
]


def main():
    print(f"Updating display_order for {len(CHAPTERS)} chapters...\n")
    ok, fail = 0, 0

    for chapter_num, cid in CHAPTERS:
        print(f"  Chapter {chapter_num} ({cid})...", end=" ", flush=True)
        try:
            token = get_firebase_id_token(UID)
            r = requests.post(
                f"{API_BASE}/setDisplayOrder",
                json={"id": cid, "uid": UID, "displayOrder": chapter_num, "firebaseIdToken": token},
            )
            r.raise_for_status()
            print("✓")
            ok += 1
        except Exception as e:
            print(f"✗ {e}")
            fail += 1
        time.sleep(0.3)

    print(f"\nDone: {ok} updated, {fail} failed.")


if __name__ == "__main__":
    main()
