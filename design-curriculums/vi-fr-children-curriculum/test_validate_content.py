"""
Property-based tests for vi-fr-children-curriculum/validate_content.py

Uses Hypothesis library with minimum 100 iterations per property.
Generates French-style strings with accented characters and multi-word entries.
"""

import sys
import copy
import string

import pytest
from hypothesis import given, settings, assume
from hypothesis import strategies as st

sys.path.insert(0, "vi-fr-children-curriculum")
from validate_content import validate, STRIP_KEYS, VALID_ACTIVITY_TYPES, FORMAT_CONFIG


# ─── Strategies ───────────────────────────────────────────────────────────────

FRENCH_LOWER_CHARS = "abcdefghijklmnopqrstuvwxyzéèêàâçôîùûëïœæ"
FORMATS = ["beginner_mini", "beginner_short", "preintermediate_short"]

# Strategy for a single lowercase French word (with accents)
french_word_st = st.text(
    alphabet=FRENCH_LOWER_CHARS, min_size=2, max_size=12
)

# Strategy for multi-word French entries (with spaces/hyphens)
french_multiword_st = st.one_of(
    french_word_st,
    st.tuples(french_word_st, french_word_st).map(lambda t: f"{t[0]} {t[1]}"),
    st.tuples(french_word_st, french_word_st).map(lambda t: f"{t[0]}-{t[1]}"),
)

format_st = st.sampled_from(FORMATS)


def vocab_list_st(min_size, max_size):
    """Generate a vocabList of unique lowercase French-style strings."""
    return st.lists(
        french_multiword_st,
        min_size=min_size,
        max_size=max_size,
        unique=True,
    )


def make_activity(activity_type, vocab_list=None):
    """Create a valid activity dict for the given type."""
    base = {
        "activityType": activity_type,
        "title": "Tiêu đề hoạt động",
        "description": "Mô tả hoạt động",
        "data": {},
    }
    if activity_type in ("viewFlashcards", "speakFlashcards", "vocabLevel1", "vocabLevel2"):
        base["data"]["vocabList"] = vocab_list or ["rouge", "bleu", "vert"]
    elif activity_type == "introAudio":
        base["data"]["text"] = "Xin chào các bé! Hôm nay chúng ta học tiếng Pháp."
    elif activity_type in ("reading", "speakReading", "readAlong"):
        base["data"]["text"] = "Le ciel est bleu. Le soleil est jaune."
        if activity_type == "reading" and vocab_list:
            base["data"]["vocabList"] = vocab_list
    elif activity_type == "writingSentence":
        base["data"]["vocabList"] = vocab_list or ["rouge", "bleu", "vert"]
        base["data"]["items"] = [
            {"prompt": "Viết câu dùng từ 'rouge'. Ví dụ: Le ballon est rouge.", "targetVocab": "rouge"},
            {"prompt": "Viết câu dùng từ 'bleu'. Ví dụ: Le ciel est bleu.", "targetVocab": "bleu"},
        ]
    return base


def build_valid_content(fmt, vocab_list=None):
    """Build a structurally valid curriculum content dict for the given format."""
    config = FORMAT_CONFIG[fmt]
    session_count = config["session_count"]
    vocab_min = config["vocab_min"]
    forbidden = config["forbidden_activities"]

    if vocab_list is None:
        # Generate a default vocab list of the right size
        default_words = ["rouge", "bleu", "vert", "jaune", "blanc", "noir", "rose",
                         "gris", "orange", "violet", "marron", "beige"]
        vocab_list = default_words[:vocab_min]

    # Determine allowed activity types for this format
    allowed = VALID_ACTIVITY_TYPES - forbidden

    sessions = []
    for i in range(session_count):
        activities = [
            make_activity("introAudio"),
            make_activity("viewFlashcards", vocab_list),
            make_activity("speakFlashcards", vocab_list),
        ]
        # Add vocabLevel1/vocabLevel2 only if allowed
        if "vocabLevel1" in allowed:
            activities.append(make_activity("vocabLevel1", vocab_list))
        if "vocabLevel2" in allowed:
            activities.append(make_activity("vocabLevel2", vocab_list))
        activities.append(make_activity("reading", vocab_list))
        activities.append(make_activity("readAlong"))
        activities.append(make_activity("introAudio"))

        sessions.append({
            "title": f"Phần {i + 1}",
            "activities": activities,
        })

    return {
        "title": "Bài học tiếng Pháp cho bé",
        "description": "Mô tả bài học tiếng Pháp dành cho trẻ em Việt Nam.",
        "preview": {"text": "Giới thiệu bài học tiếng Pháp vui nhộn cho bé."},
        "contentTypeTags": [],
        "learningSessions": sessions,
    }


