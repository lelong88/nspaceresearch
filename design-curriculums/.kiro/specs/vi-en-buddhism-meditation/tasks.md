# Implementation Plan: Vietnamese-English Buddhism & Meditation Curriculums

## Overview

Create 20 English-learning curriculums for Vietnamese speakers on Buddhism, meditation, and mindfulness. Scripts go in `vi-en-buddhism-meditation/`. Reuses root-level `api_helpers.py`.

Three formats: story_reading (contentTypeTags: ["story"], 7 curriculums), speaking (contentTypeTags: [], 6 curriculums), balanced (contentTypeTags: [], 7 curriculums). All curriculums: 4 sessions, 10-12 vocab words, price 49. Language pair: userLanguage="vi", language="en".

Execution order: (1) create validator + PBT tests, (2) run orchestrator to create collection + 3 series, (3) story-reading scripts x7, (4) speaking scripts x6, (5) balanced scripts x7, (6) verification queries, (7) documentation + cleanup.

## Tasks

- [x] 1. Create content validator with property-based tests
  - [x] 1.1 Create `vi-en-buddhism-meditation/validate_content.py` with format-aware `validate(content, format)` function
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
    - Create `vi-en-buddhism-meditation/test_validate_content.py` using Hypothesis library
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

- [x] 2. Create orchestrator script
  - [x] 2.1 Create `vi-en-buddhism-meditation/orchestrator.py`
    - Create 1 collection: "Phật Giáo, Thiền Định & Chánh Niệm" with neutral informative Vietnamese description
    - Create 3 series:
      - Series 1: "Đọc Truyện Phật Giáo" (story-reading, 7 curriculums) — description tone: `vivid_scenario`, ≤255 chars
      - Series 2: "Luyện Nói Về Thiền & Chánh Niệm" (speaking, 6 curriculums) — description tone: `empathetic_observation`, ≤255 chars
      - Series 3: "Kỹ Năng Toàn Diện" (balanced, 7 curriculums) — description tone: `bold_declaration`, ≤255 chars
    - Wire all 3 series to the collection via `add_series_to_collection`
    - Set series display orders: Series 1 = 1, Series 2 = 2, Series 3 = 3
    - Print collection_id and all 3 series_ids for use in curriculum scripts
    - Uses root-level `api_helpers.py` (create_collection, create_series, add_series_to_collection, set_series_display_order)
    - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5, 8.7, 11.2, 11.3, 11.4, 11.5_

- [x] 3. Checkpoint — Run orchestrator and verify infrastructure
  - Run `python orchestrator.py` in `vi-en-buddhism-meditation/`
  - Verify collection and 3 series exist in DB
  - Record collection_id and series_ids for curriculum scripts
  - Ensure all tests pass, ask the user if questions arise.

