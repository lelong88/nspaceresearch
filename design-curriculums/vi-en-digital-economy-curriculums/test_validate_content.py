"""
test_validate_content.py — Property-based tests for validate_content.py.

Each test is annotated with:
    # Feature: vi-en-digital-economy-curriculums, Property N: <text>

Generators are designed so `valid_curriculum(fmt, level)` always produces
content that passes `validate(content, fmt, level)`. Each property test
either asserts that the validator accepts a freshly generated valid
curriculum (positive case) or applies a minimal mutation that violates
exactly one rule and asserts the validator raises ValueError naming
that rule (negative case).

Design-time table tests (vocabulary distinctness, tone distribution,
title shape, etc.) live in a companion file `test_design_tables.py`
created by Task 1.3 — not here.
"""

from __future__ import annotations

import copy
import re
from typing import Any

import pytest
from hypothesis import HealthCheck, given, settings, strategies as st

from validate_content import (
    ACTIVITY_TEMPLATES,
    CONTENT_TYPE_TAGS,
    STRIP_KEYS,
    VALID_ACTIVITY_TYPES,
    validate,
)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SETTINGS = settings(
    max_examples=100,
    deadline=None,
    suppress_health_check=[HealthCheck.too_slow, HealthCheck.data_too_large],
)

FORMATS = ("story_reading", "speaking", "balanced")
LEVELS = ("preintermediate", "intermediate")

# Per-level target words/sentence used by the default valid_curriculum
# generator — chosen to land in the middle of each level's bounds.
_LEVEL_TARGET_AVG = {
    "preintermediate": 12,   # bounds 10-14
    "intermediate": 15,      # bounds 12-18
}

# ---------------------------------------------------------------------------
# Primitive Hypothesis strategies
# ---------------------------------------------------------------------------

_LOWERCASE_WORD = st.text(
    alphabet="abcdefghijklmnopqrstuvwxyz", min_size=3, max_size=12
)


def random_format() -> st.SearchStrategy[str]:
    """Strategy: one of the three valid formats."""
    return st.sampled_from(FORMATS)


def random_level() -> st.SearchStrategy[str]:
    """Strategy: one of the two valid levels."""
    return st.sampled_from(LEVELS)


def random_strip_key() -> st.SearchStrategy[str]:
    """Strategy: a random element of STRIP_KEYS."""
    return st.sampled_from(sorted(STRIP_KEYS))


def random_vocab_list(n: int) -> st.SearchStrategy[list[str]]:
    """Strategy: a list of n unique lowercase ASCII strings, length 3-12."""
    return st.lists(_LOWERCASE_WORD, min_size=n, max_size=n, unique=True)


def random_json_path() -> st.SearchStrategy[int]:
    """Strategy: an opaque integer used to index into the dicts of a content tree.

    Tests use this together with `_collect_dicts(content)` and modulo
    indexing — the absolute index doesn't matter, only that it lands on
    *some* reachable dict.
    """
    return st.integers(min_value=0, max_value=10_000)


# ---------------------------------------------------------------------------
# Controlled-shape generators
# ---------------------------------------------------------------------------

def controlled_passage(target_avg_sentence_length: int, n_sentences: int) -> str:
    """A deterministic English passage with controlled average sentence length.

    Each sentence is `target_avg_sentence_length` whitespace-separated tokens
    ending with a single period. Total tokens = N * target_avg, total
    sentence-terminators = N, so average = target_avg exactly.
    """
    if target_avg_sentence_length < 1:
        raise ValueError("target_avg_sentence_length must be >= 1")
    if n_sentences < 1:
        raise ValueError("n_sentences must be >= 1")

    sentence = " ".join(["alpha"] * (target_avg_sentence_length - 1) + ["alpha."])
    return " ".join([sentence] * n_sentences)


def controlled_intro_audio(word_count: int) -> str:
    """Bilingual-shaped introAudio text with exactly `word_count` whitespace tokens."""
    if word_count < 1:
        raise ValueError("word_count must be >= 1")
    return " ".join(["lorem"] * word_count)


# ---------------------------------------------------------------------------
# Activity builders
# ---------------------------------------------------------------------------

