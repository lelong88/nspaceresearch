"""
Upload all 10 chapters of "The Garden of Forgotten Letters" to the platform,
create the series, attach to Fiction collection, and set public.

Usage:
    cd original-novels/the-garden-of-forgotten-letters
    python create_all_chapters.py
"""

import sys
import requests
import importlib

# --- Auth setup ---
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API_BASE = "https://helloapi.step.is"

SERIES_TITLE = "Khu Vườn Những Lá Thư Bị Lãng Quên (The Garden of Forgotten Letters)"
FICTION_COLLECTION_KEYWORDS = ["Truyện", "Fiction"]
NUM_CHAPTERS = 10


def authenticate():
    print("Authenticating...")
    try:
        token = get_firebase_id_token(UID)
        print("  Authentication successful.")
        return token
    except Exception as e:
        print(f"  FATAL: Authentication failed: {e}")
        sys.exit(1)


def load_chapter_modules():
    modules = []
    for i in range(1, NUM_CHAPTERS + 1):
        module_name = f"chapter{i}_content"
        try:
            mod = importlib.import_module(module_name)
            curriculum = mod.get_curriculum()
            modules.append(curriculum)
            print(f"  Loaded {module_name}")
        except Exception as e:
            print(f"  FATAL: Failed to load {module_name}: {e}")
            sys.exit(1)
    return modules


def upload_curriculum(token, curriculum_dict, chapter_num):
    title = curriculum_dict.get("title", f"Chapter {chapter_num}")
    print(f"  Uploading chapter {chapter_num}: {title[:60]}...")
    resp = requests.post(f"{API_BASE}/curriculum/create", json={
        "firebaseIdToken": token,
        "content": curriculum_dict,
    })
    if resp.status_code != 200 and resp.status_code != 201:
        print(f"  FATAL: Upload failed for chapter {chapter_num}.")
        print(f"  Status: {resp.status_code}")
        try:
            print(f"  Response: {resp.json()}")
        except Exception:
            print(f"  Response text: {resp.text}")
        sys.exit(1)
    data = resp.json()
    curriculum_id = data.get("id") or data.get("curriculumId")
    if not curriculum_id:
        print(f"  FATAL: No ID returned for chapter {chapter_num}. Response: {data}")
        sys.exit(1)
    print(f"    -> ID: {curriculum_id}")
    return curriculum_id


def upload_all_chapters(token, chapter_dicts):
    print("\n--- Uploading chapters ---")
    uploaded = []
    for i, curriculum_dict in enumerate(chapter_dicts):
        chapter_num = i + 1
        cid = upload_curriculum(token, curriculum_dict, chapter_num)
        uploaded.append((chapter_num, cid))
    print(f"\nAll {len(uploaded)} chapters uploaded successfully.")
    return uploaded


def create_series(token):
    print("\n--- Creating series ---")
    resp = requests.post(f"{API_BASE}/curriculum-series/create", json={
        "firebaseIdToken": token,
        "title": SERIES_TITLE,
        "language": "en",
        "userLanguage": "vi",
    })
    if resp.status_code != 200 and resp.status_code != 201:
        print(f"  FATAL: Series creation failed. Status: {resp.status_code}")
        try:
            print(f"  Response: {resp.json()}")
        except Exception:
            print(f"  Response text: {resp.text}")
        return None
    data = resp.json()
    series_id = data.get("id") or data.get("curriculumSeriesId")
    if not series_id:
        print(f"  FATAL: No series ID returned. Response: {data}")
        return None
    print(f"  Series created: {SERIES_TITLE}")
    print(f"    -> ID: {series_id}")
    return series_id


def add_chapters_to_series(token, series_id, uploaded_chapters):
    print("\n--- Adding chapters to series ---")
    for chapter_num, curriculum_id in uploaded_chapters:
        resp = requests.post(f"{API_BASE}/curriculum-series/addCurriculum", json={
            "firebaseIdToken": token,
            "curriculumSeriesId": series_id,
            "curriculumId": curriculum_id,
            "displayOrder": chapter_num,
        })
        if resp.status_code != 200 and resp.status_code != 201:
            print(f"  ERROR: Failed to add chapter {chapter_num} (ID: {curriculum_id}) to series.")
            try:
                print(f"  Response: {resp.json()}")
            except Exception:
                print(f"  Response text: {resp.text}")
            _report_uploaded_ids(uploaded_chapters)
            sys.exit(1)
        print(f"  Added chapter {chapter_num} (display_order={chapter_num})")
    print("  All chapters added to series.")


