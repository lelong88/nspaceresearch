# Implementation Plan: Vietnamese-English Children's Curriculum

## Overview

Create 10 English-learning curriculums for Vietnamese children aged 6-10, organized into 1 collection ("Tiếng Anh Cho Bé 6-10 Tuổi") and 2 series ("Bước Đầu Tiên" with 6 beginner curriculums, "Khám Phá Thêm" with 4 preintermediate curriculums).

Implementation uses Python scripts in `vi-en-children-curriculum/`. Language pair: `userLanguage="vi"`, `language="en"`. Three curriculum formats: beginner_mini (1 session, 3-5 words, price 9), beginner_short (4 sessions, 8-10 words, price 19), preintermediate_short (4 sessions, 10-12 words, price 49). Each curriculum gets its own standalone script with hand-crafted child-friendly content. A children-specific `validate_content.py` enforces format rules before upload. The shared root-level `api_helpers.py` handles all API calls.

Execution order: (1) content validator + tests, (2) orchestrator for collection/series, (3) beginner mini scripts ×3, (4) beginner short scripts ×3, (5) preintermediate short scripts ×4, (6) README + cleanup.

## Tasks

- [x] 1. Create children-specific content validator
  - [x] 1.1 Create `vi-en-children-curriculum/validate_content.py` with format-aware `validate(content, format)` function
    - `format` parameter: `"beginner_mini"`, `"beginner_short"`, or `"preintermediate_short"`
    - Format-specific checks: session count (1 for mini, 4 for short/preintermediate), vocab count range (3-5 for mini, 8-10 for beginner_short, 10-12 for preintermediate_short)
    - Forbidden activities: `writingParagraph` and `vocabLevel3` forbidden in ALL children's formats; `vocabLevel1` and `vocabLevel2` additionally forbidden in `beginner_mini`
    - Shared checks: top-level structure (title, description, preview.text, contentTypeTags, learningSessions), session structure (title, non-empty activities), activity structure (activityType not type, valid values, title, description, data as dict), vocabList format (array of lowercase strings, field name vocabList not words), flashcard consistency (viewFlashcards/speakFlashcards identical vocabList in same session), writingSentence structure (data.vocabList, data.items with prompt and targetVocab), strip-keys exclusion (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId)
    - Raise `ValueError` with specific violation message identifying the rule, location (session/activity index), and expected vs actual value
    - _Requirements: 1.3, 1.4, 1.5, 1.6, 1.7, 3.4, 3.5, 3.6, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 10.9, 10.10_

  - [x] 1.2 Write property test: Valid content passes validation (Property 1)
    - **Property 1: Valid content passes validation**
    - Use `hypothesis` to generate well-formed curriculum content dicts matching each of the 3 formats (correct session count, vocab count within range, all required fields, no forbidden activities, no strip keys) and verify `validate(content, format)` returns without exception
    - **Validates: Requirements 1.3, 1.4, 1.5, 10.1, 10.2, 10.3, 10.4**

  - [x] 1.3 Write property test: Forbidden activities rejected per format (Property 2)
    - **Property 2: Forbidden activities are rejected per format**
    - Use `hypothesis` to inject `writingParagraph` or `vocabLevel3` into any children's curriculum and verify rejection; additionally inject `vocabLevel1`/`vocabLevel2` into `beginner_mini` format and verify rejection
    - **Validates: Requirements 3.4, 3.5, 3.6, 10.9**

  - [x] 1.4 Write property test: Strip keys rejected anywhere in JSON tree (Property 3)
    - **Property 3: Strip keys are rejected anywhere in the JSON tree**
    - Use `hypothesis` to inject strip keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId) at random depths in curriculum JSON and verify rejection with message mentioning the strip key
    - **Validates: Requirements 1.7, 10.8**

  - [x] 1.5 Write property test: Activities missing required fields rejected (Property 4)
    - **Property 4: Activities missing required fields are rejected**
    - Use `hypothesis` to generate activities missing `activityType`, `title`, `description`, or `data`, or with `data` not being a dict, and verify rejection identifying the missing field
    - **Validates: Requirements 9.1, 9.5, 10.3**

  - [x] 1.6 Write property test: Invalid activityType values rejected (Property 5)
    - **Property 5: Invalid activityType values are rejected**
    - Use `hypothesis` to generate activities with `activityType` values not in the valid set (introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence) and verify rejection
    - **Validates: Requirements 9.2, 10.4**

  - [x] 1.7 Write property test: vocabList format enforced (Property 6)
    - **Property 6: vocabList format is enforced**
    - Use `hypothesis` to generate vocab activities with non-lowercase strings, non-array vocabList, empty vocabList, or field name `words` instead of `vocabList`, and verify rejection
    - **Validates: Requirements 9.3, 10.5**

  - [x] 1.8 Write property test: Flashcard vocabList consistency (Property 7)
    - **Property 7: Flashcard vocabList consistency within sessions**
    - Use `hypothesis` to generate sessions with mismatched viewFlashcards/speakFlashcards vocabList arrays and verify rejection
    - **Validates: Requirements 9.4, 10.6**

  - [x] 1.9 Write property test: writingSentence structure enforced (Property 8)
    - **Property 8: writingSentence structure is enforced**
    - Use `hypothesis` to generate writingSentence activities with missing data.vocabList, missing/empty data.items, or items lacking prompt/targetVocab, and verify rejection
    - **Validates: Requirements 9.6, 10.7**

