# Implementation Plan: Bilingual Parity Expansion

## Overview

Create ~773 curriculums across 6 bilingual language pairs (zh-vi, zh-en, de-en, de-vi, fr-en, fr-vi) at beginner, preintermediate, and intermediate levels to reach parity with the en-vi reference pair. Implementation follows a phased approach: extend shared modules for beginner support first, then language pair by language pair with verification gates. Each language pair gets its own directory with `validate_content.py`, `api_helpers.py`, an `orchestrator.py`, and one `create_*.py` script per curriculum. Beginner curriculums (4 sessions, 12 words, no writingParagraph/vocabLevel3, price 19) are new; standard curriculums (5 sessions, 18 words, full activity set, price 49) follow the established pattern.

## Tasks

- [x] 1. Extend shared validation module for beginner support
  - [x] 1.1 Extend `validate_content.py` with level-aware `validate(content, level)` function
    - Add `level` parameter: `"beginner"` or `"standard"` (default)
    - Beginner mode: exactly 4 sessions (2 learning + 1 review + 1 final), exactly 12 unique vocab words (6 per learning session), reject writingParagraph and vocabLevel3 activities
    - Standard mode: exactly 5 sessions (3 learning + 1 review + 1 final), exactly 18 unique vocab words (6 per learning session), require writingParagraph in final session
    - Shared checks (both levels): top-level structure (title, description, preview.text, contentTypeTags, learningSessions), activity structure (activityType not type, valid values, title, description, data), vocabList format (lowercase strings, field name vocabList not words), flashcard consistency (viewFlashcards/speakFlashcards identical vocabList), writing activity structure, strip-keys exclusion
    - Raise `ValueError` with specific violation message on any failure
    - _Requirements: 2.1–2.7, 3.1–3.5, 5.1–5.10, 11.1–11.11_

  - [x] 1.2 Write property test: Top-level structure validation (Property 1)
    - **Property 1: Top-level structure validation**
    - Use `hypothesis` to generate curriculum JSON with missing/empty top-level fields and verify the validator rejects them with specific messages
    - **Validates: Requirements 5.1, 5.2, 11.4**

  - [x] 1.3 Write property test: Level-aware session structure (Property 2)
    - **Property 2: Level-aware session structure**
    - Use `hypothesis` to generate curriculum JSON with wrong session counts for each level (not 4 for beginner, not 5 for standard), missing titles, empty activities and verify rejection
    - **Validates: Requirements 2.2, 3.2, 11.5**

  - [x] 1.4 Write property test: Level-aware vocabulary distribution (Property 3)
    - **Property 3: Level-aware vocabulary distribution**
    - Use `hypothesis` to generate curriculum JSON with wrong vocab counts (not 12 for beginner, not 18 for standard, not 6 per learning session) and verify rejection
    - **Validates: Requirements 2.1, 3.1, 11.9**

  - [x] 1.5 Write property test: Beginner activity exclusions (Property 4)
    - **Property 4: Beginner activity exclusions**
    - Use `hypothesis` to generate beginner curriculum JSON containing writingParagraph or vocabLevel3 activities and verify the validator rejects them with specific messages identifying the forbidden activity type and session
    - **Validates: Requirements 2.4, 2.5**

  - [x] 1.6 Write property test: Activity structure completeness (Property 5)
    - **Property 5: Activity structure completeness**
    - Use `hypothesis` to generate activities with missing fields, `type` instead of `activityType`, invalid activityType values, inline content fields — for both beginner and standard levels
    - **Validates: Requirements 5.3, 5.4, 5.5, 5.6, 11.6**

  - [x] 1.7 Write property test: VocabList format enforcement (Property 6)
    - **Property 6: VocabList format enforcement**
    - Use `hypothesis` to generate vocab activities with uppercase strings, non-string elements, `words` field name
    - **Validates: Requirements 5.7, 5.8, 11.7**

  - [x] 1.8 Write property test: Flashcard vocabList consistency (Property 7)
    - **Property 7: Flashcard vocabList consistency**
    - Use `hypothesis` to generate sessions with mismatched viewFlashcards/speakFlashcards vocabLists
    - **Validates: Requirements 5.9, 11.8**

  - [x] 1.9 Write property test: Writing activity structure (Property 8)
    - **Property 8: Writing activity structure**
    - Use `hypothesis` to generate writingSentence/writingParagraph activities with missing or malformed data fields
    - **Validates: Requirements 11.11**

  - [x] 1.10 Write property test: Strip keys exclusion (Property 9)
    - **Property 9: Strip keys exclusion**
    - Use `hypothesis` to inject strip-keys at various depths in curriculum JSON and verify rejection
    - **Validates: Requirements 5.10, 11.10**

  - [x] 1.11 Write property test: Validator rejects invalid content with specific message (Property 10)
    - **Property 10: Validator rejects invalid content with specific message**
    - Use `hypothesis` to generate various invalid curriculum JSONs (both beginner and standard) and verify the validator always raises ValueError with a message identifying the specific violation
    - **Validates: Requirements 11.2**