- [x] 4. Create story-reading curriculum scripts (7 scripts, Series 1: "Đọc Truyện Phật Giáo")
  - [x] 4.1 Create `vi-en-buddhism-meditation/create_con_duong_giac_ngo.py` — "Con Đường Giác Ngộ"
    - Story-reading format: 4 sessions, 10 words, price 49, contentTypeTags: ["story"]
    - Level: preintermediate
    - vocabList: ["enlightenment", "renounce", "suffering", "meditation", "awakening", "compassion", "path", "wisdom", "serenity", "liberation"]
    - Activity sequence per story_reading template (sessions 1-4 as defined in design)
    - Description tone: `provocative_question`, farewell tone: `introspective_guide`
    - Series 1, display order: 1
    - Narrative: The story of Siddhartha Gautama's journey from prince to Buddha
    - Validate with `validate(content, "story_reading")` before upload
    - _Requirements: 1.1, 1.2, 1.4, 1.6, 1.7, 2.1, 3.1, 3.4, 4.1, 4.4, 4.5, 4.6, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.4, 6.5, 6.6, 7.1, 9.1-9.8, 10.1-10.11, 11.1, 11.6, 11.7, 12.1, 13.1-13.4, 16.1, 16.4_

  - [x] 4.2 Create `vi-en-buddhism-meditation/create_ngoi_chua_trong_suong.py` — "Ngôi Chùa Trong Sương"
    - Story-reading format: 4 sessions, 10 words, price 49, contentTypeTags: ["story"]
    - Level: preintermediate
    - vocabList: ["temple", "incense", "chant", "monk", "prayer", "bell", "offering", "devotion", "silence", "ritual"]
    - Description tone: `vivid_scenario`, farewell tone: `warm_accountability`
    - Series 1, display order: 2
    - Narrative: Daily life in a Vietnamese Buddhist temple at dawn
    - _Requirements: same as 4.1_

  - [x] 4.3 Create `vi-en-buddhism-meditation/create_nhung_bai_hoc_tu_hoa_sen.py` — "Những Bài Học Từ Hoa Sen"
    - Story-reading format: 4 sessions, 10 words, price 49, contentTypeTags: ["story"]
    - Level: preintermediate
    - vocabList: ["lotus", "bloom", "mud", "purity", "patience", "growth", "resilience", "beauty", "emerge", "transform"]
    - Description tone: `empathetic_observation`, farewell tone: `quiet_awe`
    - Series 1, display order: 3
    - Narrative: Buddhist moral stories using the lotus flower as metaphor
    - _Requirements: same as 4.1_

  - [x] 4.4 Create `vi-en-buddhism-meditation/create_cau_chuyen_thien_su.py` — "Câu Chuyện Thiền Sư"
    - Story-reading format: 4 sessions, 12 words, price 49, contentTypeTags: ["story"]
    - Level: intermediate
    - vocabList: ["parable", "disciple", "insight", "paradox", "detachment", "mindful", "stillness", "impermanence", "awareness", "transcend", "koan", "contemplation"]
    - Description tone: `bold_declaration`, farewell tone: `team_building_energy`
    - Series 1, display order: 4
    - Narrative: Stories of famous Zen masters and their teachings through parables
    - _Requirements: same as 4.1 (with 1.2 intermediate level)_

  - [x] 4.5 Create `vi-en-buddhism-meditation/create_hanh_trinh_chanh_niem.py` — "Hành Trình Chánh Niệm"
    - Story-reading format: 4 sessions, 12 words, price 49, contentTypeTags: ["story"]
    - Level: intermediate
    - vocabList: ["mindfulness", "breath", "anchor", "present", "observe", "acceptance", "wandering", "intention", "clarity", "equanimity", "cultivate", "surrender"]
    - Description tone: `surprising_fact`, farewell tone: `practical_momentum`
    - Series 1, display order: 5
    - Narrative: A first-person narrative of someone discovering mindfulness practice
    - _Requirements: same as 4.4_

  - [x] 4.6 Create `vi-en-buddhism-meditation/create_mua_an_cu.py` — "Mùa An Cư"
    - Story-reading format: 4 sessions, 12 words, price 49, contentTypeTags: ["story"]
    - Level: intermediate
    - vocabList: ["retreat", "discipline", "solitude", "reflection", "vow", "perseverance", "community", "harmony", "simplicity", "gratitude", "renewal", "dedication"]
    - Description tone: `metaphor_led`, farewell tone: `introspective_guide`
    - Series 1, display order: 6
    - Narrative: The Buddhist rain retreat season and monks' intensive practice
    - _Requirements: same as 4.4_

  - [x] 4.7 Create `vi-en-buddhism-meditation/create_anh_sang_tu_bi.py` — "Ánh Sáng Từ Bi"
    - Story-reading format: 4 sessions, 12 words, price 49, contentTypeTags: ["story"]
    - Level: intermediate
    - vocabList: ["compassion", "empathy", "forgiveness", "generosity", "kindness", "selfless", "benevolence", "reconciliation", "altruism", "unconditional", "embrace", "nurture"]
    - Description tone: `provocative_question`, farewell tone: `warm_accountability`
    - Series 1, display order: 7
    - Narrative: Stories illustrating the Buddhist concept of loving-kindness (metta)
    - _Requirements: same as 4.4_