- [x] 2. Checkpoint — Content validator ready
  - Ensure all tests pass, ask the user if questions arise.

- [x] 3. Create orchestrator and collection/series infrastructure
  - [x] 3.1 Create `vi-en-children-curriculum/orchestrator.py`
    - Create 1 collection: "Tiếng Anh Cho Bé 6-10 Tuổi" with neutral informative Vietnamese description
    - Create 2 series: "Bước Đầu Tiên" (description tone: `bold_declaration`, ≤255 chars) and "Khám Phá Thêm" (description tone: `vivid_scenario`, ≤255 chars)
    - Wire both series to the collection via `add_series_to_collection`
    - Set display orders for both series via `set_series_display_order`
    - Hard-code the tone assignment table from the design (all 10 curriculum description tones and farewell tones) and print it for reference
    - Log collection ID and both series IDs to stdout
    - Uses root-level `api_helpers.py` via sys.path: `create_collection`, `create_series`, `add_series_to_collection`, `set_series_display_order`
    - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 11.2, 11.3, 11.4, 11.5, 15.1_

- [x] 4. Create beginner mini curriculum scripts (3 scripts, Series 1: "Bước Đầu Tiên")
  - [x] 4.1 Create `vi-en-children-curriculum/create_colors.py` — "Thế Giới Màu Sắc"
    - Beginner mini format: 1 session, 5 words (red, blue, green, yellow, orange), price 9
    - Activity sequence: introAudio (welcome, 200-350 words, warm playful tone teaching all 5 words) → viewFlashcards → speakFlashcards → reading (40-60 words, simple sentences about colors) → speakReading → readAlong → introAudio (farewell, 200-400 words, vocab review with praise)
    - Description tone: `provocative_question` (Parent_Copy addressing parental aspirations about early English)
    - Farewell tone: `warm_accountability` (gentle encouragement to practice colors with family)
    - Preview: ~100-150 words Vietnamese Parent_Copy with vivid hooks
    - All text hand-crafted, no templates. Vietnamese marketing text for parents, bilingual child content
    - Validate with `validate(content, "beginner_mini")` before upload
    - Display order: 1 in series
    - _Requirements: 1.1, 1.3, 2.1, 3.1, 3.2, 3.4, 3.5, 3.6, 4.1, 5.1, 5.2, 5.3, 5.4, 5.7, 6.1, 6.4, 6.5, 6.6, 6.7, 7.1, 9.1, 9.2, 9.3, 9.4, 9.7, 11.1, 11.6, 12.1, 13.1, 13.2, 13.3, 13.4_

  - [x] 4.2 Create `vi-en-children-curriculum/create_pets.py` — "Bạn Thú Cưng"
    - Beginner mini format: 1 session, 5 words (dog, cat, fish, bird, rabbit), price 9
    - Same activity sequence as 4.1 but all content hand-crafted for pets topic
    - Description tone: `vivid_scenario`, farewell tone: `quiet_awe`
    - Display order: 2 in series
    - _Requirements: 1.1, 1.3, 2.1, 3.1, 3.2, 3.4, 3.5, 3.6, 4.1, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.4, 6.5, 6.6, 6.7, 6.8, 7.1, 9.1, 9.2, 9.3, 9.4, 9.7, 11.1, 11.6, 12.1, 13.1, 13.2, 13.3, 13.4_

  - [x] 4.3 Create `vi-en-children-curriculum/create_toys.py` — "Đồ Chơi Của Em"
    - Beginner mini format: 1 session, 5 words (ball, doll, car, kite, puzzle), price 9
    - Same activity sequence as 4.1 but all content hand-crafted for toys topic
    - Description tone: `empathetic_observation`, farewell tone: `practical_momentum`
    - Display order: 3 in series
    - _Requirements: 1.1, 1.3, 2.1, 3.1, 3.2, 3.4, 3.5, 3.6, 4.1, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.4, 6.5, 6.6, 6.7, 6.8, 7.1, 9.1, 9.2, 9.3, 9.4, 9.7, 11.1, 11.6, 12.1, 13.1, 13.2, 13.3, 13.4_

