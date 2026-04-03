# Implementation Plan: Media Content Parity

## Overview

Fill 6 content gaps across the language pair × content type matrix so every combination of 4 language pairs (vi-en, vi-zh, en-zh, en-en) × 3 content types (movie, music, podcast) has exactly 4 curriculums organized directly under a collection (no series). Work items use three patterns: organization-only (item 1), new content creation (items 2–3), and mirror from vi-en source (items 4–6). All scripts are deleted after verification, leaving only READMEs.

## Tasks

- [x] 1. en-zh music collection organization (orchestrator only)
  - [x] 1.1 Write `en-zh-music-series/create_en_zh_music_collection.py` orchestrator script
    - Create a new Collection titled "Learn Chinese Vocabulary Through Music (通过音乐学中文词汇)"
    - Add 4 existing curriculum IDs (HLLOA8bahIraa6rR, MX6Yw2Qrkiry1ylN, CbYWQ16GXWxNiol4, 9jRr2DrofNwyQZ1Z) directly to the collection via `curriculum-collection/addCurriculum`
    - Call `curriculum/setDisplayOrder` to assign display orders 0, 1, 2, 3
    - _Requirements: 1.1, 1.2, 1.4, 1.5_

  - [x] 1.2 Run orchestrator and verify collection organization
    - Execute `python create_en_zh_music_collection.py`
    - Confirm collection created with correct title
    - Confirm all 4 curriculums appear in collection with correct display orders
    - _Requirements: 1.4, 1.5_

- [x] 2. Checkpoint — en-zh music organization verified
  - Ensure collection is correctly set up, ask the user if questions arise.

- [x] 3. vi-zh podcast curriculums (new Chinese-language content)
  - [x] 3.1 Select 4 Chinese-language talks for vi-zh and en-zh podcasts
    - Choose 4 Chinese-language talks/podcasts with clear Mandarin speech, YouTube availability, and HSK2-HSK3 vocabulary suitability
    - These same 4 talks will be reused for en-zh podcasts (item 5)
    - Document YouTube URLs and talk titles
    - _Requirements: 7.1, 7.2, 7.3, 7.4_

  - [x] 3.2 Write `vi-zh-podcast-vocab-series/create_podcast_0.py` — first vi-zh podcast curriculum
    - Hand-write complete curriculum content with 18 HSK2-HSK3 vocabulary words (3 groups of 6) from the first Chinese-language talk
    - 5 sessions: 3 learning (12 activities each), 1 review (4 activities), 1 full reading + farewell (5 activities)
    - All user-facing text in Vietnamese (titles, descriptions, previews, introAudio, writing prompts, activity titles, session titles, vocabulary definitions)
    - Include inline `strip_keys()` and `validate()` functions
    - Set `language="zh"`, `userLanguage="vi"`, `contentTypeTags=["podcast"]`
    - Include `youtubeUrl` at top level, `title`/`description` on every activity
    - Set `is_public = false`
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 9.1, 9.2, 9.3, 9.4, 9.5_

  - [x] 3.3 Write `vi-zh-podcast-vocab-series/create_podcast_1.py` — second vi-zh podcast curriculum
    - Same structure and rules as 3.2, different Chinese-language talk and hand-written content
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 9.1, 9.2, 9.3, 9.4, 9.5_

  - [x] 3.4 Write `vi-zh-podcast-vocab-series/create_podcast_2.py` — third vi-zh podcast curriculum
    - Same structure and rules as 3.2, different Chinese-language talk and hand-written content
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 9.1, 9.2, 9.3, 9.4, 9.5_

  - [x] 3.5 Write `vi-zh-podcast-vocab-series/create_podcast_3.py` — fourth vi-zh podcast curriculum
    - Same structure and rules as 3.2, different Chinese-language talk and hand-written content
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 9.1, 9.2, 9.3, 9.4, 9.5_

  - [x] 3.6 Write `vi-zh-podcast-vocab-series/create_vi_zh_podcast_collection.py` orchestrator
    - Create Collection "Học Từ Vựng Tiếng Trung Qua Podcast (通过播客学中文词汇)"
    - Add all 4 curriculums directly to the collection via `curriculum-collection/addCurriculum`, set display orders 0–3
    - _Requirements: 2.8_

  - [x] 3.7 Run all 4 creation scripts and orchestrator, verify in database
    - Execute each `create_podcast_N.py` script, collect curriculum IDs
    - Execute orchestrator to wire collection
    - Check for duplicates by title + language + uid
    - _Requirements: 2.8, 2.9_

