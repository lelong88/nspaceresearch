# Implementation Plan: Slide Q&A Prep

## Overview

Incrementally build the Q&A Prep feature as a new FastAPI router with a service module, two Jinja2 templates, and Docker Compose volume mappings. Each task builds on the previous, starting with infrastructure and data layer, then core logic, then UI, then wiring.

## Tasks

- [x] 1. Docker Compose volume mappings and navigation link
  - [x] 1.1 Add `./slides:/app/slides` and `./output:/app/output` volume mappings to the `web` service in `docker-compose.yml`, following the existing `./meeting-audios:/app/meeting-audios` pattern
    - _Requirements: 8.1, 8.2_
  - [x] 1.2 Add a "Q&A Prep" navigation link in `app/templates/base.html` pointing to `/qa-prep`
    - _Requirements: 7.3_

- [x] 2. QA Prep service — slide reading and question generation
  - [x] 2.1 Create `app/services/qa_prep.py` with `list_slide_decks(slides_dir)` and `read_slide_content(slides_dir, project)` functions
    - `list_slide_decks` returns project names that have a `md/` subdirectory under `slides/`
    - `read_slide_content` aggregates all `.md` files sorted by filename, returns error string if empty
    - _Requirements: 1.1, 1.2, 1.3_
  - [ ]* 2.2 Write property test for deck listing (Property 1)
    - **Property 1: Deck listing filters by md/ subdirectory**
    - **Validates: Requirements 1.1**
    - Use Hypothesis to generate random directory trees with/without `md/` subdirs in a tmp dir
  - [ ]* 2.3 Write property test for slide content aggregation (Property 2)
    - **Property 2: Slide content aggregation includes all files**
    - **Validates: Requirements 1.2**
    - Generate random sets of markdown files, verify all content present in sorted order
  - [x] 2.4 Implement `generate_questions(slide_content)`, `save_questions(output_dir, project, questions)`, and `load_questions(output_dir, project)` in `app/services/qa_prep.py`
    - `generate_questions` calls the LLM via `httpx` (or `requests` via `asyncio.to_thread`) using the question generation prompt template from the design
    - Parse JSON array response, validate count is in [5, 15] range (clamp if needed)
    - `save_questions` writes `questions.json` with project name, timestamp, and questions array
    - `load_questions` reads from disk, returns None if file not found
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6_
  - [ ]* 2.5 Write property test for question count validation (Property 3)
    - **Property 3: Question count validation**
    - **Validates: Requirements 2.2**
    - Generate random-length string arrays, verify accept/clamp behavior for [5, 15] range
  - [ ]* 2.6 Write property test for question persistence round trip (Property 4)
    - **Property 4: Question persistence round trip**
    - **Validates: Requirements 2.3**
    - Generate random question sets, save then load, verify equivalence

- [x] 3. Checkpoint — Verify slide reading and question generation
  - Ensure all tests pass, ask the user if questions arise.

- [x] 4. QA Prep service — response handling, transcription, and feedback
  - [x] 4.1 Implement `save_response_audio(output_dir, project, q_number, filename, content)` in `app/services/qa_prep.py`
    - Validate file extension against allowed set {.m4a, .mp3, .mp4, .wav, .flac, .ogg, .aac, .webm, .amr, .aiff, .asf}
    - Generate random 3-char alphanumeric suffix
    - Save to `output/slide-qa-prep/<project>/responses/q<N>_<suffix>.<ext>`
    - Return the file path and suffix
    - _Requirements: 3.3, 3.4, 3.5_
  - [ ]* 4.2 Write property test for audio file extension validation (Property 5)
    - **Property 5: Audio file extension validation**
    - **Validates: Requirements 3.3, 3.5**
    - Generate random filenames with random extensions, verify accept/reject
  - [ ]* 4.3 Write property test for response file naming convention (Property 6)
    - **Property 6: Response file naming convention**
    - **Validates: Requirements 3.4**
    - Generate random question numbers and extensions, verify naming regex `q\d+_[a-zA-Z0-9]{3}\.\w+`
  - [x] 4.4 Implement `transcribe_response(audio_path)` and `generate_feedback(question, transcript, slide_content)` in `app/services/qa_prep.py`
    - `transcribe_response` calls the existing `transcribe_meetings.transcribe()` function, saves `.txt` file with same prefix as audio
    - `generate_feedback` calls LLM with the feedback prompt template from the design, returns markdown string
    - Implement `save_feedback(feedback_path, feedback)` to persist feedback as `_feedback.md`
    - _Requirements: 4.1, 4.2, 5.1, 5.2, 5.3_
  - [ ]* 4.5 Write property test for file suffix consistency (Property 7)
    - **Property 7: File suffix consistency across audio, transcript, and feedback**
    - **Validates: Requirements 4.2, 5.3**
    - Run upload flow, verify audio/transcript/feedback files share the same `q<N>_<suffix>` prefix