- [x] 5. Checkpoint — Run story-reading scripts and verify
  - Run all 7 story-reading scripts in order (display order 1-7)
  - Verify 7 curriculums exist in Series 1 with correct display orders
  - Verify prices: all 7 at price 49
  - Verify language pair: all have `language="en"`, `userLanguage="vi"`
  - Verify contentTypeTags: all 7 have `["story"]`
  - Run duplicate check for all 7 titles
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 6. Create speaking curriculum scripts (6 scripts, Series 2: "Luyện Nói Về Thiền & Chánh Niệm")
  - [x] 6.1 Create `vi-en-buddhism-meditation/create_thien_cho_nguoi_moi.py` — "Thiền Cho Người Mới"
    - Speaking format: 4 sessions, 10 words, price 49, contentTypeTags: []
    - Level: preintermediate
    - vocabList: ["breathe", "focus", "relax", "posture", "inhale", "exhale", "calm", "gentle", "steady", "release"]
    - Activity sequence per speaking template (sessions 1-4 as defined in design)
    - Description tone: `bold_declaration`, farewell tone: `quiet_awe`
    - Series 2, display order: 1
    - Topic: Practical meditation vocabulary for beginners
    - Validate with `validate(content, "speaking")` before upload
    - _Requirements: 1.1, 1.2, 1.5, 1.6, 1.7, 2.1, 3.2, 3.4, 4.2, 4.4, 4.5, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.4, 6.5, 6.6, 7.1, 9.1-9.8, 10.1-10.11, 11.1, 11.6, 11.7, 12.1, 13.1-13.4, 16.1, 16.4_

  - [x] 6.2 Create `vi-en-buddhism-meditation/create_noi_ve_chanh_niem.py` — "Nói Về Chánh Niệm"
    - Speaking format: 4 sessions, 10 words, price 49, contentTypeTags: []
    - Level: preintermediate
    - vocabList: ["awareness", "moment", "attention", "distraction", "grounding", "sensation", "acknowledge", "respond", "pause", "balance"]
    - Description tone: `vivid_scenario`, farewell tone: `team_building_energy`
    - Series 2, display order: 2
    - Topic: Conversational phrases for discussing mindfulness in English
    - _Requirements: same as 6.1_

  - [x] 6.3 Create `vi-en-buddhism-meditation/create_tai_khoa_tu.py` — "Tại Khóa Tu"
    - Speaking format: 4 sessions, 10 words, price 49, contentTypeTags: []
    - Level: preintermediate
    - vocabList: ["schedule", "session", "instructor", "guidance", "practice", "technique", "beginner", "intermediate", "silent", "mindful"]
    - Description tone: `surprising_fact`, farewell tone: `practical_momentum`
    - Series 2, display order: 3
    - Topic: Vocabulary for participating in an English-language meditation retreat
    - _Requirements: same as 6.1_

  - [x] 6.4 Create `vi-en-buddhism-meditation/create_doi_thoai_ve_phat_giao.py` — "Đối Thoại Về Phật Giáo"
    - Speaking format: 4 sessions, 12 words, price 49, contentTypeTags: []
    - Level: intermediate
    - vocabList: ["philosophy", "reincarnation", "karma", "nirvana", "dharma", "sangha", "enlighten", "meditate", "spiritual", "doctrine", "scripture", "monastery"]
    - Description tone: `empathetic_observation`, farewell tone: `introspective_guide`
    - Series 2, display order: 4
    - Topic: Vocabulary for discussing Buddhist concepts in English conversations
    - _Requirements: same as 6.1 (with 1.2 intermediate level)_

  - [x] 6.5 Create `vi-en-buddhism-meditation/create_chia_se_trai_nghiem_thien.py` — "Chia Sẻ Trải Nghiệm Thiền"
    - Speaking format: 4 sessions, 12 words, price 49, contentTypeTags: []
    - Level: intermediate
    - vocabList: ["profound", "transformative", "peaceful", "restless", "breakthrough", "struggle", "consistent", "progress", "insight", "revelation", "surrender", "blissful"]
    - Description tone: `metaphor_led`, farewell tone: `warm_accountability`
    - Series 2, display order: 5
    - Topic: Expressing personal meditation experiences in English
    - _Requirements: same as 6.4_

  - [x] 6.6 Create `vi-en-buddhism-meditation/create_phat_giao_va_doi_song.py` — "Phật Giáo Và Đời Sống Hiện Đại"
    - Speaking format: 4 sessions, 12 words, price 49, contentTypeTags: []
    - Level: intermediate
    - vocabList: ["integrate", "contemporary", "stress", "anxiety", "therapeutic", "holistic", "secular", "wellness", "resilience", "sustainable", "intentional", "flourish"]
    - Description tone: `provocative_question`, farewell tone: `quiet_awe`
    - Series 2, display order: 6
    - Topic: Discussing how Buddhism applies to modern life in English
    - _Requirements: same as 6.4_