- [x] 4. Checkpoint — vi-zh podcasts verified
  - Ensure all 4 vi-zh podcast curriculums exist with correct structure, collection wired, ask the user if questions arise.

- [x] 5. en-zh podcast curriculums (English UI, same Chinese talks)
  - [x] 5.1 Write `en-zh-podcast-vocab-series/create_podcast_0.py` — first en-zh podcast curriculum
    - Use the same Chinese-language talk as vi-zh podcast #0 (same youtubeUrl, same 18 vocabulary words)
    - All user-facing text in English with pinyin in introAudio vocabulary teaching and writing prompts
    - Set `language="zh"`, `userLanguage="en"`, `contentTypeTags=["podcast"]`
    - Include inline `strip_keys()` and `validate()` functions
    - Include `youtubeUrl` at top level, `title`/`description` on every activity
    - 5 sessions: 3 learning (12 activities each), 1 review (4 activities), 1 full reading + farewell (5 activities)
    - Set `is_public = false`
    - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6_

  - [x] 5.2 Write `en-zh-podcast-vocab-series/create_podcast_1.py` — second en-zh podcast curriculum
    - Same structure and rules as 5.1, corresponding to vi-zh podcast #1
    - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6_

  - [x] 5.3 Write `en-zh-podcast-vocab-series/create_podcast_2.py` — third en-zh podcast curriculum
    - Same structure and rules as 5.1, corresponding to vi-zh podcast #2
    - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6_

  - [x] 5.4 Write `en-zh-podcast-vocab-series/create_podcast_3.py` — fourth en-zh podcast curriculum
    - Same structure and rules as 5.1, corresponding to vi-zh podcast #3
    - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6_

  - [x] 5.5 Write `en-zh-podcast-vocab-series/create_en_zh_podcast_collection.py` orchestrator
    - Create Collection "Learn Chinese Vocabulary Through Podcasts (通过播客学中文词汇)"
    - Add all 4 curriculums directly to the collection via `curriculum-collection/addCurriculum`, set display orders 0–3
    - _Requirements: 3.9_

  - [x] 5.6 Run all 4 creation scripts and orchestrator, verify in database
    - Execute each `create_podcast_N.py` script, collect curriculum IDs
    - Execute orchestrator to wire collection
    - Verify each en-zh podcast has the same `youtubeUrl` as its vi-zh counterpart (Property 10)
    - Check for duplicates by title + language + uid
    - _Requirements: 3.9, 3.10_

- [x] 6. Checkpoint — en-zh podcasts verified
  - Ensure all 4 en-zh podcast curriculums exist, youtubeUrls match vi-zh counterparts, collection wired, ask the user if questions arise.

- [x] 7. en-en movie curriculums (mirror from vi-en)
  - [x] 7.1 Write `en-en-movie-vocab-series/create_movie_0_forrest_gump.py` — mirror Forrest Gump
    - Fetch vi-en source `5MsWSZwcWGYpfnrO` via `curriculum/getOne`
    - `strip_keys()` to remove auto-generated keys
    - Transform all Vietnamese user-facing text → hand-written English (titles, descriptions, previews, introAudio, writing prompts, activity titles/descriptions, session titles, vocabulary definitions)
    - Set `language="en"`, `userLanguage="en"`, `contentTypeTags=["movie"]`
    - Include inline `strip_keys()` and `validate()` functions
    - Set `is_public = false`
    - _Requirements: 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 9.1, 9.2, 9.3, 9.4, 9.5_

  - [x] 7.2 Write `en-en-movie-vocab-series/create_movie_1_shawshank.py` — mirror Shawshank Redemption
    - Fetch vi-en source `yCj2EZKIPTkFNqtS`, strip keys, transform Vietnamese → English
    - Same mirror pattern as 7.1
    - _Requirements: 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 9.1, 9.2, 9.3, 9.4, 9.5_

  - [x] 7.3 Write `en-en-movie-vocab-series/create_movie_2_dead_poets.py` — mirror Dead Poets Society
    - Fetch vi-en source `LLy5qjuLk0VZ7SIi`, strip keys, transform Vietnamese → English
    - Same mirror pattern as 7.1
    - _Requirements: 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 9.1, 9.2, 9.3, 9.4, 9.5_

  - [x] 7.4 Write `en-en-movie-vocab-series/create_movie_3_pursuit.py` — mirror Pursuit of Happyness
    - Fetch vi-en source `XjJRTMHxnBXFiA31`, strip keys, transform Vietnamese → English
    - Same mirror pattern as 7.1
    - _Requirements: 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 9.1, 9.2, 9.3, 9.4, 9.5_

  - [x] 7.5 Write `en-en-movie-vocab-series/create_en_en_movie_collection.py` orchestrator
    - Create Collection "Learn Vocabulary Through Cinema"
    - Add all 4 curriculums directly to the collection via `curriculum-collection/addCurriculum`, set display orders 0–3
    - _Requirements: 4.7_

  - [x] 7.6 Run all 4 mirror scripts and orchestrator, verify in database
    - Execute each `create_movie_N_*.py` script, collect curriculum IDs
    - Execute orchestrator to wire collection
    - Check for duplicates by title + language + uid
    - _Requirements: 4.7, 4.8_

