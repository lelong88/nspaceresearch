#!/usr/bin/env python3
"""
Create the IELTS Academic Vocabulary series (vi-en, intermediate) and add it to
the "Học Từ Vựng Theo Chủ Đề" collection (279d6843).

Target: Vietnamese learners aiming for IELTS 4.5–5.5
Level: intermediate
Language pair: vi-en (bilingual)
Structure: 8 curriculums × 18 words = 144 words
Sessions: 5 per curriculum (3 learning + review + full reading)

Run this ONCE to create the empty series, then run individual curriculum scripts.
"""

import sys, requests

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

API = "https://helloapi.step.is"
UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
COLLECTION_ID = "279d6843"  # Học Từ Vựng Theo Chủ Đề

def api(endpoint, body={}):
    token = get_firebase_id_token(UID)
    body["firebaseIdToken"] = token
    r = requests.post(f"{API}/{endpoint}", json=body)
    r.raise_for_status()
    return r.json()

# Create the series
result = api("curriculum-series/create", {
    "title": "Luyện Thi IELTS: Từ Vựng Học Thuật",
    "description": "144 từ vựng học thuật qua 8 bài đọc phong cách IELTS Academic — nền tảng vững chắc cho band 4.5–5.5",
})
series_id = result["id"]
print(f"Created series: {series_id}")

# Make it public
api("curriculum-series/setIsPublic", {"id": series_id, "isPublic": True})
print("Set public")

# Add to collection
api("curriculum-collection/addSeriesToCollection", {
    "curriculumCollectionId": COLLECTION_ID,
    "curriculumSeriesId": series_id,
})
print(f"Added to collection {COLLECTION_ID}")

print(f"\nSERIES_ID = \"{series_id}\"")
print("Now create individual curriculums and add them to this series.")
