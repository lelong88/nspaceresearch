# Implementation Plan: En-Zh Curriculum Mirror

## Overview

Create 61 en-zh mirror curriculums from existing vi-zh curriculums across 7 series and 5 collections. Work is organized by content type: each content type gets a `strip_keys()` utility, per-curriculum creation scripts with hand-written English text, and an orchestrator script for collection/series wiring. The strip_keys property test comes first since it validates the core utility used by all scripts.

## Tasks

- [x] 1. Create workspace structure and shared strip_keys utility
  - [x] 1.1 Create directory structure for en-zh-curriculum-mirror
    - Create `en-zh-curriculum-mirror/` with subfolders: `songs/`, `movies/`, `novels/memories-of-flavor/`, `novels/the-vanishing-painting/`, `novels/the-sound-of-music-by-the-lake/`, `textbook/`, `wisdom/`, `travel/`
    - Create a shared `en-zh-curriculum-mirror/strip_keys_helper.py` with the `strip_keys()` function and `STRIP_KEYS` constant, importable by all creation scripts
    - _Requirements: 16.1, 16.2, 15.5_

  - [ ]* 1.2 Write property test for strip_keys (Property 1)
    - **Property 1: strip_keys removes all target keys at all nesting levels**
    - **Validates: Requirements 4.2, 4.3, 11.1, 20.3**
    - Create `en-zh-curriculum-mirror/test_strip_keys.py` using `hypothesis`
    - Generate nested dict/list structures with random keys including subsets of the 10 STRIP_KEYS
    - Assert: after `strip_keys()`, no target keys exist at any nesting depth, and all other keys/values are preserved
    - Minimum 100 iterations (`@settings(max_examples=100)`)

- [x] 2. Implement song-based curriculums (4 curriculums)
  - [x] 2.1 Create songs orchestrator script
    - Create `en-zh-curriculum-mirror/songs/create_en_zh_song_series.py`
    - Creates en-zh collection "Learn Chinese Vocabulary Through Music (通过音乐学中文词汇)" via `curriculum-collection/create`
    - Creates en-zh series "Learn Chinese Vocabulary Through Songs (通过歌曲学中文词汇)" via `curriculum-series/create`
    - Wires series to collection via `curriculum-collection/addSeriesToCollection`
    - After all 4 curriculums are created, adds them to the series and sets display orders matching vi-zh source (0, 1, 2, 3)
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 2.1, 2.6, 3.1, 3.9, 10.1, 10.2_

  - [x] 2.2 Create song curriculum scripts (4 scripts)
    - Create `en-zh-curriculum-mirror/songs/create_song_1_moon.py` — mirrors `Mi4dqOv4sAOb2axi` (月亮代表我的心 – 邓丽君)
    - Create `en-zh-curriculum-mirror/songs/create_song_2_friends.py` — mirrors `4ryQKO4ffbmWJNH4` (朋友 – 周华健)
    - Create `en-zh-curriculum-mirror/songs/create_song_3_sweet_honey.py` — mirrors `5fthZeygE85aSBDS` (甜蜜蜜 – 邓丽君)
    - Create `en-zh-curriculum-mirror/songs/create_song_4_fairytale.py` — mirrors `b4pH6tU7szEqye74` (童话 – 光良)
    - Each script: fetches source via `curriculum/getOne`, strips keys, replaces all Vietnamese text with hand-written English, calls `curriculum/create` with `language="zh"`, `userLanguage="en"`, verifies the created curriculum
    - Title pattern: "Learn Through Song: '[Chinese title]' – [Artist]"
    - Hand-written English: title, description (persuasive copy), preview (~150 words), introAudio scripts, writing prompts, activity titles/descriptions, session titles, vocabulary definitions
    - _Requirements: 4.1, 4.2, 4.3, 5.1–5.11, 6.1–6.9, 7.1, 8.1–8.6, 9.1–9.4, 12.1, 12.2, 13.1–13.3, 15.1, 15.4, 17.1–17.3, 18.1–18.7, 19.1, 20.1–20.3_