- [x] 2. Verify shared API helpers module
  - [x] 2.1 Verify `api_helpers.py` has all required functions including `set_price`
    - Confirm root-level `api_helpers.py` includes: `get_token`, `create_curriculum`, `add_to_series`, `set_display_order`, `create_collection`, `create_series`, `add_series_to_collection`, `set_series_display_order`, `set_collection_display_order`, `set_price`
    - Verify `set_price(curriculum_id, price)` POSTs to `curriculum/setPrice` with correct params
    - Verify `create_curriculum` passes `language` and `userLanguage` as top-level body params
    - No changes needed if all functions are present and correct
    - _Requirements: 10.1, 10.2, 10.5, 14.3_

- [x] 3. Reuse existing tone assignment logic
  - [x] 3.1 Verify tone pre-assignment utility works for bilingual expansion
    - Confirm `tone_assigner.py` can assign description tones (6-tone palette) and farewell tones (5-tone palette) for the curriculum counts in each language pair
    - Enforce: no two adjacent curriculums in a series share the same description tone or farewell tone
    - Enforce: no two adjacent series in a collection share the same description tone
    - Enforce: no single tone exceeds 30% of descriptions per language pair
    - _Requirements: 8.1–8.7_

  - [x] 3.2 Write property test: Tone palette validity (Property 11)
    - **Property 11: Tone palette validity**
    - Use `hypothesis` to generate tone assignments and verify every description tone is one of the 6 valid types and every farewell tone is one of the 5 valid registers
    - **Validates: Requirements 8.1, 8.5**

  - [x] 3.3 Write property test: Tone adjacency constraint (Property 12)
    - **Property 12: Tone adjacency constraint**
    - Use `hypothesis` to generate sequences of tone assignments and verify no two adjacent entries share the same tone value (for both description and farewell tones within series, and series tones within collections)
    - **Validates: Requirements 8.2, 8.3, 8.6**

  - [x] 3.4 Write property test: Tone distribution cap (Property 13)
    - **Property 13: Tone distribution cap**
    - Use `hypothesis` to generate batches of description tone assignments and verify no single tone type exceeds 30% of the total
    - **Validates: Requirements 8.4**

- [x] 4. Checkpoint — Ensure shared modules are correct
  - Ensure all tests pass, ask the user if questions arise.

