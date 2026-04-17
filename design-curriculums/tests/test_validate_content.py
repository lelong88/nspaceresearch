"""
Property-based tests for validate_content.py

# Feature: multilingual-curriculum-expansion, Property 1: Top-level structure validation

**Validates: Requirements 5.9, 11.1**
"""

import copy
import pytest
from hypothesis import given, settings, assume
from hypothesis import strategies as st

from validate_content import validate


# ---------------------------------------------------------------------------
# Helper: build a minimal valid curriculum dict that passes all validation
# ---------------------------------------------------------------------------

def _make_valid_vocab_activity(activity_type, vocab_list):
    """Create a valid vocab-related activity."""
    return {
        "activityType": activity_type,
        "title": f"{activity_type} title",
        "description": f"{activity_type} description",
        "data": {"vocabList": vocab_list},
    }


def _make_writing_sentence_activity(vocab_list):
    return {
        "activityType": "writingSentence",
        "title": "Writing Sentence",
        "description": "Write sentences",
        "data": {
            "vocabList": vocab_list,
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
            "vocabList": vocab_list,
            "instructions": "Write a paragraph about the topic",
            "prompts": ["First prompt", "Second prompt"],
        },
    }


def _make_text_activity(activity_type):
    return {
        "activityType": activity_type,
        "title": f"{activity_type} title",
        "description": f"{activity_type} description",
        "data": {"text": "Some reading passage text here."},
    }


def _make_learning_session(session_num, vocab_words):
    """Build a valid learning session (sessions 1-3) with 6 vocab words."""
    activities = [
        _make_text_activity("introAudio"),
        _make_valid_vocab_activity("viewFlashcards", vocab_words),
        _make_valid_vocab_activity("speakFlashcards", vocab_words),
        _make_valid_vocab_activity("vocabLevel1", vocab_words),
        _make_valid_vocab_activity("vocabLevel2", vocab_words),
        _make_valid_vocab_activity("vocabLevel3", vocab_words),
        _make_text_activity("reading"),
        _make_text_activity("speakReading"),
        _make_text_activity("readAlong"),
        _make_writing_sentence_activity(vocab_words),
    ]
    return {"title": f"Part {session_num}", "activities": activities}


def _make_review_session(all_vocab):
    """Build a valid review session (session 4)."""
    activities = [
        _make_text_activity("introAudio"),
        _make_valid_vocab_activity("viewFlashcards", all_vocab),
        _make_valid_vocab_activity("speakFlashcards", all_vocab),
        _make_text_activity("reading"),
        _make_text_activity("speakReading"),
        _make_text_activity("readAlong"),
    ]
    return {"title": "Review", "activities": activities}


def _make_final_session(all_vocab):
    """Build a valid final session (session 5)."""
    activities = [
        _make_text_activity("reading"),
        _make_text_activity("readAlong"),
        _make_writing_paragraph_activity(all_vocab),
        _make_text_activity("introAudio"),
    ]
    return {"title": "Final Reading", "activities": activities}


def make_valid_curriculum():
    """Return a fully valid curriculum dict that passes validate()."""
    vocab_s1 = ["pomme", "maison", "jardin", "soleil", "rivière", "montagne"]
    vocab_s2 = ["école", "marché", "plage", "forêt", "château", "village"]
    vocab_s3 = ["cuisine", "voyage", "musique", "peinture", "théâtre", "danse"]
    all_vocab = vocab_s1 + vocab_s2 + vocab_s3

    return {
        "title": "Test Curriculum",
        "description": "A valid test curriculum description.",
        "contentTypeTags": [],
        "preview": {"text": "This is a valid preview text for testing."},
        "learningSessions": [
            _make_learning_session(1, vocab_s1),
            _make_learning_session(2, vocab_s2),
            _make_learning_session(3, vocab_s3),
            _make_review_session(all_vocab),
            _make_final_session(all_vocab),
        ],
    }


# ---------------------------------------------------------------------------
# Sanity check: the base curriculum is actually valid
# ---------------------------------------------------------------------------

def test_valid_curriculum_passes():
    """Ensure our helper builds a curriculum that passes validation."""
    validate(make_valid_curriculum())  # should not raise


# ---------------------------------------------------------------------------
# Hypothesis strategies for generating invalid top-level field values
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


# ---------------------------------------------------------------------------
# Property 1: Top-level structure validation
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(field=top_level_string_field, bad_value=empty_or_missing_strings)
def test_rejects_missing_or_empty_top_level_string_fields(field, bad_value):
    """
    Property 1a: Validator rejects curriculum with missing/empty title or description.

    For any curriculum JSON where 'title' or 'description' is null, empty,
    whitespace-only, or a non-string type, the validator SHALL raise ValueError
    with a message mentioning the offending field.

    # Feature: multilingual-curriculum-expansion, Property 1: Top-level structure validation
    **Validates: Requirements 5.9, 11.1**
    """
    content = make_valid_curriculum()
    content[field] = bad_value

    with pytest.raises(ValueError, match=field):
        validate(content)


@settings(max_examples=100)
@given(bad_value=empty_or_missing_strings)
def test_rejects_missing_or_empty_preview_text(bad_value):
    """
    Property 1b: Validator rejects curriculum with missing/empty preview.text.

    For any curriculum JSON where 'preview.text' is null, empty,
    whitespace-only, or a non-string type, the validator SHALL raise ValueError
    with a message mentioning 'preview'.

    # Feature: multilingual-curriculum-expansion, Property 1: Top-level structure validation
    **Validates: Requirements 5.9, 11.1**
    """
    content = make_valid_curriculum()
    content["preview"]["text"] = bad_value

    with pytest.raises(ValueError, match="preview"):
        validate(content)


@settings(max_examples=100)
@given(
    bad_preview=st.one_of(
        st.just(None),
        st.just("a string"),
        st.just(42),
        st.just([]),
        st.just({}),           # dict without 'text' key
        st.just({"other": 1}), # dict with wrong key
    )
)
def test_rejects_invalid_preview_object(bad_preview):
    """
    Property 1c: Validator rejects curriculum where 'preview' is not a dict
    with a 'text' field.

    # Feature: multilingual-curriculum-expansion, Property 1: Top-level structure validation
    **Validates: Requirements 5.9, 11.1**
    """
    content = make_valid_curriculum()
    content["preview"] = bad_preview

    with pytest.raises(ValueError, match="preview"):
        validate(content)


@settings(max_examples=100)
@given(data=st.data())
def test_rejects_missing_content_type_tags(data):
    """
    Property 1d: Validator rejects curriculum with missing contentTypeTags field.

    # Feature: multilingual-curriculum-expansion, Property 1: Top-level structure validation
    **Validates: Requirements 5.9, 11.1**
    """
    content = make_valid_curriculum()
    del content["contentTypeTags"]

    with pytest.raises(ValueError, match="contentTypeTags"):
        validate(content)


@settings(max_examples=100)
@given(
    bad_sessions=st.one_of(
        st.just(None),
        st.just("not a list"),
        st.just(42),
        st.just({}),
        st.just([]),  # empty list
    )
)
def test_rejects_missing_or_invalid_learning_sessions(bad_sessions):
    """
    Property 1e: Validator rejects curriculum with missing/empty/non-array
    learningSessions.

    # Feature: multilingual-curriculum-expansion, Property 1: Top-level structure validation
    **Validates: Requirements 5.9, 11.1**
    """
    content = make_valid_curriculum()
    content["learningSessions"] = bad_sessions

    with pytest.raises(ValueError, match="learningSessions"):
        validate(content)


