# Implementation Plan: Vi Beginner Short Curriculums

## Overview

Create 60 short, beginner-level, single-session curriculums (30 vi-en, 30 vi-zh) with 3-5 vocabulary words each, priced at 9 credits. Implementation follows: shared modules first (short content validator, `set_price` addition), then Phase 1 vi-en (orchestrator + 30 scripts), then Phase 2 vi-zh (orchestrator + 30 scripts). Each curriculum script hand-crafts all content, validates via `validate_short_content.py`, and uploads via the existing `api_helpers.py`. Tone assignments come from the existing `tone_assigner.py` with `assign_tones_for_language_pair(1, 5, 6)`.

## Tasks

- [x] 1. Add `set_price` function to `api_helpers.py`
  - [x] 1.1 Implement `set_price(curriculum_id: str, price: int) -> None` in the repo-root `api_helpers.py`
    - POST to `{API_BASE}/curriculum/setPrice` with `firebaseIdToken`, `id`, `price`
    - Use 30-second timeout, log success/failure with curriculum ID and price
    - Follow the same error handling pattern as existing functions (try/except, raise on failure)
    - _Requirements: 8.1, 8.2, 14.2_

- [x] 2. Create short content validator (`validate_short_content.py` at repo root)
  - [x] 2.1 Implement `validate_short_content.py` with the `validate_short(content: dict) -> None` function
    - Reuse logic from `validate_content.py` for: top-level structure checks (`title`, `description`, `preview.text`, `contentTypeTags`), activity structure checks (`activityType` not `type`, `title`, `description`, `data`), activity-type-specific data rules, vocabList format enforcement (lowercase strings, field name `vocabList` not `words`), flashcard consistency (viewFlashcards/speakFlashcards identical vocabList), writingSentence/writingParagraph data structure checks, strip-keys exclusion
    - New/modified checks for short format: exactly 1 learning session (not 5), between 3 and 5 unique vocabulary words total (not 18 with 6-per-session), reject any `vocabLevel3` activity
    - Raise `ValueError` with specific violation message on any failure
    - _Requirements: 1.1, 1.2, 1.5, 1.6, 11.5, 12.1–12.7, 13.1–13.10_

  - [x] 2.2 Write property test: Top-level structure validation (Property 1)
    - **Property 1: Top-level structure validation**
    - Use `hypothesis` to generate curriculum JSON with missing/empty top-level fields and verify the validator rejects them with specific messages
    - **Validates: Requirements 1.5, 13.1**

  - [x] 2.3 Write property test: Single session invariant (Property 2)
    - **Property 2: Single session invariant**
    - Use `hypothesis` to generate curriculum JSON with wrong session counts (0, 2, 5) and verify rejection
    - **Validates: Requirements 1.1, 13.2**

  - [x] 2.4 Write property test: Vocabulary count invariant (Property 3)
    - **Property 3: Vocabulary count invariant**
    - Use `hypothesis` to generate curriculum JSON with vocab counts outside 3-5 range and verify rejection
    - **Validates: Requirements 1.2, 13.9**

  - [x] 2.5 Write property test: Activity structure completeness (Property 4)
    - **Property 4: Activity structure completeness**
    - Use `hypothesis` to generate activities with missing fields, `type` instead of `activityType`, invalid activityType values, inline content fields
    - **Validates: Requirements 12.1, 12.2, 12.5, 13.3, 13.4**

  - [x] 2.6 Write property test: VocabList format enforcement (Property 5)
    - **Property 5: VocabList format enforcement**
    - Use `hypothesis` to generate vocab activities with uppercase strings, non-string elements, `words` field name
    - **Validates: Requirements 12.3, 13.5**

  - [x] 2.7 Write property test: Flashcard vocabList consistency (Property 6)
    - **Property 6: Flashcard vocabList consistency**
    - Use `hypothesis` to generate sessions with mismatched viewFlashcards/speakFlashcards vocabLists
    - **Validates: Requirements 12.4, 13.6**

  - [x] 2.8 Write property test: Writing activity structure (Property 7)
    - **Property 7: Writing activity structure**
    - Use `hypothesis` to generate writingSentence/writingParagraph activities with missing or malformed data fields
    - **Validates: Requirements 12.6, 12.7, 13.7**

  - [x] 2.9 Write property test: Strip keys exclusion (Property 8)
    - **Property 8: Strip keys exclusion**
    - Use `hypothesis` to inject strip-keys at various depths in curriculum JSON and verify rejection
    - **Validates: Requirements 1.6, 13.8**

  - [x] 2.10 Write property test: No vocabLevel3 activities (Property 9)
    - **Property 9: No vocabLevel3 activities**
    - Use `hypothesis` to generate curriculum JSON containing vocabLevel3 activities and verify rejection
    - **Validates: Requirements 11.5**

  - [x] 2.11 Write property test: Validator rejects invalid content with specific message (Property 10)
    - **Property 10: Validator rejects invalid content with specific message**
    - Use `hypothesis` to generate various invalid curriculum JSONs and verify the validator always raises `ValueError` (never silently passes) with a non-empty message identifying the specific violation
    - **Validates: Requirements 13.10**

