# Implementation Plan: ZH-ZH Advanced Chinese Curriculum Creation

## Overview

Create 8 ZH-ZH curriculums (Chinese-for-Chinese-speakers) organized into 1 collection ("中文进阶") with 2 series of 4 curriculums each, via Python scripts calling the helloapi REST API. Each script builds content JSON inline with hand-written Chinese text, creates the curriculum, verifies it, and checks for duplicates. An orchestrator script then creates the collection/series structure and sets display orders. Scripts are deleted after successful creation, leaving only a README.

## Tasks

- [x] 1. Set up workspace folder and shared utilities
  - Create `zh-zh-advanced-chinese/` directory
  - _Requirements: 18.1_

- [x] 2. Create Series 1 "思维与认知" curriculum scripts
  - [x] 2.1 Create `zh-zh-advanced-chinese/create_thinking_1_cognitive_bias.py` — 认知偏差的隐形陷阱
    - Import `firebase_token` via `sys.path` manipulation
    - Define inline `strip_keys()` function removing all keys from strip-keys.json
    - Build complete curriculum content JSON inline with all hand-written Chinese text:
      - 10 advanced vocab words (成语, 书面语, domain terms on cognitive bias): 5 for W1, 5 for W2
      - Persuasive copy description and preview in Chinese
      - Session 1 (11 activities): introAudio teaching W1, viewFlashcards, speakFlashcards, vocabLevel1-3, reading excerpt (subset of article with W1 words), speakReading, readAlong, writingSentence (5 prompts for W1), writingParagraph
      - Session 2 (11 activities): same pattern with W2 words, introAudio recaps W1 before teaching W2
      - Session 3 review (6 activities): introAudio reviewing all 10 words, viewFlashcards (all 10), vocabLevel1-3 (all 10), writingParagraph using both W1+W2
      - Session 4 full article (6 activities): introAudio intro, reading (full article 800-1200 chars with all 10 words), speakReading, readAlong, writingParagraph (culminating task), introAudio farewell reviewing all 10 words
    - All activity metadata: Chinese titles, descriptions, correct practiceMinutes per activity type
    - `create_curriculum()`: POST to `curriculum/create` with `language:"zh"`, `userLanguage:"zh"`, content as JSON string
    - `verify_curriculum()`: fetch via `curriculum/getOne`, verify language fields, 4 sessions, activity counts [11,11,6,6], activity type sequences, vocab counts, Chinese-only text, no strip-keys, reading excerpt ⊂ article, practiceMinutes values
    - `check_duplicates()`: query by title + UID, keep earliest, remove from series + delete extras
    - Print curriculum ID and title on success
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 3.1–3.11, 4.1–4.6, 5.1–5.9, 6.1–6.6, 7.1–7.7, 8.1–8.5, 9.1–9.9, 10.1, 10.2, 13.1, 13.3, 13.4, 14.1–14.3, 16.1, 16.3, 19.1–19.4, 20.1–20.3_

  - [x] 2.2 Create `zh-zh-advanced-chinese/create_thinking_2_decision_making.py` — 决策的艺术与科学
    - Same script structure as 2.1 (auth, strip_keys, create, verify, dedup)
    - 10 unique advanced vocab words on decision-making (no overlap with curriculum 1)
    - All hand-written Chinese content: description, preview, 4 sessions with full activity content
    - Full article (800-1200 chars) on decision science incorporating all 10 words
    - Verification checks all 12 correctness properties
    - _Requirements: 2.1–2.4, 3.1–3.11, 4.1–4.6, 5.1–5.9, 6.1–6.6, 7.1–7.7, 8.1–8.5, 9.1–9.9, 10.1, 10.2, 13.1, 13.3, 13.4, 14.1–14.3, 16.1, 16.3, 16.4, 19.1–19.4, 20.1–20.3_

  - [x] 2.3 Create `zh-zh-advanced-chinese/create_thinking_3_memory.py` — 记忆的建筑学
    - Same script structure as 2.1
    - 10 unique advanced vocab words on memory/neuroscience (no overlap with curriculums 1-2)
    - All hand-written Chinese content: description, preview, 4 sessions with full activity content
    - Full article (800-1200 chars) on memory incorporating all 10 words
    - Verification checks all 12 correctness properties
    - _Requirements: 2.1–2.4, 3.1–3.11, 4.1–4.6, 5.1–5.9, 6.1–6.6, 7.1–7.7, 8.1–8.5, 9.1–9.9, 10.1, 10.2, 13.1, 13.3, 13.4, 14.1–14.3, 16.1, 16.3, 16.4, 19.1–19.4, 20.1–20.3_

  - [x] 2.4 Create `zh-zh-advanced-chinese/create_thinking_4_attention.py` — 注意力经济学
    - Same script structure as 2.1
    - 10 unique advanced vocab words on attention/economics (no overlap with curriculums 1-3)
    - All hand-written Chinese content: description, preview, 4 sessions with full activity content
    - Full article (800-1200 chars) on attention economy incorporating all 10 words
    - Verification checks all 12 correctness properties
    - _Requirements: 2.1–2.4, 3.1–3.11, 4.1–4.6, 5.1–5.9, 6.1–6.6, 7.1–7.7, 8.1–8.5, 9.1–9.9, 10.1, 10.2, 13.1, 13.3, 13.4, 14.1–14.3, 16.1, 16.3, 16.4, 19.1–19.4, 20.1–20.3_

