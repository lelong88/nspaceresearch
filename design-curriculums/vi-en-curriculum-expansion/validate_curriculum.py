"""
validate_curriculum.py — Structural validation helper for vi-en curriculum expansion.

Structural validation ONLY — no content generation.
Used by all 100 curriculum creation scripts to verify content before API upload.

Each function raises ValueError with a descriptive message on validation failure.
"""

import json
import re

# ── Constants ──

VALID_ACTIVITY_TYPES = {
    "introAudio", "viewFlashcards", "speakFlashcards",
    "vocabLevel1", "vocabLevel2", "vocabLevel3",
    "reading", "speakReading", "readAlong",
    "writingSentence", "writingParagraph",
}

VALID_CONTENT_TYPE_TAGS = [
    [], ["movie"], ["music"], ["podcast"], ["story"],
]

STRIP_KEYS = {
    "mp3Url", "illustrationSet", "chapterBookmarks", "segments",
    "whiteboardItems", "userReadingId", "lessonUniqueId",
    "curriculumTags", "taskId", "imageId",
}

VOCAB_ACTIVITY_TYPES = {
    "viewFlashcards", "speakFlashcards",
    "vocabLevel1", "vocabLevel2", "vocabLevel3",
}

# Vietnamese character detection regex
_VIET_RE = re.compile(
    r'[ăâđêôơưàảãáạằẳẵắặầẩẫấậèẻẽéẹềểễếệìỉĩíịòỏõóọồổỗốộờởỡớợùủũúụừửữứựỳỷỹýỵ]',
    re.IGNORECASE,
)


# ── Internal helpers ──

def _collect_all_keys(obj):
    """Recursively collect all keys in a nested dict/list structure."""
    keys = set()
    if isinstance(obj, dict):
        for k, v in obj.items():
            keys.add(k)
            keys |= _collect_all_keys(v)
    elif isinstance(obj, list):
        for item in obj:
            keys |= _collect_all_keys(item)
    return keys


def _get_activity_types(session):
    """Return list of activityType values from a session."""
    return [a.get("activityType") for a in session.get("activities", [])]


def _collect_vocab_from_sessions(sessions, session_indices):
    """Collect vocabList words from viewFlashcards activities in specified sessions."""
    words = []
    for i in session_indices:
        if i >= len(sessions):
            continue
        for act in sessions[i].get("activities", []):
            if act.get("activityType") == "viewFlashcards":
                words.extend(act.get("data", {}).get("vocabList", []))
                break
    return words


def _check_no_strip_keys(content):
    """Check that no strip keys appear anywhere in the content."""
    found = _collect_all_keys(content) & STRIP_KEYS
    if found:
        raise ValueError(f"Strip keys found in content: {found}")


def _check_top_level(content):
    """Check required top-level fields."""
    if not isinstance(content, dict):
        raise ValueError("Content must be a dict")
    if not content.get("title"):
        raise ValueError("Missing or empty top-level 'title'")
    if not content.get("description"):
        raise ValueError("Missing or empty top-level 'description'")
    preview = content.get("preview")
    if not isinstance(preview, dict) or not preview.get("text"):
        raise ValueError("Missing or empty 'preview.text'")
    sessions = content.get("learningSessions")
    if not isinstance(sessions, list) or len(sessions) < 1:
        raise ValueError("'learningSessions' must be a non-empty array")


def _avg_sentence_length(text):
    """Compute average sentence length in words for a reading passage."""
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    if not sentences:
        return 0
    total_words = sum(len(s.split()) for s in sentences)
    return total_words / len(sentences)



# ══════════════════════════════════════════════════════════════
# Public validation functions
# ══════════════════════════════════════════════════════════════


