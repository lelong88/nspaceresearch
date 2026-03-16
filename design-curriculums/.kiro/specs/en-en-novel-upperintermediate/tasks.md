# Implementation Plan: en-en Novel — Upper-Intermediate Science Fiction

## Overview

Create a 20-chapter science fiction novel curriculum series for English-only (en-en) upper-intermediate (B2) learners. Implementation follows the structural template of "The Last Light of Alder House" (series ID: 70b5bb22) — 20 Python content modules, a validation script, a creation script, and a README. All files go in `original-novels/[novel-folder-name]/` (folder name TBD based on novel title). Key differences from Silent Clocktower: 20 chapters (not 10), en-en (no Vietnamese), B2 level, 4 vocab words per session (not 3), 20 per chapter (not 15), plain string vocabList (no translation objects).

## Tasks

- [x] 1. Create the project directory and first content module as the structural template
  - [x] 1.1 Create `original-novels/[novel-folder-name]/chapter1_content.py` with a complete `get_curriculum()` function
    - Choose a novel title and folder name (science fiction / near-future genre, distinct from Alder House mystery/gothic and Silent Clocktower mystery/detective)
    - Define the protagonist, setting, and opening premise for the 20-chapter arc
    - Define the full curriculum dict for Chapter 1 (setup chapter introducing protagonist, world, and central premise)
    - Include: English-only title following format "[Novel Title] — Chapter 1: [Chapter Title]", language "en", userLanguage "en", level "upperintermediate", audioSpeed -0.2, English preview (~150 words), English description
    - Include 20 B2-level vocabulary words as plain strings in vocabList arrays (no translation objects, no example sentences), 4 assigned per passage
    - Include 5 reading passages (~150–290 words each) in B2-level English prose with varied sentence structures, naturally incorporating assigned vocab words
    - Include 6 sessions: sessions 1–5 with viewFlashcards (4 words) + reading + readAlong; session 6 with viewFlashcards (all 20 words) + readAlong (all 5 passages concatenated with \n\n)
    - Session titles: "Session 1" through "Session 5", "Review"
    - Activity titles: "Flashcards: [topic]", "Read: [topic]", "Listen: [topic]", session 6 readAlong "Listen: Full Chapter"
    - Ensure audioSpeed = -0.2 on all activities, no strip-keys present
    - _Requirements: 1.1, 1.2, 1.3, 1.5, 1.7, 2.1–2.6, 3.1–3.6, 4.1–4.9, 5.1–5.11, 6.1, 6.2, 10.1–10.7, 11.1–11.5, 12.1, 12.2_

