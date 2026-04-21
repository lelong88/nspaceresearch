"""
Property-based tests for validate_content.py — Property 8: Writing activity structure

# Feature: bilingual-parity-expansion, Property 8: Writing activity structure

Tests that the validator rejects writingSentence and writingParagraph activities
with missing or malformed data fields.

- writingSentence: requires data.vocabList, data.items (non-empty array),
  each item with non-empty prompt and targetVocab strings
- writingParagraph: requires data.vocabList, data.instructions (non-empty string),
  data.prompts (array of strings with length >= 2)

Beginner level only has writingSentence; standard level has both.

**Validates: Requirements 11.11**
"""

import copy
import pytest
from hypothesis import given, settings, assume
from hypothesis import strategies as st

import sys
import os

# Ensure the repo root is on the path so we can import validate_content
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
# Ensure the tests directory is on the path so we can import helpers
sys.path.insert(0, os.path.dirname(__file__))
from validate_content import validate

# Import helpers from property 1 tests
from test_property_1_top_level_structure import (
    make_valid_beginner_curriculum,
    make_valid_standard_curriculum,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _get_valid_curriculum(level):
    """Return a deep copy of a valid curriculum for the given level."""
    if level == "beginner":
        return copy.deepcopy(make_valid_beginner_curriculum())
    return copy.deepcopy(make_valid_standard_curriculum())


def _find_activity(content, activity_type):
    """Find the first activity of the given type and return (session_idx, activity_idx, activity)."""
    for si, session in enumerate(content["learningSessions"]):
        for ai, activity in enumerate(session.get("activities", [])):
            if activity.get("activityType") == activity_type:
                return si, ai, activity
    return None, None, None


# Strategies
level_strategy = st.sampled_from(["beginner", "standard"])

bad_string_values = st.one_of(
    st.just(None),
    st.just(""),
    st.just("   "),
    st.just(0),
    st.just(False),
    st.just([]),
    st.just({}),
)


# ---------------------------------------------------------------------------
# Sanity: valid curriculums pass
# ---------------------------------------------------------------------------

def test_valid_beginner_passes():
    """Beginner curriculum with valid writingSentence passes."""
    validate(make_valid_beginner_curriculum(), level="beginner")


def test_valid_standard_passes():
    """Standard curriculum with valid writingSentence and writingParagraph passes."""
    validate(make_valid_standard_curriculum(), level="standard")


# ===========================================================================
# writingSentence tests (both beginner and standard)
# ===========================================================================

# Feature: bilingual-parity-expansion, Property 8: Writing activity structure

@settings(max_examples=100)
@given(level=level_strategy)
def test_writing_sentence_rejects_missing_vocab_list(level):
    """
    Property 8a: writingSentence missing data.vocabList is rejected.

    # Feature: bilingual-parity-expansion, Property 8: Writing activity structure
    **Validates: Requirements 11.11**
    """
    content = _get_valid_curriculum(level)
    si, ai, activity = _find_activity(content, "writingSentence")
    assume(activity is not None)

    del activity["data"]["vocabList"]

    with pytest.raises(ValueError, match="vocabList"):
        validate(content, level=level)


@settings(max_examples=100)
@given(level=level_strategy)
def test_writing_sentence_rejects_missing_items(level):
    """
    Property 8b: writingSentence missing data.items is rejected.

    # Feature: bilingual-parity-expansion, Property 8: Writing activity structure
    **Validates: Requirements 11.11**
    """
    content = _get_valid_curriculum(level)
    si, ai, activity = _find_activity(content, "writingSentence")
    assume(activity is not None)

    del activity["data"]["items"]

    with pytest.raises(ValueError, match="items"):
        validate(content, level=level)


@settings(max_examples=100)
@given(level=level_strategy)
def test_writing_sentence_rejects_empty_items(level):
    """
    Property 8c: writingSentence with empty data.items array is rejected.

    # Feature: bilingual-parity-expansion, Property 8: Writing activity structure
    **Validates: Requirements 11.11**
    """
    content = _get_valid_curriculum(level)
    si, ai, activity = _find_activity(content, "writingSentence")
    assume(activity is not None)

    activity["data"]["items"] = []

    with pytest.raises(ValueError, match="items"):
        validate(content, level=level)


@settings(max_examples=100)
@given(level=level_strategy)
def test_writing_sentence_rejects_item_missing_prompt(level):
    """
    Property 8d: writingSentence item missing prompt field is rejected.

    # Feature: bilingual-parity-expansion, Property 8: Writing activity structure
    **Validates: Requirements 11.11**
    """
    content = _get_valid_curriculum(level)
    si, ai, activity = _find_activity(content, "writingSentence")
    assume(activity is not None)

    # Remove prompt from the first item
    del activity["data"]["items"][0]["prompt"]

    with pytest.raises(ValueError, match="prompt"):
        validate(content, level=level)


@settings(max_examples=100)
@given(level=level_strategy)
def test_writing_sentence_rejects_item_missing_target_vocab(level):
    """
    Property 8e: writingSentence item missing targetVocab field is rejected.

    # Feature: bilingual-parity-expansion, Property 8: Writing activity structure
    **Validates: Requirements 11.11**
    """
    content = _get_valid_curriculum(level)
    si, ai, activity = _find_activity(content, "writingSentence")
    assume(activity is not None)

    del activity["data"]["items"][0]["targetVocab"]

    with pytest.raises(ValueError, match="targetVocab"):
        validate(content, level=level)


@settings(max_examples=100)
@given(level=level_strategy, bad_value=bad_string_values)
def test_writing_sentence_rejects_item_empty_prompt(level, bad_value):
    """
    Property 8f: writingSentence item with empty/invalid prompt is rejected.

    # Feature: bilingual-parity-expansion, Property 8: Writing activity structure
    **Validates: Requirements 11.11**
    """
    content = _get_valid_curriculum(level)
    si, ai, activity = _find_activity(content, "writingSentence")
    assume(activity is not None)

    activity["data"]["items"][0]["prompt"] = bad_value

    with pytest.raises(ValueError, match="prompt"):
        validate(content, level=level)


@settings(max_examples=100)
@given(level=level_strategy, bad_value=bad_string_values)
def test_writing_sentence_rejects_item_empty_target_vocab(level, bad_value):
    """
    Property 8g: writingSentence item with empty/invalid targetVocab is rejected.

    # Feature: bilingual-parity-expansion, Property 8: Writing activity structure
    **Validates: Requirements 11.11**
    """
    content = _get_valid_curriculum(level)
    si, ai, activity = _find_activity(content, "writingSentence")
    assume(activity is not None)

    activity["data"]["items"][0]["targetVocab"] = bad_value

    with pytest.raises(ValueError, match="targetVocab"):
        validate(content, level=level)


# ===========================================================================
# writingParagraph tests (standard level only)
# ===========================================================================

@settings(max_examples=100)
@given(data=st.data())
def test_writing_paragraph_rejects_missing_vocab_list(data):
    """
    Property 8h: writingParagraph missing data.vocabList is rejected (standard only).

    # Feature: bilingual-parity-expansion, Property 8: Writing activity structure
    **Validates: Requirements 11.11**
    """
    content = _get_valid_curriculum("standard")
    si, ai, activity = _find_activity(content, "writingParagraph")
    assume(activity is not None)

    del activity["data"]["vocabList"]

    with pytest.raises(ValueError, match="vocabList"):
        validate(content, level="standard")


@settings(max_examples=100)
@given(data=st.data())
def test_writing_paragraph_rejects_missing_instructions(data):
    """
    Property 8i: writingParagraph missing data.instructions is rejected.

    # Feature: bilingual-parity-expansion, Property 8: Writing activity structure
    **Validates: Requirements 11.11**
    """
    content = _get_valid_curriculum("standard")
    si, ai, activity = _find_activity(content, "writingParagraph")
    assume(activity is not None)

    del activity["data"]["instructions"]

    with pytest.raises(ValueError, match="instructions"):
        validate(content, level="standard")


@settings(max_examples=100)
@given(bad_value=bad_string_values)
def test_writing_paragraph_rejects_empty_instructions(bad_value):
    """
    Property 8j: writingParagraph with empty/invalid data.instructions is rejected.

    # Feature: bilingual-parity-expansion, Property 8: Writing activity structure
    **Validates: Requirements 11.11**
    """
    content = _get_valid_curriculum("standard")
    si, ai, activity = _find_activity(content, "writingParagraph")
    assume(activity is not None)

    activity["data"]["instructions"] = bad_value

    with pytest.raises(ValueError, match="instructions"):
        validate(content, level="standard")


@settings(max_examples=100)
@given(data=st.data())
def test_writing_paragraph_rejects_missing_prompts(data):
    """
    Property 8k: writingParagraph missing data.prompts is rejected.

    # Feature: bilingual-parity-expansion, Property 8: Writing activity structure
    **Validates: Requirements 11.11**
    """
    content = _get_valid_curriculum("standard")
    si, ai, activity = _find_activity(content, "writingParagraph")
    assume(activity is not None)

    del activity["data"]["prompts"]

    with pytest.raises(ValueError, match="prompts"):
        validate(content, level="standard")


@settings(max_examples=100)
@given(
    short_prompts=st.one_of(
        st.just([]),
        st.just(["only one prompt"]),
    )
)
def test_writing_paragraph_rejects_fewer_than_2_prompts(short_prompts):
    """
    Property 8l: writingParagraph with fewer than 2 prompts is rejected.

    # Feature: bilingual-parity-expansion, Property 8: Writing activity structure
    **Validates: Requirements 11.11**
    """
    content = _get_valid_curriculum("standard")
    si, ai, activity = _find_activity(content, "writingParagraph")
    assume(activity is not None)

    activity["data"]["prompts"] = short_prompts

    with pytest.raises(ValueError, match="prompts"):
        validate(content, level="standard")


@settings(max_examples=100)
@given(
    bad_element=st.one_of(
        st.just(42),
        st.just(None),
        st.just(True),
        st.just([]),
        st.just({}),
        st.just(3.14),
    )
)
def test_writing_paragraph_rejects_non_string_prompt_elements(bad_element):
    """
    Property 8m: writingParagraph with non-string elements in data.prompts is rejected.

    # Feature: bilingual-parity-expansion, Property 8: Writing activity structure
    **Validates: Requirements 11.11**
    """
    content = _get_valid_curriculum("standard")
    si, ai, activity = _find_activity(content, "writingParagraph")
    assume(activity is not None)

    # Replace one prompt with a non-string element
    activity["data"]["prompts"] = [bad_element, "Valid second prompt"]

    with pytest.raises(ValueError, match="prompts"):
        validate(content, level="standard")


# ===========================================================================
# Cross-level: beginner has writingSentence only, standard has both
# ===========================================================================

def test_beginner_has_no_writing_paragraph():
    """
    Beginner curriculums should not contain writingParagraph activities.
    This is a sanity check that our beginner helper is correct.

    # Feature: bilingual-parity-expansion, Property 8: Writing activity structure
    **Validates: Requirements 11.11**
    """
    content = make_valid_beginner_curriculum()
    si, ai, activity = _find_activity(content, "writingParagraph")
    assert activity is None, "Beginner curriculum should not have writingParagraph"


def test_standard_has_writing_paragraph():
    """
    Standard curriculums should contain a writingParagraph activity.
    This is a sanity check that our standard helper is correct.

    # Feature: bilingual-parity-expansion, Property 8: Writing activity structure
    **Validates: Requirements 11.11**
    """
    content = make_valid_standard_curriculum()
    si, ai, activity = _find_activity(content, "writingParagraph")
    assert activity is not None, "Standard curriculum should have writingParagraph"
