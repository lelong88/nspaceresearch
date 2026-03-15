"""
Upload all 10 chapters of "Bức Tranh Biến Mất (消失的画)" to the platform,
create the series, attach to existing Fiction collection (7nf5wi1d), and set display orders.

Usage:
    cd original-novels/vi-zh-mystery-novel
    python create_all_chapters.py
"""

import sys
import json
import requests
import importlib

# --- Auth setup ---
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API_BASE = "https://helloapi.step.is"

SERIES_TITLE = "Bức Tranh Biến Mất (消失的画)"
SERIES_DESCRIPTION = (
    "Một câu chuyện bí ẩn hấp dẫn về bức tranh nổi tiếng biến mất khỏi phòng tranh "
    "của một thị trấn nhỏ ở Trung Quốc. Theo chân Linh — cô gái Việt Nam tham gia "
    "chương trình nghệ thuật mùa hè — cùng bạn bè điều tra vụ mất tranh, khám phá "
    "bí mật ẩn giấu và tìm ra sự thật bất ngờ. 10 chương truyện với 150 từ vựng "
    "HSK2-3 quen thuộc, giúp bạn luyện đọc tiếng Trung qua ngữ cảnh tự nhiên."
)
COLLECTION_ID = "7nf5wi1d"  # Existing "Truyện (小说)" collection
NUM_CHAPTERS = 10


def authenticate():
    """Get Firebase ID token. Abort on failure."""
    print("Authenticating...")
    try:
        token = get_firebase_id_token(UID)
        print("  Authentication successful.")
        return token
    except Exception as e:
        print(f"  FATAL: Authentication failed: {e}")
        sys.exit(1)


def load_chapter_modules():
    """Import all 10 chapter content modules and return their curriculum dicts."""
    modules = []
    for i in range(1, NUM_CHAPTERS + 1):
        module_name = f"chapter{i}_content"
        try:
            mod = importlib.import_module(module_name)
            curriculum = mod.get_content()
            modules.append(curriculum)
            print(f"  Loaded {module_name}")
        except Exception as e:
            print(f"  FATAL: Failed to load {module_name}: {e}")
            sys.exit(1)
    return modules


def upload_curriculum(token, curriculum_dict, chapter_num):
    """Upload a single curriculum via curriculum/create. Returns the curriculum ID."""
    title = curriculum_dict.get("title", f"Chapter {chapter_num}")
    print(f"  Uploading chapter {chapter_num}: {title[:60]}...")
    resp = requests.post(f"{API_BASE}/curriculum/create", json={
        "firebaseIdToken": token,
        "uid": UID,
        "language": "zh",
        "userLanguage": "vi",
        "content": json.dumps(curriculum_dict),
    })
    if resp.status_code not in (200, 201):
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
    """Upload all 10 chapters. Returns list of (chapter_num, curriculum_id)."""
    print("\n--- Uploading chapters ---")
    uploaded = []
    for i, curriculum_dict in enumerate(chapter_dicts):
        chapter_num = i + 1
        cid = upload_curriculum(token, curriculum_dict, chapter_num)
        uploaded.append((chapter_num, cid))
    print(f"\nAll {len(uploaded)} chapters uploaded successfully.")
    return uploaded


def create_series(token):
    """Create the curriculum series. Returns the series ID."""
    print("\n--- Creating series ---")
    resp = requests.post(f"{API_BASE}/curriculum-series/create", json={
        "firebaseIdToken": token,
        "title": SERIES_TITLE,
        "description": SERIES_DESCRIPTION,
        "language": "zh",
        "userLanguage": "vi",
        "isPublic": True,
    })
    if resp.status_code not in (200, 201):
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
    """Add each curriculum to the series."""
    print("\n--- Adding chapters to series ---")
    for chapter_num, curriculum_id in uploaded_chapters:
        resp = requests.post(f"{API_BASE}/curriculum-series/addCurriculum", json={
            "firebaseIdToken": token,
            "curriculumSeriesId": series_id,
            "curriculumId": curriculum_id,
        })
        if resp.status_code not in (200, 201):
            print(f"  ERROR: Failed to add chapter {chapter_num} (ID: {curriculum_id}) to series.")
            try:
                print(f"  Response: {resp.json()}")
            except Exception:
                print(f"  Response text: {resp.text}")
            _report_uploaded_ids(uploaded_chapters)
            sys.exit(1)
        print(f"  Added chapter {chapter_num}")
    print("  All chapters added to series.")