@settings(max_examples=100)
@given(
    field_to_remove=st.sampled_from([
        "title", "description", "preview", "contentTypeTags", "learningSessions",
    ])
)
def test_rejects_curriculum_with_removed_top_level_field(field_to_remove):
    """
    Property 1f: Validator rejects curriculum when any required top-level field
    is completely removed from the dict.

    # Feature: multilingual-curriculum-expansion, Property 1: Top-level structure validation
    **Validates: Requirements 5.9, 11.1**
    """
    content = make_valid_curriculum()
    del content[field_to_remove]

    with pytest.raises(ValueError):
        validate(content)


def test_rejects_non_dict_content():
    """
    Property 1g: Validator rejects content that is not a dict.

    # Feature: multilingual-curriculum-expansion, Property 1: Top-level structure validation
    **Validates: Requirements 5.9, 11.1**
    """
    for bad in [None, "string", 42, [], True]:
        with pytest.raises(ValueError, match="dict"):
            validate(bad)


# ---------------------------------------------------------------------------
# Property 2: Session structure invariant
# Feature: multilingual-curriculum-expansion, Property 2: Session structure invariant
# **Validates: Requirements 5.1, 11.2**
# ---------------------------------------------------------------------------

# Strategy: generate session counts that are NOT 5
wrong_session_count = st.integers(min_value=0, max_value=20).filter(lambda n: n != 5)


@settings(max_examples=100)
@given(count=wrong_session_count)
def test_rejects_wrong_session_count(count):
    """
    Property 2a: Validator rejects curriculum with wrong number of sessions.

    For any curriculum JSON where learningSessions has a count != 5,
    the validator SHALL raise ValueError mentioning 'learningSessions' or 'sessions'.

    # Feature: multilingual-curriculum-expansion, Property 2: Session structure invariant
    **Validates: Requirements 5.1, 11.2**
    """
    content = make_valid_curriculum()
    valid_sessions = content["learningSessions"]

    if count == 0:
        content["learningSessions"] = []
    elif count < 5:
        content["learningSessions"] = valid_sessions[:count]
    else:
        # Duplicate sessions to reach the desired count
        extra = [copy.deepcopy(valid_sessions[i % 5]) for i in range(count)]
        content["learningSessions"] = extra

    with pytest.raises(ValueError):
        validate(content)


@settings(max_examples=100)
@given(
    session_idx=st.integers(min_value=0, max_value=4),
    bad_title=st.one_of(
        st.just(None),
        st.just(""),
        st.just("   "),       # whitespace-only
        st.just(0),
        st.just(False),
        st.just([]),
        st.just({}),
    ),
)
def test_rejects_missing_or_empty_session_title(session_idx, bad_title):
    """
    Property 2b: Validator rejects curriculum where any session has a
    missing, empty, whitespace-only, or non-string title.

    # Feature: multilingual-curriculum-expansion, Property 2: Session structure invariant
    **Validates: Requirements 5.1, 11.2**
    """
    content = make_valid_curriculum()
    content["learningSessions"][session_idx]["title"] = bad_title

    with pytest.raises(ValueError, match=f"Session {session_idx + 1}"):
        validate(content)


@settings(max_examples=100)
@given(session_idx=st.integers(min_value=0, max_value=4))
def test_rejects_empty_activities_array(session_idx):
    """
    Property 2c: Validator rejects curriculum where any session has an
    empty activities array.

    # Feature: multilingual-curriculum-expansion, Property 2: Session structure invariant
    **Validates: Requirements 5.1, 11.2**
    """
    content = make_valid_curriculum()
    content["learningSessions"][session_idx]["activities"] = []

    with pytest.raises(ValueError, match=f"Session {session_idx + 1}"):
        validate(content)


@settings(max_examples=100)
@given(
    session_idx=st.integers(min_value=0, max_value=4),
    bad_activities=st.one_of(
        st.just(None),
        st.just("not a list"),
        st.just(42),
        st.just({}),
    ),
)
def test_rejects_non_array_activities(session_idx, bad_activities):
    """
    Property 2d: Validator rejects curriculum where any session has a
    non-array activities field.

    # Feature: multilingual-curriculum-expansion, Property 2: Session structure invariant
    **Validates: Requirements 5.1, 11.2**
    """
    content = make_valid_curriculum()
    content["learningSessions"][session_idx]["activities"] = bad_activities

    with pytest.raises(ValueError, match=f"Session {session_idx + 1}"):
        validate(content)


@settings(max_examples=100)
@given(session_idx=st.integers(min_value=0, max_value=4))
def test_rejects_session_missing_title_key(session_idx):
    """
    Property 2e: Validator rejects curriculum where a session dict is
    missing the 'title' key entirely.

    # Feature: multilingual-curriculum-expansion, Property 2: Session structure invariant
    **Validates: Requirements 5.1, 11.2**
    """
    content = make_valid_curriculum()
    del content["learningSessions"][session_idx]["title"]

    with pytest.raises(ValueError, match=f"Session {session_idx + 1}"):
        validate(content)


@settings(max_examples=100)
@given(session_idx=st.integers(min_value=0, max_value=4))
def test_rejects_session_missing_activities_key(session_idx):
    """
    Property 2f: Validator rejects curriculum where a session dict is
    missing the 'activities' key entirely.

    # Feature: multilingual-curriculum-expansion, Property 2: Session structure invariant
    **Validates: Requirements 5.1, 11.2**
    """
    content = make_valid_curriculum()
    del content["learningSessions"][session_idx]["activities"]

    with pytest.raises(ValueError, match=f"Session {session_idx + 1}"):
        validate(content)


# ---------------------------------------------------------------------------
# Property 3: Vocabulary distribution invariant
# Feature: multilingual-curriculum-expansion, Property 3: Vocabulary distribution invariant
# **Validates: Requirements 3.4, 5.2, 11.10**
# ---------------------------------------------------------------------------


def _set_session_vocab(content, session_idx, new_vocab):
    """Replace all vocabList arrays in a learning session with new_vocab."""
    session = content["learningSessions"][session_idx]
    for activity in session["activities"]:
        at = activity.get("activityType")
        if at in (
            "viewFlashcards",
            "speakFlashcards",
            "vocabLevel1",
            "vocabLevel2",
            "vocabLevel3",
        ):
            activity["data"]["vocabList"] = list(new_vocab)
        elif at == "writingSentence":
            activity["data"]["vocabList"] = list(new_vocab)
            # Keep items consistent with new vocab
            activity["data"]["items"] = [
                {"prompt": f"Use '{w}' in a sentence", "targetVocab": w}
                for w in new_vocab
            ]


# Strategy: generate a count of vocab words that is NOT 6
wrong_per_session_count = st.integers(min_value=1, max_value=15).filter(lambda n: n != 6)