- [ ] 7. Checkpoint — Run speaking scripts and verify
  - Run all 6 speaking scripts in order (display order 1-6)
  - Verify 6 curriculums exist in Series 2 with correct display orders
  - Verify prices: all 6 at price 49
  - Verify language pair: all have `language="en"`, `userLanguage="vi"`
  - Verify contentTypeTags: all 6 have `[]`
  - Run duplicate check for all 6 titles
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 8. Create balanced curriculum scripts (7 scripts, Series 3: "Kỹ Năng Toàn Diện")
  - [x] 8.1 Create `vi-en-buddhism-meditation/create_bat_chanh_dao.py` — "Bát Chánh Đạo"
    - Balanced format: 4 sessions, 10 words, price 49, contentTypeTags: []
    - Level: preintermediate
    - vocabList: ["righteous", "speech", "action", "livelihood", "effort", "concentration", "understanding", "intention", "ethical", "conduct"]
    - Activity sequence per balanced template (sessions 1-4 as defined in design)
    - Description tone: `bold_declaration`, farewell tone: `team_building_energy`
    - Series 3, display order: 1
    - Topic: The Noble Eightfold Path explained through vocabulary and practice
    - Validate with `validate(content, "balanced")` before upload
    - _Requirements: 1.1, 1.2, 1.5, 1.6, 1.7, 2.1, 3.3, 3.4, 4.3, 4.4, 4.5, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.4, 6.5, 6.6, 7.1, 9.1-9.8, 10.1-10.11, 11.1, 11.6, 11.7, 12.1, 13.1-13.4, 16.1, 16.2, 16.3, 16.4_

  - [x] 8.2 Create `vi-en-buddhism-meditation/create_thien_dinh_moi_ngay.py` — "Thiền Định Mỗi Ngày"
    - Balanced format: 4 sessions, 10 words, price 49, contentTypeTags: []
    - Level: preintermediate
    - vocabList: ["routine", "habit", "morning", "evening", "duration", "timer", "cushion", "comfortable", "consistent", "benefit"]
    - Description tone: `empathetic_observation`, farewell tone: `practical_momentum`
    - Series 3, display order: 2
    - Topic: Daily meditation practice vocabulary and routines
    - _Requirements: same as 8.1_

  - [x] 8.3 Create `vi-en-buddhism-meditation/create_chanh_niem_trong_an_uong.py` — "Chánh Niệm Trong Ăn Uống"
    - Balanced format: 4 sessions, 10 words, price 49, contentTypeTags: []
    - Level: preintermediate
    - vocabList: ["savor", "texture", "aroma", "gratitude", "nourish", "chew", "appreciate", "portion", "mindful", "conscious"]
    - Description tone: `vivid_scenario`, farewell tone: `introspective_guide`
    - Series 3, display order: 3
    - Topic: Mindful eating vocabulary and practices
    - _Requirements: same as 8.1_

  - [x] 8.4 Create `vi-en-buddhism-meditation/create_khong_gian_thien.py` — "Không Gian Thiền"
    - Balanced format: 4 sessions, 10 words, price 49, contentTypeTags: []
    - Level: preintermediate
    - vocabList: ["sanctuary", "candle", "cushion", "altar", "tranquil", "atmosphere", "minimal", "natural", "sacred", "arrange"]
    - Description tone: `surprising_fact`, farewell tone: `warm_accountability`
    - Series 3, display order: 4
    - Topic: Vocabulary for creating and describing meditation spaces
    - _Requirements: same as 8.1_

  - [x] 8.5 Create `vi-en-buddhism-meditation/create_tu_dieu_de.py` — "Tứ Diệu Đế"
    - Balanced format: 4 sessions, 12 words, price 49, contentTypeTags: []
    - Level: intermediate
    - vocabList: ["truth", "suffering", "origin", "cessation", "noble", "craving", "attachment", "liberation", "diagnosis", "prescription", "remedy", "realization"]
    - Description tone: `metaphor_led`, farewell tone: `quiet_awe`
    - Series 3, display order: 5
    - Topic: The Four Noble Truths explored through reading, speaking, and writing
    - _Requirements: same as 8.1 (with 1.2 intermediate level)_

  - [x] 8.6 Create `vi-en-buddhism-meditation/create_thien_hanh.py` — "Thiền Hành"
    - Balanced format: 4 sessions, 12 words, price 49, contentTypeTags: []
    - Level: intermediate
    - vocabList: ["stride", "pace", "deliberate", "sensation", "grounding", "rhythm", "awareness", "surroundings", "footstep", "synchronize", "embodiment", "presence"]
    - Description tone: `provocative_question`, farewell tone: `team_building_energy`
    - Series 3, display order: 6
    - Topic: Walking meditation vocabulary and the art of mindful movement
    - _Requirements: same as 8.5_

  - [x] 8.7 Create `vi-en-buddhism-meditation/create_tam_tu_va_thien_tam_tu.py` — "Tâm Từ Và Thiền Tâm Từ"
    - Balanced format: 4 sessions, 12 words, price 49, contentTypeTags: []
    - Level: intermediate
    - vocabList: ["radiate", "wellbeing", "boundless", "extend", "recipient", "phrase", "visualize", "warmth", "genuine", "universal", "infinite", "intention"]
    - Description tone: `bold_declaration`, farewell tone: `practical_momentum`
    - Series 3, display order: 7
    - Topic: Loving-kindness meditation (metta) practice and vocabulary
    - _Requirements: same as 8.5_