def _flashcard_description(vocab: list[str]) -> str:
    return f"Học {len(vocab)} từ: " + ", ".join(vocab)


def _make_intro_audio(token_count: int) -> dict:
    return {
        "activityType": "introAudio",
        "title": "Giới thiệu bài học",
        "description": "Đoạn giới thiệu bài học bằng tiếng Việt và tiếng Anh.",
        "data": {"text": controlled_intro_audio(token_count)},
    }


def _make_session_vocab_activity(
    activity_type: str, session_vocab: list[str]
) -> dict:
    """viewFlashcards / speakFlashcards / vocabLevel1 share session vocab."""
    return {
        "activityType": activity_type,
        "title": "Flashcards: từ vựng kinh tế số",
        "description": _flashcard_description(session_vocab),
        "data": {"vocabList": list(session_vocab)},
    }


def _make_review_vocab_activity(
    activity_type: str, all_vocab: list[str]
) -> dict:
    """vocabLevel2 / vocabLevel3 review the full curriculum vocab."""
    return {
        "activityType": activity_type,
        "title": "Flashcards: ôn tập tổng hợp",
        "description": _flashcard_description(all_vocab),
        "data": {"vocabList": list(all_vocab)},
    }


def _make_reading(
    activity_type: str, target_avg: int, n_sentences: int
) -> dict:
    text = controlled_passage(target_avg, n_sentences)
    return {
        "activityType": activity_type,
        "title": "Đọc: chủ đề kinh tế số",
        "description": text[:80],
        "data": {"text": text},
    }


def _make_read_along(target_avg: int, n_sentences: int) -> dict:
    return {
        "activityType": "readAlong",
        "title": "Nghe: chủ đề kinh tế số",
        "description": "Nghe đoạn văn vừa đọc và theo dõi.",
        "data": {"text": controlled_passage(target_avg, n_sentences)},
    }


def _make_writing_sentence(session_vocab: list[str]) -> dict:
    items = [
        {"prompt": f"Use {w} in a sentence.", "targetVocab": w}
        for w in session_vocab[:3]
    ]
    return {
        "activityType": "writingSentence",
        "title": "Viết: câu với từ vựng đã học",
        "description": "Hoàn thành các câu bằng tiếng Anh dùng từ vựng đã học.",
        "data": {"vocabList": list(session_vocab), "items": items},
    }


def _make_writing_paragraph(all_vocab: list[str]) -> dict:
    return {
        "activityType": "writingParagraph",
        "title": "Viết: đoạn văn tổng hợp",
        "description": "Viết đoạn văn ngắn bằng tiếng Anh dùng từ vựng đã học.",
        "data": {
            "vocabList": list(all_vocab),
            "instructions": "Hãy viết đoạn văn 5-7 câu sử dụng các từ vựng dưới đây.",
            "prompts": [
                f"Describe how {all_vocab[0]} matters today.",
                f"Discuss why {all_vocab[1]} is changing the economy.",
            ],
        },
    }


def random_activity(activity_type: str) -> st.SearchStrategy[dict]:
    """Strategy: a valid activity object of the given type."""
    if activity_type not in VALID_ACTIVITY_TYPES:
        raise ValueError(f"unknown activity type: {activity_type}")

    @st.composite
    def _gen(draw):
        if activity_type in {"viewFlashcards", "speakFlashcards", "vocabLevel1"}:
            vocab = draw(random_vocab_list(5))
            return _make_session_vocab_activity(activity_type, vocab)
        if activity_type in {"vocabLevel2", "vocabLevel3"}:
            vocab = draw(random_vocab_list(20))
            return _make_review_vocab_activity(activity_type, vocab)
        if activity_type in {"reading", "speakReading"}:
            target_avg = draw(st.integers(min_value=10, max_value=14))
            n_sent = draw(st.integers(min_value=4, max_value=8))
            return _make_reading(activity_type, target_avg, n_sent)
        if activity_type == "readAlong":
            target_avg = draw(st.integers(min_value=10, max_value=14))
            n_sent = draw(st.integers(min_value=2, max_value=5))
            return _make_read_along(target_avg, n_sent)
        if activity_type == "introAudio":
            tokens = draw(st.integers(min_value=200, max_value=400))
            return _make_intro_audio(tokens)
        if activity_type == "writingSentence":
            vocab = draw(random_vocab_list(5))
            return _make_writing_sentence(vocab)
        if activity_type == "writingParagraph":
            vocab = draw(random_vocab_list(20))
            return _make_writing_paragraph(vocab)
        raise AssertionError(f"unhandled activity type: {activity_type}")

    return _gen()