- [ ] 8. en-en song curriculums (mirror from vi-en)
  - [ ] 8.1 Write `en-en-song-vocab-series/create_song_0_heal_the_world.py` — mirror Heal the World
    - Fetch vi-en source `qVv18hr5L4sTQs6i` via `curriculum/getOne`
    - `strip_keys()` to remove auto-generated keys
    - Transform all Vietnamese user-facing text → hand-written English
    - Set `language="en"`, `userLanguage="en"`, `contentTypeTags=["music"]`
    - Include inline `strip_keys()` and `validate()` functions
    - Set `is_public = false`
    - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 9.1, 9.2, 9.3, 9.4, 9.5_

  - [ ] 8.2 Write `en-en-song-vocab-series/create_song_1_imagine.py` — mirror Imagine
    - Fetch vi-en source `jHM7Pekp6LtLjqok`, strip keys, transform Vietnamese → English
    - Same mirror pattern as 8.1
    - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 9.1, 9.2, 9.3, 9.4, 9.5_

  - [ ] 8.3 Write `en-en-song-vocab-series/create_song_2_lean_on_me.py` — mirror Lean on Me
    - Fetch vi-en source `4Ho0bZURRPz2TiJA`, strip keys, transform Vietnamese → English
    - Same mirror pattern as 8.1
    - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 9.1, 9.2, 9.3, 9.4, 9.5_

  - [ ] 8.4 Write `en-en-song-vocab-series/create_song_3_wonderful_world.py` — mirror What a Wonderful World
    - Fetch vi-en source `5WdGkIlyRDO4dzsL`, strip keys, transform Vietnamese → English
    - Same mirror pattern as 8.1
    - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 9.1, 9.2, 9.3, 9.4, 9.5_

  - [ ] 8.5 Write `en-en-song-vocab-series/create_en_en_song_collection.py` orchestrator
    - Create Collection "Learn Vocabulary Through Music"
    - Add all 4 curriculums directly to the collection via `curriculum-collection/addCurriculum`, set display orders 0–3
    - _Requirements: 5.7_

  - [ ] 8.6 Run all 4 mirror scripts and orchestrator, verify in database
    - Execute each `create_song_N_*.py` script, collect curriculum IDs
    - Execute orchestrator to wire collection
    - Check for duplicates by title + language + uid
    - _Requirements: 5.7, 5.8_

- [ ] 9. Checkpoint — en-en movies and songs verified
  - Ensure all 8 en-en curriculums (4 movies + 4 songs) exist with correct structure, collections wired, ask the user if questions arise.

