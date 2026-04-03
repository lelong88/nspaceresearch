# Implementation Plan: Description Tone Variety

## Overview

Rewrite all descriptions across collections, series, and curriculums, plus all farewell introAudio scripts, to replace monotonous template-like openers and formulaic sign-offs with varied, individually crafted persuasive copy. Each content level has its own script(s). Curriculum updates (descriptions + farewells) are organized as one script per series. All scripts query the DB in real-time for IDs. After verification, scripts are deleted, leaving only a README.

## Tasks

- [ ] 1. Inventory current descriptions via MCP Postgres
  - [x] 1.1 Query all collections with IDs, titles, and current descriptions
    - `SELECT id, title, description FROM curriculum_collections ORDER BY display_order;`
    - Record count and note which descriptions need rewriting
    - _Requirements: 1.3_

  - [x] 1.2 Query all series with IDs, titles, current descriptions, and parent collection
    - Corrected query (actual join table is `curriculum_collection_series`):
      `SELECT cs.id, cs.title, cs.description, ccs.curriculum_collection_id FROM curriculum_series cs LEFT JOIN curriculum_collection_series ccs ON cs.id = ccs.curriculum_series_id ORDER BY cs.display_order;`
    - **Total: 46 series** (44 assigned to collections, 2 orphaned)
    - **Adjacency groupings by collection (for tone variety planning):**
      - `72d8f528` **Power English** (6 series): Curious Minds, The Boardroom, Big Ideas Bigger Words, How the World Really Works, The Science Shelf, Mind & Society
      - `279d6843` **Học Từ Vựng Theo Chủ Đề** (8 series): Từ Vựng Học Thuật Qua Bài Đọc, Tâm Lý & Phát Triển Bản Thân, Sức Khỏe & Lối Sống, Khoa Học & Công Nghệ, Kinh Tế & Tài Chính, Môi Trường & Phát Triển Bền Vững, Khám Phá Châu Âu, Văn Hóa & Xã Hội
      - `bjgtj1xj` **Fiction** (3 series): Tháp Đồng Hồ Im Lặng, Khu Vườn Những Lá Thư, The Signal Beyond
      - `7nf5wi1d` **Truyện (小说)** (3 series): Tiếng Đàn Bên Hồ, 味道的记忆, Bức Tranh Biến Mất
      - `sh8f6jxy` **Fiction (小说)** (3 series): Memories of Flavor, The Vanishing Painting, The Sound of Music by the Lake
      - `97cee550` **Truyện (Fiction)** (2 series): Ánh Sáng Cuối Cùng, Tiệm Sách Nhỏ Bên Biển
      - `64fb68f8` **Sơ Cấp 2 (初级二)** (2 series): Hán Ngữ Phổ Thông - Sơ cấp 2, Triết Lý Trong Chữ Hán
      - `55hkk58y` **Elementary 2 (初级二)** (2 series): Standard Chinese — Elementary 2, Wisdom in Chinese Characters
      - `lqhx014h` **中文进阶** (2 series): 思维与认知, 社会与文明
      - `q9j66zxj` **Học Từ Vựng Theo Chủ Đề (主题词汇)** (1 series): Khám Phá Trung Quốc
      - `verb9xeh` **Thematic Vocabulary (主题词汇)** (1 series): Explore China
      - `95ea42ed` **Huấn Luyện Viên (Coaching)** (2 series): Leadership - Cơ bản, Chủ Doanh Nghiệp
      - `89acc79b` **Tiếng Anh Chuyên Nghiệp** (1 series): Hướng Dẫn Viên Du Lịch
      - `38fb6061` **News-Based Learning** (1 series): World News
      - `zf3wbzvi` **Writing Focus** (2 series): Writing Focus, Luyện Viết Tiếng Anh
      - `rmvq0pbo` **Speaking Focus** (2 series): Speaking Focus, Luyện Nói Tiếng Anh
      - `6lzqqynb` **Audio Guide** (2 series): Audio Guide, Học Qua Nghe
      - `bdccf5d1` **Tiếng Anh Thiếu Nhi** (1 series): Dành cho bé gái 10-14 tuổi
      - No collection (2 orphaned): Tăng Trưởng Qua Khó Khăn (`jdi8d27v`), Leadership (`d50f44ae`)
    - **Description status:** 12 series have NULL descriptions, 34 have existing descriptions (many formulaic/short)
    - _Requirements: 1.2_

  - [ ] 1.3 Query all curriculums grouped by series with IDs, titles, current descriptions, and farewell introAudio text
    - `SELECT csc.curriculum_series_id, c.id, c.title, c.content->>'description' as description FROM curriculum c JOIN curriculum_series_curriculums csc ON c.id = csc.curriculum_id WHERE c.uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73' ORDER BY csc.curriculum_series_id, c.display_order;`
    - Also note the last introAudio activity text in each curriculum's last session (farewell script)
    - Record count per series and total
    - _Requirements: 1.4, 8.1_