@st.composite
def valid_curriculum_st(draw):
    """Strategy that generates a valid (format, content) pair."""
    fmt = draw(format_st)
    config = FORMAT_CONFIG[fmt]
    vmin = config["vocab_min"]
    vmax = config["vocab_max"]
    vocab = draw(vocab_list_st(vmin, vmax))
    content = build_valid_content(fmt, vocab)
    return fmt, content


# ─── Property 1: Valid content passes validation ──────────────────────────────
# Feature: vi-fr-children-curriculum, Property 1: Valid content passes validation
# **Validates: Requirements 1.3, 1.4, 1.5, 1.6, 10.1, 10.2, 10.3, 10.4**

@settings(max_examples=100)
@given(data=valid_curriculum_st())
def test_valid_content_passes_validation(data):
    """For any well-formed curriculum content matching its declared format,
    validate() returns without exception."""
    fmt, content = data
    # Should not raise
    validate(content, fmt)


# ─── Property 2: Forbidden activities are rejected per format ─────────────────
# Feature: vi-fr-children-curriculum, Property 2: Forbidden activities are rejected per format
# **Validates: Requirements 3.4, 3.5, 3.6, 10.9**

@settings(max_examples=100)
@given(
    fmt=format_st,
    session_idx=st.integers(min_value=0, max_value=3),
)
def test_forbidden_activities_rejected_writing_paragraph(fmt, session_idx):
    """Injecting writingParagraph into any format raises ValueError."""
    content = build_valid_content(fmt)
    config = FORMAT_CONFIG[fmt]
    idx = min(session_idx, config["session_count"] - 1)
    # Inject forbidden activity
    forbidden_activity = {
        "activityType": "writingParagraph",
        "title": "Viết đoạn văn",
        "description": "Viết đoạn văn tiếng Pháp",
        "data": {"text": "Viết về gia đình"},
    }
    content["learningSessions"][idx]["activities"].append(forbidden_activity)
    with pytest.raises(ValueError):
        validate(content, fmt)


@settings(max_examples=100)
@given(
    fmt=format_st,
    session_idx=st.integers(min_value=0, max_value=3),
)
def test_forbidden_activities_rejected_vocab_level3(fmt, session_idx):
    """Injecting vocabLevel3 into any format raises ValueError."""
    content = build_valid_content(fmt)
    config = FORMAT_CONFIG[fmt]
    idx = min(session_idx, config["session_count"] - 1)
    forbidden_activity = {
        "activityType": "vocabLevel3",
        "title": "Vocab Level 3",
        "description": "Bài tập từ vựng nâng cao",
        "data": {"vocabList": ["rouge", "bleu", "vert"]},
    }
    content["learningSessions"][idx]["activities"].append(forbidden_activity)
    with pytest.raises(ValueError):
        validate(content, fmt)


@settings(max_examples=100)
@given(session_idx=st.integers(min_value=0, max_value=0))
def test_forbidden_activities_rejected_vocab_level1_in_mini(session_idx):
    """Injecting vocabLevel1 into beginner_mini raises ValueError."""
    content = build_valid_content("beginner_mini")
    forbidden_activity = {
        "activityType": "vocabLevel1",
        "title": "Vocab Level 1",
        "description": "Bài tập từ vựng",
        "data": {"vocabList": ["rouge", "bleu", "vert"]},
    }
    content["learningSessions"][0]["activities"].append(forbidden_activity)
    with pytest.raises(ValueError):
        validate(content, "beginner_mini")


@settings(max_examples=100)
@given(session_idx=st.integers(min_value=0, max_value=0))
def test_forbidden_activities_rejected_vocab_level2_in_mini(session_idx):
    """Injecting vocabLevel2 into beginner_mini raises ValueError."""
    content = build_valid_content("beginner_mini")
    forbidden_activity = {
        "activityType": "vocabLevel2",
        "title": "Vocab Level 2",
        "description": "Bài tập từ vựng",
        "data": {"vocabList": ["rouge", "bleu", "vert"]},
    }
    content["learningSessions"][0]["activities"].append(forbidden_activity)
    with pytest.raises(ValueError):
        validate(content, "beginner_mini")


# ─── Property 3: Strip keys are rejected anywhere in the JSON tree ────────────
# Feature: vi-fr-children-curriculum, Property 3: Strip keys are rejected anywhere in the JSON tree
# **Validates: Requirements 1.7, 10.8**

