# Implementation Plan: Audio-Guide Curriculum

## Overview

Create a new collection "Audio Guide" and populate it with 2 series: Series 1 (2 single-language en-en advanced curriculums) and Series 2 (2 bilingual vi-en intermediate curriculums). Each curriculum is a standalone Python script with hand-written content demonstrating the `audio_guide` curriculum type — introAudio as the centerpiece (800-1000 words, 2× normal), multiple introAudio per session, no speaking, no writing, pure receptive learning like a podcast with flashcard reinforcement. One orchestrator script handles collection + both series + all wiring. After verification, scripts are deleted and README is written.

## Tasks

- [x] 1. Curriculum Scripts
  - [x] 1.1 Create `audio-guide-curriculum/create_audio_1_<topic>.py` — Single-language curriculum 1 (en-en, advanced)
    - Select an appropriate audio-guide topic during implementation (evergreen, intellectually rich, suitable for deep-dive podcast-style audio lessons at advanced level)
    - Define 10 vocabulary words in 2 groups: W1 (5 words for S1), W2 (5 words for S2) — words that enable the learner to follow extended audio content about the topic
    - Write PASSAGE_1 (S1 readAlong passage — short passage using W1 words in context), PASSAGE_2 (S2 readAlong passage using W2 words), FULL_ARTICLE (S4 combined/extended passage for both reading and readAlong)
    - Write persuasive English description (5-beat structure, audio-learning-focused), preview (~150 words about the audio learning journey and topic)
    - Write curriculum title in format "Audio Guide: <Topic Title>" — no difficulty level descriptors
    - Write 4 sessions of hand-crafted content:
      - S1 (5 activities): introAudio (extended: 800-1000 words — deep dive into topic + teach 5 words with rich context, examples, etymology), introAudio (supplementary: real-world anecdotes and usage patterns for the 5 words), viewFlashcards(W1), vocabLevel1(W1), readAlong(PASSAGE_1)
      - S2 (5 activities): introAudio (extended: 800-1000 words — second angle on topic + teach 5 more words, recap S1 words), introAudio (supplementary: compare/contrast S1 and S2 words, usage nuances), viewFlashcards(W2), vocabLevel1(W2), readAlong(PASSAGE_2)
      - S3 (4 activities): introAudio (extended review: walk through all 10 words with fresh examples and deeper analysis), viewFlashcards(ALL), vocabLevel1(ALL), vocabLevel2(ALL)
      - S4 (4 activities): introAudio (recap the full learning journey — what was covered, why it matters), reading(FULL_ARTICLE), readAlong(FULL_ARTICLE), introAudio (farewell 400-600 words — review each word one final time with a fresh example)
    - Activity titles use English prefixes: "Flashcards:", "Read:", "Listen:"
    - readAlong description: "Listen and follow along."
    - Include all activity metadata (title, description) and session titles
    - Include inline `STRIP_KEYS` set and `strip_keys()` function
    - Include inline `validate(content, "single-language")` function checking Properties 1-20 from design
    - API call: `curriculum/create` with `language="en"`, `userLanguage="en"`, `content=json.dumps(content)`
    - Print created curriculum ID
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 4.1, 4.2, 4.3, 4.4, 4.6, 4.8, 4.9, 5.1, 5.3, 5.4, 6.1, 6.2, 6.4, 6.5, 6.6, 7.1, 7.2, 7.3, 7.4, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 9.1, 12.1, 12.3, 13.1, 13.2, 14.1, 14.2, 14.5, 15.1, 15.2, 16.1, 16.2, 16.3, 16.4, 16.7_

  - [x] 1.2 Create `audio-guide-curriculum/create_audio_2_<topic>.py` — Single-language curriculum 2 (en-en, advanced)
    - Select a different audio-guide topic (same criteria as 1.1 — evergreen, intellectually rich, suitable for podcast-style audio lessons)
    - Same structure as 1.1: 10 vocab words (W1+W2), PASSAGE_1, PASSAGE_2, FULL_ARTICLE, 4 sessions (5, 5, 4, 4 activities)
    - All text content (description, preview, introAudio scripts, readAlong passages) hand-written for this specific topic — no templates or reuse from curriculum 1
    - Include inline `strip_keys()`, `validate(content, "single-language")`, and API call with `language="en"`, `userLanguage="en"`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 4.1, 4.2, 4.3, 4.4, 4.6, 4.8, 4.9, 5.1, 5.3, 5.4, 6.1, 6.2, 6.4, 6.5, 6.6, 7.1, 7.2, 7.3, 7.4, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 9.1, 12.1, 12.3, 13.1, 13.2, 14.1, 14.2, 14.5, 15.1, 15.2, 16.1, 16.2, 16.3, 16.4, 16.7_

  - [x] 1.3 Create `audio-guide-curriculum/create_audio_3_<topic>.py` — Bilingual curriculum 1 (vi-en, intermediate)
    - Select an appropriate audio-guide topic during implementation (evergreen, accessible for intermediate learners, suitable for bilingual podcast-style audio lessons with mini-stories)
    - Define 10 vocabulary words in 2 groups: W1 (5 words for S1), W2 (5 words for S2) — words useful for listening comprehension, at intermediate level
    - Write MINI_STORY_1 (S1 mini-story in English using W1 words at slow pace — also used as readAlong text), MINI_STORY_2 (S2 mini-story using W2 words), FULL_ARTICLE (S4 combined/extended passage — bilingual)
    - Write persuasive Vietnamese description (5-beat structure, audio-learning-focused), preview (~150 words in Vietnamese about the audio learning journey)
    - Write curriculum title in format "Học Qua Nghe: <Tên Chủ Đề>" — no difficulty level descriptors
    - Write 4 sessions of hand-crafted content:
      - S1 (6 activities): introAudio (bilingual: explain topic in Vietnamese, teach 5 words with pronunciation, definitions in both languages, 3 example sentences each — 800-1000 words), introAudio (supplementary: usage tips, common mistakes, cultural context — in Vietnamese), introAudio (mini-story using all 5 words — in English, slow pace), viewFlashcards(W1), vocabLevel1(W1), readAlong(MINI_STORY_1 — listen to the mini-story again)
      - S2 (6 activities): introAudio (teach 5 more words, brief recap of S1 — 800-1000 words), introAudio (supplementary), introAudio (mini-story with S2 words), viewFlashcards(W2), vocabLevel1(W2), readAlong(MINI_STORY_2)
      - S3 (5 activities): introAudio (review all 10 words in Vietnamese with fresh examples), introAudio (quiz-style: "What word means...?" with pauses for thinking), viewFlashcards(ALL), vocabLevel1(ALL), vocabLevel2(ALL)
      - S4 (4 activities): introAudio (recap journey), reading(FULL_ARTICLE), readAlong(FULL_ARTICLE), introAudio (farewell 400-600 words — each word reviewed with a fresh sentence)
    - Activity titles use Vietnamese prefixes: "Flashcards:", "Đọc:", "Nghe:"
    - readAlong description: "Nghe bài nghe và theo dõi."
    - Include all activity metadata (title, description) and session titles (Buổi 1, Buổi 2, etc.)
    - Include inline `STRIP_KEYS` set and `strip_keys()` function
    - Include inline `validate(content, "bilingual")` function checking Properties 1-20 from design
    - API call: `curriculum/create` with `language="en"`, `userLanguage="vi"`, `content=json.dumps(content)`
    - Print created curriculum ID
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 4.2, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.2, 5.3, 5.4, 6.1, 6.2, 6.4, 6.5, 6.6, 7.1, 7.2, 7.3, 7.4, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 9.1, 12.1, 12.3, 13.1, 13.2, 14.1, 14.3, 14.5, 15.1, 15.2, 16.5, 16.6, 16.7_

  - [x] 1.4 Create `audio-guide-curriculum/create_audio_4_<topic>.py` — Bilingual curriculum 2 (vi-en, intermediate)
    - Select a different audio-guide topic (same criteria as 1.3 — evergreen, accessible for intermediate learners, suitable for bilingual audio lessons with mini-stories)
    - Same structure as 1.3: 10 vocab words (W1+W2), MINI_STORY_1, MINI_STORY_2, FULL_ARTICLE, 4 sessions (6, 6, 5, 4 activities)
    - All text content (description, preview, introAudio scripts, mini-stories, readAlong passages) hand-written for this specific topic — no templates or reuse from curriculum 3
    - Include inline `strip_keys()`, `validate(content, "bilingual")`, and API call with `language="en"`, `userLanguage="vi"`
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 4.2, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.2, 5.3, 5.4, 6.1, 6.2, 6.4, 6.5, 6.6, 7.1, 7.2, 7.3, 7.4, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 9.1, 12.1, 12.3, 13.1, 13.2, 14.1, 14.3, 14.5, 15.1, 15.2, 16.5, 16.6, 16.7_

