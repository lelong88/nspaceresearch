# Implementation Plan: Fiction Novel — New Genre (Mystery/Detective)

## Overview

Create "The Silent Clocktower" (Tháp Đồng Hồ Im Lặng), a 10-chapter mystery novel curriculum series for the Vietnamese-English platform. Implementation follows the same structural template as "The Little Bookshop by the Sea" — 10 Python content modules, a validation script, a creation script, and a README. All files go in `original-novels/the-silent-clocktower/`.

## Tasks

- [x] 1. Create the project directory and first content module as the structural template
  - [x] 1.1 Create `original-novels/the-silent-clocktower/chapter1_content.py` with a complete `get_curriculum()` function
    - Define the full curriculum dict for Chapter 1: "Thị Trấn Trên Đồi (The Town on the Hill)" — setup chapter introducing Mai, the mountain town, and the stopped clocktower
    - Include: title (bilingual format), language "en", userLanguage "vi", level "preintermediate", audioSpeed -0.2, Vietnamese preview (~150 words), Vietnamese description
    - Include 15 A2-B1 vocabulary words with Vietnamese translations and example sentences, 3 assigned per passage
    - Include 5 reading passages (~150–200 words each) in simple English prose, naturally incorporating assigned vocab words
    - Include 6 sessions: sessions 1–5 with viewFlashcards (3 words) + reading + readAlong; session 6 with viewFlashcards (all 15 words) + readAlong (all 5 passages concatenated)
    - Follow all activity title/description format conventions (Flashcards:, Đọc:, Nghe:, Ôn tập, etc.)
    - Ensure no strip-keys are present
    - _Requirements: 1.1, 1.2, 1.3, 1.7, 2.1–2.6, 3.1–3.6, 4.1–4.9, 5.1–5.10, 6.1, 6.2, 10.1–10.7_

- [x] 2. Create content modules for chapters 2–5 (rising action and investigation)
  - [x] 2.1 Create `chapter2_content.py` — Chapter 2: setup continues, Mai meets key townspeople, learns about the clockmaker
    - Same structural template as chapter 1, new plot content, 15 new unique vocab words
    - _Requirements: 1.1, 1.4, 1.5, 2.1–2.6, 3.1–3.6, 4.1–4.9, 5.1–5.10, 6.1, 6.2, 10.1–10.7_
  - [x] 2.2 Create `chapter3_content.py` — Chapter 3: investigation begins, first clues discovered
    - _Requirements: 1.1, 1.5, 2.1–2.6, 3.1–3.6, 4.1–4.9, 5.1–5.10, 6.1, 6.2, 10.1–10.7_
  - [x] 2.3 Create `chapter4_content.py` — Chapter 4: deeper investigation, new suspects or leads
    - _Requirements: 1.1, 1.5, 2.1–2.6, 3.1–3.6, 4.1–4.9, 5.1–5.10, 6.1, 6.2, 10.1–10.7_
  - [x] 2.4 Create `chapter5_content.py` — Chapter 5: mid-story twist or complication
    - _Requirements: 1.1, 1.5, 2.1–2.6, 3.1–3.6, 4.1–4.9, 5.1–5.10, 6.1, 6.2, 10.1–10.7_

- [x] 3. Create content modules for chapters 6–10 (climax and resolution)
  - [x] 3.1 Create `chapter6_content.py` — Chapter 6: investigation intensifies
    - _Requirements: 1.1, 1.5, 2.1–2.6, 3.1–3.6, 4.1–4.9, 5.1–5.10, 6.1, 6.2, 10.1–10.7_
  - [x] 3.2 Create `chapter7_content.py` — Chapter 7: final investigation leads before climax
    - _Requirements: 1.1, 1.5, 2.1–2.6, 3.1–3.6, 4.1–4.9, 5.1–5.10, 6.1, 6.2, 10.1–10.7_
  - [x] 3.3 Create `chapter8_content.py` — Chapter 8: climax begins, major revelation
    - _Requirements: 1.1, 1.5, 2.1–2.6, 3.1–3.6, 4.1–4.9, 5.1–5.10, 6.1, 6.2, 10.1–10.7_
  - [x] 3.4 Create `chapter9_content.py` — Chapter 9: climax continues, confrontation or key discovery
    - _Requirements: 1.1, 1.5, 1.6, 2.1–2.6, 3.1–3.6, 4.1–4.9, 5.1–5.10, 6.1, 6.2, 10.1–10.7_
  - [x] 3.5 Create `chapter10_content.py` — Chapter 10: resolution, mystery solved, all plot threads resolved
    - _Requirements: 1.1, 1.5, 1.6, 2.1–2.6, 3.1–3.6, 4.1–4.9, 5.1–5.10, 6.1, 6.2, 10.1–10.7_

- [x] 4. Checkpoint — Verify all 10 content modules
  - Ensure all 10 `chapterN_content.py` files exist and each exports a `get_curriculum()` function returning a valid dict. Ensure no vocabulary word is repeated across any two chapters (150 unique words total). Ask the user if questions arise.

