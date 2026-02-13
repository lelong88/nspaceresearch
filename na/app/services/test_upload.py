from pathlib import Path

import pytest

from app.services.upload import save_upload, validate_extension, validate_folder_name


# --- validate_extension ---

@pytest.mark.parametrize("filename,expected", [
    ("meeting.m4a", True),
    ("meeting.MP3", True),
    ("meeting.Mp4", True),
    ("meeting.wav", True),
    ("meeting.flac", True),
    ("meeting.ogg", True),
    ("meeting.aac", True),
    ("meeting.webm", True),
    ("meeting.amr", True),
    ("meeting.aiff", True),
    ("meeting.asf", True),
    ("notes.txt", False),
    ("image.png", False),
    ("archive.zip", False),
    ("noext", False),
    ("", False),
])
def test_validate_extension(filename: str, expected: bool):
    assert validate_extension(filename) is expected


# --- validate_folder_name ---

@pytest.mark.parametrize("name,expected", [
    ("my-project", True),
    ("project_2024", True),
    ("simple", True),
    ("", False),
    ("..", False),
    ("foo/../bar", False),
    ("foo/bar", False),
    ("foo\\bar", False),
    ("..hidden", False),
])
def test_validate_folder_name(name: str, expected: bool):
    assert validate_folder_name(name) is expected


# --- save_upload ---

def test_save_upload_creates_dirs_and_file(tmp_path: Path):
    result = save_upload(tmp_path, "proj", "call.mp3", b"audio-data")

    assert result == tmp_path / "proj" / "files" / "call.mp3"
    assert result.read_bytes() == b"audio-data"
    assert (tmp_path / "proj" / "transcripts").is_dir()
    assert (tmp_path / "proj" / "summaries").is_dir()


def test_save_upload_existing_project(tmp_path: Path):
    (tmp_path / "proj" / "files").mkdir(parents=True)
    result = save_upload(tmp_path, "proj", "call.wav", b"data")
    assert result.is_file()


def test_save_upload_rejects_bad_extension(tmp_path: Path):
    with pytest.raises(ValueError, match="Unsupported file extension"):
        save_upload(tmp_path, "proj", "notes.txt", b"data")


def test_save_upload_rejects_bad_folder(tmp_path: Path):
    with pytest.raises(ValueError, match="Invalid folder name"):
        save_upload(tmp_path, "../evil", "call.mp3", b"data")


def test_save_upload_rejects_empty_folder(tmp_path: Path):
    with pytest.raises(ValueError, match="Invalid folder name"):
        save_upload(tmp_path, "", "call.mp3", b"data")
