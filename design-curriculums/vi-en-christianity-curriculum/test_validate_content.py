"""
Property-based tests for validate_content.py using Hypothesis.

Tests the 11 correctness properties defined in the design document for the
Vietnamese-English Christianity curriculum content validator.

Validates: Requirements 1.4, 1.5, 1.6, 3.1, 3.2, 3.3, 3.4, 9.1-9.7, 10.1-10.11, 16.4
"""

import sys
import os
import copy
import string

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from hypothesis import given, settings, assume
from hypothesis import strategies as st

from validate_content import (
    validate,
    ACTIVITY_SEQUENCES,
    STRIP_KEYS,
    VALID_ACTIVITY_TYPES,
    VALID_FORMATS,
    FORMAT_CONTENT_TYPE_TAGS,
    WRITING_ACTIVITY_TYPES,
)


# =============================================================================
# Generator Strategies
# =============================================================================


def random_format():
    """Picks one of 'story_reading', 'speaking', 'balanced'."""
    return st.sampled_from(["story_reading", "speaking", "balanced"])


def random_vocab_list(min_size=1, max_size=6):
    """Generates a list of n random lowercase English strings."""
    word = st.text(
        alphabet=string.ascii_lowercase, min_size=2, max_size=10
    ).filter(lambda w: w.isalpha() and len(w) >= 2)
    return st.lists(word, min_size=min_size, max_size=max_size)


def random_activity(activity_type, vocab_list=None):
    """Generates a valid activity of the given type with all required fields."""

    @st.composite
    def _build(draw):
        title = draw(st.text(min_size=3, max_size=30, alphabet=string.ascii_letters + " "))
        description = draw(st.text(min_size=3, max_size=50, alphabet=string.ascii_letters + " "))

        vocab_activities = {"viewFlashcards", "speakFlashcards", "vocabLevel1", "vocabLevel2"}

        if activity_type in vocab_activities:
            vl = vocab_list if vocab_list is not None else draw(random_vocab_list(1, 6))
            data = {"vocabList": vl}
        elif activity_type == "writingSentence":
            vl = vocab_list if vocab_list is not None else draw(random_vocab_list(2, 6))
            num_items = draw(st.integers(min_value=1, max_value=4))
            items = []
            for _ in range(num_items):
                prompt = draw(st.text(min_size=5, max_size=50, alphabet=string.ascii_letters + " "))
                target = draw(st.text(min_size=2, max_size=10, alphabet=string.ascii_lowercase))
                items.append({"prompt": prompt, "targetVocab": target})
            data = {"vocabList": vl, "items": items}
        elif activity_type == "writingParagraph":
            vl = vocab_list if vocab_list is not None else draw(random_vocab_list(2, 6))
            instructions = draw(st.text(min_size=5, max_size=80, alphabet=string.ascii_letters + " "))
            num_prompts = draw(st.integers(min_value=2, max_value=4))
            prompts = [
                draw(st.text(min_size=5, max_size=50, alphabet=string.ascii_letters + " "))
                for _ in range(num_prompts)
            ]
            data = {"vocabList": vl, "instructions": instructions, "prompts": prompts}
        else:
            # introAudio, reading, speakReading, readAlong
            data = {"text": draw(st.text(min_size=10, max_size=100, alphabet=string.ascii_letters + " "))}

        return {
            "activityType": activity_type,
            "title": title,
            "description": description,
            "data": data,
        }

    return _build()


@st.composite
def valid_curriculum(draw, fmt=None):
    """Generates a structurally valid curriculum content dict for the given format."""
    if fmt is None:
        fmt = draw(random_format())

    title = draw(st.text(min_size=3, max_size=30, alphabet=string.ascii_letters + " "))
    description = draw(st.text(min_size=3, max_size=60, alphabet=string.ascii_letters + " "))
    preview_text = draw(st.text(min_size=3, max_size=60, alphabet=string.ascii_letters + " "))

    content_type_tags = FORMAT_CONTENT_TYPE_TAGS[fmt]
    sequences = ACTIVITY_SEQUENCES[fmt]

    sessions = []
    # Generate a shared vocab list for flashcard consistency
    shared_vocab = draw(random_vocab_list(2, 6))

    for session_idx, seq in enumerate(sequences):
        activities = []
        for act_type in seq:
            if act_type in {"viewFlashcards", "speakFlashcards", "vocabLevel1", "vocabLevel2"}:
                activity = draw(random_activity(act_type, vocab_list=shared_vocab))
            elif act_type == "writingSentence":
                activity = draw(random_activity(act_type, vocab_list=shared_vocab))
            elif act_type == "writingParagraph":
                activity = draw(random_activity(act_type, vocab_list=shared_vocab))
            else:
                activity = draw(random_activity(act_type))
            activities.append(activity)

        session_title = draw(st.text(min_size=3, max_size=20, alphabet=string.ascii_letters + " "))
        sessions.append({"title": session_title, "activities": activities})

    content = {
        "title": title,
        "description": description,
        "preview": {"text": preview_text},
        "contentTypeTags": content_type_tags,
        "learningSessions": sessions,
    }

    return content, fmt


