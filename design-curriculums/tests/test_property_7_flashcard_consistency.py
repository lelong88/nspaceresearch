"""
Property-based tests for validate_content.py — Property 7: Flashcard vocabList consistency

# Feature: bilingual-parity-expansion, Property 7: Flashcard vocabList consistency

Tests that the validator rejects curriculum JSON where viewFlashcards and speakFlashcards
in the same session have mismatched vocabList arrays (different words, different order,
or extra words in one).

**Validates: Requirements 5.9, 11.8**
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
from tests.test_property_1_top_level_structure import (
    make_valid_beginner_curriculum,
    make_valid_standard_curriculum,
)


# ---------------------------------------------------------------------------
# Strategies
# ---------------------------------------------------------------------------

level_strategy = st.sampled_from(["beginner", "standard"])

# Strategy for generating a list of 6 unique lowercase words
lowercase_word = st.text(
    alphabet=st.sampled_from("abcdefghijklmnopqrstuvwxyz"),
    min_size=3,
    max_size=10,
)

vocab_list_6 = st.lists(
    lowercase_word,
    min_size=6,
    max_size=6,
).filter(lambda ws: len(set(ws)) == 6)


def _get_valid_curriculum(level):
    """Return a deep copy of a valid curriculum for the given level."""
    if level == "beginner":
        return copy.deepcopy(make_valid_beginner_curriculum())
    return copy.deepcopy(make_valid_standard_curriculum())


def _find_flashcard_session_indices(content):
    """Return indices of learning sessions that have both viewFlashcards and speakFlashcards."""
    indices = []
    for i, session in enumerate(content["learningSessions"]):
        has_view = any(a.get("activityType") == "viewFlashcards" for a in session.get("activities", []))
        has_speak = any(a.get("activityType") == "speakFlashcards" for a in session.get("activities", []))
        if has_view and has_speak:
            indices.append(i)
    return indices


def _set_flashcard_vocab(session, activity_type, vocab_list):
    """Set the vocabList for a specific flashcard activity type in a session."""
    for activity in session.get("activities", []):
        if activity.get("activityType") == activity_type:
            activity["data"]["vocabList"] = list(vocab_list)
            return


# ---------------------------------------------------------------------------
# Sanity: valid curriculums pass (flashcards already match in helpers)
# ---------------------------------------------------------------------------

def test_valid_beginner_flashcards_pass():
    """Beginner curriculum with matching flashcard vocabLists passes validation."""
    validate(make_valid_beginner_curriculum(), level="beginner")


def test_valid_standard_flashcards_pass():
    """Standard curriculum with matching flashcard vocabLists passes validation."""
    validate(make_valid_standard_curriculum(), level="standard")


# ---------------------------------------------------------------------------
# Property 7a: Different words in viewFlashcards vs speakFlashcards
# Feature: bilingual-parity-expansion, Property 7: Flashcard vocabList consistency
# **Validates: Requirements 5.9, 11.8**
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(
    level=level_strategy,
    alt_vocab=vocab_list_6,
)
def test_rejects_different_words_in_flashcards(level, alt_vocab):
    """
    Property 7a: For any session containing both viewFlashcards and speakFlashcards,
    the validator SHALL reject the curriculum if the two activities have completely
    different vocabList arrays (different words).

    # Feature: bilingual-parity-expansion, Property 7: Flashcard vocabList consistency
    **Validates: Requirements 5.9, 11.8**
    """
    content = _get_valid_curriculum(level)
    fc_indices = _find_flashcard_session_indices(content)
    assume(len(fc_indices) > 0)

    # Pick the first learning session with flashcards
    session_idx = fc_indices[0]
    session = content["learningSessions"][session_idx]

    # Get the original viewFlashcards vocab to ensure alt_vocab is actually different
    original_vocab = None
    for activity in session.get("activities", []):
        if activity.get("activityType") == "viewFlashcards":
            original_vocab = activity["data"]["vocabList"]
            break
    assume(original_vocab is not None)
    assume(alt_vocab != original_vocab)

    # Set speakFlashcards to a different vocabList
    _set_flashcard_vocab(session, "speakFlashcards", alt_vocab)

    with pytest.raises(ValueError, match="viewFlashcards.*speakFlashcards|speakFlashcards.*viewFlashcards|mismatched"):
        validate(content, level=level)


# ---------------------------------------------------------------------------
# Property 7b: Same words but different order
# Feature: bilingual-parity-expansion, Property 7: Flashcard vocabList consistency
# **Validates: Requirements 5.9, 11.8**
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(
    level=level_strategy,
    data=st.data(),
)
def test_rejects_same_words_different_order(level, data):
    """
    Property 7b: For any session containing both viewFlashcards and speakFlashcards,
    the validator SHALL reject the curriculum if the two activities have the same
    words but in a different order.

    # Feature: bilingual-parity-expansion, Property 7: Flashcard vocabList consistency
    **Validates: Requirements 5.9, 11.8**
    """
    content = _get_valid_curriculum(level)
    fc_indices = _find_flashcard_session_indices(content)
    assume(len(fc_indices) > 0)

    session_idx = fc_indices[0]
    session = content["learningSessions"][session_idx]

    # Get the original viewFlashcards vocab
    original_vocab = None
    for activity in session.get("activities", []):
        if activity.get("activityType") == "viewFlashcards":
            original_vocab = list(activity["data"]["vocabList"])
            break
    assume(original_vocab is not None)
    assume(len(original_vocab) >= 2)

    # Generate a permutation that is different from the original
    shuffled = data.draw(st.permutations(original_vocab))
    assume(list(shuffled) != original_vocab)

    _set_flashcard_vocab(session, "speakFlashcards", shuffled)

    with pytest.raises(ValueError, match="viewFlashcards.*speakFlashcards|speakFlashcards.*viewFlashcards|mismatched"):
        validate(content, level=level)


# ---------------------------------------------------------------------------
# Property 7c: One has extra words the other doesn't
# Feature: bilingual-parity-expansion, Property 7: Flashcard vocabList consistency
# **Validates: Requirements 5.9, 11.8**
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(
    level=level_strategy,
    extra_word=lowercase_word,
)
def test_rejects_extra_words_in_speak_flashcards(level, extra_word):
    """
    Property 7c: For any session containing both viewFlashcards and speakFlashcards,
    the validator SHALL reject the curriculum if speakFlashcards has extra words
    that viewFlashcards doesn't have.

    # Feature: bilingual-parity-expansion, Property 7: Flashcard vocabList consistency
    **Validates: Requirements 5.9, 11.8**
    """
    content = _get_valid_curriculum(level)
    fc_indices = _find_flashcard_session_indices(content)
    assume(len(fc_indices) > 0)

    session_idx = fc_indices[0]
    session = content["learningSessions"][session_idx]

    # Get the original viewFlashcards vocab
    original_vocab = None
    for activity in session.get("activities", []):
        if activity.get("activityType") == "viewFlashcards":
            original_vocab = list(activity["data"]["vocabList"])
            break
    assume(original_vocab is not None)
    assume(extra_word not in original_vocab)

    # speakFlashcards gets the original vocab + an extra word
    extended_vocab = original_vocab + [extra_word]
    _set_flashcard_vocab(session, "speakFlashcards", extended_vocab)

    with pytest.raises(ValueError, match="viewFlashcards.*speakFlashcards|speakFlashcards.*viewFlashcards|mismatched"):
        validate(content, level=level)


@settings(max_examples=100)
@given(
    level=level_strategy,
    extra_word=lowercase_word,
)
def test_rejects_extra_words_in_view_flashcards(level, extra_word):
    """
    Property 7d: For any session containing both viewFlashcards and speakFlashcards,
    the validator SHALL reject the curriculum if viewFlashcards has extra words
    that speakFlashcards doesn't have.

    # Feature: bilingual-parity-expansion, Property 7: Flashcard vocabList consistency
    **Validates: Requirements 5.9, 11.8**
    """
    content = _get_valid_curriculum(level)
    fc_indices = _find_flashcard_session_indices(content)
    assume(len(fc_indices) > 0)

    session_idx = fc_indices[0]
    session = content["learningSessions"][session_idx]

    # Get the original speakFlashcards vocab
    original_vocab = None
    for activity in session.get("activities", []):
        if activity.get("activityType") == "speakFlashcards":
            original_vocab = list(activity["data"]["vocabList"])
            break
    assume(original_vocab is not None)
    assume(extra_word not in original_vocab)

    # viewFlashcards gets the original vocab + an extra word
    extended_vocab = original_vocab + [extra_word]
    _set_flashcard_vocab(session, "viewFlashcards", extended_vocab)

    with pytest.raises(ValueError, match="viewFlashcards.*speakFlashcards|speakFlashcards.*viewFlashcards|mismatched"):
        validate(content, level=level)


# ---------------------------------------------------------------------------
# Property 7e: Mismatch in non-first learning session
# Feature: bilingual-parity-expansion, Property 7: Flashcard vocabList consistency
# **Validates: Requirements 5.9, 11.8**
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(
    level=level_strategy,
    alt_vocab=vocab_list_6,
)
def test_rejects_mismatch_in_any_learning_session(level, alt_vocab):
    """
    Property 7e: The validator SHALL reject flashcard mismatches in ANY session,
    not just the first learning session. Tests the second learning session
    (and review session if it has flashcards).

    # Feature: bilingual-parity-expansion, Property 7: Flashcard vocabList consistency
    **Validates: Requirements 5.9, 11.8**
    """
    content = _get_valid_curriculum(level)
    fc_indices = _find_flashcard_session_indices(content)
    assume(len(fc_indices) >= 2)

    # Target the second session with flashcards
    session_idx = fc_indices[1]
    session = content["learningSessions"][session_idx]

    original_vocab = None
    for activity in session.get("activities", []):
        if activity.get("activityType") == "viewFlashcards":
            original_vocab = activity["data"]["vocabList"]
            break
    assume(original_vocab is not None)
    assume(alt_vocab != original_vocab)

    _set_flashcard_vocab(session, "speakFlashcards", alt_vocab)

    with pytest.raises(ValueError, match="viewFlashcards.*speakFlashcards|speakFlashcards.*viewFlashcards|mismatched"):
        validate(content, level=level)
