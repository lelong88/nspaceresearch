"""
Property-based tests for validate_content.py using Hypothesis.

Feature: vi-en-buddhism-meditation
Tests the 11 correctness properties defined in the design document.
"""

import copy
import string
import sys

import pytest
from hypothesis import given, settings, assume
from hypothesis import strategies as st

sys.path.insert(0, "vi-en-buddhism-meditation")
from validate_content import (
    validate,
    ACTIVITY_SEQUENCES,
    STRIP_KEYS,
    VALID_ACTIVITY_TYPES,
    VOCAB_ACTIVITY_TYPES,
    CONTENT_TYPE_TAGS,
    WRITING_ACTIVITY_TYPES,
)


# ─── Generator Strategies ───────────────────────────────────────────────────────


@st.composite
def random_format(draw):
    """Picks one of 'story_reading', 'speaking', 'balanced'."""
    return draw(st.sampled_from(["story_reading", "speaking", "balanced"]))


@st.composite
def random_vocab_list(draw, min_size=1, max_size=12):
    """Generates a list of n random lowercase English strings."""
    n = draw(st.integers(min_value=min_size, max_value=max_size))
    words = draw(
        st.lists(
            st.text(
                alphabet=string.ascii_lowercase, min_size=3, max_size=10
            ),
            min_size=n,
            max_size=n,
        )
    )
    return words


@st.composite
def random_activity(draw, activity_type, vocab_list=None):
    """Generates a valid activity of the given type with all required fields."""
    title = draw(st.text(min_size=3, max_size=30, alphabet=string.ascii_letters + " "))
    description = draw(st.text(min_size=3, max_size=50, alphabet=string.ascii_letters + " "))

    if vocab_list is None:
        vocab_list = draw(random_vocab_list(min_size=3, max_size=8))

    data = {}

    if activity_type in VOCAB_ACTIVITY_TYPES:
        data["vocabList"] = vocab_list

    elif activity_type == "writingSentence":
        data["vocabList"] = vocab_list
        items_count = draw(st.integers(min_value=2, max_value=4))
        items = []
        for _ in range(items_count):
            items.append({
                "prompt": draw(st.text(min_size=5, max_size=40, alphabet=string.ascii_letters + " ")),
                "targetVocab": draw(st.text(min_size=3, max_size=15, alphabet=string.ascii_lowercase)),
            })
        data["items"] = items

    elif activity_type == "writingParagraph":
        data["vocabList"] = vocab_list
        data["instructions"] = draw(st.text(min_size=10, max_size=60, alphabet=string.ascii_letters + " "))
        prompts_count = draw(st.integers(min_value=2, max_value=4))
        data["prompts"] = draw(
            st.lists(
                st.text(min_size=5, max_size=40, alphabet=string.ascii_letters + " "),
                min_size=prompts_count,
                max_size=prompts_count,
            )
        )

    elif activity_type == "reading":
        data["text"] = draw(st.text(min_size=20, max_size=100, alphabet=string.ascii_letters + " ."))

    elif activity_type == "speakReading":
        data["text"] = draw(st.text(min_size=20, max_size=100, alphabet=string.ascii_letters + " ."))

    elif activity_type == "readAlong":
        data["text"] = draw(st.text(min_size=20, max_size=100, alphabet=string.ascii_letters + " ."))

    elif activity_type == "introAudio":
        data["script"] = draw(st.text(min_size=20, max_size=100, alphabet=string.ascii_letters + " ."))

    return {
        "activityType": activity_type,
        "title": title,
        "description": description,
        "data": data,
    }


