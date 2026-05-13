"""
Validator module for the Digital Economy Onboarding Curriculum.

This module contains the validate() function and associated constants
used to verify curriculum content JSON structure before upload.

The original creation script was deleted after successful curriculum creation.
This module is retained for property-based testing of the validator.
"""

STRIP_KEYS = frozenset({
    "mp3Url", "illustrationSet", "chapterBookmarks", "segments",
    "whiteboardItems", "userReadingId", "lessonUniqueId",
    "curriculumTags", "taskId", "imageId"
})

VALID_ACTIVITY_TYPES = frozenset({
    "introAudio", "viewFlashcards", "speakFlashcards",
    "vocabLevel1", "reading", "speakReading", "readAlong",
    "writingSentence"
})

EXPECTED_SEQUENCE = (
    "introAudio", "viewFlashcards", "speakFlashcards", "vocabLevel1",
    "reading", "speakReading", "readAlong", "writingSentence", "introAudio"
)

# Fields that belong inside data, not inline on the activity
CONTENT_FIELDS = frozenset({"vocabList", "text", "items", "passages"})


def _check_strip_keys(obj, path=""):
    """Recursively check for strip keys anywhere in the JSON tree."""
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key in STRIP_KEYS:
                raise ValueError(f"Strip key '{key}' found in content at {path}")
            _check_strip_keys(value, f"{path}.{key}")
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            _check_strip_keys(item, f"{path}[{i}]")


def validate(content: dict) -> None:
    """
    Validates curriculum content JSON for the digital economy onboarding curriculum.

    Checks 20 structural properties before upload. Raises ValueError with
    specific violation message on any failure.
    """
    # 1. Content is a dict
    if not isinstance(content, dict):
        raise ValueError("Content must be a dict")

    # 2. Title is non-empty string
    title = content.get("title")
    if not title or not isinstance(title, str) or not title.strip():
        raise ValueError("Missing or empty title")

    # 3. Description is non-empty string
    description = content.get("description")
    if not description or not isinstance(description, str) or not description.strip():
        raise ValueError("Missing or empty description")

    # 4. Preview is dict with non-empty text
    preview = content.get("preview")
    if not isinstance(preview, dict):
        raise ValueError("Missing or empty preview.text")
    preview_text = preview.get("text")
    if not preview_text or not isinstance(preview_text, str) or not preview_text.strip():
        raise ValueError("Missing or empty preview.text")

    # 5. contentTypeTags equals []
    tags = content.get("contentTypeTags")
    if tags != []:
        raise ValueError("contentTypeTags must be []")

    # 6. learningSessions is list with exactly 1 element
    sessions = content.get("learningSessions")
    if not isinstance(sessions, list) or len(sessions) != 1:
        raise ValueError("Must have exactly 1 learning session")

    session = sessions[0]

    # 7. Session has non-empty title
    session_title = session.get("title")
    if not session_title or not isinstance(session_title, str) or not session_title.strip():
        raise ValueError("Session missing title")

    # 8. Session has non-empty activities list
    activities = session.get("activities")
    if not isinstance(activities, list) or len(activities) == 0:
        raise ValueError("Session has no activities")

    # 9. Activity sequence matches EXPECTED_SEQUENCE
    actual_sequence = tuple(a.get("activityType", "") for a in activities)
    if actual_sequence != EXPECTED_SEQUENCE:
        raise ValueError(
            f"Activity sequence mismatch: expected {list(EXPECTED_SEQUENCE)}, "
            f"got {list(actual_sequence)}"
        )

    # 10-13. Each activity has required fields and correct structure
    view_flashcards_vocab = None
    speak_flashcards_vocab = None

    for i, activity in enumerate(activities):
        # 10. Required fields
        for field in ("activityType", "title", "description", "data"):
            if field not in activity:
                raise ValueError(f"Activity {i} missing required field: {field}")

        # 11. No 'type' field (old schema)
        if "type" in activity:
            raise ValueError("Activity uses 'type' instead of 'activityType'")

        # 12. activityType is valid
        act_type = activity["activityType"]
        if act_type not in VALID_ACTIVITY_TYPES:
            raise ValueError(f"Invalid activityType: {act_type}")

        # 13. Content fields inside data, not inline
        for field in CONTENT_FIELDS:
            if field in activity:
                raise ValueError(f"Content field '{field}' found inline on activity")

        data = activity.get("data", {})

        # 14-15. vocabList format checks
        if "vocabList" in data:
            vocab = data["vocabList"]
            if not isinstance(vocab, list):
                raise ValueError("vocabList must be array of lowercase strings")
            for word in vocab:
                if not isinstance(word, str):
                    raise ValueError("vocabList must be array of lowercase strings")
                if word != word.lower():
                    raise ValueError("vocabList must be array of lowercase strings")
            # 17. vocabList arrays have exactly 5 items
            if len(vocab) != 5:
                raise ValueError("vocabList must have exactly 5 words")

        # Check for 'words' field (must be vocabList)
        if "words" in data:
            raise ValueError("Field 'words' found — use 'vocabList'")

        # Track flashcard vocabLists for consistency check
        if act_type == "viewFlashcards":
            view_flashcards_vocab = data.get("vocabList")
        elif act_type == "speakFlashcards":
            speak_flashcards_vocab = data.get("vocabList")

        # 18-19. writingSentence structure
        if act_type == "writingSentence":
            if "vocabList" not in data or "items" not in data:
                raise ValueError("writingSentence missing data.vocabList or data.items")
            items = data["items"]
            if not isinstance(items, list) or len(items) == 0:
                raise ValueError("writingSentence missing data.vocabList or data.items")
            for item in items:
                if "prompt" not in item:
                    raise ValueError("writingSentence item missing prompt or targetVocab")
                if "targetVocab" not in item:
                    raise ValueError("writingSentence item missing prompt or targetVocab")

    # 16. viewFlashcards/speakFlashcards vocabList consistency
    if view_flashcards_vocab is not None and speak_flashcards_vocab is not None:
        if view_flashcards_vocab != speak_flashcards_vocab:
            raise ValueError("viewFlashcards/speakFlashcards vocabList mismatch")

    # 20. No strip keys anywhere in tree
    _check_strip_keys(content)
