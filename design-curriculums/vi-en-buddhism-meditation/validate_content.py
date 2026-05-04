"""
validate_content.py — Content validation for vi-en Buddhism/meditation curriculums.

Validates curriculum content JSON against structural rules and activity sequence
templates for three skill focus formats: story_reading, speaking, balanced.

Usage:
    from validate_content import validate
    validate(content, "story_reading")
    validate(content, "speaking")
    validate(content, "balanced")
"""

VALID_FORMATS = {"story_reading", "speaking", "balanced"}

VALID_ACTIVITY_TYPES = {
    "introAudio",
    "viewFlashcards",
    "speakFlashcards",
    "vocabLevel1",
    "vocabLevel2",
    "reading",
    "speakReading",
    "readAlong",
    "writingSentence",
    "writingParagraph",
}

VOCAB_ACTIVITY_TYPES = {
    "viewFlashcards",
    "speakFlashcards",
    "vocabLevel1",
    "vocabLevel2",
}

STRIP_KEYS = {
    "mp3Url",
    "illustrationSet",
    "chapterBookmarks",
    "segments",
    "whiteboardItems",
    "userReadingId",
    "lessonUniqueId",
    "curriculumTags",
    "taskId",
    "imageId",
}

WRITING_ACTIVITY_TYPES = {"writingSentence", "writingParagraph"}

# Activity sequence templates per format (0-indexed sessions)
ACTIVITY_SEQUENCES = {
    "story_reading": {
        0: ["introAudio", "viewFlashcards", "speakFlashcards", "reading", "speakReading", "readAlong", "introAudio"],
        1: ["introAudio", "viewFlashcards", "speakFlashcards", "reading", "speakReading", "readAlong", "introAudio"],
        2: ["introAudio", "viewFlashcards", "speakFlashcards", "vocabLevel1", "reading", "speakReading", "readAlong", "introAudio"],
        3: ["introAudio", "reading", "speakReading", "readAlong", "writingSentence", "introAudio"],
    },
    "speaking": {
        0: ["introAudio", "viewFlashcards", "speakFlashcards", "vocabLevel1", "speakFlashcards", "reading", "speakReading", "introAudio"],
        1: ["introAudio", "viewFlashcards", "speakFlashcards", "vocabLevel1", "speakFlashcards", "reading", "speakReading", "introAudio"],
        2: ["introAudio", "speakFlashcards", "vocabLevel1", "vocabLevel2", "speakFlashcards", "reading", "speakReading", "introAudio"],
        3: ["introAudio", "speakFlashcards", "vocabLevel2", "reading", "speakReading", "readAlong", "writingSentence", "introAudio"],
    },
    "balanced": {
        0: ["introAudio", "viewFlashcards", "speakFlashcards", "vocabLevel1", "reading", "speakReading", "readAlong", "introAudio"],
        1: ["introAudio", "viewFlashcards", "speakFlashcards", "vocabLevel1", "reading", "speakReading", "readAlong", "introAudio"],
        2: ["introAudio", "viewFlashcards", "speakFlashcards", "vocabLevel1", "vocabLevel2", "reading", "speakReading", "readAlong", "writingSentence", "introAudio"],
        3: ["introAudio", "reading", "speakReading", "readAlong", "writingSentence", "writingParagraph", "introAudio"],
    },
}

# contentTypeTags expected per format
CONTENT_TYPE_TAGS = {
    "story_reading": ["story"],
    "speaking": [],
    "balanced": [],
}


def _check_strip_keys(obj, path="content"):
    """Recursively check that no strip-keys appear anywhere in the JSON tree."""
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key in STRIP_KEYS:
                raise ValueError(
                    f"Strip-key '{key}' found at {path}.{key} — "
                    f"auto-generated keys must never be included in new content"
                )
            _check_strip_keys(value, f"{path}.{key}")
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            _check_strip_keys(item, f"{path}[{i}]")


def _validate_top_level(content):
    """Check top-level structure: title, description, preview.text, contentTypeTags, learningSessions."""
    if not isinstance(content, dict):
        raise ValueError("Content must be a JSON object (dict)")

    for field in ("title", "description"):
        val = content.get(field)
        if not val or not isinstance(val, str) or not val.strip():
            raise ValueError(f"Top-level '{field}' must be a non-null, non-empty string")

    # preview.text
    preview = content.get("preview")
    if not isinstance(preview, dict):
        raise ValueError("Top-level 'preview' must be an object with a 'text' field")
    preview_text = preview.get("text")
    if not preview_text or not isinstance(preview_text, str) or not preview_text.strip():
        raise ValueError("'preview.text' must be a non-null, non-empty string")

    # contentTypeTags
    if "contentTypeTags" not in content:
        raise ValueError("Top-level 'contentTypeTags' field is required")

    # learningSessions
    sessions = content.get("learningSessions")
    if not isinstance(sessions, list) or len(sessions) == 0:
        raise ValueError("'learningSessions' must be a non-empty array")


