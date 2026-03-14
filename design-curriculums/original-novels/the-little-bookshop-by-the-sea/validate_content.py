#!/usr/bin/env python3
"""
Validation script for The Little Bookshop by the Sea curriculum content.
Checks correctness properties 1-11 from the design document.

Run from the novel directory:
    python validate_content.py
"""

import importlib
import re
import sys
import os

# Ensure the novel directory is on the path so chapterN_content modules can be imported
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

STRIP_KEYS = {
    "mp3Url", "illustrationSet", "chapterBookmarks", "segments",
    "whiteboardItems", "userReadingId", "lessonUniqueId",
    "curriculumTags", "taskId", "imageId",
}

LEVEL_DESCRIPTORS = [
    "preintermediate", "intermediate", "beginner", "advanced",
    "sơ trung cấp", "trung cấp",
]

NUM_CHAPTERS = 10


def load_all_chapters():
    """Dynamically import all 10 chapter content modules and return their content dicts."""
    chapters = []
    for i in range(1, NUM_CHAPTERS + 1):
        module_name = f"chapter{i}_content"
        mod = importlib.import_module(module_name)
        chapters.append(mod.get_content())
    return chapters


def get_vocab_sets(content):
    """Return per-session vocab lists (sessions 0-4) and the full chapter vocab set."""
    sessions = content["learningSessions"]
    per_session = []
    all_vocab = set()
    for s in sessions[:5]:
        vl = s["activities"][0]["data"]["vocabList"]
        per_session.append(vl)
        all_vocab.update(w.lower() for w in vl)
    return per_session, all_vocab


def check_strip_keys_recursive(obj, path=""):
    """Recursively check for strip keys. Returns list of violation paths."""
    violations = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            current = f"{path}.{k}" if path else k
            if k in STRIP_KEYS:
                violations.append(current)
            violations.extend(check_strip_keys_recursive(v, current))
    elif isinstance(obj, list):
        for idx, item in enumerate(obj):
            violations.extend(check_strip_keys_recursive(item, f"{path}[{idx}]"))
    return violations



# ---------------------------------------------------------------------------
# Per-chapter property checks
# ---------------------------------------------------------------------------

def check_property_3(ch_num, content):
    """Property 3: Session and activity structure."""
    sessions = content["learningSessions"]
    errors = []

    if len(sessions) != 6:
        errors.append(f"Expected 6 sessions, got {len(sessions)}")
        return errors

    for i in range(5):
        acts = sessions[i]["activities"]
        types = [a["activityType"] for a in acts]
        expected = ["viewFlashcards", "reading", "readAlong"]
        if types != expected:
            errors.append(f"Session {i}: expected {expected}, got {types}")

    acts6 = sessions[5]["activities"]
    types6 = [a["activityType"] for a in acts6]
    expected6 = ["viewFlashcards", "readAlong"]
    if types6 != expected6:
        errors.append(f"Session 5: expected {expected6}, got {types6}")

    return errors


def check_property_4(ch_num, content):
    """Property 4: Activity data shape."""
    errors = []
    for si, session in enumerate(content["learningSessions"]):
        for ai, act in enumerate(session["activities"]):
            atype = act["activityType"]
            data = act.get("data", {})
            label = f"Session {si}, activity {ai} ({atype})"

            if atype == "viewFlashcards":
                if "vocabList" not in data or not isinstance(data["vocabList"], list) or len(data["vocabList"]) == 0:
                    errors.append(f"{label}: missing or empty vocabList")
                if "audioSpeed" not in data:
                    errors.append(f"{label}: missing audioSpeed")

            elif atype == "reading":
                if "text" not in data or not isinstance(data["text"], str) or len(data["text"]) == 0:
                    errors.append(f"{label}: missing or empty text")
                if "audioSpeed" not in data:
                    errors.append(f"{label}: missing audioSpeed")

            elif atype == "readAlong":
                if "text" not in data or not isinstance(data["text"], str) or len(data["text"]) == 0:
                    errors.append(f"{label}: missing or empty text")
                if "audioSpeed" in data:
                    errors.append(f"{label}: readAlong should NOT have audioSpeed")

    return errors


def check_property_5(ch_num, content):
    """Property 5: readAlong text == reading text in sessions 0-4."""
    errors = []
    for si in range(5):
        acts = content["learningSessions"][si]["activities"]
        reading_text = acts[1]["data"]["text"]
        readalong_text = acts[2]["data"]["text"]
        if reading_text != readalong_text:
            errors.append(f"Session {si}: reading text != readAlong text")
    return errors


def check_property_6(ch_num, content):
    """Property 6: Session 6 review aggregation."""
    errors = []
    sessions = content["learningSessions"]

    # Vocab union check
    all_vocab = set()
    for si in range(5):
        vl = sessions[si]["activities"][0]["data"]["vocabList"]
        all_vocab.update(vl)

    s6_vocab = set(sessions[5]["activities"][0]["data"]["vocabList"])
    if all_vocab != s6_vocab:
        missing = all_vocab - s6_vocab
        extra = s6_vocab - all_vocab
        if missing:
            errors.append(f"Session 5 vocabList missing: {missing}")
        if extra:
            errors.append(f"Session 5 vocabList has extra: {extra}")

    # Text concatenation check
    reading_texts = []
    for si in range(5):
        reading_texts.append(sessions[si]["activities"][1]["data"]["text"])
    expected_text = "\n\n".join(reading_texts)
    s6_text = sessions[5]["activities"][1]["data"]["text"]
    if s6_text != expected_text:
        # Show first difference location
        for i, (a, b) in enumerate(zip(expected_text, s6_text)):
            if a != b:
                errors.append(f"Session 5 readAlong text differs at char {i}")
                break
        else:
            errors.append(f"Session 5 readAlong text length mismatch: expected {len(expected_text)}, got {len(s6_text)}")
    return errors


