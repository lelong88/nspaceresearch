"""
validate_content.py — Format-aware content validator for the
vi-en Digital Economy curriculum spec.

Pure function: ``validate(content, fmt, level=None)`` either returns
``None`` (success) or raises ``ValueError`` with the violated rule, the
JSON path of the offending value, and an "expected vs actual" hint.

``fmt`` is one of ``"story_reading"``, ``"speaking"``, ``"balanced"``.
``level`` is one of ``"preintermediate"``, ``"intermediate"`` or ``None``
(skip the average-sentence-length check).

The module exposes the design-time constants ``STRIP_KEYS``,
``VALID_ACTIVITY_TYPES``, ``ACTIVITY_TEMPLATES`` and ``CONTENT_TYPE_TAGS``
so the per-curriculum scripts can import them without duplication.
"""

from __future__ import annotations

from typing import Any

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Auto-generated platform keys that must never appear in new content.
# Mirrors strip-keys.json plus a few defensive entries.
STRIP_KEYS = frozenset({
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
    # Defensive — present in strip-keys.json
    "practiceMinutes",
    "practiceTime",
    "difficultyTags",
    "skillFocusTags",
})

VALID_ACTIVITY_TYPES = frozenset({
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
})

# Activities that carry vocabList of "current session vocab"
# Must share an identical vocabList within a single session.
_SESSION_VOCAB_TYPES = ("viewFlashcards", "speakFlashcards", "vocabLevel1")

# Activities that carry a vocabList field at all.
_VOCAB_LIST_TYPES = frozenset({
    "viewFlashcards", "speakFlashcards",
    "vocabLevel1", "vocabLevel2", "vocabLevel3",
    "writingSentence", "writingParagraph",
})

# Activities whose data.text is a passage that must exist and be non-empty.
_TEXT_PASSAGE_TYPES = frozenset({
    "introAudio", "reading", "speakReading", "readAlong",
})

VALID_FORMATS = frozenset({"story_reading", "speaking", "balanced"})
VALID_LEVELS = frozenset({"preintermediate", "intermediate"})

# Per-format expected activityType sequence for each of the 4 sessions.
ACTIVITY_TEMPLATES: dict[str, list[list[str]]] = {
    "story_reading": [
        # Session 1
        ["introAudio", "viewFlashcards", "speakFlashcards",
         "reading", "speakReading", "readAlong", "introAudio"],
        # Session 2
        ["introAudio", "viewFlashcards", "speakFlashcards",
         "reading", "speakReading", "readAlong", "introAudio"],
        # Session 3
        ["introAudio", "viewFlashcards", "speakFlashcards", "vocabLevel1",
         "reading", "speakReading", "readAlong", "introAudio"],
        # Session 4 (Final)
        ["introAudio", "viewFlashcards", "speakFlashcards", "vocabLevel1",
         "reading", "speakReading", "readAlong", "writingSentence",
         "introAudio"],
    ],
    "speaking": [
        # Session 1
        ["introAudio", "viewFlashcards", "speakFlashcards", "vocabLevel1",
         "speakFlashcards", "reading", "speakReading", "introAudio"],
        # Session 2
        ["introAudio", "viewFlashcards", "speakFlashcards", "vocabLevel1",
         "speakFlashcards", "reading", "speakReading", "introAudio"],
        # Session 3
        ["introAudio", "viewFlashcards", "speakFlashcards", "vocabLevel1",
         "speakFlashcards", "reading", "speakReading", "introAudio"],
        # Session 4 (Final)
        ["introAudio", "viewFlashcards", "speakFlashcards", "vocabLevel1",
         "vocabLevel2", "speakFlashcards", "reading", "speakReading",
         "readAlong", "writingSentence", "introAudio"],
    ],
    "balanced": [
        # Session 1
        ["introAudio", "viewFlashcards", "speakFlashcards", "vocabLevel1",
         "reading", "speakReading", "readAlong", "introAudio"],
        # Session 2
        ["introAudio", "viewFlashcards", "speakFlashcards", "vocabLevel1",
         "reading", "speakReading", "readAlong", "introAudio"],
        # Session 3
        ["introAudio", "viewFlashcards", "speakFlashcards", "vocabLevel1",
         "reading", "speakReading", "readAlong", "writingSentence",
         "introAudio"],
        # Session 4 (Final)
        ["introAudio", "viewFlashcards", "speakFlashcards", "vocabLevel1",
         "vocabLevel2", "reading", "speakReading", "readAlong",
         "writingSentence", "writingParagraph", "introAudio"],
    ],
}

CONTENT_TYPE_TAGS: dict[str, list[str]] = {
    "story_reading": ["story"],
    "speaking": [],
    "balanced": [],
}

