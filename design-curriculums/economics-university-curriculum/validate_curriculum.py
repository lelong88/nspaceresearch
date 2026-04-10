"""
Shared validation helper for Economics University Curriculum content JSON.

Validates curriculum structure, activity schemas, vocabList integrity,
and top-level fields before upload. Pure Python — no API calls, no
imports beyond standard library.

Usage:
    from validate_curriculum import validate_all
    validate_all(content)  # raises ValueError on any failure
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

# Sessions 1-3: learning sessions (6 words each)
LEARNING_SESSION_SEQUENCE = [
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
]

# Session 4: review session (all 18 words)
REVIEW_SESSION_SEQUENCE = [
    "introAudio",
    "viewFlashcards",
    "speakFlashcards",
    "vocabLevel1",
    "vocabLevel2",
    "vocabLevel3",
    "writingSentence",
]

# Session 5: full-reading session (all 18 words)
FULL_READING_SESSION_SEQUENCE = [
    "introAudio",
    "reading",
    "speakReading",
    "readAlong",
    "writingParagraph",
    "introAudio",
]


def validate_session_structure(content):
    """
    Validate that the curriculum has exactly 5 sessions with correct
    activity sequences and vocabList sizes.

    Sessions 1-3: learning sessions with 6-word vocabLists
    Session 4: review session with 18-word vocabList
    Session 5: full-reading session referencing all 18 words
    """
    sessions = content.get("learningSessions")
    if not isinstance(sessions, list) or len(sessions) != 5:
        raise ValueError(
            f"Expected exactly 5 learningSessions, got "
            f"{len(sessions) if isinstance(sessions, list) else type(sessions).__name__}"
        )

    # --- Sessions 1-3: learning sessions ---
    for i in range(3):
        session = sessions[i]
        activities = session.get("activities")
        if not isinstance(activities, list):
            raise ValueError(f"Session {i+1}: 'activities' must be a list")

        actual_types = [a.get("activityType") for a in activities]
        if actual_types != LEARNING_SESSION_SEQUENCE:
            raise ValueError(
                f"Session {i+1}: activity sequence mismatch.\n"
                f"  Expected: {LEARNING_SESSION_SEQUENCE}\n"
                f"  Got:      {actual_types}"
            )

        # Check vocabList size = 6 on vocab-bearing activities
        for activity in activities:
            atype = activity.get("activityType")
            data = activity.get("data", {})
            if atype in (
                "viewFlashcards", "speakFlashcards",
                "vocabLevel1", "vocabLevel2", "vocabLevel3",
            ):
                vocab = data.get("vocabList")
                if not isinstance(vocab, list) or len(vocab) != 6:
                    raise ValueError(
                        f"Session {i+1}, {atype}: vocabList must have exactly "
                        f"6 words, got {len(vocab) if isinstance(vocab, list) else type(vocab).__name__}"
                    )

    # --- Session 4: review session ---
    session4 = sessions[3]
    activities4 = session4.get("activities")
    if not isinstance(activities4, list):
        raise ValueError("Session 4: 'activities' must be a list")

    actual_types4 = [a.get("activityType") for a in activities4]
    if actual_types4 != REVIEW_SESSION_SEQUENCE:
        raise ValueError(
            f"Session 4: activity sequence mismatch.\n"
            f"  Expected: {REVIEW_SESSION_SEQUENCE}\n"
            f"  Got:      {actual_types4}"
        )

    # Check vocabList size = 18 on vocab-bearing activities in session 4
    for activity in activities4:
        atype = activity.get("activityType")
        data = activity.get("data", {})
        if atype in (
            "viewFlashcards", "speakFlashcards",
            "vocabLevel1", "vocabLevel2", "vocabLevel3",
        ):
            vocab = data.get("vocabList")
            if not isinstance(vocab, list) or len(vocab) != 18:
                raise ValueError(
                    f"Session 4, {atype}: vocabList must have exactly "
                    f"18 words, got {len(vocab) if isinstance(vocab, list) else type(vocab).__name__}"
                )

    # --- Session 5: full-reading session ---
    session5 = sessions[4]
    activities5 = session5.get("activities")
    if not isinstance(activities5, list):
        raise ValueError("Session 5: 'activities' must be a list")

    actual_types5 = [a.get("activityType") for a in activities5]
    if actual_types5 != FULL_READING_SESSION_SEQUENCE:
        raise ValueError(
            f"Session 5: activity sequence mismatch.\n"
            f"  Expected: {FULL_READING_SESSION_SEQUENCE}\n"
            f"  Got:      {actual_types5}"
        )

    # Session 5 writingParagraph should reference all 18 words
    for activity in activities5:
        if activity.get("activityType") == "writingParagraph":
            vocab = activity.get("data", {}).get("vocabList")
            if not isinstance(vocab, list) or len(vocab) != 18:
                raise ValueError(
                    f"Session 5, writingParagraph: vocabList must have exactly "
                    f"18 words, got {len(vocab) if isinstance(vocab, list) else type(vocab).__name__}"
                )


def validate_activity_schema(activity):
    """
    Validate a single activity object:
    - Has activityType (not 'type'), title, description, data fields
    - activityType is one of 11 valid values
    - All content is inside the data object (not inline)
    - No strip keys present
    """
    # Required fields
    if "type" in activity:
        raise ValueError(
            f"Activity uses 'type' instead of 'activityType' — this is the old "
            f"corrupted schema. Found type='{activity['type']}'"
        )

    for field in ("activityType", "title", "description", "data"):
        if field not in activity:
            raise ValueError(
                f"Activity missing required field '{field}'. "
                f"Keys present: {list(activity.keys())}"
            )

    atype = activity["activityType"]
    if atype not in VALID_ACTIVITY_TYPES:
        raise ValueError(
            f"Invalid activityType '{atype}'. "
            f"Must be one of: {sorted(VALID_ACTIVITY_TYPES)}"
        )

    if not isinstance(activity["data"], dict):
        raise ValueError(
            f"Activity '{atype}': 'data' must be an object, "
            f"got {type(activity['data']).__name__}"
        )

    # Content must be inside data, not inline on the activity
    # Check for known data fields appearing at activity level
    inline_data_fields = {"text", "vocabList", "words", "items", "instructions", "prompts"}
    for field in inline_data_fields:
        if field in activity:
            raise ValueError(
                f"Activity '{atype}': field '{field}' found inline on activity "
                f"object — must be inside 'data'"
            )

    # No strip keys anywhere in the activity
    _check_strip_keys(activity, f"activity '{atype}'")


def _check_strip_keys(obj, path):
    """Recursively check for strip keys in a dict/list structure."""
    if isinstance(obj, dict):
        for key in obj:
            if key in STRIP_KEYS:
                raise ValueError(
                    f"Strip key '{key}' found in {path}"
                )
            _check_strip_keys(obj[key], f"{path}.{key}")
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            _check_strip_keys(item, f"{path}[{i}]")


def validate_vocablist_integrity(content):
    """
    Validate vocabList consistency:
    - viewFlashcards and speakFlashcards in the same session have identical vocabLists
    - All vocabList entries are lowercase strings
    - Field name is 'vocabList', never 'words'
    """
    sessions = content.get("learningSessions", [])

    for i, session in enumerate(sessions):
        activities = session.get("activities", [])

        # Check for 'words' field (wrong name)
        for activity in activities:
            data = activity.get("data", {})
            if "words" in data:
                raise ValueError(
                    f"Session {i+1}, {activity.get('activityType')}: "
                    f"uses 'words' instead of 'vocabList'"
                )

        # Find viewFlashcards and speakFlashcards vocabLists
        view_vocab = None
        speak_vocab = None
        for activity in activities:
            atype = activity.get("activityType")
            data = activity.get("data", {})
            if atype == "viewFlashcards":
                view_vocab = data.get("vocabList")
            elif atype == "speakFlashcards":
                speak_vocab = data.get("vocabList")

        # If both exist, they must match
        if view_vocab is not None and speak_vocab is not None:
            if view_vocab != speak_vocab:
                raise ValueError(
                    f"Session {i+1}: viewFlashcards vocabList != speakFlashcards vocabList.\n"
                    f"  viewFlashcards: {view_vocab}\n"
                    f"  speakFlashcards: {speak_vocab}"
                )

        # All vocabList entries must be lowercase strings
        for activity in activities:
            data = activity.get("data", {})
            vocab = data.get("vocabList")
            if vocab is not None:
                atype = activity.get("activityType")
                if not isinstance(vocab, list):
                    raise ValueError(
                        f"Session {i+1}, {atype}: vocabList must be a list, "
                        f"got {type(vocab).__name__}"
                    )
                for j, word in enumerate(vocab):
                    if not isinstance(word, str):
                        raise ValueError(
                            f"Session {i+1}, {atype}: vocabList[{j}] must be a string, "
                            f"got {type(word).__name__}: {word!r}"
                        )
                    if word != word.lower():
                        raise ValueError(
                            f"Session {i+1}, {atype}: vocabList[{j}] must be lowercase, "
                            f"got '{word}'"
                        )


def validate_top_level(content):
    """
    Validate top-level curriculum content fields:
    - contentTypeTags = []
    - title present (non-empty string)
    - description present (non-empty string)
    - preview.text present (non-empty string)
    - learningSessions is array of length 5
    """
    # contentTypeTags
    tags = content.get("contentTypeTags")
    if tags != []:
        raise ValueError(
            f"contentTypeTags must be [] (empty list), got {tags!r}"
        )

    # title
    title = content.get("title")
    if not isinstance(title, str) or not title.strip():
        raise ValueError(
            f"'title' must be a non-empty string, got {title!r}"
        )

    # description
    desc = content.get("description")
    if not isinstance(desc, str) or not desc.strip():
        raise ValueError(
            f"'description' must be a non-empty string, got {desc!r}"
        )

    # preview.text
    preview = content.get("preview")
    if not isinstance(preview, dict):
        raise ValueError(
            f"'preview' must be an object, got {type(preview).__name__ if preview is not None else 'None'}"
        )
    preview_text = preview.get("text")
    if not isinstance(preview_text, str) or not preview_text.strip():
        raise ValueError(
            f"'preview.text' must be a non-empty string, got {preview_text!r}"
        )

    # learningSessions
    sessions = content.get("learningSessions")
    if not isinstance(sessions, list) or len(sessions) != 5:
        raise ValueError(
            f"'learningSessions' must be an array of length 5, got "
            f"{len(sessions) if isinstance(sessions, list) else type(sessions).__name__}"
        )


def validate_all(content):
    """
    Run all 4 validators. Raises ValueError with a descriptive message
    on the first failure encountered.
    """
    validate_top_level(content)
    validate_session_structure(content)

    # Validate every activity's schema
    for i, session in enumerate(content.get("learningSessions", [])):
        for j, activity in enumerate(session.get("activities", [])):
            try:
                validate_activity_schema(activity)
            except ValueError as e:
                raise ValueError(
                    f"Session {i+1}, activity {j+1}: {e}"
                ) from e

    validate_vocablist_integrity(content)