- [x] 5. Create the validation script
  - [x] 5.1 Create `original-novels/the-silent-clocktower/validate_content.py` implementing all 14 correctness properties
    - Import all 10 content modules dynamically
    - Implement checks for: session count (P1), vocab counts (P2), vocab in passage text (P3), no cross-chapter vocab repeats (P4), vocab completeness (P5), readAlong = reading text (P6), session 6 full text (P7), audioSpeed (P8), passage word count (P9), title format (P10), session titles (P11), activity title formats (P12), Vietnamese metadata and language fields (P13), no strip-keys (P14)
    - Report violations in format: `FAIL [Chapter N, Session M, Activity type]: description`
    - Exit with non-zero status on any violation
    - Print summary: `All 14 properties verified across 10 chapters. 0 violations.` on success
    - _Requirements: 7.1–7.14_

  - [x] 5.2 Write property checks for session structure (Property 1)
    - **Property 1: Session structure is correct**
    - **Validates: Requirements 4.1, 4.2, 4.3**

  - [x] 5.3 Write property checks for vocabulary word counts (Property 2)
    - **Property 2: Vocabulary word counts are correct**
    - **Validates: Requirements 2.2, 3.1, 4.4, 4.5**

  - [x] 5.4 Write property checks for vocab appearing in passage text (Property 3)
    - **Property 3: Vocabulary words appear in their assigned passage**
    - **Validates: Requirements 2.3, 10.3**

  - [x] 5.5 Write property checks for no cross-chapter vocab repeats (Property 4)
    - **Property 4: No vocabulary word is repeated across chapters**
    - **Validates: Requirements 3.3**

  - [x] 5.6 Write property checks for vocab data completeness (Property 5)
    - **Property 5: Vocabulary words have complete data**
    - **Validates: Requirements 3.5, 3.6**

  - [x] 5.7 Write property checks for readAlong matching reading text (Property 6)
    - **Property 6: readAlong text matches reading text in sessions 1–5**
    - **Validates: Requirements 4.7**

  - [x] 5.8 Write property checks for session 6 full chapter text (Property 7)
    - **Property 7: Session 6 readAlong contains the full chapter text**
    - **Validates: Requirements 4.8**

  - [x] 5.9 Write property checks for audioSpeed (Property 8)
    - **Property 8: audioSpeed is set correctly**
    - **Validates: Requirements 4.9**

  - [x] 5.10 Write property checks for passage word count range (Property 9)
    - **Property 9: Passage word count is in range**
    - **Validates: Requirements 2.4, 10.4**

  - [x] 5.11 Write property checks for curriculum title format (Property 10)
    - **Property 10: Curriculum title follows the bilingual format**
    - **Validates: Requirements 2.5, 5.1**

  - [x] 5.12 Write property checks for session titles (Property 11)
    - **Property 11: Session titles are correct**
    - **Validates: Requirements 5.4, 5.5**

  - [x] 5.13 Write property checks for activity title/description formats (Property 12)
    - **Property 12: Activity titles and descriptions follow format conventions**
    - **Validates: Requirements 5.6, 5.7, 5.8, 5.9, 7.9**

  - [x] 5.14 Write property checks for Vietnamese metadata and language fields (Property 13)
    - **Property 13: Vietnamese metadata and language fields**
    - **Validates: Requirements 5.2, 5.3, 5.10, 8.4**

  - [x] 5.15 Write property checks for no strip-keys present (Property 14)
    - **Property 14: No auto-generated platform keys present**
    - **Validates: Requirements 6.2, 7.8**

- [x] 6. Checkpoint — Run validation and fix any violations
  - Run `python validate_content.py` from `original-novels/the-silent-clocktower/`. Fix any violations in the content modules. Ensure all tests pass, ask the user if questions arise.

- [x] 7. Create the creation script and README
  - [x] 7.1 Create `original-novels/the-silent-clocktower/create_all_chapters.py`
    - Authenticate via `firebase_token.get_firebase_id_token(UID)` with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`
    - Import all 10 content modules and upload each via `curriculum/create` to `https://helloapi.step.is/curriculum/create`
    - Create series via `curriculum-series/create` with Vietnamese+English title
    - Add each curriculum to series via `curriculum-series/addCurriculum` with display_order 1–10
    - Look up Fiction collection by title via `curriculum-collection/listAll`
    - Attach series to Fiction collection via `curriculum-collection/addSeriesToCollection`
    - Set series to public via `curriculum-series/setIsPublic`
    - No hardcoded IDs — all IDs from API responses or runtime lookups
    - Handle errors: abort on auth failure, abort on upload failure with response body, report already-uploaded IDs on series failure
    - _Requirements: 6.3–6.7, 8.1–8.6_

  - [x] 7.2 Create `original-novels/the-silent-clocktower/README.md`
    - Document: how content was created, series ID placeholder, Fiction collection reference, SQL queries to find chapters in DB, novel summary, enough context to recreate source materials
    - _Requirements: 9.2–9.4_

- [x] 8. Final checkpoint — Full review
  - Ensure all files are in place: 10 content modules, validate_content.py, create_all_chapters.py, README.md. Ensure validation passes with 0 violations. Ask the user if questions arise.

## Notes

- Tasks marked with `*` are optional and can be skipped — the validation checks are all implemented in task 5.1; the sub-tasks 5.2–5.15 are for individual property test refinement
- All files go in `original-novels/the-silent-clocktower/`
- No build system or test framework — scripts run directly with `python`
- The reference implementation is "The Little Bookshop by the Sea" (series `n4y9zm3v`)
- 150 unique vocabulary words total across all 10 chapters (no repeats)
- Source files will be deleted after successful upload, leaving only README.md
