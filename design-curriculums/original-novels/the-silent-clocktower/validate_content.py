#!/usr/bin/env python3
"""
Validation script for The Silent Clocktower curriculum content.
Implements all 14 correctness properties from the design document.
Run from: original-novels/the-silent-clocktower/
"""

import importlib
import re
import sys


# --- Strip keys that must NOT be present (Property 14) ---
STRIP_KEYS = {
    "mp3Url", "illustrationSet", "chapterBookmarks", "segments",
    "whiteboardItems", "userReadingId", "lessonUniqueId",
    "curriculumTags", "taskId", "imageId"
}

# Vietnamese diacritics pattern (characters with Vietnamese-specific marks)
VIETNAMESE_RE = re.compile(
    r'[àáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợ'
    r'ùúủũụưứừửữựỳýỷỹỵđ'
    r'ÀÁẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬÈÉẺẼẸÊẾỀỂỄỆÌÍỈĨỊÒÓỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢ'
    r'ÙÚỦŨỤƯỨỪỬỮỰỲÝỶỸỴĐ]'
)


def load_chapters():
    """Import all 10 content modules dynamically. Returns list of (chapter_num, curriculum)."""
    chapters = []
    for n in range(1, 11):
        module_name = f"chapter{n}_content"
        try:
            mod = importlib.import_module(module_name)
            curriculum = mod.get_curriculum()
            chapters.append((n, curriculum))
        except Exception as e:
            print(f"ERROR: Could not load {module_name}: {e}")
            sys.exit(1)
    return chapters


def check_p1_session_structure(cur, ch, violations):
    """Property 1: Session structure — 6 sessions, correct activity types per session."""
    sessions = cur.get("learningSessions", [])
    if len(sessions) != 6:
        violations.append(f"FAIL [Chapter {ch}]: Expected 6 sessions, found {len(sessions)}")
        return

    expected_15 = ["viewFlashcards", "reading", "readAlong"]
    for i in range(5):
        acts = sessions[i].get("activities", [])
        if len(acts) != 3:
            violations.append(
                f"FAIL [Chapter {ch}, Session {i+1}]: Expected 3 activities, found {len(acts)}"
            )
            continue
        types = [a.get("activityType") for a in acts]
        if types != expected_15:
            violations.append(
                f"FAIL [Chapter {ch}, Session {i+1}]: Activity types {types} != {expected_15}"
            )

    # Session 6
    acts6 = sessions[5].get("activities", [])
    expected_6 = ["viewFlashcards", "readAlong"]
    if len(acts6) != 2:
        violations.append(
            f"FAIL [Chapter {ch}, Session 6]: Expected 2 activities, found {len(acts6)}"
        )
    else:
        types6 = [a.get("activityType") for a in acts6]
        if types6 != expected_6:
            violations.append(
                f"FAIL [Chapter {ch}, Session 6]: Activity types {types6} != {expected_6}"
            )


def check_p2_vocab_counts(cur, ch, violations):
    """Property 2: Vocab word counts — 3 per session 1-5, 15 for session 6, 15 unique total."""
    sessions = cur.get("learningSessions", [])
    if len(sessions) != 6:
        return  # Already caught by P1

    all_words = []
    for i in range(5):
        fc = sessions[i]["activities"][0]
        words = fc.get("data", {}).get("vocabList", [])
        if len(words) != 3:
            violations.append(
                f"FAIL [Chapter {ch}, Session {i+1}, viewFlashcards]: Expected 3 vocab words, found {len(words)}"
            )
        all_words.extend(words)

    # Session 6 flashcards
    fc6 = sessions[5]["activities"][0]
    words6 = fc6.get("data", {}).get("vocabList", [])
    if len(words6) != 15:
        violations.append(
            f"FAIL [Chapter {ch}, Session 6, viewFlashcards]: Expected 15 vocab words, found {len(words6)}"
        )

    # Total unique
    unique = set(w.lower() for w in all_words)
    if len(unique) != 15:
        violations.append(
            f"FAIL [Chapter {ch}]: Expected 15 unique vocab words, found {len(unique)}"
        )


def check_p3_vocab_in_passage(cur, ch, violations):
    """Property 3: Each vocab word appears (case-insensitive) in its assigned passage."""
    sessions = cur.get("learningSessions", [])
    for i in range(5):
        acts = sessions[i]["activities"]
        words = acts[0].get("data", {}).get("vocabList", [])
        passage = acts[1].get("data", {}).get("text", "")
        passage_lower = passage.lower()
        for w in words:
            if w.lower() not in passage_lower:
                violations.append(
                    f"FAIL [Chapter {ch}, Session {i+1}, reading]: Vocab word '{w}' not found in passage text"
                )


def check_p4_cross_chapter_vocab(all_chapters, violations):
    """Property 4: No vocabulary word repeated across chapters."""
    seen = {}  # word -> chapter number
    for ch, cur in all_chapters:
        sessions = cur.get("learningSessions", [])
        for i in range(5):
            words = sessions[i]["activities"][0].get("data", {}).get("vocabList", [])
            for w in words:
                wl = w.lower()
                if wl in seen:
                    violations.append(
                        f"FAIL [Chapter {ch}]: Vocab word '{w}' also appears in Chapter {seen[wl]}"
                    )
                else:
                    seen[wl] = ch