# ---------------------------------------------------------------------------
# valid_curriculum strategy
# ---------------------------------------------------------------------------

def _intro_audio_role(
    session_idx: int, intro_indices: list[int], position: int
) -> str:
    """Determine the role of an introAudio at `position` in session `session_idx`.

    Mirrors the validator's role assignment:
      - welcome: first introAudio of session 1 (index 0)
      - farewell: last introAudio of session 4 (index 3)
      - mid: every other introAudio
    """
    is_first = position == intro_indices[0]
    is_last = position == intro_indices[-1]
    if session_idx == 0 and is_first:
        return "welcome"
    if session_idx == 3 and is_last:
        return "farewell"
    return "mid"


def _intro_audio_token_count(role: str) -> int:
    """Pick a safely in-bounds token count for the given role."""
    if role == "welcome":
        return 650  # within 500-800
    if role == "farewell":
        return 500  # within 400-600
    return 300      # within 200-400


def _build_session_activities(
    fmt: str,
    session_idx: int,
    session_vocab: list[str],
    all_vocab: list[str],
    target_avg: int,
) -> list[dict]:
    template = ACTIVITY_TEMPLATES[fmt][session_idx]
    intro_indices = [k for k, t in enumerate(template) if t == "introAudio"]

    activities: list[dict] = []
    for j, at in enumerate(template):
        if at == "introAudio":
            role = _intro_audio_role(session_idx, intro_indices, j)
            tokens = _intro_audio_token_count(role)
            activities.append(_make_intro_audio(tokens))
        elif at in {"viewFlashcards", "speakFlashcards", "vocabLevel1"}:
            activities.append(_make_session_vocab_activity(at, session_vocab))
        elif at in {"vocabLevel2", "vocabLevel3"}:
            activities.append(_make_review_vocab_activity(at, all_vocab))
        elif at in {"reading", "speakReading"}:
            activities.append(_make_reading(at, target_avg, n_sentences=6))
        elif at == "readAlong":
            activities.append(_make_read_along(target_avg, n_sentences=3))
        elif at == "writingSentence":
            activities.append(_make_writing_sentence(session_vocab))
        elif at == "writingParagraph":
            activities.append(_make_writing_paragraph(all_vocab))
        else:
            raise AssertionError(f"unhandled activity type in template: {at}")

    return activities


def valid_curriculum(
    fmt: str,
    level: str | None = None,
    target_avg: int | None = None,
) -> st.SearchStrategy[dict]:
    """Strategy: a structurally valid curriculum content dict.

    Always passes validate(content, fmt, level) when called with the same
    fmt and level (provided target_avg matches the level's bounds, which
    is the default).
    """
    if fmt not in FORMATS:
        raise ValueError(f"bad fmt: {fmt}")

    effective_avg = (
        target_avg
        if target_avg is not None
        else _LEVEL_TARGET_AVG.get(level, 12)
    )

    @st.composite
    def _gen(draw):
        all_vocab = draw(random_vocab_list(20))
        sessions_vocab = [all_vocab[i * 5 : (i + 1) * 5] for i in range(4)]

        sessions: list[dict] = []
        for i in range(4):
            sessions.append(
                {
                    "title": f"Buổi {i + 1}: chủ đề {i + 1}",
                    "activities": _build_session_activities(
                        fmt, i, sessions_vocab[i], all_vocab, effective_avg
                    ),
                }
            )

        return {
            "title": "Khoá học thử nghiệm Kinh Tế Số",
            "description": "Mô tả khoá học thử nghiệm dùng cho property-based testing.",
            "preview": {"text": "Đây là đoạn xem trước cho khoá học thử nghiệm."},
            "contentTypeTags": list(CONTENT_TYPE_TAGS[fmt]),
            "learningSessions": sessions,
        }

    return _gen()


