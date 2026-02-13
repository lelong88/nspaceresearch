from pathlib import Path

from app.models import ALLOWED_EXTENSIONS


def validate_extension(filename: str) -> bool:
    """Return True if the file extension (lowercased) is in ALLOWED_EXTENSIONS."""
    return Path(filename).suffix.lower() in ALLOWED_EXTENSIONS


def validate_folder_name(name: str) -> bool:
    """Return False if name is empty or contains path traversal characters."""
    if not name:
        return False
    if ".." in name or "/" in name or "\\" in name:
        return False
    return True


def save_upload(base_dir: Path, project: str, filename: str, content: bytes) -> Path:
    """Validate inputs, create project dirs, save file, return saved path."""
    if not validate_folder_name(project):
        raise ValueError(f"Invalid folder name: {project}")
    if not validate_extension(filename):
        raise ValueError(f"Unsupported file extension: {filename}")

    project_dir = base_dir / project
    for subdir in ("files", "transcripts", "summaries"):
        (project_dir / subdir).mkdir(parents=True, exist_ok=True)

    dest = project_dir / "files" / filename
    dest.write_bytes(content)
    return dest
