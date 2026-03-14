# Implementation Plan: Fiction Novel Curriculum Series

## Overview

Create a complete preintermediate-level fiction novel curriculum series (10 chapters) for Vietnamese-English learners. The novel is "Tiệm Sách Nhỏ Bên Biển (The Little Bookshop by the Sea)" — a contemporary fiction story set in a small English coastal town. Vocabulary flashcards are quick refreshers of mostly-known words; the focus is on immersive reading. Pipeline: write the novel → build chapter content modules → validate → upload via creation scripts → organize into a series → verify → clean up. All files live in `original-novels/the-little-bookshop-by-the-sea/` and are deleted after successful import, leaving only a README.

## Tasks

- [x] 1. Write the original novel (10 chapters)
  - [x] 1.1 Write chapters 1–5 prose and vocabulary lists
    - Write each chapter's narrative divided into 5 roughly equal reading passage segments
    - Use the 15 vocab words per chapter as specified in the design doc (familiar A2-B1 words, not new learning)
    - Each passage segment uses 3 of the chapter's vocab words
    - Prose uses short sentences, common grammar, preintermediate complexity
    - _Requirements: 1.2, 1.3, 1.6, 5.1, 5.2, 5.3, 5.4_

  - [x] 1.2 Write chapters 6–10 prose and vocabulary lists
    - Same constraints as 1.1
    - Verify no vocab overlap with chapters 1–5
    - Ensure the story reaches a satisfying resolution in chapter 10
    - _Requirements: 1.2, 1.3, 1.4, 1.5, 1.6, 5.1, 5.2, 5.3, 5.4_

- [x] 2. Create chapter content Python modules (chapters 1–5)
  - Each module exports `get_content()` returning the curriculum content dict
  - Title format: `"Tiệm Sách Nhỏ Bên Biển (The Little Bookshop by the Sea) — Chương N: [Vietnamese Title] ([English Title])"`
  - Vietnamese preview (~150 words with vivid hooks), Vietnamese description
  - 6 learning sessions: sessions 1–5 have [viewFlashcards, reading, readAlong], session 6 has [viewFlashcards, readAlong]
  - viewFlashcards: 3 vocab words per session (sessions 1–5), all 15 vocab for session 6
  - reading/readAlong: same text per session; session 6 readAlong = concatenation of sessions 1–5 texts
  - audioSpeed: -0.2 on viewFlashcards and reading activities
  - No strip keys anywhere in content
  - Place files in `original-novels/the-little-bookshop-by-the-sea/`
  - _Requirements: 2.1–2.8, 3.1–3.3, 3.6, 4.1, 4.3, 6.1_

- [x] 3. Create chapter content Python modules (chapters 6–10)
  - Same structure and constraints as task 2
  - _Requirements: 2.1–2.8, 3.1–3.3, 3.6, 4.1, 4.3, 6.1_

- [x] 4. Create the validation script and validate all content
  - [x] 4.1 Create `validate_content.py`
    - Import all 10 `chapterN_content` modules dynamically
    - Per-chapter checks:
      - Property 3: Exactly 6 sessions; sessions 1–5 have 3 activities [viewFlashcards, reading, readAlong]; session 6 has 2 activities [viewFlashcards, readAlong]
      - Property 4: viewFlashcards has vocabList + audioSpeed; reading has text + audioSpeed; readAlong has text
      - Property 5: readAlong text == reading text in same session (sessions 1–5)
      - Property 6: Session 6 vocabList == union of sessions 1–5; session 6 readAlong text == concatenation of sessions 1–5 reading texts
      - Property 7: Title matches `".+ — Chương \d+: .+ \(.+\)"` and contains no level descriptors
      - Property 8: Each session 1–5 viewFlashcards has exactly 3 words
      - Property 9: Every vocab word appears (case-insensitive) in its session's reading text
      - Property 10: Reading passage word counts across sessions 1–5 don't vary by more than factor of 2
      - Property 11: No strip keys anywhere in the content dict (recursive check)
    - Cross-chapter checks:
      - Property 1: Each chapter has exactly 15 unique vocab words
      - Property 2: At most 2 vocab words shared between any two chapters
    - Print pass/fail per property with details on failures
    - Place in `original-novels/the-little-bookshop-by-the-sea/`
    - _Requirements: 1.3, 1.5, 2.1–2.8, 3.1, 3.6, 4.1, 4.3, 4.5, 5.3, 5.4, 6.1_

  - [x] 4.2 Run `validate_content.py` and fix any failures
    - Run `python validate_content.py` from the novel folder
    - Fix any content modules that fail validation
    - Re-run until all properties pass

  - [x] 4.3 Run difficulty level classification on all chapters
    - For each chapter, extract the vocab list and reading passages
    - Submit them to an LLM using the same difficulty classifier prompt from `server/src/utils/activity-summary.ts:buildDifficultyPrompt`
    - Verify both vocab and reading classify as `preintermediate`
    - If any chapter classifies as `beginner` or `intermediate`, adjust the vocab/prose complexity and re-validate
    - _Property 15_