- [x] 3. Checkpoint — Shared modules ready
  - Ensure all tests pass, ask the user if questions arise.

- [x] 4. Phase 1: vi-en (30 curriculums)
  - [x] 4.1 Create `vi-beginner-short-curriculums/vi-en/` directory and `orchestrator.py`
    - Create 1 collection via `create_collection()` with Vietnamese title (e.g. "Tiếng Anh cơ bản — Bài học ngắn") and informative description (not persuasive copy)
    - Create 5 series (Everyday Life, Family and Relationships, School and Work, Food and Health, Travel and Places) via `create_series()` with Vietnamese titles and descriptions ≤255 chars using tone-assigned Tone_Palette types
    - Wire series to collection via `add_series_to_collection()`, set series display orders 1-5
    - Pre-compute tone assignments using `tone_assigner.assign_tones_for_language_pair(1, 5, 6)` and log the full assignment table
    - Log all collection/series IDs to stdout for use by curriculum scripts
    - Ensure no two adjacent series use the same Tone_Palette type
    - _Requirements: 7.1–7.9, 9.3, 9.4, 9.8, 9.9, 14.2, 14.3, 18.2_

  - [x] 4.2 Create curriculum scripts for Series 1 — Everyday Life (6 scripts)
    - Create `create_greetings.py` (balanced_skills), `create_market.py` (speaking_focus), `create_ordering_food.py` (speaking_focus), `create_directions.py` (reader), `create_daily_routines.py` (writing_lover), `create_weather.py` (balanced_skills)
    - Each script: hand-crafted Vietnamese user-facing text (persuasive copy with tone-assigned headline), English reading passages (simple sentences <15 words, present tense, high-frequency vocab), 3-5 vocabulary words per curriculum
    - Use the correct activity template per skill focus target (speaking_focus/writing_lover/reader/balanced_skills)
    - Writing activities heavily scaffolded: writingSentence with example sentence + substitution pattern, writingParagraph as guided 2-3 sentence fill-in
    - Validate via `validate_short(content)` before upload, then `create_curriculum(content, "en", "vi")`, `add_to_series()`, `set_display_order()`
    - No vocabulary overlap within the series, no two adjacent curriculums share the same skill focus target
    - Minimal Vietnamese titles (no series/collection name repetition)
    - _Requirements: 1.1–1.9, 2.1–2.5, 3.1, 3.3, 4.1–4.3, 5.1–5.4, 9.1–9.4, 10.1–10.4, 11.1–11.6, 12.1–12.8, 14.1, 14.4–14.8, 15.1, 16.1, 16.2_

  - [x] 4.3 Create curriculum scripts for Series 2 — Family and Relationships (6 scripts)
    - Create `create_family_members.py` (reader), `create_describing_people.py` (writing_lover), `create_feelings.py` (balanced_skills), `create_making_friends.py` (speaking_focus), `create_celebrations.py` (reader), `create_helping_home.py` (writing_lover)
    - Same quality and structural requirements as 4.2
    - _Requirements: 1.1–1.9, 2.1–2.5, 3.1, 3.3, 4.1–4.3, 5.1–5.4, 9.1–9.4, 10.1–10.4, 11.1–11.6, 12.1–12.8, 14.1, 14.4–14.8, 15.1, 16.1, 16.2_

  - [x] 4.4 Create curriculum scripts for Series 3 — School and Work (6 scripts)
    - Create `create_classroom.py` (balanced_skills), `create_school_day.py` (reader), `create_jobs.py` (writing_lover), `create_hobbies.py` (speaking_focus), `create_numbers_time.py` (balanced_skills), `create_about_yourself.py` (writing_lover)
    - Same quality and structural requirements as 4.2
    - _Requirements: 1.1–1.9, 2.1–2.5, 3.1, 3.3, 4.1–4.3, 5.1–5.4, 9.1–9.4, 10.1–10.4, 11.1–11.6, 12.1–12.8, 14.1, 14.4–14.8, 15.1, 16.1, 16.2_

  - [x] 4.5 Create curriculum scripts for Series 4 — Food and Health (6 scripts)
    - Create `create_fruits_vegetables.py` (reader), `create_cooking.py` (writing_lover), `create_doctor.py` (speaking_focus), `create_healthy_habits.py` (balanced_skills), `create_vn_food_english.py` (writing_lover), `create_body_exercise.py` (speaking_focus)
    - Same quality and structural requirements as 4.2
    - _Requirements: 1.1–1.9, 2.1–2.5, 3.1, 3.3, 4.1–4.3, 5.1–5.4, 9.1–9.4, 10.1–10.4, 11.1–11.6, 12.1–12.8, 14.1, 14.4–14.8, 15.1, 16.1, 16.2_

  - [x] 4.6 Create curriculum scripts for Series 5 — Travel and Places (6 scripts)
    - Create `create_airport.py` (speaking_focus), `create_hotel.py` (balanced_skills), `create_famous_places_vn.py` (reader), `create_transportation.py` (speaking_focus), `create_postcard.py` (writing_lover), `create_beach.py` (reader)
    - Same quality and structural requirements as 4.2
    - _Requirements: 1.1–1.9, 2.1–2.5, 3.1, 3.3, 4.1–4.3, 5.1–5.4, 9.1–9.4, 10.1–10.4, 11.1–11.6, 12.1–12.8, 14.1, 14.4–14.8, 15.1, 16.1, 16.2_

  - [x] 4.7 Run orchestrator pricing pass and verify vi-en phase
    - Run orchestrator pricing pass: call `set_price(curriculum_id, 9)` for all 30 vi-en curriculums
    - Run duplicate check queries for all 30 curriculum titles
    - Verify each series has exactly 6 curriculums with correct display orders, language values (language=en, userLanguage=vi), non-empty content
    - Verify skill focus distribution: 8 speaking_focus, 8 writing_lover, 7 reader, 7 balanced_skills
    - Verify no vocabulary overlap within any series
    - Verify all 30 curriculums have price=9
    - _Requirements: 4.1, 4.2, 8.1, 8.2, 17.3, 18.3, 18.4, 18.5_

