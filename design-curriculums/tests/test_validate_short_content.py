"""
Property-based tests for validate_short_content.py

# Feature: vi-beginner-short-curriculums, Property 1: Top-level structure validation

**Validates: Requirements 1.5, 13.1**
"""

import copy
import random as _random
import pytest
from hypothesis import given, settings, assume
from hypothesis import strategies as st

from validate_short_content import validate_short, VALID_ACTIVITY_TYPES, STRIP_KEYS, VOCAB_ACTIVITY_TYPES


# ---------------------------------------------------------------------------
# Helper: build a minimal valid short curriculum dict that passes validation
# Uses the balanced_skills template:
#   introAudio → viewFlashcards → speakFlashcards → vocabLevel1 → vocabLevel2
#   → reading → speakReading → readAlong → writingSentence → introAudio(farewell)
# ---------------------------------------------------------------------------

def _make_text_activity(activity_type, title_prefix=""):
    return {
        "activityType": activity_type,
        "title": f"{title_prefix}{activity_type} title",
        "description": f"{activity_type} description",
        "data": {"text": "Some text content here."},
    }


def _make_vocab_activity(activity_type, vocab_list):
    return {
        "activityType": activity_type,
        "title": f"{activity_type} title",
        "description": f"{activity_type} description",
        "data": {"vocabList": list(vocab_list)},
    }


def _make_writing_sentence_activity(vocab_list):
    return {
        "activityType": "writingSentence",
        "title": "Writing Sentence",
        "description": "Write sentences",
        "data": {
            "vocabList": list(vocab_list),
            "items": [
                {"prompt": f"Use '{w}' in a sentence", "targetVocab": w}
                for w in vocab_list
            ],
        },
    }


def make_valid_short_curriculum():
    """Return a fully valid short curriculum dict that passes validate_short().

    Uses the balanced_skills template with 4 vocab words:
    introAudio → viewFlashcards → speakFlashcards → vocabLevel1 → vocabLevel2
    → reading → speakReading → readAlong → writingSentence → introAudio(farewell)
    """
    vocab = ["hello", "goodbye", "please", "thank"]

    activities = [
        _make_text_activity("introAudio", "Welcome: "),
        _make_vocab_activity("viewFlashcards", vocab),
        _make_vocab_activity("speakFlashcards", vocab),
        _make_vocab_activity("vocabLevel1", vocab),
        _make_vocab_activity("vocabLevel2", vocab),
        _make_text_activity("reading"),
        _make_text_activity("speakReading"),
        _make_text_activity("readAlong"),
        _make_writing_sentence_activity(vocab),
        _make_text_activity("introAudio", "Farewell: "),
    ]

    return {
        "title": "Chào hỏi và giới thiệu",
        "description": "A valid short curriculum description with persuasive copy.",
        "contentTypeTags": [],
        "preview": {"text": "This is a valid preview text for the short curriculum."},
        "learningSessions": [
            {
                "title": "Bài học",
                "activities": activities,
            }
        ],
    }


# ---------------------------------------------------------------------------
# Sanity check: the base curriculum is actually valid
# ---------------------------------------------------------------------------

def test_valid_short_curriculum_passes():
    """Ensure our helper builds a curriculum that passes validation."""
    validate_short(make_valid_short_curriculum())  # should not raise


# ---------------------------------------------------------------------------
# Hypothesis strategies
# ---------------------------------------------------------------------------

empty_or_missing_strings = st.one_of(
    st.just(None),
    st.just(""),
    st.just("   "),
    st.just(0),
    st.just(False),
    st.just([]),
    st.just({}),
)

top_level_string_field = st.sampled_from(["title", "description"])


# ---------------------------------------------------------------------------
# Property 1: Top-level structure validation
# Feature: vi-beginner-short-curriculums, Property 1: Top-level structure validation
# **Validates: Requirements 1.5, 13.1**
# ---------------------------------------------------------------------------

@settings(max_examples=100)
@given(field=top_level_string_field, bad_value=empty_or_missing_strings)
def test_rejects_missing_or_empty_top_level_string_fields(field, bad_value):
    """
    Property 1a: Validator rejects curriculum with missing/empty title or description.

    # Feature: vi-beginner-short-curriculums, Property 1: Top-level structure validation
    **Validates: Requirements 1.5, 13.1**
    """
    content = make_valid_short_curriculum()
    content[field] = bad_value

    with pytest.raises(ValueError, match=field):
        validate_short(content)


@settings(max_examples=100)
@given(bad_value=empty_or_missing_strings)
def test_rejects_missing_or_empty_preview_text(bad_value):
    """
    Property 1b: Validator rejects curriculum with missing/empty preview.text.

    # Feature: vi-beginner-short-curriculums, Property 1: Top-level structure validation
    **Validates: Requirements 1.5, 13.1**
    """
    content = make_valid_short_curriculum()
    content["preview"]["text"] = bad_value

    with pytest.raises(ValueError, match="preview"):
        validate_short(content)


@settings(max_examples=100)
@given(
    bad_preview=st.one_of(
        st.just(None),
        st.just("a string"),
        st.just(42),
        st.just([]),
        st.just({}),
        st.just({"other": 1}),
    )
)
def test_rejects_invalid_preview_object(bad_preview):
    """
    Property 1c: Validator rejects curriculum where 'preview' is not a dict with a 'text' field.

    # Feature: vi-beginner-short-curriculums, Property 1: Top-level structure validation
    **Validates: Requirements 1.5, 13.1**
    """
    content = make_valid_short_curriculum()
    content["preview"] = bad_preview

    with pytest.raises(ValueError, match="preview"):
        validate_short(content)