@st.composite
def valid_curriculum(draw, fmt):
    """Generates a structurally valid curriculum content dict for the given format."""
    title = draw(st.text(min_size=3, max_size=30, alphabet=string.ascii_letters + " "))
    description = draw(st.text(min_size=10, max_size=80, alphabet=string.ascii_letters + " "))
    preview_text = draw(st.text(min_size=10, max_size=80, alphabet=string.ascii_letters + " "))

    content_type_tags = CONTENT_TYPE_TAGS[fmt]
    sequences = ACTIVITY_SEQUENCES[fmt]

    # Generate a shared vocab list for the curriculum
    vocab_list = draw(random_vocab_list(min_size=4, max_size=10))

    sessions = []
    for session_idx in range(4):
        session_title = draw(st.text(min_size=3, max_size=20, alphabet=string.ascii_letters + " "))
        activity_sequence = sequences[session_idx]

        activities = []
        for act_type in activity_sequence:
            activity = draw(random_activity(act_type, vocab_list=vocab_list))
            activities.append(activity)

        sessions.append({
            "title": session_title,
            "activities": activities,
        })

    return {
        "title": title,
        "description": description,
        "preview": {"text": preview_text},
        "contentTypeTags": content_type_tags,
        "learningSessions": sessions,
    }


@st.composite
def random_strip_key(draw):
    """Picks a random strip key from the forbidden set."""
    return draw(st.sampled_from(sorted(STRIP_KEYS)))


@st.composite
def random_json_path(draw, content):
    """Picks a random location in a content dict to inject a key.
    Returns a reference to the dict where the key should be injected."""
    # Collect all dicts in the tree
    targets = []

    def collect_dicts(obj, path=""):
        if isinstance(obj, dict):
            targets.append(obj)
            for k, v in obj.items():
                collect_dicts(v, f"{path}.{k}")
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                collect_dicts(item, f"{path}[{i}]")

    collect_dicts(content)
    assume(len(targets) > 0)
    return draw(st.sampled_from(targets))


# ─── Property Tests ─────────────────────────────────────────────────────────────


# Feature: vi-en-buddhism-meditation, Property 1: Valid content passes validation
class TestProperty1:
    """Valid content passes validation."""

    @settings(max_examples=100)
    @given(data=st.data())
    def test_valid_content_passes_validation(self, data):
        """
        **Validates: Requirements 1.4, 1.5, 1.6, 3.1, 3.2, 3.3, 3.4, 10.1-10.11**

        For any well-formed curriculum content generated according to the format
        template, validate() should not raise.
        """
        fmt = data.draw(random_format())
        content = data.draw(valid_curriculum(fmt))
        validate(content, fmt)


# Feature: vi-en-buddhism-meditation, Property 2: contentTypeTags validation per format
class TestProperty2:
    """contentTypeTags validation per format."""

    @settings(max_examples=100)
    @given(fmt=random_format(), data=st.data())
    def test_wrong_content_type_tags_raises(self, fmt, data):
        """
        **Validates: Requirements 1.4, 1.5, 10.10**

        If story_reading has wrong tags or speaking/balanced has wrong tags,
        validate() raises ValueError.
        """
        content = data.draw(valid_curriculum(fmt))
        expected_tags = CONTENT_TYPE_TAGS[fmt]

        # Generate wrong tags
        if expected_tags == ["story"]:
            wrong_tags = data.draw(st.sampled_from([[], ["music"], ["podcast"], ["movie"]]))
        else:
            wrong_tags = data.draw(st.sampled_from([["story"], ["music"], ["podcast"], ["movie"]]))

        content["contentTypeTags"] = wrong_tags

        with pytest.raises(ValueError):
            validate(content, fmt)


# Feature: vi-en-buddhism-meditation, Property 3: Strip keys rejected anywhere in JSON tree
class TestProperty3:
    """Strip keys rejected anywhere in JSON tree."""

    @settings(max_examples=100)
    @given(fmt=random_format(), data=st.data())
    def test_strip_key_injected_raises(self, fmt, data):
        """
        **Validates: Requirements 1.6, 9.5, 10.9**

        Inject any strip key at any depth, validate() raises ValueError.
        """
        content = data.draw(valid_curriculum(fmt))
        strip_key = data.draw(random_strip_key())

        # Find a random dict in the tree to inject the key
        target = data.draw(random_json_path(content))
        target[strip_key] = "injected_value"

        with pytest.raises(ValueError):
            validate(content, fmt)