def validate_activity_schema(activity):
    """Validate a single activity against CONTENT_CORRUPTION_RULES.md.

    Checks:
    - activityType field exists (not 'type')
    - activityType is a valid enum value
    - title and description are non-empty strings
    - data field is an object
    - vocabList (not 'words') is a non-empty array of lowercase strings for vocab activities
    - writingSentence has items with targetVocab and prompt
    - writingParagraph has vocabList, instructions, and prompts (≥2)
    - No strip keys present
    """
    if not isinstance(activity, dict):
        raise ValueError("Activity must be a dict")

    # Must use activityType, not type
    if "type" in activity and "activityType" not in activity:
        raise ValueError("Activity uses 'type' instead of 'activityType' — schema violation")
    act_type = activity.get("activityType")
    if not act_type:
        raise ValueError("Activity missing 'activityType'")
    if act_type not in VALID_ACTIVITY_TYPES:
        raise ValueError(f"Invalid activityType '{act_type}'. Valid: {VALID_ACTIVITY_TYPES}")

    if not activity.get("title"):
        raise ValueError(f"Activity '{act_type}' missing 'title'")
    if not isinstance(activity.get("description"), str) or activity.get("description") == "":
        raise ValueError(f"Activity '{act_type}' missing or empty 'description'")

    data = activity.get("data")
    if not isinstance(data, dict):
        raise ValueError(f"Activity '{act_type}' missing 'data' object")

    # Must not use 'words' field
    if "words" in data:
        raise ValueError(f"Activity '{act_type}' uses 'words' instead of 'vocabList' — schema violation")

    # Vocab activities: check vocabList
    if act_type in VOCAB_ACTIVITY_TYPES:
        vocab = data.get("vocabList")
        if not isinstance(vocab, list) or len(vocab) == 0:
            raise ValueError(f"Activity '{act_type}' missing or empty 'data.vocabList'")
        for w in vocab:
            if not isinstance(w, str):
                raise ValueError(f"Activity '{act_type}' vocabList contains non-string: {w}")
            if w != w.lower():
                raise ValueError(f"Activity '{act_type}' vocabList contains non-lowercase: '{w}'")

    # reading/speakReading/readAlong: check data.text
    if act_type in ("reading", "speakReading", "readAlong"):
        if not data.get("text"):
            raise ValueError(f"Activity '{act_type}' missing 'data.text'")

    # introAudio: check data.text
    if act_type == "introAudio":
        if not data.get("text"):
            raise ValueError(f"Activity '{act_type}' missing 'data.text'")

    # writingSentence: check items
    if act_type == "writingSentence":
        vocab = data.get("vocabList")
        if not isinstance(vocab, list) or len(vocab) == 0:
            raise ValueError("writingSentence missing 'data.vocabList'")
        for w in vocab:
            if not isinstance(w, str) or w != w.lower():
                raise ValueError(f"writingSentence vocabList invalid entry: '{w}'")
        items = data.get("items")
        if not isinstance(items, list) or len(items) == 0:
            raise ValueError("writingSentence missing 'data.items'")
        for i, item in enumerate(items):
            if not item.get("targetVocab"):
                raise ValueError(f"writingSentence item[{i}] missing 'targetVocab'")
            if not item.get("prompt"):
                raise ValueError(f"writingSentence item[{i}] missing 'prompt'")

    # writingParagraph: check vocabList, instructions, prompts
    if act_type == "writingParagraph":
        vocab = data.get("vocabList")
        if not isinstance(vocab, list):
            raise ValueError("writingParagraph missing 'data.vocabList'")
        for w in vocab:
            if not isinstance(w, str) or w != w.lower():
                raise ValueError(f"writingParagraph vocabList invalid entry: '{w}'")
        if not data.get("instructions"):
            raise ValueError("writingParagraph missing 'data.instructions'")
        prompts = data.get("prompts")
        if not isinstance(prompts, list) or len(prompts) < 2:
            raise ValueError("writingParagraph 'data.prompts' must be an array of ≥2 strings")
        for p in prompts:
            if not isinstance(p, str) or not p:
                raise ValueError("writingParagraph prompts must be non-empty strings")

    # No strip keys on the activity
    found = _collect_all_keys(activity) & STRIP_KEYS
    if found:
        raise ValueError(f"Activity '{act_type}' contains strip keys: {found}")