- [ ] 9. Checkpoint — Run balanced scripts and verify
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
  - [x] 11.1 Create `vi-en-buddhism-meditation/README.md` with full documentation
    - Collection ID, all 3 series IDs
    - All 20 curriculum IDs with titles, display orders, vocabulary lists, skill focus assignments, tone assignments (description and farewell), pricing
    - SQL verification queries for future reference
    - Recreation context and method
    - _Requirements: 14.1_

  - [x] 11.2 Delete all creation scripts after verification
    - Delete all 20 `create_*.py` scripts and `orchestrator.py` from `vi-en-buddhism-meditation/`
    - Only `README.md` and `validate_content.py` remain in the directory
    - _Requirements: 14.2_

  - [x] 11.3 Run final duplicate check and resolve
    - Run duplicate check query for each of the 20 curriculum titles
    - If duplicates found: keep earliest, remove from series first, then delete extras
    - _Requirements: 14.3_

- [ ] 12. Final checkpoint — All tasks complete
  - Verify 20 new curriculums total: 7 story-reading + 6 speaking + 7 balanced
  - Verify collection and series structure is correct (1 collection, 3 series, 20 curriculums)
  - Verify README.md is complete and all creation scripts are deleted
  - Verify no `setPublic` calls were made (all curriculums remain private)
  - Verify validator file remains at `vi-en-buddhism-meditation/validate_content.py`
  - Ensure all tests pass, ask the user if questions arise.

## Notes

- Collection: "Phật Giáo, Thiền Định & Chánh Niệm" (Buddhism, Meditation & Mindfulness)
- Series 1: "Đọc Truyện Phật Giáo" (Buddhist Story Reading) — 7 story-reading curriculums, series tone: vivid_scenario
- Series 2: "Luyện Nói Về Thiền & Chánh Niệm" (Speaking About Meditation & Mindfulness) — 6 speaking curriculums, series tone: empathetic_observation
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