# Average-sentence-length bounds (words / sentence) per level.
_SENTENCE_LENGTH_BOUNDS = {
    "preintermediate": (10, 14),
    "intermediate": (12, 18),
}

# introAudio word-count bounds by role.
_WELCOME_TOKEN_BOUNDS = (500, 800)
_MID_TOKEN_BOUNDS = (200, 400)
_FAREWELL_TOKEN_BOUNDS = (400, 600)

# Convenience char bounds (per Req 9.1, 9.8, 10.x).
_TITLE_MIN, _TITLE_MAX = 1, 255
_DESC_MIN, _DESC_MAX = 1, 255
_SESSION_TITLE_MIN, _SESSION_TITLE_MAX = 5, 150
_VOCAB_WORD_MIN, _VOCAB_WORD_MAX = 1, 64
_VOCAB_LIST_MIN, _VOCAB_LIST_MAX = 1, 20
_INTRO_TITLE_MIN, _INTRO_TITLE_MAX = 5, 60
_INTRO_DESC_MIN, _INTRO_DESC_MAX = 20, 200
_WRITING_DESC_MIN, _WRITING_DESC_MAX = 20, 200
_WRITING_PROMPT_MIN, _WRITING_PROMPT_MAX = 1, 500
_WRITING_INSTR_MIN, _WRITING_INSTR_MAX = 1, 1000
_WRITING_SENT_ITEMS_MIN, _WRITING_SENT_ITEMS_MAX = 1, 10
_WRITING_PARA_PROMPTS_MIN, _WRITING_PARA_PROMPTS_MAX = 2, 10


# ---------------------------------------------------------------------------
# Error helpers
# ---------------------------------------------------------------------------

def _raise(rule: str, path: str, expected: Any, actual: Any) -> None:
    """Raise a ValueError with rule name, JSON path, and expected vs actual."""
    raise ValueError(
        f"[{rule}] at {path}: expected {expected!r}, got {actual!r}"
    )


# ---------------------------------------------------------------------------
# Top-level checks (1-6)
# ---------------------------------------------------------------------------

def _check_is_dict(content: Any) -> None:
    """Check 1: content is a dict."""
    if not isinstance(content, dict):
        _raise(
            "content must be a JSON object",
            "content",
            "dict",
            type(content).__name__,
        )


def _check_required_strings(content: dict) -> None:
    """Checks 2-4: title, description, preview.text are non-empty strings."""
    # title
    title = content.get("title")
    if not isinstance(title, str) or len(title) < _TITLE_MIN:
        _raise(
            "title must be a non-empty string",
            "content.title",
            f"non-empty string ({_TITLE_MIN}-{_TITLE_MAX} chars)",
            title,
        )
    if len(title) > _TITLE_MAX:
        _raise(
            "title length out of bounds",
            "content.title",
            f"<= {_TITLE_MAX} chars",
            f"{len(title)} chars",
        )

    # description
    description = content.get("description")
    if not isinstance(description, str) or len(description) < _DESC_MIN:
        _raise(
            "description must be a non-empty string",
            "content.description",
            "non-empty string",
            description,
        )

    # preview.text
    preview = content.get("preview")
    if not isinstance(preview, dict):
        _raise(
            "preview must be an object",
            "content.preview",
            "dict",
            type(preview).__name__ if preview is not None else "missing",
        )
    preview_text = preview.get("text")
    if not isinstance(preview_text, str) or len(preview_text) < 1:
        _raise(
            "preview.text must be a non-empty string",
            "content.preview.text",
            "non-empty string",
            preview_text,
        )


def _check_content_type_tags(content: dict, fmt: str) -> None:
    """Check 5: contentTypeTags == CONTENT_TYPE_TAGS[fmt] exactly."""
    expected = CONTENT_TYPE_TAGS[fmt]
    actual = content.get("contentTypeTags")
    if actual != expected:
        _raise(
            f"contentTypeTags must equal CONTENT_TYPE_TAGS['{fmt}']",
            "content.contentTypeTags",
            expected,
            actual,
        )


def _check_learning_sessions_shape(content: dict) -> list[dict]:
    """Check 6: learningSessions is a list of exactly 4 elements. Returns the list."""
    sessions = content.get("learningSessions")
    if not isinstance(sessions, list):
        _raise(
            "learningSessions must be a list",
            "content.learningSessions",
            "list",
            type(sessions).__name__ if sessions is not None else "missing",
        )
    if len(sessions) != 4:
        _raise(
            "learningSessions must contain exactly 4 sessions",
            "content.learningSessions",
            4,
            len(sessions),
        )
    return sessions


# ---------------------------------------------------------------------------
# Session checks (7)
# ---------------------------------------------------------------------------