- [x] 5. Phase 1: zh-vi language pair (~79 curriculums: 31 beginner, 22 preintermediate, 26 intermediate)
  - [x] 5.1 Create `zh-vi/` directory structure and copy shared modules
    - Create `zh-vi/` directory with `validate_content.py` (level-aware), `api_helpers.py`
    - _Requirements: 13.3_

  - [x] 5.2 Create `zh-vi/orchestrator.py`
    - Create 3–4 collections with Chinese titles
    - Create 12–16 series with Chinese titles and Vietnamese topic labels where appropriate, descriptions ≤255 chars using assigned tones
    - Wire series to collections, set display orders for series and collections
    - Document all tone assignments (description + farewell) in comments
    - Collection descriptions: short informative category summaries (not persuasive copy)
    - Series descriptions: short persuasive hooks ≤255 chars using Tone_Palette
    - Log all collection/series IDs to stdout
    - _Requirements: 6.1–6.8, 8.1–8.4, 8.7_

  - [x] 5.3 Create beginner curriculum scripts for zh-vi (31 scripts)
    - Create `create_*.py` for each of the 31 beginner curriculums
    - Each script: hand-crafted Chinese user-facing text (persuasive copy with tone-assigned ALL-CAPS headline), Vietnamese reading passages, 12 vocabulary words (6 per learning session), 4 sessions with correct beginner activity order (no writingParagraph, no vocabLevel3)
    - Validate via `validate_content.py` with `level="beginner"` before upload
    - Set price to 19 via `set_price`
    - difficultyTags: `["beginner"]`
    - Simple reading passages with average sentence length under 15 words
    - Chinese session titles: 第1部分, 第2部分, 复习, 综合阅读
    - No vocabulary repeats within a series
    - Minimal curriculum titles (no series/collection name repetition, no difficulty level)
    - _Requirements: 1.1, 2.1–2.7, 4.1–4.8, 5.1–5.10, 7.1–7.8, 8.1–8.6, 9.1–9.5, 10.1–10.4, 14.1, 15.1–15.3_

  - [x] 5.4 Create preintermediate curriculum scripts for zh-vi (22 scripts)
    - Create `create_*.py` for each of the 22 preintermediate curriculums
    - Each script: hand-crafted Chinese user-facing text, Vietnamese reading passages, 18 vocabulary words (6 per learning session), 5 sessions with correct standard activity order (includes vocabLevel3, writingParagraph in final session)
    - Validate via `validate_content.py` with `level="standard"` before upload
    - Set price to 49 via `set_price`
    - difficultyTags: `["preintermediate"]`
    - Chinese session titles: 第1部分, 第2部分, 第3部分, 复习, 综合阅读
    - _Requirements: 1.1, 3.1–3.5, 4.1–4.8, 5.1–5.10, 7.1–7.8, 8.1–8.6, 9.1–9.5, 10.1–10.4, 14.2, 15.1–15.3_

  - [x] 5.5 Create intermediate curriculum scripts for zh-vi (26 scripts)
    - Create `create_*.py` for each of the 26 intermediate curriculums
    - Same structure as preintermediate but with difficultyTags: `["intermediate"]`
    - Validate via `validate_content.py` with `level="standard"` before upload
    - Set price to 49 via `set_price`
    - _Requirements: 1.1, 3.1–3.5, 4.1–4.8, 5.1–5.10, 7.1–7.8, 8.1–8.6, 9.1–9.5, 10.1–10.4, 14.2, 15.1–15.3_

  - [x] 5.6 Verify zh-vi phase and create README
    - Run duplicate check queries for all 79 curriculum titles
    - Verify each series has the expected number of curriculums with correct display orders
    - Verify language homogeneity via `curriculum_series_language_list` view (userLanguage=zh, language=vi)
    - Verify level gap compliance via `curriculum_series_level_gap` view
    - Verify all beginner curriculums priced at 19, all standard at 49
    - Create `zh-vi/README.md` with all collection IDs, series IDs, curriculum IDs, display orders, vocabulary lists, tone assignments, SQL verification queries, recreation instructions
    - Delete all `create_*.py` scripts after verification
    - _Requirements: 12.1–12.6_