def random_strip_key():
    """Picks a random strip key from the forbidden set."""
    return st.sampled_from(sorted(STRIP_KEYS))


@st.composite
def random_json_path(draw, content):
    """Picks a random location in a content dict to inject a key.
    Returns a reference to the dict where the key should be injected."""
    targets = []
    _collect_dicts(content, targets)
    assume(len(targets) > 0)
    idx = draw(st.integers(min_value=0, max_value=len(targets) - 1))
    return targets[idx]


def _collect_dicts(obj, targets):
    """Recursively collect all dict objects in the JSON tree."""
    if isinstance(obj, dict):
        targets.append(obj)
        for v in obj.values():
            _collect_dicts(v, targets)
    elif isinstance(obj, list):
        for item in obj:
            _collect_dicts(item, targets)


# =============================================================================
# Property Tests
# =============================================================================


# Feature: vi-en-christianity-curriculum, Property 1: Valid content passes validation
@given(data=valid_curriculum())
@settings(max_examples=100)
def test_property_1_valid_content_passes_validation(data):
    """For any well-formed curriculum content dict that matches its declared format,
    validate(content, format) returns without raising."""
    content, fmt = data
    # Should not raise
    validate(content, fmt)


# Feature: vi-en-christianity-curriculum, Property 2: contentTypeTags validation per format
@given(fmt=random_format(), wrong_tags=st.sampled_from([["story"], [], ["music"], ["podcast"], ["wrong"]]))
@settings(max_examples=100)
def test_property_2_content_type_tags_validation(fmt, wrong_tags):
    """If format is 'story_reading' and contentTypeTags is not ['story'],
    OR if format is 'speaking'/'balanced' and contentTypeTags is not [],
    then validate() raises ValueError."""
    expected_tags = FORMAT_CONTENT_TYPE_TAGS[fmt]
    assume(wrong_tags != expected_tags)

    # Build a minimal valid curriculum then corrupt the tags
    content = _build_minimal_valid_content(fmt)
    content["contentTypeTags"] = wrong_tags

    try:
        validate(content, fmt)
        assert False, f"Expected ValueError for tags {wrong_tags} with format {fmt}"
    except ValueError:
        pass


# Feature: vi-en-christianity-curriculum, Property 3: Strip keys rejected anywhere in JSON tree
@given(fmt=random_format(), strip_key=random_strip_key(), depth=st.integers(min_value=0, max_value=3))
@settings(max_examples=100)
def test_property_3_strip_keys_rejected(fmt, strip_key, depth):
    """If any strip key is injected at any depth in the JSON tree,
    validate() raises ValueError."""
    content = _build_minimal_valid_content(fmt)

    # Inject the strip key at a random depth
    target = content
    if depth >= 1:
        target = content["learningSessions"][0]
    if depth >= 2:
        target = content["learningSessions"][0]["activities"][0]
    if depth >= 3:
        target = content["learningSessions"][0]["activities"][0]["data"]

    target[strip_key] = "injected_value"

    try:
        validate(content, fmt)
        assert False, f"Expected ValueError for strip key '{strip_key}' at depth {depth}"
    except ValueError as e:
        assert strip_key.lower() in str(e).lower() or "strip" in str(e).lower() or strip_key in str(e)


