# Implementation Plan: Multilingual Curriculum Expansion

## Overview

Create ~460 curriculums across 6 language pairs (vi-fr, vi-de, en-fr, en-de, fr-fr, de-de) organized into collections and series. Implementation follows a phased approach: shared modules first, then language pair by language pair with verification gates. Each language pair gets its own directory with a shared `validate_content.py`, `api_helpers.py`, an `orchestrator.py`, and one `create_*.py` script per curriculum.

## Tasks

- [x] 1. Create shared validation module (`validate_content.py`)
  - [x] 1.1 Implement `validate_content.py` with the `validate(content: dict) -> None` function
    - Check top-level structure: non-null, non-empty `title`, `description`, `preview.text`, `contentTypeTags`, `learningSessions`
    - Check `learningSessions` is array of exactly 5 sessions, each with non-empty `title` and `activities` array
    - Check every activity has `activityType` (not `type`), `title`, `description`, `data` fields; `activityType` is one of the 11 valid values; content fields are inside `data` not inline
    - Check vocabList on viewFlashcards/speakFlashcards/vocabLevel1/vocabLevel2/vocabLevel3: non-empty array of lowercase strings, field name is `vocabList` (never `words`)
    - Check viewFlashcards and speakFlashcards in the same session have identical vocabList arrays
    - Check writingSentence: `data.vocabList`, `data.items` (non-empty array), each item has `prompt` and `targetVocab`
    - Check writingParagraph: `data.vocabList`, `data.instructions` (non-empty string), `data.prompts` (array of strings, length ≥ 2)
    - Check no strip-keys (`mp3Url`, `illustrationSet`, `chapterBookmarks`, `segments`, `whiteboardItems`, `userReadingId`, `lessonUniqueId`, `curriculumTags`, `taskId`, `imageId`) appear anywhere in the JSON tree
    - Check exactly 18 unique vocabulary words across all sessions, 6 per learning session (sessions 1-3)
    - Raise `ValueError` with specific violation message on any failure
    - _Requirements: 5.1, 5.2, 5.6, 5.7, 5.8, 5.9, 5.10, 5.11, 11.1–11.11_

  - [x] 1.2 Write property test: Top-level structure validation (Property 1)
    - **Property 1: Top-level structure validation**
    - Use `hypothesis` to generate curriculum JSON with missing/empty top-level fields and verify the validator rejects them with specific messages
    - **Validates: Requirements 5.9, 11.1**

  - [x] 1.3 Write property test: Session structure invariant (Property 2)
    - **Property 2: Session structure invariant**
    - Use `hypothesis` to generate curriculum JSON with wrong session counts, missing titles, empty activities and verify rejection
    - **Validates: Requirements 5.1, 11.2**

  - [x] 1.4 Write property test: Vocabulary distribution invariant (Property 3)
    - **Property 3: Vocabulary distribution invariant**
    - Use `hypothesis` to generate curriculum JSON with wrong vocab counts (not 18 total, not 6 per session) and verify rejection
    - **Validates: Requirements 3.4, 5.2, 11.10**

  - [x] 1.5 Write property test: Activity structure completeness (Property 4)
    - **Property 4: Activity structure completeness**
    - Use `hypothesis` to generate activities with missing fields, `type` instead of `activityType`, invalid activityType values, inline content fields
    - **Validates: Requirements 5.6, 11.3, 11.4**

  - [x] 1.6 Write property test: VocabList format enforcement (Property 5)
    - **Property 5: VocabList format enforcement**
    - Use `hypothesis` to generate vocab activities with uppercase strings, non-string elements, `words` field name
    - **Validates: Requirements 5.7, 11.5**

  - [x] 1.7 Write property test: Flashcard vocabList consistency (Property 6)
    - **Property 6: Flashcard vocabList consistency**
    - Use `hypothesis` to generate sessions with mismatched viewFlashcards/speakFlashcards vocabLists
    - **Validates: Requirements 5.8, 11.6**

  - [x] 1.8 Write property test: Writing activity structure (Property 7)
    - **Property 7: Writing activity structure**
    - Use `hypothesis` to generate writingSentence/writingParagraph activities with missing or malformed data fields
    - **Validates: Requirements 11.7, 11.8**

  - [x] 1.9 Write property test: Strip keys exclusion (Property 8)
    - **Property 8: Strip keys exclusion**
    - Use `hypothesis` to inject strip-keys at various depths in curriculum JSON and verify rejection
    - **Validates: Requirements 5.10, 11.9**

  - [x] 1.10 Write property test: Validator rejects invalid content with specific message (Property 9)
    - **Property 9: Validator rejects invalid content with specific message**
    - Use `hypothesis` to generate various invalid curriculum JSONs and verify the validator always raises an error (never silently passes) with a message identifying the specific violation
    - **Validates: Requirements 5.11, 11.11**

