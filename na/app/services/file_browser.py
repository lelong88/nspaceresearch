from pathlib import Path

from app.models import ALLOWED_EXTENSIONS, ProjectDetail, ProjectInfo


def _validate_path(base_dir: Path, *parts: str) -> Path:
    """Resolve a path and ensure it stays within base_dir."""
    resolved = (base_dir / Path(*parts)).resolve()
    if not str(resolved).startswith(str(base_dir.resolve())):
        raise ValueError("Path traversal detected")
    return resolved


def list_projects(base_dir: Path) -> list[ProjectInfo]:
    """Scan base_dir for subdirectories and count files in each."""
    if not base_dir.is_dir():
        return []

    projects = []
    for entry in sorted(base_dir.iterdir()):
        if not entry.is_dir():
            continue

        transcripts_dir = entry / "transcripts"
        summaries_dir = entry / "summaries"
        files_dir = entry / "files"

        transcript_count = len(list(transcripts_dir.iterdir())) if transcripts_dir.is_dir() else 0
        summary_count = len(list(summaries_dir.iterdir())) if summaries_dir.is_dir() else 0
        audio_count = (
            sum(1 for f in files_dir.iterdir() if f.suffix.lower() in ALLOWED_EXTENSIONS)
            if files_dir.is_dir()
            else 0
        )

        projects.append(ProjectInfo(
            name=entry.name,
            transcript_count=transcript_count,
            summary_count=summary_count,
            audio_count=audio_count,
        ))

    return projects


def list_project_files(base_dir: Path, project: str) -> ProjectDetail:
    """Return filenames from summaries/ and transcripts/ only."""
    project_dir = _validate_path(base_dir, project)
    if not project_dir.is_dir():
        raise FileNotFoundError(f"Project not found: {project}")

    transcripts_dir = project_dir / "transcripts"
    summaries_dir = project_dir / "summaries"

    transcripts = sorted(f.name for f in transcripts_dir.iterdir()) if transcripts_dir.is_dir() else []
    summaries = sorted(f.name for f in summaries_dir.iterdir()) if summaries_dir.is_dir() else []

    return ProjectDetail(name=project, transcripts=transcripts, summaries=summaries)


def read_transcript(base_dir: Path, project: str, filename: str) -> str:
    """Read transcript file content with path validation."""
    file_path = _validate_path(base_dir, project, "transcripts", filename)
    if not file_path.is_file():
        raise FileNotFoundError(f"Transcript not found: {filename}")
    return file_path.read_text(encoding="utf-8")


def read_summary(base_dir: Path, project: str, filename: str) -> str:
    """Read summary file content with path validation."""
    file_path = _validate_path(base_dir, project, "summaries", filename)
    if not file_path.is_file():
        raise FileNotFoundError(f"Summary not found: {filename}")
    return file_path.read_text(encoding="utf-8")