- [x] 2. Checkpoint — All 4 curriculum scripts created
  - Ensure all 4 curriculum scripts pass `validate(content, variant)` locally. Verify each script selects a different topic, has 10 unique vocab words, correct session/activity structure (single-language: 5,5,4,4; bilingual: 6,6,5,4), no strip keys, no difficulty level in titles, no speaking activities, no writing activities, no vocabLevel3, vocabLevel2 only in S3, reading only in S4, readAlong in S1/S2/S4, correct introAudio count per session (single-language: 2,2,1,2; bilingual: 3,3,2,2). Ask the user if questions arise.

- [x] 3. Orchestrator & Execution
  - [x] 3.1 Create `audio-guide-curriculum/create_audio_guide_series.py` — Collection + 2 Series orchestrator
    - Create collection via `curriculum-collection/create` with title, persuasive description, `isPublic: true`
    - Create Series 1 (en-en) via `curriculum-series/create` with English title "Audio Guide", English description (≤255 chars), `isPublic: true`
    - Create Series 2 (vi-en) via `curriculum-series/create` with Vietnamese title "Học Qua Nghe", Vietnamese description (≤255 chars), `isPublic: true`
    - Add both series to collection via `curriculum-collection/addSeriesToCollection`
    - Set series display orders: Series 1 = 100, Series 2 = 200 via `curriculum-series/setDisplayOrder`
    - Add 2 en-en curriculum IDs to Series 1 via `curriculum-series/addCurriculum`
    - Add 2 vi-en curriculum IDs to Series 2 via `curriculum-series/addCurriculum`
    - Set curriculum display orders within each series (0, 1) via `curriculum/setDisplayOrder`
    - Token refreshed before each API call
    - _Requirements: 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 11.1, 11.2, 12.2_

  - [x] 3.2 Run all 4 curriculum scripts and the orchestrator, verify output
    - Run `python create_audio_1_<topic>.py`, `create_audio_2_<topic>.py`, `create_audio_3_<topic>.py`, `create_audio_4_<topic>.py`
    - Paste curriculum IDs into orchestrator (2 en-en IDs for Series 1, 2 vi-en IDs for Series 2), run `python create_audio_guide_series.py`
    - _Requirements: 12.1, 12.2_

