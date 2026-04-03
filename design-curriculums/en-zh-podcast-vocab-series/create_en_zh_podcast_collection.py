"""
Orchestrator: Create en-zh podcast collection and wire 4 podcast curriculums.

Creates a Collection titled "Learn Chinese Vocabulary Through Podcasts (通过播客学中文词汇)"
and adds 4 en-zh podcast curriculums directly to it (no series).
Sets display orders 0–3.

Requirements: 3.9
"""

import sys
import requests

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API_BASE = "https://helloapi.step.is"

COLLECTION_TITLE = "Learn Chinese Vocabulary Through Podcasts (通过播客学中文词汇)"

# en-zh podcast curriculum IDs in desired display order
CURRICULUM_IDS = [
    "UMXagwItTkqbLCtg",  # #0 陳永儀 — emotions
    "uoFdPLtAQumH1Kmg",  # #1 蔣勳 — slow living
    "co657nAhEzlPs1CB",  # #2 曾之喬 — work-life balance
    "Wdur6rGTWuxF1gpl",  # #3 莊祖宜 — food & sustainability
]


def main():
    token = get_firebase_id_token(UID)
    print(f"Got Firebase token for UID {UID}")

    # 1. Create collection
    print(f"\nCreating collection: {COLLECTION_TITLE}")
    resp = requests.post(f"{API_BASE}/curriculum-collection/create", json={
        "firebaseIdToken": token,
        "title": COLLECTION_TITLE,
    })
    resp.raise_for_status()
    collection_id = resp.json()["id"]
    print(f"Collection created: {collection_id}")

    # 2. Add each curriculum to the collection and set display order
    for i, cid in enumerate(CURRICULUM_IDS):
        print(f"\nAdding curriculum {cid} to collection (display order {i})...")

        add_resp = requests.post(f"{API_BASE}/curriculum-collection/addCurriculum", json={
            "firebaseIdToken": token,
            "curriculumCollectionId": collection_id,
            "curriculumId": cid,
        })
        add_resp.raise_for_status()
        print(f"  Added to collection.")

        order_resp = requests.post(f"{API_BASE}/curriculum/setDisplayOrder", json={
            "firebaseIdToken": token,
            "id": cid,
            "displayOrder": i,
        })
        order_resp.raise_for_status()
        print(f"  Display order set to {i}.")

    print(f"\nDone! Collection '{COLLECTION_TITLE}' ({collection_id}) has {len(CURRICULUM_IDS)} curriculums.")
    print(f"Collection ID: {collection_id}")


if __name__ == "__main__":
    main()