@settings(max_examples=100)
@given(
    session_idx=st.integers(min_value=0, max_value=2),
    word_count=wrong_per_session_count,
)
def test_rejects_wrong_vocab_count_per_session(session_idx, word_count):
    """
    Property 3a: Validator rejects curriculum where a learning session
    has a number of unique vocabulary words other than 6.

    For any learning session (1-3) with fewer or more than 6 unique vocab
    words, the validator SHALL raise ValueError mentioning the session and
    the word count.

    # Feature: multilingual-curriculum-expansion, Property 3: Vocabulary distribution invariant
    **Validates: Requirements 3.4, 5.2, 11.10**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)

    # Generate a vocab list of the wrong size using unique words
    base_words = [f"testwort{i}" for i in range(word_count)]
    _set_session_vocab(content, session_idx, base_words)

    with pytest.raises(ValueError, match=f"Session {session_idx + 1}"):
        validate(content)


@settings(max_examples=100)
@given(
    session_pair=st.sampled_from([(0, 1), (0, 2), (1, 2)]),
    overlap_count=st.integers(min_value=1, max_value=6),
)
def test_rejects_duplicate_vocab_across_sessions(session_pair, overlap_count):
    """
    Property 3b: Validator rejects curriculum where vocabulary words are
    duplicated across learning sessions, causing total unique count < 18.

    For any pair of learning sessions that share one or more vocabulary words,
    the total unique count drops below 18 and the validator SHALL raise
    ValueError.

    # Feature: multilingual-curriculum-expansion, Property 3: Vocabulary distribution invariant
    **Validates: Requirements 3.4, 5.2, 11.10**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)

    src_idx, dst_idx = session_pair

    # Get the source session's vocab
    src_session = content["learningSessions"][src_idx]
    src_vocab = None
    for act in src_session["activities"]:
        if act.get("activityType") == "viewFlashcards":
            src_vocab = act["data"]["vocabList"]
            break
    assume(src_vocab is not None)

    # Get the destination session's current vocab
    dst_session = content["learningSessions"][dst_idx]
    dst_vocab = None
    for act in dst_session["activities"]:
        if act.get("activityType") == "viewFlashcards":
            dst_vocab = list(act["data"]["vocabList"])
            break
    assume(dst_vocab is not None)

    # Replace `overlap_count` words in dst with words from src
    actual_overlap = min(overlap_count, len(src_vocab), len(dst_vocab))
    assume(actual_overlap > 0)

    new_dst_vocab = list(dst_vocab)
    for i in range(actual_overlap):
        new_dst_vocab[i] = src_vocab[i]

    _set_session_vocab(content, dst_idx, new_dst_vocab)

    with pytest.raises(ValueError):
        validate(content)


@settings(max_examples=100)
@given(
    session_idx=st.integers(min_value=0, max_value=2),
)
def test_rejects_empty_vocab_in_learning_session(session_idx):
    """
    Property 3c: Validator rejects curriculum where a learning session
    has no vocabulary words at all (empty vocabList on all vocab activities).

    # Feature: multilingual-curriculum-expansion, Property 3: Vocabulary distribution invariant
    **Validates: Requirements 3.4, 5.2, 11.10**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)

    # Remove all vocab activities from the session, leaving only non-vocab ones
    session = content["learningSessions"][session_idx]
    session["activities"] = [
        act for act in session["activities"]
        if act.get("activityType") not in (
            "viewFlashcards", "speakFlashcards",
            "vocabLevel1", "vocabLevel2", "vocabLevel3",
            "writingSentence",
        )
    ]
    # Ensure activities is still non-empty (has introAudio, reading, etc.)
    assume(len(session["activities"]) > 0)

    with pytest.raises(ValueError, match=f"Session {session_idx + 1}"):
        validate(content)


@settings(max_examples=100)
@given(
    extra_words=st.lists(
        st.from_regex(r"[a-z]{3,10}", fullmatch=True),
        min_size=1,
        max_size=4,
    ),
)
def test_rejects_session_with_more_than_six_unique_words(extra_words):
    """
    Property 3d: Validator rejects curriculum where session 1 has more
    than 6 unique vocabulary words (original 6 + extras).

    # Feature: multilingual-curriculum-expansion, Property 3: Vocabulary distribution invariant
    **Validates: Requirements 3.4, 5.2, 11.10**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)

    # Get session 1's current vocab
    session = content["learningSessions"][0]
    current_vocab = None
    for act in session["activities"]:
        if act.get("activityType") == "viewFlashcards":
            current_vocab = list(act["data"]["vocabList"])
            break
    assume(current_vocab is not None)

    # Add extra unique words that don't overlap with any existing vocab
    all_existing = set()
    for i in range(3):
        for act in content["learningSessions"][i]["activities"]:
            if act.get("activityType") in ("viewFlashcards",):
                all_existing.update(act["data"]["vocabList"])

    unique_extras = [w for w in extra_words if w not in all_existing and w not in current_vocab]
    assume(len(unique_extras) > 0)

    expanded_vocab = current_vocab + unique_extras
    _set_session_vocab(content, 0, expanded_vocab)

    with pytest.raises(ValueError, match="Session 1"):
        validate(content)


# ---------------------------------------------------------------------------
# Property 4: Activity structure completeness
# Feature: multilingual-curriculum-expansion, Property 4: Activity structure completeness
# **Validates: Requirements 5.6, 11.3, 11.4**
# ---------------------------------------------------------------------------

from validate_content import VALID_ACTIVITY_TYPES

# Strategy: pick a random session and activity index within that session
session_idx_st = st.integers(min_value=0, max_value=4)

# Strategy: generate strings that are NOT valid activity types
invalid_activity_type_st = st.text(min_size=1, max_size=30).filter(
    lambda s: s not in VALID_ACTIVITY_TYPES
)

# Required activity fields (besides activityType which has its own tests)
required_activity_fields = st.sampled_from(["title", "description", "data"])


@settings(max_examples=100)
@given(session_idx=session_idx_st)
def test_rejects_activity_missing_activity_type(session_idx):
    """
    Property 4a: Validator rejects activity with missing activityType field.

    For any activity in any session where 'activityType' is absent,
    the validator SHALL raise ValueError with a message about the missing field.

    # Feature: multilingual-curriculum-expansion, Property 4: Activity structure completeness
    **Validates: Requirements 5.6, 11.3, 11.4**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)

    # Remove activityType from the first activity in the chosen session
    activity = content["learningSessions"][session_idx]["activities"][0]
    del activity["activityType"]

    with pytest.raises(ValueError, match="activityType"):
        validate(content)


@settings(max_examples=100)
@given(session_idx=session_idx_st)
def test_rejects_activity_using_type_instead_of_activity_type(session_idx):
    """
    Property 4b: Validator rejects activity using 'type' instead of 'activityType'.

    For any activity that has a 'type' field but no 'activityType' field,
    the validator SHALL raise ValueError mentioning the old schema corruption.

    # Feature: multilingual-curriculum-expansion, Property 4: Activity structure completeness
    **Validates: Requirements 5.6, 11.3, 11.4**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)

    activity = content["learningSessions"][session_idx]["activities"][0]
    # Replace activityType with type
    old_type = activity.pop("activityType")
    activity["type"] = old_type

    with pytest.raises(ValueError, match="type"):
        validate(content)


@settings(max_examples=100)
@given(
    session_idx=session_idx_st,
    bad_type=invalid_activity_type_st,
)
def test_rejects_activity_with_invalid_activity_type(session_idx, bad_type):
    """
    Property 4c: Validator rejects activity with an activityType value not in
    the 11 valid types.

    For any activity whose activityType is a non-empty string that is not one
    of the 11 valid values, the validator SHALL raise ValueError mentioning
    'invalid activityType'.

    # Feature: multilingual-curriculum-expansion, Property 4: Activity structure completeness
    **Validates: Requirements 5.6, 11.3, 11.4**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)

    activity = content["learningSessions"][session_idx]["activities"][0]
    activity["activityType"] = bad_type

    with pytest.raises(ValueError, match="activityType"):
        validate(content)


@settings(max_examples=100)
@given(
    session_idx=session_idx_st,
    field=required_activity_fields,
)
def test_rejects_activity_missing_required_field(session_idx, field):
    """
    Property 4d: Validator rejects activity missing 'title', 'description',
    or 'data' field.

    For any activity in any session where one of the required fields is removed,
    the validator SHALL raise ValueError mentioning the missing field.

    # Feature: multilingual-curriculum-expansion, Property 4: Activity structure completeness
    **Validates: Requirements 5.6, 11.3, 11.4**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)

    activity = content["learningSessions"][session_idx]["activities"][0]
    del activity[field]

    with pytest.raises(ValueError, match=field):
        validate(content)