- [x] 3. Implement movie-based curriculums (4 curriculums)
  - [x] 3.1 Create movies orchestrator script
    - Create `en-zh-curriculum-mirror/movies/create_en_zh_movie_series.py`
    - Creates en-zh collection "Learn Chinese Vocabulary Through Cinema (通过电影学中文词汇)" via `curriculum-collection/create`
    - Creates en-zh series "Learn Chinese Vocabulary Through Film (通过电影学中文词汇)" via `curriculum-series/create`
    - Wires series to collection, adds curriculums, sets display orders (0, 1, 2, 3)
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 2.2, 2.6, 3.2, 3.9, 10.1, 10.2_

  - [x] 3.2 Create movie curriculum scripts (4 scripts)
    - Create `en-zh-curriculum-mirror/movies/create_movie_1_kung_fu.py` — mirrors `3j80e3IpKczh26B0` (功夫)
    - Create `en-zh-curriculum-mirror/movies/create_movie_2_shaolin_soccer.py` — mirrors `PUABCeIlJ2uEg5rE` (少林足球)
    - Create `en-zh-curriculum-mirror/movies/create_movie_3_chinese_odyssey.py` — mirrors `EjvrQRIPPUPQW5Gt` (大话西游)
    - Create `en-zh-curriculum-mirror/movies/create_movie_4_bullets_fly.py` — mirrors `uEciL1GTo1OFZbbm` (让子弹飞)
    - Each script: fetch → strip keys → replace Vietnamese with hand-written English → create → verify
    - Title pattern: "Learn Through Film: '[Chinese title]' – [English scene description]"
    - _Requirements: 4.1–4.3, 5.1–5.11, 6.1–6.9, 7.2, 8.1–8.6, 9.1–9.4, 12.1, 12.2, 13.1–13.3, 15.1, 15.4, 17.1–17.3, 18.1–18.7, 19.2, 20.1–20.3_

- [x] 4. Checkpoint — Songs and Movies
  - Ensure all 8 song + movie curriculums are created and verified. Ensure orchestrator scripts wired them into the correct series/collections with correct display orders. Ask the user if questions arise.

- [x] 5. Implement novel: 味道的记忆 — Memories of Flavor (10 chapters)
  - [x] 5.1 Create Memories of Flavor orchestrator script
    - Create `en-zh-curriculum-mirror/novels/memories-of-flavor/create_en_zh_memories_series.py`
    - Creates en-zh collection "Fiction (小说)" via `curriculum-collection/create` (shared across all 3 novels — create once, reuse for the other two)
    - Creates en-zh series "Memories of Flavor (味道的记忆)" via `curriculum-series/create`
    - Wires series to Fiction collection, adds all 10 chapter curriculums, sets display orders 1–10
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 2.3, 2.6, 3.3, 3.9, 10.1, 10.2_

  - [x] 5.2 Create Memories of Flavor chapter scripts (10 scripts)
    - Create `en-zh-curriculum-mirror/novels/memories-of-flavor/create_chapter_N.py` for N=1..10
    - Source series ID: `uq7ezeuh` — fetch each chapter's curriculum ID from the series
    - Each script: fetch → strip keys → replace Vietnamese with hand-written English → create → verify
    - Title pattern: "Memories of Flavor (味道的记忆) — Chapter N: [English Chapter Title] ([Chinese Chapter Title])"
    - Hand-written English: description with narrative hooks/cliffhangers, preview, introAudio scripts, writing prompts, activity titles/descriptions, session titles, vocabulary definitions
    - _Requirements: 4.1–4.3, 5.1–5.11, 6.1–6.9, 7.3, 8.1–8.6, 9.1–9.4, 12.1, 12.2, 13.1–13.3, 15.2, 15.4, 17.1–17.3, 18.1–18.7, 19.3, 20.1–20.3_

