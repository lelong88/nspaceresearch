"""
validate_content.py — Shared content validation module for curriculum creation.

Validates curriculum content JSON against all Content Corruption Detection Rules
before upload. Raises ValueError with a specific violation message on any failure.

Usage:
    from validate_content import validate
    validate(content_dict)  # raises ValueError if invalid
"""

VALID_ACTIVITY_TYPES = {
    "introAudio",
    "viewFlashcards",
    "speakFlashcards",
    "vocabLevel1",
    "vocabLevel2",
    "vocabLevel3",
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
    "vocabLevel3",
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


def _validate_sessions(content):
    """Check learningSessions is exactly 5 sessions, each with title and activities."""
    sessions = content["learningSessions"]

    if len(sessions) != 5:
        raise ValueError(
            f"'learningSessions' must contain exactly 5 sessions, got {len(sessions)}"
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
            f"'type' is the old schema and is corrupted"
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

    # vocabList activities
    if activity_type in VOCAB_ACTIVITY_TYPES:
        _validate_vocab_list(data, loc, activity_type)

    # writingSentence
    if activity_type == "writingSentence":
        _validate_writing_sentence(data, loc)

    # writingParagraph
    if activity_type == "writingParagraph":
        _validate_writing_paragraph(data, loc)


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


def _validate_vocabulary_distribution(content):
    """Check exactly 18 unique vocab words total, 6 per learning session (sessions 1-3)."""
    sessions = content["learningSessions"]
    all_vocab = set()

    for i in range(3):  # Sessions 1-3 (learning sessions)
        session = sessions[i]
        session_vocab = set()

        for activity in session.get("activities", []):
            at = activity.get("activityType")
            if at in VOCAB_ACTIVITY_TYPES:
                vocab_list = activity.get("data", {}).get("vocabList", [])
                for word in vocab_list:
                    session_vocab.add(word)

        if len(session_vocab) != 6:
            raise ValueError(
                f"Session {i + 1} must have exactly 6 unique vocabulary words, "
                f"got {len(session_vocab)}: {sorted(session_vocab)}"
            )

        all_vocab.update(session_vocab)

    if len(all_vocab) != 18:
        raise ValueError(
            f"Curriculum must have exactly 18 unique vocabulary words across "
            f"sessions 1-3, got {len(all_vocab)}"
        )


def validate(content: dict) -> None:
    """
    Validates curriculum content JSON against all corruption detection rules.
    Raises ValueError with specific violation message if any check fails.

    Checks:
    - Top-level structure (title, description, preview.text, contentTypeTags, learningSessions)
    - Session structure (exactly 5 sessions, each with title and activities)
    - Activity structure (activityType, title, description, data)
    - Activity-type-specific data rules
    - vocabList format (lowercase strings, field name is vocabList not words)
    - Cross-field consistency (viewFlashcards/speakFlashcards vocabList match)
    - No strip-keys present anywhere in JSON tree
    - Exactly 18 unique vocabulary words (6 per learning session)
    """
    # 1. Top-level structure
    _validate_top_level(content)

    # 2. Session structure (exactly 5 sessions)
    _validate_sessions(content)

    # 3-7. Activity structure and type-specific validation
    sessions = content["learningSessions"]
    for i, session in enumerate(sessions):
        for j, activity in enumerate(session.get("activities", [])):
            _validate_activity(activity, i, j)

        # 5. Flashcard consistency within each session
        _validate_flashcard_consistency(session, i)

    # 8. No strip-keys anywhere in the JSON tree
    _check_strip_keys(content)

    # 9. Vocabulary distribution: 18 total, 6 per learning session
    _validate_vocabulary_distribution(content)
