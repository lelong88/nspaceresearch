# Implementation Plan: Ordinary Life Philosophy Curriculum

## Overview

Create 6 vi-en curriculums exploring the philosophy of ordinary life for Vietnamese office workers, organized into a single series. Each curriculum has 18 vocab words, 4 sessions (12, 12, 12, 9 activities), and is created via a standalone Python script calling the helloapi REST API. The first script also creates the series. After all 6 succeed: verify via SQL, check for duplicates, delete scripts, write README.

## Tasks

- [x] 1. Create folder and first curriculum script (Self-Awareness)
  - [x] 1.1 Create `ordinary-life-philosophy-curriculum/` folder and write `create_self_awareness.py`
    - Create the folder at workspace root
    - Write the full script with `build_content()`, `validate()`, `strip_keys()`, `create()`
    - `build_content()` returns the complete curriculum JSON with all hand-written Vietnamese text inline:
      - 18 vocabulary words in 3 groups of 6 related to self-awareness, cognitive biases, defense mechanisms, honest self-perception
      - Vietnamese title, multi-paragraph persuasive description (tone: `provocative_question`), ~150-word preview
      - 4 sessions with all activities: introAudio scripts (500-800 words for vocab teaching), reading passages drawing from Kahneman, Tasha Eurich, Johari Window, writingSentence/writingParagraph prompts
      - Reading passages use Vietnamese office worker scenarios (performance reviews, team dynamics, comparing to colleagues)
      - `contentTypeTags: []`, Vietnamese user-facing text, English reading passages
    - `validate()` enforces all 10 correctness properties as assertions (vocab count, session/activity counts, activity type sequences, vocabList compliance, metadata completeness, strip keys absence, vocab teaching word count, contentTypeTags empty)
    - `strip_keys()` recursively removes auto-generated platform keys
    - `create()` authenticates via `firebase_token.get_firebase_id_token(UID)`, calls `curriculum/create` with `language: "en"`, `userLanguage: "vi"`, and `content` as JSON string
    - Additionally: `create_series()` creates the series with Vietnamese title and description (≤ 255 chars, tone from palette), `add_to_series()` adds curriculum to series and sets `displayOrder: 0`
    - Print curriculum ID, series ID, and duplicate-check SQL query
    - Farewell introAudio tone: `introspective guide`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.10, 7.1, 7.2, 7.4, 7.6, 8.1, 8.2, 8.4, 8.5, 8.6, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 11.1, 12.1, 12.2, 13.1, 13.4, 13.5, 14.1, 15.1, 15.2, 15.3, 15.4, 15.5_

  - [x] 1.2 Run `create_self_awareness.py` and record curriculum ID and series ID
    - Execute the script
    - Record the curriculum ID and series ID printed by the script
    - Verify no validation errors
    - _Requirements: 1.1, 7.1, 13.5, 14.1_

- [x] 2. Checkpoint — First curriculum and series created
  - Ensure the first curriculum was created successfully and the series exists, ask the user if questions arise.

- [x] 3. Create second curriculum script (Core Values)
  - [x] 3.1 Write `create_core_values.py`
    - Full script with `build_content()`, `validate()`, `strip_keys()`, `create()`
    - `build_content()` returns the complete curriculum JSON with all hand-written Vietnamese text inline:
      - 18 vocabulary words in 3 groups of 6 related to personal values, authenticity, external pressure, values-driven decision-making
      - Vietnamese title, multi-paragraph persuasive description (tone: `empathetic_observation`), ~150-word preview
      - 4 sessions with all activities: introAudio scripts (500-800 words for vocab teaching), reading passages drawing from Brené Brown, ACT, Vietnamese filial piety dynamics
      - Reading passages use Vietnamese office worker scenarios (family pressure for "stable" careers, salary comparison, social media highlight reels, personal dreams vs. family obligations)
      - `contentTypeTags: []`, Vietnamese user-facing text, English reading passages
    - `validate()` enforces all 10 correctness properties as assertions
    - `strip_keys()` recursively removes auto-generated platform keys
    - `create()` authenticates, calls `curriculum/create`, then `curriculum-series/addCurriculum` with the series ID from task 1, sets `displayOrder: 1`
    - Hardcode or accept the series ID from the first script's output
    - Print curriculum ID and duplicate-check SQL query
    - Farewell introAudio tone: `warm accountability`
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 2.10, 7.3, 7.4, 7.5, 8.1, 8.2, 8.4, 8.5, 8.6, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 11.1, 12.1, 12.2, 13.1, 13.4, 13.5, 14.1, 15.1, 15.2, 15.3, 15.4, 15.5_

  - [x] 3.2 Run `create_core_values.py` and record curriculum ID
    - Execute the script
    - Record the curriculum ID
    - Verify no validation errors and curriculum added to series
    - _Requirements: 2.1, 7.3, 13.5, 14.1_