# ---------------------------------------------------------------------------
# Helpers used by mutation-based negative tests
# ---------------------------------------------------------------------------

def _collect_dicts(obj: Any, acc: list[dict] | None = None) -> list[dict]:
    if acc is None:
        acc = []
    if isinstance(obj, dict):
        acc.append(obj)
        for v in obj.values():
            _collect_dicts(v, acc)
    elif isinstance(obj, list):
        for item in obj:
            _collect_dicts(item, acc)
    return acc


# ===========================================================================
# Property tests
# ===========================================================================

# Feature: vi-en-digital-economy-curriculums,
# Property 1: Valid content passes validation
# Validates: Requirements 1.4, 1.5, 1.6, 3.1, 3.2, 3.3, 3.4, 5.1,
#            9.1-9.9, 10.1-10.13
@SETTINGS
@given(fmt=random_format(), level=st.one_of(st.none(), random_level()), data=st.data())
def test_property_1_valid_content_passes_validation(fmt, level, data):
    content = data.draw(valid_curriculum(fmt, level))
    # Should not raise.
    validate(content, fmt, level)


# Feature: vi-en-digital-economy-curriculums,
# Property 2: contentTypeTags must match the declared format
# Validates: Requirements 1.5, 1.6, 10.12
@SETTINGS
@given(fmt=random_format(), level=random_level(), data=st.data())
def test_property_2_content_type_tags_match_format(fmt, level, data):
    content = data.draw(valid_curriculum(fmt, level))
    # Pick any other format whose tags differ from this one — guaranteed mismatch.
    wrong_fmt = next(
        f for f in FORMATS if CONTENT_TYPE_TAGS[f] != CONTENT_TYPE_TAGS[fmt]
    )
    bad = copy.deepcopy(content)
    bad["contentTypeTags"] = list(CONTENT_TYPE_TAGS[wrong_fmt])
    with pytest.raises(ValueError, match=r"contentTypeTags"):
        validate(bad, fmt, level)


# Feature: vi-en-digital-economy-curriculums,
# Property 3: Strip keys are rejected anywhere in the JSON tree
# Validates: Requirements 1.7, 10.11
@SETTINGS
@given(
    fmt=random_format(),
    level=random_level(),
    strip_key=random_strip_key(),
    path_index=random_json_path(),
    data=st.data(),
)
def test_property_3_strip_keys_rejected_at_any_path(
    fmt, level, strip_key, path_index, data
):
    content = data.draw(valid_curriculum(fmt, level))
    dicts = _collect_dicts(content)
    target = dicts[path_index % len(dicts)]
    target[strip_key] = "injected-value"
    with pytest.raises(ValueError, match=re.escape(strip_key)):
        validate(content, fmt, level)


# Feature: vi-en-digital-economy-curriculums,
# Property 4: Activity sequence must match the format template
# Validates: Requirements 3.1, 3.2, 3.3, 3.7, 3.8, 10.2
@SETTINGS
@given(
    fmt=random_format(),
    level=random_level(),
    session_idx=st.integers(0, 3),
    data=st.data(),
)
def test_property_4_activity_sequence_must_match_template(
    fmt, level, session_idx, data
):
    content = data.draw(valid_curriculum(fmt, level))
    bad = copy.deepcopy(content)
    # Drop the last activity of the session — the template length will
    # differ, guaranteed to mismatch.
    bad["learningSessions"][session_idx]["activities"].pop()
    with pytest.raises(ValueError, match=r"activity sequence"):
        validate(bad, fmt, level)


