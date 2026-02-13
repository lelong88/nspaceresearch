import tempfile
from pathlib import Path

import pytest

from app.services.file_browser import (
    list_project_files,
    list_projects,
    read_summary,
    read_transcript,
)


@pytest.fixture
def base_dir(tmp_path: Path) -> Path:
    # Create two projects with varying content
    for proj in ["alpha", "beta"]:
        (tmp_path / proj / "files").mkdir(parents=True)
        (tmp_path / proj / "transcripts").mkdir(parents=True)
        (tmp_path / proj / "summaries").mkdir(parents=True)
        (tmp_path / proj / "images").mkdir(parents=True)

    # alpha: 1 audio, 1 transcript, 1 summary, 1 image
    (tmp_path / "alpha" / "files" / "meeting.m4a").write_bytes(b"audio")
    (tmp_path / "alpha" / "transcripts" / "meeting.txt").write_text("hello world")
    (tmp_path / "alpha" / "summaries" / "meeting.md").write_text("# Summary")
    (tmp_path / "alpha" / "images" / "pic.png").write_bytes(b"img")

    # beta: 2 audio, 0 transcripts, 0 summaries
    (tmp_path / "beta" / "files" / "call1.mp3").write_bytes(b"a")
    (tmp_path / "beta" / "files" / "call2.wav").write_bytes(b"b")
    # also a non-audio file in files/
    (tmp_path / "beta" / "files" / "notes.txt").write_text("not audio")

    return tmp_path


def test_list_projects(base_dir: Path):
    projects = list_projects(base_dir)
    assert len(projects) == 2
    assert projects[0].name == "alpha"
    assert projects[0].transcript_count == 1
    assert projects[0].summary_count == 1
    assert projects[0].audio_count == 1
    assert projects[1].name == "beta"
    assert projects[1].audio_count == 2  # notes.txt excluded


def test_list_projects_empty(tmp_path: Path):
    assert list_projects(tmp_path) == []


def test_list_projects_nonexistent(tmp_path: Path):
    assert list_projects(tmp_path / "nope") == []


def test_list_project_files_excludes_files_and_images(base_dir: Path):
    detail = list_project_files(base_dir, "alpha")
    assert detail.name == "alpha"
    assert detail.transcripts == ["meeting.txt"]
    assert detail.summaries == ["meeting.md"]


def test_list_project_files_not_found(base_dir: Path):
    with pytest.raises(FileNotFoundError):
        list_project_files(base_dir, "nonexistent")


def test_read_transcript(base_dir: Path):
    content = read_transcript(base_dir, "alpha", "meeting.txt")
    assert content == "hello world"


def test_read_transcript_not_found(base_dir: Path):
    with pytest.raises(FileNotFoundError):
        read_transcript(base_dir, "alpha", "nope.txt")


def test_read_summary(base_dir: Path):
    content = read_summary(base_dir, "alpha", "meeting.md")
    assert content == "# Summary"


def test_read_summary_not_found(base_dir: Path):
    with pytest.raises(FileNotFoundError):
        read_summary(base_dir, "alpha", "nope.md")


def test_path_traversal_read_transcript(base_dir: Path):
    with pytest.raises((FileNotFoundError, ValueError)):
        read_transcript(base_dir, "..", "etc/passwd")


def test_path_traversal_read_summary(base_dir: Path):
    with pytest.raises((FileNotFoundError, ValueError)):
        read_summary(base_dir, "..", "etc/passwd")


def test_path_traversal_list_project_files(base_dir: Path):
    with pytest.raises((FileNotFoundError, ValueError)):
        list_project_files(base_dir, "../..")