- [x] 6. Checkpoint — zh-vi phase complete
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 7. Phase 2: zh-en language pair (~111 curriculums: 60 beginner, 23 preintermediate, 28 intermediate)
  - [ ] 7.1 Create `zh-en/` directory structure and copy shared modules
    - Create `zh-en/` directory with `validate_content.py` (level-aware), `api_helpers.py`
    - _Requirements: 13.3_

  - [ ] 7.2 Create `zh-en/orchestrator.py`
    - Create 4 collections with Chinese titles
    - Create 18–22 series with Chinese titles and English topic labels where appropriate, descriptions ≤255 chars using assigned tones
    - Wire series to collections, set display orders
    - Document all tone assignments in comments
    - _Requirements: 6.1–6.8, 8.1–8.4, 8.7_

  - [ ] 7.3 Create beginner curriculum scripts for zh-en (60 scripts)
    - Hand-crafted Chinese user-facing text, English reading passages, 12 vocab words, 4 sessions, beginner activity order
    - Validate with `level="beginner"`, set price to 19, difficultyTags: `["beginner"]`
    - Simple reading passages, Chinese session titles
    - _Requirements: 1.2, 2.1–2.7, 4.1–4.8, 5.1–5.10, 7.1–7.8, 8.1–8.6, 9.1–9.5, 10.1–10.4, 14.1, 15.1–15.3_

  - [ ] 7.4 Create preintermediate curriculum scripts for zh-en (23 scripts)
    - Hand-crafted Chinese user-facing text, English reading passages, 18 vocab words, 5 sessions, standard activity order
    - Validate with `level="standard"`, set price to 49, difficultyTags: `["preintermediate"]`
    - _Requirements: 1.2, 3.1–3.5, 4.1–4.8, 5.1–5.10, 7.1–7.8, 8.1–8.6, 9.1–9.5, 10.1–10.4, 14.2, 15.1–15.3_

  - [ ] 7.5 Create intermediate curriculum scripts for zh-en (28 scripts)
    - Same structure as preintermediate but with difficultyTags: `["intermediate"]`
    - Validate with `level="standard"`, set price to 49
    - _Requirements: 1.2, 3.1–3.5, 4.1–4.8, 5.1–5.10, 7.1–7.8, 8.1–8.6, 9.1–9.5, 10.1–10.4, 14.2, 15.1–15.3_

  - [ ] 7.6 Verify zh-en phase and create README
    - Run duplicate check queries for all 111 curriculum titles
    - Verify series counts, display orders, language homogeneity (userLanguage=zh, language=en), level gap
    - Verify pricing: beginner=19, standard=49
    - Create `zh-en/README.md`, delete all `create_*.py` scripts
    - _Requirements: 12.1–12.6_