def _check_session_titles_and_activities(sessions: list[dict]) -> None:
    """Check 7: each session has non-empty title (5-150), unique titles, non-empty activities."""
    seen_titles: dict[str, int] = {}
    for i, session in enumerate(sessions):
        path = f"learningSessions[{i}]"
        if not isinstance(session, dict):
            _raise(
                "session must be an object",
                path,
                "dict",
                type(session).__name__,
            )

        title = session.get("title")
        if not isinstance(title, str) or not title.strip():
            _raise(
                "session.title must be a non-empty string",
                f"{path}.title",
                "non-empty string",
                title,
            )
        if len(title) < _SESSION_TITLE_MIN or len(title) > _SESSION_TITLE_MAX:
            _raise(
                "session.title length out of bounds",
                f"{path}.title",
                f"{_SESSION_TITLE_MIN}-{_SESSION_TITLE_MAX} chars",
                f"{len(title)} chars",
            )

        if title in seen_titles:
            _raise(
                "session.title must be unique across the curriculum",
                f"{path}.title",
                f"unique title (already used at learningSessions[{seen_titles[title]}])",
                title,
            )
        seen_titles[title] = i

        activities = session.get("activities")
        if not isinstance(activities, list) or len(activities) == 0:
            _raise(
                "session.activities must be a non-empty list",
                f"{path}.activities",
                "non-empty list",
                activities,
            )


# ---------------------------------------------------------------------------
# Activity-sequence check (8)
# ---------------------------------------------------------------------------

def _check_activity_sequence(sessions: list[dict], fmt: str) -> None:
    """Check 8: activity-type sequence in each session matches ACTIVITY_TEMPLATES[fmt][i]."""
    expected_per_session = ACTIVITY_TEMPLATES[fmt]
    for i, session in enumerate(sessions):
        activities = session.get("activities", [])
        actual_seq = [a.get("activityType") if isinstance(a, dict) else None
                      for a in activities]
        expected_seq = expected_per_session[i]
        if actual_seq != expected_seq:
            _raise(
                f"activity sequence mismatch for format '{fmt}', session {i}",
                f"learningSessions[{i}].activities[*].activityType",
                expected_seq,
                actual_seq,
            )


# ---------------------------------------------------------------------------
# Per-activity checks (9, 10)
# ---------------------------------------------------------------------------

def _check_activity_shape(activity: Any, path: str) -> tuple[str, str, str, dict]:
    """Check 9: activity has activityType, title (1-255), description (1-255), data (dict);
    no `type` field; activityType in VALID_ACTIVITY_TYPES.
    Returns (activityType, title, description, data).
    """
    if not isinstance(activity, dict):
        _raise(
            "activity must be an object",
            path,
            "dict",
            type(activity).__name__,
        )

    if "type" in activity:
        _raise(
            "activity must use 'activityType', not 'type'",
            f"{path}.type",
            "no 'type' field",
            activity.get("type"),
        )

    activity_type = activity.get("activityType")
    if not isinstance(activity_type, str) or activity_type not in VALID_ACTIVITY_TYPES:
        _raise(
            "activity.activityType must be a valid type",
            f"{path}.activityType",
            f"one of {sorted(VALID_ACTIVITY_TYPES)}",
            activity_type,
        )

    title = activity.get("title")
    if not isinstance(title, str) or len(title) < _TITLE_MIN or len(title) > _TITLE_MAX:
        _raise(
            "activity.title must be a non-empty string of 1-255 chars",
            f"{path}.title",
            f"non-empty string ({_TITLE_MIN}-{_TITLE_MAX} chars)",
            title,
        )

    description = activity.get("description")
    if (not isinstance(description, str)
            or len(description) < _DESC_MIN
            or len(description) > _DESC_MAX):
        _raise(
            "activity.description must be a non-empty string of 1-255 chars",
            f"{path}.description",
            f"non-empty string ({_DESC_MIN}-{_DESC_MAX} chars)",
            description,
        )

    data = activity.get("data")
    if not isinstance(data, dict):
        _raise(
            "activity.data must be a dict",
            f"{path}.data",
            "dict",
            type(data).__name__ if data is not None else "missing",
        )

    return activity_type, title, description, data


