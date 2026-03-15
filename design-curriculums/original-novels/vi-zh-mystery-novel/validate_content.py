#!/usr/bin/env python3
"""
Validation script for "Bức Tranh Biến Mất (消失的画)" vi-zh mystery novel.
Implements all 12 correctness properties from the design document.
Run from: original-novels/vi-zh-mystery-novel/
"""

import importlib
import re
import sys


# --- Strip keys that must NOT be present (Property 12) ---
STRIP_KEYS = {
    "mp3Url", "illustrationSet", "chapterBookmarks", "segments",
    "whiteboardItems", "userReadingId", "lessonUniqueId",
    "curriculumTags", "taskId", "imageId"
}

# Vietnamese diacritics pattern
VIETNAMESE_RE = re.compile(
    r'[àáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợ'
    r'ùúủũụưứừửữựỳýỷỹỵđ'
    r'ÀÁẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬÈÉẺẼẸÊẾỀỂỄỆÌÍỈĨỊÒÓỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢ'
    r'ÙÚỦŨỤƯỨỪỬỮỰỲÝỶỸỴĐ]'
)

# Level descriptors that must NOT appear in titles (Property 10)
FORBIDDEN_LEVEL_STRINGS = [
    "preintermediate", "sơ trung cấp", "初级", "中级",
    "beginner", "intermediate", "advanced"
]


def count_chinese_chars(text):
    """Count Chinese characters (CJK Unified Ideographs range 0x4e00-0x9fff)."""
    return sum(1 for ch in text if '\u4e00' <= ch <= '\u9fff')


def load_chapters():
    """Import all 10 content modules dynamically. Returns list of (chapter_num, curriculum)."""
    chapters = []
    for n in range(1, 11):
        module_name = f"chapter{n}_content"
        try:
            mod = importlib.import_module(module_name)
            curriculum = mod.get_content()
            chapters.append((n, curriculum))
        except Exception as e:
            print(f"ERROR: Could not load {module_name}: {e}")
            sys.exit(1)
    return chapters


# --- Property 1: Session structure ---
def check_p1_session_structure(cur, ch, violations):
    """P1: 6 sessions; sessions 1-5 have 3 activities [viewFlashcards, reading, readAlong];
    session 6 has 2 activities [viewFlashcards, readAlong]."""
    sessions = cur.get("learningSessions", [])
    if len(sessions) != 6:
        violations.append(f"FAIL [Chapter {ch}] P1: Expected 6 sessions, found {len(sessions)}")
        return

    expected_15 = ["viewFlashcards", "reading", "readAlong"]
    for i in range(5):
        acts = sessions[i].get("activities", [])
        if len(acts) != 3:
            violations.append(
                f"FAIL [Chapter {ch}, Session {i+1}] P1: Expected 3 activities, found {len(acts)}"
            )
            continue
        types = [a.get("activityType") for a in acts]
        if types != expected_15:
            violations.append(
                f"FAIL [Chapter {ch}, Session {i+1}] P1: Activity types {types} != {expected_15}"
            )

    acts6 = sessions[5].get("activities", [])
    expected_6 = ["viewFlashcards", "readAlong"]
    if len(acts6) != 2:
        violations.append(
            f"FAIL [Chapter {ch}, Session 6] P1: Expected 2 activities, found {len(acts6)}"
        )
    else:
        types6 = [a.get("activityType") for a in acts6]
        if types6 != expected_6:
            violations.append(
                f"FAIL [Chapter {ch}, Session 6] P1: Activity types {types6} != {expected_6}"
            )


# --- Property 2: Activity fields and audioSpeed ---
def check_p2_activity_fields(cur, ch, violations):
    """P2: viewFlashcards has vocabList + audioSpeed=-0.2; reading has text + audioSpeed=-0.2;
    readAlong has text."""
    sessions = cur.get("learningSessions", [])
    for i in range(len(sessions)):
        acts = sessions[i].get("activities", [])
        for act in acts:
            atype = act.get("activityType")
            data = act.get("data", {})

            if atype == "viewFlashcards":
                if "vocabList" not in data or not isinstance(data["vocabList"], list):
                    violations.append(
                        f"FAIL [Chapter {ch}, Session {i+1}, viewFlashcards] P2: Missing or invalid vocabList"
                    )
                if data.get("audioSpeed") != -0.2:
                    violations.append(
                        f"FAIL [Chapter {ch}, Session {i+1}, viewFlashcards] P2: audioSpeed = {data.get('audioSpeed')}, expected -0.2"
                    )

            elif atype == "reading":
                text = data.get("text", "")
                if not text or not isinstance(text, str):
                    violations.append(
                        f"FAIL [Chapter {ch}, Session {i+1}, reading] P2: Missing or empty text"
                    )
                if data.get("audioSpeed") != -0.2:
                    violations.append(
                        f"FAIL [Chapter {ch}, Session {i+1}, reading] P2: audioSpeed = {data.get('audioSpeed')}, expected -0.2"
                    )

            elif atype == "readAlong":
                text = data.get("text", "")
                if not text or not isinstance(text, str):
                    violations.append(
                        f"FAIL [Chapter {ch}, Session {i+1}, readAlong] P2: Missing or empty text"
                    )


