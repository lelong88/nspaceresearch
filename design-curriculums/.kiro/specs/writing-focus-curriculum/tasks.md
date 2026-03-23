# Implementation Plan: Writing-Focus Curriculum

## Overview

Create a new collection "Writing Focus" and populate it with 2 series: Series 1 (2 single-language en-en advanced curriculums) and Series 2 (2 bilingual vi-en intermediate curriculums). Each curriculum is a standalone Python script with hand-written content demonstrating the `writing_focus` curriculum type — writing as the centerpiece, no speaking activities, 10 vocab words across 2 sessions, escalating writing prompts. One orchestrator script handles collection + both series + all wiring. After verification, scripts are deleted and README is written.

## Tasks

- [x] 1. Curriculum Scripts
  - [x] 1.1 Create `writing-focus-curriculum/create_writing_1_<topic>.py` — Single-language curriculum 1 (en-en, advanced)
    - Select an appropriate writing topic during implementation (evergreen, intellectually rich, suitable for analytical/argumentative writing at advanced level)
    - Define 10 vocabulary words in 2 groups: W1 (5 words for S1), W2 (5 words for S2) — words that enable the learner to express ideas about the topic in compositions
    - Write MODEL_TEXT_1 (S1 reading passage introducing the topic, containing W1 words in context), MODEL_TEXT_2 (S2 passage presenting a different angle on the same topic, containing W2 words), FULL_ARTICLE (S4 combined/extended passage)
    - Write persuasive English description (5-beat structure, writing-journey-focused), preview (~150 words about the writing progression and topic)
    - Write curriculum title in format "Writing Focus: <Topic Title>" — no difficulty level descriptors
    - Write 4 sessions of hand-crafted content:
      - S1 (8 activities): introAudio (teach 5 words + explain writing task, 500-800 words), viewFlashcards(W1), vocabLevel1(W1), vocabLevel2(W1), reading(MODEL_TEXT_1), readAlong(MODEL_TEXT_1), writingSentence (5 items with targetVocab + "Example:" prompts), writingParagraph (respond to model text, vocabList=W1)
      - S2 (8 activities): introAudio (teach 5 more words + recap S1 writing, 500-800 words), viewFlashcards(W2), vocabLevel1(W2), vocabLevel2(W2), reading(MODEL_TEXT_2), readAlong(MODEL_TEXT_2), writingSentence (5 items), writingParagraph (compare/contrast S1 and S2 passages, vocabList=W2)
      - S3 (5 activities): introAudio (review all 10 words), viewFlashcards(ALL), vocabLevel1(ALL), vocabLevel2(ALL), writingParagraph (analytical essay 6-8 sentences, vocabList=ALL)
      - S4 (5 activities): introAudio (recap journey), reading(FULL_ARTICLE), readAlong(FULL_ARTICLE), writingParagraph (argumentative/persuasive capstone, vocabList=ALL), introAudio (farewell 400-600 words reviewing all 10 words)
    - Activity titles use English prefixes: "Flashcards:", "Read:", "Listen:", "Write:"
    - readAlong description: "Listen and follow along."
    - Include all activity metadata (title, description) and session titles
    - Include inline `STRIP_KEYS` set and `strip_keys()` function
    - Include inline `validate(content, "single-language")` function checking Properties 1-16 from design
    - API call: `curriculum/create` with `language="en"`, `userLanguage="en"`, `content=json.dumps(content)`
    - Print created curriculum ID
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 3.1, 3.2, 3.3, 3.4, 3.6, 4.1, 4.2, 4.3, 4.4, 4.5, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2, 7.5, 8.1, 8.2, 8.3, 8.4, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 10.1, 13.1, 13.3, 14.1, 14.2, 15.1, 15.2, 15.5, 16.1, 16.2, 17.1, 17.3, 17.4, 19.1, 19.2, 19.3, 19.4, 19.5, 20.1, 20.2, 20.3, 20.4, 20.5_

  - [x] 1.2 Create `writing-focus-curriculum/create_writing_2_<topic>.py` — Single-language curriculum 2 (en-en, advanced)
    - Select a different writing topic (same criteria as 1.1 — evergreen, intellectually rich, suitable for analytical/argumentative writing)
    - Same structure as 1.1: 10 vocab words (W1+W2), MODEL_TEXT_1, MODEL_TEXT_2, FULL_ARTICLE, 4 sessions (8, 8, 5, 5 activities)
    - All text content (description, preview, introAudio scripts, reading passages, writing prompts) hand-written for this specific topic — no templates or reuse from curriculum 1
    - Include inline `strip_keys()`, `validate(content, "single-language")`, and API call with `language="en"`, `userLanguage="en"`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 3.1, 3.2, 3.3, 3.4, 3.6, 4.1, 4.2, 4.3, 4.4, 4.5, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2, 7.5, 8.1, 8.2, 8.3, 8.4, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 10.1, 13.1, 13.3, 14.1, 14.2, 15.1, 15.2, 15.5, 16.1, 16.2, 17.1, 17.3, 17.4, 19.1, 19.2, 19.3, 19.4, 19.5, 20.1, 20.2, 20.3, 20.4, 20.5_

  - [x] 1.3 Create `writing-focus-curriculum/create_writing_3_<topic>.py` — Bilingual curriculum 1 (vi-en, intermediate)
    - Select an appropriate writing topic during implementation (evergreen, accessible for intermediate learners, suitable for scaffolded sentence-to-paragraph writing progression)
    - Define 10 vocabulary words in 2 groups: W1 (5 words for S1), W2 (5 words for S2) — words useful for the writing tasks, at intermediate level
    - Write MODEL_TEXT_1 (S1 reading passage containing W1 words), MODEL_TEXT_2 (S2 passage with different angle, containing W2 words), FULL_ARTICLE (S4 combined/extended passage)
    - Write persuasive Vietnamese description (5-beat structure, writing-journey-focused), preview (~150 words in Vietnamese about the writing progression)
    - Write curriculum title in format "Luyện Viết: <Tên Chủ Đề>" — no difficulty level descriptors
    - Write 4 sessions of hand-crafted content:
      - S1 (9 activities): introAudio (welcome), introAudio (bilingual vocab teaching — 5 words, Vietnamese explanations + English examples), viewFlashcards(W1), vocabLevel1(W1), vocabLevel2(W1), introAudio (reading intro), reading(MODEL_TEXT_1), readAlong(MODEL_TEXT_1), writingSentence (5 items with bilingual prompts — Vietnamese instruction + "Ví dụ:" English example, full scaffolding)
      - S2 (9 activities): introAudio (welcome), introAudio (bilingual vocab teaching — 5 new words), viewFlashcards(W2), vocabLevel1(W2), vocabLevel2(W2), introAudio (reading intro), reading(MODEL_TEXT_2), readAlong(MODEL_TEXT_2), writingSentence (5 items, slightly less scaffolding than S1)
      - S3 (7 activities): introAudio (welcome), introAudio (review all vocab), viewFlashcards(ALL), vocabLevel1(ALL), vocabLevel2(ALL), writingSentence (3 items combining S1+S2 vocab), writingParagraph (guided paragraph — structural guidance in Vietnamese, vocabList=ALL)
      - S4 (5 activities): introAudio (welcome), reading(FULL_ARTICLE), readAlong(FULL_ARTICLE), writingParagraph (less scaffolded — independent writing, vocabList=ALL), introAudio (farewell 400-600 words reviewing all 10 words)
    - Activity titles use Vietnamese prefixes: "Flashcards:", "Đọc:", "Nghe:", "Viết:"
    - readAlong description: "Nghe bài đọc và theo dõi."
    - Include all activity metadata (title, description) and session titles (Buổi 1, Buổi 2, etc.)
    - Include inline `STRIP_KEYS` set and `strip_keys()` function
    - Include inline `validate(content, "bilingual")` function checking Properties 1-16 from design
    - API call: `curriculum/create` with `language="en"`, `userLanguage="vi"`, `content=json.dumps(content)`
    - Print created curriculum ID
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 3.1, 3.2, 3.3, 3.5, 3.6, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 6.5, 6.6, 7.1, 7.2, 7.5, 8.1, 8.2, 8.3, 8.4, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 10.1, 13.1, 13.3, 14.1, 14.2, 15.1, 15.3, 15.5, 16.1, 16.2, 17.1, 17.2, 17.4, 19.1, 19.2, 20.6_

  - [x] 1.4 Create `writing-focus-curriculum/create_writing_4_<topic>.py` — Bilingual curriculum 2 (vi-en, intermediate)
    - Select a different writing topic (same criteria as 1.3 — evergreen, accessible for intermediate learners, suitable for scaffolded writing)
    - Same structure as 1.3: 10 vocab words (W1+W2), MODEL_TEXT_1, MODEL_TEXT_2, FULL_ARTICLE, 4 sessions (9, 9, 7, 5 activities)
    - All text content (description, preview, introAudio scripts, reading passages, writing prompts) hand-written for this specific topic — no templates or reuse from curriculum 3
    - Include inline `strip_keys()`, `validate(content, "bilingual")`, and API call with `language="en"`, `userLanguage="vi"`
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 3.1, 3.2, 3.3, 3.5, 3.6, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 6.5, 6.6, 7.1, 7.2, 7.5, 8.1, 8.2, 8.3, 8.4, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 10.1, 13.1, 13.3, 14.1, 14.2, 15.1, 15.3, 15.5, 16.1, 16.2, 17.1, 17.2, 17.4, 19.1, 19.2, 20.6_