def check_property_7(ch_num, content):
    """Property 7: Title format compliance."""
    errors = []
    title = content["title"]
    pattern = r".+ — Chương \d+: .+ \(.+\)"
    if not re.fullmatch(pattern, title):
        errors.append(f"Title does not match pattern: '{title}'")

    title_lower = title.lower()
    for desc in LEVEL_DESCRIPTORS:
        if desc.lower() in title_lower:
            errors.append(f"Title contains level descriptor '{desc}': '{title}'")
    return errors


def check_property_8(ch_num, content):
    """Property 8: Each session 0-4 viewFlashcards has exactly 3 words."""
    errors = []
    for si in range(5):
        vl = content["learningSessions"][si]["activities"][0]["data"]["vocabList"]
        if len(vl) != 3:
            errors.append(f"Session {si}: expected 3 vocab words, got {len(vl)}")
    return errors


def check_property_9(ch_num, content):
    """Property 9: Every vocab word appears in its session's reading text."""
    errors = []
    for si in range(5):
        acts = content["learningSessions"][si]["activities"]
        vocab = acts[0]["data"]["vocabList"]
        text_lower = acts[1]["data"]["text"].lower()
        for word in vocab:
            if word.lower() not in text_lower:
                errors.append(f"Session {si}: vocab word '{word}' not found in reading text")
    return errors


def check_property_10(ch_num, content):
    """Property 10: Reading passage word counts don't vary by more than factor of 2."""
    errors = []
    counts = []
    for si in range(5):
        text = content["learningSessions"][si]["activities"][1]["data"]["text"]
        wc = len(text.split())
        counts.append(wc)

    avg = sum(counts) / len(counts)
    for si, wc in enumerate(counts):
        if wc < avg / 2:
            errors.append(f"Session {si}: {wc} words < half of average ({avg:.0f})")
        if wc > avg * 2:
            errors.append(f"Session {si}: {wc} words > double the average ({avg:.0f})")

    return errors


def check_property_11(ch_num, content):
    """Property 11: No strip keys anywhere in content dict."""
    violations = check_strip_keys_recursive(content)
    return [f"Strip key found at: {v}" for v in violations]



# ---------------------------------------------------------------------------
# Cross-chapter property checks
# ---------------------------------------------------------------------------

def check_property_1(all_vocab_sets):
    """Property 1: Each chapter has exactly 15 unique vocab words."""
    errors = []
    for i, vocab in enumerate(all_vocab_sets):
        if len(vocab) != 15:
            errors.append(f"Chapter {i + 1}: {len(vocab)} unique vocab words (expected 15)")
    return errors


def check_property_2(all_vocab_sets):
    """Property 2: At most 2 vocab words shared between any two chapters."""
    errors = []
    for i in range(len(all_vocab_sets)):
        for j in range(i + 1, len(all_vocab_sets)):
            overlap = all_vocab_sets[i] & all_vocab_sets[j]
            if len(overlap) > 2:
                errors.append(
                    f"Chapters {i + 1} & {j + 1}: {len(overlap)} shared words "
                    f"(max 2 allowed): {sorted(overlap)}"
                )
    return errors


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

PER_CHAPTER_CHECKS = [
    (check_property_3, "Property 3 (session structure)"),
    (check_property_4, "Property 4 (activity data shape)"),
    (check_property_5, "Property 5 (reading/readAlong match)"),
    (check_property_6, "Property 6 (session 6 aggregation)"),
    (check_property_7, "Property 7 (title format)"),
    (check_property_8, "Property 8 (3 vocab per session)"),
    (check_property_9, "Property 9 (vocab in reading text)"),
    (check_property_10, "Property 10 (passage length balance)"),
    (check_property_11, "Property 11 (no strip keys)"),
]


def main():
    print("Loading all 10 chapter content modules...\n")
    chapters = load_all_chapters()
    print(f"Loaded {len(chapters)} chapters.\n")

    total_pass = 0
    total_fail = 0

    # Per-chapter checks
    all_vocab_sets = []
    for ch_idx, content in enumerate(chapters):
        ch_num = ch_idx + 1
        _, vocab_set = get_vocab_sets(content)
        all_vocab_sets.append(vocab_set)

        for check_fn, label in PER_CHAPTER_CHECKS:
            errors = check_fn(ch_num, content)
            if errors:
                print(f"Chapter {ch_num}: {label} ... FAIL")
                for e in errors:
                    print(f"  - {e}")
                total_fail += 1
            else:
                print(f"Chapter {ch_num}: {label} ... PASS")
                total_pass += 1

    print()

    # Cross-chapter checks
    errors_p1 = check_property_1(all_vocab_sets)
    if errors_p1:
        print("Cross-chapter: Property 1 (vocab count per chapter) ... FAIL")
        for e in errors_p1:
            print(f"  - {e}")
        total_fail += 1
    else:
        print("Cross-chapter: Property 1 (vocab count per chapter) ... PASS")
        total_pass += 1

    errors_p2 = check_property_2(all_vocab_sets)
    if errors_p2:
        print("Cross-chapter: Property 2 (vocab overlap between chapters) ... FAIL")
        for e in errors_p2:
            print(f"  - {e}")
        total_fail += 1
    else:
        print("Cross-chapter: Property 2 (vocab overlap between chapters) ... PASS")
        total_pass += 1

    # Summary
    print(f"\n{'=' * 50}")
    print(f"TOTAL: {total_pass} passed, {total_fail} failed")
    if total_fail == 0:
        print("All properties validated successfully!")
    else:
        print(f"{total_fail} property check(s) FAILED — review errors above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
