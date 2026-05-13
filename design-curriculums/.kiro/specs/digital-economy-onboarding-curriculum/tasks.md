# Implementation Plan: Digital Economy Onboarding Curriculum

## Overview

Create a single onboarding/demo English-learning curriculum for Vietnamese speakers on the topic of "Digital Economy" (Kinh Tế Số). The implementation consists of one standalone Python script (`digital-economy-onboarding-curriculum/create_digital_economy_onboarding.py`) with an inline validator, property-based tests for the validator using Hypothesis, and post-creation documentation/cleanup.

Language pair: userLanguage="vi", language="en". 1 session, 9 activities, 5 vocabulary words (platform, transaction, startup, innovation, digital). Free pricing (0 credits), stays private. Reuses root-level `api_helpers.py`.

## Tasks

- [x] 1. Create the curriculum script with inline validator
  - [x] 1.1 Create `digital-economy-onboarding-curriculum/create_digital_economy_onboarding.py` with inline `validate()` function
    - Define constants: `STRIP_KEYS`, `VALID_ACTIVITY_TYPES`, `EXPECTED_SEQUENCE`
    - Implement `validate(content: dict) -> None` with all 20 checks from design:
      - Top-level structure: content is dict, title non-empty, description non-empty, preview.text non-empty
      - contentTypeTags must be `[]`
      - learningSessions: list with exactly 1 element, session has title and non-empty activities
      - Activity sequence matches EXPECTED_SEQUENCE (9 activities: introAudio, viewFlashcards, speakFlashcards, vocabLevel1, reading, speakReading, readAlong, writingSentence, introAudio)
      - Each activity has activityType, title, description, data (no `type` field allowed)
      - activityType values in VALID_ACTIVITY_TYPES
      - Content fields inside `data`, not inline on activity
      - vocabList: array of lowercase strings, field name `vocabList` (never `words`)
      - viewFlashcards and speakFlashcards have identical vocabList
      - vocabList arrays have exactly 5 items
      - writingSentence: data.vocabList, data.items (non-empty), each item has prompt and targetVocab
      - No strip keys anywhere in JSON tree (recursive check)
    - Raises `ValueError` with specific violation message on any failure
    - _Requirements: 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 10.9, 10.10_

  - [x] 1.2 Implement `build_content()` function with all hand-crafted content
    - Title: minimal Vietnamese title (e.g., "Kinh Tế Số")
    - Description: persuasive copy with `surprising_fact` or `provocative_question` tone, multi-paragraph 5-beat structure, all Vietnamese
    - Preview (~150 words): vivid hooks about career in digital age, vocabulary listing, what learner will discuss after completing
    - Session title: "Khám phá Kinh Tế Số"
    - Activity 1 — introAudio welcome (500-800 words): bilingual, greet warmly, hook to daily life (Shopee, MoMo, Grab), list all 5 words, teach each word with English word + Vietnamese meaning + contextual example + digital economy connection
    - Activity 2 — viewFlashcards: vocabList ["platform", "transaction", "startup", "innovation", "digital"]
    - Activity 3 — speakFlashcards: identical vocabList to viewFlashcards
    - Activity 4 — vocabLevel1: same vocabList
    - Activity 5 — reading: expository passage 60-70 words about digital economy in Vietnam, incorporates all 5 vocab words, preintermediate grammar (10-14 words/sentence avg), connects to Vietnamese daily life
    - Activity 6 — speakReading: same text as reading
    - Activity 7 — readAlong: same text as reading
    - Activity 8 — writingSentence: 2-3 items, each with detailed prompt (Vietnamese instruction + English example sentence) and targetVocab, data.vocabList included
    - Activity 9 — introAudio farewell (400-600 words): `practical_momentum` register, review all 5 words with definitions and fresh examples, connect to digital economy theme, congratulate, encourage exploration
    - contentTypeTags: []
    - All activity titles/descriptions follow naming conventions from design
    - Every piece of text individually crafted — no templates or string interpolation
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 2.1, 2.2, 2.3, 2.4, 3.1, 3.2, 3.3, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 5.1, 5.2, 5.3, 5.4, 6.1, 6.2, 6.3, 6.4, 6.5, 7.1, 7.2, 7.3, 7.4, 7.5, 13.1, 13.2, 13.3, 13.4_

  - [x] 1.3 Implement `main()` function with API upload
    - Call `build_content()` to get content dict
    - Call `validate(content)` before upload
    - Call `create_curriculum(content, "en", "vi")` using root-level `api_helpers.py`
    - Print curriculum ID on success
    - Import via `sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")`
    - No setPrice call (free by default), no setPublic call (stays private)
    - _Requirements: 1.6, 8.1, 8.2, 9.1, 11.1, 11.2, 11.3, 11.4, 11.6_