- [ ] 2. Create folder and write collection description update script
  - [ ] 2.1 Create `description-tone-variety/` folder at workspace root
    - _Requirements: 7.1_

  - [ ] 2.2 Write `description-tone-variety/update_collection_descriptions.py`
    - Query all collection IDs and titles from DB at runtime (no hardcoded IDs)
    - Hand-write each collection description individually using varied tones from the palette
    - Each description follows Persuasive_Copy_Style (bold headline, concrete examples, vivid metaphor, transformation promise)
    - No two collections use the same rhetorical opener type
    - Match language to collection context (Vietnamese for vi-*, English for en-*)
    - Send only `{id, description, firebaseIdToken}` — do NOT send title or thumbnail
    - Log each update with ID, title, and description snippet
    - Print summary (updated/failed/total)
    - _Requirements: 1.1, 4.1, 4.2, 4.3, 4.4, 4.5, 5.1, 5.4, 6.3, 6.4, 6.5, 7.2_

  - [ ] 2.3 Run collection description update script and verify
    - Execute `python update_collection_descriptions.py`
    - Verify all collections updated via MCP postgres query
    - Confirm no "Did you know" remnants
    - _Requirements: 4.1, 4.2_

- [ ] 3. Write and run series description update script
  - [ ] 3.1 Write `description-tone-variety/update_series_descriptions.py`
    - Query all series IDs, titles, and parent collections from DB at runtime
    - Hand-write each series description individually using varied tones
    - Validate every description is ≤ 255 characters before sending
    - Adjacent series in the same collection use different rhetorical approaches
    - Send only `{id, description, firebaseIdToken}` — do NOT send title or thumbnail
    - Log each update with ID, title, and description snippet
    - Print summary (updated/failed/total)
    - _Requirements: 1.1, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 5.1, 5.2, 5.4, 6.2, 6.4, 6.5, 7.2_

  - [ ] 3.2 Run series description update script and verify
    - Execute `python update_series_descriptions.py`
    - Verify all series updated via MCP postgres query
    - Confirm no description exceeds 255 chars: `SELECT id, title, length(description) FROM curriculum_series WHERE length(description) > 255;`
    - Confirm no "Did you know" remnants
    - _Requirements: 3.1, 3.2, 3.4_

- [ ] 4. Checkpoint — Collections and series descriptions verified
  - Ensure all collection and series descriptions are updated with varied tones, ask the user if questions arise.