- [x] 5. Create beginner short curriculum scripts (3 scripts, Series 1: "Bước Đầu Tiên")
  - [x] 5.1 Create `vi-en-children-curriculum/create_playground.py` — "Sân Chơi Vui Nhộn"
    - Beginner short format: 4 sessions, 10 words (swing, slide, climb, jump, run, sand, friend, play, turn, share), price 19
    - Session 1: introAudio (welcome + teach group 1) → viewFlashcards (group 1) → speakFlashcards (group 1) → vocabLevel1 (group 1) → reading (60-80 words) → readAlong → introAudio (wrap-up)
    - Session 2: introAudio (recap group 1 + teach group 2) → viewFlashcards (group 2) → speakFlashcards (group 2) → vocabLevel1 (group 2) → reading (60-80 words) → readAlong → introAudio (wrap-up)
    - Session 3 (Review): introAudio → viewFlashcards (all) → speakFlashcards (all) → vocabLevel1 (all) → vocabLevel2 (all) → writingSentence (3-4 items with Vietnamese prompts, example sentences, substitution pattern) → introAudio (wrap-up)
    - Session 4 (Final): introAudio → reading (100-120 words) → speakReading → readAlong → writingSentence (2-3 items) → introAudio (farewell with full vocab review and celebration)
    - Description tone: `surprising_fact`, farewell tone: `introspective_guide`
    - All text hand-crafted. writingSentence prompts: simple Vietnamese instructions, complete English example sentence, 1-word substitution pattern
    - Display order: 4 in series
    - _Requirements: 1.1, 1.4, 2.1, 2.4, 3.1, 3.2, 3.3, 3.4, 3.5, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 7.2, 9.1, 9.2, 9.3, 9.4, 9.6, 9.7, 11.1, 11.6, 12.1, 13.1, 13.2, 13.3, 13.4_

  - [x] 5.2 Create `vi-en-children-curriculum/create_zoo.py` — "Vườn Thú Kỳ Diệu"
    - Beginner short format: 4 sessions, 10 words (elephant, monkey, lion, giraffe, tiger, bear, penguin, snake, zebra, parrot), price 19
    - Same 4-session structure as 5.1 but all content hand-crafted for zoo topic
    - Description tone: `metaphor_led`, farewell tone: `team_building_energy`
    - Display order: 5 in series
    - _Requirements: 1.1, 1.4, 2.1, 2.4, 3.1, 3.2, 3.3, 3.4, 3.5, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 7.2, 9.1, 9.2, 9.3, 9.4, 9.6, 9.7, 11.1, 11.6, 12.1, 13.1, 13.2, 13.3, 13.4_

  - [x] 5.3 Create `vi-en-children-curriculum/create_school.py` — "Một Ngày Ở Trường"
    - Beginner short format: 4 sessions, 10 words (teacher, student, book, pencil, desk, lunch, recess, homework, classroom, backpack), price 19
    - Same 4-session structure as 5.1 but all content hand-crafted for school topic
    - Description tone: `bold_declaration`, farewell tone: `warm_accountability`
    - Display order: 6 in series
    - _Requirements: 1.1, 1.4, 2.1, 2.4, 3.1, 3.2, 3.3, 3.4, 3.5, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 7.2, 9.1, 9.2, 9.3, 9.4, 9.6, 9.7, 11.1, 11.6, 12.1, 13.1, 13.2, 13.3, 13.4_

