"""
Property-based tests for validate_content.py — Property 10: Validator rejects invalid content with specific message

# Feature: bilingual-parity-expansion, Property 10: Validator rejects invalid content with specific message

Tests that the validator always raises ValueError (not any other exception) with a
non-empty message identifying the specific violation, for various types of invalid
curriculum JSON at both beginner and standard levels.

**Validates: Requirements 11.2**
"""

import copy
import pytest
from hypothesis import given, settings, assume
from hypothesis import strategies as st

import sys
import os

# Ensure the repo root is on the path so we can import validate_content and helpers
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from validate_content import validate

# Import helpers from property 1 test
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from test_property_1_top_level_structure import (
    make_valid_beginner_curriculum,
    make_valid_standard_curriculum,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

level_strategy = st.sampled_from(["beginner", "standard"])


def _get_valid_curriculum(level):
    """Return a deep copy of a valid curriculum for the given level."""
    if level == "beginner":
        return copy.deepcopy(make_valid_beginner_curriculum())
    return copy.deepcopy(make_valid_standard_curriculum())


def _assert_value_error_with_message(content, level):
    """Assert that validate raises ValueError with a non-empty, meaningful message."""
    with pytest.raises(ValueError) as exc_info:
        validate(content, level=level)
    msg = str(exc_info.value)
    assert len(msg) > 0, "ValueError message must be non-empty"
    # Message should contain at least one alphabetic word (meaningful text)
    assert any(c.isalpha() for c in msg), (
        f"ValueError message must contain meaningful text, got: {msg!r}"
    )


# ---------------------------------------------------------------------------
# Sanity: valid curriculums pass (no ValueError)
# ---------------------------------------------------------------------------

def test_valid_beginner_passes():
    validate(make_valid_beginner_curriculum(), level="beginner")


def test_valid_standard_passes():
    validate(make_valid_standard_curriculum(), level="standard")


# ---------------------------------------------------------------------------
# Property 10: Validator rejects invalid content with specific message
# Feature: bilingual-parity-expansion, Property 10: Validator rejects invalid content with specific message
# **Validates: Requirements 11.2**
# ---------------------------------------------------------------------------

# --- 10a: Missing top-level fields ---

@settings(max_examples=100)
@given(
    level=level_strategy,
    field=st.sampled_from(["title", "description", "preview", "contentTypeTags", "learningSessions"]),
)
def test_missing_top_level_field_raises_valueerror_with_message(level, field):
    """
    Property 10a: Removing any required top-level field raises ValueError
    with a non-empty message identifying the violation.

    # Feature: bilingual-parity-expansion, Property 10: Validator rejects invalid content with specific message
    **Validates: Requirements 11.2**
    """
    content = _get_valid_curriculum(level)
    del content[field]
    _assert_value_error_with_message(content, level)


# --- 10b: Wrong types for top-level fields ---

@settings(max_examples=100)
@given(
    level=level_strategy,
    field=st.sampled_from(["title", "description"]),
    bad_value=st.one_of(
        st.just(None),
        st.just(""),
        st.just("   "),
        st.just(42),
        st.just([]),
        st.just({}),
        st.just(False),
    ),
)
def test_bad_top_level_string_raises_valueerror_with_message(level, field, bad_value):
    """
    Property 10b: Setting title or description to invalid values raises ValueError
    with a non-empty message.

    # Feature: bilingual-parity-expansion, Property 10: Validator rejects invalid content with specific message
    **Validates: Requirements 11.2**
    """
    content = _get_valid_curriculum(level)
    content[field] = bad_value
    _assert_value_error_with_message(content, level)


# --- 10c: Wrong session counts ---

@settings(max_examples=100)
@given(level=level_strategy)
def test_wrong_session_count_raises_valueerror_with_message(level):
    """
    Property 10c: Having the wrong number of sessions for the level raises ValueError
    with a non-empty message.

    # Feature: bilingual-parity-expansion, Property 10: Validator rejects invalid content with specific message
    **Validates: Requirements 11.2**
    """
    content = _get_valid_curriculum(level)
    # Remove one session to make the count wrong
    content["learningSessions"] = content["learningSessions"][:-1]
    _assert_value_error_with_message(content, level)


# --- 10d: Forbidden activities in beginner ---

@settings(max_examples=100)
@given(forbidden=st.sampled_from(["writingParagraph", "vocabLevel3"]))
def test_forbidden_beginner_activity_raises_valueerror_with_message(forbidden):
    """
    Property 10d: Including writingParagraph or vocabLevel3 in a beginner curriculum
    raises ValueError with a non-empty message.

    # Feature: bilingual-parity-expansion, Property 10: Validator rejects invalid content with specific message
    **Validates: Requirements 11.2**
    """
    content = make_valid_beginner_curriculum()
    # Inject a forbidden activity into the first learning session
    if forbidden == "writingParagraph":
        bad_activity = {
            "activityType": "writingParagraph",
            "title": "Write paragraph",
            "description": "Write a paragraph",
            "data": {
                "vocabList": ["apple", "house"],
                "instructions": "Write about the topic",
                "prompts": ["First prompt", "Second prompt"],
            },
        }
    else:
        bad_activity = {
            "activityType": "vocabLevel3",
            "title": "Vocab Level 3",
            "description": "Advanced vocab drill",
            "data": {"vocabList": ["apple", "house", "garden", "river", "bridge", "forest"]},
        }
    content["learningSessions"][0]["activities"].append(bad_activity)
    _assert_value_error_with_message(content, "beginner")


# --- 10e: 'type' instead of 'activityType' ---

@settings(max_examples=100)
@given(level=level_strategy)
def test_type_instead_of_activitytype_raises_valueerror_with_message(level):
    """
    Property 10e: Using 'type' instead of 'activityType' on an activity raises ValueError
    with a non-empty message.

    # Feature: bilingual-parity-expansion, Property 10: Validator rejects invalid content with specific message
    **Validates: Requirements 11.2**
    """
    content = _get_valid_curriculum(level)
    activity = content["learningSessions"][0]["activities"][0]
    activity["type"] = activity.pop("activityType")
    _assert_value_error_with_message(content, level)


# --- 10f: Invalid activityType value ---

@settings(max_examples=100)
@given(
    level=level_strategy,
    bad_type=st.text(min_size=1, max_size=20).filter(
        lambda s: s not in {
            "introAudio", "viewFlashcards", "speakFlashcards",
            "vocabLevel1", "vocabLevel2", "vocabLevel3",
            "reading", "speakReading", "readAlong",
            "writingSentence", "writingParagraph",
        }
    ),
)
def test_invalid_activitytype_value_raises_valueerror_with_message(level, bad_type):
    """
    Property 10f: Using an invalid activityType value raises ValueError
    with a non-empty message.

    # Feature: bilingual-parity-expansion, Property 10: Validator rejects invalid content with specific message
    **Validates: Requirements 11.2**
    """
    content = _get_valid_curriculum(level)
    content["learningSessions"][0]["activities"][0]["activityType"] = bad_type
    _assert_value_error_with_message(content, level)


# --- 10g: 'words' instead of 'vocabList' ---

@settings(max_examples=100)
@given(level=level_strategy)
def test_words_instead_of_vocablist_raises_valueerror_with_message(level):
    """
    Property 10g: Using 'words' instead of 'vocabList' on a vocab activity raises ValueError
    with a non-empty message.

    # Feature: bilingual-parity-expansion, Property 10: Validator rejects invalid content with specific message
    **Validates: Requirements 11.2**
    """
    content = _get_valid_curriculum(level)
    # Find the first viewFlashcards activity and rename vocabList to words
    for session in content["learningSessions"]:
        for activity in session["activities"]:
            if activity["activityType"] == "viewFlashcards":
                activity["data"]["words"] = activity["data"].pop("vocabList")
                _assert_value_error_with_message(content, level)
                return


# --- 10h: Uppercase vocab words ---

@settings(max_examples=100)
@given(
    level=level_strategy,
    upper_word=st.text(
        alphabet=st.characters(whitelist_categories=("Lu",)),
        min_size=1,
        max_size=10,
    ),
)
def test_uppercase_vocab_raises_valueerror_with_message(level, upper_word):
    """
    Property 10h: Having uppercase characters in vocabList raises ValueError
    with a non-empty message.

    # Feature: bilingual-parity-expansion, Property 10: Validator rejects invalid content with specific message
    **Validates: Requirements 11.2**
    """
    assume(upper_word != upper_word.lower())
    content = _get_valid_curriculum(level)
    # Replace the first word in the first viewFlashcards vocabList
    for session in content["learningSessions"]:
        for activity in session["activities"]:
            if activity["activityType"] == "viewFlashcards":
                activity["data"]["vocabList"][0] = upper_word
                # Also update speakFlashcards to keep them consistent
                # (otherwise flashcard mismatch fires first)
                for act2 in session["activities"]:
                    if act2["activityType"] == "speakFlashcards":
                        act2["data"]["vocabList"][0] = upper_word
                _assert_value_error_with_message(content, level)
                return


# --- 10i: Mismatched flashcard vocabLists ---

@settings(max_examples=100)
@given(level=level_strategy)
def test_mismatched_flashcards_raises_valueerror_with_message(level):
    """
    Property 10i: Having mismatched viewFlashcards/speakFlashcards vocabLists
    raises ValueError with a non-empty message.

    # Feature: bilingual-parity-expansion, Property 10: Validator rejects invalid content with specific message
    **Validates: Requirements 11.2**
    """
    content = _get_valid_curriculum(level)
    # Reverse the speakFlashcards vocabList in the first learning session
    for activity in content["learningSessions"][0]["activities"]:
        if activity["activityType"] == "speakFlashcards":
            activity["data"]["vocabList"] = list(reversed(activity["data"]["vocabList"]))
            break
    _assert_value_error_with_message(content, level)


# --- 10j: Strip keys injected at various depths ---

@settings(max_examples=100)
@given(
    level=level_strategy,
    strip_key=st.sampled_from([
        "mp3Url", "illustrationSet", "chapterBookmarks", "segments",
        "whiteboardItems", "userReadingId", "lessonUniqueId",
        "curriculumTags", "taskId", "imageId",
    ]),
    depth=st.sampled_from(["top", "session", "activity", "data"]),
)
def test_strip_key_injection_raises_valueerror_with_message(level, strip_key, depth):
    """
    Property 10j: Injecting any strip key at any depth raises ValueError
    with a non-empty message.

    # Feature: bilingual-parity-expansion, Property 10: Validator rejects invalid content with specific message
    **Validates: Requirements 11.2**
    """
    content = _get_valid_curriculum(level)
    if depth == "top":
        content[strip_key] = "injected"
    elif depth == "session":
        content["learningSessions"][0][strip_key] = "injected"
    elif depth == "activity":
        content["learningSessions"][0]["activities"][0][strip_key] = "injected"
    elif depth == "data":
        content["learningSessions"][0]["activities"][0]["data"][strip_key] = "injected"
    _assert_value_error_with_message(content, level)


# --- 10k: Missing activity fields ---

@settings(max_examples=100)
@given(
    level=level_strategy,
    missing_field=st.sampled_from(["title", "description", "data"]),
)
def test_missing_activity_field_raises_valueerror_with_message(level, missing_field):
    """
    Property 10k: Removing a required field from an activity raises ValueError
    with a non-empty message.

    # Feature: bilingual-parity-expansion, Property 10: Validator rejects invalid content with specific message
    **Validates: Requirements 11.2**
    """
    content = _get_valid_curriculum(level)
    activity = content["learningSessions"][0]["activities"][0]
    if missing_field in activity:
        del activity[missing_field]
    _assert_value_error_with_message(content, level)


# --- 10l: Writing activity with missing data fields ---

@settings(max_examples=100)
@given(
    level=level_strategy,
    missing_field=st.sampled_from(["vocabList", "items"]),
)
def test_writing_sentence_missing_data_raises_valueerror_with_message(level, missing_field):
    """
    Property 10l: Removing required data fields from a writingSentence activity
    raises ValueError with a non-empty message.

    # Feature: bilingual-parity-expansion, Property 10: Validator rejects invalid content with specific message
    **Validates: Requirements 11.2**
    """
    content = _get_valid_curriculum(level)
    # Find the first writingSentence activity
    for session in content["learningSessions"]:
        for activity in session["activities"]:
            if activity["activityType"] == "writingSentence":
                if missing_field in activity["data"]:
                    del activity["data"][missing_field]
                    _assert_value_error_with_message(content, level)
                return


# --- 10m: writingParagraph missing data fields (standard only) ---

@settings(max_examples=100)
@given(missing_field=st.sampled_from(["vocabList", "instructions", "prompts"]))
def test_writing_paragraph_missing_data_raises_valueerror_with_message(missing_field):
    """
    Property 10m: Removing required data fields from a writingParagraph activity
    in a standard curriculum raises ValueError with a non-empty message.

    # Feature: bilingual-parity-expansion, Property 10: Validator rejects invalid content with specific message
    **Validates: Requirements 11.2**
    """
    content = make_valid_standard_curriculum()
    # Find the writingParagraph in the final session
    for activity in content["learningSessions"][-1]["activities"]:
        if activity["activityType"] == "writingParagraph":
            if missing_field in activity["data"]:
                del activity["data"][missing_field]
                _assert_value_error_with_message(content, "standard")
            return


# --- 10n: Non-dict content ---

@settings(max_examples=100)
@given(
    level=level_strategy,
    bad_content=st.one_of(
        st.just(None),
        st.just("a string"),
        st.just(42),
        st.just([]),
        st.just(True),
    ),
)
def test_non_dict_content_raises_valueerror_with_message(level, bad_content):
    """
    Property 10n: Passing non-dict content raises ValueError with a non-empty message.

    # Feature: bilingual-parity-expansion, Property 10: Validator rejects invalid content with specific message
    **Validates: Requirements 11.2**
    """
    _assert_value_error_with_message(bad_content, level)


# --- 10o: Wrong vocab count (too few unique words) ---

@settings(max_examples=100)
@given(level=level_strategy)
def test_wrong_vocab_count_raises_valueerror_with_message(level):
    """
    Property 10o: Having the wrong number of unique vocabulary words raises ValueError
    with a non-empty message.

    # Feature: bilingual-parity-expansion, Property 10: Validator rejects invalid content with specific message
    **Validates: Requirements 11.2**
    """
    content = _get_valid_curriculum(level)
    # Make the second learning session reuse words from the first session
    # (reducing unique word count)
    first_session_vocab = content["learningSessions"][0]["activities"][1]["data"]["vocabList"]
    for activity in content["learningSessions"][1]["activities"]:
        if "vocabList" in activity.get("data", {}):
            activity["data"]["vocabList"] = list(first_session_vocab)
    _assert_value_error_with_message(content, level)