# Feature: vi-en-digital-economy-curriculums,
# Property 5: Curriculum must have exactly 4 sessions, each well-shaped
# Validates: Requirements 3.4, 9.9, 10.2
@SETTINGS
@given(
    fmt=random_format(),
    level=random_level(),
    violation=st.sampled_from(
        ("missing", "wrong_length", "empty_title", "duplicate_titles", "empty_activities")
    ),
    data=st.data(),
)
def test_property_5_exactly_four_sessions_well_shaped(fmt, level, violation, data):
    content = data.draw(valid_curriculum(fmt, level))
    bad = copy.deepcopy(content)

    if violation == "missing":
        del bad["learningSessions"]
        pattern = r"learningSessions"
    elif violation == "wrong_length":
        bad["learningSessions"].pop()  # 3 sessions
        pattern = r"4 sessions"
    elif violation == "empty_title":
        bad["learningSessions"][0]["title"] = ""
        pattern = r"session\.title"
    elif violation == "duplicate_titles":
        bad["learningSessions"][1]["title"] = bad["learningSessions"][0]["title"]
        pattern = r"unique"
    elif violation == "empty_activities":
        bad["learningSessions"][0]["activities"] = []
        pattern = r"activities"
    else:
        raise AssertionError(violation)

    with pytest.raises(ValueError, match=pattern):
        validate(bad, fmt, level)


# Feature: vi-en-digital-economy-curriculums,
# Property 6: Session_Vocab_Group structure (5 per session, 20 unique total)
# Validates: Requirements 3.5, 5.1, 10.7, 10.8
@SETTINGS
@given(
    fmt=random_format(),
    level=random_level(),
    violation=st.sampled_from(("duplicate_within", "duplicate_across")),
    data=st.data(),
)
def test_property_6_session_vocab_groups_well_formed(fmt, level, violation, data):
    content = data.draw(valid_curriculum(fmt, level))
    bad = copy.deepcopy(content)

    def _set_session_vocab(session_idx: int, new_vocab: list[str]) -> None:
        for activity in bad["learningSessions"][session_idx]["activities"]:
            if activity["activityType"] in {
                "viewFlashcards", "speakFlashcards", "vocabLevel1"
            }:
                activity["data"]["vocabList"] = list(new_vocab)
                activity["description"] = _flashcard_description(new_vocab)

    if violation == "duplicate_within":
        session_0 = bad["learningSessions"][0]["activities"]
        current = next(
            a["data"]["vocabList"]
            for a in session_0
            if a["activityType"] == "viewFlashcards"
        )
        # Duplicate the first word in place of the last → only 4 unique entries.
        new_vocab = list(current[:-1]) + [current[0]]
        _set_session_vocab(0, new_vocab)
        pattern = r"5 unique"
    elif violation == "duplicate_across":
        # Copy session 0's vocab into session 1 → union has < 20 unique.
        session_0_vocab = next(
            a["data"]["vocabList"]
            for a in bad["learningSessions"][0]["activities"]
            if a["activityType"] == "viewFlashcards"
        )
        _set_session_vocab(1, list(session_0_vocab))
        pattern = r"20 unique"
    else:
        raise AssertionError(violation)

    with pytest.raises(ValueError, match=pattern):
        validate(bad, fmt, level)


# Feature: vi-en-digital-economy-curriculums,
# Property 7: Activity structural shape
# Validates: Requirements 9.1, 9.2, 9.5, 10.3, 10.4
@SETTINGS
@given(
    fmt=random_format(),
    level=random_level(),
    violation=st.sampled_from(
        ("rename_to_type", "invalid_activityType", "data_not_dict", "missing_title")
    ),
    data=st.data(),
)
def test_property_7_activity_shape_violations_raise(fmt, level, violation, data):
    content = data.draw(valid_curriculum(fmt, level))
    bad = copy.deepcopy(content)
    target = bad["learningSessions"][0]["activities"][0]

    if violation == "rename_to_type":
        target["type"] = target["activityType"]
        pattern = r"activityType"
    elif violation == "invalid_activityType":
        target["activityType"] = "notARealType"
        pattern = r"activityType"
    elif violation == "data_not_dict":
        target["data"] = "this is not a dict"
        pattern = r"data must be a dict"
    elif violation == "missing_title":
        target["title"] = ""
        pattern = r"title"
    else:
        raise AssertionError(violation)

    with pytest.raises(ValueError, match=pattern):
        validate(bad, fmt, level)