- [x] 6. Checkpoint — All beginner curriculums created
  - Ensure all tests pass, ask the user if questions arise.
  - Verify 6 curriculums exist in Series 1 with correct display orders 1-6
  - Verify prices: 3 mini at 9, 3 short at 19

- [x] 7. Create preintermediate short curriculum scripts (4 scripts, Series 2: "Khám Phá Thêm")
  - [x] 7.1 Create `vi-en-children-curriculum/create_nature.py` — "Khám Phá Thiên Nhiên"
    - Preintermediate short format: 4 sessions, 12 words (forest, river, mountain, butterfly, flower, leaf, rainbow, cloud, sunshine, rain, nest, seed), price 49
    - Session 1: introAudio (welcome + teach group 1) → viewFlashcards (group 1) → speakFlashcards (group 1) → vocabLevel1 (group 1) → vocabLevel2 (group 1) → reading (80-100 words) → speakReading → readAlong → introAudio (wrap-up)
    - Session 2: introAudio (recap group 1 + teach group 2) → viewFlashcards (group 2) → speakFlashcards (group 2) → vocabLevel1 (group 2) → vocabLevel2 (group 2) → reading (80-100 words) → speakReading → readAlong → introAudio (wrap-up)
    - Session 3 (Review): introAudio → viewFlashcards (all) → speakFlashcards (all) → vocabLevel1 (all) → vocabLevel2 (all) → writingSentence (4-5 items) → introAudio (wrap-up)
    - Session 4 (Final): introAudio → reading (150-180 words) → speakReading → readAlong → writingSentence (3-4 items) → introAudio (farewell with full vocab review and celebration)
    - Description tone: `empathetic_observation`, farewell tone: `quiet_awe`
    - All text hand-crafted. Vietnamese Parent_Copy for parents, bilingual child content
    - Validate with `validate(content, "preintermediate_short")` before upload
    - Display order: 1 in series
    - _Requirements: 1.1, 1.5, 2.1, 2.4, 3.1, 3.2, 3.3, 3.4, 3.5, 4.3, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 7.3, 9.1, 9.2, 9.3, 9.4, 9.6, 9.7, 11.1, 11.6, 12.1, 13.1, 13.2, 13.3, 13.4_

  - [x] 7.2 Create `vi-en-children-curriculum/create_family.py` — "Gia Đình Vui Vẻ"
    - Preintermediate short format: 4 sessions, 12 words (breakfast, dinner, weekend, picnic, garden, bicycle, story, bedtime, together, celebrate, grandparent, cousin), price 49
    - Same 4-session structure as 7.1 but all content hand-crafted for family topic
    - Description tone: `provocative_question`, farewell tone: `practical_momentum`
    - Display order: 2 in series
    - _Requirements: 1.1, 1.5, 2.1, 2.4, 3.1, 3.2, 3.3, 3.4, 3.5, 4.3, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 7.3, 9.1, 9.2, 9.3, 9.4, 9.6, 9.7, 11.1, 11.6, 12.1, 13.1, 13.2, 13.3, 13.4_

  - [x] 7.3 Create `vi-en-children-curriculum/create_superheroes.py` — "Siêu Anh Hùng Nhí"
    - Preintermediate short format: 4 sessions, 12 words (brave, kind, strong, help, rescue, protect, team, power, dream, believe, adventure, hero), price 49
    - Same 4-session structure as 7.1 but all content hand-crafted for superheroes topic
    - Description tone: `bold_declaration`, farewell tone: `introspective_guide`
    - Display order: 3 in series
    - _Requirements: 1.1, 1.5, 2.1, 2.4, 3.1, 3.2, 3.3, 3.4, 3.5, 4.3, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 7.3, 9.1, 9.2, 9.3, 9.4, 9.6, 9.7, 11.1, 11.6, 12.1, 13.1, 13.2, 13.3, 13.4_

  - [x] 7.4 Create `vi-en-children-curriculum/create_festivals.py` — "Lễ Hội Và Mùa"
    - Preintermediate short format: 4 sessions, 12 words (spring, summer, autumn, winter, festival, lantern, firework, gift, costume, parade, tradition, celebrate), price 49
    - Same 4-session structure as 7.1 but all content hand-crafted for festivals/seasons topic
    - Description tone: `surprising_fact`, farewell tone: `team_building_energy`
    - Display order: 4 in series
    - _Requirements: 1.1, 1.5, 2.1, 2.4, 3.1, 3.2, 3.3, 3.4, 3.5, 4.3, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 7.3, 9.1, 9.2, 9.3, 9.4, 9.6, 9.7, 11.1, 11.6, 12.1, 13.1, 13.2, 13.3, 13.4_

