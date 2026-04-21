"""
Property-based tests for validate_content.py — Property 2: Level-aware session structure

# Feature: bilingual-parity-expansion, Property 2: Level-aware session structure

Tests that the validator enforces correct session counts per level (4 for beginner,
5 for standard), and that each session must have a non-empty title string and a
non-empty activities array.

**Validates: Requirements 2.2, 3.2, 11.5**
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
    _make_beginner_learning_session,
    _make_standard_learning_session,
    _make_review_session,
    _make_final_session_beginner,
    _make_final_session_standard,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _get_valid_curriculum(level):
    """Return a deep copy of a valid curriculum for the given level."""
    if level == "beginner":
        return copy.deepcopy(make_valid_beginner_curriculum())
    return copy.deepcopy(make_valid_standard_curriculum())


# ---------------------------------------------------------------------------
# Sanity checks: valid curriculums pass at their respective levels
# ---------------------------------------------------------------------------

def test_valid_beginner_curriculum_passes():
    """Ensure the beginner helper builds a curriculum that passes validation."""
    validate(make_valid_beginner_curriculum(), level="beginner")


def test_valid_standard_curriculum_passes():
    """Ensure the standard helper builds a curriculum that passes validation."""
    validate(make_valid_standard_curriculum(), level="standard")


# ---------------------------------------------------------------------------
# Hypothesis strategies
# ---------------------------------------------------------------------------

level_strategy = st.sampled_from(["beginner", "standard"])

# Values that should be rejected as a session title
bad_title_values = st.one_of(
    st.just(None),
    st.just(""),
    st.just("   "),
    st.just(0),
    st.just(False),
    st.just([]),
    st.just({}),
)

# Values that should be rejected as an activities array
bad_activities_values = st.one_of(
    st.just(None),
    st.just([]),           # empty list
    st.just("not a list"),
    st.just(42),
    st.just({}),
)

# Values that should be rejected as a session (not a dict)
bad_session_values = st.one_of(
    st.just(None),
    st.just("a string"),
    st.just(42),
    st.just([]),
    st.just(True),
)


# ---------------------------------------------------------------------------
# Property 2a: Wrong session counts
# Feature: bilingual-parity-expansion, Property 2: Level-aware session structure
# **Validates: Requirements 2.2, 3.2, 11.5**
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(
    extra_sessions=st.integers(min_value=1, max_value=5),
)
def test_rejects_beginner_with_too_many_sessions(extra_sessions):
    """
    Property 2a-i: Validator rejects beginner curriculum with more than 4 sessions.

    For any beginner curriculum where learningSessions has more than 4 elements,
    the validator SHALL raise ValueError mentioning session count.

    # Feature: bilingual-parity-expansion, Property 2: Level-aware session structure
    **Validates: Requirements 2.2, 11.5**
    """
    content = _get_valid_curriculum("beginner")
    vocab = ["extra", "words", "here", "test", "more", "vocab"]
    for _ in range(extra_sessions):
        content["learningSessions"].append(
            _make_beginner_learning_session(99, vocab)
        )
    assert len(content["learningSessions"]) > 4

    with pytest.raises(ValueError, match="sessions"):
        validate(content, level="beginner")


@settings(max_examples=100)
@given(
    sessions_to_keep=st.integers(min_value=1, max_value=3),
)
def test_rejects_beginner_with_too_few_sessions(sessions_to_keep):
    """
    Property 2a-ii: Validator rejects beginner curriculum with fewer than 4 sessions.

    For any beginner curriculum where learningSessions has fewer than 4 elements,
    the validator SHALL raise ValueError mentioning session count.

    # Feature: bilingual-parity-expansion, Property 2: Level-aware session structure
    **Validates: Requirements 2.2, 11.5**
    """
    content = _get_valid_curriculum("beginner")
    content["learningSessions"] = content["learningSessions"][:sessions_to_keep]
    assert len(content["learningSessions"]) < 4

    with pytest.raises(ValueError, match="sessions"):
        validate(content, level="beginner")


@settings(max_examples=100)
@given(
    extra_sessions=st.integers(min_value=1, max_value=5),
)
def test_rejects_standard_with_too_many_sessions(extra_sessions):
    """
    Property 2a-iii: Validator rejects standard curriculum with more than 5 sessions.

    For any standard curriculum where learningSessions has more than 5 elements,
    the validator SHALL raise ValueError mentioning session count.

    # Feature: bilingual-parity-expansion, Property 2: Level-aware session structure
    **Validates: Requirements 3.2, 11.5**
    """
    content = _get_valid_curriculum("standard")
    vocab = ["extra", "words", "here", "test", "more", "vocab"]
    for _ in range(extra_sessions):
        content["learningSessions"].append(
            _make_standard_learning_session(99, vocab)
        )
    assert len(content["learningSessions"]) > 5

    with pytest.raises(ValueError, match="sessions"):
        validate(content, level="standard")


@settings(max_examples=100)
@given(
    sessions_to_keep=st.integers(min_value=1, max_value=4),
)
def test_rejects_standard_with_too_few_sessions(sessions_to_keep):
    """
    Property 2a-iv: Validator rejects standard curriculum with fewer than 5 sessions.

    For any standard curriculum where learningSessions has fewer than 5 elements,
    the validator SHALL raise ValueError mentioning session count.

    # Feature: bilingual-parity-expansion, Property 2: Level-aware session structure
    **Validates: Requirements 3.2, 11.5**
    """
    content = _get_valid_curriculum("standard")
    content["learningSessions"] = content["learningSessions"][:sessions_to_keep]
    assert len(content["learningSessions"]) < 5

    with pytest.raises(ValueError, match="sessions"):
        validate(content, level="standard")


# ---------------------------------------------------------------------------
# Property 2b: Sessions with missing titles
# Feature: bilingual-parity-expansion, Property 2: Level-aware session structure
# **Validates: Requirements 2.2, 3.2, 11.5**
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(
    level=level_strategy,
    bad_title=bad_title_values,
)
def test_rejects_session_with_missing_or_empty_title(level, bad_title):
    """
    Property 2b: Validator rejects curriculum where any session has a missing,
    empty, whitespace-only, or non-string title, at both beginner and standard levels.

    # Feature: bilingual-parity-expansion, Property 2: Level-aware session structure
    **Validates: Requirements 2.2, 3.2, 11.5**
    """
    content = _get_valid_curriculum(level)
    # Corrupt the first session's title
    content["learningSessions"][0]["title"] = bad_title

    with pytest.raises(ValueError, match="title"):
        validate(content, level=level)


@settings(max_examples=100)
@given(
    level=level_strategy,
    bad_title=bad_title_values,
)
def test_rejects_last_session_with_missing_title(level, bad_title):
    """
    Property 2b-ii: Validator rejects curriculum where the last session has a
    missing or invalid title, at both beginner and standard levels.

    # Feature: bilingual-parity-expansion, Property 2: Level-aware session structure
    **Validates: Requirements 2.2, 3.2, 11.5**
    """
    content = _get_valid_curriculum(level)
    content["learningSessions"][-1]["title"] = bad_title

    with pytest.raises(ValueError, match="title"):
        validate(content, level=level)


# ---------------------------------------------------------------------------
# Property 2c: Sessions with empty activities arrays
# Feature: bilingual-parity-expansion, Property 2: Level-aware session structure
# **Validates: Requirements 2.2, 3.2, 11.5**
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(
    level=level_strategy,
    bad_activities=bad_activities_values,
)
def test_rejects_session_with_empty_or_invalid_activities(level, bad_activities):
    """
    Property 2c: Validator rejects curriculum where any session has empty,
    missing, or non-array activities, at both beginner and standard levels.

    # Feature: bilingual-parity-expansion, Property 2: Level-aware session structure
    **Validates: Requirements 2.2, 3.2, 11.5**
    """
    content = _get_valid_curriculum(level)
    content["learningSessions"][0]["activities"] = bad_activities

    with pytest.raises(ValueError, match="activities"):
        validate(content, level=level)


@settings(max_examples=100)
@given(
    level=level_strategy,
    bad_activities=bad_activities_values,
)
def test_rejects_last_session_with_empty_activities(level, bad_activities):
    """
    Property 2c-ii: Validator rejects curriculum where the last session has
    empty or invalid activities, at both beginner and standard levels.

    # Feature: bilingual-parity-expansion, Property 2: Level-aware session structure
    **Validates: Requirements 2.2, 3.2, 11.5**
    """
    content = _get_valid_curriculum(level)
    content["learningSessions"][-1]["activities"] = bad_activities

    with pytest.raises(ValueError, match="activities"):
        validate(content, level=level)


# ---------------------------------------------------------------------------
# Property 2d: Sessions that are not dicts
# Feature: bilingual-parity-expansion, Property 2: Level-aware session structure
# **Validates: Requirements 2.2, 3.2, 11.5**
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(
    level=level_strategy,
    bad_session=bad_session_values,
)
def test_rejects_non_dict_session(level, bad_session):
    """
    Property 2d: Validator rejects curriculum where any session is not a dict,
    at both beginner and standard levels.

    # Feature: bilingual-parity-expansion, Property 2: Level-aware session structure
    **Validates: Requirements 2.2, 3.2, 11.5**
    """
    content = _get_valid_curriculum(level)
    # Replace the first session with a non-dict value
    content["learningSessions"][0] = bad_session

    with pytest.raises(ValueError):
        validate(content, level=level)


@settings(max_examples=100)
@given(
    level=level_strategy,
    bad_session=bad_session_values,
)
def test_rejects_non_dict_last_session(level, bad_session):
    """
    Property 2d-ii: Validator rejects curriculum where the last session is not a dict,
    at both beginner and standard levels.

    # Feature: bilingual-parity-expansion, Property 2: Level-aware session structure
    **Validates: Requirements 2.2, 3.2, 11.5**
    """
    content = _get_valid_curriculum(level)
    content["learningSessions"][-1] = bad_session

    with pytest.raises(ValueError):
        validate(content, level=level)
