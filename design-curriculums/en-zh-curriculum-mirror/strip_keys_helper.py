"""Shared strip_keys utility for en-zh curriculum mirror scripts.

Recursively removes auto-generated platform keys from nested dict/list structures.
Import this in any creation script:

    from strip_keys_helper import strip_keys, STRIP_KEYS
"""

STRIP_KEYS = {
    "mp3Url", "illustrationSet", "chapterBookmarks", "segments",
    "whiteboardItems", "userReadingId", "lessonUniqueId",
    "curriculumTags", "taskId", "imageId",
}


def strip_keys(obj):
    """Remove all STRIP_KEYS from obj at every nesting level."""
    if isinstance(obj, dict):
        return {k: strip_keys(v) for k, v in obj.items() if k not in STRIP_KEYS}
    if isinstance(obj, list):
        return [strip_keys(item) for item in obj]
    return obj