@settings(max_examples=100)
@given(
    field_to_remove=st.sampled_from([
        "title", "description", "preview", "contentTypeTags", "learningSessions",
    ])
)
def test_rejects_curriculum_with_removed_top_level_field(field_to_remove):
    """
    Property 1d: Validator rejects curriculum when any required top-level field
    is completely removed from the dict.

    # Feature: vi-beginner-short-curriculums, Property 1: Top-level structure validation
    **Validates: Requirements 1.5, 13.1**
    """
    content = make_valid_short_curriculum()
    del content[field_to_remove]

    with pytest.raises(ValueError):
        validate_short(content)


def test_rejects_non_dict_content():
    """
    Property 1e: Validator rejects content that is not a dict.

    # Feature: vi-beginner-short-curriculums, Property 1: Top-level structure validation
    **Validates: Requirements 1.5, 13.1**
    """
    for bad in [None, "string", 42, [], True]:
        with pytest.raises(ValueError, match="dict"):
            validate_short(bad)


# ---------------------------------------------------------------------------
# Property 2: Single session invariant
# Feature: vi-beginner-short-curriculums, Property 2: Single session invariant
# **Validates: Requirements 1.1, 13.2**
# ---------------------------------------------------------------------------

wrong_session_count = st.integers(min_value=0, max_value=10).filter(lambda n: n != 1)


@settings(max_examples=100)
@given(count=wrong_session_count)
def test_rejects_wrong_session_count(count):
    """
    Property 2a: Validator rejects curriculum with wrong number of sessions.

    For any curriculum JSON where learningSessions has a count != 1,
    the validator SHALL raise ValueError.

    # Feature: vi-beginner-short-curriculums, Property 2: Single session invariant
    **Validates: Requirements 1.1, 13.2**
    """
    content = make_valid_short_curriculum()
    valid_session = content["learningSessions"][0]

    if count == 0:
        content["learningSessions"] = []
    else:
        content["learningSessions"] = [copy.deepcopy(valid_session) for _ in range(count)]

    with pytest.raises(ValueError):
        validate_short(content)


@settings(max_examples=100)
@given(
    bad_title=st.one_of(
        st.just(None),
        st.just(""),
        st.just("   "),
        st.just(0),
        st.just(False),
        st.just([]),
        st.just({}),
    ),
)
def test_rejects_missing_or_empty_session_title(bad_title):
    """
    Property 2b: Validator rejects curriculum where the session has a
    missing, empty, whitespace-only, or non-string title.

    # Feature: vi-beginner-short-curriculums, Property 2: Single session invariant
    **Validates: Requirements 1.1, 13.2**
    """
    content = make_valid_short_curriculum()
    content["learningSessions"][0]["title"] = bad_title

    with pytest.raises(ValueError, match="Session 1"):
        validate_short(content)


@settings(max_examples=100)
@given(
    bad_activities=st.one_of(
        st.just([]),
        st.just(None),
        st.just("not a list"),
        st.just(42),
        st.just({}),
    ),
)
def test_rejects_empty_or_invalid_activities(bad_activities):
    """
    Property 2c: Validator rejects curriculum where the session has
    empty or non-array activities.

    # Feature: vi-beginner-short-curriculums, Property 2: Single session invariant
    **Validates: Requirements 1.1, 13.2**
    """
    content = make_valid_short_curriculum()
    content["learningSessions"][0]["activities"] = bad_activities

    with pytest.raises(ValueError, match="Session 1|activities"):
        validate_short(content)


# ---------------------------------------------------------------------------
# Property 3: Vocabulary count invariant
# Feature: vi-beginner-short-curriculums, Property 3: Vocabulary count invariant
# **Validates: Requirements 1.2, 13.9**
# ---------------------------------------------------------------------------


def _set_all_vocab_in_session(content, new_vocab):
    """Replace all vocabList arrays in the single session with new_vocab."""
    session = content["learningSessions"][0]
    for activity in session["activities"]:
        at = activity.get("activityType")
        if at in VOCAB_ACTIVITY_TYPES:
            activity["data"]["vocabList"] = list(new_vocab)
        elif at == "writingSentence":
            activity["data"]["vocabList"] = list(new_vocab)
            activity["data"]["items"] = [
                {"prompt": f"Use '{w}' in a sentence", "targetVocab": w}
                for w in new_vocab
            ]


# Vocab counts outside the valid 3-5 range
wrong_vocab_count = st.one_of(
    st.integers(min_value=1, max_value=2),
    st.integers(min_value=6, max_value=12),
)


@settings(max_examples=100)
@given(word_count=wrong_vocab_count)
def test_rejects_wrong_vocab_count(word_count):
    """
    Property 3a: Validator rejects curriculum where the total unique vocabulary
    words is outside the 3-5 range.

    # Feature: vi-beginner-short-curriculums, Property 3: Vocabulary count invariant
    **Validates: Requirements 1.2, 13.9**
    """
    content = make_valid_short_curriculum()
    content = copy.deepcopy(content)

    new_vocab = [f"word{i}" for i in range(word_count)]
    _set_all_vocab_in_session(content, new_vocab)

    with pytest.raises(ValueError, match="vocabulary words"):
        validate_short(content)