- [x] 6. Implement novel: 消失的画 — The Vanishing Painting (10 chapters)
  - [x] 6.1 Create The Vanishing Painting orchestrator script
    - Create `en-zh-curriculum-mirror/novels/the-vanishing-painting/create_en_zh_vanishing_series.py`
    - Creates en-zh series "The Vanishing Painting (消失的画)" via `curriculum-series/create`
    - Wires series to the existing en-zh Fiction collection (created in task 5.1), adds all 10 chapter curriculums, sets display orders 1–10
    - _Requirements: 1.2, 1.3, 1.4, 3.4, 3.9, 10.1, 10.2_

  - [x] 6.2 Create The Vanishing Painting chapter scripts (10 scripts)
    - Create `en-zh-curriculum-mirror/novels/the-vanishing-painting/create_chapter_N.py` for N=1..10
    - Source series ID: `wlzqfag8`
    - Each script: fetch → strip keys → replace Vietnamese with hand-written English → create → verify
    - Title pattern: "The Vanishing Painting (消失的画) — Chapter N: [English Chapter Title] ([Chinese Chapter Title])"
    - _Requirements: 4.1–4.3, 5.1–5.11, 6.1–6.9, 7.3, 8.1–8.6, 9.1–9.4, 12.1, 12.2, 13.1–13.3, 15.2, 15.4, 17.1–17.3, 18.1–18.7, 19.3, 20.1–20.3_

- [x] 7. Implement novel: 湖边的琴声 — The Sound of Music by the Lake (10 chapters)
  - [x] 7.1 Create The Sound of Music by the Lake orchestrator script
    - Create `en-zh-curriculum-mirror/novels/the-sound-of-music-by-the-lake/create_en_zh_lake_series.py`
    - Creates en-zh series "The Sound of Music by the Lake (湖边的琴声)" via `curriculum-series/create`
    - Wires series to the existing en-zh Fiction collection, adds all 10 chapter curriculums, sets display orders 1–10
    - _Requirements: 1.2, 1.3, 1.4, 3.5, 3.9, 10.1, 10.2_

  - [x] 7.2 Create The Sound of Music by the Lake chapter scripts (10 scripts)
    - Create `en-zh-curriculum-mirror/novels/the-sound-of-music-by-the-lake/create_chapter_N.py` for N=1..10
    - Source series ID: `z6xddztr`
    - Each script: fetch → strip keys → replace Vietnamese with hand-written English → create → verify
    - Title pattern: "The Sound of Music by the Lake (湖边的琴声) — Chapter N: [English Chapter Title] ([Chinese Chapter Title])"
    - _Requirements: 4.1–4.3, 5.1–5.11, 6.1–6.9, 7.3, 8.1–8.6, 9.1–9.4, 12.1, 12.2, 13.1–13.3, 15.2, 15.4, 17.1–17.3, 18.1–18.7, 19.3, 20.1–20.3_

- [x] 8. Checkpoint — All 3 Novels
  - Ensure all 30 novel chapter curriculums are created and verified across 3 series in the Fiction collection. Ensure display orders 1–10 per series. Ask the user if questions arise.

- [x] 9. Implement textbook curriculums — Standard Chinese Elementary 2 (25 curriculums)
  - [x] 9.1 Create textbook orchestrator script
    - Create `en-zh-curriculum-mirror/textbook/create_en_zh_textbook_series.py`
    - Creates en-zh collection "Elementary 2 (初级二)" via `curriculum-collection/create`
    - Creates en-zh series "Standard Chinese — Elementary 2" via `curriculum-series/create`
    - Wires series to collection, adds all 25 curriculums, sets display orders 1–25
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 2.4, 2.6, 3.6, 3.9, 10.1, 10.2_

  - [x] 9.2 Create textbook curriculum scripts — Lessons 1–5
    - Create `en-zh-curriculum-mirror/textbook/create_lesson_N.py` for N=1..5
    - Source series ID: `dqce6wbh` — fetch each lesson's curriculum ID from the series
    - Each script: fetch → strip keys → replace Vietnamese with hand-written English → create → verify
    - Hand-written English: title, description (pedagogical framing for English speakers), preview, introAudio scripts, writing prompts, activity titles/descriptions, session titles, vocabulary definitions
    - _Requirements: 4.1–4.3, 5.1–5.11, 6.1–6.9, 7.4, 8.1–8.6, 9.1–9.4, 12.1, 12.2, 13.1–13.3, 15.2, 15.4, 17.1–17.3, 18.1–18.7, 19.4, 20.1–20.3_

  - [x] 9.3 Create textbook curriculum scripts — Lessons 6–10
    - Create `en-zh-curriculum-mirror/textbook/create_lesson_N.py` for N=6..10
    - Same pattern as 9.2
    - _Requirements: same as 9.2_

  - [x] 9.4 Create textbook curriculum scripts — Lessons 11–15
    - Create `en-zh-curriculum-mirror/textbook/create_lesson_N.py` for N=11..15
    - Same pattern as 9.2
    - _Requirements: same as 9.2_

  - [x] 9.5 Create textbook curriculum scripts — Lessons 16–20
    - Create `en-zh-curriculum-mirror/textbook/create_lesson_N.py` for N=16..20
    - Same pattern as 9.2
    - _Requirements: same as 9.2_

  - [x] 9.6 Create textbook curriculum scripts — Lessons 21–25
    - Create `en-zh-curriculum-mirror/textbook/create_lesson_N.py` for N=21..25
    - Same pattern as 9.2
    - _Requirements: same as 9.2_

