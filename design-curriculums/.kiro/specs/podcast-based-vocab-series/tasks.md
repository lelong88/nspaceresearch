# Implementation Plan: Podcast-Based Vocab Series

## Overview

Create a new collection "Học Từ Vựng Qua Podcast" and populate it with a single series "Học Từ Vựng Qua Podcast" containing 4 curriculums. Each curriculum is built around a different podcast episode, using verbatim transcript excerpts as reading passages. One standalone Python script per curriculum + one orchestrator for collection/series creation. After verification, scripts are deleted and README is written.

## Tasks

- [x] 1. Podcast Curriculum Scripts
  - [x] 1.1 Create `podcast-based-vocab-series/create_podcast_1_<podcast>.py` — Podcast 1 curriculum
    - Select an appropriate evergreen podcast episode via web search (TED Talk or educational podcast, clear pronunciation, A2-B1 level language, educational/informational/storytelling content, no excessive profanity, available on YouTube)
    - Find verbatim podcast transcript via web search and verify accuracy
    - Find the YouTube URL for the podcast episode via web search
    - Define 18 vocabulary words drawn from the transcript (W1, W2, W3 — 6 each), prioritizing words that are genuinely in the transcript, at A2-B1 level, broadly useful, and teachable
    - Write transcript portions for sessions 1-3 (TRANSCRIPT_1, TRANSCRIPT_2, TRANSCRIPT_3 — segments containing each session's 6 words) and FULL_TRANSCRIPT (complete podcast transcript excerpt)
    - Write persuasive Vietnamese description (5-beat structure, podcast-adapted), preview (~150 words referencing the podcast episode and its themes), and curriculum title in format "Học Qua Podcast: 'Episode Title' – Podcast Name"
    - Write 5 sessions of hand-crafted introAudio scripts: welcome + podcast episode context, vocab teaching (how each word appears in the transcript), grammar/usage notes for sessions 1-3; congratulations + recap for session 4; farewell with all 18 words reviewed for session 5 (400-600 words)
    - Write writingSentence items with targetVocab, podcast-episode-themed context prompts, and "Ví dụ:" examples
    - Include `youtubeUrl` at top level of content dict
    - Include all activity metadata (title, description) following naming conventions (Flashcards:/Đọc:/Nghe:/Viết:)
    - readAlong description: "Nghe podcast và theo dõi."
    - Include inline `STRIP_KEYS` set and `strip_keys()` function
    - Include inline `validate(content)` function checking Properties 1-12 from design
    - API call: `curriculum/create` with `language="en"`, `userLanguage="vi"`, `content=json.dumps(content)`
    - Print created curriculum ID
    - _Requirements: 1.5, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 3.1, 3.2, 3.3, 3.4, 3.5, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 7.1, 7.2, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 9.1, 11.1, 11.3, 12.1, 12.2, 13.1, 14.1, 14.2, 15.1, 15.2, 15.3, 16.1, 16.2_

  - [x] 1.2 Create `podcast-based-vocab-series/create_podcast_2_<podcast>.py` — Podcast 2 curriculum
    - Select a different evergreen podcast episode via web search (same criteria as 1.1 — TED Talk or educational podcast, clear pronunciation, A2-B1 level, educational/informational/storytelling, available on YouTube)
    - Find verbatim podcast transcript and YouTube URL for the episode via web search
    - Same structure as 1.1 but with 18 vocabulary words drawn from this episode's transcript
    - All text content (description, preview, introAudio scripts, writing prompts) hand-written for this specific podcast episode — no templates or reuse from podcast 1
    - Include inline `strip_keys()`, `validate(content)`, `youtubeUrl`, and API call
    - _Requirements: 1.5, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 3.1, 3.2, 3.3, 3.4, 3.5, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 7.1, 7.2, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 9.1, 11.1, 11.3, 12.1, 12.2, 13.1, 14.1, 14.2, 15.1, 15.2, 15.3, 16.1, 16.2_

  - [x] 1.3 Create `podcast-based-vocab-series/create_podcast_3_<podcast>.py` — Podcast 3 curriculum
    - Select a different evergreen podcast episode via web search (same criteria — TED Talk or educational podcast, clear pronunciation, A2-B1 level, educational/informational/storytelling, available on YouTube)
    - Find verbatim podcast transcript and YouTube URL for the episode via web search
    - Same structure as 1.1 but with 18 vocabulary words drawn from this episode's transcript
    - All text content hand-written for this specific podcast episode
    - Include inline `strip_keys()`, `validate(content)`, `youtubeUrl`, and API call
    - _Requirements: 1.5, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 3.1, 3.2, 3.3, 3.4, 3.5, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 7.1, 7.2, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 9.1, 11.1, 11.3, 12.1, 12.2, 13.1, 14.1, 14.2, 15.1, 15.2, 15.3, 16.1, 16.2_

  - [x] 1.4 Create `podcast-based-vocab-series/create_podcast_4_<podcast>.py` — Podcast 4 curriculum
    - Select a different evergreen podcast episode via web search (same criteria — TED Talk or educational podcast, clear pronunciation, A2-B1 level, educational/informational/storytelling, available on YouTube)
    - Find verbatim podcast transcript and YouTube URL for the episode via web search
    - Same structure as 1.1 but with 18 vocabulary words drawn from this episode's transcript
    - All text content hand-written for this specific podcast episode
    - Include inline `strip_keys()`, `validate(content)`, `youtubeUrl`, and API call
    - _Requirements: 1.5, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 3.1, 3.2, 3.3, 3.4, 3.5, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 7.1, 7.2, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 9.1, 11.1, 11.3, 12.1, 12.2, 13.1, 14.1, 14.2, 15.1, 15.2, 15.3, 16.1, 16.2_

- [x] 2. Checkpoint — All 4 curriculum scripts created
  - Ensure all 4 curriculum scripts pass `validate(content)` locally. Verify each script selects a different podcast episode, has 18 unique vocab words from the transcript, correct session/activity structure, youtubeUrl present, and no strip keys. Ask the user if questions arise.

- [x] 3. Orchestrator & Execution
  - [x] 3.1 Create `podcast-based-vocab-series/create_podcast_series.py` — Collection + Series orchestrator
    - Create collection via `curriculum-collection/create` with title "Học Từ Vựng Qua Podcast (Learn Vocabulary Through Podcasts)", persuasive Vietnamese description, `isPublic: true`
    - Create series via `curriculum-series/create` with title "Học Từ Vựng Qua Podcast (Learn Vocabulary Through Podcasts)", Vietnamese description (≤255 chars), `isPublic: true`
    - Add series to collection via `curriculum-collection/addSeriesToCollection`
    - Set series display order 100 via `curriculum-series/setDisplayOrder`
    - Add all 4 curriculum IDs to series via `curriculum-series/addCurriculum`
    - Set curriculum display orders (0, 1, 2, 3) via `curriculum/setDisplayOrder`
    - Token refreshed before each API call
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 10.1, 10.2, 10.3, 11.2, 13.3_

  - [x] 3.2 Run all 4 curriculum scripts and the orchestrator, verify output
    - Run `python create_podcast_1_<podcast>.py`, `create_podcast_2_<podcast>.py`, `create_podcast_3_<podcast>.py`, `create_podcast_4_<podcast>.py`
    - Paste curriculum IDs into orchestrator, run `python create_podcast_series.py`
    - _Requirements: 11.1, 11.2_

- [x] 4. Checkpoint — Collection, series, and curriculums created
  - Ensure the orchestrator completed successfully. Verify the new collection exists, the series is inside it with display_order 100, and all 4 curriculums are in the series with display orders 0-3. Ask the user if questions arise.

- [x] 5. Post-creation verification
  - [x] 5.1 Run SQL verification queries against the database
    - Verify the new "Học Từ Vựng Qua Podcast" collection exists and is public
    - Verify the collection has exactly 1 series
    - Verify the series has exactly 4 curriculums
    - Verify series display order is 100
    - Verify curriculum display orders within the series: 0, 1, 2, 3
    - Verify each curriculum has `youtubeUrl` at top level of content JSON
    - Verify language homogeneity via `curriculum_series_language_list` (all vi-en)
    - Verify all 4 curriculums are private (`is_public = false`)
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 10.1, 10.2, 10.3, 13.1, 15.1, 16.1_

- [x] 6. Cleanup — Delete scripts and write README
  - [x] 6.1 Delete all curriculum and orchestrator scripts from `podcast-based-vocab-series/`, write `README.md`
    - README includes: collection ID and title, series ID, 4 curriculum IDs and titles (with podcast/episode), YouTube URLs used, how content was created, SQL queries to find the curriculums in the DB, enough context to recreate if needed
    - _Requirements: 11.4, 17.1, 17.2, 17.3_

- [x] 7. Final checkpoint
  - Ensure all 4 curriculums exist in DB, the new collection and series are correctly wired, all source scripts are deleted, and the folder contains only README.md. Ask the user if questions arise.

## Notes

- Each curriculum script is ~500-800 lines with all hand-written Vietnamese/English content — no templates or string interpolation for learner-facing text
- Podcast episodes are NOT pre-selected — the implementer selects appropriate episodes during implementation based on the podcast episode selection criteria in Requirements 2.1-2.7 (evergreen, clear pronunciation, A2-B1 level, no excessive profanity, well-known, sufficient transcript length, educational/informational/storytelling content)
- Podcast transcripts MUST be sourced via web search during implementation to ensure verbatim accuracy
- YouTube URLs MUST be found via web search during implementation to ensure validity
- The `validate(content)` function in each script checks structural properties (18 words, 5 sessions, activity order, title/description presence, no strip keys, youtubeUrl format, vocab in transcript, transcript substring checks, writing prompt format, farewell word review) before making the API call
- The orchestrator creates BOTH the collection AND the series (unlike topic-based expansion which only created series for an existing collection)
- Orchestrator takes curriculum IDs as constants (pasted from curriculum script output)
- Follow the exact pattern from `movie-based-vocab-series/` curriculum scripts for script structure
- All series descriptions must be under 255 characters (PostgreSQL varchar limit)
- Token is refreshed via `get_firebase_id_token(UID)` before each API call
- Content JSON includes `youtubeUrl` at top level alongside `title`, `description`, `preview`, `learningSessions`
- readAlong description is "Nghe podcast và theo dõi." (not "Nghe bài hát và theo dõi." or "Nghe lời thoại phim và theo dõi.")
