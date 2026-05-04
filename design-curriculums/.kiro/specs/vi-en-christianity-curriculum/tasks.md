# Implementation Plan: Vietnamese-English Christianity Curriculums

## Overview

Create 20 English-learning curriculums for Vietnamese speakers on Christianity topics. Scripts go in `vi-en-christianity-curriculum/`. Reuses root-level `api_helpers.py`.

Three formats: story_reading (contentTypeTags: ["story"], 7 curriculums), speaking (contentTypeTags: [], 6 curriculums), balanced (contentTypeTags: [], 7 curriculums). All curriculums: 4 sessions, 10-12 vocab words, price 49. Language pair: userLanguage="vi", language="en".

Execution order: (1) create validator + PBT tests, (2) run orchestrator to create collection + 3 series, (3) story-reading scripts x7, (4) speaking scripts x6, (5) balanced scripts x7, (6) verification queries, (7) documentation + cleanup.

## Tasks

- [ ] 1. Create content validator with property-based tests
  - [x] 1.1 Create `vi-en-christianity-curriculum/validate_content.py` with format-aware `validate(content, format)` function
    - `format` parameter: `"story_reading"`, `"speaking"`, or `"balanced"`
    - Top-level structure checks: `title` (non-empty string), `description` (non-empty string), `preview.text` (non-empty string), `contentTypeTags`, `learningSessions` (array of exactly 4 sessions)
    - Session structure: each session has `title` (non-empty string) and `activities` (non-empty array)
    - Activity structure: each activity has `activityType` (not `type`), `title`, `description`, `data` (dict); content fields inside `data`, not inline
    - Valid activityType values: introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence, writingParagraph
    - vocabList validation: array of lowercase strings, field name `vocabList` (never `words`)
    - Flashcard consistency: viewFlashcards and speakFlashcards in same session must have identical vocabList
    - writingSentence: `data.vocabList`, `data.items` (non-empty array), each item has `prompt` and `targetVocab`
    - writingParagraph: `data.vocabList`, `data.instructions` (non-empty string), `data.prompts` (array, length >= 2)
    - Strip-keys exclusion: reject any of mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId anywhere in JSON tree
    - contentTypeTags per format: `["story"]` for story_reading, `[]` for speaking/balanced
    - Activity sequence validation: verify activity type sequence matches the declared format template for each session
    - Writing activity restriction: writingSentence and writingParagraph only allowed in sessions 3 and 4
    - Raise `ValueError` with specific violation message identifying the rule, location (session/activity index), and expected vs actual value
    - _Requirements: 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 10.9, 10.10, 10.11, 16.4_

  - [x] 1.2 Write property tests for validate_content.py
    - Create `vi-en-christianity-curriculum/test_validate_content.py` using Hypothesis library
    - **Property 1: Valid content passes validation**
    - **Property 2: contentTypeTags validation per format**
    - **Property 3: Strip keys rejected anywhere in JSON tree**
    - **Property 4: Activity sequence matches declared format**
    - **Property 5: Activity structural requirements enforced**
    - **Property 6: vocabList format enforced**
    - **Property 7: Flashcard vocabList consistency within sessions**
    - **Property 8: writingSentence structure enforced**
    - **Property 9: writingParagraph structure enforced**
    - **Property 10: Top-level structure enforced**
    - **Property 11: Writing activities restricted to sessions 3 and 4**
    - Minimum 100 iterations per property test
    - Generator strategies: `valid_curriculum(format)`, `random_activity(activity_type)`, `random_vocab_list(n)`, `random_strip_key()`, `random_json_path()`, `random_format()`
    - **Validates: Requirements 1.4, 1.5, 1.6, 3.1, 3.2, 3.3, 3.4, 9.1-9.7, 10.1-10.11, 16.4**