- [x] 10. Checkpoint — Textbook
  - Ensure all 25 textbook curriculums are created and verified in the Standard Chinese — Elementary 2 series. Ensure display orders 1–25. Ask the user if questions arise.

- [x] 11. Implement wisdom curriculums (4 curriculums)
  - [x] 11.1 Create wisdom orchestrator script
    - Create `en-zh-curriculum-mirror/wisdom/create_en_zh_wisdom_series.py`
    - The wisdom series belongs to the same en-zh "Elementary 2 (初级二)" collection created in task 9.1 — reuse that collection ID
    - Creates en-zh series "Wisdom in Chinese Characters (汉字中的智慧)" via `curriculum-series/create`
    - Wires series to the Elementary 2 collection, adds all 4 curriculums, sets display orders (0, 1, 2, 3)
    - _Requirements: 1.2, 1.3, 1.4, 3.7, 3.9, 10.1, 10.2_

  - [x] 11.2 Create wisdom curriculum scripts (4 scripts)
    - Create `en-zh-curriculum-mirror/wisdom/create_wisdom_1_heart.py` — mirrors `QOvwYvTVMi6OkkWp` (心字篇)
    - Create `en-zh-curriculum-mirror/wisdom/create_wisdom_2_human.py` — mirrors `cPjQO2MkPgWdMvlv` (人字篇)
    - Create `en-zh-curriculum-mirror/wisdom/create_wisdom_3_home.py` — mirrors `tepW8yNMEOWiKnkC` (家字篇)
    - Create `en-zh-curriculum-mirror/wisdom/create_wisdom_4_action.py` — mirrors `DSsoTpLVsaE4ktmJ` (力字篇)
    - Each script: fetch → strip keys → replace Vietnamese with hand-written English → create → verify
    - Title pattern: "[English Theme] — Characters of [Concept] ([Chinese]篇)"
    - _Requirements: 4.1–4.3, 5.1–5.11, 6.1–6.9, 7.5, 8.1–8.6, 9.1–9.4, 12.1, 12.2, 13.1–13.3, 15.1, 15.4, 17.1–17.3, 18.1–18.7, 19.5, 20.1–20.3_

- [x] 12. Implement travel curriculums (4 curriculums)
  - [x] 12.1 Create travel orchestrator script
    - Create `en-zh-curriculum-mirror/travel/create_en_zh_travel_series.py`
    - Creates en-zh collection "Thematic Vocabulary (主题词汇)" via `curriculum-collection/create`
    - Creates en-zh series "Explore China (探索中国)" via `curriculum-series/create`
    - Wires series to collection, adds all 4 curriculums, sets display orders matching vi-zh source
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 2.5, 2.6, 3.8, 3.9, 10.1, 10.2_

  - [x] 12.2 Create travel curriculum scripts (4 scripts)
    - Create 4 scripts in `en-zh-curriculum-mirror/travel/`, one per travel curriculum
    - Source series ID: `yjwuyhtk` — fetch each curriculum ID from the series
    - Each script: fetch → strip keys → replace Vietnamese with hand-written English → create → verify
    - Title pattern: "[Chinese City] — [English tagline] ([Chinese tagline])"
    - _Requirements: 4.1–4.3, 5.1–5.11, 6.1–6.9, 7.6, 8.1–8.6, 9.1–9.4, 12.1, 12.2, 13.1–13.3, 15.1, 15.4, 17.1–17.3, 18.1–18.7, 19.6, 20.1–20.3_