- [x] 2. Create content modules for chapters 2–10 (setup and rising action)
  - [x] 2.1 Create `chapter2_content.py` — Chapter 2: setup continues, protagonist explores the world, meets key supporting characters
    - Same structural template as chapter 1, new plot content, 20 new unique B2 vocab words (no repeats from chapter 1)
    - _Requirements: 1.1, 1.4, 1.5, 1.7, 2.1–2.6, 3.1–3.6, 4.1–4.9, 5.1–5.11, 6.1, 6.2, 10.1–10.7, 11.1–11.5_
  - [x] 2.2 Create `chapter3_content.py` — Chapter 3: setup deepens, central conflict begins to emerge
    - _Requirements: 1.1, 1.4, 1.5, 1.7, 2.1–2.6, 3.1–3.6, 4.1–4.9, 5.1–5.11, 6.1, 6.2, 10.1–10.7, 11.1–11.5_
  - [x] 2.3 Create `chapter4_content.py` — Chapter 4: setup concludes, stakes are established
    - _Requirements: 1.1, 1.4, 1.5, 1.7, 2.1–2.6, 3.1–3.6, 4.1–4.9, 5.1–5.11, 6.1, 6.2, 10.1–10.7, 11.1–11.5_
  - [x] 2.4 Create `chapter5_content.py` — Chapter 5: rising action begins, protagonist takes first major action
    - _Requirements: 1.1, 1.5, 1.7, 2.1–2.6, 3.1–3.6, 4.1–4.9, 5.1–5.11, 6.1, 6.2, 10.1–10.7, 11.1–11.5_
  - [x] 2.5 Create `chapter6_content.py` — Chapter 6: rising action, complications and new discoveries
    - _Requirements: 1.1, 1.5, 1.7, 2.1–2.6, 3.1–3.6, 4.1–4.9, 5.1–5.11, 6.1, 6.2, 10.1–10.7, 11.1–11.5_
  - [x] 2.6 Create `chapter7_content.py` — Chapter 7: rising action, alliances and obstacles
    - _Requirements: 1.1, 1.5, 1.7, 2.1–2.6, 3.1–3.6, 4.1–4.9, 5.1–5.11, 6.1, 6.2, 10.1–10.7, 11.1–11.5_
  - [x] 2.7 Create `chapter8_content.py` — Chapter 8: rising action intensifies, major setback or revelation
    - _Requirements: 1.1, 1.5, 1.7, 2.1–2.6, 3.1–3.6, 4.1–4.9, 5.1–5.11, 6.1, 6.2, 10.1–10.7, 11.1–11.5_
  - [x] 2.8 Create `chapter9_content.py` — Chapter 9: rising action peaks, tension builds toward midpoint
    - _Requirements: 1.1, 1.5, 1.7, 2.1–2.6, 3.1–3.6, 4.1–4.9, 5.1–5.11, 6.1, 6.2, 10.1–10.7, 11.1–11.5_
  - [x] 2.9 Create `chapter10_content.py` — Chapter 10: final rising action chapter, sets up the midpoint shift
    - _Requirements: 1.1, 1.5, 1.7, 2.1–2.6, 3.1–3.6, 4.1–4.9, 5.1–5.11, 6.1, 6.2, 10.1–10.7, 11.1–11.5_

- [x] 3. Create content modules for chapters 11–20 (midpoint, escalation, climax, resolution)
  - [x] 3.1 Create `chapter11_content.py` — Chapter 11: midpoint shift, a major change in direction or understanding
    - _Requirements: 1.1, 1.5, 1.7, 2.1–2.6, 3.1–3.6, 4.1–4.9, 5.1–5.11, 6.1, 6.2, 10.1–10.7, 11.1–11.5_
  - [x] 3.2 Create `chapter12_content.py` — Chapter 12: midpoint continues, consequences of the shift unfold
    - _Requirements: 1.1, 1.5, 1.7, 2.1–2.6, 3.1–3.6, 4.1–4.9, 5.1–5.11, 6.1, 6.2, 10.1–10.7, 11.1–11.5_
  - [x] 3.3 Create `chapter13_content.py` — Chapter 13: midpoint concludes, new trajectory established
    - _Requirements: 1.1, 1.5, 1.7, 2.1–2.6, 3.1–3.6, 4.1–4.9, 5.1–5.11, 6.1, 6.2, 10.1–10.7, 11.1–11.5_
  - [x] 3.4 Create `chapter14_content.py` — Chapter 14: escalation begins, stakes rise dramatically
    - _Requirements: 1.1, 1.5, 1.7, 2.1–2.6, 3.1–3.6, 4.1–4.9, 5.1–5.11, 6.1, 6.2, 10.1–10.7, 11.1–11.5_
  - [x] 3.5 Create `chapter15_content.py` — Chapter 15: escalation, protagonist faces critical choices
    - _Requirements: 1.1, 1.5, 1.7, 2.1–2.6, 3.1–3.6, 4.1–4.9, 5.1–5.11, 6.1, 6.2, 10.1–10.7, 11.1–11.5_
  - [x] 3.6 Create `chapter16_content.py` — Chapter 16: escalation, allies tested, pressure mounts
    - _Requirements: 1.1, 1.5, 1.7, 2.1–2.6, 3.1–3.6, 4.1–4.9, 5.1–5.11, 6.1, 6.2, 10.1–10.7, 11.1–11.5_
  - [x] 3.7 Create `chapter17_content.py` — Chapter 17: final escalation, point of no return
    - _Requirements: 1.1, 1.5, 1.7, 2.1–2.6, 3.1–3.6, 4.1–4.9, 5.1–5.11, 6.1, 6.2, 10.1–10.7, 11.1–11.5_
  - [x] 3.8 Create `chapter18_content.py` — Chapter 18: climax begins, major confrontation or crisis
    - _Requirements: 1.1, 1.5, 1.7, 2.1–2.6, 3.1–3.6, 4.1–4.9, 5.1–5.11, 6.1, 6.2, 10.1–10.7, 11.1–11.5_
  - [x] 3.9 Create `chapter19_content.py` — Chapter 19: climax continues, decisive action and turning point
    - _Requirements: 1.1, 1.5, 1.6, 1.7, 2.1–2.6, 3.1–3.6, 4.1–4.9, 5.1–5.11, 6.1, 6.2, 10.1–10.7, 11.1–11.5_
  - [x] 3.10 Create `chapter20_content.py` — Chapter 20: resolution, all major plot threads resolved, satisfying conclusion
    - _Requirements: 1.1, 1.5, 1.6, 1.7, 2.1–2.6, 3.1–3.6, 4.1–4.9, 5.1–5.11, 6.1, 6.2, 10.1–10.7, 11.1–11.5_