- [x] 4. Create third curriculum script (Contentment vs. Complacency)
  - [x] 4.1 Write `create_contentment.py`
    - Full script with `build_content()`, `validate()`, `strip_keys()`, `create()`
    - `build_content()` returns the complete curriculum JSON with all hand-written Vietnamese text inline:
      - 18 vocabulary words in 3 groups of 6 related to contentment, complacency, satisfaction, ambition, psychology of enough
      - Vietnamese title, multi-paragraph persuasive description (tone: `bold_declaration`), ~150-word preview
      - 4 sessions with all activities: introAudio scripts (500-800 words for vocab teaching), reading passages drawing from Stoic philosophy (Seneca, Marcus Aurelius), Buddhist santuṭṭhi, hedonic adaptation research
      - Reading passages use Vietnamese office worker scenarios (colleague who got promoted, "good enough" question, Sunday-night dread cycle)
      - `contentTypeTags: []`, Vietnamese user-facing text, English reading passages
    - `validate()` enforces all 10 correctness properties as assertions
    - `strip_keys()` recursively removes auto-generated platform keys
    - `create()` authenticates, calls `curriculum/create`, adds to series with `displayOrder: 2`
    - Print curriculum ID and duplicate-check SQL query
    - Farewell introAudio tone: `quiet awe`
    - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 3.10, 7.3, 7.4, 7.5, 8.1, 8.2, 8.4, 8.5, 8.6, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 11.1, 12.1, 12.2, 13.1, 13.4, 13.5, 14.1, 15.1, 15.2, 15.3, 15.4, 15.5_

  - [x] 4.2 Run `create_contentment.py` and record curriculum ID
    - Execute the script
    - Record the curriculum ID
    - Verify no validation errors and curriculum added to series
    - _Requirements: 3.1, 7.3, 13.5, 14.1_

- [x] 5. Create fourth curriculum script (Growth Mindset)
  - [x] 5.1 Write `create_growth_mindset.py`
    - Full script with `build_content()`, `validate()`, `strip_keys()`, `create()`
    - `build_content()` returns the complete curriculum JSON with all hand-written Vietnamese text inline:
      - 18 vocabulary words in 3 groups of 6 related to growth mindset, self-compassion, honest assessment, toxic positivity vs. genuine growth
      - Vietnamese title, multi-paragraph persuasive description (tone: `vivid_scenario`), ~150-word preview
      - 4 sessions with all activities: introAudio scripts (500-800 words for vocab teaching), reading passages drawing from Carol Dweck's nuanced later work, Kristin Neff's self-compassion research, Japanese hansei (反省)
      - Reading passages use Vietnamese office worker scenarios (receiving harsh feedback, failing a project, motivational content making you feel worse, gap between "I can do anything" and honest self-assessment)
      - `contentTypeTags: []`, Vietnamese user-facing text, English reading passages
    - `validate()` enforces all 10 correctness properties as assertions
    - `strip_keys()` recursively removes auto-generated platform keys
    - `create()` authenticates, calls `curriculum/create`, adds to series with `displayOrder: 3`
    - Print curriculum ID and duplicate-check SQL query
    - Farewell introAudio tone: `practical momentum`
    - _Requirements: 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 4.10, 7.3, 7.4, 7.5, 8.1, 8.2, 8.4, 8.5, 8.6, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 11.1, 12.1, 12.2, 13.1, 13.4, 13.5, 14.1, 15.1, 15.2, 15.3, 15.4, 15.5_

  - [x] 5.2 Run `create_growth_mindset.py` and record curriculum ID
    - Execute the script
    - Record the curriculum ID
    - Verify no validation errors and curriculum added to series
    - _Requirements: 4.1, 7.3, 13.5, 14.1_

