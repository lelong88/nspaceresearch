# Implementation Plan: Speaking-Focus Curriculum

## Overview

Create a new collection "Speaking Focus" and populate it with 2 series: Series 1 (2 single-language en-en advanced curriculums) and Series 2 (2 bilingual vi-en intermediate curriculums). Each curriculum is a standalone Python script with hand-written content demonstrating the `speaking_focus` curriculum type — speaking as the centerpiece, no writing activities, 10 vocab words across 2 sessions, escalating speak prompts, `speakFlashcards`/`speakReading` retained as pronunciation scaffolding. One orchestrator script handles collection + both series + all wiring. After verification, scripts are deleted and README is written.

## Tasks

- [x] 1. Curriculum Scripts
  - [x] 1.1 Create `speaking-focus-curriculum/create_speaking_1_<topic>.py` — Single-language curriculum 1 (en-en, advanced)
    - Select an appropriate speaking topic during implementation (evergreen, intellectually rich, suitable for debate/argumentation/presentation at advanced level)
    - Define 10 vocabulary words in 2 groups: W1 (5 words for S1), W2 (5 words for S2) — words that enable the learner to express ideas about the topic in speech
    - Write PASSAGE_1 (S1 reading passage introducing the topic, containing W1 words in context), PASSAGE_2 (S2 passage presenting a different angle on the same topic, containing W2 words), FULL_ARTICLE (S4 combined/extended passage)
    - Write persuasive English description (5-beat structure, speaking-journey-focused), preview (~150 words about the speaking progression and topic)
    - Write curriculum title in format "Speaking Focus: <Topic Title>" — no difficulty level descriptors
    - Write 4 sessions of hand-crafted content:
      - S1 (8 activities): introAudio (teach 5 words with pronunciation emphasis + explain speaking tasks, 500-800 words), viewFlashcards(W1), speakFlashcards(W1), vocabLevel1(W1), reading(PASSAGE_1), speakReading(PASSAGE_1), speak (open-ended: explain concept using ≥3 new words), speak (role-play: conversational scenario)
      - S2 (8 activities): introAudio (teach 5 more words + recap S1 speaking, 500-800 words), viewFlashcards(W2), speakFlashcards(W2), vocabLevel1(W2), reading(PASSAGE_2), speakReading(PASSAGE_2), speak (summarize both passages orally), speak (debate: argue for/against a position from the text)
      - S3 (6 activities): introAudio (review all 10 words), viewFlashcards(ALL), speakFlashcards(ALL), vocabLevel1(ALL), speak (2-minute monologue on the topic), speak (respond to a counter-argument)
      - S4 (7 activities): introAudio (recap journey), reading(FULL_ARTICLE), speakReading(FULL_ARTICLE), readAlong(FULL_ARTICLE), speak (present a 2-minute summary of the article), speak (impromptu response to a follow-up question), introAudio (farewell 400-600 words reviewing all 10 words)
    - speak activity data shape: `{ text: "<prompt>", audioSpeed: -0.3 }` — no `lessonUniqueId`
    - Activity titles use English prefixes: "Flashcards:", "Read:", "Listen:", "Speak:"
    - readAlong description: "Listen and follow along."
    - Include all activity metadata (title, description) and session titles
    - Include inline `STRIP_KEYS` set and `strip_keys()` function
    - Include inline `validate(content, "single-language")` function checking Properties 1-18 from design
    - API call: `curriculum/create` with `language="en"`, `userLanguage="en"`, `content=json.dumps(content)`
    - Print created curriculum ID
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 3.1, 3.2, 3.3, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 4.4, 6.1, 6.2, 6.3, 7.1, 7.2, 7.3, 7.4, 8.1, 8.2, 8.3, 8.4, 8.6, 9.1, 9.2, 9.3, 9.4, 10.1, 10.2, 10.4, 10.5, 10.6, 10.7, 10.8, 11.1, 14.1, 14.3, 15.1, 15.2, 16.1, 16.2, 16.5, 17.1, 17.2, 18.1, 18.2, 18.3, 18.4, 18.5_

  - [x] 1.2 Create `speaking-focus-curriculum/create_speaking_2_<topic>.py` — Single-language curriculum 2 (en-en, advanced)
    - Select a different speaking topic (same criteria as 1.1 — evergreen, intellectually rich, suitable for debate/argumentation/presentation)
    - Same structure as 1.1: 10 vocab words (W1+W2), PASSAGE_1, PASSAGE_2, FULL_ARTICLE, 4 sessions (8, 8, 6, 7 activities)
    - All text content (description, preview, introAudio scripts, reading passages, speak prompts) hand-written for this specific topic — no templates or reuse from curriculum 1
    - Include inline `strip_keys()`, `validate(content, "single-language")`, and API call with `language="en"`, `userLanguage="en"`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 3.1, 3.2, 3.3, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 4.4, 6.1, 6.2, 6.3, 7.1, 7.2, 7.3, 7.4, 8.1, 8.2, 8.3, 8.4, 8.6, 9.1, 9.2, 9.3, 9.4, 10.1, 10.2, 10.4, 10.5, 10.6, 10.7, 10.8, 11.1, 14.1, 14.3, 15.1, 15.2, 16.1, 16.2, 16.5, 17.1, 17.2, 18.1, 18.2, 18.3, 18.4, 18.5_

  - [x] 1.3 Create `speaking-focus-curriculum/create_speaking_3_<topic>.py` — Bilingual curriculum 1 (vi-en, intermediate)
    - Select an appropriate speaking topic during implementation (evergreen, accessible for intermediate learners, suitable for scaffolded speaking progression)
    - Define 10 vocabulary words in 2 groups: W1 (5 words for S1), W2 (5 words for S2) — words useful for the speaking tasks, at intermediate level
    - Write PASSAGE_1 (S1 reading passage containing W1 words), PASSAGE_2 (S2 passage with different angle, containing W2 words), FULL_ARTICLE (S4 combined/extended passage)
    - Write persuasive Vietnamese description (5-beat structure, speaking-journey-focused), preview (~150 words in Vietnamese about the speaking progression)
    - Write curriculum title in format "Luyện Nói: <Tên Chủ Đề>" — no difficulty level descriptors
    - Write 4 sessions of hand-crafted content:
      - S1 (11 activities): introAudio (welcome), introAudio (bilingual vocab teaching with pronunciation — 5 words, Vietnamese explanations + English examples), viewFlashcards(W1), speakFlashcards(W1), vocabLevel1(W1), vocabLevel2(W1), introAudio (reading intro), reading(PASSAGE_1), speakReading(PASSAGE_1), readAlong(PASSAGE_1), speak (guided: say a sentence using a word, with example provided in Vietnamese prompt)
      - S2 (11 activities): introAudio (welcome), introAudio (bilingual vocab teaching — 5 new words), viewFlashcards(W2), speakFlashcards(W2), vocabLevel1(W2), vocabLevel2(W2), introAudio (reading intro), reading(PASSAGE_2), speakReading(PASSAGE_2), readAlong(PASSAGE_2), speak (slightly less scaffolded: describe topic using 2-3 new words)
      - S3 (8 activities): introAudio (welcome), introAudio (review all vocab), viewFlashcards(ALL), speakFlashcards(ALL), vocabLevel1(ALL), vocabLevel2(ALL), speak (describe a picture/scenario using vocab), speak (answer a question about the topic)
      - S4 (6 activities): introAudio (welcome), reading(FULL_ARTICLE), speakReading(FULL_ARTICLE), readAlong(FULL_ARTICLE), speak (summarize what you read in 3-4 sentences), introAudio (farewell 400-600 words reviewing all 10 words)
    - speak activity data shape: `{ text: "<prompt in Vietnamese>", audioSpeed: -0.3 }` — no `lessonUniqueId`
    - Activity titles use Vietnamese prefixes: "Flashcards:", "Đọc:", "Nghe:", "Nói:"
    - readAlong description: "Nghe bài đọc và theo dõi."
    - Include all activity metadata (title, description) and session titles (Buổi 1, Buổi 2, etc.)
    - Include inline `STRIP_KEYS` set and `strip_keys()` function
    - Include inline `validate(content, "bilingual")` function checking Properties 1-18 from design
    - API call: `curriculum/create` with `language="en"`, `userLanguage="vi"`, `content=json.dumps(content)`
    - Print created curriculum ID
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 3.1, 3.2, 3.4, 3.5, 3.6, 3.7, 5.1, 5.2, 5.3, 5.4, 5.5, 6.1, 6.2, 6.3, 7.5, 7.6, 8.1, 8.2, 8.3, 8.5, 8.6, 9.1, 9.2, 9.3, 9.4, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 11.1, 14.1, 14.3, 15.1, 15.2, 16.1, 16.3, 16.5, 17.1, 17.2, 18.6_

  - [x] 1.4 Create `speaking-focus-curriculum/create_speaking_4_<topic>.py` — Bilingual curriculum 2 (vi-en, intermediate)
    - Select a different speaking topic (same criteria as 1.3 — evergreen, accessible for intermediate learners, suitable for scaffolded speaking)
    - Same structure as 1.3: 10 vocab words (W1+W2), PASSAGE_1, PASSAGE_2, FULL_ARTICLE, 4 sessions (11, 11, 8, 6 activities)
    - All text content (description, preview, introAudio scripts, reading passages, speak prompts) hand-written for this specific topic — no templates or reuse from curriculum 3
    - Include inline `strip_keys()`, `validate(content, "bilingual")`, and API call with `language="en"`, `userLanguage="vi"`
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 3.1, 3.2, 3.4, 3.5, 3.6, 3.7, 5.1, 5.2, 5.3, 5.4, 5.5, 6.1, 6.2, 6.3, 7.5, 7.6, 8.1, 8.2, 8.3, 8.5, 8.6, 9.1, 9.2, 9.3, 9.4, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 11.1, 14.1, 14.3, 15.1, 15.2, 16.1, 16.3, 16.5, 17.1, 17.2, 18.6_