- [ ] 2. Create orchestrator script
  - [x] 2.1 Create `vi-en-christianity-curriculum/orchestrator.py`
    - Create 1 collection: "Kitô Giáo & Đức Tin" with neutral informative Vietnamese description
    - Create 3 series:
      - Series 1: "Đọc Truyện Kinh Thánh" (story-reading, 7 curriculums) — description tone: `vivid_scenario`, ≤255 chars
      - Series 2: "Luyện Nói Về Đức Tin" (speaking, 6 curriculums) — description tone: `empathetic_observation`, ≤255 chars
      - Series 3: "Kỹ Năng Toàn Diện" (balanced, 7 curriculums) — description tone: `bold_declaration`, ≤255 chars
    - Wire all 3 series to the collection via `add_series_to_collection`
    - Set series display orders: Series 1 = 1, Series 2 = 2, Series 3 = 3
    - Print collection_id and all 3 series_ids for use in curriculum scripts
    - Uses root-level `api_helpers.py` (create_collection, create_series, add_series_to_collection, set_series_display_order)
    - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5, 8.7, 11.2, 11.3, 11.4, 11.5_

- [x] 3. Checkpoint — Run orchestrator and verify infrastructure
  - Run `python orchestrator.py` in `vi-en-christianity-curriculum/`
  - Verify collection and 3 series exist in DB
  - Record collection_id and series_ids for curriculum scripts
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 4. Create story-reading curriculum scripts (7 scripts, Series 1: "Đọc Truyện Kinh Thánh")
  - [x] 4.1 Create `vi-en-christianity-curriculum/create_cau_chuyen_sang_the.py` — "Câu Chuyện Sáng Thế"
    - Story-reading format: 4 sessions, 10 words, price 49, contentTypeTags: ["story"]
    - Level: preintermediate
    - vocabList: ["creation", "paradise", "forbidden", "temptation", "innocence", "serpent", "disobedience", "banish", "garden", "blessing"]
    - Activity sequence per story_reading template (sessions 1-4 as defined in design)
    - Description tone: `provocative_question`, farewell tone: `introspective_guide`
    - Series 1, display order: 1
    - Narrative: The creation story from Genesis and the Garden of Eden
    - Validate with `validate(content, "story_reading")` before upload
    - _Requirements: 1.1, 1.2, 1.4, 1.6, 1.7, 2.1, 3.1, 3.4, 4.1, 4.4, 4.5, 4.6, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.4, 6.5, 6.6, 7.1, 9.1-9.8, 10.1-10.11, 11.1, 11.6, 11.7, 12.1, 13.1-13.4, 16.1, 16.4_

  - [x] 4.2 Create `vi-en-christianity-curriculum/create_hanh_trinh_cua_moi_se.py` — "Hành Trình Của Môi-se"
    - Story-reading format: 4 sessions, 10 words, price 49, contentTypeTags: ["story"]
    - Level: preintermediate
    - vocabList: ["exodus", "pharaoh", "plague", "commandment", "wilderness", "covenant", "deliver", "miracle", "tablet", "prophet"]
    - Description tone: `vivid_scenario`, farewell tone: `warm_accountability`
    - Series 1, display order: 2
    - Narrative: Moses leading the Israelites out of Egypt through the Red Sea
    - _Requirements: same as 4.1_

  - [x] 4.3 Create `vi-en-christianity-curriculum/create_dem_thanh_giang_sinh.py` — "Đêm Thánh Giáng Sinh"
    - Story-reading format: 4 sessions, 10 words, price 49, contentTypeTags: ["story"]
    - Level: preintermediate
    - vocabList: ["manger", "shepherd", "angel", "star", "humble", "journey", "inn", "swaddling", "proclaim", "adore"]
    - Description tone: `empathetic_observation`, farewell tone: `quiet_awe`
    - Series 1, display order: 3
    - Narrative: The nativity story of Jesus's birth in Bethlehem
    - _Requirements: same as 4.1_

  - [x] 4.4 Create `vi-en-christianity-curriculum/create_con_duong_thap_gia.py` — "Con Đường Thập Giá"
    - Story-reading format: 4 sessions, 10 words, price 49, contentTypeTags: ["story"]
    - Level: intermediate
    - vocabList: ["crucifixion", "resurrection", "sacrifice", "betrayal", "redemption", "tomb", "ascension", "atonement", "crown", "eternal"]
    - Description tone: `bold_declaration`, farewell tone: `team_building_energy`
    - Series 1, display order: 4
    - Narrative: The passion narrative — Jesus's trial, crucifixion, and resurrection
    - _Requirements: same as 4.1 (with 1.2 intermediate level)_

  - [x] 4.5 Create `vi-en-christianity-curriculum/create_nhung_du_ngon_cua_chua.py` — "Những Dụ Ngôn Của Chúa"
    - Story-reading format: 4 sessions, 12 words, price 49, contentTypeTags: ["story"]
    - Level: intermediate
    - vocabList: ["parable", "prodigal", "compassion", "sow", "harvest", "repentance", "mercy", "neighbor", "forgive", "steward", "vineyard", "inheritance"]
    - Description tone: `surprising_fact`, farewell tone: `practical_momentum`
    - Series 1, display order: 5
    - Narrative: Jesus's parables — the Prodigal Son, Good Samaritan, and Sower
    - _Requirements: same as 4.4_

  - [x] 4.6 Create `vi-en-christianity-curriculum/create_thanh_phaolo_tren_duong.py` — "Thánh Phaolô Trên Đường Đa-mát"
    - Story-reading format: 4 sessions, 12 words, price 49, contentTypeTags: ["story"]
    - Level: intermediate
    - vocabList: ["conversion", "missionary", "epistle", "persecution", "apostle", "revelation", "preach", "congregation", "testimony", "gentile", "shipwreck", "imprisonment"]
    - Description tone: `metaphor_led`, farewell tone: `introspective_guide`
    - Series 1, display order: 6
    - Narrative: Paul's conversion and missionary journeys across the Roman Empire
    - _Requirements: same as 4.4_

  - [x] 4.7 Create `vi-en-christianity-curriculum/create_cac_vi_thanh_tu_dao.py` — "Các Vị Thánh Tử Đạo Việt Nam"
    - Story-reading format: 4 sessions, 12 words, price 49, contentTypeTags: ["story"]
    - Level: intermediate
    - vocabList: ["martyr", "persevere", "tribunal", "decree", "steadfast", "witness", "diocese", "catechist", "proclaim", "endure", "venerate", "canonize"]
    - Description tone: `provocative_question`, farewell tone: `warm_accountability`
    - Series 1, display order: 7
    - Narrative: Stories of Vietnamese Christian martyrs and their faith under persecution
    - _Requirements: same as 4.4_

