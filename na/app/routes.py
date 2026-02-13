import dataclasses
import json

import markdown
from fastapi import APIRouter, Cookie, Depends, File, Form, Request, UploadFile
from fastapi.responses import HTMLResponse, RedirectResponse
from sse_starlette.sse import EventSourceResponse

from app.auth import create_session_token, validate_session_token, verify_password
from app.config import settings
from app.templating import templates
from app.services.file_browser import (
    list_project_files,
    list_projects,
    read_summary,
    read_transcript,
)
from app.services.pipeline import run_pipeline
from app.services.upload import save_upload

router = APIRouter()


# ---------------------------------------------------------------------------
# Auth dependency
# ---------------------------------------------------------------------------

class NotAuthenticated(Exception):
    """Raised when the user is not authenticated."""


def get_current_user(session_token: str | None = Cookie(default=None)):
    """Check session cookie. Redirect to /login if missing or invalid."""
    if not session_token or not validate_session_token(session_token):
        raise NotAuthenticated()


# ---------------------------------------------------------------------------
# Login / Logout
# ---------------------------------------------------------------------------

@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.post("/login")
async def login_submit(request: Request, password: str = Form(...)):
    if not verify_password(password):
        return templates.TemplateResponse(
            "login.html",
            {"request": request, "error": "Incorrect password"},
        )
    token = create_session_token()
    response = RedirectResponse(url="/", status_code=302)
    response.set_cookie("session_token", token, httponly=True, samesite="lax")
    return response


@router.post("/logout")
async def logout():
    response = RedirectResponse(url="/login", status_code=302)
    response.delete_cookie("session_token")
    return response


# ---------------------------------------------------------------------------
# Home — list projects
# ---------------------------------------------------------------------------

@router.get("/", response_class=HTMLResponse)
async def home(request: Request, _=Depends(get_current_user)):
    projects = list_projects(settings.BASE_DIR)
    return templates.TemplateResponse(
        "home.html", {"request": request, "projects": projects}
    )


# ---------------------------------------------------------------------------
# Project detail
# ---------------------------------------------------------------------------

@router.get("/project/{name}", response_class=HTMLResponse)
async def project_detail(request: Request, name: str, _=Depends(get_current_user)):
    try:
        detail = list_project_files(settings.BASE_DIR, name)
    except FileNotFoundError:
        return HTMLResponse("Project not found", status_code=404)
    return templates.TemplateResponse(
        "project.html", {"request": request, "project": detail}
    )


# ---------------------------------------------------------------------------
# Transcript / Summary viewers
# ---------------------------------------------------------------------------

@router.get("/project/{name}/transcript/{file}", response_class=HTMLResponse)
async def view_transcript(
    request: Request, name: str, file: str, _=Depends(get_current_user)
):
    try:
        content = read_transcript(settings.BASE_DIR, name, file)
    except FileNotFoundError:
        return HTMLResponse("Transcript not found", status_code=404)
    return templates.TemplateResponse(
        "viewer.html",
        {"request": request, "project_name": name, "filename": file, "content": content, "content_type": "transcript"},
    )


@router.get("/project/{name}/summary/{file}", response_class=HTMLResponse)
async def view_summary(
    request: Request, name: str, file: str, _=Depends(get_current_user)
):
    try:
        raw = read_summary(settings.BASE_DIR, name, file)
    except FileNotFoundError:
        return HTMLResponse("Summary not found", status_code=404)
    html_content = markdown.markdown(raw)
    return templates.TemplateResponse(
        "viewer.html",
        {"request": request, "project_name": name, "filename": file, "content": html_content, "content_type": "summary"},
    )


# ---------------------------------------------------------------------------
# Upload
# ---------------------------------------------------------------------------

@router.get("/upload", response_class=HTMLResponse)
async def upload_page(request: Request, _=Depends(get_current_user)):
    projects = list_projects(settings.BASE_DIR)
    return templates.TemplateResponse(
        "upload.html", {"request": request, "projects": projects}
    )


@router.post("/upload")
async def upload_submit(
    request: Request,
    project: str = Form(...),
    new_project: str = Form(""),
    file: UploadFile = File(...),
    _=Depends(get_current_user),
):
    folder = new_project.strip() if new_project.strip() else project
    try:
        content = await file.read()
        save_upload(settings.BASE_DIR, folder, file.filename, content)
    except ValueError as exc:
        projects = list_projects(settings.BASE_DIR)
        return templates.TemplateResponse(
            "upload.html",
            {"request": request, "projects": projects, "error": str(exc)},
            status_code=400,
        )
    return RedirectResponse(url=f"/project/{folder}", status_code=302)


# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------

@router.post("/pipeline/{project}")
async def trigger_pipeline(request: Request, project: str, _=Depends(get_current_user)):
    return templates.TemplateResponse(
        "pipeline.html", {"request": request, "project": project}
    )


@router.get("/pipeline/{project}/stream")
async def pipeline_stream(project: str, _=Depends(get_current_user)):
    async def event_generator():
        async for event in run_pipeline(project, settings.BASE_DIR):
            yield json.dumps(dataclasses.asdict(event))

    return EventSourceResponse(event_generator())