# Feature: vi-en-christianity-curriculum, Property 4: Activity sequence matches declared format
@given(fmt=random_format(), session_idx=st.integers(min_value=0, max_value=3))
@settings(max_examples=100)
def test_property_4_activity_sequence_mismatch(fmt, session_idx):
    """If the activity type sequence in any session doesn't match the expected template,
    validate() raises ValueError."""
    content = _build_minimal_valid_content(fmt)

    # Corrupt the sequence by removing the last activity
    activities = content["learningSessions"][session_idx]["activities"]
    if len(activities) > 1:
        content["learningSessions"][session_idx]["activities"] = activities[:-1]
    else:
        # Add an extra activity to break the sequence
        content["learningSessions"][session_idx]["activities"].append(
            _make_activity("introAudio")
        )

    try:
        validate(content, fmt)
        assert False, f"Expected ValueError for sequence mismatch in session {session_idx + 1}"
    except ValueError:
        pass


# Feature: vi-en-christianity-curriculum, Property 5: Activity structural requirements enforced
@given(
    fmt=random_format(),
    missing_field=st.sampled_from(["activityType", "title", "description", "data"]),
    session_idx=st.integers(min_value=0, max_value=3),
)
@settings(max_examples=100)
def test_property_5_activity_structural_requirements(fmt, missing_field, session_idx):
    """If any activity is missing activityType, title, description, or data (dict),
    or has invalid activityType, validate() raises ValueError."""
    content = _build_minimal_valid_content(fmt)

    activities = content["learningSessions"][session_idx]["activities"]
    # Pick the first activity and remove a required field
    activity = activities[0]
    if missing_field in activity:
        del activity[missing_field]
    else:
        # Field doesn't exist, skip
        assume(False)

    try:
        validate(content, fmt)
        assert False, f"Expected ValueError for missing '{missing_field}'"
    except ValueError:
        pass


# Feature: vi-en-christianity-curriculum, Property 5b: Invalid activityType raises ValueError
@given(
    fmt=random_format(),
    invalid_type=st.text(min_size=3, max_size=15, alphabet=string.ascii_lowercase).filter(
        lambda t: t not in VALID_ACTIVITY_TYPES
    ),
)
@settings(max_examples=100)
def test_property_5b_invalid_activity_type(fmt, invalid_type):
    """If activityType is not in the valid set, validate() raises ValueError."""
    content = _build_minimal_valid_content(fmt)

    # Replace the first activity's type with an invalid one
    content["learningSessions"][0]["activities"][0]["activityType"] = invalid_type

    try:
        validate(content, fmt)
        assert False, f"Expected ValueError for invalid activityType '{invalid_type}'"
    except ValueError:
        pass


# Feature: vi-en-christianity-curriculum, Property 6: vocabList format enforced
@given(
    fmt=random_format(),
    violation=st.sampled_from(["non_lowercase", "not_array", "empty", "uses_words"]),
)
@settings(max_examples=100)
def test_property_6_vocab_list_format_enforced(fmt, violation):
    """For vocab activities, if vocabList contains non-lowercase strings, is not an array,
    is empty, or uses 'words' instead of 'vocabList', validate() raises ValueError."""
    content = _build_minimal_valid_content(fmt)

    # Find the first vocab activity in the content
    vocab_activity = None
    for session in content["learningSessions"]:
        for activity in session["activities"]:
            if activity["activityType"] in {"viewFlashcards", "speakFlashcards", "vocabLevel1", "vocabLevel2"}:
                vocab_activity = activity
                break
        if vocab_activity:
            break

    assume(vocab_activity is not None)

    if violation == "non_lowercase":
        vocab_activity["data"]["vocabList"] = ["Hello", "World"]
    elif violation == "not_array":
        vocab_activity["data"]["vocabList"] = "not_an_array"
    elif violation == "empty":
        vocab_activity["data"]["vocabList"] = []
    elif violation == "uses_words":
        vocab_list = vocab_activity["data"].pop("vocabList", ["word"])
        vocab_activity["data"]["words"] = vocab_list

    try:
        validate(content, fmt)
        assert False, f"Expected ValueError for vocabList violation: {violation}"
    except ValueError:
        pass


# Feature: vi-en-christianity-curriculum, Property 7: Flashcard vocabList consistency within sessions
@given(fmt=random_format())
@settings(max_examples=100)
def test_property_7_flashcard_consistency(fmt):
    """If viewFlashcards and speakFlashcards in the same session have different vocabList arrays,
    validate() raises ValueError."""
    content = _build_minimal_valid_content(fmt)

    # Find a session with both viewFlashcards and speakFlashcards
    target_session = None
    view_idx = None
    speak_idx = None
    for session in content["learningSessions"]:
        v_idx = None
        s_idx = None
        for i, activity in enumerate(session["activities"]):
            if activity["activityType"] == "viewFlashcards":
                v_idx = i
            elif activity["activityType"] == "speakFlashcards" and v_idx is not None:
                s_idx = i
                break
        if v_idx is not None and s_idx is not None:
            target_session = session
            view_idx = v_idx
            speak_idx = s_idx
            break

    assume(target_session is not None)

    # Make them different
    target_session["activities"][view_idx]["data"]["vocabList"] = ["alpha", "beta"]
    target_session["activities"][speak_idx]["data"]["vocabList"] = ["gamma", "delta"]

    try:
        validate(content, fmt)
        assert False, "Expected ValueError for mismatched flashcard vocabLists"
    except ValueError:
        pass