def _check_activity_title_description_conventions(
    activity_type: str,
    title: str,
    description: str,
    data: dict,
    path: str,
) -> None:
    """Check 10: per-type title/description conventions from Req 9.8."""

    if activity_type in {"viewFlashcards", "speakFlashcards",
                         "vocabLevel1", "vocabLevel2"}:
        # title = "Flashcards: <topic>"
        if not title.startswith("Flashcards: "):
            _raise(
                f"{activity_type}.title must start with 'Flashcards: '",
                f"{path}.title",
                "starts with 'Flashcards: '",
                title,
            )
        topic = title[len("Flashcards: "):].strip()
        if not topic:
            _raise(
                f"{activity_type}.title topic is empty after 'Flashcards: '",
                f"{path}.title",
                "non-empty topic after prefix",
                title,
            )
        # description = "Học N từ: w1, w2, ..."
        vocab_list = data.get("vocabList", [])
        if isinstance(vocab_list, list) and all(isinstance(w, str) for w in vocab_list):
            expected_desc = f"Học {len(vocab_list)} từ: " + ", ".join(vocab_list)
            if description != expected_desc:
                _raise(
                    f"{activity_type}.description must follow Req 9.8 convention",
                    f"{path}.description",
                    expected_desc,
                    description,
                )

    elif activity_type in {"reading", "speakReading"}:
        # title = "Đọc: <topic>"
        if not title.startswith("Đọc: "):
            _raise(
                f"{activity_type}.title must start with 'Đọc: '",
                f"{path}.title",
                "starts with 'Đọc: '",
                title,
            )
        topic = title[len("Đọc: "):].strip()
        if not topic:
            _raise(
                f"{activity_type}.title topic is empty after 'Đọc: '",
                f"{path}.title",
                "non-empty topic after prefix",
                title,
            )
        # description = first 80 chars of data.text (no ellipsis appended;
        # if shorter than 80 chars, the full text is used).
        text = data.get("text")
        if isinstance(text, str) and text:
            expected_desc = text[:80]
            if description != expected_desc:
                _raise(
                    f"{activity_type}.description must equal first 80 chars of data.text",
                    f"{path}.description",
                    expected_desc,
                    description,
                )

    elif activity_type == "readAlong":
        # title = "Nghe: <topic>"
        if not title.startswith("Nghe: "):
            _raise(
                "readAlong.title must start with 'Nghe: '",
                f"{path}.title",
                "starts with 'Nghe: '",
                title,
            )
        topic = title[len("Nghe: "):].strip()
        if not topic:
            _raise(
                "readAlong.title topic is empty after 'Nghe: '",
                f"{path}.title",
                "non-empty topic after prefix",
                title,
            )
        # description fixed string per Req 9.8
        expected_desc = "Nghe đoạn văn vừa đọc và theo dõi."
        if description != expected_desc:
            _raise(
                "readAlong.description must follow Req 9.8 convention",
                f"{path}.description",
                expected_desc,
                description,
            )

    elif activity_type == "introAudio":
        # title length 5-60 chars
        if len(title) < _INTRO_TITLE_MIN or len(title) > _INTRO_TITLE_MAX:
            _raise(
                "introAudio.title length out of bounds",
                f"{path}.title",
                f"{_INTRO_TITLE_MIN}-{_INTRO_TITLE_MAX} chars",
                f"{len(title)} chars",
            )
        # description 20-200 chars
        if (len(description) < _INTRO_DESC_MIN
                or len(description) > _INTRO_DESC_MAX):
            _raise(
                "introAudio.description length out of bounds",
                f"{path}.description",
                f"{_INTRO_DESC_MIN}-{_INTRO_DESC_MAX} chars",
                f"{len(description)} chars",
            )

    elif activity_type in {"writingSentence", "writingParagraph"}:
        # title = "Viết: <topic>"
        if not title.startswith("Viết: "):
            _raise(
                f"{activity_type}.title must start with 'Viết: '",
                f"{path}.title",
                "starts with 'Viết: '",
                title,
            )
        topic = title[len("Viết: "):].strip()
        if not topic:
            _raise(
                f"{activity_type}.title topic is empty after 'Viết: '",
                f"{path}.title",
                "non-empty topic after prefix",
                title,
            )
        # description 20-200 chars
        if (len(description) < _WRITING_DESC_MIN
                or len(description) > _WRITING_DESC_MAX):
            _raise(
                f"{activity_type}.description length out of bounds",
                f"{path}.description",
                f"{_WRITING_DESC_MIN}-{_WRITING_DESC_MAX} chars",
                f"{len(description)} chars",
            )


# ---------------------------------------------------------------------------
# vocabList shape (11)
# ---------------------------------------------------------------------------