- [x] 2. Create shared API helpers module (`api_helpers.py`)
  - [x] 2.1 Implement `api_helpers.py` with all API wrapper functions
    - `get_token()` — wraps `firebase_token.get_firebase_id_token` with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`
    - `create_curriculum(content, language, user_language)` — POST to `curriculum/create` with `language` and `userLanguage` as top-level body params, `content` as JSON string; returns curriculum ID
    - `add_to_series(series_id, curriculum_id)` — POST to `curriculum-series/addCurriculum`
    - `set_display_order(curriculum_id, order)` — POST to `curriculum/setDisplayOrder`
    - `create_collection(title, description)` — POST to `curriculum-collection/create`; returns collection ID
    - `create_series(title, description)` — POST to `curriculum-series/create`; returns series ID
    - `add_series_to_collection(collection_id, series_id)` — POST to `curriculum-collection/addSeriesToCollection`
    - `set_series_display_order(series_id, order)` — POST to `curriculum-series/setDisplayOrder`
    - `set_collection_display_order(collection_id, order)` — POST to `curriculum-collection/setDisplayOrder`
    - Use 30-second timeout on all requests; log errors with context on failure
    - _Requirements: 6.1–6.7, 6.11, 6.12, 9.6, 9.7, 9.8_

  - [x] 2.2 Write unit tests for `api_helpers.py`
    - Verify `create_curriculum` passes `language` and `userLanguage` as top-level body params (not only inside content)
    - Verify no `setPublic` calls are made
    - Verify error handling logs and continues on API failure
    - _Requirements: 6.11, 6.12, 9.8_

- [x] 3. Create tone assignment logic
  - [x] 3.1 Implement tone pre-assignment utility
    - Create a function/module that assigns description tones (6-tone palette) and farewell tones (5-tone palette) to all curriculums, series, and collections for a language pair
    - Enforce: no two adjacent curriculums in a series share the same description tone or farewell tone
    - Enforce: no two adjacent series in a collection share the same description tone
    - Enforce: no single tone exceeds 30% of descriptions per language pair
    - Output tone assignments as a data structure usable by orchestrator and curriculum scripts
    - _Requirements: 8.1–8.7_

  - [x] 3.2 Write property test: Tone palette validity (Property 10)
    - **Property 10: Tone palette validity**
    - Use `hypothesis` to generate tone assignments and verify every description tone is one of the 6 valid types and every farewell tone is one of the 5 valid registers
    - **Validates: Requirements 8.1, 8.5**

  - [x] 3.3 Write property test: Tone adjacency constraint (Property 11)
    - **Property 11: Tone adjacency constraint**
    - Use `hypothesis` to generate sequences of tone assignments and verify no two adjacent entries share the same tone value (for both description and farewell tones within series, and series tones within collections)
    - **Validates: Requirements 8.2, 8.3, 8.6**

  - [x] 3.4 Write property test: Tone distribution cap (Property 12)
    - **Property 12: Tone distribution cap**
    - Use `hypothesis` to generate batches of description tone assignments and verify no single tone type exceeds 30% of the total
    - **Validates: Requirements 8.4**

- [x] 4. Checkpoint — Ensure shared modules are correct
  - Ensure all tests pass, ask the user if questions arise.

- [x] 5. Phase 1: vi-fr language pair (~100 curriculums)
  - [x] 5.1 Create `vi-fr/` directory structure and copy shared modules
    - Create `vi-fr/` directory with `validate_content.py`, `api_helpers.py`
    - Create series subdirectories: `a1_food_dining/` through `d5_traditions_festivals/` (20 series)
    - _Requirements: 9.3_

  - [x] 5.2 Create `vi-fr/orchestrator.py`
    - Create 4 collections (Daily Life and Travel, Business and Professional, Academic and Intellectual, Culture and Society) with Vietnamese titles and French topic labels in parentheses
    - Create 20 series (5 per collection) with Vietnamese titles, French labels, descriptions ≤255 chars using assigned tones
    - Wire series to collections, set display orders for series and collections
    - Document all tone assignments in comments
    - Collection descriptions: short informative category summaries (not persuasive copy)
    - Series descriptions: short persuasive hooks ≤255 chars using Tone_Palette
    - Log all collection/series IDs to stdout
    - _Requirements: 2.1, 2.5, 3.1, 6.1–6.9, 8.1–8.4, 8.8, 8.9, 10.2_

  - [x] 5.3 Create curriculum scripts for Collection A — Daily Life and Travel (25 scripts)
    - Create `create_*.py` for each of the 25 curriculums across series A1–A5
    - Each script: hand-crafted Vietnamese user-facing text (persuasive copy with tone-assigned headline), French reading passages, 18 vocabulary words (6 per learning session), 5 sessions with correct activity order
    - Validate via `validate_content.py` before upload
    - Vietnamese persuasive copy conventions, French reading at preintermediate-to-intermediate level
    - No vocabulary repeats within a series (90 unique words per series)
    - Minimal curriculum titles (no series/collection name repetition)
    - _Requirements: 1.1, 1.7, 3.1, 3.2, 3.4, 3.5, 5.1–5.10, 7.1–7.10, 8.1–8.7, 9.1, 12.1, 12.5, 12.9_

  - [x] 5.4 Create curriculum scripts for Collection B — Business and Professional (25 scripts)
    - Same structure as 5.3 for series B1–B5
    - _Requirements: 1.1, 1.7, 3.1, 3.2, 3.4, 3.5, 5.1–5.10, 7.1–7.10, 8.1–8.7, 9.1, 12.1, 12.5, 12.9_

  - [x] 5.5 Create curriculum scripts for Collection C — Academic and Intellectual (25 scripts)
    - Same structure as 5.3 for series C1–C5
    - _Requirements: 1.1, 1.7, 3.1, 3.2, 3.4, 3.5, 5.1–5.10, 7.1–7.10, 8.1–8.7, 9.1, 12.1, 12.5, 12.9_

  - [x] 5.6 Create curriculum scripts for Collection D — Culture and Society (25 scripts)
    - Same structure as 5.3 for series D1–D5
    - _Requirements: 1.1, 1.7, 3.1, 3.2, 3.4, 3.5, 5.1–5.10, 7.1–7.10, 8.1–8.7, 9.1, 12.1, 12.5, 12.9_

  - [x] 5.7 Verify vi-fr phase and create README
    - Run duplicate check queries for all 100 curriculum titles
    - Verify each series has 5 curriculums with correct display orders, language values (userLanguage=vi, language=fr), non-empty content
    - Verify language homogeneity via `curriculum_series_language_list` view
    - Verify level gap via `curriculum_series_level_gap` view
    - Create `vi-fr/README.md` with all collection IDs, series IDs, curriculum IDs, display orders, vocabulary lists, tone assignments, SQL verification queries, recreation instructions
    - Delete all `create_*.py` scripts after verification
    - _Requirements: 9.4, 9.5, 9.9, 10.3, 10.4, 10.5, 10.6, 13.1–13.6_

- [ ] 6. Checkpoint — vi-fr phase complete
  - Ensure all tests pass, ask the user if questions arise.

- [x] 7. Phase 2: vi-de language pair (~100 curriculums)
  - [x] 7.1 Create `vi-de/` directory structure and copy shared modules
    - Create `vi-de/` directory with `validate_content.py`, `api_helpers.py`
    - Create series subdirectories (20 series)
    - _Requirements: 9.3_

  - [x] 7.2 Create `vi-de/orchestrator.py`
    - Same structure as vi-fr orchestrator but with German topic labels in parentheses
    - Vietnamese titles for collections and series, German labels where appropriate
    - _Requirements: 2.1, 2.6, 3.1, 6.1–6.9, 8.1–8.4, 8.8, 8.9, 10.2_

  - [x] 7.3 Create curriculum scripts for Collections A–D (100 scripts)
    - Hand-crafted Vietnamese user-facing text, German reading passages at preintermediate-to-intermediate level
    - 18 vocabulary words per curriculum from standard High German (Hochdeutsch)
    - Vietnamese persuasive copy, German reading passages
    - Same quality and structural requirements as vi-fr
    - _Requirements: 1.2, 1.7, 3.1, 3.2, 3.4, 3.5, 5.1–5.10, 7.1–7.10, 8.1–8.7, 9.1, 12.2, 12.5, 12.10_

  - [x] 7.4 Verify vi-de phase and create README
    - Same verification as vi-fr: duplicates, series counts, language homogeneity (userLanguage=vi, language=de), level gap, display orders
    - Create `vi-de/README.md`, delete scripts
    - _Requirements: 9.4, 9.5, 9.9, 10.3, 10.4, 10.5, 10.6, 13.1–13.6_

- [ ] 8. Checkpoint — vi-de phase complete
  - Ensure all tests pass, ask the user if questions arise.

- [x] 9. Phase 3: en-fr language pair (~100 curriculums)
  - [x] 9.1 Create `en-fr/` directory structure and copy shared modules
    - Create `en-fr/` directory with `validate_content.py`, `api_helpers.py`
    - Create series subdirectories (20 series)
    - _Requirements: 9.3_

  - [x] 9.2 Create `en-fr/orchestrator.py`
    - English titles for collections and series, French topic labels in parentheses
    - _Requirements: 2.1, 2.7, 3.1, 6.1–6.9, 8.1–8.4, 8.8, 8.9, 10.2_

  - [x] 9.3 Create curriculum scripts for Collections A–D (100 scripts)
    - Hand-crafted English user-facing text (English persuasive copy conventions), French reading passages
    - Contexts relevant to English-speaking learners (expats, international students, business travelers)
    - 18 vocabulary words per curriculum from standard French
    - _Requirements: 1.3, 1.7, 3.1, 3.3, 3.4, 3.5, 5.1–5.10, 7.1–7.10, 8.1–8.7, 9.1, 12.1, 12.6, 12.9_

  - [x] 9.4 Verify en-fr phase and create README
    - Same verification pattern: duplicates, series counts, language homogeneity (userLanguage=en, language=fr), level gap, display orders
    - Create `en-fr/README.md`, delete scripts
    - _Requirements: 9.4, 9.5, 9.9, 10.3, 10.4, 10.5, 10.6, 13.1–13.6_

- [ ] 10. Checkpoint — en-fr phase complete
  - Ensure all tests pass, ask the user if questions arise.

- [x] 11. Phase 4: en-de language pair (~100 curriculums)
  - [x] 11.1 Create `en-de/` directory structure and copy shared modules
    - Create `en-de/` directory with `validate_content.py`, `api_helpers.py`
    - Create series subdirectories (20 series)
    - _Requirements: 9.3_

  - [x] 11.2 Create `en-de/orchestrator.py`
    - English titles for collections and series, German topic labels in parentheses
    - _Requirements: 2.1, 2.8, 3.1, 6.1–6.9, 8.1–8.4, 8.8, 8.9, 10.2_

  - [x] 11.3 Create curriculum scripts for Collections A–D (100 scripts)
    - Hand-crafted English user-facing text, German reading passages
    - Contexts relevant to English-speaking learners
    - 18 vocabulary words per curriculum from standard High German
    - _Requirements: 1.4, 1.7, 3.1, 3.3, 3.4, 3.5, 5.1–5.10, 7.1–7.10, 8.1–8.7, 9.1, 12.2, 12.6, 12.10_

  - [x] 11.4 Verify en-de phase and create README
    - Same verification pattern (userLanguage=en, language=de)
    - Create `en-de/README.md`, delete scripts
    - _Requirements: 9.4, 9.5, 9.9, 10.3, 10.4, 10.5, 10.6, 13.1–13.6_

- [ ] 12. Checkpoint — en-de phase complete
  - Ensure all tests pass, ask the user if questions arise.

- [x] 13. Phase 5: fr-fr language pair (~30 curriculums)
  - [x] 13.1 Create `fr-fr/` directory structure and copy shared modules
    - Create `fr-fr/` directory with `validate_content.py`, `api_helpers.py`
    - Create series subdirectories: `e1_literary_analysis/` through `f3_media_journalism/` (6 series)
    - _Requirements: 9.3_

  - [x] 13.2 Create `fr-fr/orchestrator.py`
    - Create 2 collections (Literature and Advanced Culture, Professional Mastery) with French titles
    - Create 6 series (3 per collection) with French titles, descriptions ≤255 chars
    - Wire series to collections, set display orders
    - _Requirements: 2.2, 2.9, 4.1, 6.1–6.9, 8.1–8.4, 8.8, 8.9, 10.2_

  - [x] 13.3 Create curriculum scripts for Collection E — Literature and Advanced Culture (15 scripts)
    - All content entirely in French (introAudio, descriptions, previews, writing prompts, reading passages)
    - Vocabulary from formal/literary French registers (soutenu, littéraire)
    - French persuasive copy conventions adapted to French rhetorical traditions
    - _Requirements: 1.5, 1.8, 4.1, 4.2, 4.4, 5.1–5.10, 7.1–7.10, 8.1–8.7, 9.1, 12.3, 12.7_

  - [x] 13.4 Create curriculum scripts for Collection F — Professional Mastery (15 scripts)
    - Same as 13.3 for series F1–F3
    - _Requirements: 1.5, 1.8, 4.1, 4.2, 4.4, 5.1–5.10, 7.1–7.10, 8.1–8.7, 9.1, 12.3, 12.7_

  - [x] 13.5 Verify fr-fr phase and create README
    - Verify each series has 5 curriculums, language homogeneity (userLanguage=fr, language=fr), level gap, display orders
    - Create `fr-fr/README.md`, delete scripts
    - _Requirements: 9.4, 9.5, 9.9, 10.3, 10.4, 10.5, 10.6, 13.1–13.6_

- [ ] 14. Checkpoint — fr-fr phase complete
  - Ensure all tests pass, ask the user if questions arise.

- [x] 15. Phase 6: de-de language pair (~30 curriculums)
  - [x] 15.1 Create `de-de/` directory structure and copy shared modules
    - Create `de-de/` directory with `validate_content.py`, `api_helpers.py`
    - Create series subdirectories (6 series)
    - _Requirements: 9.3_

  - [x] 15.2 Create `de-de/orchestrator.py`
    - Create 2 collections (Literature and Advanced Culture, Professional Mastery) with German titles
    - Create 6 series (3 per collection) with German titles, descriptions ≤255 chars
    - Wire series to collections, set display orders
    - _Requirements: 2.2, 2.10, 4.1, 6.1–6.9, 8.1–8.4, 8.8, 8.9, 10.2_

  - [x] 15.3 Create curriculum scripts for Collection E — Literature and Advanced Culture (15 scripts)
    - All content entirely in German (introAudio, descriptions, previews, writing prompts, reading passages)
    - Vocabulary from formal/academic German registers (Bildungssprache, Fachsprache)
    - German persuasive copy conventions adapted to German rhetorical traditions
    - _Requirements: 1.6, 1.8, 4.1, 4.3, 4.5, 5.1–5.10, 7.1–7.10, 8.1–8.7, 9.1, 12.4, 12.8_

  - [x] 15.4 Create curriculum scripts for Collection F — Professional Mastery (15 scripts)
    - Same as 15.3 for series F1–F3
    - _Requirements: 1.6, 1.8, 4.1, 4.3, 4.5, 5.1–5.10, 7.1–7.10, 8.1–8.7, 9.1, 12.4, 12.8_

  - [x] 15.5 Verify de-de phase and create README
    - Verify each series has 5 curriculums, language homogeneity (userLanguage=de, language=de), level gap, display orders
    - Create `de-de/README.md`, delete scripts
    - _Requirements: 9.4, 9.5, 9.9, 10.3, 10.4, 10.5, 10.6, 13.1–13.6_

- [x] 16. Final checkpoint — All phases complete
  - Ensure all tests pass, ask the user if questions arise.
  - Verify total curriculum count across all 6 language pairs (~460)
  - Verify all READMEs are in place and all creation scripts are deleted

## Notes

- Tasks marked with `*` are optional and can be skipped for faster MVP
- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation between language pair phases
- Property tests validate the content validator and tone assigner (Properties 1–12 from the design)
- The `validate_content.py` and `api_helpers.py` modules are created once and copied to each language pair directory
- Phased execution order: vi-fr → vi-de → en-fr → en-de → fr-fr → de-de
- All curriculum content must be hand-crafted — no template-based generation