def validate_session_vocablist_match(session):
    """Check that viewFlashcards and speakFlashcards in the same session have identical vocabList.

    Only checks sessions that contain both activity types.
    """
    view_vocab = None
    speak_vocab = None

    for act in session.get("activities", []):
        at = act.get("activityType")
        if at == "viewFlashcards":
            view_vocab = act.get("data", {}).get("vocabList", [])
        elif at == "speakFlashcards":
            speak_vocab = act.get("data", {}).get("vocabList", [])

    if view_vocab is not None and speak_vocab is not None:
        if view_vocab != speak_vocab:
            raise ValueError(
                f"viewFlashcards/speakFlashcards vocabList mismatch in session "
                f"'{session.get('title', '?')}': {view_vocab} vs {speak_vocab}"
            )


def validate_content_type_tags(content):
    """Check contentTypeTags is present at top level and is a valid value.

    Valid values: [], ["movie"], ["music"], ["podcast"], ["story"]
    """
    if "contentTypeTags" not in content:
        raise ValueError("Missing 'contentTypeTags' at top level")
    tags = content["contentTypeTags"]
    if tags not in VALID_CONTENT_TYPE_TAGS:
        raise ValueError(
            f"Invalid contentTypeTags: {tags}. "
            f"Valid: {VALID_CONTENT_TYPE_TAGS}"
        )


def validate_bilingual_prompts(content, level):
    """Check Vietnamese in writingSentence prompts for bilingual curriculums.

    For bilingual levels (beginner, preintermediate, intermediate):
    - writingSentence prompt fields must contain Vietnamese characters
    For beginner specifically:
    - prompts must also contain an English example sentence

    Args:
        content: curriculum content dict
        level: one of 'beginner', 'preintermediate', 'intermediate',
               'upperintermediate', 'advanced'
    """
    bilingual_levels = {"beginner", "preintermediate", "intermediate"}
    if level not in bilingual_levels:
        return  # Not bilingual — skip check

    sessions = content.get("learningSessions", [])
    for si, session in enumerate(sessions):
        for ai, act in enumerate(session.get("activities", [])):
            if act.get("activityType") != "writingSentence":
                continue
            items = act.get("data", {}).get("items", [])
            for ii, item in enumerate(items):
                prompt = item.get("prompt", "")
                loc = f"session[{si}].activity[{ai}].item[{ii}]"

                # Check Vietnamese characters in prompt
                if not _VIET_RE.search(prompt):
                    raise ValueError(
                        f"{loc}: writingSentence prompt missing Vietnamese characters "
                        f"(required for {level} bilingual curriculum)"
                    )

                # Beginner: also check for English example
                if level == "beginner":
                    # Heuristic: English example should contain common English words
                    # and be distinguishable from pure Vietnamese
                    ascii_words = re.findall(r'\b[a-zA-Z]{2,}\b', prompt)
                    if len(ascii_words) < 3:
                        raise ValueError(
                            f"{loc}: beginner writingSentence prompt missing English example "
                            f"(need at least a few English words as example)"
                        )



# ══════════════════════════════════════════════════════════════
# Curriculum-type validators
# ══════════════════════════════════════════════════════════════