- [x] 5. Checkpoint — vi-en phase complete
  - Ensure all tests pass, ask the user if questions arise.

- [x] 6. Phase 2: vi-zh (30 curriculums)
  - [x] 6.1 Create `vi-beginner-short-curriculums/vi-zh/` directory and `orchestrator.py`
    - Create 1 collection with Vietnamese title (e.g. "Tiếng Trung cơ bản — Bài học ngắn") and informative description
    - Create 5 series (Everyday Life, Family and Relationships, School and Work, Food and Health, Travel and Places) with Vietnamese titles and descriptions ≤255 chars using tone-assigned Tone_Palette types
    - Wire series to collection, set series display orders 1-5
    - Pre-compute tone assignments using `tone_assigner.assign_tones_for_language_pair(1, 5, 6)`
    - Log all IDs to stdout
    - _Requirements: 7.1–7.9, 9.3, 9.4, 9.8, 9.9, 14.2, 14.3, 18.2_

  - [x] 6.2 Create curriculum scripts for Series 1 — Everyday Life (6 scripts)
    - Create `create_greetings.py` (balanced_skills), `create_store.py` (speaking_focus), `create_restaurant.py` (speaking_focus), `create_directions.py` (reader), `create_daily_schedule.py` (writing_lover), `create_weather_clothing.py` (balanced_skills)
    - Each script: hand-crafted Vietnamese user-facing text, Chinese reading passages (simple sentences, basic grammar 是/有/在/了/的, high-frequency characters), 3-5 simplified Chinese vocabulary words per curriculum
    - Use the correct activity template per skill focus target
    - Writing activities heavily scaffolded for beginners
    - Validate via `validate_short(content)` before upload, then `create_curriculum(content, "zh", "vi")`, `add_to_series()`, `set_display_order()`
    - No vocabulary overlap within the series, no two adjacent curriculums share the same skill focus target
    - _Requirements: 1.1–1.9, 2.1–2.5, 3.2, 3.4, 4.1–4.3, 6.1–6.4, 9.1–9.4, 10.1–10.4, 11.1–11.6, 12.1–12.8, 14.1, 14.4–14.8, 15.1, 16.1, 16.2_

  - [x] 6.3 Create curriculum scripts for Series 2 — Family and Relationships (6 scripts)
    - Create `create_family_members.py` (reader), `create_describing_people.py` (writing_lover), `create_feelings.py` (balanced_skills), `create_chinese_friends.py` (speaking_focus), `create_chinese_new_year.py` (reader), `create_household_chores.py` (writing_lover)
    - Same quality and structural requirements as 6.2
    - _Requirements: 1.1–1.9, 2.1–2.5, 3.2, 3.4, 4.1–4.3, 6.1–6.4, 9.1–9.4, 10.1–10.4, 11.1–11.6, 12.1–12.8, 14.1, 14.4–14.8, 15.1, 16.1, 16.2_

  - [x] 6.4 Create curriculum scripts for Series 3 — School and Work (6 scripts)
    - Create `create_school_supplies.py` (balanced_skills), `create_school_day.py` (reader), `create_common_jobs.py` (writing_lover), `create_interests.py` (speaking_focus), `create_numbers_counting.py` (balanced_skills), `create_about_my_life.py` (writing_lover)
    - Same quality and structural requirements as 6.2
    - _Requirements: 1.1–1.9, 2.1–2.5, 3.2, 3.4, 4.1–4.3, 6.1–6.4, 9.1–9.4, 10.1–10.4, 11.1–11.6, 12.1–12.8, 14.1, 14.4–14.8, 15.1, 16.1, 16.2_

  - [x] 6.5 Create curriculum scripts for Series 4 — Food and Health (6 scripts)
    - Create `create_chinese_foods.py` (reader), `create_simple_recipe.py` (writing_lover), `create_visiting_doctor.py` (speaking_focus), `create_staying_healthy.py` (balanced_skills), `create_vn_vs_cn_cuisine.py` (writing_lover), `create_body_parts.py` (speaking_focus)
    - Same quality and structural requirements as 6.2
    - _Requirements: 1.1–1.9, 2.1–2.5, 3.2, 3.4, 4.1–4.3, 6.1–6.4, 9.1–9.4, 10.1–10.4, 11.1–11.6, 12.1–12.8, 14.1, 14.4–14.8, 15.1, 16.1, 16.2_

  - [x] 6.6 Create curriculum scripts for Series 5 — Travel and Places (6 scripts)
    - Create `create_train_station.py` (speaking_focus), `create_hotel.py` (balanced_skills), `create_famous_places_china.py` (reader), `create_getting_around.py` (speaking_focus), `create_writing_trip.py` (writing_lover), `create_park.py` (reader)
    - Same quality and structural requirements as 6.2
    - _Requirements: 1.1–1.9, 2.1–2.5, 3.2, 3.4, 4.1–4.3, 6.1–6.4, 9.1–9.4, 10.1–10.4, 11.1–11.6, 12.1–12.8, 14.1, 14.4–14.8, 15.1, 16.1, 16.2_

  - [x] 6.7 Run orchestrator pricing pass and verify vi-zh phase
    - Run orchestrator pricing pass: call `set_price(curriculum_id, 9)` for all 30 vi-zh curriculums
    - Run duplicate check queries for all 30 curriculum titles
    - Verify each series has exactly 6 curriculums with correct display orders, language values (language=zh, userLanguage=vi), non-empty content
    - Verify skill focus distribution: 8 speaking_focus, 8 writing_lover, 7 reader, 7 balanced_skills
    - Verify no vocabulary overlap within any series
    - Verify all 30 curriculums have price=9
    - _Requirements: 4.1, 4.2, 8.1, 8.2, 17.3, 18.3, 18.4, 18.5_