def _check_vocab_list_shape(data: dict, activity_type: str, path: str) -> list[str]:
    """Check 11: vocabList is array of lowercase strings (1-64 chars each, 1-20 items);
    never named 'words'. Returns the validated vocabList.
    """
    if "words" in data:
        _raise(
            "vocab field must be named 'vocabList', not 'words'",
            f"{path}.words",
            "no 'words' field",
            data["words"],
        )

    vocab_list = data.get("vocabList")
    if not isinstance(vocab_list, list):
        _raise(
            f"{activity_type}.data.vocabList must be a list",
            f"{path}.vocabList",
            "list",
            type(vocab_list).__name__ if vocab_list is not None else "missing",
        )
    if len(vocab_list) < _VOCAB_LIST_MIN or len(vocab_list) > _VOCAB_LIST_MAX:
        _raise(
            f"{activity_type}.data.vocabList length out of bounds",
            f"{path}.vocabList",
            f"{_VOCAB_LIST_MIN}-{_VOCAB_LIST_MAX} items",
            f"{len(vocab_list)} items",
        )

    for j, word in enumerate(vocab_list):
        wpath = f"{path}.vocabList[{j}]"
        if not isinstance(word, str):
            _raise(
                "vocabList entry must be a string",
                wpath,
                "str",
                type(word).__name__,
            )
        if len(word) < _VOCAB_WORD_MIN or len(word) > _VOCAB_WORD_MAX:
            _raise(
                "vocabList entry length out of bounds",
                wpath,
                f"{_VOCAB_WORD_MIN}-{_VOCAB_WORD_MAX} chars",
                f"{len(word)} chars",
            )
        if word != word.lower():
            _raise(
                "vocabList entry must be lowercase",
                wpath,
                word.lower(),
                word,
            )

    return vocab_list


# ---------------------------------------------------------------------------
# Per-session vocab consistency (12) and per-session vocab group (13)
# ---------------------------------------------------------------------------

def _check_session_vocab_consistency(sessions: list[dict]) -> list[list[str]]:
    """Check 12: viewFlashcards / speakFlashcards / vocabLevel1 in the same session
    share an identical data.vocabList (same order).

    Returns the Session_Vocab_Group list (length 4) for downstream Check 13/14.
    """
    session_vocab_groups: list[list[str]] = []

    for i, session in enumerate(sessions):
        ref_vocab: list[str] | None = None
        ref_path: str | None = None
        for j, activity in enumerate(session.get("activities", [])):
            if not isinstance(activity, dict):
                continue
            at = activity.get("activityType")
            if at not in _SESSION_VOCAB_TYPES:
                continue
            data = activity.get("data") or {}
            if not isinstance(data, dict):
                continue
            vlist = data.get("vocabList")
            if not isinstance(vlist, list):
                continue
            cur_path = f"learningSessions[{i}].activities[{j}].data.vocabList"
            if ref_vocab is None:
                ref_vocab = list(vlist)
                ref_path = cur_path
            elif list(vlist) != ref_vocab:
                _raise(
                    f"vocabList mismatch within session {i} "
                    f"between {at} and earlier session-vocab activity",
                    cur_path,
                    f"{ref_vocab} (from {ref_path})",
                    list(vlist),
                )

        if ref_vocab is None:
            # Should never happen if Check 8 passed (templates always include
            # at least viewFlashcards + speakFlashcards in every session), but
            # guard anyway so the property holds independently.
            _raise(
                f"session {i} is missing a Session_Vocab_Group",
                f"learningSessions[{i}]",
                "at least one of viewFlashcards/speakFlashcards/vocabLevel1",
                "none found",
            )

        session_vocab_groups.append(ref_vocab)

    return session_vocab_groups


def _check_session_vocab_group_size(session_vocab_groups: list[list[str]]) -> None:
    """Check 13: each Session_Vocab_Group has exactly 5 unique words."""
    for i, group in enumerate(session_vocab_groups):
        unique = set(group)
        if len(group) != 5 or len(unique) != 5:
            _raise(
                f"Session_Vocab_Group must have exactly 5 unique words",
                f"learningSessions[{i}] (Session_Vocab_Group)",
                "5 unique words",
                f"{len(group)} entries, {len(unique)} unique: {group}",
            )


def _check_curriculum_vocab_total(session_vocab_groups: list[list[str]]) -> None:
    """Check 14: union of 4 Session_Vocab_Groups has exactly 20 unique words."""
    union: set[str] = set()
    for group in session_vocab_groups:
        union.update(group)
    total_entries = sum(len(g) for g in session_vocab_groups)
    if total_entries != 20 or len(union) != 20:
        _raise(
            "union of 4 Session_Vocab_Groups must have exactly 20 unique words",
            "learningSessions[*] (Session_Vocab_Groups union)",
            "20 unique words across 4 sessions of 5",
            f"{total_entries} total entries, {len(union)} unique",
        )


# ---------------------------------------------------------------------------
# Reading-text presence (15), writingSentence (16), writingParagraph (17)
# ---------------------------------------------------------------------------

def _check_reading_text_present(activity_type: str, data: dict, path: str) -> None:
    """Check 15: reading / speakReading / readAlong have non-empty data.text."""
    if activity_type in {"reading", "speakReading", "readAlong"}:
        text = data.get("text")
        if not isinstance(text, str) or not text.strip():
            _raise(
                f"{activity_type}.data.text must be a non-empty string",
                f"{path}.text",
                "non-empty string",
                text,
            )