- [ ] 8. Checkpoint — zh-en phase complete
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 9. Phase 3: de-en language pair (~149 curriculums: 59 beginner, 52 preintermediate, 38 intermediate)
  - [ ] 9.1 Create `de-en/` directory structure and copy shared modules
    - Create `de-en/` directory with `validate_content.py` (level-aware), `api_helpers.py`
    - _Requirements: 13.3_

  - [ ] 9.2 Create `de-en/orchestrator.py`
    - Create 4–5 collections with German titles
    - Create 25–30 series with German titles and English topic labels where appropriate, descriptions ≤255 chars using assigned tones
    - Wire series to collections, set display orders
    - Document all tone assignments in comments
    - _Requirements: 6.1–6.8, 8.1–8.4, 8.7_

  - [ ] 9.3 Create beginner curriculum scripts for de-en (59 scripts)
    - Hand-crafted German user-facing text, English reading passages, 12 vocab words, 4 sessions, beginner activity order
    - Validate with `level="beginner"`, set price to 19, difficultyTags: `["beginner"]`
    - Simple reading passages, German session titles: Teil 1, Teil 2, Wiederholung, Abschlusslektüre
    - _Requirements: 1.3, 2.1–2.7, 4.1–4.8, 5.1–5.10, 7.1–7.8, 8.1–8.6, 9.1–9.5, 10.1–10.4, 14.1, 15.1–15.3_

  - [ ] 9.4 Create preintermediate curriculum scripts for de-en (52 scripts)
    - Hand-crafted German user-facing text, English reading passages, 18 vocab words, 5 sessions, standard activity order
    - Validate with `level="standard"`, set price to 49, difficultyTags: `["preintermediate"]`
    - German session titles: Teil 1, Teil 2, Teil 3, Wiederholung, Abschlusslektüre
    - _Requirements: 1.3, 3.1–3.5, 4.1–4.8, 5.1–5.10, 7.1–7.8, 8.1–8.6, 9.1–9.5, 10.1–10.4, 14.2, 15.1–15.3_

  - [ ] 9.5 Create intermediate curriculum scripts for de-en (38 scripts)
    - Same structure as preintermediate but with difficultyTags: `["intermediate"]`
    - Validate with `level="standard"`, set price to 49
    - _Requirements: 1.3, 3.1–3.5, 4.1–4.8, 5.1–5.10, 7.1–7.8, 8.1–8.6, 9.1–9.5, 10.1–10.4, 14.2, 15.1–15.3_

  - [ ] 9.6 Verify de-en phase and create README
    - Run duplicate check queries for all 149 curriculum titles
    - Verify series counts, display orders, language homogeneity (userLanguage=de, language=en), level gap
    - Verify pricing: beginner=19, standard=49
    - Create `de-en/README.md`, delete all `create_*.py` scripts
    - _Requirements: 12.1–12.6_

- [ ] 10. Checkpoint — de-en phase complete
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 11. Phase 4: de-vi language pair (~155 curriculums: 60 beginner, 56 preintermediate, 39 intermediate)
  - [ ] 11.1 Create `de-vi/` directory structure and copy shared modules
    - Create `de-vi/` directory with `validate_content.py` (level-aware), `api_helpers.py`
    - _Requirements: 13.3_

  - [ ] 11.2 Create `de-vi/orchestrator.py`
    - Create 4–5 collections with German titles
    - Create 25–31 series with German titles and Vietnamese topic labels where appropriate, descriptions ≤255 chars using assigned tones
    - Wire series to collections, set display orders
    - Document all tone assignments in comments
    - _Requirements: 6.1–6.8, 8.1–8.4, 8.7_

  - [ ] 11.3 Create beginner curriculum scripts for de-vi (60 scripts)
    - Hand-crafted German user-facing text, Vietnamese reading passages, 12 vocab words, 4 sessions, beginner activity order
    - Validate with `level="beginner"`, set price to 19, difficultyTags: `["beginner"]`
    - German session titles: Teil 1, Teil 2, Wiederholung, Abschlusslektüre
    - _Requirements: 1.4, 2.1–2.7, 4.1–4.8, 5.1–5.10, 7.1–7.8, 8.1–8.6, 9.1–9.5, 10.1–10.4, 14.1, 15.1–15.3_

  - [ ] 11.4 Create preintermediate curriculum scripts for de-vi (56 scripts)
    - Hand-crafted German user-facing text, Vietnamese reading passages, 18 vocab words, 5 sessions, standard activity order
    - Validate with `level="standard"`, set price to 49, difficultyTags: `["preintermediate"]`
    - _Requirements: 1.4, 3.1–3.5, 4.1–4.8, 5.1–5.10, 7.1–7.8, 8.1–8.6, 9.1–9.5, 10.1–10.4, 14.2, 15.1–15.3_

  - [ ] 11.5 Create intermediate curriculum scripts for de-vi (39 scripts)
    - Same structure as preintermediate but with difficultyTags: `["intermediate"]`
    - Validate with `level="standard"`, set price to 49
    - _Requirements: 1.4, 3.1–3.5, 4.1–4.8, 5.1–5.10, 7.1–7.8, 8.1–8.6, 9.1–9.5, 10.1–10.4, 14.2, 15.1–15.3_

  - [ ] 11.6 Verify de-vi phase and create README
    - Run duplicate check queries for all 155 curriculum titles
    - Verify series counts, display orders, language homogeneity (userLanguage=de, language=vi), level gap
    - Verify pricing: beginner=19, standard=49
    - Create `de-vi/README.md`, delete all `create_*.py` scripts
    - _Requirements: 12.1–12.6_

