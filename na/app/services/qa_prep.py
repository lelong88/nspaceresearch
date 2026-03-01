"""QA Prep service — slide reading, question generation, response handling, and session state."""

from __future__ import annotations

import json
import random
import re
import string
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from app.config import settings
from app.models import ALLOWED_EXTENSIONS


# ---------------------------------------------------------------------------
# Slide reading
# ---------------------------------------------------------------------------

def list_slide_decks(slides_dir: Path) -> list[str]:
    """Return sorted project names that have a md/ subdirectory under slides_dir."""
    if not slides_dir.exists():
        return []
    return sorted(
        d.name
        for d in slides_dir.iterdir()
        if d.is_dir() and (d / "md").is_dir()
    )


def read_slide_content(slides_dir: Path, project: str) -> str:
    """Aggregate all .md files from slides/<project>/md/ sorted by name.

    Returns the concatenated content, or an error string starting with
    "Error:" if the directory is missing or empty.
    """
    md_dir = slides_dir / project / "md"
    if not md_dir.is_dir():
        return f"Error: No slide content found for project {project}"
    md_files = sorted(f for f in md_dir.iterdir() if f.is_file() and f.suffix == ".md")
    if not md_files:
        return f"Error: No slide content found for project {project}"
    return "\n\n".join(f.read_text() for f in md_files)


# ---------------------------------------------------------------------------
# Question generation
# ---------------------------------------------------------------------------

_QUESTION_PROMPT = """You are an interview coach. Given the following slide deck content, generate {n} \
interview-style questions that a presenter might be asked during a Q&A session.
Focus on key data points, strategic decisions, and areas that need justification.
Return ONLY a JSON array of question strings.

Slide content:
{slide_content}"""


def _clamp_questions(questions: list[str]) -> list[str]:
    """Ensure question count is within [5, 15]. Clamp if outside range."""
    if len(questions) < 5:
        return questions  # accept as-is if LLM returned fewer
    return questions[:15]


def generate_questions(slide_content: str) -> list[str]:
    """Call LLM to generate 5-15 interview questions from slide content."""
    import requests

    n = 10  # target question count
    prompt = _QUESTION_PROMPT.format(n=n, slide_content=slide_content)

    resp = requests.post(
        f"{settings.OPENAI_COMPATIBLE_URL}/chat/completions",
        headers={"Authorization": f"Bearer {settings.OPENAI_KEY}"},
        json={
            "model": settings.MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
        },
        timeout=120,
    )
    resp.raise_for_status()

    content = resp.json()["choices"][0]["message"]["content"]
    # Strip markdown code fences if present
    content = content.strip()
    if content.startswith("```"):
        content = re.sub(r"^```\w*\n?", "", content)
        content = re.sub(r"\n?```$", "", content)
        content = content.strip()

    questions = json.loads(content)
    if not isinstance(questions, list):
        raise ValueError("LLM did not return a JSON array")
    questions = [str(q) for q in questions]
    return _clamp_questions(questions)


def save_questions(output_dir: Path, project: str, questions: list[str]) -> Path:
    """Persist questions to output/slide-qa-prep/<project>/questions.json."""
    dest_dir = output_dir / "slide-qa-prep" / project
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / "questions.json"
    data = {
        "project": project,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "questions": questions,
    }
    dest.write_text(json.dumps(data, indent=2))
    return dest


def load_questions(output_dir: Path, project: str) -> list[str] | None:
    """Load questions from disk, return None if not found."""
    path = output_dir / "slide-qa-prep" / project / "questions.json"
    if not path.exists():
        return None
    data = json.loads(path.read_text())
    return data.get("questions")


# ---------------------------------------------------------------------------
# Response handling
# ---------------------------------------------------------------------------

def _random_suffix(length: int = 3) -> str:
    """Generate a random alphanumeric suffix."""
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


def validate_audio_extension(filename: str) -> bool:
    """Return True if the file extension is in ALLOWED_EXTENSIONS."""
    return Path(filename).suffix.lower() in ALLOWED_EXTENSIONS


def save_response_audio(
    output_dir: Path,
    project: str,
    q_number: int,
    filename: str,
    content: bytes,
) -> tuple[Path, str]:
    """Save audio file with q<N>_<random_3_char>.<ext> naming.

    Returns (saved_path, suffix).
    Raises ValueError for unsupported extensions.
    """
    ext = Path(filename).suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file extension: {ext}. Allowed: {', '.join(sorted(ALLOWED_EXTENSIONS))}"
        )

    suffix = _random_suffix()
    dest_dir = output_dir / "slide-qa-prep" / project / "responses"
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / f"q{q_number}_{suffix}{ext}"
    dest.write_bytes(content)
    return dest, suffix


# ---------------------------------------------------------------------------
# Transcription
# ---------------------------------------------------------------------------

