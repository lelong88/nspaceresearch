from pathlib import Path
from typing import Callable

from app.models import ALLOWED_EXTENSIONS


def get_transcript_output_path(audio_path: Path) -> Path:
    """Given audio file path like project/files/foo.m4a, return project/transcripts/foo.txt."""
    project_dir = audio_path.parent.parent
    return project_dir / "transcripts" / (audio_path.stem + ".txt")


def get_untranscribed_files(project_dir: Path) -> list[Path]:
    """Return sorted list of audio files in project_dir/files/ that lack a corresponding transcript."""
    audio_dir = project_dir / "files"
    if not audio_dir.exists():
        return []

    transcripts_dir = project_dir / "transcripts"
    existing_stems: set[str] = set()
    if transcripts_dir.exists():
        existing_stems = {f.stem for f in transcripts_dir.iterdir() if f.suffix == ".txt"}

    untranscribed = [
        f for f in sorted(audio_dir.iterdir())
        if f.is_file() and f.suffix.lower() in ALLOWED_EXTENSIONS and f.stem not in existing_stems
    ]
    return untranscribed


def transcribe_file(audio_path: Path, on_progress: Callable[[str], None]) -> str:
    """Transcribe an audio file and save the result. Returns the transcript text."""
    import transcribe_meetings

    name = audio_path.stem
    on_progress(f"Starting transcription for {name}")

    on_progress(f"Uploading {name} to Soniox API...")
    text = transcribe_meetings.transcribe(audio_path)

    output_path = get_transcript_output_path(audio_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text)

    on_progress(f"Transcription complete for {name} ({len(text)} chars)")
    return text