def check_collection_accessible(token):
    """Verify that existing collection 7nf5wi1d is accessible via listAll. Returns True/False."""
    print("\n--- Checking existing collection accessibility ---")
    resp = requests.post(f"{API_BASE}/curriculum-collection/listAll", json={
        "firebaseIdToken": token,
    })
    if resp.status_code != 200:
        print(f"  FATAL: Failed to list collections. Status: {resp.status_code}")
        try:
            print(f"  Response: {resp.json()}")
        except Exception:
            print(f"  Response text: {resp.text}")
        return False

    collections = resp.json()
    if not isinstance(collections, list):
        collections = collections.get("data", collections.get("collections", []))

    for coll in collections:
        coll_id = coll.get("id") or coll.get("curriculumCollectionId")
        if coll_id == COLLECTION_ID:
            title = coll.get("title", "?")
            print(f"  Found collection: \"{title}\" -> ID: {coll_id}")
            return True

    print(f"  FATAL: Collection {COLLECTION_ID} not found in listAll response.")
    print("  Available collections:")
    for coll in collections:
        cid = coll.get("id") or coll.get("curriculumCollectionId", "?")
        print(f"    - \"{coll.get('title', '?')}\" (ID: {cid})")
    return False


def attach_series_to_collection(token, series_id):
    """Attach the series to the existing Fiction collection."""
    print("\n--- Attaching series to existing collection ---")
    resp = requests.post(f"{API_BASE}/curriculum-collection/addSeriesToCollection", json={
        "firebaseIdToken": token,
        "curriculumCollectionId": COLLECTION_ID,
        "curriculumSeriesId": series_id,
    })
    if resp.status_code not in (200, 201):
        print(f"  ERROR: Failed to attach series to collection {COLLECTION_ID}.")
        try:
            print(f"  Response: {resp.json()}")
        except Exception:
            print(f"  Response text: {resp.text}")
        return False
    print(f"  Series {series_id} attached to collection {COLLECTION_ID}.")
    return True


def set_display_orders(token, uploaded_chapters):
    """Set display orders 1-10 for each curriculum."""
    print("\n--- Setting display orders ---")
    for chapter_num, curriculum_id in uploaded_chapters:
        resp = requests.post(f"{API_BASE}/curriculum/setDisplayOrder", json={
            "firebaseIdToken": token,
            "curriculumId": curriculum_id,
            "displayOrder": chapter_num,
        })
        if resp.status_code not in (200, 201):
            print(f"  ERROR: Failed to set display order for chapter {chapter_num} (ID: {curriculum_id}).")
            try:
                print(f"  Response: {resp.json()}")
            except Exception:
                print(f"  Response text: {resp.text}")
            return False
        print(f"  Chapter {chapter_num} -> displayOrder={chapter_num}")
    print("  All display orders set.")
    return True


def _report_uploaded_ids(uploaded_chapters):
    """Print already-uploaded curriculum IDs for manual cleanup."""
    print("\n  === Already-uploaded curriculum IDs (for manual cleanup) ===")
    for chapter_num, curriculum_id in uploaded_chapters:
        print(f"    Chapter {chapter_num}: {curriculum_id}")
    print("  ===========================================================")


def main():
    # 1. Authenticate
    token = authenticate()

    # 2. Load all chapter content modules
    print("\n--- Loading chapter content modules ---")
    chapter_dicts = load_chapter_modules()

    # 3. Upload all 10 chapters
    uploaded_chapters = upload_all_chapters(token, chapter_dicts)

    # 4. Create series
    series_id = create_series(token)
    if not series_id:
        _report_uploaded_ids(uploaded_chapters)
        sys.exit(1)

    # 5. Add each curriculum to the series
    add_chapters_to_series(token, series_id, uploaded_chapters)

    # 6. Check that existing collection is accessible
    if not check_collection_accessible(token):
        _report_uploaded_ids(uploaded_chapters)
        print(f"  Series ID: {series_id}")
        sys.exit(1)

    # 7. Attach series to existing collection
    if not attach_series_to_collection(token, series_id):
        _report_uploaded_ids(uploaded_chapters)
        print(f"  Series ID: {series_id}")
        sys.exit(1)

    # 8. Set display orders 1-10
    if not set_display_orders(token, uploaded_chapters):
        _report_uploaded_ids(uploaded_chapters)
        print(f"  Series ID: {series_id}")
        sys.exit(1)

    # Done
    print("\n" + "=" * 60)
    print("SUCCESS!")
    print(f"  Series: {SERIES_TITLE}")
    print(f"  Series ID: {series_id}")
    print(f"  Collection ID: {COLLECTION_ID}")
    print(f"  Chapters uploaded: {len(uploaded_chapters)}")
    for chapter_num, curriculum_id in uploaded_chapters:
        print(f"    Chapter {chapter_num}: {curriculum_id}")
    print("=" * 60)


if __name__ == "__main__":
    main()