def transcribe_response(audio_path: Path) -> str:
    """Transcribe an audio response using the existing Soniox transcription service.

    Saves the transcript as a .txt file with the same q<N>_<suffix> prefix.
    Returns the transcript text.
    """
    import transcribe_meetings

    text = transcribe_meetings.transcribe(audio_path)
    transcript_path = audio_path.with_suffix(".txt")
    transcript_path.write_text(text)
    return text


# ---------------------------------------------------------------------------
# Feedback generation
# ---------------------------------------------------------------------------

_FEEDBACK_PROMPT = """You are an interview coach evaluating a presenter's response to a Q&A question.

Question: {question}
Presenter's response: {transcript}
Actual slide content: {slide_content}

Evaluate the response for:
1. **Accuracy** — Does the response align with the slide content?
2. **Completeness** — Are key points covered?
3. **Clarity** — Is the answer well-structured and clear?

Provide specific feedback with suggestions for improvement."""


def generate_feedback(question: str, transcript: str, slide_content: str) -> str:
    """Call LLM to evaluate the response. Returns markdown feedback."""
    import requests

    prompt = _FEEDBACK_PROMPT.format(
        question=question, transcript=transcript, slide_content=slide_content
    )

    resp = requests.post(
        f"{settings.OPENAI_COMPATIBLE_URL}/chat/completions",
        headers={"Authorization": f"Bearer {settings.OPENAI_KEY}"},
        json={
            "model": settings.MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.5,
        },
        timeout=120,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


def save_feedback(feedback_path: Path, feedback: str) -> None:
    """Persist feedback markdown to disk."""
    feedback_path.parent.mkdir(parents=True, exist_ok=True)
    feedback_path.write_text(feedback)


# ---------------------------------------------------------------------------
# Session state and progress tracking
# ---------------------------------------------------------------------------

# Regex to parse response filenames: q<number>_<3char suffix>.<ext>
_RESPONSE_RE = re.compile(r"^q(\d+)_([a-zA-Z0-9]{3})\.(\w+)$")


@dataclass
class ResponseAttempt:
    suffix: str
    audio_file: str
    transcript: str | None = None
    feedback: str | None = None
    upload_time: float = 0.0


@dataclass
class QuestionState:
    number: int
    text: str
    attempts: list[ResponseAttempt] = field(default_factory=list)


@dataclass
class SessionState:
    project: str
    questions: list[QuestionState] = field(default_factory=list)
    total_questions: int = 0
    answered_count: int = 0
    feedback_count: int = 0


def load_session_state(
    output_dir: Path, project: str, questions: list[str] | None = None
) -> SessionState:
    """Scan output dir to build per-question state with attempts.

    Groups attempts by question number, orders by file mtime ascending.
    """
    questions = questions or []
    responses_dir = output_dir / "slide-qa-prep" / project / "responses"

    # Build a map: question_number -> list of (suffix, audio_filename, mtime)
    attempts_map: dict[int, list[ResponseAttempt]] = {}

    if responses_dir.is_dir():
        for f in responses_dir.iterdir():
            if not f.is_file():
                continue
            m = _RESPONSE_RE.match(f.name)
            if not m:
                continue
            q_num = int(m.group(1))
            suffix = m.group(2)
            ext = m.group(3)

            # Skip transcript and feedback files in this pass
            if ext == "txt" or f.name.endswith("_feedback.md"):
                continue

            # Look for corresponding transcript and feedback
            transcript_path = responses_dir / f"q{q_num}_{suffix}.txt"
            feedback_path = responses_dir / f"q{q_num}_{suffix}_feedback.md"

            transcript_text = None
            if transcript_path.exists():
                transcript_text = transcript_path.read_text()

            feedback_text = None
            if feedback_path.exists():
                feedback_text = feedback_path.read_text()

            attempt = ResponseAttempt(
                suffix=suffix,
                audio_file=f.name,
                transcript=transcript_text,
                feedback=feedback_text,
                upload_time=f.stat().st_mtime,
            )

            attempts_map.setdefault(q_num, []).append(attempt)

    # Sort attempts within each question by upload time
    for q_num in attempts_map:
        attempts_map[q_num].sort(key=lambda a: a.upload_time)

    # Build question states
    question_states = []
    for i, q_text in enumerate(questions, start=1):
        qs = QuestionState(
            number=i,
            text=q_text,
            attempts=attempts_map.get(i, []),
        )
        question_states.append(qs)

    answered = sum(1 for qs in question_states if qs.attempts)
    with_feedback = sum(
        1 for qs in question_states if any(a.feedback for a in qs.attempts)
    )

    return SessionState(
        project=project,
        questions=question_states,
        total_questions=len(questions),
        answered_count=answered,
        feedback_count=with_feedback,
    )
