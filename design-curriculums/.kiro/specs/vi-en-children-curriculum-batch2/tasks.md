# Implementation Plan: Vietnamese-English Children's Curriculum — Batch 2

## Overview

Create 10 MORE English-learning curriculums for Vietnamese children aged 6-10 (Batch 2), adding to the existing collection "Tiếng Anh Cho Bé 6-10 Tuổi" (ID: `uyw1ywsg`). Adds 6 beginner curriculums to Series 1 "Bước Đầu Tiên" (ID: `8ncwoino`, display orders 7-12) and 4 preintermediate curriculums to Series 2 "Khám Phá Thêm" (ID: `l8l9bexl`, display orders 5-8).

No orchestrator needed — reuses existing collection and series. Scripts go in `vi-en-children-curriculum-batch2/`. Reuses existing `vi-en-children-curriculum/validate_content.py` (must be recreated since it was deleted after Batch 1) and root-level `api_helpers.py`.

Three formats: beginner_mini (1 session, 3-5 words, price 9), beginner_short (4 sessions, 8-10 words, price 19), preintermediate_short (4 sessions, 10-12 words, price 49). Zero vocabulary overlap with Batch 1 or between Batch 2 curriculums.

Execution order: (1) recreate validator, (2) beginner mini scripts ×3, (3) beginner short scripts ×3, (4) preintermediate short scripts ×4, (5) documentation + cleanup.

## Tasks

- [x] 1. Recreate children-specific content validator
  - [x] 1.1 Recreate `vi-en-children-curriculum/validate_content.py` with format-aware `validate(content, format)` function
    - Identical to the Batch 1 validator (recreated because it was deleted after Batch 1 execution)
    - `format` parameter: `"beginner_mini"`, `"beginner_short"`, or `"preintermediate_short"`
    - Format-specific checks: session count (1 for mini, 4 for short/preintermediate), vocab count range (3-5 for mini, 8-10 for beginner_short, 10-12 for preintermediate_short)
    - Forbidden activities: `writingParagraph` and `vocabLevel3` forbidden in ALL children's formats; `vocabLevel1` and `vocabLevel2` additionally forbidden in `beginner_mini`
    - Shared checks: top-level structure, session structure, activity structure, vocabList format, flashcard consistency, writingSentence structure, strip-keys exclusion
    - Raise `ValueError` with specific violation message identifying the rule, location, and expected vs actual value
    - _Requirements: 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 10.9, 10.10, 10.11_

- [x] 2. Checkpoint — Validator ready
  - Verify validator imports correctly from `vi-en-children-curriculum/validate_content.py`
  - Quick smoke test with a minimal valid content dict for each format

- [x] 3. Create beginner mini curriculum scripts (3 scripts, Series 1: "Bước Đầu Tiên")
  - [x] 3.1 Create `vi-en-children-curriculum-batch2/create_vehicles.py` — "Xe Cộ Quanh Em"
    - Beginner mini format: 1 session, 5 words (bus, truck, train, boat, plane), price 9
    - Activity sequence: introAudio (welcome, 200-350 words) → viewFlashcards → speakFlashcards → reading (40-60 words) → speakReading → readAlong → introAudio (farewell, 200-400 words)
    - Description tone: `vivid_scenario`, farewell tone: `quiet_awe`
    - Series ID: `8ncwoino`, display order: 7
    - Validate with `validate(content, "beginner_mini")` before upload
    - _Requirements: 1.1, 1.3, 2.1, 3.1, 3.2, 3.4, 3.5, 3.6, 4.1, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.4, 6.5, 6.6, 7.1, 8.1, 8.4, 8.6, 8.7, 9.1-9.7, 11.2, 11.3, 12.1, 12.3, 12.6, 12.9, 12.10, 13.1, 14.1-14.4, 17.1_

  - [x] 3.2 Create `vi-en-children-curriculum-batch2/create_fruits.py` — "Trái Cây Ngon Lành"
    - Beginner mini format: 1 session, 5 words (apple, banana, grape, mango, watermelon), price 9
    - Same activity sequence as 3.1 but all content hand-crafted for fruits topic
    - Description tone: `provocative_question`, farewell tone: `practical_momentum`
    - Series ID: `8ncwoino`, display order: 8
    - _Requirements: 1.1, 1.3, 2.1, 3.1, 3.2, 3.4, 3.5, 3.6, 4.1, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.4, 6.5, 6.6, 7.1, 8.1, 8.4, 8.6, 8.7, 9.1-9.7, 11.2, 11.3, 12.1, 12.3, 12.6, 12.9, 12.10, 13.1, 14.1-14.4_

  - [x] 3.3 Create `vi-en-children-curriculum-batch2/create_body_parts.py` — "Cơ Thể Của Em"
    - Beginner mini format: 1 session, 5 words (hand, foot, eye, ear, nose), price 9
    - Same activity sequence as 3.1 but all content hand-crafted for body parts topic
    - Description tone: `empathetic_observation`, farewell tone: `introspective_guide`
    - Series ID: `8ncwoino`, display order: 9
    - _Requirements: 1.1, 1.3, 2.1, 3.1, 3.2, 3.4, 3.5, 3.6, 4.1, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.4, 6.5, 6.6, 7.1, 8.1, 8.4, 8.6, 8.7, 9.1-9.7, 11.2, 11.3, 12.1, 12.3, 12.6, 12.9, 12.10, 13.1, 14.1-14.4_