def check_p5_vocab_completeness(cur, ch, violations):
    """Property 5: Vocab entries are non-empty strings (adapted for vocabList format)."""
    sessions = cur.get("learningSessions", [])
    for i in range(5):
        words = sessions[i]["activities"][0].get("data", {}).get("vocabList", [])
        for w in words:
            if not isinstance(w, str) or not w.strip():
                violations.append(
                    f"FAIL [Chapter {ch}, Session {i+1}, viewFlashcards]: Vocab entry is empty or not a string: {w!r}"
                )
    # Session 6
    words6 = sessions[5]["activities"][0].get("data", {}).get("vocabList", [])
    for w in words6:
        if not isinstance(w, str) or not w.strip():
            violations.append(
                f"FAIL [Chapter {ch}, Session 6, viewFlashcards]: Vocab entry is empty or not a string: {w!r}"
            )


def check_p6_readalong_matches_reading(cur, ch, violations):
    """Property 6: readAlong text matches reading text in sessions 1-5."""
    sessions = cur.get("learningSessions", [])
    for i in range(5):
        acts = sessions[i]["activities"]
        reading_text = acts[1].get("data", {}).get("text", "")
        readalong_text = acts[2].get("data", {}).get("text", "")
        if reading_text != readalong_text:
            violations.append(
                f"FAIL [Chapter {ch}, Session {i+1}, readAlong]: Text does not match reading activity text"
            )


def check_p7_session6_full_text(cur, ch, violations):
    """Property 7: Session 6 readAlong text = concatenation of all 5 passages joined with \\n\\n."""
    sessions = cur.get("learningSessions", [])
    passages = []
    for i in range(5):
        text = sessions[i]["activities"][1].get("data", {}).get("text", "")
        passages.append(text)
    expected = "\n\n".join(passages)
    actual = sessions[5]["activities"][1].get("data", {}).get("text", "")
    if actual != expected:
        violations.append(
            f"FAIL [Chapter {ch}, Session 6, readAlong]: Full chapter text does not match concatenation of 5 passages"
        )


def check_p8_audio_speed(cur, ch, violations):
    """Property 8: viewFlashcards and reading activities have audioSpeed = -0.2 in their data."""
    sessions = cur.get("learningSessions", [])
    for i in range(6):
        acts = sessions[i].get("activities", [])
        for act in acts:
            atype = act.get("activityType")
            data = act.get("data", {})
            if atype in ("viewFlashcards", "reading"):
                speed = data.get("audioSpeed")
                if speed != -0.2:
                    violations.append(
                        f"FAIL [Chapter {ch}, Session {i+1}, {atype}]: audioSpeed = {speed}, expected -0.2"
                    )


def check_p9_passage_word_count(cur, ch, violations):
    """Property 9: Each passage is 135-220 words (±10% tolerance of 150-200)."""
    sessions = cur.get("learningSessions", [])
    for i in range(5):
        text = sessions[i]["activities"][1].get("data", {}).get("text", "")
        wc = len(text.split())
        if wc < 135 or wc > 220:
            violations.append(
                f"FAIL [Chapter {ch}, Session {i+1}, reading]: Passage word count {wc} outside range 135-220"
            )


def check_p10_title_format(cur, ch, violations):
    """Property 10: Title matches pattern with Vietnamese + English + 'Chương N'."""
    title = cur.get("title", "")
    # Must contain "Chương N" where N is the chapter number
    pattern = rf"Chương {ch}"
    if pattern not in title:
        violations.append(
            f"FAIL [Chapter {ch}]: Title does not contain '{pattern}': {title!r}"
        )
    # Must contain Vietnamese characters
    if not VIETNAMESE_RE.search(title):
        violations.append(
            f"FAIL [Chapter {ch}]: Title does not contain Vietnamese characters"
        )
    # Must contain parenthesized English title
    if "(" not in title or ")" not in title:
        violations.append(
            f"FAIL [Chapter {ch}]: Title missing parenthesized English title"
        )


def check_p11_session_titles(cur, ch, violations):
    """Property 11: Sessions 1-5 are 'Phần 1' through 'Phần 5', session 6 is 'Ôn tập'."""
    sessions = cur.get("learningSessions", [])
    for i in range(5):
        expected = f"Phần {i+1}"
        actual = sessions[i].get("title", "")
        if actual != expected:
            violations.append(
                f"FAIL [Chapter {ch}, Session {i+1}]: Title = {actual!r}, expected {expected!r}"
            )
    actual6 = sessions[5].get("title", "")
    if actual6 != "Ôn tập":
        violations.append(
            f"FAIL [Chapter {ch}, Session 6]: Title = {actual6!r}, expected 'Ôn tập'"
        )