# Feature: vi-en-buddhism-meditation, Property 4: Activity sequence matches declared format
class TestProperty4:
    """Activity sequence matches declared format."""

    @settings(max_examples=100)
    @given(fmt=random_format(), data=st.data())
    def test_wrong_activity_sequence_raises(self, fmt, data):
        """
        **Validates: Requirements 3.1, 3.2, 3.3, 10.11**

        If activity sequence doesn't match template, validate() raises ValueError.
        """
        content = data.draw(valid_curriculum(fmt))

        # Pick a random session to corrupt
        session_idx = data.draw(st.integers(min_value=0, max_value=3))
        session = content["learningSessions"][session_idx]
        activities = session["activities"]

        # Corrupt the sequence: either swap two activities, remove one, or add one
        mutation = data.draw(st.sampled_from(["swap", "remove", "add"]))

        if mutation == "swap" and len(activities) >= 2:
            i = data.draw(st.integers(min_value=0, max_value=len(activities) - 2))
            j = i + 1
            # Only swap if they have different types (otherwise sequence unchanged)
            assume(activities[i]["activityType"] != activities[j]["activityType"])
            activities[i], activities[j] = activities[j], activities[i]
        elif mutation == "remove" and len(activities) >= 2:
            idx = data.draw(st.integers(min_value=0, max_value=len(activities) - 1))
            activities.pop(idx)
        else:
            # Add an extra activity
            extra_type = data.draw(st.sampled_from(sorted(VALID_ACTIVITY_TYPES)))
            vocab = data.draw(random_vocab_list(min_size=3, max_size=5))
            extra = data.draw(random_activity(extra_type, vocab_list=vocab))
            insert_idx = data.draw(st.integers(min_value=0, max_value=len(activities)))
            activities.insert(insert_idx, extra)

        with pytest.raises(ValueError):
            validate(content, fmt)


# Feature: vi-en-buddhism-meditation, Property 5: Activity structural requirements enforced
class TestProperty5:
    """Activity structural requirements enforced."""

    @settings(max_examples=100)
    @given(fmt=random_format(), data=st.data())
    def test_missing_activity_fields_raises(self, fmt, data):
        """
        **Validates: Requirements 9.1, 9.2, 10.3, 10.4**

        Missing activityType/title/description/data raises ValueError.
        """
        content = data.draw(valid_curriculum(fmt))

        # Pick a random session and activity
        session_idx = data.draw(st.integers(min_value=0, max_value=3))
        session = content["learningSessions"][session_idx]
        activities = session["activities"]
        activity_idx = data.draw(st.integers(min_value=0, max_value=len(activities) - 1))

        # Remove a required field
        field_to_remove = data.draw(st.sampled_from(["activityType", "title", "description", "data"]))
        if field_to_remove in activities[activity_idx]:
            del activities[activity_idx][field_to_remove]
        else:
            assume(False)

        with pytest.raises(ValueError):
            validate(content, fmt)


# Feature: vi-en-buddhism-meditation, Property 6: vocabList format enforced
class TestProperty6:
    """vocabList format enforced."""

    @settings(max_examples=100)
    @given(fmt=random_format(), data=st.data())
    def test_invalid_vocab_list_raises(self, fmt, data):
        """
        **Validates: Requirements 9.3, 10.5**

        Non-lowercase strings, non-array, empty, or field named 'words' raises ValueError.
        """
        content = data.draw(valid_curriculum(fmt))

        # Find a vocab activity in the content
        vocab_activities = []
        for s_idx, session in enumerate(content["learningSessions"]):
            for a_idx, activity in enumerate(session["activities"]):
                if activity["activityType"] in VOCAB_ACTIVITY_TYPES:
                    vocab_activities.append((s_idx, a_idx))

        assume(len(vocab_activities) > 0)
        s_idx, a_idx = data.draw(st.sampled_from(vocab_activities))
        activity = content["learningSessions"][s_idx]["activities"][a_idx]

        # Choose a corruption type
        corruption = data.draw(st.sampled_from([
            "non_lowercase", "non_array", "empty", "words_field"
        ]))

        if corruption == "non_lowercase":
            activity["data"]["vocabList"] = ["Hello", "World", "Test"]
        elif corruption == "non_array":
            activity["data"]["vocabList"] = "not_an_array"
        elif corruption == "empty":
            activity["data"]["vocabList"] = []
        elif corruption == "words_field":
            vocab = activity["data"].pop("vocabList")
            activity["data"]["words"] = vocab

        with pytest.raises(ValueError):
            validate(content, fmt)