@st.composite
def strip_key_injection_st(draw):
    """Generate a format, valid content, a strip key, and a path to inject it."""
    fmt = draw(format_st)
    content = build_valid_content(fmt)
    strip_key = draw(st.sampled_from(sorted(STRIP_KEYS)))

    config = FORMAT_CONFIG[fmt]
    session_count = config["session_count"]

    # Choose injection depth: top-level, session-level, activity-level, or data-level
    depth = draw(st.sampled_from(["top", "session", "activity", "data"]))
    session_idx = draw(st.integers(min_value=0, max_value=session_count - 1))

    if depth == "top":
        content[strip_key] = "injected"
    elif depth == "session":
        content["learningSessions"][session_idx][strip_key] = "injected"
    elif depth == "activity":
        activities = content["learningSessions"][session_idx]["activities"]
        act_idx = draw(st.integers(min_value=0, max_value=len(activities) - 1))
        activities[act_idx][strip_key] = "injected"
    else:  # data
        activities = content["learningSessions"][session_idx]["activities"]
        act_idx = draw(st.integers(min_value=0, max_value=len(activities) - 1))
        activities[act_idx]["data"][strip_key] = "injected"

    return fmt, content


@settings(max_examples=100)
@given(data=strip_key_injection_st())
def test_strip_keys_rejected_anywhere(data):
    """If a strip key is injected at any depth, validate() raises ValueError."""
    fmt, content = data
    with pytest.raises(ValueError, match="Strip-key"):
        validate(content, fmt)


# ─── Property 4: Activities missing required fields are rejected ──────────────
# Feature: vi-fr-children-curriculum, Property 4: Activities missing required fields are rejected
# **Validates: Requirements 9.1, 9.5, 10.3**

@settings(max_examples=100)
@given(
    fmt=format_st,
    missing_field=st.sampled_from(["activityType", "title", "description", "data"]),
)
def test_activities_missing_required_fields_rejected(fmt, missing_field):
    """Removing any required field from an activity raises ValueError."""
    content = build_valid_content(fmt)
    # Remove the field from the first activity of the first session
    activity = content["learningSessions"][0]["activities"][0]
    if missing_field in activity:
        del activity[missing_field]
    with pytest.raises(ValueError):
        validate(content, fmt)


@settings(max_examples=100)
@given(fmt=format_st)
def test_activity_data_not_dict_rejected(fmt):
    """If data is not a dict, validate() raises ValueError."""
    content = build_valid_content(fmt)
    # Set data to a non-dict value
    content["learningSessions"][0]["activities"][0]["data"] = "not a dict"
    with pytest.raises(ValueError):
        validate(content, fmt)


# ─── Property 5: Invalid activityType values are rejected ────────────────────
# Feature: vi-fr-children-curriculum, Property 5: Invalid activityType values are rejected
# **Validates: Requirements 9.2, 10.4**

@settings(max_examples=100)
@given(
    fmt=format_st,
    invalid_type=st.text(
        alphabet=string.ascii_lowercase + string.digits + "_",
        min_size=3,
        max_size=20,
    ),
)
def test_invalid_activity_type_rejected(fmt, invalid_type):
    """Random strings not in the valid set are rejected as activityType."""
    assume(invalid_type not in VALID_ACTIVITY_TYPES)
    content = build_valid_content(fmt)
    # Replace the first activity's type with an invalid one
    content["learningSessions"][0]["activities"][0]["activityType"] = invalid_type
    with pytest.raises(ValueError):
        validate(content, fmt)


# ─── Property 6: vocabList format is enforced ─────────────────────────────────
# Feature: vi-fr-children-curriculum, Property 6: vocabList format is enforced
# **Validates: Requirements 9.3, 10.5, 14.5**

@settings(max_examples=100)
@given(fmt=st.sampled_from(["beginner_short", "preintermediate_short"]))
def test_vocab_list_non_lowercase_rejected(fmt):
    """Non-lowercase strings in vocabList are rejected."""
    content = build_valid_content(fmt)
    # Find a viewFlashcards activity and inject an uppercase word
    for session in content["learningSessions"]:
        for activity in session["activities"]:
            if activity["activityType"] == "viewFlashcards":
                activity["data"]["vocabList"][0] = "Rouge"  # uppercase R
                break
        break
    with pytest.raises(ValueError):
        validate(content, fmt)


@settings(max_examples=100)
@given(
    fmt=st.sampled_from(["beginner_short", "preintermediate_short"]),
    bad_value=st.sampled_from(["not_a_list", 123, None]),
)
def test_vocab_list_not_array_rejected(fmt, bad_value):
    """Non-array vocabList is rejected."""
    content = build_valid_content(fmt)
    for session in content["learningSessions"]:
        for activity in session["activities"]:
            if activity["activityType"] == "viewFlashcards":
                activity["data"]["vocabList"] = bad_value
                break
        break
    with pytest.raises(ValueError):
        validate(content, fmt)