def _check_intro_audio_text_present(activity_type: str, data: dict, path: str) -> None:
    """Required for Check 19 — introAudio.data.text non-empty string."""
    if activity_type == "introAudio":
        text = data.get("text")
        if not isinstance(text, str) or not text.strip():
            _raise(
                "introAudio.data.text must be a non-empty string",
                f"{path}.text",
                "non-empty string",
                text,
            )


def _check_writing_sentence(data: dict, path: str) -> None:
    """Check 16: writingSentence has data.vocabList, data.items (1-10), each item
    has non-empty prompt (1-500) and targetVocab (1-64) where targetVocab ∈ data.vocabList.
    """
    vocab_list = data.get("vocabList")
    if not isinstance(vocab_list, list) or not vocab_list:
        _raise(
            "writingSentence.data.vocabList must be a non-empty list",
            f"{path}.vocabList",
            "non-empty list",
            vocab_list,
        )

    items = data.get("items")
    if not isinstance(items, list):
        _raise(
            "writingSentence.data.items must be a list",
            f"{path}.items",
            "list",
            type(items).__name__ if items is not None else "missing",
        )
    if (len(items) < _WRITING_SENT_ITEMS_MIN
            or len(items) > _WRITING_SENT_ITEMS_MAX):
        _raise(
            "writingSentence.data.items length out of bounds",
            f"{path}.items",
            f"{_WRITING_SENT_ITEMS_MIN}-{_WRITING_SENT_ITEMS_MAX} items",
            f"{len(items)} items",
        )

    for k, item in enumerate(items):
        ipath = f"{path}.items[{k}]"
        if not isinstance(item, dict):
            _raise(
                "writingSentence item must be an object",
                ipath,
                "dict",
                type(item).__name__,
            )

        prompt = item.get("prompt")
        if (not isinstance(prompt, str)
                or len(prompt) < _WRITING_PROMPT_MIN
                or len(prompt) > _WRITING_PROMPT_MAX):
            _raise(
                "writingSentence item.prompt out of bounds",
                f"{ipath}.prompt",
                f"non-empty string ({_WRITING_PROMPT_MIN}-{_WRITING_PROMPT_MAX} chars)",
                prompt,
            )

        target = item.get("targetVocab")
        if (not isinstance(target, str)
                or len(target) < _VOCAB_WORD_MIN
                or len(target) > _VOCAB_WORD_MAX):
            _raise(
                "writingSentence item.targetVocab out of bounds",
                f"{ipath}.targetVocab",
                f"non-empty string ({_VOCAB_WORD_MIN}-{_VOCAB_WORD_MAX} chars)",
                target,
            )
        if target not in vocab_list:
            _raise(
                "writingSentence item.targetVocab must be in data.vocabList",
                f"{ipath}.targetVocab",
                f"one of {vocab_list}",
                target,
            )


def _check_writing_paragraph(data: dict, path: str) -> None:
    """Check 17: writingParagraph has data.vocabList, data.instructions (1-1000),
    data.prompts (2-10 non-empty strings, each 1-500).
    """
    vocab_list = data.get("vocabList")
    if not isinstance(vocab_list, list) or not vocab_list:
        _raise(
            "writingParagraph.data.vocabList must be a non-empty list",
            f"{path}.vocabList",
            "non-empty list",
            vocab_list,
        )

    instructions = data.get("instructions")
    if (not isinstance(instructions, str)
            or len(instructions) < _WRITING_INSTR_MIN
            or len(instructions) > _WRITING_INSTR_MAX):
        _raise(
            "writingParagraph.data.instructions out of bounds",
            f"{path}.instructions",
            f"non-empty string ({_WRITING_INSTR_MIN}-{_WRITING_INSTR_MAX} chars)",
            instructions,
        )

    prompts = data.get("prompts")
    if not isinstance(prompts, list):
        _raise(
            "writingParagraph.data.prompts must be a list",
            f"{path}.prompts",
            "list",
            type(prompts).__name__ if prompts is not None else "missing",
        )
    if (len(prompts) < _WRITING_PARA_PROMPTS_MIN
            or len(prompts) > _WRITING_PARA_PROMPTS_MAX):
        _raise(
            "writingParagraph.data.prompts length out of bounds",
            f"{path}.prompts",
            f"{_WRITING_PARA_PROMPTS_MIN}-{_WRITING_PARA_PROMPTS_MAX} prompts",
            f"{len(prompts)} prompts",
        )
    for k, p in enumerate(prompts):
        ppath = f"{path}.prompts[{k}]"
        if (not isinstance(p, str)
                or len(p) < _WRITING_PROMPT_MIN
                or len(p) > _WRITING_PROMPT_MAX):
            _raise(
                "writingParagraph prompt out of bounds",
                ppath,
                f"non-empty string ({_WRITING_PROMPT_MIN}-{_WRITING_PROMPT_MAX} chars)",
                p,
            )