- [x] 4. Checkpoint — Verify all 20 content modules
  - Ensure all 20 `chapterN_content.py` files exist and each exports a `get_curriculum()` function returning a valid dict
  - Ensure no vocabulary word is repeated across any two chapters (400 unique words total)
  - Ensure all vocabList entries are plain strings (no translation objects)
  - Ensure all titles, previews, descriptions, and session titles are English-only (no Vietnamese/Chinese)
  - Ensure all session titles follow "Session N" / "Review" convention
  - Ask the user if questions arise

- [x] 5. Create the validation script with all 14 correctness properties
  - [x] 5.1 Create `original-novels/[novel-folder-name]/validate_content.py` implementing all 14 correctness properties
    - Import all 20 content modules dynamically
    - Implement checks for: session count (P1), vocab counts (P2), vocab in passage text (P3), no cross-chapter vocab repeats (P4), vocabList plain strings (P5), readAlong = reading text (P6), session 6 full text (P7), audioSpeed (P8), passage word count (P9), English-only title format (P10), session titles (P11), activity title/description formats (P12), English-only metadata and language fields (P13), no strip-keys (P14)
    - Report violations in format: `FAIL [Chapter N, Session M, Activity type]: description`
    - Exit with non-zero status on any violation
    - Print summary: `All 14 properties verified across 20 chapters. 0 violations.` on success
    - _Requirements: 7.1–7.14_

  - [x] 5.2 Write property check for session structure (Property 1)
    - **Property 1: Session structure is correct**
    - **Validates: Requirements 4.1, 4.2, 4.3, 7.1, 7.2, 7.3**

  - [x] 5.3 Write property check for vocabulary word counts (Property 2)
    - **Property 2: Vocabulary word counts are correct**
    - **Validates: Requirements 2.2, 3.1, 4.4, 4.5, 7.4, 7.5**

  - [x] 5.4 Write property check for vocab appearing in passage text (Property 3)
    - **Property 3: Vocabulary words appear in their assigned passage**
    - **Validates: Requirements 2.3, 7.7, 10.3**

  - [x] 5.5 Write property check for no cross-chapter vocab repeats (Property 4)
    - **Property 4: No vocabulary word is repeated across chapters**
    - **Validates: Requirements 3.3, 7.12**

  - [x] 5.6 Write property check for vocabList plain strings (Property 5)
    - **Property 5: VocabList contains plain strings only**
    - **Validates: Requirements 3.5, 3.6, 11.5**

  - [x] 5.7 Write property check for readAlong matching reading text (Property 6)
    - **Property 6: readAlong text matches reading text in sessions 1–5**
    - **Validates: Requirements 4.7**

  - [x] 5.8 Write property check for session 6 full chapter text (Property 7)
    - **Property 7: Session 6 readAlong contains the full chapter text**
    - **Validates: Requirements 4.8, 7.6**

  - [x] 5.9 Write property check for audioSpeed (Property 8)
    - **Property 8: audioSpeed is set correctly on all activities**
    - **Validates: Requirements 4.9, 7.11**

  - [x] 5.10 Write property check for passage word count range (Property 9)
    - **Property 9: Passage word count is in range**
    - **Validates: Requirements 2.4, 10.4**

  - [x] 5.11 Write property check for English-only title format (Property 10)
    - **Property 10: Curriculum title follows English-only format**
    - **Validates: Requirements 2.5, 5.1, 8.8**

  - [x] 5.12 Write property check for session titles (Property 11)
    - **Property 11: Session titles are correct**
    - **Validates: Requirements 5.4, 5.5**

  - [x] 5.13 Write property check for activity title/description formats (Property 12)
    - **Property 12: Activity titles, descriptions, and required fields**
    - **Validates: Requirements 5.6, 5.7, 5.8, 5.9, 7.9, 11.4**

  - [x] 5.14 Write property check for English-only metadata and language fields (Property 13)
    - **Property 13: English-only metadata and language fields**
    - **Validates: Requirements 5.2, 5.3, 5.10, 5.11, 7.10, 7.13, 8.6**

  - [x] 5.15 Write property check for no strip-keys present (Property 14)
    - **Property 14: No auto-generated platform keys present**
    - **Validates: Requirements 6.2, 7.8**