- [x] 5. QA Prep service — session state and progress tracking
  - [x] 5.1 Implement `load_session_state(output_dir, project)` in `app/services/qa_prep.py`
    - Scan `responses/` directory, parse filenames to extract question number and suffix
    - Group attempts by question number, order by file mtime ascending
    - Build `SessionState` with `answered_count` and `feedback_count`
    - _Requirements: 3.6, 6.1, 6.2, 6.3_
  - [ ]* 5.2 Write property test for session state grouping and ordering (Property 8)
    - **Property 8: Session state groups attempts by question and orders by time**
    - **Validates: Requirements 3.6**
    - Generate random response file sets in tmp dir, verify grouping and ordering
  - [ ]* 5.3 Write property test for progress count accuracy (Property 9)
    - **Property 9: Progress count accuracy**
    - **Validates: Requirements 6.1**
    - Generate random session states, verify `answered_count` and `feedback_count` derivation
  - [ ]* 5.4 Write property test for append-only uploads (Property 10)
    - **Property 10: Append-only uploads**
    - **Validates: Requirements 6.3**
    - Run sequential uploads to the same question, verify no files are deleted

- [x] 6. Checkpoint — Verify response handling and session state
  - Ensure all tests pass, ask the user if questions arise.

- [x] 7. FastAPI routes and templates
  - [x] 7.1 Create `app/routes_qa_prep.py` with the QA Prep `APIRouter`
    - `GET /qa-prep` — calls `list_slide_decks`, renders `qa_prep_select.html` with deck list
    - `GET /qa-prep/{project}` — calls `load_questions` and `load_session_state`, renders `qa_prep_session.html`
    - `POST /qa-prep/{project}/generate` — calls `read_slide_content` and `generate_questions`, saves questions, redirects to session page
    - `POST /qa-prep/{project}/upload/{q_number}` — validates upload, calls `save_response_audio`, `transcribe_response`, `generate_feedback`, `save_feedback`, redirects to session page
    - All endpoints use `Depends(get_current_user)` for authentication
    - Validate project name (no `..`, `/`, `\`) to prevent path traversal
    - Handle LLM and transcription errors with flash messages
    - _Requirements: 1.4, 2.6, 3.5, 4.4, 5.5, 7.1, 7.2, 7.4_
  - [x] 7.2 Create `app/templates/qa_prep_select.html` extending `base.html`
    - Display available slide decks as clickable cards linking to `/qa-prep/<project>`
    - Show message if no decks are available
    - _Requirements: 1.1_
  - [x] 7.3 Create `app/templates/qa_prep_session.html` extending `base.html`
    - Progress indicator showing answered/total and feedback/total counts
    - Numbered question list with per-question file upload form (accept audio types)
    - Per-question expandable attempt history showing transcript text and feedback markdown
    - Visual distinction for questions with responses, transcripts, and feedback (e.g., status badges)
    - "Generate Questions" / "Regenerate Questions" button
    - Error display area for flash messages
    - _Requirements: 2.5, 3.1, 3.2, 3.3, 3.6, 4.3, 5.4, 6.1, 6.2_

- [x] 8. Register router in main.py
  - [x] 8.1 Import `qa_prep_router` from `app.routes_qa_prep` and call `app.include_router(qa_prep_router)` in `app/main.py`
    - _Requirements: 7.4_
  - [ ]* 8.2 Write unit tests for route registration and auth enforcement
    - Test that `/qa-prep` returns 401/redirect without auth
    - Test that `/qa-prep` returns 200 with valid auth
    - Test that `/qa-prep/{project}` returns correct template
    - _Requirements: 1.4, 7.1, 7.2_

- [x] 9. Final checkpoint — Full integration verification
  - Ensure all tests pass, ask the user if questions arise.

## Notes

- Tasks marked with `*` are optional and can be skipped for faster MVP
- Each task references specific requirements for traceability
- Property tests use Hypothesis with `@settings(max_examples=100)`
- Test file location: `app/services/test_qa_prep.py`
- Checkpoints ensure incremental validation
- The upload endpoint processes transcription and feedback synchronously per request; async background processing can be added later if needed