- [x] 4. Create beginner short curriculum scripts (3 scripts, Series 1: "Bước Đầu Tiên")
  - [x] 4.1 Create `vi-en-children-curriculum-batch2/create_weather.py` — "Thời Tiết Hôm Nay"
    - Beginner short format: 4 sessions, 10 words (sunny, rainy, windy, hot, cold, snow, storm, foggy, warm, cool), price 19
    - Session 1: introAudio → viewFlashcards (group 1) → speakFlashcards (group 1) → vocabLevel1 (group 1) → reading (60-80 words) → readAlong → introAudio
    - Session 2: introAudio → viewFlashcards (group 2) → speakFlashcards (group 2) → vocabLevel1 (group 2) → reading (60-80 words) → readAlong → introAudio
    - Session 3: introAudio → viewFlashcards (all) → speakFlashcards (all) → vocabLevel1 (all) → vocabLevel2 (all) → writingSentence (3-4 items) → introAudio
    - Session 4: introAudio → reading (100-120 words) → speakReading → readAlong → writingSentence (2-3 items) → introAudio (farewell)
    - Description tone: `surprising_fact`, farewell tone: `warm_accountability`
    - Series ID: `8ncwoino`, display order: 10
    - _Requirements: 1.1, 1.4, 2.1, 2.4, 3.1, 3.2, 3.3, 3.4, 3.5, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 7.2, 8.1, 8.4, 8.6, 8.7, 9.1-9.7, 11.2, 11.3, 12.1, 12.3, 12.6, 12.9, 12.10, 13.1, 14.1-14.4_

  - [x] 4.2 Create `vi-en-children-curriculum-batch2/create_food.py` — "Bữa Ăn Vui Vẻ"
    - Beginner short format: 4 sessions, 10 words (rice, soup, egg, milk, bread, chicken, noodle, cake, cookie, juice), price 19
    - Same 4-session structure as 4.1 but all content hand-crafted for food topic
    - Description tone: `metaphor_led`, farewell tone: `team_building_energy`
    - Series ID: `8ncwoino`, display order: 11
    - _Requirements: 1.1, 1.4, 2.1, 2.4, 3.1, 3.2, 3.3, 3.4, 3.5, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 7.2, 8.1, 8.4, 8.6, 8.7, 9.1-9.7, 11.2, 11.3, 12.1, 12.3, 12.6, 12.9, 12.10, 13.1, 14.1-14.4_

  - [x] 4.3 Create `vi-en-children-curriculum-batch2/create_clothing.py` — "Tủ Quần Áo"
    - Beginner short format: 4 sessions, 10 words (shirt, pants, dress, shoes, hat, socks, jacket, skirt, scarf, gloves), price 19
    - Same 4-session structure as 4.1 but all content hand-crafted for clothing topic
    - Description tone: `bold_declaration`, farewell tone: `quiet_awe`
    - Series ID: `8ncwoino`, display order: 12
    - _Requirements: 1.1, 1.4, 2.1, 2.4, 3.1, 3.2, 3.3, 3.4, 3.5, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 7.2, 8.1, 8.4, 8.6, 8.7, 9.1-9.7, 11.2, 11.3, 12.1, 12.3, 12.6, 12.9, 12.10, 13.1, 14.1-14.4_