# Feature: vi-en-buddhism-meditation, Property 7: Flashcard vocabList consistency within sessions
class TestProperty7:
    """Flashcard vocabList consistency within sessions."""

    @settings(max_examples=100)
    @given(fmt=random_format(), data=st.data())
    def test_mismatched_flashcard_vocab_raises(self, fmt, data):
        """
        **Validates: Requirements 9.4, 10.6**

        Mismatched viewFlashcards/speakFlashcards vocabList raises ValueError.
        """
        content = data.draw(valid_curriculum(fmt))

        # Find a session with both viewFlashcards and speakFlashcards
        target_sessions = []
        for s_idx, session in enumerate(content["learningSessions"]):
            has_view = False
            has_speak = False
            for activity in session["activities"]:
                if activity["activityType"] == "viewFlashcards":
                    has_view = True
                elif activity["activityType"] == "speakFlashcards":
                    has_speak = True
            if has_view and has_speak:
                target_sessions.append(s_idx)

        assume(len(target_sessions) > 0)
        s_idx = data.draw(st.sampled_from(target_sessions))
        session = content["learningSessions"][s_idx]

        # Find the speakFlashcards activity and change its vocabList
        for activity in session["activities"]:
            if activity["activityType"] == "speakFlashcards":
                # Generate a different vocab list
                different_vocab = data.draw(random_vocab_list(min_size=3, max_size=6))
                # Ensure it's actually different
                assume(different_vocab != activity["data"]["vocabList"])
                activity["data"]["vocabList"] = different_vocab
                break

        with pytest.raises(ValueError):
            validate(content, fmt)


# Feature: vi-en-buddhism-meditation, Property 8: writingSentence structure enforced
class TestProperty8:
    """writingSentence structure enforced."""

    @settings(max_examples=100)
    @given(fmt=random_format(), data=st.data())
    def test_invalid_writing_sentence_raises(self, fmt, data):
        """
        **Validates: Requirements 9.6, 10.7**

        Missing vocabList, items, or item fields raises ValueError.
        """
        content = data.draw(valid_curriculum(fmt))

        # Find a writingSentence activity
        ws_activities = []
        for s_idx, session in enumerate(content["learningSessions"]):
            for a_idx, activity in enumerate(session["activities"]):
                if activity["activityType"] == "writingSentence":
                    ws_activities.append((s_idx, a_idx))

        assume(len(ws_activities) > 0)
        s_idx, a_idx = data.draw(st.sampled_from(ws_activities))
        activity = content["learningSessions"][s_idx]["activities"][a_idx]

        # Choose a corruption type
        corruption = data.draw(st.sampled_from([
            "missing_vocabList", "missing_items", "empty_items",
            "missing_prompt", "missing_targetVocab"
        ]))

        if corruption == "missing_vocabList":
            del activity["data"]["vocabList"]
        elif corruption == "missing_items":
            if "items" in activity["data"]:
                del activity["data"]["items"]
            else:
                assume(False)
        elif corruption == "empty_items":
            activity["data"]["items"] = []
        elif corruption == "missing_prompt":
            if activity["data"].get("items"):
                item_idx = data.draw(st.integers(min_value=0, max_value=len(activity["data"]["items"]) - 1))
                del activity["data"]["items"][item_idx]["prompt"]
            else:
                assume(False)
        elif corruption == "missing_targetVocab":
            if activity["data"].get("items"):
                item_idx = data.draw(st.integers(min_value=0, max_value=len(activity["data"]["items"]) - 1))
                del activity["data"]["items"][item_idx]["targetVocab"]
            else:
                assume(False)

        with pytest.raises(ValueError):
            validate(content, fmt)