- [ ] 5. Write and run curriculum description update scripts (one per series)
  - [ ] 5.1 Identify all series and their curriculum counts from the inventory (task 1)
    - List each series ID, title, and number of curriculums
    - Plan one script per series
    - _Requirements: 7.1_

  - [ ] 5.2 Write first batch of per-series curriculum update scripts
    - For each series, create `description-tone-variety/update_curriculum_series_<slug>.py`
    - Each script queries curriculum IDs in its target series from DB at runtime
    - For each curriculum: fetch full content via `curriculum/getOne`, replace the `description` field AND the farewell introAudio `text` field, strip `mp3Url` from the farewell activity only, push entire content back via `curriculum/update`
    - CRITICAL: Preserve all generated keys on all non-farewell activities — only strip `mp3Url` on the farewell introAudio
    - Hand-write each curriculum description AND farewell script individually using varied tones
    - No two adjacent curriculums in the series use the same opener type (for descriptions) or the same farewell tone
    - No single opener type exceeds 30% of descriptions in the series
    - Farewell scripts follow the quality standard (~400-600 words): review vocabulary with definitions and fresh examples, summarize learning journey, warm encouraging sign-off
    - Match language to curriculum context
    - Log each update with ID, title, and snippets of new description + farewell
    - Print summary (updated/failed/total)
    - _Requirements: 1.1, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 5.1, 5.2, 5.3, 5.4, 6.1, 6.4, 6.5, 7.1, 7.2, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7_

  - [ ] 5.3 Run first batch of curriculum update scripts and verify
    - Execute each per-series script
    - Verify descriptions updated via MCP postgres
    - Spot-check a few curriculums via `curriculum/getOne` to confirm: all non-description content preserved, farewell introAudio text updated, farewell mp3Url stripped, all other activities' mp3Url intact
    - _Requirements: 2.3, 6.1, 8.4, 8.5_

  - [ ] 5.4 Write and run remaining per-series curriculum update scripts
    - Continue until all series are covered
    - Same rules as 5.2 (descriptions + farewells, varied tones, mp3Url strip on farewell only)
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 5.1, 5.2, 5.3, 5.4, 6.1, 6.4, 6.5, 7.1, 7.2, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7_

- [ ] 6. Checkpoint — All curriculum descriptions and farewells verified
  - Ensure all curriculum descriptions updated with varied tones
  - Ensure all farewell introAudio scripts updated with varied tones
  - Verify farewell mp3Url stripped on all updated curriculums
  - Verify no "Did you know" remnants across all curriculums
  - Verify tone distribution: no opener type > 30% at curriculum level
  - Ask the user if questions arise.

- [ ] 7. Full verification pass
  - [ ] 7.1 Verify no template remnants across all three content levels
    - Run queries checking for "Did you know" and other template patterns in collections, series, and curriculums
    - _Requirements: 2.1, 3.1, 4.1_

  - [ ] 7.2 Verify tone distribution constraints
    - Count opener types at each content level
    - Confirm no single type > 30% at any level
    - Confirm no adjacent duplicates within any series or collection
    - _Requirements: 5.1, 5.2, 5.3_

  - [ ] 7.3 Verify content preservation on a sample of curriculums
    - Fetch 3-5 curriculums via `curriculum/getOne` and confirm: all non-description/non-farewell fields intact, farewell introAudio text is new, farewell mp3Url is stripped, all other activities' generated keys preserved
    - _Requirements: 2.3, 6.1, 8.4, 8.5_

  - [ ] 7.4 Verify series description lengths
    - Confirm no series description exceeds 255 chars
    - _Requirements: 3.4_

- [ ] 8. Cleanup and documentation
  - [ ] 8.1 Delete all update scripts from `description-tone-variety/`
    - Remove all `.py` files
    - _Requirements: 7.3_

  - [ ] 8.2 Create `description-tone-variety/README.md`
    - Document what was changed (all descriptions across collections, series, curriculums)
    - Include SQL queries to verify descriptions in DB
    - Include tone palette reference and distribution rules
    - Provide instructions to re-run if needed
    - _Requirements: 7.3_

## Notes

- Curriculum update scripts MUST NOT strip generated keys on non-farewell activities — only modify the `description` field and the farewell introAudio `text` field
- Strip `mp3Url` ONLY on the farewell introAudio activity (last introAudio in last session) so audio is regenerated from new text
- Farewell scripts follow the quality standard: ~400-600 words, review each vocabulary word with definition and fresh example, summarize learning journey, warm encouraging sign-off
- Series descriptions have a hard 255-char DB limit — validate before sending
- Collection and series updates send only `{id, description, firebaseIdToken}` — never include title or thumbnail
- All descriptions and farewells are hand-written — no template functions or string interpolation for learner-facing text
- Scripts query DB at runtime for IDs — no hardcoded IDs that go stale
- The tone palette has 6 types: provocative question, bold declaration, vivid scenario, empathetic observation, surprising fact, metaphor-led hook
- Task 5 (curriculum scripts) is the bulk of the work — one script per series, each with individually crafted descriptions AND farewell scripts
