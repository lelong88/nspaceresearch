"""
Property-based tests for the validate() function in create_digital_economy_onboarding.py.

Uses Hypothesis to generate varied inputs and verify universal correctness properties
of the curriculum content validator.
"""

import copy
import random
import string

import pytest
from hypothesis import given, settings, assume
from hypothesis.strategies import (
    composite,
    text,
    lists,
    sampled_from,
    integers,
    just,
    one_of,
    none,
    booleans,
)

from create_digital_economy_onboarding import (
    validate,
    STRIP_KEYS,
    VALID_ACTIVITY_TYPES,
    EXPECTED_SEQUENCE,
)


# ---------------------------------------------------------------------------
# Generator Strategies
# ---------------------------------------------------------------------------


@composite
def valid_vocab_lists(draw):
    """Generate a valid vocabList: exactly 5 lowercase words."""
    words = []
    for _ in range(5):
        word = draw(
            text(
                alphabet=string.ascii_lowercase,
                min_size=3,
                max_size=12,
            )
        )
        words.append(word)
    return words


@composite
def valid_writing_items(draw, vocab_list):
    """Generate valid writingSentence items targeting words from the vocab list."""
    num_items = draw(integers(min_value=2, max_value=3))
    items = []
    for i in range(num_items):
        target = vocab_list[i % len(vocab_list)]
        prompt = draw(
            text(
                alphabet=string.ascii_letters + string.digits + " .,!?'",
                min_size=20,
                max_size=100,
            )
        )
        items.append({"prompt": prompt, "targetVocab": target})
    return items


@composite
def valid_content(draw):
    """
    Generate a well-formed curriculum content dict that satisfies all validation constraints.

    Structure: 1 session, 9 activities in EXPECTED_SEQUENCE order, all fields present,
    vocabList with exactly 5 lowercase words, viewFlashcards and speakFlashcards have
    identical vocabLists.
    """
    # Generate varied but valid text fields
    title = draw(text(alphabet=string.ascii_letters + " ", min_size=3, max_size=30))
    assume(title.strip() != "")

    description = draw(
        text(alphabet=string.ascii_letters + string.digits + " .,!?\n", min_size=10, max_size=200)
    )
    assume(description.strip() != "")

    preview_text = draw(
        text(alphabet=string.ascii_letters + string.digits + " .,!?\n", min_size=10, max_size=200)
    )
    assume(preview_text.strip() != "")

    session_title = draw(
        text(alphabet=string.ascii_letters + " ", min_size=3, max_size=30)
    )
    assume(session_title.strip() != "")

    # Generate a single vocabList used across all activities that need it
    vocab_list = draw(valid_vocab_lists())

    # Generate writing items
    writing_items = draw(valid_writing_items(vocab_list))

    # Generate reading text
    reading_text = draw(
        text(
            alphabet=string.ascii_letters + string.digits + " .,!?'",
            min_size=50,
            max_size=300,
        )
    )
    assume(reading_text.strip() != "")

    # Generate introAudio text
    intro_text = draw(
        text(
            alphabet=string.ascii_letters + string.digits + " .,!?'\n",
            min_size=50,
            max_size=300,
        )
    )
    assume(intro_text.strip() != "")

    farewell_text = draw(
        text(
            alphabet=string.ascii_letters + string.digits + " .,!?'\n",
            min_size=50,
            max_size=300,
        )
    )
    assume(farewell_text.strip() != "")

    # Build activities in the exact EXPECTED_SEQUENCE order
    activities = [
        # 1. introAudio (welcome)
        {
            "activityType": "introAudio",
            "title": draw(text(alphabet=string.ascii_letters + " ", min_size=3, max_size=30)),
            "description": draw(text(alphabet=string.ascii_letters + " ", min_size=3, max_size=50)),
            "data": {"text": intro_text},
        },
        # 2. viewFlashcards
        {
            "activityType": "viewFlashcards",
            "title": draw(text(alphabet=string.ascii_letters + " ", min_size=3, max_size=30)),
            "description": draw(text(alphabet=string.ascii_letters + " ", min_size=3, max_size=50)),
            "data": {"vocabList": list(vocab_list)},
        },
        # 3. speakFlashcards (identical vocabList)
        {
            "activityType": "speakFlashcards",
            "title": draw(text(alphabet=string.ascii_letters + " ", min_size=3, max_size=30)),
            "description": draw(text(alphabet=string.ascii_letters + " ", min_size=3, max_size=50)),
            "data": {"vocabList": list(vocab_list)},
        },
        # 4. vocabLevel1
        {
            "activityType": "vocabLevel1",
            "title": draw(text(alphabet=string.ascii_letters + " ", min_size=3, max_size=30)),
            "description": draw(text(alphabet=string.ascii_letters + " ", min_size=3, max_size=50)),
            "data": {"vocabList": list(vocab_list)},
        },
        # 5. reading
        {
            "activityType": "reading",
            "title": draw(text(alphabet=string.ascii_letters + " ", min_size=3, max_size=30)),
            "description": draw(text(alphabet=string.ascii_letters + " ", min_size=3, max_size=50)),
            "data": {"text": reading_text, "vocabList": list(vocab_list)},
        },
        # 6. speakReading
        {
            "activityType": "speakReading",
            "title": draw(text(alphabet=string.ascii_letters + " ", min_size=3, max_size=30)),
            "description": draw(text(alphabet=string.ascii_letters + " ", min_size=3, max_size=50)),
            "data": {"text": reading_text},
        },
        # 7. readAlong
        {
            "activityType": "readAlong",
            "title": draw(text(alphabet=string.ascii_letters + " ", min_size=3, max_size=30)),
            "description": draw(text(alphabet=string.ascii_letters + " ", min_size=3, max_size=50)),
            "data": {"text": reading_text},
        },
        # 8. writingSentence
        {
            "activityType": "writingSentence",
            "title": draw(text(alphabet=string.ascii_letters + " ", min_size=3, max_size=30)),
            "description": draw(text(alphabet=string.ascii_letters + " ", min_size=3, max_size=50)),
            "data": {"vocabList": list(vocab_list), "items": writing_items},
        },
        # 9. introAudio (farewell)
        {
            "activityType": "introAudio",
            "title": draw(text(alphabet=string.ascii_letters + " ", min_size=3, max_size=30)),
            "description": draw(text(alphabet=string.ascii_letters + " ", min_size=3, max_size=50)),
            "data": {"text": farewell_text},
        },
    ]

    # Ensure all activity titles and descriptions are non-empty after strip
    for act in activities:
        assume(act["title"].strip() != "")
        assume(act["description"].strip() != "")

    content = {
        "title": title,
        "description": description,
        "preview": {"text": preview_text},
        "contentTypeTags": [],
        "learningSessions": [
            {
                "title": session_title,
                "activities": activities,
            }
        ],
    }

    return content