@settings(max_examples=100)
@given(
    session_idx=session_idx_st,
    bad_value=st.one_of(
        st.just(None),
        st.just(""),
        st.just(0),
        st.just(False),
        st.just([]),
    ),
)
def test_rejects_activity_with_empty_activity_type(session_idx, bad_value):
    """
    Property 4e: Validator rejects activity where activityType is empty,
    null, or a non-string type.

    # Feature: multilingual-curriculum-expansion, Property 4: Activity structure completeness
    **Validates: Requirements 5.6, 11.3, 11.4**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)

    activity = content["learningSessions"][session_idx]["activities"][0]
    activity["activityType"] = bad_value

    with pytest.raises(ValueError, match="activityType"):
        validate(content)


@settings(max_examples=100)
@given(session_idx=session_idx_st)
def test_rejects_activity_with_data_not_a_dict(session_idx):
    """
    Property 4f: Validator rejects activity where 'data' is not a dict.

    For any activity where 'data' is replaced with a non-dict value,
    the validator SHALL raise ValueError mentioning 'data'.

    # Feature: multilingual-curriculum-expansion, Property 4: Activity structure completeness
    **Validates: Requirements 5.6, 11.3, 11.4**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)

    activity = content["learningSessions"][session_idx]["activities"][0]
    activity["data"] = "not a dict"

    with pytest.raises(ValueError, match="data"):
        validate(content)


# ---------------------------------------------------------------------------
# Property 5: VocabList format enforcement
# Feature: multilingual-curriculum-expansion, Property 5: VocabList format enforcement
# **Validates: Requirements 5.7, 11.5**
# ---------------------------------------------------------------------------

# Vocab activity types that require vocabList validation
_VOCAB_ACTIVITY_TYPES = [
    "viewFlashcards",
    "speakFlashcards",
    "vocabLevel1",
    "vocabLevel2",
    "vocabLevel3",
]

# Strategy: pick a vocab activity type
vocab_activity_type_st = st.sampled_from(_VOCAB_ACTIVITY_TYPES)

# Strategy: pick a learning session (0-2) where vocab activities live
learning_session_st = st.integers(min_value=0, max_value=2)

# Strategy: generate strings that contain at least one uppercase character
uppercase_word_st = st.from_regex(r"[a-z]*[A-Z][a-zA-Z]*", fullmatch=True).filter(
    lambda s: s != s.lower()
)

# Strategy: generate non-string elements that could sneak into vocabList
non_string_element_st = st.one_of(
    st.integers(),
    st.booleans(),
    st.lists(st.text(min_size=0, max_size=5), min_size=0, max_size=3),
    st.dictionaries(st.text(min_size=1, max_size=5), st.text(min_size=0, max_size=5), min_size=0, max_size=3),
)


def _set_all_vocab_activities_in_session(content, session_idx, mutator):
    """Apply a mutator function to the data dict of every vocab activity in a session.

    This ensures ALL vocab activities are mutated consistently so the test
    doesn't fail on a different activity's check first.
    """
    session = content["learningSessions"][session_idx]
    for activity in session["activities"]:
        at = activity.get("activityType")
        if at in _VOCAB_ACTIVITY_TYPES:
            mutator(activity["data"], at)


@settings(max_examples=100)
@given(
    session_idx=learning_session_st,
    uppercase_word=uppercase_word_st,
    position=st.integers(min_value=0, max_value=5),
)
def test_rejects_uppercase_strings_in_vocab_list(session_idx, uppercase_word, position):
    """
    Property 5a: Validator rejects vocab activities with uppercase strings in vocabList.

    For any vocab activity (viewFlashcards, speakFlashcards, vocabLevel1,
    vocabLevel2, vocabLevel3) where any element in vocabList contains uppercase
    characters, the validator SHALL raise ValueError mentioning 'lowercase'.

    # Feature: multilingual-curriculum-expansion, Property 5: VocabList format enforcement
    **Validates: Requirements 5.7, 11.5**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)

    # Clamp position to valid index range (0-5 for 6-word vocab)
    idx = position % 6

    def inject_uppercase(data, _at):
        vocab = list(data["vocabList"])
        vocab[idx] = uppercase_word
        data["vocabList"] = vocab

    _set_all_vocab_activities_in_session(content, session_idx, inject_uppercase)

    with pytest.raises(ValueError, match="lowercase"):
        validate(content)


@settings(max_examples=100)
@given(
    session_idx=learning_session_st,
    bad_element=non_string_element_st,
    position=st.integers(min_value=0, max_value=5),
)
def test_rejects_non_string_elements_in_vocab_list(session_idx, bad_element, position):
    """
    Property 5b: Validator rejects vocab activities with non-string elements in vocabList.

    For any vocab activity where vocabList contains a non-string element
    (number, boolean, list, dict), the validator SHALL raise ValueError
    mentioning 'string'.

    # Feature: multilingual-curriculum-expansion, Property 5: VocabList format enforcement
    **Validates: Requirements 5.7, 11.5**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)

    idx = position % 6

    def inject_non_string(data, _at):
        vocab = list(data["vocabList"])
        vocab[idx] = bad_element
        data["vocabList"] = vocab

    _set_all_vocab_activities_in_session(content, session_idx, inject_non_string)

    with pytest.raises(ValueError, match="string"):
        validate(content)


@settings(max_examples=100)
@given(session_idx=learning_session_st)
def test_rejects_words_field_name_instead_of_vocab_list(session_idx):
    """
    Property 5c: Validator rejects vocab activities using 'words' field name
    instead of 'vocabList'.

    For any vocab activity where the field is named 'words' instead of
    'vocabList', the validator SHALL raise ValueError mentioning 'words'.

    # Feature: multilingual-curriculum-expansion, Property 5: VocabList format enforcement
    **Validates: Requirements 5.7, 11.5**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)

    def rename_to_words(data, _at):
        vocab = data.pop("vocabList")
        data["words"] = vocab

    _set_all_vocab_activities_in_session(content, session_idx, rename_to_words)

    with pytest.raises(ValueError, match="words"):
        validate(content)


# ---------------------------------------------------------------------------
# Property 6: Flashcard vocabList consistency
# Feature: multilingual-curriculum-expansion, Property 6: Flashcard vocabList consistency
# **Validates: Requirements 5.8, 11.6**
# ---------------------------------------------------------------------------


def _get_view_flashcards_vocab(content, session_idx):
    """Return the vocabList from the viewFlashcards activity in a session."""
    session = content["learningSessions"][session_idx]
    for activity in session["activities"]:
        if activity.get("activityType") == "viewFlashcards":
            return list(activity["data"]["vocabList"])
    return None


def _set_speak_flashcards_vocab(content, session_idx, new_vocab):
    """Replace only the speakFlashcards vocabList in a session."""
    session = content["learningSessions"][session_idx]
    for activity in session["activities"]:
        if activity.get("activityType") == "speakFlashcards":
            activity["data"]["vocabList"] = new_vocab


@settings(max_examples=100)
@given(
    session_idx=st.integers(min_value=0, max_value=4),
)
def test_rejects_shuffled_speak_flashcards_vocab(session_idx):
    """
    Property 6a: Validator rejects session where speakFlashcards vocabList
    has the same elements as viewFlashcards but in a different order.

    The validator requires identical arrays (same elements, same order).

    # Feature: multilingual-curriculum-expansion, Property 6: Flashcard vocabList consistency
    **Validates: Requirements 5.8, 11.6**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)

    view_vocab = _get_view_flashcards_vocab(content, session_idx)
    assume(view_vocab is not None and len(view_vocab) >= 2)

    # Create a reversed copy (guaranteed different order for lists with 2+ elements)
    shuffled = list(reversed(view_vocab))
    assume(shuffled != view_vocab)

    _set_speak_flashcards_vocab(content, session_idx, shuffled)

    with pytest.raises(ValueError, match="mismatched"):
        validate(content)


