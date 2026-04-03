# Implementation Plan: Uncomfortable Growth Curriculum

## Overview

Create 4 mini `balanced_skills` curriculums on the theme "Get comfortable being uncomfortable is the essence of language learning." Each curriculum is a standalone Python script with hand-written content. After successful creation and verification, scripts are deleted, leaving only a README.

## Tasks

- [x] 1. Set up folder structure and shared utilities
  - [x] 1.1 Create `uncomfortable-growth-curriculum/` folder
    - Create the directory at workspace root
    - _Requirements: 16.1_
  
  - [x] 1.2 Create shared `strip_keys()` helper
    - Define inline in each script or as a shared module
    - Must remove: `mp3Url`, `illustrationSet`, `chapterBookmarks`, `segments`, `whiteboardItems`, `userReadingId`, `lessonUniqueId`, `curriculumTags`, `taskId`, `imageId`
    - _Requirements: 9.1, 9.2_

- [x] 2. Create en-en curriculum (English speaker learning English)
  - [x] 2.1 Write `create_en_en.py` script with complete curriculum content
    - Hand-write all text: title, description (5-beat persuasive copy), preview (~150 words)
    - 5 vocabulary words about cognitive psychology, neuroplasticity, growth mindset
    - Session 1 (8 activities): introAudio, viewFlashcards, speakFlashcards, vocabLevel1, reading, speakReading, readAlong, writingSentence
    - Session 2 (6 activities): introAudio, reading, speakReading, readAlong, writingParagraph, introAudio (farewell)
    - All activities must have title, description
    - Set `language: "en"`, `userLanguage: "en"` as top-level body params
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 5.2, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2, 7.3, 7.4, 8.1-8.8, 12.1, 12.2, 13.1, 13.2, 13.3, 14.1, 14.3, 14.4, 17.1, 17.5_

  - [x] 2.2 Run script to create en-en curriculum in database
    - Execute `python create_en_en.py`
    - Verify API returns curriculum ID
    - _Requirements: 11.1, 11.2_

- [x] 3. Create en-zh curriculum (English speaker learning Chinese)
  - [x] 3.1 Write `create_en_zh.py` script with complete curriculum content
    - Hand-write all text: title, description (5-beat persuasive copy), preview (~150 words)
    - 6 Chinese vocabulary words about perseverance, self-cultivation, Chinese philosophical tradition
    - Session 1 (9 activities): introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence
    - Session 2 (5 activities): introAudio, reading, speakReading, readAlong, introAudio (farewell)
    - User-facing text in English, reading passages in Chinese
    - Set `language: "zh"`, `userLanguage: "en"` as top-level body params
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 5.3, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2, 7.3, 7.4, 8.1-8.8, 12.1, 12.2, 13.1, 13.2, 13.3, 14.1, 14.2, 17.2, 17.5_

  - [x] 3.2 Run script to create en-zh curriculum in database
    - Execute `python create_en_zh.py`
    - Verify API returns curriculum ID
    - _Requirements: 11.1, 11.2_

- [x] 4. Create vi-zh curriculum (Vietnamese speaker learning Chinese)
  - [x] 4.1 Write `create_vi_zh.py` script with complete curriculum content
    - Hand-write all text: title, description (5-beat persuasive copy), preview (~150 words)
    - 6 Chinese vocabulary words about resilience, emotional regulation, learning journey
    - Session 1 (9 activities): introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence
    - Session 2 (5 activities): introAudio, reading, speakReading, readAlong, introAudio (farewell)
    - User-facing text in Vietnamese, reading passages in Chinese
    - Set `language: "zh"`, `userLanguage: "vi"` as top-level body params
    - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 5.4, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2, 7.3, 7.4, 7.5, 8.1-8.8, 12.1, 12.2, 13.1, 13.2, 13.3, 14.1, 14.2, 17.3, 17.5_

  - [x] 4.2 Run script to create vi-zh curriculum in database
    - Execute `python create_vi_zh.py`
    - Verify API returns curriculum ID
    - _Requirements: 11.1, 11.2_