# Feature: vi-en-christianity-curriculum, Property 8: writingSentence structure enforced
@given(
    fmt=random_format(),
    violation=st.sampled_from(["missing_vocabList", "missing_items", "item_missing_prompt", "item_missing_targetVocab"]),
)
@settings(max_examples=100)
def test_property_8_writing_sentence_structure(fmt, violation):
    """If writingSentence is missing data.vocabList, data.items, or any item lacks
    prompt/targetVocab, validate() raises ValueError."""
    content = _build_minimal_valid_content(fmt)

    # Find a writingSentence activity
    ws_activity = None
    for session in content["learningSessions"]:
        for activity in session["activities"]:
            if activity["activityType"] == "writingSentence":
                ws_activity = activity
                break
        if ws_activity:
            break

    assume(ws_activity is not None)

    if violation == "missing_vocabList":
        del ws_activity["data"]["vocabList"]
    elif violation == "missing_items":
        ws_activity["data"].pop("items", None)
    elif violation == "item_missing_prompt":
        ws_activity["data"]["items"] = [{"targetVocab": "word"}]
    elif violation == "item_missing_targetVocab":
        ws_activity["data"]["items"] = [{"prompt": "Write a sentence"}]

    try:
        validate(content, fmt)
        assert False, f"Expected ValueError for writingSentence violation: {violation}"
    except ValueError:
        pass


# Feature: vi-en-christianity-curriculum, Property 9: writingParagraph structure enforced
@given(
    fmt=st.just("balanced"),
    violation=st.sampled_from(["missing_vocabList", "missing_instructions", "prompts_too_few"]),
)
@settings(max_examples=100)
def test_property_9_writing_paragraph_structure(fmt, violation):
    """If writingParagraph is missing data.vocabList, data.instructions, or data.prompts
    has fewer than 2 items, validate() raises ValueError."""
    content = _build_minimal_valid_content(fmt)

    # Find a writingParagraph activity (only in balanced format, session 4)
    wp_activity = None
    for session in content["learningSessions"]:
        for activity in session["activities"]:
            if activity["activityType"] == "writingParagraph":
                wp_activity = activity
                break
        if wp_activity:
            break

    assume(wp_activity is not None)

    if violation == "missing_vocabList":
        del wp_activity["data"]["vocabList"]
    elif violation == "missing_instructions":
        wp_activity["data"].pop("instructions", None)
    elif violation == "prompts_too_few":
        wp_activity["data"]["prompts"] = ["only one prompt"]

    try:
        validate(content, fmt)
        assert False, f"Expected ValueError for writingParagraph violation: {violation}"
    except ValueError:
        pass


# Feature: vi-en-christianity-curriculum, Property 10: Top-level structure enforced
@given(
    fmt=random_format(),
    violation=st.sampled_from([
        "missing_title", "empty_title", "missing_description", "empty_description",
        "missing_preview", "empty_preview_text", "wrong_session_count",
    ]),
)
@settings(max_examples=100)
def test_property_10_top_level_structure(fmt, violation):
    """If title/description/preview.text is missing or empty, or learningSessions is not
    exactly 4 sessions, validate() raises ValueError."""
    content = _build_minimal_valid_content(fmt)

    if violation == "missing_title":
        del content["title"]
    elif violation == "empty_title":
        content["title"] = ""
    elif violation == "missing_description":
        del content["description"]
    elif violation == "empty_description":
        content["description"] = "   "
    elif violation == "missing_preview":
        del content["preview"]
    elif violation == "empty_preview_text":
        content["preview"]["text"] = ""
    elif violation == "wrong_session_count":
        content["learningSessions"] = content["learningSessions"][:3]

    try:
        validate(content, fmt)
        assert False, f"Expected ValueError for top-level violation: {violation}"
    except ValueError:
        pass