# ---------------------------------------------------------------------------
# Property Tests
# ---------------------------------------------------------------------------


# Feature: digital-economy-onboarding-curriculum, Property 1: Structural validity — valid content passes validation
@given(content=valid_content())
@settings(max_examples=100)
def test_valid_content_passes_validation(content):
    """
    Property 1: Any well-formed curriculum content dict that satisfies all constraints
    should pass validation without raising an exception.

    **Validates: Requirements 1.4, 1.5, 3.1, 3.2, 4.1, 4.2, 4.3, 4.4, 4.6, 10.1-10.10**
    """
    # Should not raise
    validate(content)


# Feature: digital-economy-onboarding-curriculum, Property 2: Strip keys rejected anywhere in JSON tree
@given(
    content=valid_content(),
    strip_key=sampled_from(sorted(STRIP_KEYS)),
    depth=integers(min_value=0, max_value=3),
)
@settings(max_examples=100)
def test_strip_keys_rejected_anywhere(content, strip_key, depth):
    """
    Property 2: If any strip key is injected at any depth in the JSON tree,
    validate() shall raise a ValueError mentioning the strip key.

    **Validates: Requirements 1.5, 10.8**
    """
    mutated = copy.deepcopy(content)

    # Inject strip key at various depths
    if depth == 0:
        # Top level
        mutated[strip_key] = "injected"
    elif depth == 1:
        # Inside preview
        mutated["preview"][strip_key] = "injected"
    elif depth == 2:
        # Inside a session
        mutated["learningSessions"][0][strip_key] = "injected"
    else:
        # Inside an activity's data
        mutated["learningSessions"][0]["activities"][0]["data"][strip_key] = "injected"

    with pytest.raises(ValueError, match=strip_key):
        validate(mutated)


# Feature: digital-economy-onboarding-curriculum, Property 3: vocabList format enforcement
@given(
    content=valid_content(),
    violation_type=sampled_from(["non_lowercase", "non_string", "words_field"]),
)
@settings(max_examples=100)
def test_vocab_list_format_enforcement(content, violation_type):
    """
    Property 3: vocabList must be an array of lowercase strings using the field name
    'vocabList'. Non-lowercase strings, non-string items, or field named 'words'
    shall cause validate() to raise ValueError.

    **Validates: Requirements 2.4, 10.5**
    """
    mutated = copy.deepcopy(content)

    if violation_type == "non_lowercase":
        # Inject an uppercase word into viewFlashcards vocabList
        mutated["learningSessions"][0]["activities"][1]["data"]["vocabList"][0] = "UPPERCASE"
    elif violation_type == "non_string":
        # Inject a non-string item into viewFlashcards vocabList
        mutated["learningSessions"][0]["activities"][1]["data"]["vocabList"][0] = 12345
    elif violation_type == "words_field":
        # Rename vocabList to words in the reading activity data
        reading_data = mutated["learningSessions"][0]["activities"][4]["data"]
        reading_data["words"] = reading_data.pop("vocabList")

    with pytest.raises(ValueError):
        validate(mutated)