# ---------------------------------------------------------------------------
# Strip-keys recursive scan (18)
# ---------------------------------------------------------------------------

def _check_no_strip_keys(obj: Any, path: str) -> None:
    """Check 18: recursive scan rejects any STRIP_KEYS element anywhere in the JSON tree."""
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key in STRIP_KEYS:
                _raise(
                    f"strip-key '{key}' found in content",
                    f"{path}.{key}",
                    f"no key from STRIP_KEYS ({sorted(STRIP_KEYS)})",
                    key,
                )
            _check_no_strip_keys(value, f"{path}.{key}")
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            _check_no_strip_keys(item, f"{path}[{i}]")


# ---------------------------------------------------------------------------
# introAudio word-count check (19)
# ---------------------------------------------------------------------------

def _whitespace_token_count(text: str) -> int:
    """Count whitespace-separated tokens in text."""
    return len(text.split())


def _check_intro_audio_word_counts(sessions: list[dict]) -> None:
    """Check 19: introAudio whitespace-token counts.

    Roles (based on the activity templates which always start and end each session
    with an introAudio):
      - welcome: first introAudio of session 1 — 500-800 tokens
      - mid-session wrap-ups/recaps:
          last introAudio of sessions 1-3, first introAudio of sessions 2-3 — 200-400 tokens
      - farewell: last introAudio of session 4 — 400-600 tokens
    """
    # Collect (path, text, tokens, role) for the relevant introAudios.
    def _intro_audios_in(session_idx: int) -> list[tuple[int, dict]]:
        """Return list of (activity_idx, activity_dict) for introAudios in session_idx."""
        out: list[tuple[int, dict]] = []
        session = sessions[session_idx]
        for j, activity in enumerate(session.get("activities", [])):
            if (isinstance(activity, dict)
                    and activity.get("activityType") == "introAudio"):
                out.append((j, activity))
        return out

    def _check_role(session_idx: int, activity_idx: int, activity: dict,
                    role: str, lo: int, hi: int) -> None:
        data = activity.get("data") or {}
        text = data.get("text", "") if isinstance(data, dict) else ""
        if not isinstance(text, str):
            text = ""
        tokens = _whitespace_token_count(text)
        if tokens < lo or tokens > hi:
            _raise(
                f"introAudio word count out of bounds for role '{role}'",
                f"learningSessions[{session_idx}].activities[{activity_idx}].data.text",
                f"{lo}-{hi} whitespace tokens",
                f"{tokens} tokens",
            )

    # Session 1: welcome = first introAudio, wrap-up = last introAudio.
    s1_intros = _intro_audios_in(0)
    if s1_intros:
        first_idx, first_act = s1_intros[0]
        _check_role(0, first_idx, first_act, "welcome",
                    *_WELCOME_TOKEN_BOUNDS)
        last_idx, last_act = s1_intros[-1]
        if last_idx != first_idx:
            _check_role(0, last_idx, last_act, "session 1 wrap-up",
                        *_MID_TOKEN_BOUNDS)

    # Sessions 2-3: first introAudio = recap, last introAudio = wrap-up; both 200-400.
    for s in (1, 2):
        intros = _intro_audios_in(s)
        if intros:
            first_idx, first_act = intros[0]
            _check_role(s, first_idx, first_act, f"session {s + 1} recap",
                        *_MID_TOKEN_BOUNDS)
            last_idx, last_act = intros[-1]
            if last_idx != first_idx:
                _check_role(s, last_idx, last_act, f"session {s + 1} wrap-up",
                            *_MID_TOKEN_BOUNDS)

    # Session 4: last introAudio = farewell, 400-600 tokens.
    s4_intros = _intro_audios_in(3)
    if s4_intros:
        last_idx, last_act = s4_intros[-1]
        _check_role(3, last_idx, last_act, "farewell",
                    *_FAREWELL_TOKEN_BOUNDS)


# ---------------------------------------------------------------------------
# Average sentence length (20)
# ---------------------------------------------------------------------------

_SENTENCE_TERMINATORS = (".", "!", "?")


def _count_sentences(text: str) -> int:
    """Count sentence terminators (., !, ?) in text. Returns at least 1 for non-empty text."""
    n = sum(text.count(t) for t in _SENTENCE_TERMINATORS)
    return max(n, 1)


