"""
Property tests for Economics University Curriculum validators.

Tests Properties 1-4 from the design document:
  1. Curriculum structure validity
  2. Activity schema compliance
  3. VocabList integrity
  4. No vocabulary duplication within a series

Run: python economics-university-curriculum/test_properties.py
"""

import sys
import copy
import json

sys.path.insert(0, "economics-university-curriculum")
from validate_curriculum import (
    validate_session_structure,
    validate_activity_schema,
    validate_vocablist_integrity,
    STRIP_KEYS,
)

# ---------------------------------------------------------------------------
# Minimal valid curriculum fixture (18 words, 5 sessions, correct sequences)
# ---------------------------------------------------------------------------

W1 = ["supply", "demand", "equilibrium", "surplus", "shortage", "quantity"]
W2 = ["elasticity", "substitute", "complement", "shift", "curve", "price"]
W3 = ["allocate", "ration", "ceiling", "floor", "incentive", "scarcity"]
ALL_18 = W1 + W2 + W3


def _act(activity_type, vocab=None, extra_data=None):
    """Build a minimal valid activity dict."""
    data = {}
    if vocab is not None:
        data["vocabList"] = list(vocab)
    if activity_type == "reading" or activity_type == "speakReading" or activity_type == "readAlong":
        data["text"] = "Placeholder reading text."
    if activity_type == "introAudio":
        data["text"] = "Placeholder intro."
    if activity_type == "writingSentence":
        data["vocabList"] = list(vocab) if vocab else []
        data["items"] = [{"prompt": "Write a sentence.", "targetVocab": (vocab or ["word"])[0]}]
    if activity_type == "writingParagraph":
        data["vocabList"] = list(ALL_18)
        data["instructions"] = "Write a paragraph."
        data["prompts"] = ["Prompt 1", "Prompt 2"]
    if extra_data:
        data.update(extra_data)
    return {
        "activityType": activity_type,
        "title": f"Title for {activity_type}",
        "description": f"Desc for {activity_type}",
        "data": data,
    }


def _learning_session(vocab):
    return {
        "activities": [
            _act("introAudio"),
            _act("viewFlashcards", vocab),
            _act("speakFlashcards", vocab),
            _act("vocabLevel1", vocab),
            _act("vocabLevel2", vocab),
            _act("vocabLevel3", vocab),
            _act("reading"),
            _act("speakReading"),
            _act("readAlong"),
            _act("writingSentence", vocab),
        ]
    }


def _review_session():
    return {
        "activities": [
            _act("introAudio"),
            _act("viewFlashcards", ALL_18),
            _act("speakFlashcards", ALL_18),
            _act("vocabLevel1", ALL_18),
            _act("vocabLevel2", ALL_18),
            _act("vocabLevel3", ALL_18),
            _act("writingSentence", ALL_18),
        ]
    }


def _full_reading_session():
    return {
        "activities": [
            _act("introAudio"),
            _act("reading"),
            _act("speakReading"),
            _act("readAlong"),
            _act("writingParagraph"),
            _act("introAudio"),
        ]
    }


def build_valid_content():
    return {
        "title": "Supply & Demand – Cung va Cau",
        "contentTypeTags": [],
        "description": "Placeholder description.",
        "preview": {"text": "Placeholder preview."},
        "learningSessions": [
            _learning_session(W1),
            _learning_session(W2),
            _learning_session(W3),
            _review_session(),
            _full_reading_session(),
        ],
    }


# ---------------------------------------------------------------------------
# Test helpers
# ---------------------------------------------------------------------------

results = []


def run_test(name, fn):
    try:
        fn()
        results.append((name, True, None))
        print(f"  PASS  {name}")
    except Exception as e:
        results.append((name, False, str(e)))
        print(f"  FAIL  {name}: {e}")