- [x] 7. Checkpoint — vi-zh phase complete
  - Ensure all tests pass, ask the user if questions arise.

- [x] 8. Documentation and cleanup
  - [x] 8.1 Create `vi-beginner-short-curriculums/vi-en/README.md`
    - Document: collection ID, all 5 series IDs, all 30 curriculum IDs with titles and display orders, vocabulary lists per curriculum, tone assignments (description and farewell), skill focus targets per curriculum, SQL verification queries, recreation instructions
    - _Requirements: 17.1_

  - [x] 8.2 Create `vi-beginner-short-curriculums/vi-zh/README.md`
    - Same documentation as 8.1 for the vi-zh language pair
    - _Requirements: 17.1_

  - [x] 8.3 Delete all `create_*.py` and `orchestrator.py` scripts after verification
    - Delete all Python scripts from `vi-en/` and `vi-zh/`, leaving only README.md files
    - _Requirements: 17.2_

- [x] 9. Final checkpoint — All phases complete
  - Ensure all tests pass, ask the user if questions arise.
  - Verify total: 60 curriculums (30 vi-en + 30 vi-zh), 2 collections, 10 series, all priced at 9 credits
  - Verify all READMEs are in place and all creation scripts are deleted

## Notes

- Tasks marked with `*` are optional and can be skipped for faster MVP
- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation between phases
- Property tests (Properties 1-10) validate the short content validator using `hypothesis`
- Tone assignment is handled by the existing `tone_assigner.py` — no new tone tests needed
- Phased execution order: shared modules → vi-en → vi-zh
- All curriculum content must be hand-crafted — no template-based text generation
- Activity structure (types, order) can use shared patterns, but all text is per-curriculum
- The `set_price` function is added to the existing repo-root `api_helpers.py`, not a new file