- [x] 6. Checkpoint — First 4 curriculums created and in series
  - Ensure all 4 curriculums created successfully and added to the series with correct display orders (0-3), ask the user if questions arise.

- [x] 7. Create fifth curriculum script (Meaning in Work)
  - [x] 7.1 Write `create_meaning_in_work.py`
    - Full script with `build_content()`, `validate()`, `strip_keys()`, `create()`
    - `build_content()` returns the complete curriculum JSON with all hand-written Vietnamese text inline:
      - 18 vocabulary words in 3 groups of 6 related to meaning-making, craftsmanship, purpose, contribution, psychology of meaningful work
      - Vietnamese title, multi-paragraph persuasive description (tone: `metaphor_led`), ~150-word preview
      - 4 sessions with all activities: introAudio scripts (500-800 words for vocab teaching), reading passages drawing from Viktor Frankl's logotherapy, Amy Wrzesniewski's job crafting research, Japanese ikigai as daily purpose
      - Reading passages use Vietnamese office worker scenarios (data entry clerk finding meaning in accuracy, accountant protecting families, "dream job" mythology vs. finding depth in the job you have)
      - `contentTypeTags: []`, Vietnamese user-facing text, English reading passages
    - `validate()` enforces all 10 correctness properties as assertions
    - `strip_keys()` recursively removes auto-generated platform keys
    - `create()` authenticates, calls `curriculum/create`, adds to series with `displayOrder: 4`
    - Print curriculum ID and duplicate-check SQL query
    - Farewell introAudio tone: `team-building energy`
    - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 5.10, 7.3, 7.4, 7.5, 8.1, 8.2, 8.4, 8.5, 8.6, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 11.1, 12.1, 12.2, 13.1, 13.4, 13.5, 14.1, 15.1, 15.2, 15.3, 15.4, 15.5_

  - [x] 7.2 Run `create_meaning_in_work.py` and record curriculum ID
    - Execute the script
    - Record the curriculum ID
    - Verify no validation errors and curriculum added to series
    - _Requirements: 5.1, 7.3, 13.5, 14.1_

- [x] 8. Create sixth curriculum script (Cultural Perspectives)
  - [x] 8.1 Write `create_cultural_perspectives.py`
    - Full script with `build_content()`, `validate()`, `strip_keys()`, `create()`
    - `build_content()` returns the complete curriculum JSON with all hand-written Vietnamese text inline:
      - 18 vocabulary words in 3 groups of 6 related to cross-cultural psychology, definitions of success, collectivism vs. individualism, building a personal philosophy
      - Vietnamese title, multi-paragraph persuasive description (tone: `surprising_fact`), ~150-word preview
      - 4 sessions with all activities: introAudio scripts (500-800 words for vocab teaching), reading passages drawing from Hofstede's cultural dimensions, Vietnamese collectivism vs. Western individualism, Chinese "face" (面子), Korean "nunchi" (눈치), Japanese ikigai
      - Reading passages use Vietnamese office worker scenarios (comparing life to American LinkedIn influencer, Tết family gatherings "Con làm ở đâu? Lương bao nhiêu?", success looking different in Hanoi/Tokyo/San Francisco)
      - `contentTypeTags: []`, Vietnamese user-facing text, English reading passages
    - `validate()` enforces all 10 correctness properties as assertions
    - `strip_keys()` recursively removes auto-generated platform keys
    - `create()` authenticates, calls `curriculum/create`, adds to series with `displayOrder: 5`
    - Print curriculum ID and duplicate-check SQL query
    - Farewell introAudio tone: `introspective guide`
    - _Requirements: 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 6.10, 7.3, 7.4, 7.5, 8.1, 8.2, 8.4, 8.5, 8.6, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 11.1, 12.1, 12.2, 13.1, 13.4, 13.5, 14.1, 15.1, 15.2, 15.3, 15.4, 15.5_

  - [x] 8.2 Run `create_cultural_perspectives.py` and record curriculum ID
    - Execute the script
    - Record the curriculum ID
    - Verify no validation errors and curriculum added to series
    - _Requirements: 6.1, 7.3, 13.5, 14.1_

- [x] 9. Checkpoint — All 6 curriculums created and in series
  - Ensure all 6 curriculums created successfully and added to the series with correct display orders (0-5), ask the user if questions arise.

