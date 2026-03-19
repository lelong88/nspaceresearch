# Implementation Plan: Vi-Zh Song-Based Vocab Series

## Overview

Create a new collection "Học Từ Vựng Tiếng Trung Qua Âm Nhạc (通过音乐学中文词汇)" and populate it with a single series "Học Từ Vựng Qua Bài Hát Trung Quốc (通过中文歌曲学词汇)" containing 4 curriculums. Each curriculum is built around a different evergreen Chinese (Mandarin) song, using verbatim simplified Chinese lyrics as reading passages. One standalone Python script per curriculum + one orchestrator for collection/series creation. After verification, scripts are deleted and README is written.

## Tasks

- [ ] 1. Chinese Song Curriculum Scripts
  - [ ] 1.1 Create `vi-zh-song-based-vocab-series/create_zh_song_1_<artist>.py` — Chinese Song 1 curriculum
    - Select an appropriate evergreen Chinese song via web search (clear Mandarin pronunciation, HSK 3-4 level lyrics, no rap/heavy dialect, no excessive slang, well-known on YouTube)
    - Find verbatim song lyrics in simplified Chinese via web search and verify accuracy
    - Find the official YouTube URL for the song via web search
    - Define 18 Chinese vocabulary words drawn from the lyrics (W1, W2, W3 — 6 each), prioritizing words that are genuinely in the lyrics, at HSK 3-4 level, broadly useful, and teachable
    - Write lyric portions for sessions 1-3 (LYRICS_1, LYRICS_2, LYRICS_3 — verse/chorus sections containing each session's 6 words) and FULL_LYRICS (complete song in simplified Chinese)
    - Write persuasive Vietnamese description (5-beat structure, Chinese song-adapted), preview (~150 words referencing the song and its themes), and curriculum title in format "Học Qua Bài Hát: '中文歌名' – 歌手名"
    - Write 5 sessions of hand-crafted introAudio scripts in Vietnamese: welcome + song context, vocab teaching (how each Chinese word appears in the lyrics with Vietnamese definitions), grammar/usage notes for sessions 1-3; congratulations + recap for session 4; farewell with all 18 words reviewed for session 5 (400-600 words)
    - Write writingSentence items with targetVocab (Chinese word), Vietnamese context prompts, and "Ví dụ:" with Chinese example sentences
    - Include `youtubeUrl` at top level of content dict
    - Include all activity metadata (title, description) following naming conventions (Flashcards:/Đọc:/Nghe:/Viết:)
    - Include inline `STRIP_KEYS` set and `strip_keys()` function
    - Include inline `validate(content)` function checking Properties 1-12 from design
    - API call: `curriculum/create` with `language="zh"`, `userLanguage="vi"`, `content=json.dumps(content)`
    - Print created curriculum ID
    - _Requirements: 1.5, 2.1-2.5, 3.1-3.5, 4.1-4.7, 5.1-5.3, 6.1-6.6, 7.1-7.2, 8.1-8.7, 9.1, 11.1, 11.3, 12.1-12.2, 13.1, 14.1-14.2, 15.1-15.3, 16.1-16.2_

  - [ ] 1.2 Create `vi-zh-song-based-vocab-series/create_zh_song_2_<artist>.py` — Chinese Song 2 curriculum
    - Select a different evergreen Chinese song via web search (same criteria as 1.1 — clear Mandarin pronunciation, HSK 3-4 level lyrics, no rap/heavy dialect, well-known)
    - Find verbatim song lyrics in simplified Chinese and official YouTube URL via web search
    - Same structure as 1.1 but with 18 vocabulary words drawn from this song's lyrics
    - All text content (description, preview, introAudio scripts, writing prompts) hand-written for this specific song — no templates or reuse from song 1
    - Include inline `strip_keys()`, `validate(content)`, `youtubeUrl`, and API call
    - _Requirements: 1.5, 2.1-2.5, 3.1-3.5, 4.1-4.7, 5.1-5.3, 6.1-6.6, 7.1-7.2, 8.1-8.7, 9.1, 11.1, 11.3, 12.1-12.2, 13.1, 14.1-14.2, 15.1-15.3, 16.1-16.2_

  - [ ] 1.3 Create `vi-zh-song-based-vocab-series/create_zh_song_3_<artist>.py` — Chinese Song 3 curriculum
    - Select a different evergreen Chinese song via web search (same criteria — clear Mandarin pronunciation, HSK 3-4 level lyrics, no rap/heavy dialect, well-known)
    - Find verbatim song lyrics in simplified Chinese and official YouTube URL via web search
    - Same structure as 1.1 but with 18 vocabulary words drawn from this song's lyrics
    - All text content hand-written for this specific song
    - Include inline `strip_keys()`, `validate(content)`, `youtubeUrl`, and API call
    - _Requirements: 1.5, 2.1-2.5, 3.1-3.5, 4.1-4.7, 5.1-5.3, 6.1-6.6, 7.1-7.2, 8.1-8.7, 9.1, 11.1, 11.3, 12.1-12.2, 13.1, 14.1-14.2, 15.1-15.3, 16.1-16.2_

  - [ ] 1.4 Create `vi-zh-song-based-vocab-series/create_zh_song_4_<artist>.py` — Chinese Song 4 curriculum
    - Select a different evergreen Chinese song via web search (same criteria — clear Mandarin pronunciation, HSK 3-4 level lyrics, no rap/heavy dialect, well-known)
    - Find verbatim song lyrics in simplified Chinese and official YouTube URL via web search
    - Same structure as 1.1 but with 18 vocabulary words drawn from this song's lyrics
    - All text content hand-written for this specific song
    - Include inline `strip_keys()`, `validate(content)`, `youtubeUrl`, and API call
    - _Requirements: 1.5, 2.1-2.5, 3.1-3.5, 4.1-4.7, 5.1-5.3, 6.1-6.6, 7.1-7.2, 8.1-8.7, 9.1, 11.1, 11.3, 12.1-12.2, 13.1, 14.1-14.2, 15.1-15.3, 16.1-16.2_

- [ ] 2. Checkpoint — All 4 curriculum scripts created
  - Ensure all 4 curriculum scripts pass `validate(content)` locally. Verify each script selects a different Chinese song, has 18 unique Chinese vocab words from the lyrics, correct session/activity structure, youtubeUrl present, and no strip keys. Ask the user if questions arise.

- [ ] 3. Orchestrator & Execution
  - [ ] 3.1 Create `vi-zh-song-based-vocab-series/create_zh_song_series.py` — Collection + Series orchestrator
    - Create collection via `curriculum-collection/create` with title "Học Từ Vựng Tiếng Trung Qua Âm Nhạc (通过音乐学中文词汇)", persuasive Vietnamese description, `isPublic: true`
    - Create series via `curriculum-series/create` with title "Học Từ Vựng Qua Bài Hát Trung Quốc (通过中文歌曲学词汇)", Vietnamese description (≤255 chars), `isPublic: true`
    - Add series to collection via `curriculum-collection/addSeriesToCollection`
    - Set series display order 100 via `curriculum-series/setDisplayOrder`
    - Add all 4 curriculum IDs to series via `curriculum-series/addCurriculum`
    - Set curriculum display orders (0, 1, 2, 3) via `curriculum/setDisplayOrder`
    - Token refreshed before each API call
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 10.1, 10.2, 10.3, 11.2, 13.3_

  - [ ] 3.2 Run all 4 curriculum scripts and the orchestrator, verify output
    - Run `python create_zh_song_1_<artist>.py`, `create_zh_song_2_<artist>.py`, `create_zh_song_3_<artist>.py`, `create_zh_song_4_<artist>.py`
    - Paste curriculum IDs into orchestrator, run `python create_zh_song_series.py`
    - _Requirements: 11.1, 11.2_

- [ ] 4. Checkpoint — Collection, series, and curriculums created
  - Ensure the orchestrator completed successfully. Verify the new collection exists, the series is inside it with display_order 100, and all 4 curriculums are in the series with display orders 0-3. Ask the user if questions arise.

- [ ] 5. Post-creation verification
  - [ ] 5.1 Run SQL verification queries against the database
    - Verify the new "Học Từ Vựng Tiếng Trung Qua Âm Nhạc" collection exists and is public
    - Verify the collection has exactly 1 series
    - Verify the series has exactly 4 curriculums
    - Verify series display order is 100
    - Verify curriculum display orders within the series: 0, 1, 2, 3
    - Verify each curriculum has `youtubeUrl` at top level of content JSON
    - Verify language homogeneity via `curriculum_series_language_list` (all zh/vi)
    - Verify all 4 curriculums are private (`is_public = false`)
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 10.1, 10.2, 10.3, 13.1, 15.1, 16.1_

- [ ] 6. Cleanup — Delete scripts and write README
  - [ ] 6.1 Delete all curriculum and orchestrator scripts from `vi-zh-song-based-vocab-series/`, write `README.md`
    - README includes: collection ID and title, series ID, 4 curriculum IDs and titles (with Chinese song/artist), YouTube URLs used, how content was created, SQL queries to find the curriculums in the DB, enough context to recreate if needed
    - _Requirements: 11.4, 17.1, 17.2, 17.3_

- [ ] 7. Final checkpoint
  - Ensure all 4 curriculums exist in DB, the new collection and series are correctly wired, all source scripts are deleted, and the folder contains only README.md. Ask the user if questions arise.

## Notes

- Each curriculum script is ~500-800 lines with all hand-written Vietnamese/Chinese content — no templates or string interpolation for learner-facing text
- Songs are NOT pre-selected — the implementer selects appropriate Chinese songs during implementation based on the song selection criteria in Requirements 2.1-2.5 (evergreen, clear Mandarin pronunciation, HSK 3-4 level lyrics, no rap/heavy dialect, no excessive slang)
- Good candidate songs include classic Mandopop ballads from artists like 邓丽君 (Teresa Teng), 周杰伦 (Jay Chou — slower ballads only), 王菲 (Faye Wong), 刘德华 (Andy Lau), 张学友 (Jacky Cheung), 李宗盛 (Jonathan Lee), etc.
- Song lyrics MUST be sourced via web search during implementation to ensure verbatim accuracy in simplified Chinese
- YouTube URLs MUST be found via web search during implementation to ensure validity
- The `validate(content)` function in each script checks structural properties (18 words, 5 sessions, activity order, title/description presence, no strip keys, youtubeUrl format, vocab in lyrics, lyrics substring checks, writing prompt format, farewell word review) before making the API call
- The orchestrator creates BOTH the collection AND the series (same pattern as vi-en song series)
- Orchestrator takes curriculum IDs as constants (pasted from curriculum script output)
- Follow the exact pattern from `song-based-vocab-series/create_song_1_michael_jackson.py` for script structure, adapted for zh/vi language pair
- All series descriptions must be under 255 characters (PostgreSQL varchar limit)
- Token is refreshed via `get_firebase_id_token(UID)` before each API call
- Content JSON includes `youtubeUrl` at top level alongside `title`, `description`, `preview`, `learningSessions`
- API calls use `language="zh"` and `userLanguage="vi"` (NOT `language="en"`)
- Vietnamese is used for all user-facing instructional text; simplified Chinese is used for reading passages (lyrics) and vocabulary words
