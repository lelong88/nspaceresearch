from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from app.routes import NotAuthenticated, router
from app.templating import templates  # noqa: F401 — re-export for convenience

APP_DIR = Path(__file__).resolve().parent


def create_app() -> FastAPI:
    application = FastAPI(title="Meeting Audio Web App")

    application.mount(
        "/static",
        StaticFiles(directory=APP_DIR / "static"),
        name="static",
    )

    application.include_router(router)

    @application.exception_handler(NotAuthenticated)
    async def not_authenticated_handler(request, exc):
        return RedirectResponse(url="/login", status_code=302)

    return application


app = create_app()