def check_p12_activity_title_formats(cur, ch, violations):
    """Property 12: Activity title/description format conventions."""
    sessions = cur.get("learningSessions", [])
    for i in range(6):
        acts = sessions[i].get("activities", [])
        for act in acts:
            atype = act.get("activityType")
            title = act.get("title", "")
            desc = act.get("description", "")

            # All activities must have non-empty title and description
            if not title.strip():
                violations.append(
                    f"FAIL [Chapter {ch}, Session {i+1}, {atype}]: Empty title"
                )
            if not desc.strip():
                violations.append(
                    f"FAIL [Chapter {ch}, Session {i+1}, {atype}]: Empty description"
                )

            # viewFlashcards title starts with "Flashcards:"
            if atype == "viewFlashcards" and not title.startswith("Flashcards:"):
                violations.append(
                    f"FAIL [Chapter {ch}, Session {i+1}, viewFlashcards]: Title does not start with 'Flashcards:': {title!r}"
                )

            # reading title starts with "Đọc:"
            if atype == "reading" and not title.startswith("Đọc:"):
                violations.append(
                    f"FAIL [Chapter {ch}, Session {i+1}, reading]: Title does not start with 'Đọc:': {title!r}"
                )

            # readAlong in sessions 1-5 starts with "Nghe:"
            if atype == "readAlong" and i < 5 and not title.startswith("Nghe:"):
                violations.append(
                    f"FAIL [Chapter {ch}, Session {i+1}, readAlong]: Title does not start with 'Nghe:': {title!r}"
                )

            # Session 6 readAlong contains "Toàn bộ câu chuyện"
            if atype == "readAlong" and i == 5 and "Toàn bộ câu chuyện" not in title:
                violations.append(
                    f"FAIL [Chapter {ch}, Session 6, readAlong]: Title does not contain 'Toàn bộ câu chuyện': {title!r}"
                )


def check_p13_vietnamese_metadata(cur, ch, violations):
    """Property 13: Vietnamese metadata — preview.text and description contain Vietnamese diacritics,
    language = 'en', userLanguage = 'vi'."""
    preview_text = cur.get("preview", {}).get("text", "")
    description = cur.get("description", "")

    if not VIETNAMESE_RE.search(preview_text):
        violations.append(
            f"FAIL [Chapter {ch}]: preview.text does not contain Vietnamese characters"
        )
    if not VIETNAMESE_RE.search(description):
        violations.append(
            f"FAIL [Chapter {ch}]: description does not contain Vietnamese characters"
        )
    if cur.get("language") != "en":
        violations.append(
            f"FAIL [Chapter {ch}]: language = {cur.get('language')!r}, expected 'en'"
        )
    if cur.get("userLanguage") != "vi":
        violations.append(
            f"FAIL [Chapter {ch}]: userLanguage = {cur.get('userLanguage')!r}, expected 'vi'"
        )


def check_p14_no_strip_keys(cur, ch, violations):
    """Property 14: Recursively check that no strip-keys exist anywhere in the curriculum dict."""
    def _scan(obj, path=""):
        if isinstance(obj, dict):
            for key, val in obj.items():
                if key in STRIP_KEYS:
                    violations.append(
                        f"FAIL [Chapter {ch}]: Forbidden key '{key}' found at {path}.{key}"
                    )
                _scan(val, f"{path}.{key}")
        elif isinstance(obj, list):
            for idx, item in enumerate(obj):
                _scan(item, f"{path}[{idx}]")
    _scan(cur, "root")


def validate_all():
    """Import all 10 content modules, run all 14 property checks, return violations."""
    chapters = load_chapters()
    violations = []

    for ch, cur in chapters:
        print(f"Validating chapter {ch}...", end=" ")
        ch_violations_before = len(violations)

        # Per-chapter properties
        check_p1_session_structure(cur, ch, violations)
        check_p2_vocab_counts(cur, ch, violations)
        check_p3_vocab_in_passage(cur, ch, violations)
        check_p5_vocab_completeness(cur, ch, violations)
        check_p6_readalong_matches_reading(cur, ch, violations)
        check_p7_session6_full_text(cur, ch, violations)
        check_p8_audio_speed(cur, ch, violations)
        check_p9_passage_word_count(cur, ch, violations)
        check_p10_title_format(cur, ch, violations)
        check_p11_session_titles(cur, ch, violations)
        check_p12_activity_title_formats(cur, ch, violations)
        check_p13_vietnamese_metadata(cur, ch, violations)
        check_p14_no_strip_keys(cur, ch, violations)

        if len(violations) == ch_violations_before:
            print("OK")
        else:
            print()
            for v in violations[ch_violations_before:]:
                print(f"  {v}")

    # Cross-chapter property
    print("Cross-chapter vocab check...", end=" ")
    cross_before = len(violations)
    check_p4_cross_chapter_vocab(chapters, violations)
    if len(violations) == cross_before:
        print("OK")
    else:
        print()
        for v in violations[cross_before:]:
            print(f"  {v}")

    return violations


def main():
    violations = validate_all()
    print()
    if violations:
        print(f"{len(violations)} violations found. Fix before uploading.")
        sys.exit(1)
    else:
        print("All 14 properties verified across 10 chapters. 0 violations.")
        sys.exit(0)


if __name__ == "__main__":
    main()