- [x] 5. Checkpoint — Run story-reading scripts and verify
  - Run all 7 story-reading scripts in order (display order 1-7)
  - Verify 7 curriculums exist in Series 1 with correct display orders
  - Verify prices: all 7 at price 49
  - Verify language pair: all have `language="en"`, `userLanguage="vi"`
  - Verify contentTypeTags: all 7 have `["story"]`
  - Run duplicate check for all 7 titles
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 6. Create speaking curriculum scripts (6 scripts, Series 2: "Luyện Nói Về Đức Tin")
  - [x] 6.1 Create `vi-en-christianity-curriculum/create_tai_nha_tho.py` — "Tại Nhà Thờ"
    - Speaking format: 4 sessions, 10 words, price 49, contentTypeTags: []
    - Level: preintermediate
    - vocabList: ["congregation", "sermon", "hymn", "pew", "altar", "choir", "worship", "kneel", "communion", "blessing"]
    - Activity sequence per speaking template (sessions 1-4 as defined in design)
    - Description tone: `bold_declaration`, farewell tone: `quiet_awe`
    - Series 2, display order: 1
    - Topic: Vocabulary for attending church services and describing worship activities
    - Validate with `validate(content, "speaking")` before upload
    - _Requirements: 1.1, 1.2, 1.5, 1.6, 1.7, 2.1, 3.2, 3.4, 4.2, 4.4, 4.5, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.4, 6.5, 6.6, 7.1, 9.1-9.8, 10.1-10.11, 11.1, 11.6, 11.7, 12.1, 13.1-13.4, 16.1, 16.4_

  - [x] 6.2 Create `vi-en-christianity-curriculum/create_cau_nguyen_moi_ngay.py` — "Cầu Nguyện Mỗi Ngày"
    - Speaking format: 4 sessions, 10 words, price 49, contentTypeTags: []
    - Level: preintermediate
    - vocabList: ["prayer", "gratitude", "petition", "intercede", "meditate", "devotion", "rosary", "intention", "praise", "thanksgiving"]
    - Description tone: `vivid_scenario`, farewell tone: `team_building_energy`
    - Series 2, display order: 2
    - Topic: Conversational phrases for discussing prayer life and spiritual habits
    - _Requirements: same as 6.1_

  - [x] 6.3 Create `vi-en-christianity-curriculum/create_noi_ve_duc_tin.py` — "Nói Về Đức Tin"
    - Speaking format: 4 sessions, 10 words, price 49, contentTypeTags: []
    - Level: preintermediate
    - vocabList: ["faith", "believe", "grace", "soul", "salvation", "eternal", "scripture", "gospel", "trust", "hope"]
    - Description tone: `surprising_fact`, farewell tone: `practical_momentum`
    - Series 2, display order: 3
    - Topic: Vocabulary for expressing personal faith and beliefs in English conversations
    - _Requirements: same as 6.1_

  - [x] 6.4 Create `vi-en-christianity-curriculum/create_doi_thoai_lien_ton.py` — "Đối Thoại Liên Tôn"
    - Speaking format: 4 sessions, 12 words, price 49, contentTypeTags: []
    - Level: intermediate
    - vocabList: ["dialogue", "doctrine", "denomination", "ecumenical", "theology", "interfaith", "tradition", "sacrament", "liturgy", "orthodox", "evangelical", "charismatic"]
    - Description tone: `empathetic_observation`, farewell tone: `introspective_guide`
    - Series 2, display order: 4
    - Topic: Vocabulary for discussing Christianity with people of other faiths respectfully
    - _Requirements: same as 6.1 (with 1.2 intermediate level)_

  - [x] 6.5 Create `vi-en-christianity-curriculum/create_chia_se_chung_tu.py` — "Chia Sẻ Chứng Từ"
    - Speaking format: 4 sessions, 12 words, price 49, contentTypeTags: []
    - Level: intermediate
    - vocabList: ["testimony", "transform", "encounter", "surrender", "renewal", "conviction", "calling", "breakthrough", "deliverance", "restoration", "reconcile", "profound"]
    - Description tone: `metaphor_led`, farewell tone: `warm_accountability`
    - Series 2, display order: 5
    - Topic: Expressing personal spiritual experiences and testimony in English
    - _Requirements: same as 6.4_

  - [x] 6.6 Create `vi-en-christianity-curriculum/create_phuc_vu_cong_dong.py` — "Phục Vụ Cộng Đồng"
    - Speaking format: 4 sessions, 12 words, price 49, contentTypeTags: []
    - Level: intermediate
    - vocabList: ["volunteer", "outreach", "compassion", "donate", "shelter", "orphanage", "mission", "advocate", "dignity", "empower", "stewardship", "generosity"]
    - Description tone: `provocative_question`, farewell tone: `quiet_awe`
    - Series 2, display order: 6
    - Topic: Discussing Christian community service and charity work in English
    - _Requirements: same as 6.4_

