# Implementation Plan: Description Tone Variety

## Overview

Rewrite all descriptions across collections, series, and curriculums, plus all farewell introAudio scripts, to replace monotonous template-like openers and formulaic sign-offs with varied, individually crafted persuasive copy. Each content level has its own script(s). Curriculum updates (descriptions + farewells) are organized as one script per series. All scripts query the DB in real-time for IDs. After verification, scripts are deleted, leaving only a README.

## Tasks

- [x] 1. Inventory current descriptions via MCP Postgres
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

  - [x] 1.3 Query all curriculums grouped by series with IDs, titles, current descriptions, and farewell introAudio text
    - Corrected query (actual table is `curriculum_series_items`, title is in `content` jsonb):
      `SELECT csi.curriculum_series_id, c.id, c.content->>'title' as title, c.content->>'description' as description FROM curriculum c JOIN curriculum_series_items csi ON c.id = csi.curriculum_id WHERE c.uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73' ORDER BY csi.curriculum_series_id, c.display_order;`
    - Farewell introAudio query (last introAudio in last session):
      `SELECT c.id, (SELECT a->'data'->>'text' FROM jsonb_array_elements(c.content->'learningSessions'->-1->'activities') WITH ORDINALITY AS t(a, idx) WHERE a->>'activityType' = 'introAudio' ORDER BY idx DESC LIMIT 1) as farewell_text FROM curriculum c WHERE c.id = '<id>';`
    - **Total: 326 unique curriculums across 45 series** (327 rows; 1 curriculum "Nấu Cá Hồi Áp Chảo" appears in 2 series)
    - **374 total curriculums owned by this UID; 48 not in any series**
    - **Farewell status: 197 curriculums have farewell introAudio, 130 do not** (novels/stories with readAlong-heavy final sessions may lack a farewell introAudio)
    - **Curriculum counts per series (for per-series script planning):**
      - `009194da` **Dành cho bé gái 10-14 tuổi** — 2 curriculums
      - `04kh7nyk` **Audio Guide** — 2 curriculums
      - `09o7ke5d` **How the World Really Works** — 8 curriculums
      - `0ofwj9eg` **Wisdom in Chinese Characters** — 4 curriculums
      - `1e6e8a71` **Hướng Dẫn Viên Du Lịch (Tour Guides)** — 4 curriculums
      - `1r0l5nos` **Big Ideas, Bigger Words** — 8 curriculums
      - `2wlmlwpz` **The Signal Beyond** — 20 curriculums
      - `3d836654` **World News** — 4 curriculums
      - `6aqul3cz` **Khám Phá Châu Âu (Discover Europe)** — 4 curriculums
      - `6k2ij0ut` **Tâm Lý & Phát Triển Bản Thân** — 3 curriculums
      - `70b5bb22` **Ánh Sáng Cuối Cùng (The Last Light of Alder House)** — 20 curriculums
      - `85d6512e` **Chủ Doanh Nghiệp (Business Owner)** — 5 curriculums
      - `8c79a794` **Leadership - Cơ bản** — 1 curriculum
      - `8ncovquk` **Speaking Focus** — 2 curriculums
      - `8vwp780s` **Memories of Flavor (en-zh)** — 10 curriculums
      - `9gfei23g` **The Boardroom** — 8 curriculums
      - `bapehjcu` **Từ Vựng Học Thuật Qua Bài Đọc** — 8 curriculums
      - `db5930f6` **Curious Minds** — 10 curriculums
      - `dqce6wbh` **Hán Ngữ Phổ Thông - Sơ cấp 2** — 25 curriculums
      - `e24f29c4` **Sức Khỏe & Lối Sống** — 8 curriculums
      - `f5ort29f` **Khu Vườn Những Lá Thư** — 10 curriculums
      - `jdi8d27v` **Tăng Trưởng Qua Khó Khăn** — 2 curriculums
      - `kxxkeo1f` **Mind & Society** — 11 curriculums
      - `mg9ud60h` **Môi Trường & Phát Triển Bền Vững** — 4 curriculums
      - `mkxbcpty` **思维与认知** — 4 curriculums
      - `n1jopztf` **Writing Focus** — 2 curriculums
      - `n4y9zm3v` **Tiệm Sách Nhỏ Bên Biển** — 10 curriculums
      - `n7qs5dwv` **Văn Hóa & Xã Hội** — 4 curriculums
      - `nywzaazm` **The Vanishing Painting (en-zh)** — 10 curriculums
      - `qm9pj07x` **社会与文明** — 4 curriculums
      - `r01mrt51` **Học Qua Nghe** — 2 curriculums
      - `r8vwa6hv` **Tháp Đồng Hồ Im Lặng** — 10 curriculums
      - `ry534vdc` **Explore China (en-zh)** — 4 curriculums
      - `sltfah2w` **Standard Chinese — Elementary 2** — 25 curriculums
      - `strxp8gn` **Luyện Viết Tiếng Anh** — 2 curriculums
      - `sv3uijyq` **Khoa Học & Công Nghệ** — 4 curriculums
      - `u6mywecv` **Kinh Tế & Tài Chính** — 4 curriculums
      - `ui33faux` **Luyện Nói Tiếng Anh** — 4 curriculums
      - `uq7ezeuh` **味道的记忆 (vi-zh)** — 10 curriculums
      - `vxvh04b5` **Triết Lý Trong Chữ Hán (vi-zh)** — 4 curriculums
      - `wlzqfag8` **Bức Tranh Biến Mất (vi-zh)** — 10 curriculums
      - `xb4mrvfp` **The Sound of Music by the Lake (en-zh)** — 10 curriculums
      - `xwznpgdr` **The Science Shelf** — 7 curriculums
      - `yjwuyhtk` **Khám Phá Trung Quốc (vi-zh)** — 4 curriculums
      - `z6xddztr` **Tiếng Đàn Bên Hồ (vi-zh)** — 10 curriculums
    - **Farewell introAudio patterns observed:**
      - English vocab curriculums: ~1900-2800 chars, review each word with definition + example, warm sign-off
      - Vietnamese vocab curriculums: ~600-1000 chars, shorter review, warm sign-off in Vietnamese
      - Chinese character curriculums: ~1300-1500 chars, review radical + characters, philosophical sign-off
      - Novel/story curriculums: Many lack farewell introAudio (final session is readAlong-heavy)
    - **Content structure notes for update scripts:**
      - Sessions key: `learningSessions` (not `sessions`)
      - Activity type key: `activityType` (not `type`)
      - Activity text is at: `activity.data.text` (not `activity.text`)
      - Activity mp3Url is at: `activity.data.mp3Url`
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

