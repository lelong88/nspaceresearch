"""
Property-based tests for validate_content.py — Property 5: Activity structure completeness

# Feature: bilingual-parity-expansion, Property 5: Activity structure completeness

Tests that the validator rejects activities with missing fields, `type` instead of
`activityType`, invalid activityType values, missing title/description/data fields,
and content fields inline (not inside data) — for BOTH beginner and standard levels.

**Validates: Requirements 5.3, 5.4, 5.5, 5.6, 11.6**
"""

import copy
import pytest
from hypothesis import given, settings, assume
from hypothesis import strategies as st

import sys
import os

# Ensure the repo root is on the path so we can import validate_content
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from validate_content import validate, VALID_ACTIVITY_TYPES, BEGINNER_FORBIDDEN_ACTIVITIES

# Import helpers from property 1 tests
from tests.test_property_1_top_level_structure import (
    make_valid_beginner_curriculum,
    make_valid_standard_curriculum,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

# Which level to test
level_strategy = st.sampled_from(["beginner", "standard"])

# Valid activity types for beginner (excludes writingParagraph and vocabLevel3)
BEGINNER_VALID_TYPES = VALID_ACTIVITY_TYPES - BEGINNER_FORBIDDEN_ACTIVITIES


def _get_valid_curriculum(level):
    """Return a deep copy of a valid curriculum for the given level."""
    if level == "beginner":
        return copy.deepcopy(make_valid_beginner_curriculum())
    return copy.deepcopy(make_valid_standard_curriculum())


def _get_first_activity(content):
    """Return a reference to the first activity in the first session."""
    return content["learningSessions"][0]["activities"][0]


# Strategy for random strings that are NOT valid activity types
invalid_activity_type_strategy = st.text(
    alphabet=st.characters(whitelist_categories=("L", "N")),
    min_size=1,
    max_size=30,
).filter(lambda s: s not in VALID_ACTIVITY_TYPES)


# ---------------------------------------------------------------------------
# Sanity checks: base curriculums pass validation at their respective levels
# ---------------------------------------------------------------------------

def test_valid_beginner_curriculum_passes():
    """Ensure the beginner helper builds a curriculum that passes validation."""
    validate(make_valid_beginner_curriculum(), level="beginner")


def test_valid_standard_curriculum_passes():
    """Ensure the standard helper builds a curriculum that passes validation."""
    validate(make_valid_standard_curriculum(), level="standard")


# ---------------------------------------------------------------------------
# Property 5a: Activities with missing activityType field
# Feature: bilingual-parity-expansion, Property 5: Activity structure completeness
# **Validates: Requirements 5.3, 5.4, 11.6**
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(level=level_strategy)
def test_rejects_activity_missing_activityType(level):
    """
    Property 5a: Validator rejects activities where activityType is missing entirely.

    For any curriculum at any level, removing the activityType field from an activity
    SHALL cause the validator to raise ValueError.

    # Feature: bilingual-parity-expansion, Property 5: Activity structure completeness
    **Validates: Requirements 5.3, 5.4, 11.6**
    """
    content = _get_valid_curriculum(level)
    activity = _get_first_activity(content)
    del activity["activityType"]

    with pytest.raises(ValueError, match="activityType"):
        validate(content, level=level)


# ---------------------------------------------------------------------------
# Property 5b: Activities using `type` instead of `activityType`
# Feature: bilingual-parity-expansion, Property 5: Activity structure completeness
# **Validates: Requirements 5.3, 11.6**
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(level=level_strategy)
def test_rejects_activity_using_type_instead_of_activityType(level):
    """
    Property 5b: Validator rejects activities that use 'type' instead of 'activityType'.

    For any curriculum at any level, if an activity has 'type' but not 'activityType',
    the validator SHALL raise ValueError mentioning 'type'.

    # Feature: bilingual-parity-expansion, Property 5: Activity structure completeness
    **Validates: Requirements 5.3, 11.6**
    """
    content = _get_valid_curriculum(level)
    activity = _get_first_activity(content)
    original_type = activity.pop("activityType")
    activity["type"] = original_type

    with pytest.raises(ValueError, match="type"):
        validate(content, level=level)


# ---------------------------------------------------------------------------
# Property 5c: Activities with invalid activityType values (random strings)
# Feature: bilingual-parity-expansion, Property 5: Activity structure completeness
# **Validates: Requirements 5.5, 11.6**
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(level=level_strategy, bad_type=invalid_activity_type_strategy)
def test_rejects_activity_with_invalid_activityType(level, bad_type):
    """
    Property 5c: Validator rejects activities with activityType values not in the
    valid set.

    For any curriculum at any level, setting activityType to a random string that
    is not one of the 11 valid types SHALL cause the validator to raise ValueError.

    # Feature: bilingual-parity-expansion, Property 5: Activity structure completeness
    **Validates: Requirements 5.5, 11.6**
    """
    content = _get_valid_curriculum(level)
    activity = _get_first_activity(content)
    activity["activityType"] = bad_type

    with pytest.raises(ValueError, match="activityType"):
        validate(content, level=level)


# ---------------------------------------------------------------------------
# Property 5d: Activities with missing title field
# Feature: bilingual-parity-expansion, Property 5: Activity structure completeness
# **Validates: Requirements 5.4, 11.6**
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(level=level_strategy)
def test_rejects_activity_missing_title(level):
    """
    Property 5d: Validator rejects activities where the title field is missing.

    For any curriculum at any level, removing the title field from an activity
    SHALL cause the validator to raise ValueError mentioning 'title'.

    # Feature: bilingual-parity-expansion, Property 5: Activity structure completeness
    **Validates: Requirements 5.4, 11.6**
    """
    content = _get_valid_curriculum(level)
    activity = _get_first_activity(content)
    del activity["title"]

    with pytest.raises(ValueError, match="title"):
        validate(content, level=level)


# ---------------------------------------------------------------------------
# Property 5e: Activities with missing description field
# Feature: bilingual-parity-expansion, Property 5: Activity structure completeness
# **Validates: Requirements 5.4, 11.6**
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(level=level_strategy)
def test_rejects_activity_missing_description(level):
    """
    Property 5e: Validator rejects activities where the description field is missing.

    For any curriculum at any level, removing the description field from an activity
    SHALL cause the validator to raise ValueError mentioning 'description'.

    # Feature: bilingual-parity-expansion, Property 5: Activity structure completeness
    **Validates: Requirements 5.4, 11.6**
    """
    content = _get_valid_curriculum(level)
    activity = _get_first_activity(content)
    del activity["description"]

    with pytest.raises(ValueError, match="description"):
        validate(content, level=level)


# ---------------------------------------------------------------------------
# Property 5f: Activities with missing data field
# Feature: bilingual-parity-expansion, Property 5: Activity structure completeness
# **Validates: Requirements 5.4, 5.6, 11.6**
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(
    level=level_strategy,
    bad_data=st.one_of(
        st.just(None),
        st.just("a string"),
        st.just(42),
        st.just([]),
        st.just(True),
    ),
)
def test_rejects_activity_with_missing_or_invalid_data(level, bad_data):
    """
    Property 5f: Validator rejects activities where the data field is missing,
    null, or not a dict.

    For any curriculum at any level, setting the data field to a non-dict value
    SHALL cause the validator to raise ValueError mentioning 'data'.

    # Feature: bilingual-parity-expansion, Property 5: Activity structure completeness
    **Validates: Requirements 5.4, 5.6, 11.6**
    """
    content = _get_valid_curriculum(level)
    activity = _get_first_activity(content)
    activity["data"] = bad_data

    with pytest.raises(ValueError, match="data"):
        validate(content, level=level)


@settings(max_examples=100)
@given(level=level_strategy)
def test_rejects_activity_with_deleted_data_field(level):
    """
    Property 5f-extra: Validator rejects activities where the data field is
    completely removed from the activity dict.

    # Feature: bilingual-parity-expansion, Property 5: Activity structure completeness
    **Validates: Requirements 5.4, 5.6, 11.6**
    """
    content = _get_valid_curriculum(level)
    activity = _get_first_activity(content)
    del activity["data"]

    with pytest.raises(ValueError, match="data"):
        validate(content, level=level)


# ---------------------------------------------------------------------------
# Property 5g: Activities with content fields inline (not inside data)
# Feature: bilingual-parity-expansion, Property 5: Activity structure completeness
# **Validates: Requirements 5.6, 11.6**
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(level=level_strategy)
def test_rejects_writing_activity_with_inline_content_fields(level):
    """
    Property 5g: Validator rejects activities where content fields are placed
    inline on the activity instead of inside data.

    For writingSentence, moving vocabList and items from data to the activity
    level and leaving data empty SHALL cause the validator to raise ValueError
    because data is missing the required content fields.

    # Feature: bilingual-parity-expansion, Property 5: Activity structure completeness
    **Validates: Requirements 5.6, 11.6**
    """
    content = _get_valid_curriculum(level)
    # Find the writingSentence activity in the first learning session
    session = content["learningSessions"][0]
    for activity in session["activities"]:
        if activity["activityType"] == "writingSentence":
            # Move content fields inline (out of data)
            activity["vocabList"] = activity["data"]["vocabList"]
            activity["items"] = activity["data"]["items"]
            activity["data"] = {}  # empty data — content is inline
            break

    with pytest.raises(ValueError):
        validate(content, level=level)


@settings(max_examples=100)
@given(level=level_strategy)
def test_rejects_vocab_activity_with_inline_vocabList(level):
    """
    Property 5g-vocab: Validator rejects vocab activities where vocabList is
    placed inline on the activity instead of inside data.

    Moving vocabList from data to the activity level and leaving data empty
    SHALL cause the validator to raise ValueError.

    # Feature: bilingual-parity-expansion, Property 5: Activity structure completeness
    **Validates: Requirements 5.6, 11.6**
    """
    content = _get_valid_curriculum(level)
    # Target the viewFlashcards activity (second activity in learning sessions)
    activity = content["learningSessions"][0]["activities"][1]
    assert activity["activityType"] == "viewFlashcards"

    vocab = activity["data"]["vocabList"]
    activity["vocabList"] = vocab  # inline
    activity["data"] = {}  # empty data

    with pytest.raises(ValueError):
        validate(content, level=level)


# ---------------------------------------------------------------------------
# Property 5h: Combined — both levels tested with various missing fields
# Feature: bilingual-parity-expansion, Property 5: Activity structure completeness
# **Validates: Requirements 5.3, 5.4, 5.5, 5.6, 11.6**
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(
    level=level_strategy,
    field_to_remove=st.sampled_from(["activityType", "title", "description", "data"]),
)
def test_rejects_activity_with_any_required_field_removed(level, field_to_remove):
    """
    Property 5h: Validator rejects activities when any required field
    (activityType, title, description, data) is removed, at both levels.

    # Feature: bilingual-parity-expansion, Property 5: Activity structure completeness
    **Validates: Requirements 5.3, 5.4, 5.5, 5.6, 11.6**
    """
    content = _get_valid_curriculum(level)
    activity = _get_first_activity(content)
    del activity[field_to_remove]

    with pytest.raises(ValueError):
        validate(content, level=level)
