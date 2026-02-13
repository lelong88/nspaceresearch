from pathlib import Path
from typing import Callable


def get_summary_output_path(transcript_path: Path) -> Path:
    """Given transcript path like project/transcripts/foo.txt, return project/summaries/foo.md."""
    project_dir = transcript_path.parent.parent
    return project_dir / "summaries" / (transcript_path.stem + ".md")


def get_unsummarized_transcripts(project_dir: Path) -> list[Path]:
    """Return sorted list of transcript files in project_dir/transcripts/ that lack a corresponding summary."""
    transcripts_dir = project_dir / "transcripts"
    if not transcripts_dir.exists():
        return []

    summaries_dir = project_dir / "summaries"
    existing_stems: set[str] = set()
    if summaries_dir.exists():
        existing_stems = {f.stem for f in summaries_dir.iterdir() if f.suffix == ".md"}

    return [
        f for f in sorted(transcripts_dir.iterdir())
        if f.is_file() and f.suffix == ".txt" and f.stem not in existing_stems
    ]


def summarize_transcript(transcript_path: Path, on_progress: Callable[[str], None]) -> str:
    """Summarize a transcript file and save the result. Returns the summary text."""
    import summarize_meetings

    name = transcript_path.stem
    on_progress(f"Starting summarization for {name}")

    text = transcript_path.read_text()
    on_progress(f"Calling LLM API for {name}...")
    summary = summarize_meetings.summarize(text)

    output_path = get_summary_output_path(transcript_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(summary)

    on_progress(f"Summarization complete for {name} ({len(summary)} chars)")
    return summary