@settings(max_examples=100)
@given(fmt=st.sampled_from(["beginner_short", "preintermediate_short"]))
def test_vocab_list_empty_array_rejected(fmt):
    """Empty vocabList array is rejected."""
    content = build_valid_content(fmt)
    for session in content["learningSessions"]:
        for activity in session["activities"]:
            if activity["activityType"] == "viewFlashcards":
                activity["data"]["vocabList"] = []
                break
        break
    with pytest.raises(ValueError):
        validate(content, fmt)


@settings(max_examples=100)
@given(fmt=st.sampled_from(["beginner_short", "preintermediate_short"]))
def test_vocab_list_words_field_name_rejected(fmt):
    """Using 'words' instead of 'vocabList' is rejected."""
    content = build_valid_content(fmt)
    for session in content["learningSessions"]:
        for activity in session["activities"]:
            if activity["activityType"] == "viewFlashcards":
                vocab = activity["data"].pop("vocabList")
                activity["data"]["words"] = vocab
                break
        break
    with pytest.raises(ValueError):
        validate(content, fmt)


# ─── Property 7: Flashcard vocabList consistency within sessions ──────────────
# Feature: vi-fr-children-curriculum, Property 7: Flashcard vocabList consistency within sessions
# **Validates: Requirements 9.4, 10.6**

@settings(max_examples=100)
@given(
    fmt=format_st,
    extra_word=french_multiword_st,
)
def test_flashcard_vocab_list_inconsistency_rejected(fmt, extra_word):
    """viewFlashcards and speakFlashcards with different vocabList raises ValueError."""
    content = build_valid_content(fmt)
    # Find the first session with both viewFlashcards and speakFlashcards
    for session in content["learningSessions"]:
        view_found = False
        speak_found = False
        for activity in session["activities"]:
            if activity["activityType"] == "viewFlashcards":
                view_found = True
            elif activity["activityType"] == "speakFlashcards":
                speak_found = True
                # Modify speakFlashcards vocabList to differ
                activity["data"]["vocabList"] = activity["data"]["vocabList"] + [extra_word]
        if view_found and speak_found:
            break
    with pytest.raises(ValueError):
        validate(content, fmt)


# ─── Property 8: writingSentence structure is enforced ────────────────────────
# Feature: vi-fr-children-curriculum, Property 8: writingSentence structure is enforced
# **Validates: Requirements 9.6, 10.7**

def _build_content_with_writing_sentence(fmt):
    """Build content that includes a writingSentence activity (for short/preintermediate)."""
    # Only beginner_short and preintermediate_short allow writingSentence
    # and have enough sessions to include it
    config = FORMAT_CONFIG[fmt]
    vocab_min = config["vocab_min"]
    default_words = ["rouge", "bleu", "vert", "jaune", "blanc", "noir", "rose",
                     "gris", "orange", "violet", "marron", "beige"]
    vocab_list = default_words[:vocab_min]
    content = build_valid_content(fmt, vocab_list)

    # Add a writingSentence activity to the last session
    last_session = content["learningSessions"][-1]
    ws_activity = make_activity("writingSentence", vocab_list)
    last_session["activities"].insert(-1, ws_activity)  # before last introAudio
    return content, vocab_list


@settings(max_examples=100)
@given(fmt=st.sampled_from(["beginner_short", "preintermediate_short"]))
def test_writing_sentence_missing_vocab_list_rejected(fmt):
    """writingSentence without data.vocabList raises ValueError."""
    content, _ = _build_content_with_writing_sentence(fmt)
    # Find the writingSentence activity and remove vocabList
    for session in content["learningSessions"]:
        for activity in session["activities"]:
            if activity["activityType"] == "writingSentence":
                del activity["data"]["vocabList"]
                break
    with pytest.raises(ValueError):
        validate(content, fmt)


@settings(max_examples=100)
@given(fmt=st.sampled_from(["beginner_short", "preintermediate_short"]))
def test_writing_sentence_missing_items_rejected(fmt):
    """writingSentence without data.items raises ValueError."""
    content, _ = _build_content_with_writing_sentence(fmt)
    for session in content["learningSessions"]:
        for activity in session["activities"]:
            if activity["activityType"] == "writingSentence":
                del activity["data"]["items"]
                break
    with pytest.raises(ValueError):
        validate(content, fmt)


@settings(max_examples=100)
@given(
    fmt=st.sampled_from(["beginner_short", "preintermediate_short"]),
    missing_field=st.sampled_from(["prompt", "targetVocab"]),
)
def test_writing_sentence_items_missing_fields_rejected(fmt, missing_field):
    """writingSentence items without prompt or targetVocab raises ValueError."""
    content, _ = _build_content_with_writing_sentence(fmt)
    for session in content["learningSessions"]:
        for activity in session["activities"]:
            if activity["activityType"] == "writingSentence":
                # Remove the field from the first item
                del activity["data"]["items"][0][missing_field]
                break
    with pytest.raises(ValueError):
        validate(content, fmt)
