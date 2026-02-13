from dataclasses import dataclass


@dataclass
class ProjectInfo:
    name: str
    transcript_count: int
    summary_count: int
    audio_count: int


@dataclass
class ProjectDetail:
    name: str
    transcripts: list[str]   # filenames
    summaries: list[str]     # filenames


@dataclass
class PipelineEvent:
    event_type: str   # "progress", "error", "complete"
    message: str
    file_name: str | None = None
    step: str | None = None   # "transcription" or "summarization"


ALLOWED_EXTENSIONS: set[str] = {
    ".m4a", ".mp3", ".mp4", ".wav", ".flac",
    ".ogg", ".aac", ".webm", ".amr", ".aiff", ".asf",
}
