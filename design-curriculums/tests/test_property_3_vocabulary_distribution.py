"""
Property-based tests for validate_content.py — Property 3: Level-aware vocabulary distribution

# Feature: bilingual-parity-expansion, Property 3: Level-aware vocabulary distribution

Tests that the validator enforces correct vocabulary word counts per level:
- Beginner: exactly 12 unique words total, 6 per learning session (2 learning sessions)
- Standard: exactly 18 unique words total, 6 per learning session (3 learning sessions)

**Validates: Requirements 2.1, 3.1, 11.9**
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
    _make_vocab_activity,
    _make_text_activity,
    _make_writing_sentence_activity,
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


def _replace_session_vocab(session, new_vocab, level):
    """Replace all vocab words in a learning session's vocab activities with new_vocab.
    Preserves the activity structure but swaps the vocabList."""
    from validate_content import VOCAB_ACTIVITY_TYPES
    for activity in session.get("activities", []):
        at = activity.get("activityType")
        if at in VOCAB_ACTIVITY_TYPES:
            activity["data"]["vocabList"] = list(new_vocab)
        if at == "writingSentence":
            activity["data"]["vocabList"] = list(new_vocab)
            if new_vocab:
                activity["data"]["items"] = [
                    {"prompt": "Use the word in a sentence", "targetVocab": new_vocab[0]}
                ]


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

# Generate wrong per-session vocab counts (not 6)
wrong_vocab_count = st.integers(min_value=1, max_value=20).filter(lambda x: x != 6)

# A pool of unique lowercase words to draw from
word_pool = [
    "alpha", "bravo", "charlie", "delta", "echo", "foxtrot",
    "golf", "hotel", "india", "juliet", "kilo", "lima",
    "mike", "november", "oscar", "papa", "quebec", "romeo",
    "sierra", "tango", "uniform", "victor", "whiskey", "xray",
    "yankee", "zulu", "amber", "bronze", "coral", "dusk",
]


# ---------------------------------------------------------------------------
# Property 3a: Beginner with wrong total vocab count (not 12)
# Feature: bilingual-parity-expansion, Property 3: Level-aware vocabulary distribution
# **Validates: Requirements 2.1, 11.9**
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(
    session1_count=st.integers(min_value=1, max_value=10),
    session2_count=st.integers(min_value=1, max_value=10),
)
def test_rejects_beginner_with_wrong_total_vocab(session1_count, session2_count):
    """
    Property 3a: Validator rejects beginner curriculum when total unique vocab
    words across learning sessions is not 12.

    For any beginner curriculum where the 2 learning sessions do not collectively
    contain exactly 12 unique vocabulary words, the validator SHALL raise ValueError.

    # Feature: bilingual-parity-expansion, Property 3: Level-aware vocabulary distribution
    **Validates: Requirements 2.1, 11.9**
    """
    # Skip the valid case (6 + 6 = 12 unique)
    assume(session1_count != 6 or session2_count != 6)

    content = _get_valid_curriculum("beginner")

    vocab_s1 = word_pool[:session1_count]
    vocab_s2 = word_pool[session1_count:session1_count + session2_count]

    _replace_session_vocab(content["learningSessions"][0], vocab_s1, "beginner")
    _replace_session_vocab(content["learningSessions"][1], vocab_s2, "beginner")

    with pytest.raises(ValueError):
        validate(content, level="beginner")


# ---------------------------------------------------------------------------
# Property 3b: Standard with wrong total vocab count (not 18)
# Feature: bilingual-parity-expansion, Property 3: Level-aware vocabulary distribution
# **Validates: Requirements 3.1, 11.9**
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(
    session1_count=st.integers(min_value=1, max_value=10),
    session2_count=st.integers(min_value=1, max_value=10),
    session3_count=st.integers(min_value=1, max_value=10),
)
def test_rejects_standard_with_wrong_total_vocab(session1_count, session2_count, session3_count):
    """
    Property 3b: Validator rejects standard curriculum when total unique vocab
    words across learning sessions is not 18.

    For any standard curriculum where the 3 learning sessions do not collectively
    contain exactly 18 unique vocabulary words, the validator SHALL raise ValueError.

    # Feature: bilingual-parity-expansion, Property 3: Level-aware vocabulary distribution
    **Validates: Requirements 3.1, 11.9**
    """
    # Skip the valid case (6 + 6 + 6 = 18 unique)
    assume(session1_count != 6 or session2_count != 6 or session3_count != 6)

    content = _get_valid_curriculum("standard")

    offset = 0
    vocab_s1 = word_pool[offset:offset + session1_count]
    offset += session1_count
    vocab_s2 = word_pool[offset:offset + session2_count]
    offset += session2_count
    vocab_s3 = word_pool[offset:offset + session3_count]

    _replace_session_vocab(content["learningSessions"][0], vocab_s1, "standard")
    _replace_session_vocab(content["learningSessions"][1], vocab_s2, "standard")
    _replace_session_vocab(content["learningSessions"][2], vocab_s3, "standard")

    with pytest.raises(ValueError):
        validate(content, level="standard")


# ---------------------------------------------------------------------------
# Property 3c: Learning sessions with wrong per-session vocab count (not 6)
# Feature: bilingual-parity-expansion, Property 3: Level-aware vocabulary distribution
# **Validates: Requirements 2.1, 3.1, 11.9**
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(
    bad_count=wrong_vocab_count,
    session_idx=st.sampled_from([0, 1]),
)
def test_rejects_beginner_session_with_wrong_vocab_count(bad_count, session_idx):
    """
    Property 3c-i: Validator rejects beginner curriculum when any learning session
    has a vocab count other than 6.

    # Feature: bilingual-parity-expansion, Property 3: Level-aware vocabulary distribution
    **Validates: Requirements 2.1, 11.9**
    """
    content = _get_valid_curriculum("beginner")

    # Build a vocab list of the wrong size using unique words
    bad_vocab = word_pool[:bad_count]
    _replace_session_vocab(content["learningSessions"][session_idx], bad_vocab, "beginner")

    with pytest.raises(ValueError):
        validate(content, level="beginner")


@settings(max_examples=100)
@given(
    bad_count=wrong_vocab_count,
    session_idx=st.sampled_from([0, 1, 2]),
)
def test_rejects_standard_session_with_wrong_vocab_count(bad_count, session_idx):
    """
    Property 3c-ii: Validator rejects standard curriculum when any learning session
    has a vocab count other than 6.

    # Feature: bilingual-parity-expansion, Property 3: Level-aware vocabulary distribution
    **Validates: Requirements 3.1, 11.9**
    """
    content = _get_valid_curriculum("standard")

    bad_vocab = word_pool[:bad_count]
    _replace_session_vocab(content["learningSessions"][session_idx], bad_vocab, "standard")

    with pytest.raises(ValueError):
        validate(content, level="standard")


# ---------------------------------------------------------------------------
# Property 3d: Duplicate vocab words across sessions reducing unique count
# Feature: bilingual-parity-expansion, Property 3: Level-aware vocabulary distribution
# **Validates: Requirements 2.1, 3.1, 11.9**
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(
    overlap_count=st.integers(min_value=1, max_value=5),
)
def test_rejects_beginner_with_duplicate_vocab_across_sessions(overlap_count):
    """
    Property 3d-i: Validator rejects beginner curriculum when vocab words are
    duplicated across learning sessions, reducing the total unique count below 12.

    Even if each session has exactly 6 words, if some words overlap between
    sessions the total unique count drops below 12 and must be rejected.

    # Feature: bilingual-parity-expansion, Property 3: Level-aware vocabulary distribution
    **Validates: Requirements 2.1, 11.9**
    """
    content = _get_valid_curriculum("beginner")

    # Session 1: 6 unique words
    vocab_s1 = word_pool[:6]
    # Session 2: overlap_count words from session 1 + remaining from pool
    # This gives 6 words per session but < 12 unique total
    overlapping = vocab_s1[:overlap_count]
    fresh = word_pool[6:6 + (6 - overlap_count)]
    vocab_s2 = overlapping + fresh
    assert len(vocab_s2) == 6

    _replace_session_vocab(content["learningSessions"][0], vocab_s1, "beginner")
    _replace_session_vocab(content["learningSessions"][1], vocab_s2, "beginner")

    # Total unique should be 12 - overlap_count, which is < 12
    total_unique = len(set(vocab_s1) | set(vocab_s2))
    assert total_unique < 12

    with pytest.raises(ValueError, match="unique vocabulary words"):
        validate(content, level="beginner")


@settings(max_examples=100)
@given(
    overlap_count=st.integers(min_value=1, max_value=5),
    overlap_pair=st.sampled_from([(0, 1), (0, 2), (1, 2)]),
)
def test_rejects_standard_with_duplicate_vocab_across_sessions(overlap_count, overlap_pair):
    """
    Property 3d-ii: Validator rejects standard curriculum when vocab words are
    duplicated across any pair of learning sessions, reducing the total unique
    count below 18.

    Even if each session has exactly 6 words, if some words overlap between
    sessions the total unique count drops below 18 and must be rejected.

    # Feature: bilingual-parity-expansion, Property 3: Level-aware vocabulary distribution
    **Validates: Requirements 3.1, 11.9**
    """
    content = _get_valid_curriculum("standard")

    # Build 3 sessions of 6 words each, with overlap between the chosen pair
    src_idx, dst_idx = overlap_pair
    other_idx = [i for i in [0, 1, 2] if i != src_idx and i != dst_idx][0]

    # Source session: 6 unique words
    vocab_src = word_pool[:6]
    # Destination session: overlap_count words from source + fresh words
    overlapping = vocab_src[:overlap_count]
    fresh_dst = word_pool[6:6 + (6 - overlap_count)]
    vocab_dst = overlapping + fresh_dst
    assert len(vocab_dst) == 6
    # Other session: 6 completely fresh words
    vocab_other = word_pool[12:18]

    sessions_vocab = [None, None, None]
    sessions_vocab[src_idx] = vocab_src
    sessions_vocab[dst_idx] = vocab_dst
    sessions_vocab[other_idx] = vocab_other

    for i in range(3):
        _replace_session_vocab(content["learningSessions"][i], sessions_vocab[i], "standard")

    # Total unique should be < 18
    total_unique = len(set(sessions_vocab[0]) | set(sessions_vocab[1]) | set(sessions_vocab[2]))
    assert total_unique < 18

    with pytest.raises(ValueError, match="unique vocabulary words"):
        validate(content, level="standard")