def validate_balanced_skills_beginner(content):
    """Validate a beginner balanced_skills curriculum.

    Structure: 12 words (2 groups of 6), 4 sessions.
    - S1: introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2,
          reading, speakReading, readAlong, writingSentence (6 words)
    - S2: introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2,
          reading, speakReading, readAlong, writingSentence (6 words)
    - S3 (review): introAudio, viewFlashcards, speakFlashcards, vocabLevel1,
          vocabLevel2, writingSentence (all 12 words)
    - S4 (final reading): introAudio, reading, speakReading, readAlong, introAudio (all words)

    Constraints: no writingParagraph, no vocabLevel3, avg sentence length <15 words.
    """
    _check_top_level(content)
    _check_no_strip_keys(content)

    sessions = content["learningSessions"]

    # 4 sessions
    if len(sessions) != 4:
        raise ValueError(f"Beginner balanced_skills requires 4 sessions, got {len(sessions)}")

    # Check each session has title and activities
    for i, s in enumerate(sessions):
        if not s.get("title"):
            raise ValueError(f"Session {i} missing 'title'")
        if not s.get("activities"):
            raise ValueError(f"Session {i} missing 'activities'")

    # Validate all activities
    for si, s in enumerate(sessions):
        for ai, act in enumerate(s["activities"]):
            validate_activity_schema(act)
        validate_session_vocablist_match(s)

    # Check forbidden activity types
    for si, s in enumerate(sessions):
        for act in s["activities"]:
            at = act["activityType"]
            if at == "writingParagraph":
                raise ValueError(f"Session {si}: writingParagraph forbidden in beginner curriculum")
            if at == "vocabLevel3":
                raise ValueError(f"Session {si}: vocabLevel3 forbidden in beginner curriculum")

    # Expected activity sequences
    expected_s1 = ["introAudio", "viewFlashcards", "speakFlashcards", "vocabLevel1",
                   "vocabLevel2", "reading", "speakReading", "readAlong", "writingSentence"]
    expected_s2 = expected_s1
    expected_s3 = ["introAudio", "viewFlashcards", "speakFlashcards", "vocabLevel1",
                   "vocabLevel2", "writingSentence"]
    expected_s4 = ["introAudio", "reading", "speakReading", "readAlong", "introAudio"]

    for si, expected in enumerate([expected_s1, expected_s2, expected_s3, expected_s4]):
        actual = _get_activity_types(sessions[si])
        if actual != expected:
            raise ValueError(
                f"Session {si} activity sequence mismatch.\n"
                f"  Expected: {expected}\n"
                f"  Got:      {actual}"
            )

    # Vocab word count: 12 words total, 2 groups of 6
    w1 = sessions[0]["activities"][1]["data"]["vocabList"]  # viewFlashcards S1
    w2 = sessions[1]["activities"][1]["data"]["vocabList"]  # viewFlashcards S2
    if len(w1) != 6:
        raise ValueError(f"S1 vocab group must have 6 words, got {len(w1)}")
    if len(w2) != 6:
        raise ValueError(f"S2 vocab group must have 6 words, got {len(w2)}")

    all_words = set(w1 + w2)
    if len(all_words) != 12:
        raise ValueError(f"Total unique vocab must be 12, got {len(all_words)} (overlap detected)")

    # Review session (S3) should have all 12 words
    review_vocab = sessions[2]["activities"][1]["data"]["vocabList"]  # viewFlashcards S3
    if set(review_vocab) != all_words:
        raise ValueError(
            f"Review session vocabList should contain all 12 words. "
            f"Missing: {all_words - set(review_vocab)}"
        )

    # Check average sentence length in reading passages
    for si in [0, 1]:
        for act in sessions[si]["activities"]:
            if act["activityType"] == "reading":
                avg = _avg_sentence_length(act["data"]["text"])
                if avg >= 15:
                    raise ValueError(
                        f"Session {si} reading avg sentence length {avg:.1f} words "
                        f"(must be <15 for beginner)"
                    )