def _validate_content_type_tags(content, fmt):
    """Verify contentTypeTags matches the expected value for the format."""
    expected = CONTENT_TYPE_TAGS[fmt]
    actual = content.get("contentTypeTags")
    if actual != expected:
        raise ValueError(
            f"contentTypeTags mismatch for format '{fmt}': "
            f"expected {expected}, got {actual}"
        )


def _validate_sessions(content):
    """Check learningSessions has exactly 4 sessions, each with title and activities."""
    sessions = content["learningSessions"]

    if len(sessions) != 4:
        raise ValueError(
            f"'learningSessions' must contain exactly 4 sessions, got {len(sessions)}"
        )

    for i, session in enumerate(sessions):
        if not isinstance(session, dict):
            raise ValueError(f"Session {i + 1} must be an object")

        title = session.get("title")
        if not title or not isinstance(title, str) or not title.strip():
            raise ValueError(f"Session {i + 1} must have a non-empty 'title' string")

        activities = session.get("activities")
        if not isinstance(activities, list) or len(activities) == 0:
            raise ValueError(f"Session {i + 1} must have a non-empty 'activities' array")


def _validate_activity(activity, session_idx, activity_idx):
    """Check a single activity has required fields and valid activityType."""
    loc = f"Session {session_idx + 1}, Activity {activity_idx + 1}"

    if not isinstance(activity, dict):
        raise ValueError(f"{loc}: activity must be an object")

    # Must use activityType, not type
    if "type" in activity and "activityType" not in activity:
        raise ValueError(
            f"{loc}: uses 'type' instead of 'activityType' — "
            f"field must be 'activityType'"
        )

    activity_type = activity.get("activityType")
    if not activity_type or not isinstance(activity_type, str):
        raise ValueError(f"{loc}: missing or empty 'activityType' field")

    if activity_type not in VALID_ACTIVITY_TYPES:
        raise ValueError(
            f"{loc}: invalid activityType '{activity_type}'. "
            f"Must be one of: {', '.join(sorted(VALID_ACTIVITY_TYPES))}"
        )

    for field in ("title", "description"):
        val = activity.get(field)
        if not isinstance(val, str):
            raise ValueError(f"{loc} ({activity_type}): missing '{field}' field")

    data = activity.get("data")
    if not isinstance(data, dict):
        raise ValueError(f"{loc} ({activity_type}): missing 'data' field (must be an object)")

    # Validate activity-type-specific data
    _validate_activity_data(activity_type, data, loc)


def _validate_activity_data(activity_type, data, loc):
    """Validate activity-type-specific data fields."""
    if activity_type in VOCAB_ACTIVITY_TYPES:
        _validate_vocab_list(data, loc, activity_type)

    if activity_type == "writingSentence":
        _validate_writing_sentence(data, loc)

    if activity_type == "writingParagraph":
        _validate_writing_paragraph(data, loc)


def _validate_vocab_list(data, loc, activity_type):
    """Validate vocabList on vocab activities: non-empty array of lowercase strings."""
    if "words" in data:
        raise ValueError(
            f"{loc} ({activity_type}): uses 'words' instead of 'vocabList' — "
            f"field name must be 'vocabList'"
        )

    vocab_list = data.get("vocabList")
    if not isinstance(vocab_list, list) or len(vocab_list) == 0:
        raise ValueError(
            f"{loc} ({activity_type}): 'data.vocabList' must be a non-empty array"
        )

    for j, word in enumerate(vocab_list):
        if not isinstance(word, str):
            raise ValueError(
                f"{loc} ({activity_type}): vocabList[{j}] must be a string, "
                f"got {type(word).__name__}"
            )
        if word != word.lower():
            raise ValueError(
                f"{loc} ({activity_type}): vocabList[{j}] '{word}' must be lowercase"
            )


def _validate_writing_sentence(data, loc):
    """Validate writingSentence data: vocabList, items with prompt and targetVocab."""
    if "vocabList" not in data:
        raise ValueError(f"{loc} (writingSentence): missing 'data.vocabList'")

    vocab_list = data.get("vocabList")
    if not isinstance(vocab_list, list) or len(vocab_list) == 0:
        raise ValueError(
            f"{loc} (writingSentence): 'data.vocabList' must be a non-empty array"
        )

    items = data.get("items")
    if not isinstance(items, list) or len(items) == 0:
        raise ValueError(
            f"{loc} (writingSentence): 'data.items' must be a non-empty array"
        )

    for j, item in enumerate(items):
        if not isinstance(item, dict):
            raise ValueError(
                f"{loc} (writingSentence): items[{j}] must be an object"
            )
        for field in ("prompt", "targetVocab"):
            val = item.get(field)
            if not val or not isinstance(val, str) or not val.strip():
                raise ValueError(
                    f"{loc} (writingSentence): items[{j}] missing or empty '{field}'"
                )


