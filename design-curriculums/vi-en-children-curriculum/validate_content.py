"""
validate_content.py — Children's curriculum content validator.

Validates curriculum content JSON for Vietnamese-English children's curriculums
(ages 6-10). Supports three formats:
  - "beginner_mini": 1 session, 3-5 unique vocab words, no vocabLevel1/vocabLevel2
  - "beginner_short": 4 sessions, 8-10 unique vocab words
  - "preintermediate_short": 4 sessions, 10-12 unique vocab words

All formats forbid writingParagraph and vocabLevel3.
beginner_mini additionally forbids vocabLevel1 and vocabLevel2.

Usage:
    from validate_content import validate
    validate(content_dict, format="beginner_mini")
    validate(content_dict, format="beginner_short")
    validate(content_dict, format="preintermediate_short")
"""

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
}

# Forbidden in ALL children's formats
CHILDREN_FORBIDDEN_ACTIVITIES = {"writingParagraph", "vocabLevel3"}

# Additionally forbidden in beginner_mini
BEGINNER_MINI_EXTRA_FORBIDDEN = {"vocabLevel1", "vocabLevel2"}

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

# Format configuration
FORMAT_CONFIG = {
    "beginner_mini": {
        "session_count": 1,
        "vocab_min": 3,
        "vocab_max": 5,
        "forbidden": CHILDREN_FORBIDDEN_ACTIVITIES | BEGINNER_MINI_EXTRA_FORBIDDEN,
    },
    "beginner_short": {
        "session_count": 4,
        "vocab_min": 8,
        "vocab_max": 10,
        "forbidden": CHILDREN_FORBIDDEN_ACTIVITIES,
    },
    "preintermediate_short": {
        "session_count": 4,
        "vocab_min": 10,
        "vocab_max": 12,
        "forbidden": CHILDREN_FORBIDDEN_ACTIVITIES,
    },
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
        raise ValueError("Top-level 'preview' must be a dict with a 'text' field")
    preview_text = preview.get("text")
    if not preview_text or not isinstance(preview_text, str) or not preview_text.strip():
        raise ValueError("'preview.text' must be a non-null, non-empty string")

    # contentTypeTags must be []
    tags = content.get("contentTypeTags")
    if tags != []:
        raise ValueError(
            f"'contentTypeTags' must be an empty list [], got {tags!r}"
        )

    # learningSessions
    sessions = content.get("learningSessions")
    if not isinstance(sessions, list) or len(sessions) == 0:
        raise ValueError("'learningSessions' must be a non-empty array")


def _validate_sessions(content, fmt):
    """Check learningSessions has the correct count per format, each with title and activities."""
    sessions = content["learningSessions"]
    config = FORMAT_CONFIG[fmt]
    expected = config["session_count"]

    if len(sessions) != expected:
        raise ValueError(
            f"'learningSessions' must contain exactly {expected} session(s) for "
            f"format '{fmt}', got {len(sessions)}"
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


def _validate_activity(activity, session_idx, activity_idx, fmt):
    """Check a single activity has required fields and valid activityType."""
    loc = f"Session {session_idx + 1}, Activity {activity_idx + 1}"
    config = FORMAT_CONFIG[fmt]

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

    # Format-specific: reject forbidden activity types
    if activity_type in config["forbidden"]:
        raise ValueError(
            f"{loc}: activityType '{activity_type}' is not allowed in "
            f"'{fmt}' format"
        )

    for field in ("title", "description"):
        val = activity.get(field)
        if not isinstance(val, str):
            raise ValueError(f"{loc} ({activity_type}): missing '{field}' field")

    data = activity.get("data")
    if not isinstance(data, dict):
        raise ValueError(f"{loc} ({activity_type}): missing 'data' field (must be a dict)")

    # Validate activity-type-specific data
    _validate_activity_data(activity_type, data, loc)


def _validate_activity_data(activity_type, data, loc):
    """Validate activity-type-specific data fields."""
    if activity_type in VOCAB_ACTIVITY_TYPES:
        _validate_vocab_list(data, loc, activity_type)

    if activity_type == "writingSentence":
        _validate_writing_sentence(data, loc)


def _validate_vocab_list(data, loc, activity_type):
    """Validate vocabList on vocab activities: non-empty array of lowercase strings."""
    # Must not use 'words' field name
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

    for j, word in enumerate(vocab_list):
        if not isinstance(word, str):
            raise ValueError(
                f"{loc} (writingSentence): vocabList[{j}] must be a string, "
                f"got {type(word).__name__}"
            )
        if word != word.lower():
            raise ValueError(
                f"{loc} (writingSentence): vocabList[{j}] '{word}' must be lowercase"
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


def _validate_flashcard_consistency(session, session_idx):
    """Check viewFlashcards and speakFlashcards in the same session have identical vocabList."""
    view_vocab = None
    speak_vocab = None

    for activity in session.get("activities", []):
        at = activity.get("activityType")
        if at == "viewFlashcards":
            view_vocab = activity.get("data", {}).get("vocabList")
        elif at == "speakFlashcards":
            speak_vocab = activity.get("data", {}).get("vocabList")

    if view_vocab is not None and speak_vocab is not None:
        if view_vocab != speak_vocab:
            raise ValueError(
                f"Session {session_idx + 1}: viewFlashcards and speakFlashcards "
                f"have mismatched vocabList arrays. "
                f"viewFlashcards: {view_vocab}, speakFlashcards: {speak_vocab}"
            )


def _validate_total_vocab(content, fmt):
    """Check total unique vocab count across all vocabList fields is within range for the format."""
    config = FORMAT_CONFIG[fmt]
    vocab_min = config["vocab_min"]
    vocab_max = config["vocab_max"]
    all_vocab = set()

    sessions = content["learningSessions"]
    for session in sessions:
        for activity in session.get("activities", []):
            at = activity.get("activityType")
            if at in VOCAB_ACTIVITY_TYPES:
                vocab_list = activity.get("data", {}).get("vocabList", [])
                for word in vocab_list:
                    if isinstance(word, str):
                        all_vocab.add(word)

    if len(all_vocab) < vocab_min or len(all_vocab) > vocab_max:
        raise ValueError(
            f"Total unique vocab count must be {vocab_min}-{vocab_max} for "
            f"format '{fmt}', got {len(all_vocab)}: {sorted(all_vocab)}"
        )


def validate(content: dict, format: str) -> None:
    """
    Validates curriculum content JSON for children's curriculums.

    Args:
        content: The curriculum content dict
        format: One of "beginner_mini", "beginner_short", "preintermediate_short"

    Raises:
        ValueError with specific violation message on any failure.
    """
    # Validate format parameter
    if format not in FORMAT_CONFIG:
        raise ValueError(
            f"Invalid format '{format}'. Must be one of: "
            f"{', '.join(sorted(FORMAT_CONFIG.keys()))}"
        )

    # 1. Top-level structure
    _validate_top_level(content)

    # 2. Session structure (format-aware count)
    _validate_sessions(content, format)

    # 3. Activity structure, type validation, and format-specific forbidden checks
    sessions = content["learningSessions"]
    for i, session in enumerate(sessions):
        for j, activity in enumerate(session.get("activities", [])):
            _validate_activity(activity, i, j, format)

        # 4. Flashcard consistency within each session
        _validate_flashcard_consistency(session, i)

    # 5. No strip-keys anywhere in the JSON tree
    _check_strip_keys(content)

    # 6. Total unique vocab count within expected range
    _validate_total_vocab(content, format)