# Feature: vi-en-buddhism-meditation, Property 9: writingParagraph structure enforced
class TestProperty9:
    """writingParagraph structure enforced."""

    @settings(max_examples=100)
    @given(fmt=random_format(), data=st.data())
    def test_invalid_writing_paragraph_raises(self, fmt, data):
        """
        **Validates: Requirements 9.7, 10.8**

        Missing vocabList, instructions, or prompts (< 2) raises ValueError.
        """
        content = data.draw(valid_curriculum(fmt))

        # Find a writingParagraph activity
        wp_activities = []
        for s_idx, session in enumerate(content["learningSessions"]):
            for a_idx, activity in enumerate(session["activities"]):
                if activity["activityType"] == "writingParagraph":
                    wp_activities.append((s_idx, a_idx))

        assume(len(wp_activities) > 0)
        s_idx, a_idx = data.draw(st.sampled_from(wp_activities))
        activity = content["learningSessions"][s_idx]["activities"][a_idx]

        # Choose a corruption type
        corruption = data.draw(st.sampled_from([
            "missing_vocabList", "missing_instructions", "empty_instructions",
            "missing_prompts", "too_few_prompts"
        ]))

        if corruption == "missing_vocabList":
            del activity["data"]["vocabList"]
        elif corruption == "missing_instructions":
            if "instructions" in activity["data"]:
                del activity["data"]["instructions"]
            else:
                assume(False)
        elif corruption == "empty_instructions":
            activity["data"]["instructions"] = ""
        elif corruption == "missing_prompts":
            if "prompts" in activity["data"]:
                del activity["data"]["prompts"]
            else:
                assume(False)
        elif corruption == "too_few_prompts":
            activity["data"]["prompts"] = ["only one"]

        with pytest.raises(ValueError):
            validate(content, fmt)


# Feature: vi-en-buddhism-meditation, Property 10: Top-level structure enforced
class TestProperty10:
    """Top-level structure enforced."""

    @settings(max_examples=100)
    @given(fmt=random_format(), data=st.data())
    def test_invalid_top_level_raises(self, fmt, data):
        """
        **Validates: Requirements 10.1, 10.2, 3.4**

        Missing/empty title, description, preview.text, or wrong session count
        raises ValueError.
        """
        content = data.draw(valid_curriculum(fmt))

        # Choose a corruption type
        corruption = data.draw(st.sampled_from([
            "missing_title", "empty_title",
            "missing_description", "empty_description",
            "missing_preview_text", "empty_preview_text",
            "wrong_session_count_less", "wrong_session_count_more",
        ]))

        if corruption == "missing_title":
            del content["title"]
        elif corruption == "empty_title":
            content["title"] = ""
        elif corruption == "missing_description":
            del content["description"]
        elif corruption == "empty_description":
            content["description"] = ""
        elif corruption == "missing_preview_text":
            content["preview"] = {}
        elif corruption == "empty_preview_text":
            content["preview"]["text"] = ""
        elif corruption == "wrong_session_count_less":
            # Remove sessions to have fewer than 4
            remove_count = data.draw(st.integers(min_value=1, max_value=3))
            content["learningSessions"] = content["learningSessions"][:4 - remove_count]
        elif corruption == "wrong_session_count_more":
            # Add an extra session
            extra_session = copy.deepcopy(content["learningSessions"][0])
            content["learningSessions"].append(extra_session)

        with pytest.raises(ValueError):
            validate(content, fmt)


# Feature: vi-en-buddhism-meditation, Property 11: Writing activities restricted to sessions 3 and 4
class TestProperty11:
    """Writing activities restricted to sessions 3 and 4."""

    @settings(max_examples=100)
    @given(fmt=random_format(), data=st.data())
    def test_writing_in_early_sessions_raises(self, fmt, data):
        """
        **Validates: Requirements 16.4**

        Writing activities in session 1 or 2 raises ValueError.
        """
        content = data.draw(valid_curriculum(fmt))

        # Pick session 0 or 1 (sessions 1 or 2 in 1-indexed)
        session_idx = data.draw(st.integers(min_value=0, max_value=1))
        session = content["learningSessions"][session_idx]

        # Pick a writing activity type
        writing_type = data.draw(st.sampled_from(sorted(WRITING_ACTIVITY_TYPES)))

        # Generate a valid writing activity
        vocab = data.draw(random_vocab_list(min_size=3, max_size=6))
        writing_activity = data.draw(random_activity(writing_type, vocab_list=vocab))

        # Insert it into the session (this will also break the sequence, but
        # the writing restriction check should catch it regardless)
        session["activities"].append(writing_activity)

        with pytest.raises(ValueError):
            validate(content, fmt)