@settings(max_examples=100)
@given(
    session_idx=st.integers(min_value=0, max_value=4),
    extra_word=st.from_regex(r"[a-z]{3,10}", fullmatch=True),
)
def test_rejects_speak_flashcards_with_extra_element(session_idx, extra_word):
    """
    Property 6b: Validator rejects session where speakFlashcards vocabList
    has more elements than viewFlashcards (different length).

    # Feature: multilingual-curriculum-expansion, Property 6: Flashcard vocabList consistency
    **Validates: Requirements 5.8, 11.6**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)

    view_vocab = _get_view_flashcards_vocab(content, session_idx)
    assume(view_vocab is not None)
    assume(extra_word not in view_vocab)

    longer_vocab = list(view_vocab) + [extra_word]
    _set_speak_flashcards_vocab(content, session_idx, longer_vocab)

    with pytest.raises(ValueError, match="mismatched"):
        validate(content)


@settings(max_examples=100)
@given(
    session_idx=st.integers(min_value=0, max_value=4),
)
def test_rejects_speak_flashcards_with_fewer_elements(session_idx):
    """
    Property 6c: Validator rejects session where speakFlashcards vocabList
    has fewer elements than viewFlashcards.

    # Feature: multilingual-curriculum-expansion, Property 6: Flashcard vocabList consistency
    **Validates: Requirements 5.8, 11.6**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)

    view_vocab = _get_view_flashcards_vocab(content, session_idx)
    assume(view_vocab is not None and len(view_vocab) >= 2)

    shorter_vocab = view_vocab[:-1]
    _set_speak_flashcards_vocab(content, session_idx, shorter_vocab)

    with pytest.raises(ValueError, match="mismatched"):
        validate(content)


@settings(max_examples=100)
@given(
    session_idx=st.integers(min_value=0, max_value=4),
    replacement_word=st.from_regex(r"[a-z]{3,10}", fullmatch=True),
    position=st.integers(min_value=0, max_value=5),
)
def test_rejects_speak_flashcards_with_different_element(session_idx, replacement_word, position):
    """
    Property 6d: Validator rejects session where speakFlashcards vocabList
    has one element replaced with a different word.

    # Feature: multilingual-curriculum-expansion, Property 6: Flashcard vocabList consistency
    **Validates: Requirements 5.8, 11.6**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)

    view_vocab = _get_view_flashcards_vocab(content, session_idx)
    assume(view_vocab is not None and len(view_vocab) > 0)

    idx = position % len(view_vocab)
    assume(replacement_word != view_vocab[idx])

    modified_vocab = list(view_vocab)
    modified_vocab[idx] = replacement_word
    assume(modified_vocab != view_vocab)

    _set_speak_flashcards_vocab(content, session_idx, modified_vocab)

    with pytest.raises(ValueError, match="mismatched"):
        validate(content)


@settings(max_examples=100)
@given(
    session_idx=st.integers(min_value=0, max_value=4),
    random_words=st.lists(
        st.from_regex(r"[a-z]{3,10}", fullmatch=True),
        min_size=1,
        max_size=10,
    ),
)
def test_rejects_speak_flashcards_with_completely_different_vocab(session_idx, random_words):
    """
    Property 6e: Validator rejects session where speakFlashcards vocabList
    is a completely different set of words from viewFlashcards.

    # Feature: multilingual-curriculum-expansion, Property 6: Flashcard vocabList consistency
    **Validates: Requirements 5.8, 11.6**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)

    view_vocab = _get_view_flashcards_vocab(content, session_idx)
    assume(view_vocab is not None)
    assume(random_words != view_vocab)

    _set_speak_flashcards_vocab(content, session_idx, random_words)

    with pytest.raises(ValueError, match="mismatched"):
        validate(content)


# ---------------------------------------------------------------------------
# Property 7: Writing activity structure
# Feature: multilingual-curriculum-expansion, Property 7: Writing activity structure
# **Validates: Requirements 11.7, 11.8**
# ---------------------------------------------------------------------------


def _find_writing_sentence_activity(content, session_idx):
    """Return the index of the writingSentence activity in a session, or None."""
    session = content["learningSessions"][session_idx]
    for i, activity in enumerate(session["activities"]):
        if activity.get("activityType") == "writingSentence":
            return i
    return None


def _find_writing_paragraph_activity(content, session_idx):
    """Return the index of the writingParagraph activity in a session, or None."""
    session = content["learningSessions"][session_idx]
    for i, activity in enumerate(session["activities"]):
        if activity.get("activityType") == "writingParagraph":
            return i
    return None


# --- writingSentence tests (sessions 1-3) ---

@settings(max_examples=100)
@given(session_idx=st.integers(min_value=0, max_value=2))
def test_rejects_writing_sentence_missing_vocab_list(session_idx):
    """
    Property 7a: Validator rejects writingSentence activity with missing data.vocabList.

    For any writingSentence activity where data.vocabList is absent,
    the validator SHALL raise ValueError mentioning 'vocabList'.

    # Feature: multilingual-curriculum-expansion, Property 7: Writing activity structure
    **Validates: Requirements 11.7, 11.8**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)

    act_idx = _find_writing_sentence_activity(content, session_idx)
    assume(act_idx is not None)

    del content["learningSessions"][session_idx]["activities"][act_idx]["data"]["vocabList"]

    with pytest.raises(ValueError, match="vocabList"):
        validate(content)


@settings(max_examples=100)
@given(session_idx=st.integers(min_value=0, max_value=2))
def test_rejects_writing_sentence_missing_items(session_idx):
    """
    Property 7b: Validator rejects writingSentence activity with missing data.items.

    For any writingSentence activity where data.items is absent,
    the validator SHALL raise ValueError mentioning 'items'.

    # Feature: multilingual-curriculum-expansion, Property 7: Writing activity structure
    **Validates: Requirements 11.7, 11.8**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)

    act_idx = _find_writing_sentence_activity(content, session_idx)
    assume(act_idx is not None)

    del content["learningSessions"][session_idx]["activities"][act_idx]["data"]["items"]

    with pytest.raises(ValueError, match="items"):
        validate(content)