- [x] 7. Checkpoint — Run speaking scripts and verify
  - Run all 6 speaking scripts in order (display order 1-6)
  - Verify 6 curriculums exist in Series 2 with correct display orders
  - Verify prices: all 6 at price 49
  - Verify language pair: all have `language="en"`, `userLanguage="vi"`
  - Verify contentTypeTags: all 6 have `[]`
  - Run duplicate check for all 6 titles
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 8. Create balanced curriculum scripts (7 scripts, Series 3: "Kỹ Năng Toàn Diện")
  - [x] 8.1 Create `vi-en-christianity-curriculum/create_mua_phuc_sinh.py` — "Mùa Phục Sinh"
    - Balanced format: 4 sessions, 10 words, price 49, contentTypeTags: []
    - Level: preintermediate
    - vocabList: ["resurrection", "lent", "fasting", "palm", "vigil", "rejoice", "tomb", "risen", "celebrate", "renewal"]
    - Activity sequence per balanced template (sessions 1-4 as defined in design)
    - Description tone: `bold_declaration`, farewell tone: `team_building_energy`
    - Series 3, display order: 1
    - Topic: Easter traditions, meaning, and celebrations in Christian culture
    - Validate with `validate(content, "balanced")` before upload
    - _Requirements: 1.1, 1.2, 1.5, 1.6, 1.7, 2.1, 3.3, 3.4, 4.3, 4.4, 4.5, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.4, 6.5, 6.6, 7.1, 9.1-9.8, 10.1-10.11, 11.1, 11.6, 11.7, 12.1, 13.1-13.4, 16.1, 16.2, 16.3, 16.4_

  - [x] 8.2 Create `vi-en-christianity-curriculum/create_thanh_ca_va_tho_phuong.py` — "Thánh Ca Và Thờ Phượng"
    - Balanced format: 4 sessions, 10 words, price 49, contentTypeTags: []
    - Level: preintermediate
    - vocabList: ["hymn", "melody", "chorus", "praise", "worship", "harmony", "lyric", "uplift", "sacred", "joyful"]
    - Description tone: `empathetic_observation`, farewell tone: `practical_momentum`
    - Series 3, display order: 2
    - Topic: Christian hymns, worship music, and their role in spiritual life
    - _Requirements: same as 8.1_

  - [x] 8.3 Create `vi-en-christianity-curriculum/create_giang_sinh_o_viet_nam.py` — "Giáng Sinh Ở Việt Nam"
    - Balanced format: 4 sessions, 10 words, price 49, contentTypeTags: []
    - Level: preintermediate
    - vocabList: ["nativity", "carol", "ornament", "festive", "midnight", "lantern", "tradition", "gather", "exchange", "goodwill"]
    - Description tone: `vivid_scenario`, farewell tone: `introspective_guide`
    - Series 3, display order: 3
    - Topic: How Vietnamese Christians celebrate Christmas with local traditions
    - _Requirements: same as 8.1_

  - [x] 8.4 Create `vi-en-christianity-curriculum/create_bi_tich_va_nghi_le.py` — "Bí Tích Và Nghi Lễ"
    - Balanced format: 4 sessions, 10 words, price 49, contentTypeTags: []
    - Level: preintermediate
    - vocabList: ["baptism", "confirmation", "eucharist", "confession", "anoint", "matrimony", "ordination", "sacred", "ceremony", "vow"]
    - Description tone: `surprising_fact`, farewell tone: `warm_accountability`
    - Series 3, display order: 4
    - Topic: The seven sacraments and key Christian rituals explained
    - _Requirements: same as 8.1_

  - [x] 8.5 Create `vi-en-christianity-curriculum/create_duc_tin_va_doi_song.py` — "Đức Tin Và Đời Sống"
    - Balanced format: 4 sessions, 12 words, price 49, contentTypeTags: []
    - Level: intermediate
    - vocabList: ["integrity", "discernment", "conscience", "virtue", "temptation", "perseverance", "humility", "gratitude", "discipline", "accountability", "purpose", "vocation"]
    - Description tone: `metaphor_led`, farewell tone: `quiet_awe`
    - Series 3, display order: 5
    - Topic: How Christian faith integrates with modern daily life and ethical decisions
    - _Requirements: same as 8.1 (with 1.2 intermediate level)_

  - [x] 8.6 Create `vi-en-christianity-curriculum/create_lich_su_giao_hoi.py` — "Lịch Sử Giáo Hội"
    - Balanced format: 4 sessions, 12 words, price 49, contentTypeTags: []
    - Level: intermediate
    - vocabList: ["reformation", "council", "missionary", "cathedral", "monastery", "crusade", "schism", "papal", "diocese", "ecumenical", "renaissance", "enlightenment"]
    - Description tone: `provocative_question`, farewell tone: `team_building_energy`
    - Series 3, display order: 6
    - Topic: Key moments in Church history from early Christians to the modern era
    - _Requirements: same as 8.5_

  - [x] 8.7 Create `vi-en-christianity-curriculum/create_triet_hoc_kito_giao.py` — "Triết Học Kitô Giáo"
    - Balanced format: 4 sessions, 12 words, price 49, contentTypeTags: []
    - Level: intermediate
    - vocabList: ["theodicy", "providence", "omniscient", "benevolent", "freewill", "transcendence", "incarnation", "trinity", "revelation", "redemption", "existential", "contemplation"]
    - Description tone: `bold_declaration`, farewell tone: `practical_momentum`
    - Series 3, display order: 7
    - Topic: Christian philosophical concepts — free will, theodicy, love, and meaning
    - _Requirements: same as 8.5_