- [ ] 12. Checkpoint — de-vi phase complete
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 13. Phase 5: fr-en language pair (~138 curriculums: 58 beginner, 51 preintermediate, 29 intermediate)
  - [ ] 13.1 Create `fr-en/` directory structure and copy shared modules
    - Create `fr-en/` directory with `validate_content.py` (level-aware), `api_helpers.py`
    - _Requirements: 13.3_

  - [ ] 13.2 Create `fr-en/orchestrator.py`
    - Create 4–5 collections with French titles
    - Create 22–28 series with French titles and English topic labels where appropriate, descriptions ≤255 chars using assigned tones
    - Wire series to collections, set display orders
    - Document all tone assignments in comments
    - _Requirements: 6.1–6.8, 8.1–8.4, 8.7_

  - [ ] 13.3 Create beginner curriculum scripts for fr-en (58 scripts)
    - Hand-crafted French user-facing text, English reading passages, 12 vocab words, 4 sessions, beginner activity order
    - Validate with `level="beginner"`, set price to 19, difficultyTags: `["beginner"]`
    - Simple reading passages, French session titles: Partie 1, Partie 2, Révision, Lecture finale
    - _Requirements: 1.5, 2.1–2.7, 4.1–4.8, 5.1–5.10, 7.1–7.8, 8.1–8.6, 9.1–9.5, 10.1–10.4, 14.1, 15.1–15.3_

  - [ ] 13.4 Create preintermediate curriculum scripts for fr-en (51 scripts)
    - Hand-crafted French user-facing text, English reading passages, 18 vocab words, 5 sessions, standard activity order
    - Validate with `level="standard"`, set price to 49, difficultyTags: `["preintermediate"]`
    - French session titles: Partie 1, Partie 2, Partie 3, Révision, Lecture finale
    - _Requirements: 1.5, 3.1–3.5, 4.1–4.8, 5.1–5.10, 7.1–7.8, 8.1–8.6, 9.1–9.5, 10.1–10.4, 14.2, 15.1–15.3_

  - [ ] 13.5 Create intermediate curriculum scripts for fr-en (29 scripts)
    - Same structure as preintermediate but with difficultyTags: `["intermediate"]`
    - Validate with `level="standard"`, set price to 49
    - _Requirements: 1.5, 3.1–3.5, 4.1–4.8, 5.1–5.10, 7.1–7.8, 8.1–8.6, 9.1–9.5, 10.1–10.4, 14.2, 15.1–15.3_

  - [ ] 13.6 Verify fr-en phase and create README
    - Run duplicate check queries for all 138 curriculum titles
    - Verify series counts, display orders, language homogeneity (userLanguage=fr, language=en), level gap
    - Verify pricing: beginner=19, standard=49
    - Create `fr-en/README.md`, delete all `create_*.py` scripts
    - _Requirements: 12.1–12.6_

- [ ] 14. Checkpoint — fr-en phase complete
  - Ensure all tests pass, ask the user if questions arise.


