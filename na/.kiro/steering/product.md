# Product Overview

Internal productivity toolkit for an insurance agency (Manulife Vietnam). Two main capabilities:

1. **Meeting Audio Pipeline** — A FastAPI web app that processes meeting audio recordings: upload → transcribe (Soniox API) → summarize (OpenAI-compatible LLM). Organized by project folders. Includes session auth, SSE-based progress streaming, and a file browser for transcripts/summaries.

2. **Slide QA Prep** — Generates interview-style Q&A questions from OCR'd slide decks, accepts voice responses, transcribes them, and provides AI-generated feedback on accuracy/completeness.

3. **Standalone scripts** — Utility scripts at the repo root for OCR'ing slide images (`ocr_slides.py`), generating PowerPoint decks programmatically (`gen_pptx.py`), and text-to-speech via Gemini or AWS Polly.

The domain is insurance agency management — compensation schemes, risk metrics (VAR/VaR), agency hierarchy, and Vietnamese-English bilingual content. A detailed domain glossary lives in `glossary.md`.
