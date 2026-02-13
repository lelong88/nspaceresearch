import asyncio
from collections.abc import AsyncGenerator
from pathlib import Path

from app.models import PipelineEvent
from app.services.transcription import get_untranscribed_files, transcribe_file
from app.services.summarization import get_unsummarized_transcripts, summarize_transcript


async def run_pipeline(project: str, base_dir: Path) -> AsyncGenerator[PipelineEvent, None]:
    """Run the transcription → summarization pipeline for a project, yielding progress events."""
    project_dir = base_dir / project

    if not project_dir.exists():
        yield PipelineEvent(event_type="error", message=f"Project directory not found: {project}")
        return

    # --- Transcription phase ---
    untranscribed = get_untranscribed_files(project_dir)
    if untranscribed:
        yield PipelineEvent(
            event_type="progress",
            message=f"Found {len(untranscribed)} file(s) to transcribe",
            step="transcription",
        )

    for audio_path in untranscribed:
        name = audio_path.name
        yield PipelineEvent(
            event_type="progress",
            message=f"Transcribing {name}...",
            file_name=name,
            step="transcription",
        )
        try:
            await asyncio.to_thread(transcribe_file, audio_path, lambda msg: None)
        except Exception as exc:
            yield PipelineEvent(
                event_type="error",
                message=f"Transcription failed for {name}: {exc}",
                file_name=name,
                step="transcription",
            )
            continue
        yield PipelineEvent(
            event_type="progress",
            message=f"Transcription complete for {name}",
            file_name=name,
            step="transcription",
        )

    # --- Summarization phase ---
    unsummarized = get_unsummarized_transcripts(project_dir)
    if unsummarized:
        yield PipelineEvent(
            event_type="progress",
            message=f"Found {len(unsummarized)} transcript(s) to summarize",
            step="summarization",
        )

    for transcript_path in unsummarized:
        name = transcript_path.name
        yield PipelineEvent(
            event_type="progress",
            message=f"Summarizing {name}...",
            file_name=name,
            step="summarization",
        )
        try:
            await asyncio.to_thread(summarize_transcript, transcript_path, lambda msg: None)
        except Exception as exc:
            yield PipelineEvent(
                event_type="error",
                message=f"Summarization failed for {name}: {exc}",
                file_name=name,
                step="summarization",
            )
            continue
        yield PipelineEvent(
            event_type="progress",
            message=f"Summarization complete for {name}",
            file_name=name,
            step="summarization",
        )

    # --- Done ---
    yield PipelineEvent(
        event_type="complete",
        message=f"Pipeline finished for project '{project}'",
    )
