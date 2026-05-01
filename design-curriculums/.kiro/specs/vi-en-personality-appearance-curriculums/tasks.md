# Tasks

## Task 1: Create validation script and folder setup

- [x] 1.1 Create `vi-en-personality-appearance-curriculums/` folder
- [x] 1.2 Create `validate_personality_appearance.py` implementing all 11 correctness properties as assertions against a curriculum content dict (session structure, vocab distribution, reading passage constraints, vocab format, activity schema, title formats, top-level structure, strip-keys, introAudio coverage, valid activity types)
  - _Requirements: 1.1–1.7, 2.1–2.7, 3.4, 7.1–7.11, 8.1–8.8, 9.1, 15.1–15.6_
- [x] 1.3 Create `orchestrate_series.py` that creates the series "Miêu Tả Người Quen" via `curriculum-series/create` with Vietnamese title and description (≤255 chars, surprising_fact tone), and has functions to add curriculums and set display orders (Personality=1, Appearance=2)
  - _Requirements: 10.1, 10.2, 14.1_

## Task 2: Create Curriculum 1 — Miêu Tả Tính Cách (Describing Personalities)

- [x] 2.1 Create `create_personality.py` with hand-written content: W1 (outgoing, shy, generous, patient, stubborn), W2 (honest, cheerful, calm, confident, creative), W3 (reliable, thoughtful, ambitious, easygoing, sensitive)
  - _Requirements: 3.1, 3.3, 3.4, 12.1, 13.1_
- [x] 2.2 Write all introAudio scripts in Vietnamese teaching each word with personality-describing context examples (describing friends, family, colleagues); farewell script (400–600 words) using introspective_guide tone
  - _Requirements: 6.1–6.6, 14.6_
- [x] 2.3 Write 3 first-person mini-speech reading passages (2–4 sentences each, describing people the learner knows) and 1 review passage (6–12 sentences) using all 15 vocab words
  - _Requirements: 2.1–2.7_
- [x] 2.4 Write persuasive description (empathetic_observation tone), preview (~150 words in Vietnamese), and all activity metadata (titles, descriptions following format conventions)
  - _Requirements: 4.1, 5.2–5.6, 7.2–7.5, 8.1–8.8, 14.5_
- [x] 2.5 Run validation, execute script, verify curriculum created successfully
  - _Requirements: 11.1–11.4, 15.1–15.7, 16.1–16.3_

## Task 3: Create Curriculum 2 — Miêu Tả Ngoại Hình (Describing Appearances)

- [x] 3.1 Create `create_appearance.py` with hand-written content: W1 (tall, slim, curly, straight, freckles), W2 (muscular, pale, tan, beard, bald), W3 (chubby, elegant, wrinkles, dimples, broad)
  - _Requirements: 3.2, 3.3, 3.4, 12.1, 13.1_
- [x] 3.2 Write all introAudio scripts in Vietnamese teaching each word with appearance-describing context examples (describing how people look in everyday situations); farewell script (400–600 words) using warm_accountability tone
  - _Requirements: 6.1–6.6, 14.6_
- [x] 3.3 Write 3 first-person mini-speech reading passages (2–4 sentences each, describing people's physical features) and 1 review passage (6–12 sentences) using all 15 vocab words
  - _Requirements: 2.1–2.7_
- [x] 3.4 Write persuasive description (vivid_scenario tone), preview (~150 words in Vietnamese), and all activity metadata (titles, descriptions following format conventions)
  - _Requirements: 4.2, 5.2–5.6, 7.2–7.5, 8.1–8.8, 14.5_
- [x] 3.5 Run validation, execute script, verify curriculum created successfully
  - _Requirements: 11.1–11.4, 15.1–15.7, 16.1–16.3_

## Task 4: Series assembly and verification

- [x] 4.1 Run orchestrator to create series and add both curriculums with sequential display orders (Personality=1, Appearance=2)
  - _Requirements: 10.1–10.4, 14.1_
- [x] 4.2 Run cross-curriculum vocab uniqueness check (Property 5) across both curriculums
  - _Requirements: 3.5, 14.3_
- [x] 4.3 Query DB to verify both curriculums are in the series with correct display orders and `is_public: false`
  - _Requirements: 10.2, 10.3, 11.3_
- [x] 4.4 Check for and clean up any duplicate curriculums
  - _Requirements: 16.1–16.3_

## Task 5: Documentation and cleanup

- [x] 5.1 Create `vi-en-personality-appearance-curriculums/README.md` with: series ID and title, both curriculum IDs and titles, display orders, vocab lists, tone assignments, creation method, SQL queries, recreation context
  - _Requirements: 12.5_
- [x] 5.2 Delete all `.py` scripts from the folder (creation scripts, orchestrator, validation script)
  - _Requirements: 12.6_