- [x] 5. Checkpoint — All beginner curriculums created
  - Verify 6 new curriculums exist in Series 1 with display orders 7-12
  - Verify prices: 3 mini at 9, 3 short at 19
  - Verify language pair: all have `language="en"`, `userLanguage="vi"`
  - Run duplicate check for all 6 titles

- [x] 6. Create preintermediate short curriculum scripts (4 scripts, Series 2: "Khám Phá Thêm")
  - [x] 6.1 Create `vi-en-children-curriculum-batch2/create_numbers.py` — "Đếm Và Khám Phá"
    - Preintermediate short format: 4 sessions, 12 words (count, number, add, minus, equal, double, half, pair, dozen, zero, hundred, thousand), price 49
    - Session 1: introAudio → viewFlashcards (group 1) → speakFlashcards (group 1) → vocabLevel1 (group 1) → vocabLevel2 (group 1) → reading (80-100 words) → speakReading → readAlong → introAudio
    - Session 2: introAudio → viewFlashcards (group 2) → speakFlashcards (group 2) → vocabLevel1 (group 2) → vocabLevel2 (group 2) → reading (80-100 words) → speakReading → readAlong → introAudio
    - Session 3: introAudio → viewFlashcards (all) → speakFlashcards (all) → vocabLevel1 (all) → vocabLevel2 (all) → writingSentence (4-5 items) → introAudio
    - Session 4: introAudio → reading (150-180 words) → speakReading → readAlong → writingSentence (3-4 items) → introAudio (farewell)
    - Description tone: `empathetic_observation`, farewell tone: `practical_momentum`
    - Series ID: `l8l9bexl`, display order: 5
    - _Requirements: 1.1, 1.5, 2.1, 2.4, 3.1, 3.2, 3.3, 3.4, 3.5, 4.3, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 7.3, 8.2, 8.5, 8.6, 8.7, 9.1-9.7, 11.2, 11.3, 12.1, 12.3, 12.6, 12.9, 12.10, 13.1, 14.1-14.4, 17.2_

  - [x] 6.2 Create `vi-en-children-curriculum-batch2/create_shapes.py` — "Hình Dạng Kỳ Thú"
    - Preintermediate short format: 4 sessions, 12 words (circle, square, triangle, rectangle, star, diamond, oval, cube, sphere, straight, corner, pattern), price 49
    - Same 4-session structure as 6.1 but all content hand-crafted for shapes topic
    - Description tone: `provocative_question`, farewell tone: `warm_accountability`
    - Series ID: `l8l9bexl`, display order: 6
    - _Requirements: 1.1, 1.5, 2.1, 2.4, 3.1, 3.2, 3.3, 3.4, 3.5, 4.3, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 7.3, 8.2, 8.5, 8.6, 8.7, 9.1-9.7, 11.2, 11.3, 12.1, 12.3, 12.6, 12.9, 12.10, 13.1, 14.1-14.4_

  - [x] 6.3 Create `vi-en-children-curriculum-batch2/create_ocean.py` — "Đại Dương Xanh"
    - Preintermediate short format: 4 sessions, 12 words (whale, dolphin, shark, octopus, turtle, crab, jellyfish, seahorse, coral, wave, shell, seaweed), price 49
    - Same 4-session structure as 6.1 but all content hand-crafted for ocean animals topic
    - Description tone: `vivid_scenario`, farewell tone: `introspective_guide`
    - Series ID: `l8l9bexl`, display order: 7
    - _Requirements: 1.1, 1.5, 2.1, 2.4, 3.1, 3.2, 3.3, 3.4, 3.5, 4.3, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 7.3, 8.2, 8.5, 8.6, 8.7, 9.1-9.7, 11.2, 11.3, 12.1, 12.3, 12.6, 12.9, 12.10, 13.1, 14.1-14.4_

  - [x] 6.4 Create `vi-en-children-curriculum-batch2/create_sports.py` — "Thể Thao Sôi Động"
    - Preintermediate short format: 4 sessions, 12 words (soccer, swim, basketball, tennis, dance, stretch, throw, catch, goal, score, practice, champion), price 49
    - Same 4-session structure as 6.1 but all content hand-crafted for sports topic
    - Description tone: `bold_declaration`, farewell tone: `team_building_energy`
    - Series ID: `l8l9bexl`, display order: 8
    - _Requirements: 1.1, 1.5, 2.1, 2.4, 3.1, 3.2, 3.3, 3.4, 3.5, 4.3, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 7.3, 8.2, 8.5, 8.6, 8.7, 9.1-9.7, 11.2, 11.3, 12.1, 12.3, 12.6, 12.9, 12.10, 13.1, 14.1-14.4_