@settings(max_examples=100)
@given(session_idx=st.integers(min_value=0, max_value=2))
def test_rejects_writing_sentence_empty_items(session_idx):
    """
    Property 7c: Validator rejects writingSentence activity with empty data.items array.

    For any writingSentence activity where data.items is an empty array,
    the validator SHALL raise ValueError mentioning 'items'.

    # Feature: multilingual-curriculum-expansion, Property 7: Writing activity structure
    **Validates: Requirements 11.7, 11.8**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)

    act_idx = _find_writing_sentence_activity(content, session_idx)
    assume(act_idx is not None)

    content["learningSessions"][session_idx]["activities"][act_idx]["data"]["items"] = []

    with pytest.raises(ValueError, match="items"):
        validate(content)


@settings(max_examples=100)
@given(
    session_idx=st.integers(min_value=0, max_value=2),
    field_to_remove=st.sampled_from(["prompt", "targetVocab"]),
)
def test_rejects_writing_sentence_item_missing_required_field(session_idx, field_to_remove):
    """
    Property 7d: Validator rejects writingSentence activity where an item
    is missing 'prompt' or 'targetVocab'.

    For any writingSentence item where a required field is absent or empty,
    the validator SHALL raise ValueError mentioning the missing field.

    # Feature: multilingual-curriculum-expansion, Property 7: Writing activity structure
    **Validates: Requirements 11.7, 11.8**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)

    act_idx = _find_writing_sentence_activity(content, session_idx)
    assume(act_idx is not None)

    items = content["learningSessions"][session_idx]["activities"][act_idx]["data"]["items"]
    assume(len(items) > 0)

    del items[0][field_to_remove]

    with pytest.raises(ValueError, match=field_to_remove):
        validate(content)


@settings(max_examples=100)
@given(
    session_idx=st.integers(min_value=0, max_value=2),
    field_to_empty=st.sampled_from(["prompt", "targetVocab"]),
    bad_value=st.one_of(
        st.just(None),
        st.just(""),
        st.just("   "),
    ),
)
def test_rejects_writing_sentence_item_empty_required_field(session_idx, field_to_empty, bad_value):
    """
    Property 7e: Validator rejects writingSentence activity where an item
    has an empty, null, or whitespace-only 'prompt' or 'targetVocab'.

    # Feature: multilingual-curriculum-expansion, Property 7: Writing activity structure
    **Validates: Requirements 11.7, 11.8**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)

    act_idx = _find_writing_sentence_activity(content, session_idx)
    assume(act_idx is not None)

    items = content["learningSessions"][session_idx]["activities"][act_idx]["data"]["items"]
    assume(len(items) > 0)

    items[0][field_to_empty] = bad_value

    with pytest.raises(ValueError, match=field_to_empty):
        validate(content)


# --- writingParagraph tests (session 5, index 4) ---

@settings(max_examples=100)
@given(data=st.data())
def test_rejects_writing_paragraph_missing_vocab_list(data):
    """
    Property 7f: Validator rejects writingParagraph activity with missing data.vocabList.

    For any writingParagraph activity where data.vocabList is absent,
    the validator SHALL raise ValueError mentioning 'vocabList'.

    # Feature: multilingual-curriculum-expansion, Property 7: Writing activity structure
    **Validates: Requirements 11.7, 11.8**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)

    act_idx = _find_writing_paragraph_activity(content, 4)
    assume(act_idx is not None)

    del content["learningSessions"][4]["activities"][act_idx]["data"]["vocabList"]

    with pytest.raises(ValueError, match="vocabList"):
        validate(content)


@settings(max_examples=100)
@given(data=st.data())
def test_rejects_writing_paragraph_missing_instructions(data):
    """
    Property 7g: Validator rejects writingParagraph activity with missing data.instructions.

    For any writingParagraph activity where data.instructions is absent,
    the validator SHALL raise ValueError mentioning 'instructions'.

    # Feature: multilingual-curriculum-expansion, Property 7: Writing activity structure
    **Validates: Requirements 11.7, 11.8**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)

    act_idx = _find_writing_paragraph_activity(content, 4)
    assume(act_idx is not None)

    del content["learningSessions"][4]["activities"][act_idx]["data"]["instructions"]

    with pytest.raises(ValueError, match="instructions"):
        validate(content)


@settings(max_examples=100)
@given(
    bad_value=st.one_of(
        st.just(None),
        st.just(""),
        st.just("   "),
        st.just(0),
        st.just(False),
        st.just([]),
    ),
)
def test_rejects_writing_paragraph_empty_instructions(bad_value):
    """
    Property 7h: Validator rejects writingParagraph activity where data.instructions
    is empty, null, whitespace-only, or a non-string type.

    # Feature: multilingual-curriculum-expansion, Property 7: Writing activity structure
    **Validates: Requirements 11.7, 11.8**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)

    act_idx = _find_writing_paragraph_activity(content, 4)
    assume(act_idx is not None)

    content["learningSessions"][4]["activities"][act_idx]["data"]["instructions"] = bad_value

    with pytest.raises(ValueError, match="instructions"):
        validate(content)


@settings(max_examples=100)
@given(data=st.data())
def test_rejects_writing_paragraph_missing_prompts(data):
    """
    Property 7i: Validator rejects writingParagraph activity with missing data.prompts.

    For any writingParagraph activity where data.prompts is absent,
    the validator SHALL raise ValueError mentioning 'prompts'.

    # Feature: multilingual-curriculum-expansion, Property 7: Writing activity structure
    **Validates: Requirements 11.7, 11.8**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)

    act_idx = _find_writing_paragraph_activity(content, 4)
    assume(act_idx is not None)

    del content["learningSessions"][4]["activities"][act_idx]["data"]["prompts"]

    with pytest.raises(ValueError, match="prompts"):
        validate(content)


@settings(max_examples=100)
@given(
    prompt_count=st.integers(min_value=0, max_value=1),
)
def test_rejects_writing_paragraph_fewer_than_two_prompts(prompt_count):
    """
    Property 7j: Validator rejects writingParagraph activity where data.prompts
    has fewer than 2 items.

    # Feature: multilingual-curriculum-expansion, Property 7: Writing activity structure
    **Validates: Requirements 11.7, 11.8**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)

    act_idx = _find_writing_paragraph_activity(content, 4)
    assume(act_idx is not None)

    prompts = ["A single prompt"] if prompt_count == 1 else []
    content["learningSessions"][4]["activities"][act_idx]["data"]["prompts"] = prompts

    with pytest.raises(ValueError, match="prompts"):
        validate(content)


@settings(max_examples=100)
@given(
    non_string_prompt=st.one_of(
        st.integers(),
        st.booleans(),
        st.just(None),
        st.lists(st.text(min_size=0, max_size=5), min_size=0, max_size=2),
        st.dictionaries(st.text(min_size=1, max_size=5), st.text(min_size=0, max_size=5), min_size=0, max_size=2),
    ),
    position=st.integers(min_value=0, max_value=1),
)
def test_rejects_writing_paragraph_non_string_prompts(non_string_prompt, position):
    """
    Property 7k: Validator rejects writingParagraph activity where data.prompts
    contains a non-string element.

    For any writingParagraph activity where any element in data.prompts is not
    a string, the validator SHALL raise ValueError mentioning 'prompts'.

    # Feature: multilingual-curriculum-expansion, Property 7: Writing activity structure
    **Validates: Requirements 11.7, 11.8**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)

    act_idx = _find_writing_paragraph_activity(content, 4)
    assume(act_idx is not None)

    prompts = list(content["learningSessions"][4]["activities"][act_idx]["data"]["prompts"])
    prompts[position] = non_string_prompt
    content["learningSessions"][4]["activities"][act_idx]["data"]["prompts"] = prompts

    with pytest.raises(ValueError, match="prompts"):
        validate(content)


# ---------------------------------------------------------------------------
# Property 8: Strip keys exclusion
# Feature: multilingual-curriculum-expansion, Property 8: Strip keys exclusion
# **Validates: Requirements 5.10, 11.9**
# ---------------------------------------------------------------------------

from validate_content import STRIP_KEYS

# Strategy: pick any strip key
strip_key_st = st.sampled_from(sorted(STRIP_KEYS))


@settings(max_examples=100)
@given(strip_key=strip_key_st)
def test_rejects_strip_key_at_top_level(strip_key):
    """
    Property 8a: Validator rejects curriculum with a strip-key at the top level.

    For any curriculum JSON where a strip-key appears as a top-level field,
    the validator SHALL raise ValueError mentioning the specific strip-key name.

    # Feature: multilingual-curriculum-expansion, Property 8: Strip keys exclusion
    **Validates: Requirements 5.10, 11.9**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)
    content[strip_key] = "should_not_be_here"

    with pytest.raises(ValueError, match=strip_key):
        validate(content)