def validate_balanced_skills_standard(content):
    """Validate a preintermediate/intermediate/upperintermediate/advanced balanced_skills curriculum.

    Structure: 18 words (3 groups of 6), 5 sessions.
    - S1-S3: introAudio, introAudio, viewFlashcards, speakFlashcards, vocabLevel1,
             vocabLevel2, introAudio, reading, speakReading, readAlong, writingSentence (6 words each)
    - S4 (review): introAudio, viewFlashcards, speakFlashcards, vocabLevel1,
             vocabLevel2, writingSentence (all 18 words)
    - S5 (final reading): introAudio, reading, speakReading, readAlong,
             writingParagraph, introAudio (all words)
    """
    _check_top_level(content)
    _check_no_strip_keys(content)

    sessions = content["learningSessions"]

    # 5 sessions
    if len(sessions) != 5:
        raise ValueError(f"Standard balanced_skills requires 5 sessions, got {len(sessions)}")

    for i, s in enumerate(sessions):
        if not s.get("title"):
            raise ValueError(f"Session {i} missing 'title'")
        if not s.get("activities"):
            raise ValueError(f"Session {i} missing 'activities'")

    # Validate all activities
    for si, s in enumerate(sessions):
        for act in s["activities"]:
            validate_activity_schema(act)
        validate_session_vocablist_match(s)

    # Expected activity sequences
    expected_learning = [
        "introAudio", "introAudio", "viewFlashcards", "speakFlashcards",
        "vocabLevel1", "vocabLevel2", "introAudio", "reading", "speakReading",
        "readAlong", "writingSentence",
    ]
    expected_review = [
        "introAudio", "viewFlashcards", "speakFlashcards",
        "vocabLevel1", "vocabLevel2", "writingSentence",
    ]
    expected_final = [
        "introAudio", "reading", "speakReading", "readAlong",
        "writingParagraph", "introAudio",
    ]

    for si in range(3):
        actual = _get_activity_types(sessions[si])
        if actual != expected_learning:
            raise ValueError(
                f"Session {si} activity sequence mismatch.\n"
                f"  Expected: {expected_learning}\n"
                f"  Got:      {actual}"
            )

    actual_s4 = _get_activity_types(sessions[3])
    if actual_s4 != expected_review:
        raise ValueError(
            f"Session 3 (review) activity sequence mismatch.\n"
            f"  Expected: {expected_review}\n"
            f"  Got:      {actual_s4}"
        )

    actual_s5 = _get_activity_types(sessions[4])
    if actual_s5 != expected_final:
        raise ValueError(
            f"Session 4 (final reading) activity sequence mismatch.\n"
            f"  Expected: {expected_final}\n"
            f"  Got:      {actual_s5}"
        )

    # Vocab: 18 words, 3 groups of 6
    groups = []
    for si in range(3):
        # viewFlashcards is at index 2 in learning sessions
        vf = sessions[si]["activities"][2]
        vocab = vf["data"]["vocabList"]
        if len(vocab) != 6:
            raise ValueError(f"S{si+1} vocab group must have 6 words, got {len(vocab)}")
        groups.append(vocab)

    all_words = set()
    for g in groups:
        all_words.update(g)
    if len(all_words) != 18:
        raise ValueError(f"Total unique vocab must be 18, got {len(all_words)}")

    # Review session (S4) should have all 18 words
    review_vf = sessions[3]["activities"][1]  # viewFlashcards in review
    if set(review_vf["data"]["vocabList"]) != all_words:
        missing = all_words - set(review_vf["data"]["vocabList"])
        raise ValueError(f"Review session vocabList missing words: {missing}")



def validate_writing_focus_bilingual(content):
    """Validate a bilingual writing_focus curriculum.

    Structure: 10 words (2 groups of 5), 4 sessions.
    - S1: introAudio, introAudio, viewFlashcards, vocabLevel1, vocabLevel2,
          introAudio, reading, readAlong, writingSentence (5 words)
    - S2: introAudio, introAudio, viewFlashcards, vocabLevel1, vocabLevel2,
          introAudio, reading, readAlong, writingSentence (5 words)
    - S3: introAudio, introAudio, viewFlashcards, vocabLevel1, vocabLevel2,
          writingSentence, writingParagraph (all 10 words)
    - S4: introAudio, reading, readAlong, writingParagraph, introAudio (all words)

    Constraints: no speakFlashcards, no speakReading, no vocabLevel3.
    """
    _check_top_level(content)
    _check_no_strip_keys(content)

    sessions = content["learningSessions"]

    if len(sessions) != 4:
        raise ValueError(f"Writing_focus bilingual requires 4 sessions, got {len(sessions)}")

    for i, s in enumerate(sessions):
        if not s.get("title"):
            raise ValueError(f"Session {i} missing 'title'")
        if not s.get("activities"):
            raise ValueError(f"Session {i} missing 'activities'")

    # Validate all activities and check forbidden types
    for si, s in enumerate(sessions):
        for act in s["activities"]:
            validate_activity_schema(act)
            at = act["activityType"]
            if at == "speakFlashcards":
                raise ValueError(f"Session {si}: speakFlashcards forbidden in writing_focus")
            if at == "speakReading":
                raise ValueError(f"Session {si}: speakReading forbidden in writing_focus")
            if at == "vocabLevel3":
                raise ValueError(f"Session {si}: vocabLevel3 forbidden in writing_focus")

    # Expected activity sequences
    expected_s1 = [
        "introAudio", "introAudio", "viewFlashcards", "vocabLevel1", "vocabLevel2",
        "introAudio", "reading", "readAlong", "writingSentence",
    ]
    expected_s2 = expected_s1
    expected_s3 = [
        "introAudio", "introAudio", "viewFlashcards", "vocabLevel1", "vocabLevel2",
        "writingSentence", "writingParagraph",
    ]
    expected_s4 = [
        "introAudio", "reading", "readAlong", "writingParagraph", "introAudio",
    ]

    for si, expected in enumerate([expected_s1, expected_s2, expected_s3, expected_s4]):
        actual = _get_activity_types(sessions[si])
        if actual != expected:
            raise ValueError(
                f"Session {si} activity sequence mismatch.\n"
                f"  Expected: {expected}\n"
                f"  Got:      {actual}"
            )

    # Vocab: 10 words, 2 groups of 5
    # viewFlashcards is at index 2 in S1 and S2
    w1 = sessions[0]["activities"][2]["data"]["vocabList"]
    w2 = sessions[1]["activities"][2]["data"]["vocabList"]
    if len(w1) != 5:
        raise ValueError(f"S1 vocab group must have 5 words, got {len(w1)}")
    if len(w2) != 5:
        raise ValueError(f"S2 vocab group must have 5 words, got {len(w2)}")

    all_words = set(w1 + w2)
    if len(all_words) != 10:
        raise ValueError(f"Total unique vocab must be 10, got {len(all_words)}")

    # S3 viewFlashcards (index 2) should have all 10 words
    review_vocab = sessions[2]["activities"][2]["data"]["vocabList"]
    if set(review_vocab) != all_words:
        missing = all_words - set(review_vocab)
        raise ValueError(f"S3 viewFlashcards vocabList missing words: {missing}")