- [x] 9. Checkpoint — Run balanced scripts and verify
  - Run all 7 balanced scripts in order (display order 1-7)
  - Verify 7 curriculums exist in Series 3 with correct display orders
  - Verify prices: all 7 at price 49
  - Verify language pair: all have `language="en"`, `userLanguage="vi"`
  - Verify contentTypeTags: all 7 have `[]`
  - Run duplicate check for all 7 titles
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 10. Verification — Confirm all 20 curriculums in database
  - [x] 10.1 Run full verification queries
    - Count all 20 curriculum IDs exist in DB
    - Verify language pair: all have `language="en"`, `user_language="vi"`
    - Verify all prices are 49
    - Verify series membership and display orders (7 in Series 1, 6 in Series 2, 7 in Series 3)
    - Verify contentTypeTags: 7 story-reading have `["story"]`, 13 speaking/balanced have `[]`
    - Verify collection-series wiring (1 collection, 3 series, correct display orders)
    - Verify no duplicates across all 20 titles
    - _Requirements: 15.3, 15.4_

  - [x] 10.2 Resolve any issues found during verification
    - If missing curriculums: recreate affected scripts and re-run
    - If duplicates: keep earliest, remove from series, delete extras
    - If wrong display orders or prices: fix via API calls
    - _Requirements: 15.4_

