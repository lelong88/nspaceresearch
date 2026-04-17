"""
validate_short_content.py — Content validation for short single-session curriculums.

Adapted from validate_content.py for the short format:
- Exactly 1 learning session (not 5)
- Between 3 and 5 unique vocabulary words total (not 18 with 6-per-session)
- No vocabLevel3 activities (beginner-only)

Raises ValueError with a specific violation message on any failure.

Usage:
    from validate_short_content import validate_short
    validate_short(content_dict)  # raises ValueError if invalid
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
    """Check learningSessions is exactly 1 session with title and activities."""
    sessions = content["learningSessions"]

    if len(sessions) != 1:
        raise ValueError(
            f"'learningSessions' must contain exactly 1 session, got {len(sessions)}"
        )

    session = sessions[0]
    if not isinstance(session, dict):
        raise ValueError("Session 1 must be an object")

    title = session.get("title")
    if not title or not isinstance(title, str) or not title.strip():
        raise ValueError("Session 1 must have a non-empty 'title' string")

    activities = session.get("activities")
    if not isinstance(activities, list) or len(activities) == 0:
        raise ValueError("Session 1 must have a non-empty 'activities' array")


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


def _validate_no_vocab_level3(content):
    """Reject any activity with activityType vocabLevel3."""
    sessions = content["learningSessions"]
    for i, session in enumerate(sessions):
        for j, activity in enumerate(session.get("activities", [])):
            at = activity.get("activityType")
            if at == "vocabLevel3":
                raise ValueError(
                    f"Session {i + 1}, Activity {j + 1}: "
                    f"vocabLevel3 is not allowed in short curriculums "
                    f"(reduces cognitive load for beginners)"
                )


def _validate_vocabulary_distribution(content):
    """Check between 3 and 5 unique vocabulary words total across the single session."""
    sessions = content["learningSessions"]
    all_vocab = set()

    for session in sessions:
        for activity in session.get("activities", []):
            at = activity.get("activityType")
            if at in VOCAB_ACTIVITY_TYPES:
                vocab_list = activity.get("data", {}).get("vocabList", [])
                for word in vocab_list:
                    if isinstance(word, str):
                        all_vocab.add(word)

    count = len(all_vocab)
    if count < 3 or count > 5:
        raise ValueError(
            f"Short curriculum must have between 3 and 5 unique vocabulary words, "
            f"got {count}: {sorted(all_vocab)}"
        )


def validate_short(content: dict) -> None:
    """
    Validates short curriculum content JSON. Raises ValueError on failure.

    Checks:
    - Top-level structure (title, description, preview.text, contentTypeTags)
    - Exactly 1 learning session with title and activities
    - Activity structure (activityType, title, description, data)
    - Activity-type-specific data rules (vocabList, writingSentence, writingParagraph)
    - viewFlashcards/speakFlashcards vocabList consistency
    - No strip-keys anywhere in JSON tree
    - Between 3 and 5 unique vocabulary words total
    - No vocabLevel3 activities
    - vocabList contains lowercase strings, field name is vocabList (not words)
    """
    # 1. Top-level structure
    _validate_top_level(content)

    # 2. Session structure (exactly 1 session)
    _validate_sessions(content)

    # 3. No vocabLevel3 activities
    _validate_no_vocab_level3(content)

    # 4. Activity structure and type-specific validation
    sessions = content["learningSessions"]
    for i, session in enumerate(sessions):
        for j, activity in enumerate(session.get("activities", [])):
            _validate_activity(activity, i, j)

        # 5. Flashcard consistency within each session
        _validate_flashcard_consistency(session, i)

    # 6. No strip-keys anywhere in the JSON tree
    _check_strip_keys(content)

    # 7. Vocabulary distribution: 3-5 unique words total
    _validate_vocabulary_distribution(content)
