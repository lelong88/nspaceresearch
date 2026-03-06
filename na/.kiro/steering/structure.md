# Project Structure

```
├── app/                        # FastAPI web application
│   ├── main.py                 # App factory, router mounting
│   ├── config.py               # Settings from env vars
│   ├── auth.py                 # Session token auth (itsdangerous)
│   ├── models.py               # Dataclasses (ProjectInfo, PipelineEvent, etc.)
│   ├── routes.py               # Main routes (home, project, upload, pipeline)
│   ├── routes_qa_prep.py       # QA Prep routes (deck selection, question gen, response upload)
│   ├── templating.py           # Jinja2 templates setup
│   ├── services/               # Business logic layer
│   │   ├── file_browser.py     # List projects, read transcripts/summaries
│   │   ├── pipeline.py         # Transcription → summarization pipeline (async generator)
│   │   ├── transcription.py    # Soniox transcription service
│   │   ├── summarization.py    # LLM summarization service
│   │   ├── qa_prep.py          # QA question gen, feedback, session state
│   │   └── upload.py           # File upload handling
│   ├── templates/              # Jinja2 HTML templates
│   └── static/                 # Static assets
│
├── meeting-audios/             # Meeting data, organized by project
│   └── <project-name>/
│       ├── files/              # Raw audio files (DO NOT modify)
│       ├── transcripts/        # Generated .txt transcripts (DO NOT modify)
│       └── summaries/          # Generated .md summaries (use these)
│
├── slides/                     # Slide decks, organized by project
│   └── <project-name>/
│       ├── images/             # Raw slide images (DO NOT modify)
│       └── md/                 # OCR'd markdown per slide (use these)
│
├── output/                     # Generated output files, organized by project
│   └── <project-name>/        # Scripts, reports, generated content go here
│
├── glossary.md                 # Bilingual Vietnamese-English domain glossary
├── ocr_slides.py               # Batch OCR slides → markdown
├── gen_pptx.py                 # Programmatic PowerPoint generation
├── gemini-tts.py               # Google Gemini TTS
├── polly-tts.py                # AWS Polly TTS
├── Dockerfile                  # Python 3.12-slim container
└── docker-compose.yml          # Single service, port 6006
```

## Key Conventions

- Generated output files go in `output/<project-name>/`
- `files/`, `transcripts/`, and `images/` folders contain raw data — do not modify
- Use `summaries/` and `md/` folders as source content for AI tasks
- Each meeting project has a consistent `files/ → transcripts/ → summaries/` pipeline structure
- Each slide project has `images/ → md/` structure (OCR'd via `ocr_slides.py`)
- Standalone utility scripts live at the repo root
- Web app code lives entirely under `app/`