- [x] 2. Checkpoint — All 4 curriculum scripts created
  - Ensure all 4 curriculum scripts pass `validate(content, variant)` locally. Verify each script selects a different topic, has 10 unique vocab words, correct session/activity structure (single-language: 8,8,6,7; bilingual: 11,11,8,6), no strip keys, no difficulty level in titles, no writing activities, speak data shape correct (audioSpeed=-0.3, no lessonUniqueId), and speak count per session matches variant (single-language: 2 per session; bilingual: 1,1,2,1). Ask the user if questions arise.

- [x] 3. Orchestrator & Execution
  - [x] 3.1 Create `speaking-focus-curriculum/create_speaking_focus_series.py` — Collection + 2 Series orchestrator
    - Create collection via `curriculum-collection/create` with title, persuasive description, `isPublic: true`
    - Create Series 1 (en-en) via `curriculum-series/create` with English title "Speaking Focus", English description (≤255 chars), `isPublic: true`
    - Create Series 2 (vi-en) via `curriculum-series/create` with Vietnamese title "Luyện Nói Tiếng Anh", Vietnamese description (≤255 chars), `isPublic: true`
    - Add both series to collection via `curriculum-collection/addSeriesToCollection`
    - Set series display orders: Series 1 = 100, Series 2 = 200 via `curriculum-series/setDisplayOrder`
    - Add 2 en-en curriculum IDs to Series 1 via `curriculum-series/addCurriculum`
    - Add 2 vi-en curriculum IDs to Series 2 via `curriculum-series/addCurriculum`
    - Set curriculum display orders within each series (0, 1) via `curriculum/setDisplayOrder`
    - Token refreshed before each API call
    - _Requirements: 12.1, 12.2, 12.3, 12.4, 12.5, 12.6, 13.1, 13.2, 14.2_

  - [x] 3.2 Run all 4 curriculum scripts and the orchestrator, verify output
    - Run `python create_speaking_1_<topic>.py`, `create_speaking_2_<topic>.py`, `create_speaking_3_<topic>.py`, `create_speaking_4_<topic>.py`
    - Paste curriculum IDs into orchestrator (2 en-en IDs for Series 1, 2 vi-en IDs for Series 2), run `python create_speaking_focus_series.py`
    - _Requirements: 14.1, 14.2_

