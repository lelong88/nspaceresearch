#!/usr/bin/env python3
"""
Update 20 curriculums with high-quality rewritten content.

Reads each curriculum content file from hugo/curriculums/, fetches the existing
curriculum from the database via API, patches the relevant fields (preview,
introAudio, writingSentence, writingParagraph), strips mp3Url where content
changed, and uploads via the curriculum/update endpoint.
"""
import json, sys, time, importlib, os, requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")
from firebase_token import get_firebase_id_token

API_BASE = "https://helloapi.step.is/curriculum"
UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"

# All curriculum content modules (filename without .py)
MODULES = [
    "sleep", "attention", "microplastics", "color", "fermentation",
    "procrastination", "ocean_floor", "forgiveness", "vertical_farms",
    "fungi", "music_math", "choice", "biomimicry", "negotiation",
    "quantum", "loneliness", "ai_ethics", "habits", "bridges", "crowds",
]


def load_content(module_name):
    """Import a curriculum content module and return its CONTENT dict."""
    mod = importlib.import_module(f"curriculums.{module_name}")
    return mod.CONTENT


def fetch_curriculum(cid):
    """Fetch existing curriculum content from the API."""
    token = get_firebase_id_token(UID)
    r = requests.post(f"{API_BASE}/getOne", json={"id": cid, "uid": UID, "firebaseIdToken": token})
    r.raise_for_status()
    data = r.json()
    # content is stored as JSON string in the DB, returned as-is or parsed
    content = data.get("content")
    if isinstance(content, str):
        return json.loads(content)
    return content


def strip_mp3(obj):
    """Recursively remove mp3Url keys from a dict/list."""
    if isinstance(obj, dict):
        return {k: strip_mp3(v) for k, v in obj.items() if k != "mp3Url"}
    if isinstance(obj, list):
        return [strip_mp3(item) for item in obj]
    return obj


def find_activity(session, activity_type, index=0):
    """Find the nth activity of a given type in a session."""
    count = 0
    for act in session.get("activities", []):
        if act.get("activityType") == activity_type:
            if count == index:
                return act
            count += 1
    return None


def patch_curriculum(existing, content):
    """
    Patch an existing curriculum JSON with new content from a content file.

    Patches:
    - preview.text (strip mp3Url from preview)
    - Session 1 introAudio text
    - Session 2 introAudio text
    - Session 3 introAudio text (review intro)
    - Session 4 introAudio text (final intro)
    - Session 4 farewell introAudio text
    - Session 1 & 2 writingSentence items (strip mp3Url)
    - Session 1-4 writingParagraph prompts (strip mp3Url)
    """
    sessions = existing.get("learningSessions", [])
    if len(sessions) < 4:
        raise ValueError(f"Expected 4 sessions, got {len(sessions)}")

    # 1. Patch preview
    existing["preview"]["text"] = content["preview"]
    if "mp3Url" in existing["preview"]:
        del existing["preview"]["mp3Url"]

    # 2. Patch Session 1 introAudio
    s1_intro = find_activity(sessions[0], "introAudio", 0)
    if s1_intro:
        s1_intro["data"]["text"] = content["s1_intro"]
        s1_intro["data"].pop("mp3Url", None)
        # Clear whiteboard/chapter bookmarks since text changed
        s1_intro["data"].pop("whiteboardItems", None)
        s1_intro["data"].pop("chapterBookmarks", None)

    # 3. Patch Session 2 introAudio
    s2_intro = find_activity(sessions[1], "introAudio", 0)
    if s2_intro:
        s2_intro["data"]["text"] = content["s2_intro"]
        s2_intro["data"].pop("mp3Url", None)
        s2_intro["data"].pop("whiteboardItems", None)
        s2_intro["data"].pop("chapterBookmarks", None)

    # 4. Patch Session 3 introAudio (review)
    s3_intro = find_activity(sessions[2], "introAudio", 0)
    if s3_intro:
        s3_intro["data"]["text"] = content["s3_intro"]
        s3_intro["data"].pop("mp3Url", None)
        s3_intro["data"].pop("whiteboardItems", None)
        s3_intro["data"].pop("chapterBookmarks", None)

    # 5. Patch Session 4 introAudio (final reading intro)
    s4_intro = find_activity(sessions[3], "introAudio", 0)
    if s4_intro:
        s4_intro["data"]["text"] = content["s4_intro"]
        s4_intro["data"].pop("mp3Url", None)
        s4_intro["data"].pop("whiteboardItems", None)
        s4_intro["data"].pop("chapterBookmarks", None)

    # 6. Patch Session 4 farewell (second introAudio in session 4)
    s4_farewell = find_activity(sessions[3], "introAudio", 1)
    if s4_farewell:
        s4_farewell["data"]["text"] = content["s4_farewell"]
        s4_farewell["data"].pop("mp3Url", None)
        s4_farewell["data"].pop("whiteboardItems", None)
        s4_farewell["data"].pop("chapterBookmarks", None)

    # 7. Patch writingSentence items (Sessions 1 & 2)
    for si, key in [(0, "s1_ws_items"), (1, "s2_ws_items")]:
        ws = find_activity(sessions[si], "writingSentence", 0)
        if ws and key in content:
            # Replace items, stripping mp3Url
            ws["data"]["items"] = [
                {"prompt": item["prompt"], "targetVocab": item["targetVocab"]}
                for item in content[key]
            ]

    # 8. Patch writingParagraph prompts (Sessions 1-4)
    wp_keys = [
        (0, "s1_wp_prompts"),
        (1, "s2_wp_prompts"),
        (2, "s3_wp_prompts"),
        (3, "s4_wp_prompts"),
    ]
    for si, key in wp_keys:
        wp = find_activity(sessions[si], "writingParagraph", 0)
        if wp and key in content:
            wp["data"]["prompts"] = content[key]
            wp["data"].pop("mp3Url", None)

    return existing


def upload_update(cid, content_json):
    """Upload patched curriculum via the update endpoint."""
    token = get_firebase_id_token(UID)
    r = requests.post(
        f"{API_BASE}/update",
        json={
            "id": cid,
            "uid": UID,
            "content": json.dumps(content_json),
            "firebaseIdToken": token,
        },
    )
    r.raise_for_status()
    return r.json()


def main():
    print(f"Updating {len(MODULES)} curriculums...\n")
    ok, fail = 0, 0

    for i, mod_name in enumerate(MODULES):
        content = load_content(mod_name)
        cid = content["curriculum_id"]
        title = content["title"]
        print(f"[{i+1}/{len(MODULES)}] {title} ({cid})...", end=" ", flush=True)

        try:
            # Fetch existing curriculum
            existing = fetch_curriculum(cid)

            # Patch with new content
            patched = patch_curriculum(existing, content)

            # Upload
            upload_update(cid, patched)
            print("✓")
            ok += 1
        except Exception as e:
            print(f"✗ {e}")
            fail += 1

        time.sleep(0.5)

    print(f"\nDone: {ok} updated, {fail} failed.")


if __name__ == "__main__":
    main()