- [x] 8. Checkpoint — All 10 curriculums created
  - Ensure all tests pass, ask the user if questions arise.
  - Verify 6 curriculums in Series 1 ("Bước Đầu Tiên") with display orders 1-6
  - Verify 4 curriculums in Series 2 ("Khám Phá Thêm") with display orders 1-4
  - Verify prices: 3 mini at 9, 3 short at 19, 4 preintermediate at 49
  - Verify language pair: all curriculums have `language="en"`, `userLanguage="vi"`
  - Run duplicate check queries for all 10 curriculum titles

- [x] 9. Documentation and cleanup
  - [x] 9.1 Create `vi-en-children-curriculum/README.md`
    - Document: collection ID, series IDs, all 10 curriculum IDs with titles and display orders
    - Document: vocabulary lists per curriculum, tone assignments (description and farewell for all 10)
    - Document: pricing (9/19/49 per format), language pair (vi-en)
    - Include SQL verification queries: count curriculums, verify language pair, verify prices, verify series membership and display orders, verify no duplicates
    - Include recreation instructions
    - _Requirements: 14.1_

  - [x] 9.2 Delete all creation scripts after verification
    - Delete `orchestrator.py`, all 10 `create_*.py` scripts, and `validate_content.py` from `vi-en-children-curriculum/`
    - Only `README.md` remains in the directory
    - _Requirements: 14.2_

  - [x] 9.3 Run duplicate check and resolve
    - Run duplicate check query for each of the 10 curriculum titles
    - If duplicates found: keep earliest, remove from series first, then delete extras
    - _Requirements: 14.3_

- [x] 10. Final checkpoint — All tasks complete
  - Ensure all tests pass, ask the user if questions arise.
  - Verify 10 curriculums total: 3 mini + 3 short + 4 preintermediate
  - Verify collection and series structure is correct
  - Verify README.md is in place and all creation scripts are deleted
  - Verify no `setPublic` calls were made (all curriculums remain private)

## Notes

- Tasks marked with `*` are optional and can be skipped for faster MVP
- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation between phases
- Property tests validate the children-specific content validator (Properties 1-8) from the design
- The `validate_content.py` is children-specific — different from the adult validator in `en-de/` (different session counts, vocab ranges, forbidden activities)
- Root-level `api_helpers.py` is reused as-is — no changes needed
- All curriculum content must be hand-crafted — no template-based generation
- Three formats: beginner_mini (1 session, 3-5 words, price 9), beginner_short (4 sessions, 8-10 words, price 19), preintermediate_short (4 sessions, 10-12 words, price 49)
- Vietnamese session titles: "Phần 1", "Phần 2", "Ôn tập", "Đọc tổng hợp" (for short/preintermediate)
- All marketing text (title, description, preview) in Vietnamese targeting parents
- All learner-facing content (introAudio, reading, writing prompts) bilingual with warm child-friendly tone
- No vocabulary overlap across the 10 curriculums
- Tone distribution across 10 descriptions: provocative_question ×2, vivid_scenario ×1, empathetic_observation ×2, surprising_fact ×2, metaphor_led ×1, bold_declaration ×2 — max 20%, all ≤30% ✓
- No adjacent tone duplicates within either series ✓