@settings(max_examples=100)
@given(
    strip_key=strip_key_st,
    session_idx=st.integers(min_value=0, max_value=4),
)
def test_rejects_strip_key_inside_session(strip_key, session_idx):
    """
    Property 8b: Validator rejects curriculum with a strip-key inside a session object.

    For any session in the curriculum where a strip-key is injected as a field,
    the validator SHALL raise ValueError mentioning the specific strip-key name.

    # Feature: multilingual-curriculum-expansion, Property 8: Strip keys exclusion
    **Validates: Requirements 5.10, 11.9**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)
    content["learningSessions"][session_idx][strip_key] = "injected"

    with pytest.raises(ValueError, match=strip_key):
        validate(content)


@settings(max_examples=100)
@given(
    strip_key=strip_key_st,
    session_idx=st.integers(min_value=0, max_value=4),
)
def test_rejects_strip_key_inside_activity(strip_key, session_idx):
    """
    Property 8c: Validator rejects curriculum with a strip-key inside an activity object.

    For any activity in any session where a strip-key is injected as a field,
    the validator SHALL raise ValueError mentioning the specific strip-key name.

    # Feature: multilingual-curriculum-expansion, Property 8: Strip keys exclusion
    **Validates: Requirements 5.10, 11.9**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)
    activities = content["learningSessions"][session_idx]["activities"]
    activities[0][strip_key] = "injected"

    with pytest.raises(ValueError, match=strip_key):
        validate(content)


@settings(max_examples=100)
@given(
    strip_key=strip_key_st,
    session_idx=st.integers(min_value=0, max_value=4),
)
def test_rejects_strip_key_inside_activity_data(strip_key, session_idx):
    """
    Property 8d: Validator rejects curriculum with a strip-key inside an activity's data object.

    For any activity in any session where a strip-key is injected inside the
    'data' dict, the validator SHALL raise ValueError mentioning the specific
    strip-key name.

    # Feature: multilingual-curriculum-expansion, Property 8: Strip keys exclusion
    **Validates: Requirements 5.10, 11.9**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)
    activities = content["learningSessions"][session_idx]["activities"]
    activities[0]["data"][strip_key] = "injected"

    with pytest.raises(ValueError, match=strip_key):
        validate(content)


@settings(max_examples=100)
@given(
    strip_key=strip_key_st,
    nesting_depth=st.integers(min_value=1, max_value=5),
)
def test_rejects_strip_key_at_deep_nesting(strip_key, nesting_depth):
    """
    Property 8e: Validator rejects curriculum with a strip-key buried at
    arbitrary nesting depth inside the JSON tree.

    For any curriculum JSON where a strip-key is injected inside nested dicts
    within an activity's data, the validator SHALL raise ValueError mentioning
    the specific strip-key name.

    # Feature: multilingual-curriculum-expansion, Property 8: Strip keys exclusion
    **Validates: Requirements 5.10, 11.9**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)

    # Build a nested structure and inject the strip key at the deepest level
    nested = {}
    current = nested
    for i in range(nesting_depth - 1):
        current[f"level{i}"] = {}
        current = current[f"level{i}"]
    current[strip_key] = "deeply_injected"

    # Inject the nested structure into the first activity's data in session 1
    content["learningSessions"][0]["activities"][0]["data"]["nested_test"] = nested

    with pytest.raises(ValueError, match=strip_key):
        validate(content)


# ---------------------------------------------------------------------------
# Property 9: Validator rejects invalid content with specific message
# Feature: multilingual-curriculum-expansion, Property 9: Validator rejects invalid content with specific message
# **Validates: Requirements 5.11, 11.11**
# ---------------------------------------------------------------------------


# --- Mutation strategies: each takes a valid curriculum and breaks it in one way ---

def _mutate_remove_top_level_field(content, rng):
    """Remove a required top-level field."""
    field = rng.choice(["title", "description", "preview", "contentTypeTags", "learningSessions"])
    del content[field]
    return content


def _mutate_empty_top_level_string(content, rng):
    """Set a top-level string field to an empty/invalid value."""
    field = rng.choice(["title", "description"])
    bad = rng.choice([None, "", "   ", 0, False, []])
    content[field] = bad
    return content


def _mutate_bad_preview(content, rng):
    """Corrupt the preview field."""
    choice = rng.choice(["remove_text", "empty_text", "non_dict"])
    if choice == "remove_text":
        content["preview"] = {"other": "no text key"}
    elif choice == "empty_text":
        content["preview"]["text"] = rng.choice([None, "", "   "])
    else:
        content["preview"] = rng.choice([None, "string", 42, []])
    return content


def _mutate_wrong_session_count(content, rng):
    """Change the number of sessions to something other than 5."""
    count = rng.choice([0, 1, 2, 3, 4, 6, 7, 8])
    sessions = content["learningSessions"]
    if count == 0:
        content["learningSessions"] = []
    elif count < 5:
        content["learningSessions"] = sessions[:count]
    else:
        import copy as _cp
        extra = [_cp.deepcopy(sessions[i % 5]) for i in range(count)]
        content["learningSessions"] = extra
    return content


def _mutate_bad_session_title(content, rng):
    """Corrupt a session title."""
    idx = rng.randint(0, 4)
    content["learningSessions"][idx]["title"] = rng.choice([None, "", "   ", 0, False])
    return content


def _mutate_empty_activities(content, rng):
    """Set a session's activities to empty or non-array."""
    idx = rng.randint(0, 4)
    content["learningSessions"][idx]["activities"] = rng.choice([[], None, "bad", 42])
    return content


def _mutate_bad_activity_type(content, rng):
    """Corrupt an activity's activityType."""
    s_idx = rng.randint(0, 4)
    activities = content["learningSessions"][s_idx]["activities"]
    a_idx = rng.randint(0, len(activities) - 1)
    choice = rng.choice(["remove", "use_type", "invalid_value", "empty"])
    if choice == "remove":
        activities[a_idx].pop("activityType", None)
    elif choice == "use_type":
        old = activities[a_idx].pop("activityType")
        activities[a_idx]["type"] = old
    elif choice == "invalid_value":
        activities[a_idx]["activityType"] = "totallyInvalidType"
    else:
        activities[a_idx]["activityType"] = rng.choice([None, "", 0])
    return content


def _mutate_remove_activity_field(content, rng):
    """Remove a required field from an activity."""
    s_idx = rng.randint(0, 4)
    activities = content["learningSessions"][s_idx]["activities"]
    a_idx = rng.randint(0, len(activities) - 1)
    field = rng.choice(["title", "description", "data"])
    activities[a_idx].pop(field, None)
    return content