@settings(max_examples=100)
@given(valid_count=st.integers(min_value=3, max_value=5))
def test_accepts_valid_vocab_counts(valid_count):
    """
    Property 3b: Validator accepts curriculum with 3, 4, or 5 unique vocabulary words.

    # Feature: vi-beginner-short-curriculums, Property 3: Vocabulary count invariant
    **Validates: Requirements 1.2, 13.9**
    """
    content = make_valid_short_curriculum()
    content = copy.deepcopy(content)

    new_vocab = [f"word{i}" for i in range(valid_count)]
    _set_all_vocab_in_session(content, new_vocab)

    validate_short(content)  # should not raise


# ---------------------------------------------------------------------------
# Property 4: Activity structure completeness
# Feature: vi-beginner-short-curriculums, Property 4: Activity structure completeness
# **Validates: Requirements 12.1, 12.2, 12.5, 13.3, 13.4**
# ---------------------------------------------------------------------------

# Strategy: generate strings that are NOT valid activity types
invalid_activity_type_st = st.text(min_size=1, max_size=30).filter(
    lambda s: s not in VALID_ACTIVITY_TYPES
)

required_activity_fields = st.sampled_from(["title", "description", "data"])

# Pick an activity index within the balanced_skills template (10 activities, 0-9)
activity_idx_st = st.integers(min_value=0, max_value=9)


@settings(max_examples=100)
@given(activity_idx=activity_idx_st)
def test_rejects_activity_missing_activity_type(activity_idx):
    """
    Property 4a: Validator rejects activity with missing activityType field.

    # Feature: vi-beginner-short-curriculums, Property 4: Activity structure completeness
    **Validates: Requirements 12.1, 12.2, 12.5, 13.3, 13.4**
    """
    content = make_valid_short_curriculum()
    content = copy.deepcopy(content)

    activity = content["learningSessions"][0]["activities"][activity_idx]
    del activity["activityType"]

    with pytest.raises(ValueError, match="activityType"):
        validate_short(content)


@settings(max_examples=100)
@given(activity_idx=activity_idx_st)
def test_rejects_activity_using_type_instead_of_activity_type(activity_idx):
    """
    Property 4b: Validator rejects activity using 'type' instead of 'activityType'.

    # Feature: vi-beginner-short-curriculums, Property 4: Activity structure completeness
    **Validates: Requirements 12.1, 12.2, 12.5, 13.3, 13.4**
    """
    content = make_valid_short_curriculum()
    content = copy.deepcopy(content)

    activity = content["learningSessions"][0]["activities"][activity_idx]
    old_type = activity.pop("activityType")
    activity["type"] = old_type

    with pytest.raises(ValueError, match="type"):
        validate_short(content)


@settings(max_examples=100)
@given(
    activity_idx=activity_idx_st,
    bad_type=invalid_activity_type_st,
)
def test_rejects_activity_with_invalid_activity_type(activity_idx, bad_type):
    """
    Property 4c: Validator rejects activity with an activityType value not in
    the valid set.

    # Feature: vi-beginner-short-curriculums, Property 4: Activity structure completeness
    **Validates: Requirements 12.1, 12.2, 12.5, 13.3, 13.4**
    """
    content = make_valid_short_curriculum()
    content = copy.deepcopy(content)

    activity = content["learningSessions"][0]["activities"][activity_idx]
    activity["activityType"] = bad_type

    with pytest.raises(ValueError, match="activityType"):
        validate_short(content)


@settings(max_examples=100)
@given(
    activity_idx=activity_idx_st,
    field=required_activity_fields,
)
def test_rejects_activity_missing_required_field(activity_idx, field):
    """
    Property 4d: Validator rejects activity missing 'title', 'description', or 'data'.

    # Feature: vi-beginner-short-curriculums, Property 4: Activity structure completeness
    **Validates: Requirements 12.1, 12.2, 12.5, 13.3, 13.4**
    """
    content = make_valid_short_curriculum()
    content = copy.deepcopy(content)

    activity = content["learningSessions"][0]["activities"][activity_idx]
    del activity[field]

    with pytest.raises(ValueError, match=field):
        validate_short(content)


@settings(max_examples=100)
@given(
    activity_idx=activity_idx_st,
    bad_value=st.one_of(
        st.just(None),
        st.just(""),
        st.just(0),
        st.just(False),
        st.just([]),
    ),
)
def test_rejects_activity_with_inline_content_fields(activity_idx, bad_value):
    """
    Property 4e: Validator rejects activity where activityType is empty,
    null, or a non-string type (inline content corruption).

    # Feature: vi-beginner-short-curriculums, Property 4: Activity structure completeness
    **Validates: Requirements 12.1, 12.2, 12.5, 13.3, 13.4**
    """
    content = make_valid_short_curriculum()
    content = copy.deepcopy(content)

    activity = content["learningSessions"][0]["activities"][activity_idx]
    activity["activityType"] = bad_value

    with pytest.raises(ValueError, match="activityType"):
        validate_short(content)