def find_fiction_collection(token):
    print("\n--- Looking up Fiction collection ---")
    resp = requests.post(f"{API_BASE}/curriculum-collection/listAll", json={
        "firebaseIdToken": token,
    })
    if resp.status_code != 200:
        print(f"  FATAL: Failed to list collections. Status: {resp.status_code}")
        try:
            print(f"  Response: {resp.json()}")
        except Exception:
            print(f"  Response text: {resp.text}")
        return None
    collections = resp.json()
    if not isinstance(collections, list):
        collections = collections.get("data", collections.get("collections", []))
    for coll in collections:
        title = coll.get("title", "")
        for keyword in FICTION_COLLECTION_KEYWORDS:
            if keyword.lower() in title.lower():
                coll_id = coll.get("id") or coll.get("curriculumCollectionId")
                print(f"  Found Fiction collection: \"{title}\" -> ID: {coll_id}")
                return coll_id
    print("  FATAL: Could not find Fiction collection by title.")
    print("  Available collections:")
    for coll in collections:
        print(f"    - \"{coll.get('title', '?')}\" (ID: {coll.get('id', '?')})")
    return None


def attach_series_to_collection(token, series_id, collection_id):
    print("\n--- Attaching series to Fiction collection ---")
    resp = requests.post(f"{API_BASE}/curriculum-collection/addSeriesToCollection", json={
        "firebaseIdToken": token,
        "curriculumCollectionId": collection_id,
        "curriculumSeriesId": series_id,
    })
    if resp.status_code != 200 and resp.status_code != 201:
        print(f"  ERROR: Failed to attach series to collection.")
        try:
            print(f"  Response: {resp.json()}")
        except Exception:
            print(f"  Response text: {resp.text}")
        return False
    print(f"  Series {series_id} attached to collection {collection_id}.")
    return True


def set_series_public(token, series_id):
    print("\n--- Setting series to public ---")
    resp = requests.post(f"{API_BASE}/curriculum-series/setIsPublic", json={
        "firebaseIdToken": token,
        "curriculumSeriesId": series_id,
        "isPublic": True,
    })
    if resp.status_code != 200 and resp.status_code != 201:
        print(f"  ERROR: Failed to set series public.")
        try:
            print(f"  Response: {resp.json()}")
        except Exception:
            print(f"  Response text: {resp.text}")
        return False
    print(f"  Series {series_id} is now public.")
    return True


def _report_uploaded_ids(uploaded_chapters):
    print("\n  === Already-uploaded curriculum IDs (for manual cleanup) ===")
    for chapter_num, curriculum_id in uploaded_chapters:
        print(f"    Chapter {chapter_num}: {curriculum_id}")
    print("  ===========================================================")


def main():
    token = authenticate()
    print("\n--- Loading chapter content modules ---")
    chapter_dicts = load_chapter_modules()
    uploaded_chapters = upload_all_chapters(token, chapter_dicts)
    series_id = create_series(token)
    if not series_id:
        _report_uploaded_ids(uploaded_chapters)
        sys.exit(1)
    add_chapters_to_series(token, series_id, uploaded_chapters)
    collection_id = find_fiction_collection(token)
    if not collection_id:
        _report_uploaded_ids(uploaded_chapters)
        print(f"  Series ID: {series_id}")
        sys.exit(1)
    if not attach_series_to_collection(token, series_id, collection_id):
        _report_uploaded_ids(uploaded_chapters)
        print(f"  Series ID: {series_id}")
        sys.exit(1)
    if not set_series_public(token, series_id):
        print("  WARNING: Series created and attached but not set to public.")
        print(f"  Series ID: {series_id}")
    print("\n" + "=" * 60)
    print("SUCCESS!")
    print(f"  Series: {SERIES_TITLE}")
    print(f"  Series ID: {series_id}")
    print(f"  Collection ID: {collection_id}")
    print(f"  Chapters uploaded: {len(uploaded_chapters)}")
    for chapter_num, curriculum_id in uploaded_chapters:
        print(f"    Chapter {chapter_num}: {curriculum_id}")
    print("=" * 60)


if __name__ == "__main__":
    main()