def expect_raises(callable_fn, substr=None):
    """Assert that callable_fn raises ValueError (optionally containing substr)."""
    try:
        callable_fn()
    except ValueError as e:
        if substr and substr.lower() not in str(e).lower():
            raise AssertionError(f"ValueError raised but missing '{substr}': {e}")
        return
    raise AssertionError("Expected ValueError but none was raised")


class AssertionError(Exception):
    pass


# ===========================================================================
# Property 1: Curriculum structure validity
# Validates: Requirements 3.1, 3.2, 3.3, 3.4, 3.5
# ===========================================================================

print("\n--- Property 1: Curriculum structure validity ---")


def test_p1_valid():
    """Valid fixture passes validate_session_structure."""
    validate_session_structure(build_valid_content())


def test_p1_wrong_session_count():
    """Reject content with != 5 sessions."""
    c = build_valid_content()
    c["learningSessions"] = c["learningSessions"][:3]
    expect_raises(lambda: validate_session_structure(c), "5")


def test_p1_wrong_activity_order():
    """Reject session with shuffled activity order."""
    c = build_valid_content()
    acts = c["learningSessions"][0]["activities"]
    acts[1], acts[2] = acts[2], acts[1]  # swap viewFlashcards / speakFlashcards
    expect_raises(lambda: validate_session_structure(c), "sequence")


def test_p1_wrong_vocab_size():
    """Reject learning session with wrong vocabList size (not 6)."""
    c = build_valid_content()
    vf = c["learningSessions"][0]["activities"][1]  # viewFlashcards
    vf["data"]["vocabList"] = ["a", "b", "c"]  # only 3
    expect_raises(lambda: validate_session_structure(c), "6")


run_test("P1.1 valid fixture passes", test_p1_valid)
run_test("P1.2 wrong session count rejected", test_p1_wrong_session_count)
run_test("P1.3 wrong activity order rejected", test_p1_wrong_activity_order)
run_test("P1.4 wrong vocabList size rejected", test_p1_wrong_vocab_size)


# ===========================================================================
# Property 2: Activity schema compliance
# Validates: Requirements 12.1, 12.2, 12.5, 12.6, 12.7, 3.6
# ===========================================================================

print("\n--- Property 2: Activity schema compliance ---")


def test_p2_valid():
    """Every activity in the valid fixture passes validate_activity_schema."""
    c = build_valid_content()
    for session in c["learningSessions"]:
        for act in session["activities"]:
            validate_activity_schema(act)


def test_p2_type_instead_of_activityType():
    """Reject activity using 'type' instead of 'activityType'."""
    bad = {"type": "reading", "title": "T", "description": "D", "data": {"text": "x"}}
    expect_raises(lambda: validate_activity_schema(bad), "type")


def test_p2_missing_fields():
    """Reject activity missing required fields."""
    bad = {"activityType": "reading", "title": "T"}  # missing description, data
    expect_raises(lambda: validate_activity_schema(bad), "missing")


def test_p2_strip_keys():
    """Reject activity containing a strip key."""
    bad = _act("reading")
    bad["data"]["mp3Url"] = "http://example.com/audio.mp3"
    expect_raises(lambda: validate_activity_schema(bad), "strip key")


def test_p2_inline_data():
    """Reject activity with content data inline (not inside 'data')."""
    bad = _act("reading")
    bad["vocabList"] = ["word"]  # inline, should be in data
    expect_raises(lambda: validate_activity_schema(bad), "inline")


run_test("P2.1 valid activities pass", test_p2_valid)
run_test("P2.2 'type' instead of 'activityType' rejected", test_p2_type_instead_of_activityType)
run_test("P2.3 missing fields rejected", test_p2_missing_fields)
run_test("P2.4 strip keys rejected", test_p2_strip_keys)
run_test("P2.5 inline data rejected", test_p2_inline_data)


# ===========================================================================
# Property 3: VocabList integrity
# Validates: Requirements 12.3, 12.4
# ===========================================================================