- [ ] 11. Documentation and cleanup
  - [x] 11.1 Create `vi-en-christianity-curriculum/README.md` with full documentation
    - Collection ID, all 3 series IDs
    - All 20 curriculum IDs with titles, display orders, vocabulary lists, skill focus assignments, tone assignments (description and farewell), pricing
    - SQL verification queries for future reference
    - Recreation context and method
    - _Requirements: 14.1_

  - [x] 11.2 Delete all creation scripts after verification
    - Delete all 20 `create_*.py` scripts and `orchestrator.py` from `vi-en-christianity-curriculum/`
    - Only `README.md` and `validate_content.py` remain in the directory
    - _Requirements: 14.2_

  - [x] 11.3 Run final duplicate check and resolve
    - Run duplicate check query for each of the 20 curriculum titles
    - If duplicates found: keep earliest, remove from series first, then delete extras
    - _Requirements: 14.3_

- [x] 12. Final checkpoint — All tasks complete
  - Verify 20 new curriculums total: 7 story-reading + 6 speaking + 7 balanced
  - Verify collection and series structure is correct (1 collection, 3 series, 20 curriculums)
  - Verify README.md is complete and all creation scripts are deleted
  - Verify no `setPublic` calls were made (all curriculums remain private)
  - Verify validator file remains at `vi-en-christianity-curriculum/validate_content.py`
  - Ensure all tests pass, ask the user if questions arise.

## Notes

- Collection: "Kitô Giáo & Đức Tin" (Christianity & Faith)
- Series 1: "Đọc Truyện Kinh Thánh" (Bible Story Reading) — 7 story-reading curriculums, series tone: vivid_scenario
- Series 2: "Luyện Nói Về Đức Tin" (Speaking About Faith) — 6 speaking curriculums, series tone: empathetic_observation
- Series 3: "Kỹ Năng Toàn Diện" (Comprehensive Skills) — 7 balanced curriculums, series tone: bold_declaration
- Root-level `api_helpers.py` is reused as-is — no changes needed
- All curriculum content must be hand-crafted — no template-based generation for learner-facing text
- Vietnamese session titles: "Phần 1", "Phần 2", "Ôn tập", "Đọc tổng hợp" (or similar per format)
- All marketing text (title, description, preview) in Vietnamese
- introAudio scripts: bilingual (Vietnamese explanations for English vocabulary)
- Reading passages: entirely in English
- vocabList: English words in lowercase
- Vocabulary overlap: max 2 shared words between any two curriculums (verified in design)
- Tone assignments pre-planned in design document — no adjacent duplicates, no tone >30%
- Description tone distribution: provocative_question (4), bold_declaration (4), vivid_scenario (3), empathetic_observation (3), surprising_fact (3), metaphor_led (3)
- Farewell tone distribution: introspective_guide (4), warm_accountability (4), team_building_energy (4), quiet_awe (4), practical_momentum (4)
- Writing activities only in sessions 3 and 4
- All curriculums private by default — no setPublic calls
- Tasks marked with `*` are optional and can be skipped for faster MVP
- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation
- Property tests validate universal correctness properties from the design document