# ---------------------------------------------------------------------------
# Property 5: VocabList format enforcement
# Feature: vi-beginner-short-curriculums, Property 5: VocabList format enforcement
# **Validates: Requirements 12.3, 13.5**
# ---------------------------------------------------------------------------

_VOCAB_ACTIVITY_TYPES_LIST = sorted(VOCAB_ACTIVITY_TYPES)

vocab_activity_type_st = st.sampled_from(_VOCAB_ACTIVITY_TYPES_LIST)

uppercase_word_st = st.from_regex(r"[a-z]*[A-Z][a-zA-Z]*", fullmatch=True).filter(
    lambda s: s != s.lower()
)

non_string_element_st = st.one_of(
    st.integers(),
    st.booleans(),
    st.lists(st.text(min_size=0, max_size=5), min_size=0, max_size=3),
    st.dictionaries(
        st.text(min_size=1, max_size=5),
        st.text(min_size=0, max_size=5),
        min_size=0,
        max_size=3,
    ),
)


def _set_all_vocab_activities_data(content, mutator):
    """Apply a mutator function to the data dict of every vocab activity in the session."""
    session = content["learningSessions"][0]
    for activity in session["activities"]:
        at = activity.get("activityType")
        if at in VOCAB_ACTIVITY_TYPES:
            mutator(activity["data"], at)


@settings(max_examples=100)
@given(
    uppercase_word=uppercase_word_st,
    position=st.integers(min_value=0, max_value=3),
)
def test_rejects_uppercase_strings_in_vocab_list(uppercase_word, position):
    """
    Property 5a: Validator rejects vocab activities with uppercase strings in vocabList.

    # Feature: vi-beginner-short-curriculums, Property 5: VocabList format enforcement
    **Validates: Requirements 12.3, 13.5**
    """
    content = make_valid_short_curriculum()
    content = copy.deepcopy(content)

    def inject_uppercase(data, _at):
        vocab = list(data["vocabList"])
        idx = position % len(vocab)
        vocab[idx] = uppercase_word
        data["vocabList"] = vocab

    _set_all_vocab_activities_data(content, inject_uppercase)

    with pytest.raises(ValueError, match="lowercase"):
        validate_short(content)


@settings(max_examples=100)
@given(
    bad_element=non_string_element_st,
    position=st.integers(min_value=0, max_value=3),
)
def test_rejects_non_string_elements_in_vocab_list(bad_element, position):
    """
    Property 5b: Validator rejects vocab activities with non-string elements in vocabList.

    # Feature: vi-beginner-short-curriculums, Property 5: VocabList format enforcement
    **Validates: Requirements 12.3, 13.5**
    """
    content = make_valid_short_curriculum()
    content = copy.deepcopy(content)

    def inject_non_string(data, _at):
        vocab = list(data["vocabList"])
        idx = position % len(vocab)
        vocab[idx] = bad_element
        data["vocabList"] = vocab

    _set_all_vocab_activities_data(content, inject_non_string)

    with pytest.raises(ValueError, match="string"):
        validate_short(content)


@settings(max_examples=100)
@given(data=st.data())
def test_rejects_words_field_name_instead_of_vocab_list(data):
    """
    Property 5c: Validator rejects vocab activities using 'words' field name
    instead of 'vocabList'.

    # Feature: vi-beginner-short-curriculums, Property 5: VocabList format enforcement
    **Validates: Requirements 12.3, 13.5**
    """
    content = make_valid_short_curriculum()
    content = copy.deepcopy(content)

    def rename_to_words(data_dict, _at):
        vocab = data_dict.pop("vocabList")
        data_dict["words"] = vocab

    _set_all_vocab_activities_data(content, rename_to_words)

    with pytest.raises(ValueError, match="words"):
        validate_short(content)


# ---------------------------------------------------------------------------
# Property 6: Flashcard vocabList consistency
# Feature: vi-beginner-short-curriculums, Property 6: Flashcard vocabList consistency
# **Validates: Requirements 12.4, 13.6**
# ---------------------------------------------------------------------------


def _get_view_flashcards_vocab(content):
    """Return the vocabList from the viewFlashcards activity."""
    session = content["learningSessions"][0]
    for activity in session["activities"]:
        if activity.get("activityType") == "viewFlashcards":
            return list(activity["data"]["vocabList"])
    return None


def _set_speak_flashcards_vocab(content, new_vocab):
    """Replace only the speakFlashcards vocabList."""
    session = content["learningSessions"][0]
    for activity in session["activities"]:
        if activity.get("activityType") == "speakFlashcards":
            activity["data"]["vocabList"] = new_vocab


@settings(max_examples=100)
@given(data=st.data())
def test_rejects_shuffled_speak_flashcards_vocab(data):
    """
    Property 6a: Validator rejects session where speakFlashcards vocabList
    has the same elements as viewFlashcards but in a different order.

    # Feature: vi-beginner-short-curriculums, Property 6: Flashcard vocabList consistency
    **Validates: Requirements 12.4, 13.6**
    """
    content = make_valid_short_curriculum()
    content = copy.deepcopy(content)

    view_vocab = _get_view_flashcards_vocab(content)
    assume(view_vocab is not None and len(view_vocab) >= 2)

    shuffled = list(reversed(view_vocab))
    assume(shuffled != view_vocab)

    _set_speak_flashcards_vocab(content, shuffled)

    with pytest.raises(ValueError, match="mismatched"):
        validate_short(content)


