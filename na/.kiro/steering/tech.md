# Tech Stack

## Language & Runtime
- Python 3.12

## Web Framework
- FastAPI with Uvicorn (ASGI)
- Jinja2 templates (server-rendered HTML)
- SSE (Server-Sent Events) via `sse-starlette` for pipeline progress streaming

## Key Libraries
- `itsdangerous` — session token signing
- `python-dotenv` — env var loading from `.env`
- `markdown` — rendering summaries as HTML
- `python-multipart` — file upload handling
- `requests` — HTTP calls to external LLM/transcription APIs
- `Pillow` — image processing for slide OCR
- `boto3` — AWS Polly TTS
- `python-pptx` — programmatic PowerPoint generation

## External Services
- Soniox API — audio transcription
- OpenAI-compatible API — summarization, question generation, feedback, OCR
- Google Gemini API — TTS
- AWS Polly — TTS

## Containerization
- Docker + docker-compose
- Port 6006
- Volumes mount `meeting-audios/`, `slides/`, `output/` into the container

## Common Commands

```bash
# Run the web app locally
uvicorn app.main:app --host 0.0.0.0 --port 6006

# Run with Docker
docker compose up --build

# OCR slide images to markdown
python ocr_slides.py

# Generate TTS audio
python gemini-tts.py <input_file.txt>
python polly-tts.py <input_file.txt>

# Install dependencies
pip install -r requirements.txt
pip install -r app/requirements.txt
```

## Configuration
All secrets and config via `.env` file: `APP_PASSWORD`, `SECRET_KEY`, `SONIOX_API_KEY`, `OPENAI_COMPATIBLE_URL`, `OPENAI_KEY`, `MODEL`, `GEMINI_API_KEY`.