- [x] 5. Create vi-en curriculum (Vietnamese speaker learning English)
  - [x] 5.1 Write `create_vi_en.py` script with complete curriculum content
    - Hand-write all text: title, description (5-beat persuasive copy), preview (~150 words)
    - 6 English vocabulary words about stepping outside comfort zone, embracing failure, science of learning
    - Session 1 (9 activities): introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence
    - Session 2 (5 activities): introAudio, reading, speakReading, readAlong, introAudio (farewell)
    - User-facing text in Vietnamese, reading passages in English
    - Set `language: "en"`, `userLanguage: "vi"` as top-level body params
    - _Requirements: 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 5.5, 6.1, 6.2, 6.3, 6.4, 6.5, 7.1, 7.2, 7.3, 7.4, 7.5, 8.1-8.8, 12.1, 12.2, 13.1, 13.2, 13.3, 14.1, 14.2, 17.4, 17.5_

  - [x] 5.2 Run script to create vi-en curriculum in database
    - Execute `python create_vi_en.py`
    - Verify API returns curriculum ID
    - _Requirements: 11.1, 11.2_

- [x] 6. Checkpoint - Verify all 4 curriculums created
  - Ensure all 4 curriculums exist in database with correct structure
  - Verify activity counts: en-en (8,6), bilingual (9,5)
  - Verify vocabulary counts: en-en (5), bilingual (6)
  - Ask the user if questions arise.

- [x] 7. Add curriculums to feature collections and series
  - [x] 7.1 Query existing collections and series for each language pair
    - Call `curriculum-collection/listAll` and `curriculum-series/listAll`
    - Identify appropriate placement for each curriculum
    - _Requirements: 10.1_

  - [x] 7.2 Create new series if needed for each language pair
    - If no appropriate series exists, create with descriptive title and persuasive description
    - en-en/en-zh: "Uncomfortable Growth" (English title)
    - vi-zh/vi-en: "Tăng Trưởng Qua Khó Khăn" (Vietnamese title)
    - _Requirements: 10.2_

  - [x] 7.3 Add each curriculum to its series and set display order
    - Call `curriculum-series/addCurriculum` for each curriculum
    - Call `curriculum/setDisplayOrder` based on existing curriculums in series
    - _Requirements: 10.3_

  - [x] 7.4 Verify language homogeneity in each series
    - Query series to confirm all curriculums have same `language` and `user_language`
    - _Requirements: 10.4_

- [x] 8. Post-creation verification and duplicate check
  - [x] 8.1 Check for duplicate curriculums
    - Query DB for curriculums with same title and language owned by same user
    - Delete extras if found, keeping earliest-created one
    - _Requirements: 15.1, 15.2_

  - [x] 8.2 Verify all curriculums are private
    - Confirm `is_public: false` for all 4 curriculums
    - _Requirements: 11.1_

  - [x] 8.3 Verify no strip-keys in curriculum content
    - Fetch each curriculum via API and check for forbidden keys
    - _Requirements: 9.1_

- [x] 9. Final checkpoint - All curriculums verified
  - Ensure all tests pass, ask the user if questions arise.

- [x] 10. Cleanup and documentation
  - [x] 10.1 Delete source Python scripts
    - Remove `create_en_en.py`, `create_en_zh.py`, `create_vi_zh.py`, `create_vi_en.py`
    - _Requirements: 12.4, 16.3_

  - [x] 10.2 Create README.md with creation details
    - Document which collections/series each curriculum was placed in (with IDs)
    - List curriculum IDs and titles for all 4
    - Include SQL queries to find curriculums in DB
    - Provide enough context to recreate if needed
    - _Requirements: 16.2_

## Notes

- Each curriculum script must have ALL text hand-written — no templates, no f-string interpolation for learner-facing content
- Vocabulary words across the 4 curriculums are NOT translations of each other — each is native to its target language
- The theme "Get comfortable being uncomfortable" is explored from different cultural/linguistic angles per curriculum
- All curriculums remain private until content generation (audio, illustrations) is complete
- Source scripts are deleted after successful creation, leaving only README for audit trail