# --- Property 3: Vocab count ---
def check_p3_vocab_counts(cur, ch, violations):
    """P3: 15 unique words per chapter, 3 per session 1-5."""
    sessions = cur.get("learningSessions", [])
    if len(sessions) != 6:
        return

    all_words = []
    for i in range(5):
        fc = sessions[i]["activities"][0]
        words = fc.get("data", {}).get("vocabList", [])
        if len(words) != 3:
            violations.append(
                f"FAIL [Chapter {ch}, Session {i+1}] P3: Expected 3 vocab words, found {len(words)}"
            )
        all_words.extend(words)

    unique = set(all_words)
    if len(unique) != 15:
        violations.append(
            f"FAIL [Chapter {ch}] P3: Expected 15 unique vocab words, found {len(unique)}"
        )


# --- Property 4: readAlong == reading text ---
def check_p4_readalong_matches_reading(cur, ch, violations):
    """P4: Identical text in sessions 1-5 between reading and readAlong."""
    sessions = cur.get("learningSessions", [])
    for i in range(5):
        acts = sessions[i]["activities"]
        if len(acts) < 3:
            continue
        reading_text = acts[1].get("data", {}).get("text", "")
        readalong_text = acts[2].get("data", {}).get("text", "")
        if reading_text != readalong_text:
            violations.append(
                f"FAIL [Chapter {ch}, Session {i+1}] P4: readAlong text does not match reading text"
            )


# --- Property 5: Session 6 concatenation ---
def check_p5_session6_concatenation(cur, ch, violations):
    """P5: Session 6 readAlong text = '\\n\\n'.join(passages 1-5)."""
    sessions = cur.get("learningSessions", [])
    if len(sessions) != 6:
        return
    passages = []
    for i in range(5):
        text = sessions[i]["activities"][1].get("data", {}).get("text", "")
        passages.append(text)
    expected = "\n\n".join(passages)
    actual = sessions[5]["activities"][1].get("data", {}).get("text", "")
    if actual != expected:
        violations.append(
            f"FAIL [Chapter {ch}, Session 6] P5: readAlong text does not match concatenation of passages 1-5"
        )


# --- Property 6: Session 6 vocab union ---
def check_p6_session6_vocab_union(cur, ch, violations):
    """P6: Session 6 viewFlashcards vocabList = union of sessions 1-5 vocabLists (all 15 words)."""
    sessions = cur.get("learningSessions", [])
    if len(sessions) != 6:
        return
    expected_words = []
    for i in range(5):
        words = sessions[i]["activities"][0].get("data", {}).get("vocabList", [])
        expected_words.extend(words)
    actual_words = sessions[5]["activities"][0].get("data", {}).get("vocabList", [])

    if set(actual_words) != set(expected_words):
        violations.append(
            f"FAIL [Chapter {ch}, Session 6] P6: vocabList {actual_words} != union of sessions 1-5 {expected_words}"
        )
    if len(actual_words) != 15:
        violations.append(
            f"FAIL [Chapter {ch}, Session 6] P6: Expected 15 words in session 6 vocabList, found {len(actual_words)}"
        )


# --- Property 7: Cross-chapter overlap ≤ 2 ---
def check_p7_cross_chapter_overlap(all_chapters, violations):
    """P7: At most 2 shared vocab words between any pair of chapters."""
    chapter_vocabs = {}
    for ch, cur in all_chapters:
        sessions = cur.get("learningSessions", [])
        words = set()
        for i in range(5):
            vl = sessions[i]["activities"][0].get("data", {}).get("vocabList", [])
            words.update(vl)
        chapter_vocabs[ch] = words

    chapters = sorted(chapter_vocabs.keys())
    for i in range(len(chapters)):
        for j in range(i + 1, len(chapters)):
            ch_a, ch_b = chapters[i], chapters[j]
            overlap = chapter_vocabs[ch_a] & chapter_vocabs[ch_b]
            if len(overlap) > 2:
                violations.append(
                    f"FAIL P7: Chapters {ch_a} and {ch_b} share {len(overlap)} vocab words (max 2): {overlap}"
                )