- [x] 4. Checkpoint — Collection, 2 series, and curriculums created
  - Ensure the orchestrator completed successfully. Verify the new collection exists, Series 1 (en-en) has display_order 100 with 2 curriculums (orders 0, 1), Series 2 (vi-en) has display_order 200 with 2 curriculums (orders 0, 1). Ask the user if questions arise.

- [x] 5. Post-creation verification
  - [x] 5.1 Run SQL verification queries against the database
    - Verify the new "Audio Guide" collection exists and is public
    - Verify the collection has exactly 2 series
    - Verify Series 1 (en-en) has exactly 2 curriculums with display orders 0, 1
    - Verify Series 2 (vi-en) has exactly 2 curriculums with display orders 0, 1
    - Verify series display orders: 100 (Series 1), 200 (Series 2)
    - Verify language homogeneity via `curriculum_series_language_list` (Series 1: all en-en, Series 2: all vi-en)
    - Verify all 4 curriculums are private (`is_public = false`)
    - Verify no level gap violations via `curriculum_series_level_gap`
    - _Requirements: 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 11.1, 11.2, 14.1, 14.2, 14.3, 14.4, 15.1_

- [x] 6. Cleanup — Delete scripts and write README
  - [x] 6.1 Delete all curriculum and orchestrator scripts from `audio-guide-curriculum/`, write `README.md`
    - README includes: collection ID and title, Series 1 ID and title, Series 2 ID and title, 4 curriculum IDs and titles (with topics), how content was created (audio_guide type, 2 variants), SQL queries to find the curriculums in the DB, enough context to recreate if needed
    - _Requirements: 12.4, 17.1, 17.2, 17.3_

- [x] 7. Final checkpoint
  - Ensure all 4 curriculums exist in DB, the new collection and both series are correctly wired, all source scripts are deleted, and the folder contains only README.md. Ask the user if questions arise.

## Notes

- Each curriculum script is ~500-800 lines with all hand-written content — no templates or string interpolation for learner-facing text
- Topics are NOT pre-selected — the implementer selects appropriate topics during implementation based on the criteria (evergreen, intellectually rich for single-language; accessible for bilingual)
- Two series are required because single-language (en-en) and bilingual (vi-en) curriculums cannot share a series (language homogeneity rule)
- The `validate(content, variant)` function in each script checks structural properties (10 words, 4 sessions, activity sequences, title/description presence, no strip keys, vocab in passages, introAudio count per session, farewell word review, no difficulty level in title, no speaking activities, no writing activities, no vocabLevel3, vocabLevel2 only in S3, reading only in S4, readAlong in S1/S2/S4) before making the API call
- The orchestrator creates ONE collection and TWO series (same pattern as writing-focus-curriculum and speaking-focus-curriculum)
- Orchestrator takes 4 curriculum IDs as constants (pasted from curriculum script output): 2 en-en for Series 1, 2 vi-en for Series 2
- KEY DIFFERENTIATOR: introAudio scripts are 800-1000 words (2× the normal 400-600 words) — the audio IS the lesson, not just the intro
- Single-language variant: 2 introAudio per learning session (S1-S2) — one extended, one supplementary
- Bilingual variant: 3 introAudio per learning session (S1-S2) — one bilingual vocab teaching, one supplementary, one mini-story in target_language at slow pace
- Bilingual S3 has a quiz-style introAudio ("What word means...?" with pauses for thinking)
- No `speakFlashcards`, `speakReading`, `speak`, `writingSentence`, `writingParagraph` in any session — pure receptive learning
- No `vocabLevel3` anywhere. `vocabLevel2` only in S3 (review session)
- `readAlong` replaces `reading` in S1-S2. S4 is the only session with a `reading` activity
- No `youtubeUrl` — audio_guide curriculums use authored content, not media excerpts
- All series descriptions must be under 255 characters (PostgreSQL varchar limit)
- Token is refreshed via `get_firebase_id_token(UID)` before each API call
- Follow the exact pattern from `speaking-focus-curriculum/` and `writing-focus-curriculum/` for script structure, orchestrator, and validation
- This curriculum type is designed for commuters, passive learners, and people who want to absorb language through listening — the content model is closer to a podcast with flashcard reinforcement