- [x] 6. Checkpoint — Run validation and fix any violations
  - Run `python validate_content.py` from `original-novels/[novel-folder-name]/`
  - Fix any violations in the content modules
  - Ensure all 14 properties pass across all 20 chapters with 0 violations
  - Ask the user if questions arise

- [x] 7. Create the creation script and README
  - [x] 7.1 Create `original-novels/[novel-folder-name]/create_all_chapters.py`
    - Authenticate via `firebase_token.get_firebase_id_token(UID)` with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`
    - Import all 20 content modules and upload each via `curriculum/create` to `https://helloapi.step.is/curriculum/create`
    - Create series via `curriculum-series/create` with English-only title (no level descriptor), language "en", userLanguage "en"
    - Add each curriculum to series via `curriculum-series/addCurriculum` with display_order 1–20
    - Look up or create an en-en fiction collection: search `curriculum-collection/listAll` for an existing en-en fiction collection by title; if not found, create one via `curriculum-collection/create` with title "Fiction", language "en", userLanguage "en"
    - Must NOT use the vi-en "Truyện (Fiction)" collection (ID: 97cee550)
    - Attach series to en-en fiction collection via `curriculum-collection/addSeriesToCollection`
    - Set series to public via `curriculum-series/setIsPublic`
    - No hardcoded IDs — all IDs from API responses or runtime lookups
    - Handle errors: abort on auth failure, abort on upload failure with response body, report already-uploaded IDs on series failure
    - _Requirements: 6.3–6.7, 8.1–8.8_

  - [x] 7.2 Create `original-novels/[novel-folder-name]/README.md`
    - Document: how content was created, series ID placeholder, en-en fiction collection reference, SQL queries to find all 20 chapter curriculums in DB, novel summary, enough context to recreate source materials
    - _Requirements: 9.2–9.4_

- [x] 8. Final checkpoint — Full review
  - Ensure all files are in place: 20 content modules, validate_content.py, create_all_chapters.py, README.md
  - Ensure validation passes with 0 violations across all 20 chapters
  - Ensure 400 unique vocabulary words total, all plain strings
  - Ensure all content is English-only with no Vietnamese/Chinese text
  - Ask the user if questions arise

## Notes

- Tasks marked with `*` are optional and can be skipped — the validation checks are all implemented in task 5.1; sub-tasks 5.2–5.15 are for individual property test refinement
- All files go in `original-novels/[novel-folder-name]/` (folder name determined in task 1.1 based on novel title)
- No build system or test framework — scripts run directly with `python`
- The reference implementation is "The Last Light of Alder House" (series `70b5bb22`)
- 400 unique vocabulary words total across all 20 chapters (no repeats)
- Source files will be deleted after successful upload, leaving only README.md
- Key structural differences from Silent Clocktower reference: 20 chapters, 4 vocab/session, 20 vocab/chapter, plain string vocabList, English-only text, "Session N"/"Review" titles, "Read:"/"Listen:" prefixes, B2 prose level, 135–320 word passage range