def _mutate_vocab_uppercase(content, rng):
    """Inject an uppercase word into a vocab activity's vocabList."""
    s_idx = rng.randint(0, 2)
    session = content["learningSessions"][s_idx]
    for act in session["activities"]:
        if act.get("activityType") in _VOCAB_ACTIVITY_TYPES:
            vocab = list(act["data"]["vocabList"])
            idx = rng.randint(0, len(vocab) - 1)
            vocab[idx] = "UpperCase"
            act["data"]["vocabList"] = vocab
    return content


def _mutate_vocab_words_field(content, rng):
    """Rename vocabList to 'words' on a vocab activity."""
    s_idx = rng.randint(0, 2)
    session = content["learningSessions"][s_idx]
    for act in session["activities"]:
        if act.get("activityType") in _VOCAB_ACTIVITY_TYPES:
            vocab = act["data"].pop("vocabList")
            act["data"]["words"] = vocab
            break
    return content


def _mutate_flashcard_mismatch(content, rng):
    """Make viewFlashcards and speakFlashcards vocabLists differ in a session."""
    s_idx = rng.randint(0, 2)
    session = content["learningSessions"][s_idx]
    for act in session["activities"]:
        if act.get("activityType") == "speakFlashcards":
            act["data"]["vocabList"] = list(reversed(act["data"]["vocabList"]))
            break
    return content


def _mutate_inject_strip_key(content, rng):
    """Inject a strip-key at a random location in the JSON tree."""
    key = rng.choice(sorted(STRIP_KEYS))
    location = rng.choice(["top", "session", "activity", "data"])
    if location == "top":
        content[key] = "injected"
    elif location == "session":
        s_idx = rng.randint(0, 4)
        content["learningSessions"][s_idx][key] = "injected"
    elif location == "activity":
        s_idx = rng.randint(0, 4)
        acts = content["learningSessions"][s_idx]["activities"]
        acts[0][key] = "injected"
    else:
        s_idx = rng.randint(0, 4)
        acts = content["learningSessions"][s_idx]["activities"]
        acts[0]["data"][key] = "injected"
    return content


def _mutate_wrong_vocab_count(content, rng):
    """Change vocab count in a learning session to something other than 6."""
    s_idx = rng.randint(0, 2)
    count = rng.choice([1, 2, 3, 4, 5, 7, 8, 9])
    new_vocab = [f"xword{i}" for i in range(count)]
    _set_session_vocab(content, s_idx, new_vocab)
    return content


def _mutate_writing_sentence_missing_field(content, rng):
    """Remove a required field from a writingSentence activity."""
    for s_idx in range(3):
        act_idx = _find_writing_sentence_activity(content, s_idx)
        if act_idx is not None:
            field = rng.choice(["vocabList", "items"])
            data = content["learningSessions"][s_idx]["activities"][act_idx]["data"]
            if field in data:
                del data[field]
            return content
    return content


def _mutate_writing_paragraph_missing_field(content, rng):
    """Remove a required field from a writingParagraph activity."""
    act_idx = _find_writing_paragraph_activity(content, 4)
    if act_idx is not None:
        field = rng.choice(["vocabList", "instructions", "prompts"])
        data = content["learningSessions"][4]["activities"][act_idx]["data"]
        if field in data:
            del data[field]
    return content


# All mutation strategies collected
_ALL_MUTATIONS = [
    _mutate_remove_top_level_field,
    _mutate_empty_top_level_string,
    _mutate_bad_preview,
    _mutate_wrong_session_count,
    _mutate_bad_session_title,
    _mutate_empty_activities,
    _mutate_bad_activity_type,
    _mutate_remove_activity_field,
    _mutate_vocab_uppercase,
    _mutate_vocab_words_field,
    _mutate_flashcard_mismatch,
    _mutate_inject_strip_key,
    _mutate_wrong_vocab_count,
    _mutate_writing_sentence_missing_field,
    _mutate_writing_paragraph_missing_field,
]

import random as _random


@settings(max_examples=100)
@given(
    mutation_idx=st.integers(min_value=0, max_value=len(_ALL_MUTATIONS) - 1),
    seed=st.integers(min_value=0, max_value=2**32 - 1),
)
def test_validator_always_raises_on_invalid_content(mutation_idx, seed):
    """
    Property 9a: For ANY invalid curriculum JSON produced by applying a random
    mutation to valid content, the validator SHALL raise ValueError (never
    silently pass) and the error message SHALL be non-empty.

    This meta-property randomly selects from 15 different mutation strategies
    covering all structural violation categories and verifies the validator
    catches every one.

    # Feature: multilingual-curriculum-expansion, Property 9: Validator rejects invalid content with specific message
    **Validates: Requirements 5.11, 11.11**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)

    rng = _random.Random(seed)
    mutator = _ALL_MUTATIONS[mutation_idx]
    content = mutator(content, rng)

    with pytest.raises(ValueError) as exc_info:
        validate(content)

    # Error message must be non-empty and identify the violation
    msg = str(exc_info.value)
    assert len(msg) > 0, "Validator raised ValueError but with an empty message"


@settings(max_examples=100)
@given(
    mutations=st.lists(
        st.integers(min_value=0, max_value=len(_ALL_MUTATIONS) - 1),
        min_size=2,
        max_size=4,
    ),
    seed=st.integers(min_value=0, max_value=2**32 - 1),
)
def test_validator_raises_on_multiply_mutated_content(mutations, seed):
    """
    Property 9b: For ANY invalid curriculum JSON produced by applying MULTIPLE
    random mutations to valid content, the validator SHALL raise ValueError
    (never silently pass) and the error message SHALL be non-empty.

    This tests that combining multiple mutations never accidentally produces
    content that passes validation.

    # Feature: multilingual-curriculum-expansion, Property 9: Validator rejects invalid content with specific message
    **Validates: Requirements 5.11, 11.11**
    """
    content = make_valid_curriculum()
    content = copy.deepcopy(content)

    rng = _random.Random(seed)
    for idx in mutations:
        try:
            content = _ALL_MUTATIONS[idx](content, rng)
        except (KeyError, IndexError, TypeError):
            # A prior mutation may have removed structure needed by a later one;
            # the content is already invalid, so just continue
            pass

    with pytest.raises(ValueError) as exc_info:
        validate(content)

    msg = str(exc_info.value)
    assert len(msg) > 0, "Validator raised ValueError but with an empty message"


@settings(max_examples=100)
@given(
    bad_content=st.one_of(
        st.just(None),
        st.just("not a dict"),
        st.just(42),
        st.just([]),
        st.just(True),
        st.just(0.5),
        st.dictionaries(
            st.text(min_size=1, max_size=10),
            st.text(min_size=0, max_size=10),
            min_size=0,
            max_size=3,
        ),
    ),
)
def test_validator_raises_on_completely_random_content(bad_content):
    """
    Property 9c: For ANY non-curriculum input (non-dict types, random dicts
    without required fields), the validator SHALL raise ValueError with a
    non-empty message.

    # Feature: multilingual-curriculum-expansion, Property 9: Validator rejects invalid content with specific message
    **Validates: Requirements 5.11, 11.11**
    """
    with pytest.raises(ValueError) as exc_info:
        validate(bad_content)

    msg = str(exc_info.value)
    assert len(msg) > 0, "Validator raised ValueError but with an empty message"