# --- Property 8: Passage length 80-180 Chinese characters ---
def check_p8_passage_length(cur, ch, violations):
    """P8: Chinese character count for each passage in sessions 1-5 must be 80-180."""
    sessions = cur.get("learningSessions", [])
    for i in range(5):
        text = sessions[i]["activities"][1].get("data", {}).get("text", "")
        cc = count_chinese_chars(text)
        if cc < 80 or cc > 180:
            violations.append(
                f"FAIL [Chapter {ch}, Session {i+1}] P8: Chinese char count {cc} outside range 80-180"
            )


# --- Property 9: Vocab in passages ---
def check_p9_vocab_in_passages(cur, ch, violations):
    """P9: Every vocab word appears as substring in its session's reading passage."""
    sessions = cur.get("learningSessions", [])
    for i in range(5):
        acts = sessions[i]["activities"]
        words = acts[0].get("data", {}).get("vocabList", [])
        passage = acts[1].get("data", {}).get("text", "")
        for w in words:
            if w not in passage:
                violations.append(
                    f"FAIL [Chapter {ch}, Session {i+1}] P9: Vocab word '{w}' not found in passage"
                )


# --- Property 10: Title format + no level ---
def check_p10_title_format(cur, ch, violations):
    """P10: Title contains 'Chương N:', does NOT contain level descriptors."""
    title = cur.get("title", "")
    pattern = f"Chương {ch}:"
    if pattern not in title:
        violations.append(
            f"FAIL [Chapter {ch}] P10: Title does not contain '{pattern}': {title!r}"
        )
    title_lower = title.lower()
    for forbidden in FORBIDDEN_LEVEL_STRINGS:
        if forbidden.lower() in title_lower:
            violations.append(
                f"FAIL [Chapter {ch}] P10: Title contains forbidden level string '{forbidden}': {title!r}"
            )


# --- Property 11: Preview 100-200 words + Vietnamese metadata ---
def check_p11_preview_and_metadata(cur, ch, violations):
    """P11: Preview text word count in range 100-200, description has Vietnamese diacritics,
    language='zh', userLanguage='vi'."""
    preview_text = cur.get("preview", {}).get("text", "")
    description = cur.get("description", "")

    # Preview word count
    word_count = len(preview_text.split())
    if word_count < 100 or word_count > 200:
        violations.append(
            f"FAIL [Chapter {ch}] P11: Preview word count {word_count} outside range 100-200"
        )

    # Description has Vietnamese diacritics
    if not VIETNAMESE_RE.search(description):
        violations.append(
            f"FAIL [Chapter {ch}] P11: Description does not contain Vietnamese diacritics"
        )

    # Language checks
    if cur.get("language") != "zh":
        violations.append(
            f"FAIL [Chapter {ch}] P11: language = {cur.get('language')!r}, expected 'zh'"
        )
    if cur.get("userLanguage") != "vi":
        violations.append(
            f"FAIL [Chapter {ch}] P11: userLanguage = {cur.get('userLanguage')!r}, expected 'vi'"
        )


# --- Property 12: No strip keys ---
def check_p12_no_strip_keys(cur, ch, violations):
    """P12: Recursive check for forbidden keys."""
    def _scan(obj, path=""):
        if isinstance(obj, dict):
            for key, val in obj.items():
                if key in STRIP_KEYS:
                    violations.append(
                        f"FAIL [Chapter {ch}] P12: Forbidden key '{key}' found at {path}.{key}"
                    )
                _scan(val, f"{path}.{key}")
        elif isinstance(obj, list):
            for idx, item in enumerate(obj):
                _scan(item, f"{path}[{idx}]")
    _scan(cur, "root")


# --- Main validation ---
def validate_all():
    """Import all 10 content modules, run all 12 property checks, return violations."""
    chapters = load_chapters()
    violations = []

    for ch, cur in chapters:
        print(f"Validating chapter {ch}...", end=" ")
        ch_violations_before = len(violations)

        check_p1_session_structure(cur, ch, violations)
        check_p2_activity_fields(cur, ch, violations)
        check_p3_vocab_counts(cur, ch, violations)
        check_p4_readalong_matches_reading(cur, ch, violations)
        check_p5_session6_concatenation(cur, ch, violations)
        check_p6_session6_vocab_union(cur, ch, violations)
        check_p8_passage_length(cur, ch, violations)
        check_p9_vocab_in_passages(cur, ch, violations)
        check_p10_title_format(cur, ch, violations)
        check_p11_preview_and_metadata(cur, ch, violations)
        check_p12_no_strip_keys(cur, ch, violations)

        if len(violations) == ch_violations_before:
            print("OK")
        else:
            print()
            for v in violations[ch_violations_before:]:
                print(f"  {v}")

    # Cross-chapter property
    print("Cross-chapter vocab overlap check...", end=" ")
    cross_before = len(violations)
    check_p7_cross_chapter_overlap(chapters, violations)
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
        print("All 12 properties verified across 10 chapters. 0 violations.")
        sys.exit(0)


if __name__ == "__main__":
    main()