def _check_average_sentence_length(sessions: list[dict], level: str) -> None:
    """Check 20: when level is provided, average sentence length across union of all
    `reading` + `speakReading` data.text is within 10-14 (preintermediate) or 12-18 (intermediate).
    """
    bounds = _SENTENCE_LENGTH_BOUNDS[level]
    lo, hi = bounds

    total_tokens = 0
    total_sentences = 0
    paths: list[str] = []

    for i, session in enumerate(sessions):
        for j, activity in enumerate(session.get("activities", [])):
            if not isinstance(activity, dict):
                continue
            at = activity.get("activityType")
            if at not in {"reading", "speakReading"}:
                continue
            data = activity.get("data") or {}
            if not isinstance(data, dict):
                continue
            text = data.get("text", "")
            if not isinstance(text, str) or not text.strip():
                continue
            total_tokens += _whitespace_token_count(text)
            total_sentences += _count_sentences(text)
            paths.append(f"learningSessions[{i}].activities[{j}].data.text")

    if total_sentences == 0:
        # Cannot compute average; treat as a violation since reading passages
        # are mandatory for the formats covered by this spec.
        _raise(
            "no reading/speakReading text found to compute average sentence length",
            "learningSessions[*].activities[*].data.text",
            "at least one non-empty reading/speakReading passage",
            "none",
        )

    avg = total_tokens / total_sentences
    if avg < lo or avg > hi:
        _raise(
            f"average sentence length out of bounds for level '{level}'",
            "(union of reading + speakReading data.text)",
            f"{lo}-{hi} words/sentence",
            f"{avg:.2f} words/sentence (tokens={total_tokens}, sentences={total_sentences})",
        )


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------

def validate(content: dict, fmt: str, level: str | None = None) -> None:
    """Validate curriculum content for the vi-en Digital Economy spec.

    Args:
        content: Full curriculum content dict (top-level title, description,
                 preview, contentTypeTags, learningSessions).
        fmt: One of "story_reading", "speaking", "balanced".
        level: One of "preintermediate", "intermediate", or None
               (skip the average-sentence-length check).

    Raises:
        ValueError describing the rule violated, the JSON path of the offending
        value, and the expected vs actual values.
    """
    # Argument validation (programmer error, not a content-corruption rule)
    if fmt not in VALID_FORMATS:
        raise ValueError(
            f"[bad argument] fmt must be one of {sorted(VALID_FORMATS)}, "
            f"got {fmt!r}"
        )
    if level is not None and level not in VALID_LEVELS:
        raise ValueError(
            f"[bad argument] level must be one of {sorted(VALID_LEVELS)} or None, "
            f"got {level!r}"
        )

    # Check 1: content is a dict
    _check_is_dict(content)

    # Checks 2-4: title, description, preview.text
    _check_required_strings(content)

    # Check 5: contentTypeTags == CONTENT_TYPE_TAGS[fmt]
    _check_content_type_tags(content, fmt)

    # Check 6: learningSessions list of exactly 4 elements
    sessions = _check_learning_sessions_shape(content)

    # Check 7: each session has non-empty title (5-150), unique, non-empty activities
    _check_session_titles_and_activities(sessions)

    # Check 8: activity-type sequence matches ACTIVITY_TEMPLATES[fmt][i]
    _check_activity_sequence(sessions, fmt)

    # Checks 9, 10, 11, 15, 16, 17 — per-activity checks
    for i, session in enumerate(sessions):
        for j, activity in enumerate(session.get("activities", [])):
            apath = f"learningSessions[{i}].activities[{j}]"
            activity_type, title, description, data = _check_activity_shape(
                activity, apath
            )
            _check_activity_title_description_conventions(
                activity_type, title, description, data, apath
            )

            # Check 11: vocabList shape (only for activities that carry a vocabList).
            if activity_type in _VOCAB_LIST_TYPES:
                _check_vocab_list_shape(data, activity_type, f"{apath}.data")

            # Check 15: reading/speakReading/readAlong text presence.
            _check_reading_text_present(activity_type, data, f"{apath}.data")

            # Required for Check 19: introAudio text presence.
            _check_intro_audio_text_present(activity_type, data, f"{apath}.data")

            # Check 16: writingSentence shape.
            if activity_type == "writingSentence":
                _check_writing_sentence(data, f"{apath}.data")

            # Check 17: writingParagraph shape.
            if activity_type == "writingParagraph":
                _check_writing_paragraph(data, f"{apath}.data")

    # Check 12: viewFlashcards / speakFlashcards / vocabLevel1 share an identical
    # data.vocabList per session. Returns the 4 Session_Vocab_Groups.
    session_vocab_groups = _check_session_vocab_consistency(sessions)

    # Check 13: each Session_Vocab_Group has exactly 5 unique words
    _check_session_vocab_group_size(session_vocab_groups)

    # Check 14: union of 4 Session_Vocab_Groups has exactly 20 unique words
    _check_curriculum_vocab_total(session_vocab_groups)

    # Check 18: recursive scan rejects any STRIP_KEYS element anywhere in the tree
    _check_no_strip_keys(content, "content")

    # Check 19: introAudio whitespace-token counts by role
    _check_intro_audio_word_counts(sessions)

    # Check 20: average sentence length matches level bounds (skip if level is None)
    if level is not None:
        _check_average_sentence_length(sessions, level)
