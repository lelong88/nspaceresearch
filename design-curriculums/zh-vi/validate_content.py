"""
validate_content.py — Shared content validation module for curriculum creation.

Validates curriculum content JSON against all Content Corruption Detection Rules
before upload. Raises ValueError with a specific violation message on any failure.

Supports two levels:
  - "beginner": 4 sessions (2 learning + 1 review + 1 final), 12 unique vocab words,
                no writingParagraph, no vocabLevel3
  - "standard": 5 sessions (3 learning + 1 review + 1 final), 18 unique vocab words,
                full activity set including writingParagraph in final session

Usage:
    from validate_content import validate
    validate(content_dict)                    # standard (default)
    validate(content_dict, level="beginner")  # beginner
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

BEGINNER_FORBIDDEN_ACTIVITIES = {"writingParagraph", "vocabLevel3"}

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

# Level configuration
LEVEL_CONFIG = {
    "beginner": {
        "session_count": 4,
        "learning_session_count": 2,
        "total_vocab": 12,
    },
    "standard": {
        "session_count": 5,
        "learning_session_count": 3,
        "total_vocab": 18,
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


def _validate_sessions(content, level):
    """Check learningSessions has the correct count per level, each with title and activities."""
    sessions = content["learningSessions"]
    expected = LEVEL_CONFIG[level]["session_count"]

    if len(sessions) != expected:
        raise ValueError(
            f"'learningSessions' must contain exactly {expected} sessions for "
            f"{level} level, got {len(sessions)}"
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


def _validate_activity(activity, session_idx, activity_idx, level):
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

    # Beginner-specific: reject forbidden activity types
    if level == "beginner" and activity_type in BEGINNER_FORBIDDEN_ACTIVITIES:
        raise ValueError(
            f"{loc}: activityType '{activity_type}' is not allowed in beginner "
            f"curriculums"
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


def _validate_vocabulary_distribution(content, level):
    """Check vocab word count per level: 12 for beginner (2 learning sessions), 18 for standard (3 learning sessions)."""
    sessions = content["learningSessions"]
    config = LEVEL_CONFIG[level]
    learning_count = config["learning_session_count"]
    expected_total = config["total_vocab"]
    all_vocab = set()

    for i in range(learning_count):
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

    if len(all_vocab) != expected_total:
        raise ValueError(
            f"Curriculum must have exactly {expected_total} unique vocabulary words "
            f"across sessions 1-{learning_count} for {level} level, "
            f"got {len(all_vocab)}"
        )


def _validate_beginner_exclusions(content):
    """Check that beginner curriculums have no writingParagraph or vocabLevel3 activities."""
    sessions = content["learningSessions"]
    for i, session in enumerate(sessions):
        for j, activity in enumerate(session.get("activities", [])):
            at = activity.get("activityType")
            if at in BEGINNER_FORBIDDEN_ACTIVITIES:
                raise ValueError(
                    f"Session {i + 1}, Activity {j + 1}: activityType '{at}' is "
                    f"not allowed in beginner curriculums"
                )


def _validate_standard_writing_paragraph(content):
    """Check that standard curriculums have a writingParagraph activity in the final session."""
    sessions = content["learningSessions"]
    final_session = sessions[-1]
    has_writing_paragraph = False

    for activity in final_session.get("activities", []):
        if activity.get("activityType") == "writingParagraph":
            has_writing_paragraph = True
            break

    if not has_writing_paragraph:
        raise ValueError(
            f"Standard curriculum final session (Session {len(sessions)}) must "
            f"include a writingParagraph activity"
        )


def validate(content: dict, level: str = "standard") -> None:
    """
    Validates curriculum content JSON against all corruption detection rules.
    Raises ValueError with specific violation message if any check fails.

    Parameters:
        content: The curriculum content JSON dict
        level: "beginner" for 4-session/12-word structure,
               "standard" for 5-session/18-word structure (default)

    Checks (all levels):
    - Top-level structure (title, description, preview.text, contentTypeTags, learningSessions)
    - Session structure (correct count per level, each with title and activities)
    - Activity structure (activityType not type, valid values, title, description, data)
    - Activity-type-specific data rules
    - vocabList format (lowercase strings, field name is vocabList not words)
    - Cross-field consistency (viewFlashcards/speakFlashcards vocabList match)
    - No strip-keys present anywhere in JSON tree
    - Vocabulary distribution (correct count per level, 6 per learning session)

    Beginner-specific checks:
    - Exactly 4 sessions (2 learning + 1 review + 1 final)
    - Exactly 12 unique vocabulary words (6 per learning session)
    - No writingParagraph activities
    - No vocabLevel3 activities

    Standard-specific checks:
    - Exactly 5 sessions (3 learning + 1 review + 1 final)
    - Exactly 18 unique vocabulary words (6 per learning session)
    - writingParagraph required in final session
    """
    # Validate level parameter
    if level not in LEVEL_CONFIG:
        raise ValueError(
            f"Invalid level '{level}'. Must be 'beginner' or 'standard'"
        )

    # 1. Top-level structure
    _validate_top_level(content)

    # 2. Session structure (level-aware count)
    _validate_sessions(content, level)

    # 3. Beginner-specific: reject forbidden activity types
    if level == "beginner":
        _validate_beginner_exclusions(content)

    # 4. Activity structure and type-specific validation
    sessions = content["learningSessions"]
    for i, session in enumerate(sessions):
        for j, activity in enumerate(session.get("activities", [])):
            _validate_activity(activity, i, j, level)

        # 5. Flashcard consistency within each session
        _validate_flashcard_consistency(session, i)

    # 6. No strip-keys anywhere in the JSON tree
    _check_strip_keys(content)

    # 7. Vocabulary distribution (level-aware)
    _validate_vocabulary_distribution(content, level)

    # 8. Standard-specific: require writingParagraph in final session
    if level == "standard":
        _validate_standard_writing_paragraph(content)
