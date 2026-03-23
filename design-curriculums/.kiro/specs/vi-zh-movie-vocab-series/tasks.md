# Implementation Plan: Vi-Zh Movie-Based Vocab Series

## Overview

Create a new collection "Học Từ Vựng Tiếng Trung Qua Điện Ảnh (通过电影学中文词汇)" and populate it with a single series "Học Từ Vựng Tiếng Trung Qua Phim (通过电影学中文词汇)" containing 4 curriculums. Each curriculum is built around a different iconic Chinese (Mandarin) movie scene, using verbatim simplified Chinese dialogue as reading passages. One standalone Python script per curriculum + one orchestrator for collection/series creation. After verification, scripts are deleted and README is written.

## Tasks

- [x] 1. Chinese Movie Curriculum Scripts
  - [x] 1.1 Create `vi-zh-movie-vocab-series/create_zh_movie_1_<movie>.py` — Chinese Movie 1 curriculum
    - Select an appropriate well-known Chinese (Mandarin) movie scene via web search (clear Mandarin pronunciation, HSK2-HSK3 level dialogue, no excessive profanity or graphic content, well-known on YouTube)
    - Find verbatim Chinese movie dialogue/monologue (simplified characters) via web search and verify accuracy
    - Find the YouTube URL for the scene clip via web search
    - Define 18 Chinese vocabulary words drawn from the dialogue (W1, W2, W3 — 6 each), prioritizing words that are genuinely in the dialogue, at HSK2-HSK3 level, broadly useful, and teachable; avoid single-character function words (的, 了, 在, 是, 和) unless in compound/idiomatic context
    - Write dialogue portions for sessions 1-3 (DIALOGUE_1, DIALOGUE_2, DIALOGUE_3 — segments containing each session's 6 words) and FULL_DIALOGUE (complete scene dialogue/monologue in simplified Chinese)
    - Write persuasive Vietnamese description (5-beat structure, Chinese movie-adapted), preview (~150 words referencing the Chinese movie scene and its themes), and curriculum title in format "Học Qua Phim: '中文电影名' – Mô tả cảnh phim"
    - Write 5 sessions of hand-crafted introAudio scripts: welcome + Chinese movie scene context, vocab teaching (how each Chinese word appears in the dialogue, with pinyin pronunciation), grammar/usage notes for sessions 1-3; congratulations + recap for session 4; farewell with all 18 Chinese words reviewed with pinyin for session 5 (400-600 words)
    - Write writingSentence items with targetVocab, movie-scene-themed context prompts including pinyin in parentheses, and "Ví dụ:" with Chinese example sentences
    - Include `youtubeUrl` at top level of content dict
    - Include all activity metadata (title, description) following naming conventions (Flashcards:/Đọc:/Nghe:/Viết:); readAlong description = "Nghe lời thoại phim và theo dõi."
    - Include inline `STRIP_KEYS` set and `strip_keys()` function
    - Include inline `validate(content)` function checking Properties 1-12 from design
    - API call: `curriculum/create` with `language="zh"`, `userLanguage="vi"`, `content=json.dumps(content)`
    - Print created curriculum ID
    - _Requirements: 1.5, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 3.1, 3.2, 3.3, 3.4, 3.5, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 7.1, 7.2, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 9.1, 11.1, 11.3, 12.1, 12.2, 13.1, 14.1, 14.2, 15.1, 15.2, 15.3, 16.1, 16.2_

  - [x] 1.2 Create `vi-zh-movie-vocab-series/create_zh_movie_2_<movie>.py` — Chinese Movie 2 curriculum
    - Select a different well-known Chinese (Mandarin) movie scene via web search (same criteria as 1.1 — clear Mandarin pronunciation, HSK2-HSK3 level dialogue, no excessive profanity, well-known)
    - Find verbatim Chinese movie dialogue (simplified characters) and YouTube URL for the scene via web search
    - Same structure as 1.1 but with 18 Chinese vocabulary words drawn from this scene's dialogue
    - All text content (description, preview, introAudio scripts, writing prompts) hand-written for this specific Chinese movie scene — no templates or reuse from movie 1
    - Include inline `strip_keys()`, `validate(content)`, `youtubeUrl`, and API call with `language="zh"`, `userLanguage="vi"`
    - _Requirements: 1.5, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 3.1, 3.2, 3.3, 3.4, 3.5, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 7.1, 7.2, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 9.1, 11.1, 11.3, 12.1, 12.2, 13.1, 14.1, 14.2, 15.1, 15.2, 15.3, 16.1, 16.2_

  - [x] 1.3 Create `vi-zh-movie-vocab-series/create_zh_movie_3_<movie>.py` — Chinese Movie 3 curriculum
    - Select a different well-known Chinese (Mandarin) movie scene via web search (same criteria — clear Mandarin pronunciation, HSK2-HSK3 level dialogue, no excessive profanity, well-known)
    - Find verbatim Chinese movie dialogue (simplified characters) and YouTube URL for the scene via web search
    - Same structure as 1.1 but with 18 Chinese vocabulary words drawn from this scene's dialogue
    - All text content hand-written for this specific Chinese movie scene
    - Include inline `strip_keys()`, `validate(content)`, `youtubeUrl`, and API call with `language="zh"`, `userLanguage="vi"`
    - _Requirements: 1.5, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 3.1, 3.2, 3.3, 3.4, 3.5, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 7.1, 7.2, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 9.1, 11.1, 11.3, 12.1, 12.2, 13.1, 14.1, 14.2, 15.1, 15.2, 15.3, 16.1, 16.2_

  - [x] 1.4 Create `vi-zh-movie-vocab-series/create_zh_movie_4_<movie>.py` — Chinese Movie 4 curriculum
    - Select a different well-known Chinese (Mandarin) movie scene via web search (same criteria — clear Mandarin pronunciation, HSK2-HSK3 level dialogue, no excessive profanity, well-known)
    - Find verbatim Chinese movie dialogue (simplified characters) and YouTube URL for the scene via web search
    - Same structure as 1.1 but with 18 Chinese vocabulary words drawn from this scene's dialogue
    - All text content hand-written for this specific Chinese movie scene
    - Include inline `strip_keys()`, `validate(content)`, `youtubeUrl`, and API call with `language="zh"`, `userLanguage="vi"`
    - _Requirements: 1.5, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 3.1, 3.2, 3.3, 3.4, 3.5, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 7.1, 7.2, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 9.1, 11.1, 11.3, 12.1, 12.2, 13.1, 14.1, 14.2, 15.1, 15.2, 15.3, 16.1, 16.2_

- [x] 2. Checkpoint — All 4 Chinese movie curriculum scripts created
  - Ensure all 4 curriculum scripts pass `validate(content)` locally. Verify each script selects a different Chinese movie scene, has 18 unique Chinese vocab words from the dialogue, correct session/activity structure, youtubeUrl present, language="zh"/userLanguage="vi", and no strip keys. Ask the user if questions arise.

- [x] 3. Orchestrator & Execution
  - [x] 3.1 Create `vi-zh-movie-vocab-series/create_zh_movie_series.py` — Collection + Series orchestrator
    - Create collection via `curriculum-collection/create` with title "Học Từ Vựng Tiếng Trung Qua Điện Ảnh (通过电影学中文词汇)", persuasive Vietnamese description, `isPublic: true`
    - Create series via `curriculum-series/create` with title "Học Từ Vựng Tiếng Trung Qua Phim (通过电影学中文词汇)", Vietnamese description (≤255 chars), `isPublic: true`
    - Add series to collection via `curriculum-collection/addSeriesToCollection`
    - Set series display order 100 via `curriculum-series/setDisplayOrder`
    - Add all 4 curriculum IDs to series via `curriculum-series/addCurriculum`
    - Set curriculum display orders (0, 1, 2, 3) via `curriculum/setDisplayOrder`
    - Token refreshed before each API call
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 10.1, 10.2, 10.3, 11.2, 13.3_

  - [x] 3.2 Run all 4 curriculum scripts and the orchestrator, verify output
    - Run `python create_zh_movie_1_<movie>.py`, `create_zh_movie_2_<movie>.py`, `create_zh_movie_3_<movie>.py`, `create_zh_movie_4_<movie>.py`
    - Paste curriculum IDs into orchestrator, run `python create_zh_movie_series.py`
    - _Requirements: 11.1, 11.2_

- [x] 4. Checkpoint — Collection, series, and curriculums created
  - Ensure the orchestrator completed successfully. Verify the new collection exists, the series is inside it with display_order 100, and all 4 curriculums are in the series with display orders 0-3. Ask the user if questions arise.

- [x] 5. Post-creation verification
  - [x] 5.1 Run SQL verification queries against the database
    - Verify the new "Học Từ Vựng Tiếng Trung Qua Điện Ảnh" collection exists and is public
    - Verify the collection has exactly 1 series
    - Verify the series has exactly 4 curriculums
    - Verify series display order is 100
    - Verify curriculum display orders within the series: 0, 1, 2, 3
    - Verify each curriculum has `youtubeUrl` at top level of content JSON
    - Verify language homogeneity via `curriculum_series_language_list` (all vi-zh)
    - Verify all 4 curriculums are private (`is_public = false`)
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 10.1, 10.2, 10.3, 13.1, 15.1, 16.1_

- [x] 6. Cleanup — Delete scripts and write README
  - [x] 6.1 Delete all curriculum and orchestrator scripts from `vi-zh-movie-vocab-series/`, write `README.md`
    - README includes: collection ID and title, series ID, 4 curriculum IDs and titles (with Chinese movie/scene), YouTube URLs used, how content was created, SQL queries to find the curriculums in the DB, enough context to recreate if needed
    - _Requirements: 11.4, 17.1, 17.2, 17.3_

- [x] 7. Final checkpoint
  - Ensure all 4 curriculums exist in DB, the new collection and series are correctly wired, all source scripts are deleted, and the folder contains only README.md. Ask the user if questions arise.

## Notes

- Each curriculum script is ~500-800 lines with all hand-written Vietnamese/Chinese content — no templates or string interpolation for learner-facing text
- Movie scenes are NOT pre-selected — the implementer selects appropriate Chinese (Mandarin) movie scenes during implementation based on the movie scene selection criteria in Requirements 2.1-2.6 (well-known, clear Mandarin pronunciation, HSK2-HSK3 level dialogue, no excessive profanity, well-known on YouTube, sufficient dialogue length)
- Chinese movie dialogue MUST be sourced via web search during implementation to ensure verbatim accuracy in simplified Chinese characters
- YouTube URLs MUST be found via web search during implementation to ensure validity
- The `validate(content)` function in each script checks structural properties (18 words, 5 sessions, activity order, title/description presence, no strip keys, youtubeUrl format, Chinese vocab in dialogue, dialogue substring checks, writing prompt format with pinyin, farewell word review) before making the API call
- The orchestrator creates BOTH the collection AND the series (same pattern as the vi-en movie series and vi-zh song series)
- Orchestrator takes curriculum IDs as constants (pasted from curriculum script output)
- Follow the exact pattern from `vi-zh-song-vocab-series/` curriculum scripts for script structure, adapted for movie dialogue instead of song lyrics (DIALOGUE_1/2/3/FULL_DIALOGUE instead of LYRICS_1/2/3/FULL_LYRICS)
- All series descriptions must be under 255 characters (PostgreSQL varchar limit)
- Token is refreshed via `get_firebase_id_token(UID)` before each API call
- Content JSON includes `youtubeUrl` at top level alongside `title`, `description`, `preview`, `learningSessions`
- Key difference from vi-en movie series: `language="zh"` instead of `language="en"`, introAudio scripts include pinyin when teaching vocabulary, writing prompts include pinyin in parentheses and Chinese example sentences
- Curriculum titles use Chinese characters for movie names (e.g., "Học Qua Phim: '霸王别姬' – Cảnh đối thoại giữa Điệp Y và Cúc Tiên")
- readAlong description for all curriculums: "Nghe lời thoại phim và theo dõi."
- Session 5 title for all curriculums: "Đọc toàn bộ lời thoại"