- [ ] 10. en-en podcast curriculums (mirror from vi-en)
  - [ ] 10.1 Write `en-en-podcast-vocab-series/create_podcast_0_tim_urban.py` — mirror Tim Urban
    - Fetch vi-en source `lPa8rC1ua4rJrOUl` via `curriculum/getOne`
    - `strip_keys()` to remove auto-generated keys
    - Transform all Vietnamese user-facing text → hand-written English
    - Set `language="en"`, `userLanguage="en"`, `contentTypeTags=["podcast"]`
    - Include inline `strip_keys()` and `validate()` functions
    - Set `is_public = false`
    - _Requirements: 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 9.1, 9.2, 9.3, 9.4, 9.5_

  - [ ] 10.2 Write `en-en-podcast-vocab-series/create_podcast_1_amy_cuddy.py` — mirror Amy Cuddy
    - Fetch vi-en source `6r63yMCmoRH4AcWr`, strip keys, transform Vietnamese → English
    - Same mirror pattern as 10.1
    - _Requirements: 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 9.1, 9.2, 9.3, 9.4, 9.5_

  - [ ] 10.3 Write `en-en-podcast-vocab-series/create_podcast_2_julian_treasure.py` — mirror Julian Treasure
    - Fetch vi-en source `DUfee1HEWcBcNEXp`, strip keys, transform Vietnamese → English
    - Same mirror pattern as 10.1
    - _Requirements: 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 9.1, 9.2, 9.3, 9.4, 9.5_

  - [ ] 10.4 Write `en-en-podcast-vocab-series/create_podcast_3_brene_brown.py` — mirror Brené Brown
    - Fetch vi-en source `z0qB88II5SgkKYrp`, strip keys, transform Vietnamese → English
    - Same mirror pattern as 10.1
    - _Requirements: 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 9.1, 9.2, 9.3, 9.4, 9.5_

  - [ ] 10.5 Write `en-en-podcast-vocab-series/create_en_en_podcast_collection.py` orchestrator
    - Create Collection "Learn Vocabulary Through Podcasts"
    - Add all 4 curriculums directly to the collection via `curriculum-collection/addCurriculum`, set display orders 0–3
    - _Requirements: 6.7_

  - [ ] 10.6 Run all 4 mirror scripts and orchestrator, verify in database
    - Execute each `create_podcast_N_*.py` script, collect curriculum IDs
    - Execute orchestrator to wire collection
    - Check for duplicates by title + language + uid
    - _Requirements: 6.7, 6.8_

- [ ] 11. Checkpoint — en-en podcasts verified
  - Ensure all 4 en-en podcast curriculums exist with correct structure, collection wired, ask the user if questions arise.

- [ ] 12. Parity verification
  - [ ] 12.1 Run parity matrix query
    - Query database for all curriculums grouped by (language, userLanguage, contentTypeTags)
    - Verify exactly 4 curriculums per cell for all 12 cells (4 language pairs × 3 content types = 48 total)
    - _Requirements: 8.1, 8.2_

  - [ ] 12.2 Verify collection membership
    - Confirm every media curriculum belongs to exactly one Collection (directly, not via series)
    - _Requirements: 8.3_

  - [ ] 12.3 Verify no duplicates across all 48 curriculums
    - Check for multiple curriculums with same title + language + userLanguage + uid
    - _Requirements: 8.5_

  - [ ] 12.4 Verify Chinese podcast source differentiation
    - Confirm vi-zh and en-zh podcast `youtubeUrl` values differ from all vi-en and en-en podcast `youtubeUrl` values
    - Confirm vi-zh and en-zh podcast pairs share the same 4 `youtubeUrl` values
    - _Requirements: 7.1, 7.2_

- [ ] 13. Cleanup
  - [ ] 13.1 Delete all creation and orchestrator scripts from all 6 folders
    - Remove all `.py` files from: `en-zh-music-series/`, `vi-zh-podcast-vocab-series/`, `en-zh-podcast-vocab-series/`, `en-en-movie-vocab-series/`, `en-en-song-vocab-series/`, `en-en-podcast-vocab-series/`
    - _Requirements: 2.10, 3.11, 4.9, 5.9, 6.9_

  - [ ] 13.2 Create README.md in each of the 6 folders
    - Document: how content was created, collection/series IDs and titles, curriculum IDs and titles, SQL queries to find content in DB, recreation instructions
    - _Requirements: 2.10, 3.11, 4.9, 5.9, 6.9_

- [ ] 14. Final checkpoint — Full parity achieved
  - Ensure all 48 curriculums exist, all collections wired, all scripts deleted, all READMEs created, ask the user if questions arise.

## Notes

- Tasks marked with `*` are optional and can be skipped for faster MVP
- Items 2–3 (vi-zh/en-zh podcasts) require selecting 4 Chinese-language talks first (task 3.1) — this blocks all 8 podcast creation scripts
- Items 4–6 (en-en mirrors) are independent of each other and can be done in any order
- Mirror scripts fetch vi-en source at runtime — no hardcoded content from source curriculums
- All text must be hand-written per curriculum — no templated content generation
- All new curriculums must be private (`is_public = false`)
- Source scripts are deleted after verification, leaving only READMEs