- [x] 10. Post-creation verification
  - [x] 10.1 Verify all 6 curriculums exist in DB
    - Run SQL: `SELECT id, content->>'title' as title, language, user_language, is_public, created_at FROM curriculum WHERE uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73' AND content->>'title' IN ('<all 6 titles>') ORDER BY created_at;`
    - Confirm 6 rows returned, all with `language = 'en'`, `user_language = 'vi'`, `is_public = false`
    - _Requirements: 7.5, 12.1, 13.5_

  - [x] 10.2 Verify series membership and display order
    - Run SQL: `SELECT cs.id AS series_id, cs.title, csc.curriculum_id, c.content->>'title' AS curriculum_title, c.display_order FROM curriculum_series cs JOIN curriculum_series_items csc ON cs.id = csc.curriculum_series_id JOIN curriculum c ON csc.curriculum_id = c.id WHERE cs.id = '<series_id>' ORDER BY c.display_order;`
    - Confirm 6 curriculums in series with display orders 0-5 in correct progression
    - _Requirements: 7.3, 7.4_

  - [x] 10.3 Verify series description length
    - Run SQL: `SELECT id, title, length(description) as desc_length, description FROM curriculum_series WHERE id = '<series_id>';`
    - Confirm description ≤ 255 characters
    - _Requirements: 7.2_

  - [x] 10.4 Verify language homogeneity
    - Run SQL: `SELECT array_agg(DISTINCT c.language) AS languages, array_agg(DISTINCT c.user_language) AS user_languages FROM curriculum_series cs JOIN curriculum_series_items csc ON cs.id = csc.curriculum_series_id JOIN curriculum c ON csc.curriculum_id = c.id WHERE cs.id = '<series_id>';`
    - Confirm languages = `{en}`, user_languages = `{vi}`
    - _Requirements: 7.5_

  - [x] 10.5 Verify all curriculums are private
    - Run SQL: `SELECT id, content->>'title' as title, is_public FROM curriculum WHERE id IN ('<all 6 IDs>');`
    - Confirm all `is_public = false`
    - _Requirements: 12.1, 12.2, 12.3_

- [x] 11. Duplicate check
  - [x] 11.1 Check for duplicate curriculums
    - Run SQL: `SELECT content->>'title' as title, COUNT(*) as cnt FROM curriculum WHERE uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73' GROUP BY content->>'title' HAVING COUNT(*) > 1;`
    - If duplicates found: keep earliest, remove from series first if needed, then delete extras
    - _Requirements: 14.1, 14.2, 14.3_

- [x] 12. Cleanup and documentation
  - [x] 12.1 Delete all 6 creation scripts
    - Delete `create_self_awareness.py`, `create_core_values.py`, `create_contentment.py`, `create_growth_mindset.py`, `create_meaning_in_work.py`, `create_cultural_perspectives.py`
    - _Requirements: 13.2_

  - [x] 12.2 Write `ordinary-life-philosophy-curriculum/README.md`
    - Document: all 6 curriculum IDs, series ID, SQL queries to find them, vocabulary lists for each curriculum, tone assignments (description + farewell), recreation context
    - _Requirements: 13.3_

- [x] 13. Final checkpoint — All verified and cleaned up
  - Ensure all tests pass, ask the user if questions arise.

## Notes

- Each script is substantial — all text content (descriptions, previews, introAudio scripts, reading passages, writing prompts) is hand-written inline, not templated
- The `validate()` function enforces all 10 correctness properties as assertions before any API call — this is the primary correctness mechanism
- The first script (`create_self_awareness.py`) additionally creates the series; subsequent scripts receive the series ID
- Description tone assignments: provocative_question → empathetic_observation → bold_declaration → vivid_scenario → metaphor_led → surprising_fact (all 6 tones used exactly once, no adjacent duplicates)
- Farewell tone assignments: introspective guide → warm accountability → quiet awe → practical momentum → team-building energy → introspective guide (no adjacent duplicates)
- Display order 0-5 follows the intended learning progression: self-awareness → core values → contentment → growth mindset → meaning in work → cultural perspectives
- Series is NOT made public — content generation (audio, illustrations) happens after creation
- All scripts authenticate via `firebase_token.get_firebase_id_token()` with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`