def _validate_writing_paragraph(data, loc):
    """Validate writingParagraph data: vocabList, instructions, prompts."""
    if "vocabList" not in data:
        raise ValueError(f"{loc} (writingParagraph): missing 'data.vocabList'")

    vocab_list = data.get("vocabList")
    if not isinstance(vocab_list, list) or len(vocab_list) == 0:
        raise ValueError(
            f"{loc} (writingParagraph): 'data.vocabList' must be a non-empty array"
        )

    instructions = data.get("instructions")
    if not instructions or not isinstance(instructions, str) or not instructions.strip():
        raise ValueError(
            f"{loc} (writingParagraph): 'data.instructions' must be a non-empty string"
        )

    prompts = data.get("prompts")
    if not isinstance(prompts, list):
        raise ValueError(
            f"{loc} (writingParagraph): 'data.prompts' must be an array"
        )
    if len(prompts) < 2:
        raise ValueError(
            f"{loc} (writingParagraph): 'data.prompts' must have at least 2 items, "
            f"got {len(prompts)}"
        )
    for j, p in enumerate(prompts):
        if not isinstance(p, str):
            raise ValueError(
                f"{loc} (writingParagraph): prompts[{j}] must be a string"
            )


def _validate_flashcard_consistency(session, session_idx):
    """Check viewFlashcards and speakFlashcards in the same session have identical vocabList."""
    view_vocabs = []
    speak_vocabs = []

    for activity in session.get("activities", []):
        at = activity.get("activityType")
        vocab = activity.get("data", {}).get("vocabList")
        if at == "viewFlashcards" and vocab is not None:
            view_vocabs.append(vocab)
        elif at == "speakFlashcards" and vocab is not None:
            speak_vocabs.append(vocab)

    # If both viewFlashcards and speakFlashcards exist, all must share the same vocabList
    if view_vocabs and speak_vocabs:
        # All view vocabs should be the same
        reference = view_vocabs[0]
        for vl in speak_vocabs:
            if vl != reference:
                raise ValueError(
                    f"Session {session_idx + 1}: viewFlashcards and speakFlashcards "
                    f"have mismatched vocabList arrays. "
                    f"viewFlashcards: {reference}, speakFlashcards: {vl}"
                )


def _validate_activity_sequence(content, fmt):
    """Verify activity type sequence matches the declared format template for each session."""
    sessions = content["learningSessions"]
    expected_sequences = ACTIVITY_SEQUENCES[fmt]

    for i, session in enumerate(sessions):
        activities = session.get("activities", [])
        actual_sequence = [a.get("activityType") for a in activities]
        expected_sequence = expected_sequences[i]

        if actual_sequence != expected_sequence:
            raise ValueError(
                f"Session {i + 1} activity sequence mismatch for format '{fmt}': "
                f"expected {expected_sequence}, got {actual_sequence}"
            )


def _validate_writing_restriction(content):
    """Writing activities (writingSentence, writingParagraph) only allowed in sessions 3 and 4."""
    sessions = content["learningSessions"]

    for i, session in enumerate(sessions):
        if i >= 2:  # Sessions 3 and 4 (0-indexed: 2, 3) are allowed
            continue
        for j, activity in enumerate(session.get("activities", [])):
            at = activity.get("activityType")
            if at in WRITING_ACTIVITY_TYPES:
                raise ValueError(
                    f"Session {i + 1}, Activity {j + 1}: "
                    f"activityType '{at}' is only allowed in sessions 3 and 4, "
                    f"found in session {i + 1}"
                )


def validate(content: dict, format: str) -> None:
    """
    Validates curriculum content JSON for Buddhism/meditation curriculums.

    Args:
        content: The curriculum content dict
        format: One of "story_reading", "speaking", "balanced"

    Raises:
        ValueError with specific violation message on any failure.
    """
    # Validate format parameter
    if format not in VALID_FORMATS:
        raise ValueError(
            f"Invalid format '{format}'. Must be one of: {', '.join(sorted(VALID_FORMATS))}"
        )

    # 1. Top-level structure
    _validate_top_level(content)

    # 2. contentTypeTags matches format
    _validate_content_type_tags(content, format)

    # 3. Session structure (exactly 4 sessions)
    _validate_sessions(content)

    # 4. Activity structure and type-specific validation
    sessions = content["learningSessions"]
    for i, session in enumerate(sessions):
        for j, activity in enumerate(session.get("activities", [])):
            _validate_activity(activity, i, j)

        # 5. Flashcard consistency within each session
        _validate_flashcard_consistency(session, i)

    # 6. No strip-keys anywhere in the JSON tree
    _check_strip_keys(content)

    # 7. Activity sequence matches format template
    _validate_activity_sequence(content, format)

    # 8. Writing activities restricted to sessions 3 and 4
    _validate_writing_restriction(content)
