"""
Property-based tests for validate_content.py — Property 1: Top-level structure validation

# Feature: bilingual-parity-expansion, Property 1: Top-level structure validation

Tests that the validator rejects curriculum JSON with missing/empty top-level fields
(title, description, preview.text, contentTypeTags, learningSessions) for BOTH
beginner and standard levels.

**Validates: Requirements 5.1, 5.2, 11.4**
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
# Helpers: build minimal valid curriculum dicts for beginner and standard
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


def _make_standard_learning_session(session_num, vocab_words):
    """Build a valid standard learning session with 6 vocab words.
    Standard: includes vocabLevel3."""
    activities = [
        _make_text_activity("introAudio"),
        _make_vocab_activity("viewFlashcards", vocab_words),
        _make_vocab_activity("speakFlashcards", vocab_words),
        _make_vocab_activity("vocabLevel1", vocab_words),
        _make_vocab_activity("vocabLevel2", vocab_words),
        _make_vocab_activity("vocabLevel3", vocab_words),
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


def _make_final_session_standard(all_vocab):
    """Build a valid standard final session — includes writingParagraph."""
    activities = [
        _make_text_activity("reading"),
        _make_text_activity("readAlong"),
        _make_writing_paragraph_activity(all_vocab),
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


def make_valid_standard_curriculum():
    """Return a fully valid standard curriculum (5 sessions, 18 words)."""
    vocab_s1 = ["pomme", "maison", "jardin", "soleil", "riviere", "montagne"]
    vocab_s2 = ["ecole", "marche", "plage", "foret", "chateau", "village"]
    vocab_s3 = ["cuisine", "voyage", "musique", "peinture", "theatre", "danse"]
    all_vocab = vocab_s1 + vocab_s2 + vocab_s3

    return {
        "title": "Standard Test Curriculum",
        "description": "A valid standard test curriculum description.",
        "contentTypeTags": [],
        "preview": {"text": "This is a valid preview text for standard testing."},
        "learningSessions": [
            _make_standard_learning_session(1, vocab_s1),
            _make_standard_learning_session(2, vocab_s2),
            _make_standard_learning_session(3, vocab_s3),
            _make_review_session(all_vocab),
            _make_final_session_standard(all_vocab),
        ],
    }


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
# Hypothesis strategies
# ---------------------------------------------------------------------------

# Values that should be rejected as a "non-null, non-empty string"
empty_or_missing_strings = st.one_of(
    st.just(None),
    st.just(""),
    st.just("   "),          # whitespace-only
    st.just(0),
    st.just(False),
    st.just([]),
    st.just({}),
)

# Which top-level string field to corrupt
top_level_string_field = st.sampled_from(["title", "description"])

# Which level to test
level_strategy = st.sampled_from(["beginner", "standard"])


def _get_valid_curriculum(level):
    """Return a deep copy of a valid curriculum for the given level."""
    if level == "beginner":
        return copy.deepcopy(make_valid_beginner_curriculum())
    return copy.deepcopy(make_valid_standard_curriculum())


# ---------------------------------------------------------------------------
# Property 1: Top-level structure validation
# Feature: bilingual-parity-expansion, Property 1: Top-level structure validation
# **Validates: Requirements 5.1, 5.2, 11.4**
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(level=level_strategy, field=top_level_string_field, bad_value=empty_or_missing_strings)
def test_rejects_missing_or_empty_top_level_string_fields(level, field, bad_value):
    """
    Property 1a: Validator rejects curriculum with missing/empty title or description
    at both beginner and standard levels.

    For any curriculum JSON where 'title' or 'description' is null, empty,
    whitespace-only, or a non-string type, the validator SHALL raise ValueError
    with a message mentioning the offending field.

    # Feature: bilingual-parity-expansion, Property 1: Top-level structure validation
    **Validates: Requirements 5.1, 5.2, 11.4**
    """
    content = _get_valid_curriculum(level)
    content[field] = bad_value

    with pytest.raises(ValueError, match=field):
        validate(content, level=level)


@settings(max_examples=100)
@given(level=level_strategy, bad_value=empty_or_missing_strings)
def test_rejects_missing_or_empty_preview_text(level, bad_value):
    """
    Property 1b: Validator rejects curriculum with missing/empty preview.text
    at both beginner and standard levels.

    For any curriculum JSON where 'preview.text' is null, empty,
    whitespace-only, or a non-string type, the validator SHALL raise ValueError
    with a message mentioning 'preview'.

    # Feature: bilingual-parity-expansion, Property 1: Top-level structure validation
    **Validates: Requirements 5.1, 5.2, 11.4**
    """
    content = _get_valid_curriculum(level)
    content["preview"]["text"] = bad_value

    with pytest.raises(ValueError, match="preview"):
        validate(content, level=level)


@settings(max_examples=100)
@given(
    level=level_strategy,
    bad_preview=st.one_of(
        st.just(None),
        st.just("a string"),
        st.just(42),
        st.just([]),
        st.just({}),           # dict without 'text' key
        st.just({"other": 1}), # dict with wrong key
    ),
)
def test_rejects_invalid_preview_object(level, bad_preview):
    """
    Property 1c: Validator rejects curriculum where 'preview' is not a dict
    with a 'text' field, at both beginner and standard levels.

    # Feature: bilingual-parity-expansion, Property 1: Top-level structure validation
    **Validates: Requirements 5.1, 5.2, 11.4**
    """
    content = _get_valid_curriculum(level)
    content["preview"] = bad_preview

    with pytest.raises(ValueError, match="preview"):
        validate(content, level=level)


@settings(max_examples=100)
@given(level=level_strategy)
def test_rejects_missing_content_type_tags(level):
    """
    Property 1d: Validator rejects curriculum with missing contentTypeTags field
    at both beginner and standard levels.

    # Feature: bilingual-parity-expansion, Property 1: Top-level structure validation
    **Validates: Requirements 5.1, 5.2, 11.4**
    """
    content = _get_valid_curriculum(level)
    del content["contentTypeTags"]

    with pytest.raises(ValueError, match="contentTypeTags"):
        validate(content, level=level)


@settings(max_examples=100)
@given(
    level=level_strategy,
    bad_sessions=st.one_of(
        st.just(None),
        st.just("not a list"),
        st.just(42),
        st.just({}),
        st.just([]),  # empty list
    ),
)
def test_rejects_missing_or_invalid_learning_sessions(level, bad_sessions):
    """
    Property 1e: Validator rejects curriculum with missing/empty/non-array
    learningSessions at both beginner and standard levels.

    # Feature: bilingual-parity-expansion, Property 1: Top-level structure validation
    **Validates: Requirements 5.1, 5.2, 11.4**
    """
    content = _get_valid_curriculum(level)
    content["learningSessions"] = bad_sessions

    with pytest.raises(ValueError, match="learningSessions"):
        validate(content, level=level)


@settings(max_examples=100)
@given(
    level=level_strategy,
    field_to_remove=st.sampled_from([
        "title", "description", "preview", "contentTypeTags", "learningSessions",
    ]),
)
def test_rejects_curriculum_with_removed_top_level_field(level, field_to_remove):
    """
    Property 1f: Validator rejects curriculum when any required top-level field
    is completely removed from the dict, at both beginner and standard levels.

    # Feature: bilingual-parity-expansion, Property 1: Top-level structure validation
    **Validates: Requirements 5.1, 5.2, 11.4**
    """
    content = _get_valid_curriculum(level)
    del content[field_to_remove]

    with pytest.raises(ValueError):
        validate(content, level=level)


@settings(max_examples=100)
@given(level=level_strategy)
def test_rejects_non_dict_content(level):
    """
    Property 1g: Validator rejects content that is not a dict,
    at both beginner and standard levels.

    # Feature: bilingual-parity-expansion, Property 1: Top-level structure validation
    **Validates: Requirements 5.1, 5.2, 11.4**
    """
    for bad in [None, "string", 42, [], True]:
        with pytest.raises(ValueError, match="dict"):
            validate(bad, level=level)