- [ ] 15. Phase 6: fr-vi language pair (~141 curriculums: 60 beginner, 55 preintermediate, 26 intermediate)
  - [ ] 15.1 Create `fr-vi/` directory structure and copy shared modules
    - Create `fr-vi/` directory with `validate_content.py` (level-aware), `api_helpers.py`
    - _Requirements: 13.3_

  - [ ] 15.2 Create `fr-vi/orchestrator.py`
    - Create 4–5 collections with French titles
    - Create 23–28 series with French titles and Vietnamese topic labels where appropriate, descriptions ≤255 chars using assigned tones
    - Wire series to collections, set display orders
    - Document all tone assignments in comments
    - _Requirements: 6.1–6.8, 8.1–8.4, 8.7_

  - [ ] 15.3 Create beginner curriculum scripts for fr-vi (60 scripts)
    - Hand-crafted French user-facing text, Vietnamese reading passages, 12 vocab words, 4 sessions, beginner activity order
    - Validate with `level="beginner"`, set price to 19, difficultyTags: `["beginner"]`
    - French session titles: Partie 1, Partie 2, Révision, Lecture finale
    - _Requirements: 1.6, 2.1–2.7, 4.1–4.8, 5.1–5.10, 7.1–7.8, 8.1–8.6, 9.1–9.5, 10.1–10.4, 14.1, 15.1–15.3_

  - [ ] 15.4 Create preintermediate curriculum scripts for fr-vi (55 scripts)
    - Hand-crafted French user-facing text, Vietnamese reading passages, 18 vocab words, 5 sessions, standard activity order
    - Validate with `level="standard"`, set price to 49, difficultyTags: `["preintermediate"]`
    - French session titles: Partie 1, Partie 2, Partie 3, Révision, Lecture finale
    - _Requirements: 1.6, 3.1–3.5, 4.1–4.8, 5.1–5.10, 7.1–7.8, 8.1–8.6, 9.1–9.5, 10.1–10.4, 14.2, 15.1–15.3_

  - [ ] 15.5 Create intermediate curriculum scripts for fr-vi (26 scripts)
    - Same structure as preintermediate but with difficultyTags: `["intermediate"]`
    - Validate with `level="standard"`, set price to 49
    - _Requirements: 1.6, 3.1–3.5, 4.1–4.8, 5.1–5.10, 7.1–7.8, 8.1–8.6, 9.1–9.5, 10.1–10.4, 14.2, 15.1–15.3_

  - [ ] 15.6 Verify fr-vi phase and create README
    - Run duplicate check queries for all 141 curriculum titles
    - Verify series counts, display orders, language homogeneity (userLanguage=fr, language=vi), level gap
    - Verify pricing: beginner=19, standard=49
    - Create `fr-vi/README.md`, delete all `create_*.py` scripts
    - _Requirements: 12.1–12.6_

- [ ] 16. Final checkpoint — All phases complete
  - Ensure all tests pass, ask the user if questions arise.
  - Verify total curriculum count across all 6 language pairs (~773)
  - Verify all READMEs are in place and all creation scripts are deleted
  - Verify parity with en-vi reference pair: ≥60 beginner, ≥59 preintermediate, ≥63 intermediate per pair

## Notes

- Tasks marked with `*` are optional and can be skipped for faster MVP
- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation between language pair phases
- Property tests validate the content validator (Properties 1–10) and tone assigner (Properties 11–13) from the design
- The `validate_content.py` is extended with level-aware support and copied to each language pair directory
- The root-level `api_helpers.py` already has `set_price` — no changes needed, just copy to each pair directory
- Phased execution order: zh-vi → zh-en → de-en → de-vi → fr-en → fr-vi (Chinese pairs first, then German, then French)
- All curriculum content must be hand-crafted — no template-based generation
- Beginner curriculums: 4 sessions, 12 words, no writingParagraph/vocabLevel3, price 19
- Standard curriculums (preintermediate/intermediate): 5 sessions, 18 words, full activity set, price 49
- Within each phase, create beginner curriculums first, then preintermediate, then intermediate
- Session titles by user language: zh (第1部分, 复习, 综合阅读), de (Teil 1, Wiederholung, Abschlusslektüre), fr (Partie 1, Révision, Lecture finale)