- [x] 4. Checkpoint — Collection, 2 series, and curriculums created
  - Ensure the orchestrator completed successfully. Verify the new collection exists, Series 1 (en-en) has display_order 100 with 2 curriculums (orders 0, 1), Series 2 (vi-en) has display_order 200 with 2 curriculums (orders 0, 1). Ask the user if questions arise.

- [x] 5. Post-creation verification
  - [x] 5.1 Run SQL verification queries against the database
    - Verify the new "Speaking Focus" collection exists and is public
    - Verify the collection has exactly 2 series
    - Verify Series 1 (en-en) has exactly 2 curriculums with display orders 0, 1
    - Verify Series 2 (vi-en) has exactly 2 curriculums with display orders 0, 1
    - Verify series display orders: 100 (Series 1), 200 (Series 2)
    - Verify language homogeneity via `curriculum_series_language_list` (Series 1: all en-en, Series 2: all vi-en)
    - Verify all 4 curriculums are private (`is_public = false`)
    - Verify no level gap violations via `curriculum_series_level_gap`
    - _Requirements: 12.1, 12.2, 12.3, 12.4, 12.5, 12.6, 13.1, 13.2, 16.1, 16.2, 16.3, 16.4, 17.1_

- [x] 6. Cleanup — Delete scripts and write README
  - [x] 6.1 Delete all curriculum and orchestrator scripts from `speaking-focus-curriculum/`, write `README.md`
    - README includes: collection ID and title, Series 1 ID and title, Series 2 ID and title, 4 curriculum IDs and titles (with topics), how content was created (speaking_focus type, 2 variants), SQL queries to find the curriculums in the DB, enough context to recreate if needed
    - _Requirements: 14.4, 19.1, 19.2, 19.3_

