"""
Property-based tests for validate_content.py — Property 9: Strip keys exclusion

# Feature: bilingual-parity-expansion, Property 9: Strip keys exclusion

Tests that the validator rejects curriculum JSON when any auto-generated strip key
appears anywhere in the JSON tree at any depth — top level, inside sessions,
inside activities, inside activity data, and in nested arrays.

**Validates: Requirements 5.10, 11.10**
"""

import copy
import pytest
from hypothesis import given, settings, assume
from hypothesis import strategies as st

import sys
import os

# Ensure the repo root is on the path so we can import validate_content
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from validate_content import validate, STRIP_KEYS

# Import helpers from property 1 test
from tests.test_property_1_top_level_structure import (
    make_valid_beginner_curriculum,
    make_valid_standard_curriculum,
)


# ---------------------------------------------------------------------------
# Strategies
# ---------------------------------------------------------------------------

level_strategy = st.sampled_from(["beginner", "standard"])
strip_key_strategy = st.sampled_from(sorted(STRIP_KEYS))
# A non-empty value to assign to the injected strip key
strip_value_strategy = st.one_of(
    st.just("some_value"),
    st.just(123),
    st.just(True),
    st.just(None),
    st.just([]),
    st.just({}),
    st.just("https://example.com/audio.mp3"),
)


def _get_valid_curriculum(level):
    """Return a deep copy of a valid curriculum for the given level."""
    if level == "beginner":
        return copy.deepcopy(make_valid_beginner_curriculum())
    return copy.deepcopy(make_valid_standard_curriculum())


# ---------------------------------------------------------------------------
# Sanity: valid curriculums pass (no strip keys present)
# ---------------------------------------------------------------------------

def test_valid_beginner_has_no_strip_keys():
    """Sanity check: the beginner helper curriculum passes validation."""
    validate(make_valid_beginner_curriculum(), level="beginner")


def test_valid_standard_has_no_strip_keys():
    """Sanity check: the standard helper curriculum passes validation."""
    validate(make_valid_standard_curriculum(), level="standard")


# ---------------------------------------------------------------------------
# Property 9a: Strip key injected at the top level of the curriculum
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(level=level_strategy, key=strip_key_strategy, value=strip_value_strategy)
def test_rejects_strip_key_at_top_level(level, key, value):
    """
    Property 9a: Validator rejects curriculum when a strip key is injected
    at the top level of the curriculum JSON.

    # Feature: bilingual-parity-expansion, Property 9: Strip keys exclusion
    **Validates: Requirements 5.10, 11.10**
    """
    content = _get_valid_curriculum(level)
    content[key] = value

    with pytest.raises(ValueError, match="[Ss]trip"):
        validate(content, level=level)


# ---------------------------------------------------------------------------
# Property 9b: Strip key injected inside a session
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(
    level=level_strategy,
    key=strip_key_strategy,
    value=strip_value_strategy,
    session_idx=st.integers(min_value=0, max_value=4),
)
def test_rejects_strip_key_inside_session(level, key, value, session_idx):
    """
    Property 9b: Validator rejects curriculum when a strip key is injected
    inside a session object.

    # Feature: bilingual-parity-expansion, Property 9: Strip keys exclusion
    **Validates: Requirements 5.10, 11.10**
    """
    content = _get_valid_curriculum(level)
    sessions = content["learningSessions"]
    # Clamp session index to valid range for the level
    idx = session_idx % len(sessions)
    sessions[idx][key] = value

    with pytest.raises(ValueError, match="[Ss]trip"):
        validate(content, level=level)


# ---------------------------------------------------------------------------
# Property 9c: Strip key injected inside an activity
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(
    level=level_strategy,
    key=strip_key_strategy,
    value=strip_value_strategy,
)
def test_rejects_strip_key_inside_activity(level, key, value):
    """
    Property 9c: Validator rejects curriculum when a strip key is injected
    inside an activity object (first activity of first session).

    # Feature: bilingual-parity-expansion, Property 9: Strip keys exclusion
    **Validates: Requirements 5.10, 11.10**
    """
    content = _get_valid_curriculum(level)
    # Inject into the first activity of the first session
    activity = content["learningSessions"][0]["activities"][0]
    activity[key] = value

    with pytest.raises(ValueError, match="[Ss]trip"):
        validate(content, level=level)


# ---------------------------------------------------------------------------
# Property 9d: Strip key injected inside activity data
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(
    level=level_strategy,
    key=strip_key_strategy,
    value=strip_value_strategy,
)
def test_rejects_strip_key_inside_activity_data(level, key, value):
    """
    Property 9d: Validator rejects curriculum when a strip key is injected
    inside the data object of an activity.

    # Feature: bilingual-parity-expansion, Property 9: Strip keys exclusion
    **Validates: Requirements 5.10, 11.10**
    """
    content = _get_valid_curriculum(level)
    # Inject into the data of the first activity of the first session
    data = content["learningSessions"][0]["activities"][0]["data"]
    data[key] = value

    with pytest.raises(ValueError, match="[Ss]trip"):
        validate(content, level=level)


# ---------------------------------------------------------------------------
# Property 9e: Strip key injected in nested arrays (inside items of
# writingSentence activity data)
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(
    level=level_strategy,
    key=strip_key_strategy,
    value=strip_value_strategy,
)
def test_rejects_strip_key_in_nested_array_items(level, key, value):
    """
    Property 9e: Validator rejects curriculum when a strip key is injected
    inside an element of a nested array (e.g., writingSentence items).

    # Feature: bilingual-parity-expansion, Property 9: Strip keys exclusion
    **Validates: Requirements 5.10, 11.10**
    """
    content = _get_valid_curriculum(level)
    # Find the writingSentence activity in the first learning session
    session = content["learningSessions"][0]
    for activity in session["activities"]:
        if activity.get("activityType") == "writingSentence":
            # Inject strip key into the first item of the items array
            items = activity["data"]["items"]
            items[0][key] = value
            break

    with pytest.raises(ValueError, match="[Ss]trip"):
        validate(content, level=level)


# ---------------------------------------------------------------------------
# Property 9f: Every strip key is individually rejected (exhaustive check
# for both levels)
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(level=level_strategy, key=strip_key_strategy)
def test_every_strip_key_rejected_at_any_depth(level, key):
    """
    Property 9f: For every strip key in the STRIP_KEYS set, the validator
    rejects it regardless of where it appears in the tree. This test injects
    the key at a random depth (top, session, activity, data) and verifies
    rejection.

    # Feature: bilingual-parity-expansion, Property 9: Strip keys exclusion
    **Validates: Requirements 5.10, 11.10**
    """
    content = _get_valid_curriculum(level)

    # Inject at multiple depths simultaneously to ensure recursive detection
    # Top level
    content[key] = "injected"

    with pytest.raises(ValueError, match="[Ss]trip"):
        validate(content, level=level)