- [x] 3. Write and run series description update script
  - [x] 3.1 Write `description-tone-variety/update_series_descriptions.py`
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

- [x] 4. Checkpoint — Collections and series descriptions verified
  - Ensure all collection and series descriptions are updated with varied tones, ask the user if questions arise.

- [x] 5. Write and run curriculum description update scripts (one per series)
  - [x] 5.1 Identify all series and their curriculum counts from the inventory (task 1)
    - List each series ID, title, and number of curriculums
    - Plan one script per series
    - **Live query results (45 series, 326 curriculums total):**
      - `009194da` **Dành cho bé gái 10-14 tuổi** — 2 curriculums → `update_curriculum_series_be_gai.py`
      - `04kh7nyk` **Audio Guide** — 2 curriculums → `update_curriculum_series_audio_guide.py`
      - `09o7ke5d` **How the World Really Works** — 8 curriculums → `update_curriculum_series_how_world_works.py`
      - `0ofwj9eg` **Wisdom in Chinese Characters (汉字中的智慧)** — 4 curriculums → `update_curriculum_series_wisdom_chars_enzh.py`
      - `1e6e8a71` **Hướng Dẫn Viên Du Lịch (Tour Guides)** — 4 curriculums → `update_curriculum_series_tour_guides.py`
      - `1r0l5nos` **Big Ideas, Bigger Words** — 8 curriculums → `update_curriculum_series_big_ideas.py`
      - `2wlmlwpz` **The Signal Beyond** — 20 curriculums → `update_curriculum_series_signal_beyond.py`
      - `3d836654` **World News** — 4 curriculums → `update_curriculum_series_world_news.py`
      - `6aqul3cz` **Khám Phá Châu Âu (Discover Europe)** — 4 curriculums → `update_curriculum_series_chau_au.py`
      - `6k2ij0ut` **Tâm Lý & Phát Triển Bản Thân** — 3 curriculums → `update_curriculum_series_tam_ly.py`
      - `70b5bb22` **Ánh Sáng Cuối Cùng (The Last Light of Alder House)** — 20 curriculums → `update_curriculum_series_anh_sang.py`
      - `85d6512e` **Chủ Doanh Nghiệp (Business Owner)** — 5 curriculums → `update_curriculum_series_chu_doanh_nghiep.py`
      - `8c79a794` **Leadership - Cơ bản** — 1 curriculum → `update_curriculum_series_leadership.py`
      - `8ncovquk` **Speaking Focus** — 2 curriculums → `update_curriculum_series_speaking_focus.py`
      - `8vwp780s` **Memories of Flavor (味道的记忆)** — 10 curriculums → `update_curriculum_series_memories_flavor_enzh.py`
      - `9gfei23g` **The Boardroom** — 8 curriculums → `update_curriculum_series_boardroom.py`
      - `bapehjcu` **Từ Vựng Học Thuật Qua Bài Đọc** — 8 curriculums → `update_curriculum_series_tu_vung_hoc_thuat.py`
      - `db5930f6` **Curious Minds** — 10 curriculums → `update_curriculum_series_curious_minds.py`
      - `dqce6wbh` **Hán Ngữ Phổ Thông - Sơ cấp 2** — 25 curriculums → `update_curriculum_series_han_ngu_so_cap.py`
      - `e24f29c4` **Sức Khỏe & Lối Sống** — 8 curriculums → `update_curriculum_series_suc_khoe.py`
      - `f5ort29f` **Khu Vườn Những Lá Thư (The Garden of Forgotten Letters)** — 10 curriculums → `update_curriculum_series_khu_vuon.py`
      - `jdi8d27v` **Tăng Trưởng Qua Khó Khăn** — 2 curriculums → `update_curriculum_series_tang_truong.py`
      - `kxxkeo1f` **Mind & Society** — 11 curriculums → `update_curriculum_series_mind_society.py`
      - `mg9ud60h` **Môi Trường & Phát Triển Bền Vững** — 4 curriculums → `update_curriculum_series_moi_truong.py`
      - `mkxbcpty` **思维与认知** — 4 curriculums → `update_curriculum_series_siwei_yuren.py`
      - `n1jopztf` **Writing Focus** — 2 curriculums → `update_curriculum_series_writing_focus.py`
      - `n4y9zm3v` **Tiệm Sách Nhỏ Bên Biển** — 10 curriculums → `update_curriculum_series_tiem_sach.py`
      - `n7qs5dwv` **Văn Hóa & Xã Hội** — 4 curriculums → `update_curriculum_series_van_hoa.py`
      - `nywzaazm` **The Vanishing Painting (消失的画)** — 10 curriculums → `update_curriculum_series_vanishing_painting_enzh.py`
      - `qm9pj07x` **社会与文明** — 4 curriculums → `update_curriculum_series_shehui_wenming.py`
      - `r01mrt51` **Học Qua Nghe** — 2 curriculums → `update_curriculum_series_hoc_qua_nghe.py`
      - `r8vwa6hv` **Tháp Đồng Hồ Im Lặng** — 10 curriculums → `update_curriculum_series_thap_dong_ho.py`
      - `ry534vdc` **Explore China (探索中国)** — 4 curriculums → `update_curriculum_series_explore_china_enzh.py`
      - `sltfah2w` **Standard Chinese — Elementary 2** — 25 curriculums → `update_curriculum_series_standard_chinese.py`
      - `strxp8gn` **Luyện Viết Tiếng Anh** — 2 curriculums → `update_curriculum_series_luyen_viet.py`
      - `sv3uijyq` **Khoa Học & Công Nghệ** — 4 curriculums → `update_curriculum_series_khoa_hoc.py`
      - `u6mywecv` **Kinh Tế & Tài Chính** — 4 curriculums → `update_curriculum_series_kinh_te.py`
      - `ui33faux` **Luyện Nói Tiếng Anh** — 4 curriculums → `update_curriculum_series_luyen_noi.py`
      - `uq7ezeuh` **味道的记忆 (Ký Ức Hương Vị)** — 10 curriculums → `update_curriculum_series_memories_flavor_vizh.py`
      - `vxvh04b5` **Triết Lý Trong Chữ Hán** — 4 curriculums → `update_curriculum_series_triet_ly_chu_han.py`
      - `wlzqfag8` **Bức Tranh Biến Mất (消失的画)** — 10 curriculums → `update_curriculum_series_buc_tranh_vizh.py`
      - `xb4mrvfp` **The Sound of Music by the Lake (湖边的琴声)** — 10 curriculums → `update_curriculum_series_sound_music_enzh.py`
      - `xwznpgdr` **The Science Shelf** — 7 curriculums → `update_curriculum_series_science_shelf.py`
      - `yjwuyhtk` **Khám Phá Trung Quốc (探索中国)** — 4 curriculums → `update_curriculum_series_kham_pha_tq.py`
      - `z6xddztr` **Tiếng Đàn Bên Hồ (湖边的琴声)** — 10 curriculums → `update_curriculum_series_tieng_dan_vizh.py`
    - **Plan: 45 scripts total, one per series**
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