- [x] 7. Final checkpoint
  - Ensure all 4 curriculums exist in DB, the new collection and both series are correctly wired, all source scripts are deleted, and the folder contains only README.md. Ask the user if questions arise.

## Notes

- Each curriculum script is ~400-600 lines with all hand-written content — no templates or string interpolation for learner-facing text
- Topics are NOT pre-selected — the implementer selects appropriate topics during implementation based on the criteria (evergreen, intellectually rich for single-language; accessible for bilingual)
- Two series are required because single-language (en-en) and bilingual (vi-en) curriculums cannot share a series (language homogeneity rule)
- The `validate(content, variant)` function in each script checks structural properties (10 words, 4 sessions, activity sequences, title/description presence, no strip keys, vocab in passages, speak data shape, speak count per session, farewell word review, no difficulty level in title, no writing activities) before making the API call
- The orchestrator creates ONE collection and TWO series (same pattern as writing-focus-curriculum)
- Orchestrator takes 4 curriculum IDs as constants (pasted from curriculum script output): 2 en-en for Series 1, 2 vi-en for Series 2
- Single-language variant: 2 `speak` activities per session, prompts escalate from explain → role-play → summarize → debate → monologue → counter-argument → presentation → impromptu response
- Bilingual variant: 1 `speak` in S1-S2, 2 in S3, 1 in S4. Prompts are simpler with examples in Vietnamese
- `speak` activity data shape: `{ text: string, audioSpeed: -0.3 }` — no `lessonUniqueId` (auto-generated)
- No `writingSentence`, `writingParagraph`, or `vocabLevel3` in any session
- Single-language drops `vocabLevel2` as well; bilingual keeps it
- `speakFlashcards` and `speakReading` are retained as pronunciation scaffolding (distinct from open-ended `speak`)
- No `youtubeUrl` — speaking_focus curriculums use authored reading passages, not media excerpts
- All series descriptions must be under 255 characters (PostgreSQL varchar limit)
- Token is refreshed via `get_firebase_id_token(UID)` before each API call
- Follow the exact pattern from `writing-focus-curriculum/` for script structure, orchestrator, and validation