# Feature: vi-en-digital-economy-curriculums,
# Property 8: vocabList format
# Validates: Requirements 5.5, 9.3, 10.5
@SETTINGS
@given(
    fmt=random_format(),
    level=random_level(),
    violation=st.sampled_from(
        ("uppercase_word", "renamed_words", "non_string_item", "empty_list")
    ),
    data=st.data(),
)
def test_property_8_vocab_list_format(fmt, level, violation, data):
    content = data.draw(valid_curriculum(fmt, level))
    bad = copy.deepcopy(content)
    # Mutate the SAME field on every session-vocab activity in session 0
    # so the consistency check (Property 9) does not pre-empt this one.
    siblings = [
        a for a in bad["learningSessions"][0]["activities"]
        if a["activityType"] in {"viewFlashcards", "speakFlashcards", "vocabLevel1"}
    ]

    if violation == "uppercase_word":
        # Uppercase the first word everywhere AND keep the description in sync
        # so the convention check (which runs before the vocabList check) does
        # not pre-empt the lowercase rule we are testing.
        for a in siblings:
            vlist = a["data"]["vocabList"]
            vlist[0] = vlist[0].upper()
            a["description"] = _flashcard_description(vlist)
        pattern = r"lowercase"
    elif violation == "renamed_words":
        # Move vocabList → words AND update description so the convention check
        # (which uses data.get("vocabList", [])) passes — this lets the actual
        # vocabList-shape check fire.
        for a in siblings:
            a["data"]["words"] = a["data"].pop("vocabList")
            a["description"] = _flashcard_description([])
        pattern = r"vocabList"
    elif violation == "non_string_item":
        # Replace one item with an int. The description-convention check skips
        # when the list contains non-strings, so the vocabList shape check fires.
        for a in siblings:
            a["data"]["vocabList"][0] = 42
        pattern = r"vocabList"
    elif violation == "empty_list":
        # Empty the list AND the description so the convention check accepts
        # it (its expected becomes "Học 0 từ: ") and the length check fires.
        for a in siblings:
            a["data"]["vocabList"] = []
            a["description"] = _flashcard_description([])
        pattern = r"vocabList"
    else:
        raise AssertionError(violation)

    with pytest.raises(ValueError, match=pattern):
        validate(bad, fmt, level)


# Feature: vi-en-digital-economy-curriculums,
# Property 9: Flashcard / vocabLevel vocabList consistency within a session
# Validates: Requirements 9.4, 10.6
@SETTINGS
@given(fmt=random_format(), level=random_level(), data=st.data())
def test_property_9_session_vocab_list_consistency(fmt, level, data):
    content = data.draw(valid_curriculum(fmt, level))
    bad = copy.deepcopy(content)
    # Mutate ONLY the speakFlashcards in session 0, leaving viewFlashcards alone
    # → the two no longer share a vocabList.
    speak = next(
        a for a in bad["learningSessions"][0]["activities"]
        if a["activityType"] == "speakFlashcards"
    )
    permuted = list(reversed(speak["data"]["vocabList"]))
    speak["data"]["vocabList"] = permuted
    speak["description"] = _flashcard_description(permuted)

    with pytest.raises(ValueError, match=r"vocabList mismatch"):
        validate(bad, fmt, level)


# Feature: vi-en-digital-economy-curriculums,
# Property 10: writingSentence shape
# Validates: Requirements 9.6, 10.9
@SETTINGS
@given(
    fmt=random_format(),
    level=random_level(),
    violation=st.sampled_from(
        ("empty_items", "target_not_in_vocab", "missing_prompt")
    ),
    data=st.data(),
)
def test_property_10_writing_sentence_shape(fmt, level, violation, data):
    content = data.draw(valid_curriculum(fmt, level))
    bad = copy.deepcopy(content)
    # writingSentence is always present in the final session for every fmt.
    ws = next(
        a for s in bad["learningSessions"] for a in s["activities"]
        if a["activityType"] == "writingSentence"
    )

    if violation == "empty_items":
        ws["data"]["items"] = []
        pattern = r"items"
    elif violation == "target_not_in_vocab":
        ws["data"]["items"][0]["targetVocab"] = "zzznotaword"
        pattern = r"targetVocab"
    elif violation == "missing_prompt":
        ws["data"]["items"][0]["prompt"] = ""
        pattern = r"prompt"
    else:
        raise AssertionError(violation)

    with pytest.raises(ValueError, match=pattern):
        validate(bad, fmt, level)