@settings(max_examples=100)
@given(extra_word=st.from_regex(r"[a-z]{3,10}", fullmatch=True))
def test_rejects_speak_flashcards_with_extra_element(extra_word):
    """
    Property 6b: Validator rejects session where speakFlashcards vocabList
    has more elements than viewFlashcards.

    # Feature: vi-beginner-short-curriculums, Property 6: Flashcard vocabList consistency
    **Validates: Requirements 12.4, 13.6**
    """
    content = make_valid_short_curriculum()
    content = copy.deepcopy(content)

    view_vocab = _get_view_flashcards_vocab(content)
    assume(view_vocab is not None)
    assume(extra_word not in view_vocab)

    longer_vocab = list(view_vocab) + [extra_word]
    _set_speak_flashcards_vocab(content, longer_vocab)

    with pytest.raises(ValueError, match="mismatched"):
        validate_short(content)


@settings(max_examples=100)
@given(
    replacement_word=st.from_regex(r"[a-z]{3,10}", fullmatch=True),
    position=st.integers(min_value=0, max_value=3),
)
def test_rejects_speak_flashcards_with_different_element(replacement_word, position):
    """
    Property 6c: Validator rejects session where speakFlashcards vocabList
    has one element replaced with a different word.

    # Feature: vi-beginner-short-curriculums, Property 6: Flashcard vocabList consistency
    **Validates: Requirements 12.4, 13.6**
    """
    content = make_valid_short_curriculum()
    content = copy.deepcopy(content)

    view_vocab = _get_view_flashcards_vocab(content)
    assume(view_vocab is not None and len(view_vocab) > 0)

    idx = position % len(view_vocab)
    assume(replacement_word != view_vocab[idx])

    modified_vocab = list(view_vocab)
    modified_vocab[idx] = replacement_word
    assume(modified_vocab != view_vocab)

    _set_speak_flashcards_vocab(content, modified_vocab)

    with pytest.raises(ValueError, match="mismatched"):
        validate_short(content)


# ---------------------------------------------------------------------------
# Property 7: Writing activity structure
# Feature: vi-beginner-short-curriculums, Property 7: Writing activity structure
# **Validates: Requirements 12.6, 12.7, 13.7**
# ---------------------------------------------------------------------------


def _find_writing_sentence_activity(content):
    """Return the index of the writingSentence activity, or None."""
    session = content["learningSessions"][0]
    for i, activity in enumerate(session["activities"]):
        if activity.get("activityType") == "writingSentence":
            return i
    return None


def _add_writing_paragraph_activity(content):
    """Add a writingParagraph activity to the session and return the content."""
    vocab = ["hello", "goodbye", "please", "thank"]
    wp_activity = {
        "activityType": "writingParagraph",
        "title": "Writing Paragraph",
        "description": "Write a paragraph",
        "data": {
            "vocabList": list(vocab),
            "instructions": "Write a paragraph about greetings",
            "prompts": ["First prompt", "Second prompt"],
        },
    }
    # Insert before the farewell introAudio (last activity)
    activities = content["learningSessions"][0]["activities"]
    activities.insert(len(activities) - 1, wp_activity)
    return content


def _find_writing_paragraph_activity(content):
    """Return the index of the writingParagraph activity, or None."""
    session = content["learningSessions"][0]
    for i, activity in enumerate(session["activities"]):
        if activity.get("activityType") == "writingParagraph":
            return i
    return None


# --- writingSentence tests ---

@settings(max_examples=100)
@given(data=st.data())
def test_rejects_writing_sentence_missing_vocab_list(data):
    """
    Property 7a: Validator rejects writingSentence activity with missing data.vocabList.

    # Feature: vi-beginner-short-curriculums, Property 7: Writing activity structure
    **Validates: Requirements 12.6, 12.7, 13.7**
    """
    content = make_valid_short_curriculum()
    content = copy.deepcopy(content)

    act_idx = _find_writing_sentence_activity(content)
    assume(act_idx is not None)

    del content["learningSessions"][0]["activities"][act_idx]["data"]["vocabList"]

    with pytest.raises(ValueError, match="vocabList"):
        validate_short(content)


@settings(max_examples=100)
@given(data=st.data())
def test_rejects_writing_sentence_missing_items(data):
    """
    Property 7b: Validator rejects writingSentence activity with missing data.items.

    # Feature: vi-beginner-short-curriculums, Property 7: Writing activity structure
    **Validates: Requirements 12.6, 12.7, 13.7**
    """
    content = make_valid_short_curriculum()
    content = copy.deepcopy(content)

    act_idx = _find_writing_sentence_activity(content)
    assume(act_idx is not None)

    del content["learningSessions"][0]["activities"][act_idx]["data"]["items"]

    with pytest.raises(ValueError, match="items"):
        validate_short(content)


@settings(max_examples=100)
@given(
    field_to_corrupt=st.sampled_from(["prompt", "targetVocab"]),
    bad_value=st.one_of(st.just(None), st.just(""), st.just("   ")),
)
def test_rejects_writing_sentence_item_empty_required_field(field_to_corrupt, bad_value):
    """
    Property 7c: Validator rejects writingSentence item with empty/null prompt or targetVocab.

    # Feature: vi-beginner-short-curriculums, Property 7: Writing activity structure
    **Validates: Requirements 12.6, 12.7, 13.7**
    """
    content = make_valid_short_curriculum()
    content = copy.deepcopy(content)

    act_idx = _find_writing_sentence_activity(content)
    assume(act_idx is not None)

    items = content["learningSessions"][0]["activities"][act_idx]["data"]["items"]
    assume(len(items) > 0)
    items[0][field_to_corrupt] = bad_value

    with pytest.raises(ValueError, match=field_to_corrupt):
        validate_short(content)