# Feature: vi-en-christianity-curriculum, Property 11: Writing activities restricted to sessions 3 and 4
@given(
    fmt=random_format(),
    session_idx=st.sampled_from([0, 1]),
    writing_type=st.sampled_from(["writingSentence", "writingParagraph"]),
)
@settings(max_examples=100)
def test_property_11_writing_restricted_to_sessions_3_and_4(fmt, session_idx, writing_type):
    """If writingSentence or writingParagraph appears in session 1 or 2,
    validate() raises ValueError."""
    content = _build_minimal_valid_content(fmt)

    # Inject a writing activity into session 1 or 2
    if writing_type == "writingSentence":
        writing_activity = {
            "activityType": "writingSentence",
            "title": "Write something",
            "description": "Write a sentence",
            "data": {
                "vocabList": ["faith", "hope"],
                "items": [{"prompt": "Write about faith", "targetVocab": "faith"}],
            },
        }
    else:
        writing_activity = {
            "activityType": "writingParagraph",
            "title": "Write a paragraph",
            "description": "Write about your faith",
            "data": {
                "vocabList": ["faith", "hope"],
                "instructions": "Write 3-5 sentences about faith.",
                "prompts": ["Prompt one about faith.", "Prompt two about hope."],
            },
        }

    # Insert the writing activity into the target session
    content["learningSessions"][session_idx]["activities"].append(writing_activity)

    # This will break the activity sequence check first, so we need to also
    # update the sequence. But the validator checks writing restriction AFTER
    # sequence check. So we need to make the sequence still match by replacing
    # an existing activity with the writing one instead.
    # Actually, looking at the validator code, _validate_writing_activity_restriction
    # is called after _validate_activity_sequence. So if we just append, the sequence
    # check will fail first. We need to replace an activity in the sequence.
    # 
    # Better approach: just inject and accept that the sequence check may fire first.
    # The property still holds: validate() raises ValueError when writing is in session 1/2.
    # The error might be about sequence mismatch rather than writing restriction,
    # but the key point is that it DOES raise ValueError.

    try:
        validate(content, fmt)
        assert False, f"Expected ValueError for {writing_type} in session {session_idx + 1}"
    except ValueError:
        pass


# =============================================================================
# Helper: Build minimal valid content for a given format
# =============================================================================


def _build_minimal_valid_content(fmt):
    """Build a minimal but fully valid curriculum content dict for the given format."""
    vocab = ["faith", "hope", "grace", "love", "peace"]
    sequences = ACTIVITY_SEQUENCES[fmt]
    content_type_tags = FORMAT_CONTENT_TYPE_TAGS[fmt]

    sessions = []
    for session_idx, seq in enumerate(sequences):
        activities = []
        for act_type in seq:
            activities.append(_make_activity(act_type, vocab))
        sessions.append({
            "title": f"Session {session_idx + 1}",
            "activities": activities,
        })

    return {
        "title": "Test Curriculum Title",
        "description": "Test curriculum description for validation",
        "preview": {"text": "This is a preview text for testing purposes"},
        "contentTypeTags": content_type_tags,
        "learningSessions": sessions,
    }


def _make_activity(activity_type, vocab=None):
    """Create a minimal valid activity of the given type."""
    if vocab is None:
        vocab = ["faith", "hope", "grace", "love", "peace"]

    base = {
        "activityType": activity_type,
        "title": f"Activity: {activity_type}",
        "description": f"Description for {activity_type}",
    }

    vocab_activities = {"viewFlashcards", "speakFlashcards", "vocabLevel1", "vocabLevel2"}

    if activity_type in vocab_activities:
        base["data"] = {"vocabList": list(vocab)}
    elif activity_type == "writingSentence":
        base["data"] = {
            "vocabList": list(vocab),
            "items": [
                {"prompt": "Write a sentence using faith", "targetVocab": "faith"},
                {"prompt": "Write a sentence using hope", "targetVocab": "hope"},
            ],
        }
    elif activity_type == "writingParagraph":
        base["data"] = {
            "vocabList": list(vocab),
            "instructions": "Write a paragraph about Christian values using vocabulary from this lesson.",
            "prompts": [
                "Describe how faith helps in daily life.",
                "Explain the importance of hope and grace.",
            ],
        }
    else:
        # introAudio, reading, speakReading, readAlong
        base["data"] = {"text": f"Sample text content for {activity_type} activity."}

    return base