- [x] 2. Checkpoint — All 4 curriculum scripts created
  - Ensure all 4 curriculum scripts pass `validate(content, variant)` locally. Verify each script selects a different topic, has 10 unique vocab words, correct session/activity structure (single-language: 8,8,5,5; bilingual: 9,9,7,5), no strip keys, no difficulty level in titles, and writingParagraph in every session (single-language) or S3-S4 (bilingual). Ask the user if questions arise.

- [x] 3. Orchestrator & Execution
  - [x] 3.1 Create `writing-focus-curriculum/create_writing_focus_series.py` — Collection + 2 Series orchestrator
    - Create collection via `curriculum-collection/create` with title, persuasive description, `isPublic: true`
    - Create Series 1 (en-en) via `curriculum-series/create` with English title "Writing Focus", English description (≤255 chars), `isPublic: true`
    - Create Series 2 (vi-en) via `curriculum-series/create` with Vietnamese title "Luyện Viết Tiếng Anh", Vietnamese description (≤255 chars), `isPublic: true`
    - Add both series to collection via `curriculum-collection/addSeriesToCollection`
    - Set series display orders: Series 1 = 100, Series 2 = 200 via `curriculum-series/setDisplayOrder`
    - Add 2 en-en curriculum IDs to Series 1 via `curriculum-series/addCurriculum`
    - Add 2 vi-en curriculum IDs to Series 2 via `curriculum-series/addCurriculum`
    - Set curriculum display orders within each series (0, 1) via `curriculum/setDisplayOrder`
    - Token refreshed before each API call
    - _Requirements: 11.1, 11.2, 11.3, 11.4, 11.5, 12.1, 12.2, 13.2_

  - [x] 3.2 Run all 4 curriculum scripts and the orchestrator, verify output
    - Run `python create_writing_1_<topic>.py`, `create_writing_2_<topic>.py`, `create_writing_3_<topic>.py`, `create_writing_4_<topic>.py`
    - Paste curriculum IDs into orchestrator (2 en-en IDs for Series 1, 2 vi-en IDs for Series 2), run `python create_writing_focus_series.py`
    - _Requirements: 13.1, 13.2_