def validate_speaking_focus(content):
    """Validate a speaking_focus curriculum.

    Structure: 18 words (3 groups of 6), 5 sessions.
    - S1-S3: introAudio, introAudio, viewFlashcards, speakFlashcards, vocabLevel1,
             vocabLevel2, introAudio, reading, speakReading, readAlong, writingSentence (6 words each)
    - S4 (review): introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2 (all 18 words)
    - S5 (final reading): introAudio, reading, speakReading, readAlong, writingSentence,
             introAudio (all words)

    Constraints: speakFlashcards+speakReading in every learning session, no writingParagraph.
    """
    _check_top_level(content)
    _check_no_strip_keys(content)

    sessions = content["learningSessions"]

    if len(sessions) != 5:
        raise ValueError(f"Speaking_focus requires 5 sessions, got {len(sessions)}")

    for i, s in enumerate(sessions):
        if not s.get("title"):
            raise ValueError(f"Session {i} missing 'title'")
        if not s.get("activities"):
            raise ValueError(f"Session {i} missing 'activities'")

    # Validate all activities and check forbidden types
    for si, s in enumerate(sessions):
        for act in s["activities"]:
            validate_activity_schema(act)
            if act["activityType"] == "writingParagraph":
                raise ValueError(f"Session {si}: writingParagraph forbidden in speaking_focus")
        validate_session_vocablist_match(s)

    # Check speakFlashcards and speakReading in every learning session (S1-S3)
    for si in range(3):
        types = _get_activity_types(sessions[si])
        if "speakFlashcards" not in types:
            raise ValueError(f"Session {si}: speakFlashcards required in every learning session")
        if "speakReading" not in types:
            raise ValueError(f"Session {si}: speakReading required in every learning session")

    # Expected activity sequences
    expected_learning = [
        "introAudio", "introAudio", "viewFlashcards", "speakFlashcards",
        "vocabLevel1", "vocabLevel2", "introAudio", "reading", "speakReading",
        "readAlong", "writingSentence",
    ]
    expected_review = [
        "introAudio", "viewFlashcards", "speakFlashcards",
        "vocabLevel1", "vocabLevel2",
    ]
    expected_final = [
        "introAudio", "reading", "speakReading", "readAlong",
        "writingSentence", "introAudio",
    ]

    for si in range(3):
        actual = _get_activity_types(sessions[si])
        if actual != expected_learning:
            raise ValueError(
                f"Session {si} activity sequence mismatch.\n"
                f"  Expected: {expected_learning}\n"
                f"  Got:      {actual}"
            )

    actual_s4 = _get_activity_types(sessions[3])
    if actual_s4 != expected_review:
        raise ValueError(
            f"Session 3 (review) activity sequence mismatch.\n"
            f"  Expected: {expected_review}\n"
            f"  Got:      {actual_s4}"
        )

    actual_s5 = _get_activity_types(sessions[4])
    if actual_s5 != expected_final:
        raise ValueError(
            f"Session 4 (final reading) activity sequence mismatch.\n"
            f"  Expected: {expected_final}\n"
            f"  Got:      {actual_s5}"
        )

    # Vocab: 18 words, 3 groups of 6
    groups = []
    for si in range(3):
        vf = sessions[si]["activities"][2]  # viewFlashcards at index 2
        vocab = vf["data"]["vocabList"]
        if len(vocab) != 6:
            raise ValueError(f"S{si+1} vocab group must have 6 words, got {len(vocab)}")
        groups.append(vocab)

    all_words = set()
    for g in groups:
        all_words.update(g)
    if len(all_words) != 18:
        raise ValueError(f"Total unique vocab must be 18, got {len(all_words)}")

    # Review session (S4) should have all 18 words
    review_vf = sessions[3]["activities"][1]  # viewFlashcards in review
    if set(review_vf["data"]["vocabList"]) != all_words:
        missing = all_words - set(review_vf["data"]["vocabList"])
        raise ValueError(f"Review session vocabList missing words: {missing}")