- [x] 2. Write property-based tests for the validator
  - [x] 2.1 Create `digital-economy-onboarding-curriculum/test_validate.py` with Hypothesis property tests
    - Import validate function from the script
    - Use `@settings(max_examples=100)` for all property tests
    - Create `@composite` generator strategies for valid base content dicts
    - **Property 1: Structural validity — valid content passes validation**
    - **Validates: Requirements 1.4, 1.5, 3.1, 3.2, 4.1, 4.2, 4.3, 4.4, 4.6, 10.1-10.10**
  
  - [x] 2.2 Write property test: Strip keys rejected anywhere in JSON tree
    - **Property 2: Strip keys rejected anywhere in JSON tree**
    - Generate valid content, inject a random strip key at a random depth
    - Assert validate() raises ValueError mentioning the strip key
    - **Validates: Requirements 1.5, 10.8**

  - [x] 2.3 Write property test: vocabList format enforcement
    - **Property 3: vocabList format enforcement**
    - Test non-lowercase strings, non-string items, field named `words` instead of `vocabList`
    - Assert validate() raises ValueError
    - **Validates: Requirements 2.4, 10.5**

  - [x] 2.4 Write property test: Activity sequence enforcement
    - **Property 4: Activity sequence enforcement**
    - Generate content with shuffled/missing/extra activities
    - Assert validate() raises ValueError indicating sequence mismatch
    - **Validates: Requirements 3.1, 10.2**

  - [x] 2.5 Write property test: viewFlashcards/speakFlashcards vocabList consistency
    - **Property 5: viewFlashcards/speakFlashcards vocabList consistency**
    - Generate content where the two vocabLists differ
    - Assert validate() raises ValueError
    - **Validates: Requirements 3.2, 10.6**

  - [x] 2.6 Write property test: writingSentence structural completeness
    - **Property 6: writingSentence structural completeness**
    - Generate content with missing data.vocabList, missing data.items, items without prompt or targetVocab
    - Assert validate() raises ValueError
    - **Validates: Requirements 4.4, 10.7**

  - [x] 2.7 Write property test: contentTypeTags enforcement
    - **Property 7: contentTypeTags enforcement**
    - Generate content where contentTypeTags is not exactly `[]`
    - Assert validate() raises ValueError
    - **Validates: Requirements 1.4, 10.9**

- [x] 3. Checkpoint — Validate script and run tests
  - Verify `build_content()` output passes `validate()` (smoke test)
  - Verify reading passage word count is 60-70 words
  - Verify introAudio welcome script is 500-800 words
  - Verify introAudio farewell script is 400-600 words
  - Verify vocabList has exactly 5 words
  - Run property tests with `python -m pytest digital-economy-onboarding-curriculum/test_validate.py -v`
  - Ensure all tests pass, ask the user if questions arise.

- [x] 4. Run script and verify curriculum in database
  - [x] 4.1 Execute the creation script
    - Run `python create_digital_economy_onboarding.py` in `digital-economy-onboarding-curriculum/`
    - Record the returned curriculum ID
    - _Requirements: 11.1, 11.2, 11.3, 11.4, 11.6_

  - [x] 4.2 Verify curriculum in database
    - Query curriculum by title and UID to confirm it exists
    - Verify language="en", userLanguage="vi"
    - Verify content structure: 1 session, 9 activities, correct activity sequence
    - Verify contentTypeTags is `[]`
    - Verify curriculum is not public
    - _Requirements: 1.1, 1.2, 1.4, 1.6, 3.1_

  - [x] 4.3 Run duplicate check
    - Query for duplicate titles with same UID
    - If duplicates found: keep earliest, delete extras
    - _Requirements: 12.3_

- [x] 5. Documentation and cleanup
  - [x] 5.1 Create `digital-economy-onboarding-curriculum/README.md`
    - Document curriculum ID, title, vocabulary list
    - Document pricing (free, 0 credits)
    - Document language pair (vi-en)
    - Include SQL verification queries
    - Include recreation context and method
    - _Requirements: 12.1_

  - [x] 5.2 Delete creation script after verification
    - Delete `create_digital_economy_onboarding.py` from `digital-economy-onboarding-curriculum/`
    - Only README.md and test_validate.py remain in the directory
    - _Requirements: 12.2_

- [x] 6. Final checkpoint — All tasks complete
  - Verify 1 new curriculum exists in database with correct structure
  - Verify README.md is complete
  - Verify creation script is deleted
  - Verify no setPublic calls were made (curriculum remains private)
  - Verify no setPrice calls were made (free by default)
  - Ensure all tests pass, ask the user if questions arise.

## Notes

- Tasks marked with `*` are optional and can be skipped for faster MVP
- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation
- Property tests validate universal correctness properties from the design document
- Unit tests validate specific examples and edge cases
- Root-level `api_helpers.py` is reused as-is — no changes needed
- All curriculum content must be hand-crafted — no template-based generation
- Vietnamese marketing text (title, description, preview)
- introAudio scripts: bilingual (Vietnamese explanations for English vocabulary)
- Reading passage: entirely in English, 60-70 words
- vocabList: 5 English words in lowercase: platform, transaction, startup, innovation, digital
- Standalone curriculum — no series, no collection, no orchestrator needed
- Free pricing (0 credits) — no setPrice call
- Stays private — no setPublic call