# Feature: vi-en-digital-economy-curriculums,
# Property 11: writingParagraph shape
# Validates: Requirements 9.7, 10.10
@SETTINGS
@given(
    level=random_level(),
    violation=st.sampled_from(("too_few_prompts", "empty_instructions")),
    data=st.data(),
)
def test_property_11_writing_paragraph_shape_negative(level, violation, data):
    """writingParagraph shape rules. Only `balanced` final session has it."""
    fmt = "balanced"
    content = data.draw(valid_curriculum(fmt, level))
    bad = copy.deepcopy(content)
    wp = next(
        a for s in bad["learningSessions"] for a in s["activities"]
        if a["activityType"] == "writingParagraph"
    )
    if violation == "too_few_prompts":
        wp["data"]["prompts"] = wp["data"]["prompts"][:1]
        pattern = r"prompts"
    elif violation == "empty_instructions":
        wp["data"]["instructions"] = ""
        pattern = r"instructions"
    else:
        raise AssertionError(violation)

    with pytest.raises(ValueError, match=pattern):
        validate(bad, fmt, level)


@SETTINGS
@given(level=random_level(), data=st.data())
def test_property_11_writing_paragraph_valid_passes(level, data):
    """Positive case: a valid balanced curriculum (which contains a writingParagraph)
    must pass validation."""
    fmt = "balanced"
    content = data.draw(valid_curriculum(fmt, level))
    validate(content, fmt, level)


# Feature: vi-en-digital-economy-curriculums,
# Property 12: Reading passage average sentence length matches level
# Validates: Requirement 2.4
@SETTINGS
@given(level=random_level(), fmt=random_format(), data=st.data())
def test_property_12_avg_sentence_length_in_bounds_passes(level, fmt, data):
    """A controlled-passage curriculum at the level's center target must pass."""
    content = data.draw(valid_curriculum(fmt, level))
    validate(content, fmt, level)


@SETTINGS
@given(level=random_level(), fmt=random_format(), data=st.data())
def test_property_12_avg_sentence_length_too_short_raises(level, fmt, data):
    """An average below the level's lower bound must raise."""
    # preintermediate floor 10 → use 8; intermediate floor 12 → use 9.
    target = 8 if level == "preintermediate" else 9
    content = data.draw(valid_curriculum(fmt, level, target_avg=target))
    with pytest.raises(ValueError, match=r"average sentence length"):
        validate(content, fmt, level)


@SETTINGS
@given(level=random_level(), fmt=random_format(), data=st.data())
def test_property_12_avg_sentence_length_too_long_raises(level, fmt, data):
    """An average above the level's upper bound must raise."""
    # preintermediate cap 14 → use 20; intermediate cap 18 → use 22.
    target = 20 if level == "preintermediate" else 22
    content = data.draw(valid_curriculum(fmt, level, target_avg=target))
    with pytest.raises(ValueError, match=r"average sentence length"):
        validate(content, fmt, level)


# Feature: vi-en-digital-economy-curriculums,
# Property 13: introAudio word counts match script role
# Validates: Requirements 8.1, 8.3, 8.4
@SETTINGS
@given(
    fmt=random_format(),
    level=random_level(),
    role=st.sampled_from(("welcome", "farewell", "mid")),
    direction=st.sampled_from(("too_short", "too_long")),
    data=st.data(),
)
def test_property_13_intro_audio_word_counts(fmt, level, role, direction, data):
    """Mutating any introAudio's text outside its role-specific bounds must raise."""
    content = data.draw(valid_curriculum(fmt, level))
    bad = copy.deepcopy(content)

    if role == "welcome":
        intros = [
            a for a in bad["learningSessions"][0]["activities"]
            if a["activityType"] == "introAudio"
        ]
        target = intros[0]
        lo, hi = 500, 800
    elif role == "farewell":
        intros = [
            a for a in bad["learningSessions"][3]["activities"]
            if a["activityType"] == "introAudio"
        ]
        target = intros[-1]
        lo, hi = 400, 600
    else:  # mid
        # last introAudio of session 1 is always a mid session-1 wrap-up.
        intros = [
            a for a in bad["learningSessions"][0]["activities"]
            if a["activityType"] == "introAudio"
        ]
        target = intros[-1] if len(intros) >= 2 else intros[0]
        lo, hi = 200, 400

    new_count = max(1, lo - 50) if direction == "too_short" else hi + 50
    target["data"]["text"] = controlled_intro_audio(new_count)

    with pytest.raises(ValueError, match=r"introAudio word count"):
        validate(bad, fmt, level)