def validate_vocab_acquisition(content):
    """Validate a vocab_acquisition curriculum.

    Structure: 24 words (4 groups of 6), 6 sessions.
    - S1-S4: introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2,
             vocabLevel3, reading, readAlong (6 words each)
    - S5 (review): introAudio, viewFlashcards, speakFlashcards, vocabLevel1,
             vocabLevel2, vocabLevel3 (all 24 words)
    - S6 (final reading): introAudio, reading, readAlong, introAudio (all words)

    Constraints: vocabLevel1-3 in every learning session, no writingParagraph.
    """
    _check_top_level(content)
    _check_no_strip_keys(content)

    sessions = content["learningSessions"]

    if len(sessions) != 6:
        raise ValueError(f"Vocab_acquisition requires 6 sessions, got {len(sessions)}")

    for i, s in enumerate(sessions):
        if not s.get("title"):
            raise ValueError(f"Session {i} missing 'title'")
        if not s.get("activities"):
            raise ValueError(f"Session {i} missing 'activities'")

    # Validate all activities and check forbidden types
    for si, s in enumerate(sessions):
        for act in s["activities"]:
            validate_activity_schema(act)
            if act["activityType"] == "writingParagraph":
                raise ValueError(f"Session {si}: writingParagraph forbidden in vocab_acquisition")
        validate_session_vocablist_match(s)

    # Check vocabLevel1-3 in every learning session (S1-S4)
    for si in range(4):
        types = _get_activity_types(sessions[si])
        for vl in ["vocabLevel1", "vocabLevel2", "vocabLevel3"]:
            if vl not in types:
                raise ValueError(f"Session {si}: {vl} required in every learning session")

    # Expected activity sequences
    expected_learning = [
        "introAudio", "viewFlashcards", "speakFlashcards",
        "vocabLevel1", "vocabLevel2", "vocabLevel3",
        "reading", "readAlong",
    ]
    expected_review = [
        "introAudio", "viewFlashcards", "speakFlashcards",
        "vocabLevel1", "vocabLevel2", "vocabLevel3",
    ]
    expected_final = [
        "introAudio", "reading", "readAlong", "introAudio",
    ]

    for si in range(4):
        actual = _get_activity_types(sessions[si])
        if actual != expected_learning:
            raise ValueError(
                f"Session {si} activity sequence mismatch.\n"
                f"  Expected: {expected_learning}\n"
                f"  Got:      {actual}"
            )

    actual_s5 = _get_activity_types(sessions[4])
    if actual_s5 != expected_review:
        raise ValueError(
            f"Session 4 (review) activity sequence mismatch.\n"
            f"  Expected: {expected_review}\n"
            f"  Got:      {actual_s5}"
        )

    actual_s6 = _get_activity_types(sessions[5])
    if actual_s6 != expected_final:
        raise ValueError(
            f"Session 5 (final reading) activity sequence mismatch.\n"
            f"  Expected: {expected_final}\n"
            f"  Got:      {actual_s6}"
        )

    # Vocab: 24 words, 4 groups of 6
    groups = []
    for si in range(4):
        vf = sessions[si]["activities"][1]  # viewFlashcards at index 1
        vocab = vf["data"]["vocabList"]
        if len(vocab) != 6:
            raise ValueError(f"S{si+1} vocab group must have 6 words, got {len(vocab)}")
        groups.append(vocab)

    all_words = set()
    for g in groups:
        all_words.update(g)
    if len(all_words) != 24:
        raise ValueError(f"Total unique vocab must be 24, got {len(all_words)}")

    # Review session (S5) should have all 24 words
    review_vf = sessions[4]["activities"][1]  # viewFlashcards in review
    if set(review_vf["data"]["vocabList"]) != all_words:
        missing = all_words - set(review_vf["data"]["vocabList"])
        raise ValueError(f"Review session vocabList missing words: {missing}")