- [x] 3. Checkpoint — Run and verify Series 1 scripts
  - Run each of the 4 Series 1 scripts (`python create_thinking_1_cognitive_bias.py` through `create_thinking_4_attention.py`)
  - Confirm each prints curriculum ID + title with all verification checks passing (✓ PASS)
  - Record the 4 curriculum IDs for the orchestrator
  - Ensure all tests pass, ask the user if questions arise.

- [x] 4. Create Series 2 "社会与文明" curriculum scripts
  - [x] 4.1 Create `zh-zh-advanced-chinese/create_society_1_language_thought.py` — 语言如何塑造思维
    - Same script structure as 2.1 (auth, strip_keys, create, verify, dedup)
    - 10 unique advanced vocab words on linguistics/cognition
    - All hand-written Chinese content: description, preview, 4 sessions with full activity content
    - Full article (800-1200 chars) on how language shapes thought incorporating all 10 words
    - Verification checks all 12 correctness properties
    - _Requirements: 2.1–2.4, 3.1–3.11, 4.1–4.6, 5.1–5.9, 6.1–6.6, 7.1–7.7, 8.1–8.5, 9.1–9.9, 10.1, 10.2, 13.1, 13.3, 13.4, 14.1–14.3, 17.1, 17.3, 19.1–19.4, 20.1–20.3_

  - [x] 4.2 Create `zh-zh-advanced-chinese/create_society_2_city_logic.py` — 城市的隐秘逻辑
    - Same script structure as 2.1
    - 10 unique advanced vocab words on urban studies (no overlap with curriculum 5)
    - All hand-written Chinese content: description, preview, 4 sessions with full activity content
    - Full article (800-1200 chars) on city logic incorporating all 10 words
    - Verification checks all 12 correctness properties
    - _Requirements: 2.1–2.4, 3.1–3.11, 4.1–4.6, 5.1–5.9, 6.1–6.6, 7.1–7.7, 8.1–8.5, 9.1–9.9, 10.1, 10.2, 13.1, 13.3, 13.4, 14.1–14.3, 17.1, 17.3, 17.4, 19.1–19.4, 20.1–20.3_

  - [x] 4.3 Create `zh-zh-advanced-chinese/create_society_3_trust.py` — 信任的崩塌与重建
    - Same script structure as 2.1
    - 10 unique advanced vocab words on social trust (no overlap with curriculums 5-6)
    - All hand-written Chinese content: description, preview, 4 sessions with full activity content
    - Full article (800-1200 chars) on trust incorporating all 10 words
    - Verification checks all 12 correctness properties
    - _Requirements: 2.1–2.4, 3.1–3.11, 4.1–4.6, 5.1–5.9, 6.1–6.6, 7.1–7.7, 8.1–8.5, 9.1–9.9, 10.1, 10.2, 13.1, 13.3, 13.4, 14.1–14.3, 17.1, 17.3, 17.4, 19.1–19.4, 20.1–20.3_

  - [x] 4.4 Create `zh-zh-advanced-chinese/create_society_4_algorithm_ethics.py` — 算法时代的伦理困境
    - Same script structure as 2.1
    - 10 unique advanced vocab words on tech ethics (no overlap with curriculums 5-7)
    - All hand-written Chinese content: description, preview, 4 sessions with full activity content
    - Full article (800-1200 chars) on algorithm ethics incorporating all 10 words
    - Verification checks all 12 correctness properties
    - _Requirements: 2.1–2.4, 3.1–3.11, 4.1–4.6, 5.1–5.9, 6.1–6.6, 7.1–7.7, 8.1–8.5, 9.1–9.9, 10.1, 10.2, 13.1, 13.3, 13.4, 14.1–14.3, 17.1, 17.3, 17.4, 19.1–19.4, 20.1–20.3_