# Feature: digital-economy-onboarding-curriculum, Property 4: Activity sequence enforcement
@given(
    content=valid_content(),
    mutation_type=sampled_from(["shuffle", "missing", "extra"]),
)
@settings(max_examples=100)
def test_activity_sequence_enforcement(content, mutation_type):
    """
    Property 4: If the activity sequence does not match EXPECTED_SEQUENCE
    (shuffled, missing, or extra activities), validate() shall raise ValueError.

    **Validates: Requirements 3.1, 10.2**
    """
    mutated = copy.deepcopy(content)
    activities = mutated["learningSessions"][0]["activities"]

    if mutation_type == "shuffle":
        # Swap two adjacent activities (ensure it actually changes the sequence)
        if len(activities) >= 2:
            # Swap index 1 and 2 (viewFlashcards and speakFlashcards)
            activities[1], activities[2] = activities[2], activities[1]
    elif mutation_type == "missing":
        # Remove one activity
        activities.pop(3)  # Remove vocabLevel1
    elif mutation_type == "extra":
        # Add a duplicate activity
        extra = copy.deepcopy(activities[0])
        activities.append(extra)

    with pytest.raises(ValueError):
        validate(mutated)


# Feature: digital-economy-onboarding-curriculum, Property 5: viewFlashcards/speakFlashcards vocabList consistency
@given(content=valid_content())
@settings(max_examples=100)
def test_flashcards_vocab_list_consistency(content):
    """
    Property 5: If viewFlashcards and speakFlashcards vocabLists differ,
    validate() shall raise ValueError.

    **Validates: Requirements 3.2, 10.6**
    """
    mutated = copy.deepcopy(content)

    # Modify speakFlashcards vocabList to differ from viewFlashcards
    speak_vocab = mutated["learningSessions"][0]["activities"][2]["data"]["vocabList"]
    # Reverse the list to make it different (guaranteed different since 5 unique words)
    speak_vocab.reverse()

    # Ensure it's actually different from viewFlashcards
    view_vocab = mutated["learningSessions"][0]["activities"][1]["data"]["vocabList"]
    assume(view_vocab != speak_vocab)

    with pytest.raises(ValueError, match="vocabList mismatch"):
        validate(mutated)


# Feature: digital-economy-onboarding-curriculum, Property 6: writingSentence structural completeness
@given(
    content=valid_content(),
    violation_type=sampled_from(["missing_vocabList", "missing_items", "item_no_prompt", "item_no_targetVocab"]),
)
@settings(max_examples=100)
def test_writing_sentence_structural_completeness(content, violation_type):
    """
    Property 6: writingSentence must have data.vocabList, data.items (non-empty),
    and each item must have prompt and targetVocab. Missing any of these shall
    cause validate() to raise ValueError.

    **Validates: Requirements 4.4, 10.7**
    """
    mutated = copy.deepcopy(content)

    # writingSentence is at index 7 in the activity sequence
    ws_data = mutated["learningSessions"][0]["activities"][7]["data"]

    if violation_type == "missing_vocabList":
        del ws_data["vocabList"]
    elif violation_type == "missing_items":
        del ws_data["items"]
    elif violation_type == "item_no_prompt":
        del ws_data["items"][0]["prompt"]
    elif violation_type == "item_no_targetVocab":
        del ws_data["items"][0]["targetVocab"]

    with pytest.raises(ValueError):
        validate(mutated)


# Feature: digital-economy-onboarding-curriculum, Property 7: contentTypeTags enforcement
@given(
    content=valid_content(),
    bad_value=one_of(
        just(["movie"]),
        just(["music"]),
        just(["podcast"]),
        just(["story"]),
        just(["movie", "music"]),
        just(None),
        just(""),
        just([""]),
    ),
)
@settings(max_examples=100)
def test_content_type_tags_enforcement(content, bad_value):
    """
    Property 7: contentTypeTags must be exactly []. Any other value
    shall cause validate() to raise ValueError.

    **Validates: Requirements 1.4, 10.9**
    """
    mutated = copy.deepcopy(content)
    mutated["contentTypeTags"] = bad_value

    with pytest.raises(ValueError):
        validate(mutated)