# Feature: vi-en-digital-economy-curriculums,
# Property 14: Activity title/description conventions
# Validates: Requirement 9.8
@SETTINGS
@given(
    fmt=random_format(),
    level=random_level(),
    violation=st.sampled_from(
        (
            "flashcard_title_no_prefix",
            "reading_desc_not_first_80",
            "read_along_wrong_desc",
            "intro_title_too_short",
            "writing_title_no_prefix",
        )
    ),
    data=st.data(),
)
def test_property_14_title_description_conventions(fmt, level, violation, data):
    content = data.draw(valid_curriculum(fmt, level))
    bad = copy.deepcopy(content)

    if violation == "flashcard_title_no_prefix":
        target = next(
            a for a in bad["learningSessions"][0]["activities"]
            if a["activityType"] == "viewFlashcards"
        )
        target["title"] = "Bài học từ vựng"  # missing "Flashcards: " prefix
        pattern = r"Flashcards"
    elif violation == "reading_desc_not_first_80":
        target = next(
            a for s in bad["learningSessions"] for a in s["activities"]
            if a["activityType"] == "reading"
        )
        target["description"] = "Mô tả không khớp với data.text."
        pattern = r"first 80"
    elif violation == "read_along_wrong_desc":
        target = next(
            a for s in bad["learningSessions"] for a in s["activities"]
            if a["activityType"] == "readAlong"
        )
        target["description"] = "Mô tả khác với chuẩn quy định cho readAlong."
        pattern = r"readAlong"
    elif violation == "intro_title_too_short":
        target = next(
            a for s in bad["learningSessions"] for a in s["activities"]
            if a["activityType"] == "introAudio"
        )
        target["title"] = "Hi"  # 2 chars, below 5-char floor
        pattern = r"introAudio\.title"
    elif violation == "writing_title_no_prefix":
        target = next(
            a for s in bad["learningSessions"] for a in s["activities"]
            if a["activityType"] == "writingSentence"
        )
        target["title"] = "Bài tập viết"  # missing "Viết: " prefix
        pattern = r"Viết"
    else:
        raise AssertionError(violation)

    with pytest.raises(ValueError, match=pattern):
        validate(bad, fmt, level)


# Feature: vi-en-digital-economy-curriculums,
# Property 15: Top-level structural fields
# Validates: Requirements 10.1, 10.13
@SETTINGS
@given(
    fmt=random_format(),
    level=random_level(),
    violation=st.sampled_from(
        (
            "missing_title",
            "empty_title",
            "title_not_string",
            "missing_description",
            "empty_description",
            "missing_preview_text",
            "preview_not_dict",
        )
    ),
    data=st.data(),
)
def test_property_15_top_level_fields(fmt, level, violation, data):
    content = data.draw(valid_curriculum(fmt, level))
    bad = copy.deepcopy(content)

    if violation == "missing_title":
        del bad["title"]
        pattern = r"title"
    elif violation == "empty_title":
        bad["title"] = ""
        pattern = r"title"
    elif violation == "title_not_string":
        bad["title"] = 12345
        pattern = r"title"
    elif violation == "missing_description":
        del bad["description"]
        pattern = r"description"
    elif violation == "empty_description":
        bad["description"] = ""
        pattern = r"description"
    elif violation == "missing_preview_text":
        del bad["preview"]["text"]
        pattern = r"preview\.text"
    elif violation == "preview_not_dict":
        bad["preview"] = "not a dict"
        pattern = r"preview"
    else:
        raise AssertionError(violation)

    with pytest.raises(ValueError, match=pattern):
        validate(bad, fmt, level)