- [x] 4. Checkpoint — Collection, 2 series, and curriculums created
  - Ensure the orchestrator completed successfully. Verify the new collection exists, Series 1 (en-en) has display_order 100 with 2 curriculums (orders 0, 1), Series 2 (vi-en) has display_order 200 with 2 curriculums (orders 0, 1). Ask the user if questions arise.

- [x] 5. Post-creation verification
  - [x] 5.1 Run SQL verification queries against the database
    - Verify the new "Writing Focus" collection exists and is public
    - Verify the collection has exactly 2 series
    - Verify Series 1 (en-en) has exactly 2 curriculums with display orders 0, 1
    - Verify Series 2 (vi-en) has exactly 2 curriculums with display orders 0, 1
    - Verify series display orders: 100 (Series 1), 200 (Series 2)
    - Verify language homogeneity via `curriculum_series_language_list` (Series 1: all en-en, Series 2: all vi-en)
    - Verify all 4 curriculums are private (`is_public = false`)
    - Verify no level gap violations via `curriculum_series_level_gap`
    - _Requirements: 11.1, 11.2, 11.3, 11.4, 11.5, 12.1, 12.2, 15.1, 15.2, 15.3, 15.4, 16.1_

- [x] 6. Cleanup — Delete scripts and write README
  - [x] 6.1 Delete all curriculum and orchestrator scripts from `writing-focus-curriculum/`, write `README.md`
    - README includes: collection ID and title, Series 1 ID and title, Series 2 ID and title, 4 curriculum IDs and titles (with topics), how content was created (writing_focus type, 2 variants), SQL queries to find the curriculums in the DB, enough context to recreate if needed
    - _Requirements: 13.4, 18.1, 18.2, 18.3_

- [x] 7. Final checkpoint
  - Ensure all 4 curriculums exist in DB, the new collection and both series are correctly wired, all source scripts are deleted, and the folder contains only README.md. Ask the user if questions arise.

## Notes

- Each curriculum script is ~400-600 lines with all hand-written content — no templates or string interpolation for learner-facing text
- Topics are NOT pre-selected — the implementer selects appropriate topics during implementation based on the criteria (evergreen, intellectually rich for single-language; accessible for bilingual)
- Two series are required because single-language (en-en) and bilingual (vi-en) curriculums cannot share a series (language homogeneity rule)
- The `validate(content, variant)` function in each script checks structural properties (10 words, 4 sessions, activity sequences, title/description presence, no strip keys, vocab in passages, writing prompt format, farewell word review, no difficulty level in title) before making the API call
- The orchestrator creates ONE collection and TWO series (unlike podcast-based which created one collection + one series)
- Orchestrator takes 4 curriculum IDs as constants (pasted from curriculum script output): 2 en-en for Series 1, 2 vi-en for Series 2
- Single-language variant: `writingParagraph` in every session (S1-S4), prompts escalate from paragraph response → compare/contrast → analytical essay → argumentative capstone
- Bilingual variant: `writingSentence` dominates S1-S3, `writingParagraph` introduced at S3-S4, prompts in Vietnamese with English responses
- No `youtubeUrl` — writing_focus curriculums use authored model texts, not media excerpts
- No `speakFlashcards`, `speakReading`, or `vocabLevel3` in any session
- All series descriptions must be under 255 characters (PostgreSQL varchar limit)
- Token is refreshed via `get_firebase_id_token(UID)` before each API call