# --- writingParagraph tests ---

@settings(max_examples=100)
@given(data=st.data())
def test_rejects_writing_paragraph_missing_vocab_list(data):
    """
    Property 7d: Validator rejects writingParagraph activity with missing data.vocabList.

    # Feature: vi-beginner-short-curriculums, Property 7: Writing activity structure
    **Validates: Requirements 12.6, 12.7, 13.7**
    """
    content = make_valid_short_curriculum()
    content = copy.deepcopy(content)
    content = _add_writing_paragraph_activity(content)

    act_idx = _find_writing_paragraph_activity(content)
    assume(act_idx is not None)

    del content["learningSessions"][0]["activities"][act_idx]["data"]["vocabList"]

    with pytest.raises(ValueError, match="vocabList"):
        validate_short(content)


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
    Property 7e: Validator rejects writingParagraph activity where data.instructions
    is empty, null, whitespace-only, or a non-string type.

    # Feature: vi-beginner-short-curriculums, Property 7: Writing activity structure
    **Validates: Requirements 12.6, 12.7, 13.7**
    """
    content = make_valid_short_curriculum()
    content = copy.deepcopy(content)
    content = _add_writing_paragraph_activity(content)

    act_idx = _find_writing_paragraph_activity(content)
    assume(act_idx is not None)

    content["learningSessions"][0]["activities"][act_idx]["data"]["instructions"] = bad_value

    with pytest.raises(ValueError, match="instructions"):
        validate_short(content)


@settings(max_examples=100)
@given(prompt_count=st.integers(min_value=0, max_value=1))
def test_rejects_writing_paragraph_fewer_than_two_prompts(prompt_count):
    """
    Property 7f: Validator rejects writingParagraph activity where data.prompts
    has fewer than 2 items.

    # Feature: vi-beginner-short-curriculums, Property 7: Writing activity structure
    **Validates: Requirements 12.6, 12.7, 13.7**
    """
    content = make_valid_short_curriculum()
    content = copy.deepcopy(content)
    content = _add_writing_paragraph_activity(content)

    act_idx = _find_writing_paragraph_activity(content)
    assume(act_idx is not None)

    prompts = ["A single prompt"] if prompt_count == 1 else []
    content["learningSessions"][0]["activities"][act_idx]["data"]["prompts"] = prompts

    with pytest.raises(ValueError, match="prompts"):
        validate_short(content)


# ---------------------------------------------------------------------------
# Property 8: Strip keys exclusion
# Feature: vi-beginner-short-curriculums, Property 8: Strip keys exclusion
# **Validates: Requirements 1.6, 13.8**
# ---------------------------------------------------------------------------

strip_key_st = st.sampled_from(sorted(STRIP_KEYS))


@settings(max_examples=100)
@given(strip_key=strip_key_st)
def test_rejects_strip_key_at_top_level(strip_key):
    """
    Property 8a: Validator rejects curriculum with a strip-key at the top level.

    # Feature: vi-beginner-short-curriculums, Property 8: Strip keys exclusion
    **Validates: Requirements 1.6, 13.8**
    """
    content = make_valid_short_curriculum()
    content = copy.deepcopy(content)
    content[strip_key] = "should_not_be_here"

    with pytest.raises(ValueError, match=strip_key):
        validate_short(content)


@settings(max_examples=100)
@given(strip_key=strip_key_st)
def test_rejects_strip_key_inside_session(strip_key):
    """
    Property 8b: Validator rejects curriculum with a strip-key inside the session object.

    # Feature: vi-beginner-short-curriculums, Property 8: Strip keys exclusion
    **Validates: Requirements 1.6, 13.8**
    """
    content = make_valid_short_curriculum()
    content = copy.deepcopy(content)
    content["learningSessions"][0][strip_key] = "injected"

    with pytest.raises(ValueError, match=strip_key):
        validate_short(content)


@settings(max_examples=100)
@given(strip_key=strip_key_st)
def test_rejects_strip_key_inside_activity(strip_key):
    """
    Property 8c: Validator rejects curriculum with a strip-key inside an activity object.

    # Feature: vi-beginner-short-curriculums, Property 8: Strip keys exclusion
    **Validates: Requirements 1.6, 13.8**
    """
    content = make_valid_short_curriculum()
    content = copy.deepcopy(content)
    content["learningSessions"][0]["activities"][0][strip_key] = "injected"

    with pytest.raises(ValueError, match=strip_key):
        validate_short(content)


@settings(max_examples=100)
@given(strip_key=strip_key_st)
def test_rejects_strip_key_inside_activity_data(strip_key):
    """
    Property 8d: Validator rejects curriculum with a strip-key inside an activity's data.

    # Feature: vi-beginner-short-curriculums, Property 8: Strip keys exclusion
    **Validates: Requirements 1.6, 13.8**
    """
    content = make_valid_short_curriculum()
    content = copy.deepcopy(content)
    content["learningSessions"][0]["activities"][0]["data"][strip_key] = "injected"

    with pytest.raises(ValueError, match=strip_key):
        validate_short(content)


@settings(max_examples=100)
@given(
    strip_key=strip_key_st,
    nesting_depth=st.integers(min_value=1, max_value=5),
)
def test_rejects_strip_key_at_deep_nesting(strip_key, nesting_depth):
    """
    Property 8e: Validator rejects curriculum with a strip-key buried at
    arbitrary nesting depth inside the JSON tree.

    # Feature: vi-beginner-short-curriculums, Property 8: Strip keys exclusion
    **Validates: Requirements 1.6, 13.8**
    """
    content = make_valid_short_curriculum()
    content = copy.deepcopy(content)

    nested = {}
    current = nested
    for i in range(nesting_depth - 1):
        current[f"level{i}"] = {}
        current = current[f"level{i}"]
    current[strip_key] = "deeply_injected"

    content["learningSessions"][0]["activities"][0]["data"]["nested_test"] = nested

    with pytest.raises(ValueError, match=strip_key):
        validate_short(content)


# ---------------------------------------------------------------------------
# Property 9: No vocabLevel3 activities
# Feature: vi-beginner-short-curriculums, Property 9: No vocabLevel3 activities
# **Validates: Requirements 11.5**
# ---------------------------------------------------------------------------

# Strategy: pick a position in the activities list to inject vocabLevel3
inject_position_st = st.integers(min_value=0, max_value=9)


@settings(max_examples=100)
@given(inject_position=inject_position_st)
def test_rejects_vocab_level3_activity(inject_position):
    """
    Property 9a: Validator rejects curriculum containing a vocabLevel3 activity.

    For any curriculum JSON where a vocabLevel3 activity is present at any
    position, the validator SHALL raise ValueError mentioning 'vocabLevel3'.

    # Feature: vi-beginner-short-curriculums, Property 9: No vocabLevel3 activities
    **Validates: Requirements 11.5**
    """
    content = make_valid_short_curriculum()
    content = copy.deepcopy(content)

    vocab = ["hello", "goodbye", "please", "thank"]
    vl3_activity = {
        "activityType": "vocabLevel3",
        "title": "Vocab Level 3",
        "description": "Advanced vocab drill",
        "data": {"vocabList": list(vocab)},
    }

    activities = content["learningSessions"][0]["activities"]
    activities.insert(inject_position, vl3_activity)

    with pytest.raises(ValueError, match="vocabLevel3"):
        validate_short(content)


@settings(max_examples=100)
@given(
    replace_idx=st.sampled_from([3, 4]),  # vocabLevel1 (idx 3) or vocabLevel2 (idx 4)
)
def test_rejects_vocab_level3_replacing_valid_vocab_activity(replace_idx):
    """
    Property 9b: Validator rejects curriculum where a vocabLevel1 or vocabLevel2
    activity is replaced with vocabLevel3.

    # Feature: vi-beginner-short-curriculums, Property 9: No vocabLevel3 activities
    **Validates: Requirements 11.5**
    """
    content = make_valid_short_curriculum()
    content = copy.deepcopy(content)

    content["learningSessions"][0]["activities"][replace_idx]["activityType"] = "vocabLevel3"

    with pytest.raises(ValueError, match="vocabLevel3"):
        validate_short(content)


# ---------------------------------------------------------------------------
# Property 10: Validator rejects invalid content with specific message
# Feature: vi-beginner-short-curriculums, Property 10: Validator rejects invalid content with specific message
# **Validates: Requirements 13.10**
# ---------------------------------------------------------------------------


def _mutate_remove_top_level_field(content, rng):
    field = rng.choice(["title", "description", "preview", "contentTypeTags", "learningSessions"])
    del content[field]
    return content


def _mutate_empty_top_level_string(content, rng):
    field = rng.choice(["title", "description"])
    content[field] = rng.choice([None, "", "   ", 0, False, []])
    return content


def _mutate_bad_preview(content, rng):
    choice = rng.choice(["remove_text", "empty_text", "non_dict"])
    if choice == "remove_text":
        content["preview"] = {"other": "no text key"}
    elif choice == "empty_text":
        content["preview"]["text"] = rng.choice([None, "", "   "])
    else:
        content["preview"] = rng.choice([None, "string", 42, []])
    return content


def _mutate_wrong_session_count(content, rng):
    count = rng.choice([0, 2, 3, 5])
    valid_session = content["learningSessions"][0]
    if count == 0:
        content["learningSessions"] = []
    else:
        content["learningSessions"] = [copy.deepcopy(valid_session) for _ in range(count)]
    return content


def _mutate_bad_session_title(content, rng):
    content["learningSessions"][0]["title"] = rng.choice([None, "", "   ", 0, False])
    return content


def _mutate_empty_activities(content, rng):
    content["learningSessions"][0]["activities"] = rng.choice([[], None, "bad", 42])
    return content


def _mutate_bad_activity_type(content, rng):
    activities = content["learningSessions"][0]["activities"]
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
    activities = content["learningSessions"][0]["activities"]
    a_idx = rng.randint(0, len(activities) - 1)
    field = rng.choice(["title", "description", "data"])
    activities[a_idx].pop(field, None)
    return content


def _mutate_vocab_uppercase(content, rng):
    session = content["learningSessions"][0]
    for act in session["activities"]:
        if act.get("activityType") in VOCAB_ACTIVITY_TYPES:
            vocab = list(act["data"]["vocabList"])
            idx = rng.randint(0, len(vocab) - 1)
            vocab[idx] = "UpperCase"
            act["data"]["vocabList"] = vocab
    return content


def _mutate_vocab_words_field(content, rng):
    session = content["learningSessions"][0]
    for act in session["activities"]:
        if act.get("activityType") in VOCAB_ACTIVITY_TYPES:
            vocab = act["data"].pop("vocabList")
            act["data"]["words"] = vocab
            break
    return content


def _mutate_flashcard_mismatch(content, rng):
    session = content["learningSessions"][0]
    for act in session["activities"]:
        if act.get("activityType") == "speakFlashcards":
            act["data"]["vocabList"] = list(reversed(act["data"]["vocabList"]))
            break
    return content


def _mutate_inject_strip_key(content, rng):
    key = rng.choice(sorted(STRIP_KEYS))
    location = rng.choice(["top", "session", "activity", "data"])
    if location == "top":
        content[key] = "injected"
    elif location == "session":
        content["learningSessions"][0][key] = "injected"
    elif location == "activity":
        content["learningSessions"][0]["activities"][0][key] = "injected"
    else:
        content["learningSessions"][0]["activities"][0]["data"][key] = "injected"
    return content


def _mutate_wrong_vocab_count(content, rng):
    count = rng.choice([1, 2, 6, 7, 8, 9])
    new_vocab = [f"xword{i}" for i in range(count)]
    _set_all_vocab_in_session(content, new_vocab)
    return content


def _mutate_inject_vocab_level3(content, rng):
    vocab = ["hello", "goodbye", "please", "thank"]
    vl3 = {
        "activityType": "vocabLevel3",
        "title": "VL3",
        "description": "VL3 desc",
        "data": {"vocabList": list(vocab)},
    }
    content["learningSessions"][0]["activities"].insert(2, vl3)
    return content


def _mutate_writing_sentence_missing_field(content, rng):
    act_idx = _find_writing_sentence_activity(content)
    if act_idx is not None:
        field = rng.choice(["vocabList", "items"])
        data = content["learningSessions"][0]["activities"][act_idx]["data"]
        if field in data:
            del data[field]
    return content


_ALL_SHORT_MUTATIONS = [
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
    _mutate_inject_vocab_level3,
    _mutate_writing_sentence_missing_field,
]


@settings(max_examples=100)
@given(
    mutation_idx=st.integers(min_value=0, max_value=len(_ALL_SHORT_MUTATIONS) - 1),
    seed=st.integers(min_value=0, max_value=2**32 - 1),
)
def test_validator_always_raises_on_invalid_content(mutation_idx, seed):
    """
    Property 10a: For ANY invalid curriculum JSON produced by applying a random
    mutation to valid content, the validator SHALL raise ValueError (never
    silently pass) and the error message SHALL be non-empty.

    # Feature: vi-beginner-short-curriculums, Property 10: Validator rejects invalid content with specific message
    **Validates: Requirements 13.10**
    """
    content = make_valid_short_curriculum()
    content = copy.deepcopy(content)

    rng = _random.Random(seed)
    mutator = _ALL_SHORT_MUTATIONS[mutation_idx]
    content = mutator(content, rng)

    with pytest.raises(ValueError) as exc_info:
        validate_short(content)

    msg = str(exc_info.value)
    assert len(msg) > 0, "Validator raised ValueError but with an empty message"


@settings(max_examples=100)
@given(
    mutations=st.lists(
        st.integers(min_value=0, max_value=len(_ALL_SHORT_MUTATIONS) - 1),
        min_size=2,
        max_size=4,
        unique=True,
    ),
    seed=st.integers(min_value=0, max_value=2**32 - 1),
)
def test_validator_raises_on_multiply_mutated_content(mutations, seed):
    """
    Property 10b: For ANY invalid curriculum JSON produced by applying MULTIPLE
    distinct random mutations to valid content, the validator SHALL raise
    ValueError (never silently pass) and the error message SHALL be non-empty.

    # Feature: vi-beginner-short-curriculums, Property 10: Validator rejects invalid content with specific message
    **Validates: Requirements 13.10**
    """
    content = make_valid_short_curriculum()
    content = copy.deepcopy(content)

    rng = _random.Random(seed)
    for idx in mutations:
        try:
            content = _ALL_SHORT_MUTATIONS[idx](content, rng)
        except (KeyError, IndexError, TypeError, AttributeError, ValueError):
            # A prior mutation may have removed structure needed by a later one;
            # the content is already invalid, so just continue
            pass

    with pytest.raises(ValueError) as exc_info:
        validate_short(content)

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
    Property 10c: For ANY non-curriculum input (non-dict types, random dicts
    without required fields), the validator SHALL raise ValueError with a
    non-empty message.

    # Feature: vi-beginner-short-curriculums, Property 10: Validator rejects invalid content with specific message
    **Validates: Requirements 13.10**
    """
    with pytest.raises(ValueError) as exc_info:
        validate_short(bad_content)

    msg = str(exc_info.value)
    assert len(msg) > 0, "Validator raised ValueError but with an empty message"