- [x] 5. Create chapter creation scripts and upload all 10 chapters
  - [x] 5.1 Create `create_chapter1_vi.py` through `create_chapter10_vi.py`
    - Each script imports its `chapterN_content` module and `firebase_token`
    - Authenticates with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`
    - POSTs to `https://helloapi.step.is/curriculum/create` with `{ firebaseIdToken, uid, language: "en", userLanguage: "vi", content: json.dumps(get_content()) }`
    - Prints created curriculum ID and title on success
    - Uses `sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")` for firebase_token import
    - No hardcoded curriculum/series/collection IDs
    - Place in `original-novels/the-little-bookshop-by-the-sea/`
    - _Requirements: 7.1–7.5, 10.1_

  - [x] 5.2 Run creation scripts for all 10 chapters
    - Run each `create_chapterN_vi.py` sequentially (1 through 10)
    - Record the returned curriculum IDs and titles
    - Verify each script prints success
    - _Requirements: 7.1, 7.5_

- [x] 6. Create and run the series organization script
  - [x] 6.1 Create `organize_series.py`
    - Authenticate with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`
    - POST `curriculum-series/create` with bilingual title "Tiệm Sách Nhỏ Bên Biển (The Little Bookshop by the Sea)" and Vietnamese description, `isPublic: true`
    - POST `curriculum-collection/listAll` to find "Truyện (Fiction)" collection ID by title at runtime
    - POST `curriculum/list` to find all 10 chapter curriculum IDs by title pattern at runtime
    - For each chapter (ordered 1–10):
      - POST `curriculum-series/addCurriculum` to add curriculum to series
      - POST `curriculum/setDisplayOrder` with displayOrder = chapter number
    - POST `curriculum-collection/addSeriesToCollection` to add series to Fiction collection
    - Print series ID and all curriculum-to-series mappings on success
    - No hardcoded IDs
    - Place in `original-novels/the-little-bookshop-by-the-sea/`
    - _Requirements: 8.1–8.6, 3.4, 3.5_

  - [x] 6.2 Run `organize_series.py`
    - Run the script and verify series creation, curriculum additions, collection attachment, and display orders
    - Record the series ID for verification
    - _Requirements: 8.1–8.3, 8.5_

- [x] 7. Post-upload verification
  - Run SQL to confirm all 10 curriculums are in the series with correct display_order (1–10)
  - Run SQL to confirm all curriculums have `language = 'en'` and `user_language = 'vi'`
  - Verify series is attached to the "Truyện (Fiction)" collection
  - _Requirements: 8.5, 10.1, 10.4_

- [x] 8. Cleanup and README creation
  - [x] 8.1 Create `README.md` in `original-novels/the-little-bookshop-by-the-sea/`
    - Document how the content was created
    - Include the series ID
    - Include SQL query to list all chapter curriculums with titles and display_orders
    - Include enough context to recreate source materials if needed
    - _Requirements: 9.2, 9.3_

  - [x] 8.2 Delete all source files except README.md
    - Delete all `chapterN_content.py`, `create_chapterN_vi.py`, `organize_series.py`, `validate_content.py`
    - Retain only `README.md`
    - _Requirements: 9.1_