def validate_reader(content):
    """Validate a reader curriculum.

    Structure: 12-18 words, 4 sessions.
    - S1: introAudio, viewFlashcards, vocabLevel1, reading, readAlong, speakReading (6 words)
    - S2: introAudio, viewFlashcards, vocabLevel1, reading, readAlong, speakReading (6 words)
    - S3 (review): introAudio, viewFlashcards, vocabLevel1, vocabLevel2 (all words)
    - S4 (full story): introAudio, reading (≥500 words), readAlong, speakReading, introAudio (all words)

    Constraints: readAlong in every session, final reading ≥500 words, 12-18 total words.
    """
    _check_top_level(content)
    _check_no_strip_keys(content)

    sessions = content["learningSessions"]

    if len(sessions) != 4:
        raise ValueError(f"Reader requires 4 sessions, got {len(sessions)}")

    for i, s in enumerate(sessions):
        if not s.get("title"):
            raise ValueError(f"Session {i} missing 'title'")
        if not s.get("activities"):
            raise ValueError(f"Session {i} missing 'activities'")

    # Validate all activities
    for si, s in enumerate(sessions):
        for act in s["activities"]:
            validate_activity_schema(act)
        validate_session_vocablist_match(s)

    # readAlong must be in every session
    for si, s in enumerate(sessions):
        types = _get_activity_types(s)
        if "readAlong" not in types:
            raise ValueError(f"Session {si}: readAlong required in every session for reader curriculum")

    # Expected activity sequences
    expected_s1 = [
        "introAudio", "viewFlashcards", "vocabLevel1",
        "reading", "readAlong", "speakReading",
    ]
    expected_s2 = expected_s1
    expected_s3 = [
        "introAudio", "viewFlashcards", "vocabLevel1", "vocabLevel2",
    ]
    expected_s4 = [
        "introAudio", "reading", "readAlong", "speakReading", "introAudio",
    ]

    for si, expected in enumerate([expected_s1, expected_s2, expected_s3, expected_s4]):
        actual = _get_activity_types(sessions[si])
        if actual != expected:
            raise ValueError(
                f"Session {si} activity sequence mismatch.\n"
                f"  Expected: {expected}\n"
                f"  Got:      {actual}"
            )

    # Vocab: 12-18 words total
    all_words = set()
    for si in range(2):
        vf = sessions[si]["activities"][1]  # viewFlashcards at index 1
        vocab = vf["data"]["vocabList"]
        all_words.update(vocab)

    total = len(all_words)
    if total < 12 or total > 18:
        raise ValueError(f"Reader requires 12-18 total unique vocab words, got {total}")

    # Final reading (S4) must be ≥500 words
    final_session = sessions[3]
    final_reading_text = None
    for act in final_session["activities"]:
        if act["activityType"] == "reading":
            final_reading_text = act["data"]["text"]
            break

    if not final_reading_text:
        raise ValueError("Final session missing reading activity")

    word_count = len(final_reading_text.split())
    if word_count < 500:
        raise ValueError(
            f"Final reading must be ≥500 words, got {word_count}"
        )
