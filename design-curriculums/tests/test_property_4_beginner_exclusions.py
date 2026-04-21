"""
Property-based tests for validate_content.py — Property 4: Beginner activity exclusions

# Feature: bilingual-parity-expansion, Property 4: Beginner activity exclusions

Tests that the validator rejects beginner curriculum JSON containing writingParagraph
or vocabLevel3 activities, with error messages identifying the forbidden activity type
and the session where it was found.

**Validates: Requirements 2.4, 2.5**
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


# ---------------------------------------------------------------------------
# Helpers: build minimal valid beginner curriculum
# ---------------------------------------------------------------------------

def _make_vocab_activity(activity_type, vocab_list):
    """Create a valid vocab-related activity."""
    return {
        "activityType": activity_type,
        "title": f"{activity_type} title",
        "description": f"{activity_type} description",
        "data": {"vocabList": list(vocab_list)},
    }


def _make_text_activity(activity_type):
    """Create a valid text-based activity (introAudio, reading, etc.)."""
    return {
        "activityType": activity_type,
        "title": f"{activity_type} title",
        "description": f"{activity_type} description",
        "data": {"text": "Some passage text here."},
    }


def _make_writing_sentence_activity(vocab_list):
    return {
        "activityType": "writingSentence",
        "title": "Writing Sentence",
        "description": "Write sentences",
        "data": {
            "vocabList": list(vocab_list),
            "items": [
                {"prompt": "Use the word in a sentence", "targetVocab": vocab_list[0]},
            ],
        },
    }


def _make_writing_paragraph_activity(vocab_list):
    """Create a valid writingParagraph activity (forbidden in beginner)."""
    return {
        "activityType": "writingParagraph",
        "title": "Writing Paragraph",
        "description": "Write a paragraph",
        "data": {
            "vocabList": list(vocab_list),
            "instructions": "Write a paragraph about the topic",
            "prompts": ["First prompt", "Second prompt"],
        },
    }


def _make_vocab_level3_activity(vocab_list):
    """Create a valid vocabLevel3 activity (forbidden in beginner)."""
    return {
        "activityType": "vocabLevel3",
        "title": "Vocab Level 3",
        "description": "Advanced vocab drill",
        "data": {"vocabList": list(vocab_list)},
    }


def _make_beginner_learning_session(session_num, vocab_words):
    """Build a valid beginner learning session with 6 vocab words.
    Beginner: no vocabLevel3, no writingParagraph."""
    activities = [
        _make_text_activity("introAudio"),
        _make_vocab_activity("viewFlashcards", vocab_words),
        _make_vocab_activity("speakFlashcards", vocab_words),
        _make_vocab_activity("vocabLevel1", vocab_words),
        _make_vocab_activity("vocabLevel2", vocab_words),
        _make_text_activity("reading"),
        _make_text_activity("speakReading"),
        _make_text_activity("readAlong"),
        _make_writing_sentence_activity(vocab_words),
    ]
    return {"title": f"Part {session_num}", "activities": activities}


def _make_review_session(all_vocab):
    """Build a valid review session."""
    activities = [
        _make_text_activity("introAudio"),
        _make_vocab_activity("viewFlashcards", all_vocab),
        _make_vocab_activity("speakFlashcards", all_vocab),
        _make_text_activity("reading"),
        _make_text_activity("speakReading"),
        _make_text_activity("readAlong"),
    ]
    return {"title": "Review", "activities": activities}


def _make_final_session_beginner(all_vocab):
    """Build a valid beginner final session — NO writingParagraph."""
    activities = [
        _make_text_activity("reading"),
        _make_text_activity("readAlong"),
        _make_text_activity("introAudio"),
    ]
    return {"title": "Final Reading", "activities": activities}


def make_valid_beginner_curriculum():
    """Return a fully valid beginner curriculum (4 sessions, 12 words)."""
    vocab_s1 = ["apple", "house", "garden", "river", "bridge", "forest"]
    vocab_s2 = ["market", "school", "castle", "village", "temple", "island"]
    all_vocab = vocab_s1 + vocab_s2

    return {
        "title": "Beginner Test Curriculum",
        "description": "A valid beginner test curriculum description.",
        "contentTypeTags": [],
        "preview": {"text": "This is a valid preview text for beginner testing."},
        "learningSessions": [
            _make_beginner_learning_session(1, vocab_s1),
            _make_beginner_learning_session(2, vocab_s2),
            _make_review_session(all_vocab),
            _make_final_session_beginner(all_vocab),
        ],
    }


# ---------------------------------------------------------------------------
# Sanity check: base beginner curriculum passes validation
# ---------------------------------------------------------------------------

def test_valid_beginner_curriculum_passes():
    """Ensure the beginner helper builds a curriculum that passes validation."""
    validate(make_valid_beginner_curriculum(), level="beginner")


# ---------------------------------------------------------------------------
# Hypothesis strategies
# ---------------------------------------------------------------------------

# Session indices in a beginner curriculum (0-3: session 1, session 2, review, final)
beginner_session_index = st.integers(min_value=0, max_value=3)

# Position within a session's activity list to inject the forbidden activity
# We use a strategy that picks a valid insertion index based on the session
activity_insert_position = st.integers(min_value=0, max_value=20)


# ---------------------------------------------------------------------------
# Property 4: Beginner activity exclusions
# Feature: bilingual-parity-expansion, Property 4: Beginner activity exclusions
# **Validates: Requirements 2.4, 2.5**
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(session_idx=beginner_session_index, insert_pos=activity_insert_position)
def test_rejects_writing_paragraph_in_beginner(session_idx, insert_pos):
    """
    Property 4a: Validator rejects beginner curriculum containing writingParagraph
    in any session.

    For any beginner curriculum JSON where a writingParagraph activity is injected
    into any session, the validator SHALL raise ValueError with a message identifying
    'writingParagraph' as the forbidden activity type.

    # Feature: bilingual-parity-expansion, Property 4: Beginner activity exclusions
    **Validates: Requirements 2.4, 2.5**
    """
    content = copy.deepcopy(make_valid_beginner_curriculum())
    session = content["learningSessions"][session_idx]
    activities = session["activities"]

    # Clamp insert position to valid range
    pos = insert_pos % (len(activities) + 1)

    # Inject a writingParagraph activity
    vocab = ["apple", "house", "garden", "river", "bridge", "forest"]
    forbidden_activity = _make_writing_paragraph_activity(vocab)
    activities.insert(pos, forbidden_activity)

    with pytest.raises(ValueError, match="writingParagraph"):
        validate(content, level="beginner")


@settings(max_examples=100)
@given(session_idx=beginner_session_index, insert_pos=activity_insert_position)
def test_rejects_vocab_level3_in_beginner(session_idx, insert_pos):
    """
    Property 4b: Validator rejects beginner curriculum containing vocabLevel3
    in any session.

    For any beginner curriculum JSON where a vocabLevel3 activity is injected
    into any session, the validator SHALL raise ValueError with a message identifying
    'vocabLevel3' as the forbidden activity type.

    # Feature: bilingual-parity-expansion, Property 4: Beginner activity exclusions
    **Validates: Requirements 2.4, 2.5**
    """
    content = copy.deepcopy(make_valid_beginner_curriculum())
    session = content["learningSessions"][session_idx]
    activities = session["activities"]

    # Clamp insert position to valid range
    pos = insert_pos % (len(activities) + 1)

    # Inject a vocabLevel3 activity
    vocab = ["apple", "house", "garden", "river", "bridge", "forest"]
    forbidden_activity = _make_vocab_level3_activity(vocab)
    activities.insert(pos, forbidden_activity)

    with pytest.raises(ValueError, match="vocabLevel3"):
        validate(content, level="beginner")


@settings(max_examples=100)
@given(
    session_idx=beginner_session_index,
    forbidden_type=st.sampled_from(["writingParagraph", "vocabLevel3"]),
)
def test_error_message_identifies_session(session_idx, forbidden_type):
    """
    Property 4c: Validator error message identifies which session contains the
    forbidden activity.

    For any beginner curriculum JSON where a forbidden activity (writingParagraph
    or vocabLevel3) is injected into a specific session, the error message SHALL
    reference the session number (1-indexed).

    # Feature: bilingual-parity-expansion, Property 4: Beginner activity exclusions
    **Validates: Requirements 2.4, 2.5**
    """
    content = copy.deepcopy(make_valid_beginner_curriculum())
    session = content["learningSessions"][session_idx]

    # Build the forbidden activity
    vocab = ["apple", "house", "garden", "river", "bridge", "forest"]
    if forbidden_type == "writingParagraph":
        forbidden_activity = _make_writing_paragraph_activity(vocab)
    else:
        forbidden_activity = _make_vocab_level3_activity(vocab)

    # Append to the session's activities
    session["activities"].append(forbidden_activity)

    # The error message should mention the session number (1-indexed)
    expected_session_num = str(session_idx + 1)

    with pytest.raises(ValueError) as exc_info:
        validate(content, level="beginner")

    error_msg = str(exc_info.value)
    # Verify the error identifies the forbidden activity type
    assert forbidden_type in error_msg, (
        f"Error message should mention '{forbidden_type}', got: {error_msg}"
    )
    # Verify the error identifies the session (as "Session N")
    assert f"Session {expected_session_num}" in error_msg, (
        f"Error message should mention 'Session {expected_session_num}', got: {error_msg}"
    )


@settings(max_examples=100)
@given(
    forbidden_type=st.sampled_from(["writingParagraph", "vocabLevel3"]),
    replace_idx=st.integers(min_value=0, max_value=8),
)
def test_rejects_forbidden_activity_replacing_existing(forbidden_type, replace_idx):
    """
    Property 4d: Validator rejects beginner curriculum when a forbidden activity
    replaces an existing valid activity in a learning session.

    This tests the scenario where a forbidden activity is not just appended but
    replaces an existing activity at any position in a learning session.

    # Feature: bilingual-parity-expansion, Property 4: Beginner activity exclusions
    **Validates: Requirements 2.4, 2.5**
    """
    content = copy.deepcopy(make_valid_beginner_curriculum())
    # Use the first learning session (index 0)
    session = content["learningSessions"][0]
    activities = session["activities"]

    # Clamp replacement index to valid range
    idx = replace_idx % len(activities)

    # Build the forbidden activity
    vocab = ["apple", "house", "garden", "river", "bridge", "forest"]
    if forbidden_type == "writingParagraph":
        forbidden_activity = _make_writing_paragraph_activity(vocab)
    else:
        forbidden_activity = _make_vocab_level3_activity(vocab)

    # Replace the activity at the chosen index
    activities[idx] = forbidden_activity

    with pytest.raises(ValueError, match=forbidden_type):
        validate(content, level="beginner")