- [x] 5. Checkpoint — Run and verify Series 2 scripts
  - Run each of the 4 Series 2 scripts (`python create_society_1_language_thought.py` through `create_society_4_algorithm_ethics.py`)
  - Confirm each prints curriculum ID + title with all verification checks passing (✓ PASS)
  - Record the 4 curriculum IDs for the orchestrator
  - Ensure all tests pass, ask the user if questions arise.

- [x] 6. Create and run orchestrator script
  - [x] 6.1 Create `zh-zh-advanced-chinese/orchestrator.py`
    - Import `firebase_token` via `sys.path`
    - Hardcode the 8 curriculum IDs (filled in from tasks 3 and 5)
    - Create collection "中文进阶" via `curriculum-collection/create` with Chinese description, `isPublic: false`
    - Create series "思维与认知" via `curriculum-series/create` with Chinese description (<255 chars), `isPublic: false`
    - Create series "社会与文明" via `curriculum-series/create` with Chinese description (<255 chars), `isPublic: false`
    - Add 4 curriculums to each series via `curriculum-series/addCurriculum`
    - Set display orders on curriculums (0, 1, 2, 3) within each series via `curriculum/setDisplayOrder`
    - Add both series to collection via `curriculum-collection/addSeriesToCollection`
    - Set series display orders (100, 200) via `curriculum-series/setDisplayOrder`
    - Set collection display order via `curriculum-collection/setDisplayOrder`
    - Verify: collection fetchable, series fetchable, curriculums in correct series, display orders correct
    - Print all IDs (collection, series, curriculums)
    - _Requirements: 1.1–1.5, 11.3, 12.1–12.4, 15.1–15.4_

  - [x] 6.2 Run orchestrator and verify organization
    - Run `python orchestrator.py`
    - Confirm collection, series, and curriculum organization is correct
    - Verify display orders are set
    - Ensure all tests pass, ask the user if questions arise.

- [x] 7. Cleanup and documentation
  - [x] 7.1 Delete all Python scripts from `zh-zh-advanced-chinese/`
    - Delete all 8 creation scripts and the orchestrator script
    - _Requirements: 13.5, 18.3_

  - [x] 7.2 Create `zh-zh-advanced-chinese/README.md`
    - Document collection ID and title ("中文进阶")
    - Document series IDs and titles ("思维与认知", "社会与文明")
    - Document all 8 curriculum IDs, titles, display orders, and vocabulary words
    - Include SQL queries to find everything in the DB
    - Document creation method and enough context to recreate if needed
    - _Requirements: 18.2_

- [x] 8. Final checkpoint
  - Verify all 8 curriculums are accessible via `curriculum/getOne`
  - Verify collection and series structure is correct
  - Verify `zh-zh-advanced-chinese/` contains only README.md
  - Ensure all tests pass, ask the user if questions arise.

## Notes

- Each curriculum script is substantial (~2000+ chars of hand-written Chinese content) — one task per script
- All Chinese text (introAudio scripts, articles, descriptions, previews, writing prompts) must be hand-written inline, not templated
- Vocabulary words must not repeat within a series (40 unique words per series, 80 total)
- The orchestrator requires all 8 curriculum IDs from Phase 1 before it can run
- Scripts are deleted after successful creation per workspace conventions
- Property-based tests are implemented as inline verification steps within each creation script (Properties 1-12 from design.md), not as separate test files, since there is no test framework in this repo