print("\n--- Property 3: VocabList integrity ---")


def test_p3_valid():
    """Valid fixture passes validate_vocablist_integrity."""
    validate_vocablist_integrity(build_valid_content())


def test_p3_mismatched_flashcards():
    """Reject session where viewFlashcards != speakFlashcards vocabList."""
    c = build_valid_content()
    speak = c["learningSessions"][0]["activities"][2]  # speakFlashcards
    speak["data"]["vocabList"] = ["different", "words", "here", "now", "yes", "no"]
    expect_raises(lambda: validate_vocablist_integrity(c), "!=")


def test_p3_uppercase_words():
    """Reject vocabList with uppercase entries."""
    c = build_valid_content()
    # Set uppercase in BOTH flashcard activities so mismatch check passes first
    c["learningSessions"][0]["activities"][1]["data"]["vocabList"][0] = "Supply"
    c["learningSessions"][0]["activities"][2]["data"]["vocabList"][0] = "Supply"
    expect_raises(lambda: validate_vocablist_integrity(c), "lowercase")


def test_p3_words_field_name():
    """Reject activity using 'words' instead of 'vocabList'."""
    c = build_valid_content()
    vf = c["learningSessions"][0]["activities"][1]  # viewFlashcards
    vf["data"]["words"] = vf["data"].pop("vocabList")
    expect_raises(lambda: validate_vocablist_integrity(c), "words")


run_test("P3.1 valid fixture passes", test_p3_valid)
run_test("P3.2 mismatched flashcards rejected", test_p3_mismatched_flashcards)
run_test("P3.3 uppercase words rejected", test_p3_uppercase_words)
run_test("P3.4 'words' field name rejected", test_p3_words_field_name)


# ===========================================================================
# Property 4: No vocabulary duplication within a series
# Validates: Requirements 4.8
# ===========================================================================

print("\n--- Property 4: No vocabulary duplication within a series ---")


def collect_all_vocab(content):
    """Extract all unique vocab words from a curriculum content JSON."""
    words = set()
    for session in content.get("learningSessions", []):
        for act in session.get("activities", []):
            vl = act.get("data", {}).get("vocabList")
            if isinstance(vl, list):
                words.update(vl)
    return words


def check_no_series_duplicates(curriculum_contents):
    """
    Given a list of curriculum content dicts (one series = 5 curriculums),
    verify the union of all vocab words has no duplicates.
    Returns (ok: bool, duplicates: set).
    """
    seen = set()
    duplicates = set()
    for content in curriculum_contents:
        vocab = collect_all_vocab(content)
        overlap = seen & vocab
        duplicates.update(overlap)
        seen.update(vocab)
    return len(duplicates) == 0, duplicates


def test_p4_single_curriculum_no_dupes():
    """A single curriculum trivially has no series-level duplicates."""
    c = build_valid_content()
    ok, dupes = check_no_series_duplicates([c])
    assert ok, f"Unexpected duplicates: {dupes}"


def test_p4_deliberate_duplicate():
    """Detect duplicates when two curriculums share a word."""
    c1 = build_valid_content()
    c2 = build_valid_content()  # same words as c1 → all 18 are duplicated
    ok, dupes = check_no_series_duplicates([c1, c2])
    assert not ok, "Should have detected duplicates"
    assert len(dupes) == 18, f"Expected 18 duplicates, got {len(dupes)}"


run_test("P4.1 single curriculum — no dupes", test_p4_single_curriculum_no_dupes)
run_test("P4.2 deliberate duplicate detected", test_p4_deliberate_duplicate)


# ===========================================================================
# Summary
# ===========================================================================

print("\n--- Summary ---")
passed = sum(1 for _, ok, _ in results if ok)
failed = sum(1 for _, ok, _ in results if not ok)
print(f"{passed} passed, {failed} failed, {len(results)} total")

sys.exit(0 if failed == 0 else 1)
