"""QA Prep routes — deck selection, question generation, response upload."""

from __future__ import annotations

import asyncio
from pathlib import Path

import markdown as md_lib
from fastapi import APIRouter, Depends, File, Request, UploadFile
from fastapi.responses import HTMLResponse, RedirectResponse

from app.config import settings
from app.routes import NotAuthenticated, get_current_user
from app.services.qa_prep import (
    generate_feedback,
    generate_questions,
    list_slide_decks,
    load_questions,
    load_session_state,
    read_slide_content,
    save_feedback,
    save_questions,
    save_response_audio,
    transcribe_response,
    validate_audio_extension,
)
from app.templating import templates

qa_prep_router = APIRouter()

SLIDES_DIR = Path("slides")
OUTPUT_DIR = Path("output")


def _validate_project(project: str) -> bool:
    """Reject path traversal characters."""
    return ".." not in project and "/" not in project and "\\" not in project


# ---------------------------------------------------------------------------
# Deck selection
# ---------------------------------------------------------------------------

@qa_prep_router.get("/qa-prep", response_class=HTMLResponse)
async def qa_prep_select(request: Request, _=Depends(get_current_user)):
    decks = list_slide_decks(SLIDES_DIR)
    return templates.TemplateResponse(
        "qa_prep_select.html", {"request": request, "decks": decks}
    )


# ---------------------------------------------------------------------------
# Session page
# ---------------------------------------------------------------------------

@qa_prep_router.get("/qa-prep/{project}", response_class=HTMLResponse)
async def qa_prep_session(request: Request, project: str, _=Depends(get_current_user)):
    if not _validate_project(project):
        return HTMLResponse("Invalid project name", status_code=400)

    questions = load_questions(OUTPUT_DIR, project)
    state = load_session_state(OUTPUT_DIR, project, questions)

    # Convert feedback markdown to HTML for display
    for qs in state.questions:
        for attempt in qs.attempts:
            if attempt.feedback:
                attempt.feedback = md_lib.markdown(attempt.feedback)

    return templates.TemplateResponse(
        "qa_prep_session.html",
        {
            "request": request,
            "project": project,
            "state": state,
            "error": None,
        },
    )


# ---------------------------------------------------------------------------
# Generate / regenerate questions
# ---------------------------------------------------------------------------

@qa_prep_router.post("/qa-prep/{project}/generate")
async def qa_prep_generate(request: Request, project: str, _=Depends(get_current_user)):
    if not _validate_project(project):
        return HTMLResponse("Invalid project name", status_code=400)

    slide_content = read_slide_content(SLIDES_DIR, project)
    if slide_content.startswith("Error:"):
        # Render session page with error
        questions = load_questions(OUTPUT_DIR, project)
        state = load_session_state(OUTPUT_DIR, project, questions)
        return templates.TemplateResponse(
            "qa_prep_session.html",
            {"request": request, "project": project, "state": state, "error": slide_content},
        )

    try:
        questions = await asyncio.to_thread(generate_questions, slide_content)
        save_questions(OUTPUT_DIR, project, questions)
    except Exception as exc:
        questions = load_questions(OUTPUT_DIR, project)
        state = load_session_state(OUTPUT_DIR, project, questions)
        return templates.TemplateResponse(
            "qa_prep_session.html",
            {"request": request, "project": project, "state": state, "error": f"Question generation failed: {exc}"},
        )

    return RedirectResponse(url=f"/qa-prep/{project}", status_code=302)


# ---------------------------------------------------------------------------
# Upload voice response
# ---------------------------------------------------------------------------

@qa_prep_router.post("/qa-prep/{project}/upload/{q_number}")
async def qa_prep_upload(
    request: Request,
    project: str,
    q_number: int,
    file: UploadFile = File(...),
    _=Depends(get_current_user),
):
    if not _validate_project(project):
        return HTMLResponse("Invalid project name", status_code=400)

    if not file.filename or not validate_audio_extension(file.filename):
        questions = load_questions(OUTPUT_DIR, project)
        state = load_session_state(OUTPUT_DIR, project, questions)
        return templates.TemplateResponse(
            "qa_prep_session.html",
            {
                "request": request,
                "project": project,
                "state": state,
                "error": "Unsupported file format. Allowed: .m4a, .mp3, .mp4, .wav, .flac, .ogg, .aac, .webm, .amr, .aiff, .asf",
            },
            status_code=400,
        )

    content = await file.read()
    audio_path, suffix = save_response_audio(OUTPUT_DIR, project, q_number, file.filename, content)

    # Transcribe
    error_msg = None
    transcript = None
    try:
        transcript = await asyncio.to_thread(transcribe_response, audio_path)
    except Exception as exc:
        error_msg = f"Transcription failed: {exc}"

    # Feedback (only if transcription succeeded)
    if transcript and not error_msg:
        try:
            slide_content = read_slide_content(SLIDES_DIR, project)
            questions = load_questions(OUTPUT_DIR, project)
            question_text = questions[q_number - 1] if questions and q_number <= len(questions) else "Unknown question"
            feedback = await asyncio.to_thread(generate_feedback, question_text, transcript, slide_content)
            feedback_path = audio_path.parent / f"q{q_number}_{suffix}_feedback.md"
            save_feedback(feedback_path, feedback)
        except Exception as exc:
            error_msg = f"Feedback generation failed: {exc}"

    if error_msg:
        questions = load_questions(OUTPUT_DIR, project)
        state = load_session_state(OUTPUT_DIR, project, questions)
        return templates.TemplateResponse(
            "qa_prep_session.html",
            {"request": request, "project": project, "state": state, "error": error_msg},
        )

    return RedirectResponse(url=f"/qa-prep/{project}", status_code=302)
