"""
Property-based tests for validate_content.py — Property 6: VocabList format enforcement

# Feature: bilingual-parity-expansion, Property 6: VocabList format enforcement

Tests that the validator rejects vocab activities with uppercase strings, non-string
elements, `words` field name instead of `vocabList`, and empty vocabList arrays —
for BOTH beginner and standard levels.

**Validates: Requirements 5.7, 5.8, 11.7**
"""

import copy
import pytest
from hypothesis import given, settings, assume
from hypothesis import strategies as st

import sys
import os

# Ensure the repo root is on the path so we can import validate_content
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from validate_content import validate

# Reuse helpers from property 1 tests
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from test_property_1_top_level_structure import (
    make_valid_beginner_curriculum,
    make_valid_standard_curriculum,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

level_strategy = st.sampled_from(["beginner", "standard"])

# Vocab activity types present in beginner curriculums (no vocabLevel3)
BEGINNER_VOCAB_TYPES = ["viewFlashcards", "speakFlashcards", "vocabLevel1", "vocabLevel2"]

# Vocab activity types present in standard curriculums (includes vocabLevel3)
STANDARD_VOCAB_TYPES = ["viewFlashcards", "speakFlashcards", "vocabLevel1", "vocabLevel2", "vocabLevel3"]


def _get_valid_curriculum(level):
    """Return a deep copy of a valid curriculum for the given level."""
    if level == "beginner":
        return copy.deepcopy(make_valid_beginner_curriculum())
    return copy.deepcopy(make_valid_standard_curriculum())


def _get_learning_session_indices(level):
    """Return the indices of learning sessions (not review/final) for the level."""
    if level == "beginner":
        return [0, 1]  # 2 learning sessions
    return [0, 1, 2]  # 3 learning sessions


def _get_vocab_activity_types(level):
    """Return the vocab activity types available for the given level."""
    if level == "beginner":
        return BEGINNER_VOCAB_TYPES
    return STANDARD_VOCAB_TYPES


def _find_vocab_activity_in_session(session, activity_type):
    """Find the index of a specific vocab activity in a session's activities list."""
    for i, activity in enumerate(session.get("activities", [])):
        if activity.get("activityType") == activity_type:
            return i
    return None


# Strategy: generate a string that contains at least one uppercase character
uppercase_string_strategy = st.text(
    alphabet=st.sampled_from("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"),
    min_size=1,
    max_size=20,
).filter(lambda s: s != s.lower())

# Strategy: generate non-string elements that should be rejected in vocabList
non_string_element_strategy = st.one_of(
    st.integers(min_value=-100, max_value=100),
    st.just(True),
    st.just(False),
    st.just(None),
    st.just([]),
    st.just(["nested"]),
    st.just({}),
    st.just({"key": "value"}),
)


# ---------------------------------------------------------------------------
# Sanity: base curriculums pass validation
# ---------------------------------------------------------------------------

def test_valid_beginner_curriculum_passes():
    """Sanity check: beginner curriculum with valid vocabLists passes."""
    validate(make_valid_beginner_curriculum(), level="beginner")


def test_valid_standard_curriculum_passes():
    """Sanity check: standard curriculum with valid vocabLists passes."""
    validate(make_valid_standard_curriculum(), level="standard")


# ---------------------------------------------------------------------------
# Property 6a: Uppercase strings in vocabList are rejected
# Feature: bilingual-parity-expansion, Property 6: VocabList format enforcement
# **Validates: Requirements 5.7, 5.8, 11.7**
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(
    level=level_strategy,
    uppercase_word=uppercase_string_strategy,
)
def test_rejects_uppercase_strings_in_vocablist(level, uppercase_word):
    """
    Property 6a: Validator rejects vocab activities where vocabList contains
    uppercase strings, at both beginner and standard levels.

    For any vocab activity where any element in vocabList is not fully lowercase,
    the validator SHALL raise ValueError mentioning 'lowercase'.

    # Feature: bilingual-parity-expansion, Property 6: VocabList format enforcement
    **Validates: Requirements 5.7, 5.8, 11.7**
    """
    content = _get_valid_curriculum(level)
    session_indices = _get_learning_session_indices(level)
    vocab_types = _get_vocab_activity_types(level)

    # Pick the first learning session and first vocab activity type to corrupt
    session_idx = session_indices[0]
    session = content["learningSessions"][session_idx]

    # Replace the first word in all vocab activities in this session with the uppercase word
    for activity in session["activities"]:
        if activity.get("activityType") in vocab_types:
            activity["data"]["vocabList"][0] = uppercase_word

    with pytest.raises(ValueError, match="lowercase"):
        validate(content, level=level)


# ---------------------------------------------------------------------------
# Property 6b: Non-string elements in vocabList are rejected
# Feature: bilingual-parity-expansion, Property 6: VocabList format enforcement
# **Validates: Requirements 5.7, 5.8, 11.7**
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(
    level=level_strategy,
    bad_element=non_string_element_strategy,
)
def test_rejects_non_string_elements_in_vocablist(level, bad_element):
    """
    Property 6b: Validator rejects vocab activities where vocabList contains
    non-string elements (ints, bools, lists, dicts, None), at both beginner
    and standard levels.

    For any vocab activity where any element in vocabList is not a string,
    the validator SHALL raise ValueError mentioning 'string'.

    # Feature: bilingual-parity-expansion, Property 6: VocabList format enforcement
    **Validates: Requirements 5.7, 5.8, 11.7**
    """
    content = _get_valid_curriculum(level)
    session_indices = _get_learning_session_indices(level)
    vocab_types = _get_vocab_activity_types(level)

    # Pick the first learning session and inject the bad element
    session_idx = session_indices[0]
    session = content["learningSessions"][session_idx]

    for activity in session["activities"]:
        if activity.get("activityType") in vocab_types:
            activity["data"]["vocabList"][0] = bad_element

    with pytest.raises(ValueError, match="string"):
        validate(content, level=level)


# ---------------------------------------------------------------------------
# Property 6c: Using 'words' field name instead of 'vocabList' is rejected
# Feature: bilingual-parity-expansion, Property 6: VocabList format enforcement
# **Validates: Requirements 5.7, 5.8, 11.7**
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(
    level=level_strategy,
    vocab_type_idx=st.integers(min_value=0, max_value=3),
)
def test_rejects_words_field_name_instead_of_vocablist(level, vocab_type_idx):
    """
    Property 6c: Validator rejects vocab activities that use 'words' as the
    field name instead of 'vocabList', at both beginner and standard levels.

    For any vocab activity where the data uses 'words' instead of 'vocabList',
    the validator SHALL raise ValueError mentioning 'words' or 'vocabList'.

    # Feature: bilingual-parity-expansion, Property 6: VocabList format enforcement
    **Validates: Requirements 5.7, 5.8, 11.7**
    """
    content = _get_valid_curriculum(level)
    session_indices = _get_learning_session_indices(level)
    vocab_types = _get_vocab_activity_types(level)

    # Clamp the index to available vocab types
    actual_idx = vocab_type_idx % len(vocab_types)
    target_type = vocab_types[actual_idx]

    # Pick the first learning session
    session_idx = session_indices[0]
    session = content["learningSessions"][session_idx]

    for activity in session["activities"]:
        if activity.get("activityType") == target_type:
            # Rename vocabList to words
            vocab_data = activity["data"].pop("vocabList")
            activity["data"]["words"] = vocab_data
            break

    with pytest.raises(ValueError, match="words"):
        validate(content, level=level)


# ---------------------------------------------------------------------------
# Property 6d: Empty vocabList arrays are rejected
# Feature: bilingual-parity-expansion, Property 6: VocabList format enforcement
# **Validates: Requirements 5.7, 5.8, 11.7**
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(
    level=level_strategy,
    vocab_type_idx=st.integers(min_value=0, max_value=3),
)
def test_rejects_empty_vocablist_arrays(level, vocab_type_idx):
    """
    Property 6d: Validator rejects vocab activities where vocabList is an
    empty array, at both beginner and standard levels.

    For any vocab activity where vocabList is [], the validator SHALL raise
    ValueError mentioning 'vocabList' and 'non-empty'.

    # Feature: bilingual-parity-expansion, Property 6: VocabList format enforcement
    **Validates: Requirements 5.7, 5.8, 11.7**
    """
    content = _get_valid_curriculum(level)
    session_indices = _get_learning_session_indices(level)
    vocab_types = _get_vocab_activity_types(level)

    actual_idx = vocab_type_idx % len(vocab_types)
    target_type = vocab_types[actual_idx]

    # Pick the first learning session
    session_idx = session_indices[0]
    session = content["learningSessions"][session_idx]

    for activity in session["activities"]:
        if activity.get("activityType") == target_type:
            activity["data"]["vocabList"] = []
            break

    with pytest.raises(ValueError, match="non-empty"):
        validate(content, level=level)