- [x] 13. Checkpoint — Wisdom and Travel
  - Ensure all 8 wisdom + travel curriculums are created and verified. Ensure orchestrator scripts wired them into the correct series/collections with correct display orders. Ask the user if questions arise.

- [x] 14. Create verification script and run final checks
  - [x] 14.1 Create verify_all.py integration verification script
    - Create `en-zh-curriculum-mirror/verify_all.py`
    - Fetches all 61 en-zh curriculums and their 61 vi-zh source counterparts
    - For each pair, verifies:
      - Property 2: Chinese content identical (reading text, vocab words, pinyin, youtubeUrl, audioSpeed)
      - Property 3: Structural preservation (session count, activity count, activity type sequence)
      - Property 4: Language params correct (`language=zh`, `userLanguage=en`)
      - Property 10: `is_public` is false
      - Property 11: User-facing text differs between mirror and source
      - Property 12: Vocabulary definitions handled correctly
      - Property 13: Activity metadata follows English patterns
    - Queries series/collection metadata to verify:
      - Property 5: Display orders match vi-zh source
      - Property 6: No cross-contamination (en-zh content only in en-zh containers)
      - Property 7: Series descriptions under 255 chars
      - Property 8: Title patterns correct per content type
      - Property 9: Curriculum count parity (61 en-zh = 61 vi-zh)
    - Prints pass/fail summary per property
    - _Requirements: 1.5, 5.1–5.11, 10.1–10.3, 14.1–14.4, 20.1–20.3_

  - [ ]* 14.2 Write property tests for verification properties
    - **Property 2: Chinese content preservation**
    - **Property 3: Structural preservation**
    - **Property 4: Language parameters correct**
    - **Property 5: Display order preservation**
    - **Property 6: No cross-contamination**
    - **Property 9: Curriculum count parity**
    - **Property 10: Private by default**
    - **Validates: Requirements 5.1–5.11, 10.1–10.3, 14.1–14.4, 12.1–12.2**
    - These are integration-level checks in verify_all.py, not standalone property-based tests (they require live DB state)

- [x] 15. Clean up workspace and create READMEs
  - [x] 15.1 Create README files for each content type subfolder
    - After all curriculums for a content type are verified, create a README.md in each subfolder documenting:
      - En-zh collection ID and title
      - En-zh series ID and title
      - Mirror curriculum IDs and titles with corresponding source curriculum IDs
      - How content was created (fetch → strip → transform → upload pattern)
      - SQL queries to find the curriculums in the DB
      - Enough context to recreate if needed
    - _Requirements: 16.3_

  - [x] 15.2 Delete creation scripts after verification
    - After verify_all.py confirms all 61 curriculums pass all checks, delete all Python creation scripts and orchestrator scripts from each subfolder, leaving only READMEs
    - _Requirements: 15.6, 16.4_

- [x] 16. Final checkpoint — Full verification
  - Run verify_all.py to confirm all 61 en-zh curriculums across 7 series and 5 collections pass all correctness properties. Ensure all creation scripts are deleted and only READMEs remain. Ensure all tests pass, ask the user if questions arise.

## Notes

- Tasks marked with `*` are optional and can be skipped for faster MVP
- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation after each content type batch
- The strip_keys property test (task 1.2) validates the core utility used by all 61 creation scripts
- The Fiction collection (task 5.1) and Elementary 2 collection (task 9.1) are each shared by multiple series — create once, reuse
- Textbook lessons are grouped in batches of 5 to keep tasks manageable (25 total)
- All scripts use Python with `requests`, `firebase_token`, and `json` — no build system or test framework beyond `hypothesis` for the strip_keys test