- [x] 7. Checkpoint — All 10 Batch 2 curriculums created
  - Verify 6 curriculums in Series 1 with display orders 7-12
  - Verify 4 curriculums in Series 2 with display orders 5-8
  - Verify prices: 3 mini at 9, 3 short at 19, 4 preintermediate at 49
  - Verify language pair: all have `language="en"`, `userLanguage="vi"`
  - Run duplicate check for all 10 titles
  - Verify zero vocabulary overlap with Batch 1 and between Batch 2 curriculums

- [x] 8. Documentation and cleanup
  - [x] 8.1 Update `vi-en-children-curriculum/README.md` with Batch 2 information
    - Add all 10 Batch 2 curriculum IDs, titles, display orders, vocabulary lists, tone assignments, and pricing
    - Update SQL verification queries to include Batch 2 IDs
    - _Requirements: 15.1_

  - [x] 8.2 Create `vi-en-children-curriculum-batch2/README.md` with pointer to main README
    - Brief note that Batch 2 scripts were deleted after creation
    - Pointer to `vi-en-children-curriculum/README.md` for full documentation
    - _Requirements: 15.2_

  - [x] 8.3 Delete all Batch 2 creation scripts after verification
    - Delete all 10 `create_*.py` scripts from `vi-en-children-curriculum-batch2/`
    - Only `README.md` remains in the directory
    - _Requirements: 15.2_

  - [x] 8.4 Run duplicate check and resolve
    - Run duplicate check query for each of the 10 curriculum titles
    - If duplicates found: keep earliest, remove from series first, then delete extras
    - _Requirements: 15.3_

- [x] 9. Final checkpoint — All tasks complete
  - Verify 10 new curriculums total: 3 mini + 3 short + 4 preintermediate
  - Verify collection and series structure is correct (20 total curriculums across both batches)
  - Verify README.md is updated and all creation scripts are deleted
  - Verify no `setPublic` calls were made (all curriculums remain private)
  - Verify validator file remains at `vi-en-children-curriculum/validate_content.py` for future batches

## Notes

- No orchestrator needed — reuses existing collection (uyw1ywsg) and series (8ncwoino, l8l9bexl)
- Display orders continue from Batch 1: Series 1 starts at 7, Series 2 starts at 5
- The children-specific validator must be recreated at `vi-en-children-curriculum/validate_content.py` since it was deleted after Batch 1
- Root-level `api_helpers.py` is reused as-is — no changes needed
- All curriculum content must be hand-crafted — no template-based generation
- Three formats: beginner_mini (1 session, 3-5 words, price 9), beginner_short (4 sessions, 8-10 words, price 19), preintermediate_short (4 sessions, 10-12 words, price 49)
- Vietnamese session titles: "Phần 1", "Phần 2", "Ôn tập", "Đọc tổng hợp" (for short/preintermediate)
- All marketing text (title, description, preview) in Vietnamese targeting parents
- All learner-facing content (introAudio, reading, writing prompts) bilingual with warm child-friendly tone
- Zero vocabulary overlap with Batch 1 (120+ words) and between Batch 2 curriculums
- Tone adjacency with Batch 1 verified: Series 1 first ≠ bold_declaration/warm_accountability, Series 2 first ≠ surprising_fact/team_building_energy
- Tone distribution across 10 Batch 2 descriptions: max 20%, all ≤30% ✓
- No adjacent tone duplicates within either series ✓
- Farewell tones evenly distributed: 2 each across 5 registers ✓
- No new property-based tests needed — existing validator tests from Batch 1 cover all structural validation
- The validator file is kept after Batch 2 (not deleted) to support potential future batches
