# Implementation Plan: Mental Well-being Curriculum

## Overview

Create 10 vi-en mental well-being curriculums organized into 1 collection with 2 series (General Audience × 5, Medical Students × 5). Each curriculum is a standalone Python script with hand-written content, inline validation, and API calls via `api_helpers.py`. After creation, scripts are deleted and a README.md documents everything.

Creation order: collection + series setup → 5 general-audience scripts (G1–G5) → 5 medical-student scripts (M1–M5) → verification → README + cleanup.

## Tasks

- [x] 1. Create collection and series setup script
  - [x] 1.1 Create `mental-wellbeing-curriculum/create_setup.py` that creates the collection, both series, wires them together, and sets display orders
    - Create collection "Sức Khỏe Tinh Thần (Mental Well-being)" with neutral informative description
    - Create general-audience series "Sức Khỏe Tinh Thần — Đời Sống (Everyday Mental Well-being)" with ≤255-char description using `vivid_scenario` tone
    - Create medical-student series "Sức Khỏe Tinh Thần — Sinh Viên Y Khoa (Mental Well-being for Medical Students)" with ≤255-char description using `bold_declaration` tone
    - Wire both series to the collection via `add_series_to_collection`
    - Set series display orders: general = 0, medical = 1
    - Print all created IDs (collection_id, general_series_id, medical_series_id) for use by subsequent scripts
    - Do NOT call `setPublic` with `isPublic: true` on anything
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6_

- [x] 2. Create general-audience beginner curriculums (G1–G2)
  - [x] 2.1 Create `mental-wellbeing-curriculum/create_g1_daily_emotions.py` — G1 beginner curriculum on daily emotions and self-awareness
    - Build complete content JSON with 4 sessions, 12 vocab words: anxious, calm, overwhelmed, grateful, frustrated, mood, emotion, stress, relax, breathe, balance, mindful
    - Session structure: Phần 1 (6 words), Phần 2 (6 words), Ôn tập (all 12), Đọc toàn bài
    - Activity pattern per learning session: introAudio → viewFlashcards → speakFlashcards → vocabLevel1 → vocabLevel2 → reading → speakReading → readAlong → writingSentence
    - Review session: introAudio → viewFlashcards → speakFlashcards → vocabLevel1 → vocabLevel2 → writingSentence
    - Final session: introAudio → reading → speakReading → readAlong → writingParagraph → introAudio (farewell)
    - Description tone: `empathetic_observation` — ALL-CAPS Vietnamese headline, multi-paragraph persuasive copy
    - Farewell tone: `warm accountability`
    - Vietnamese titles/descriptions/preview/introAudio; English reading passages at beginner level
    - Inline `validate()` checking all 3 correctness properties before API call
    - Query general series ID from DB at runtime, add to series, set display_order=0, set price=49
    - Print duplicate-check SQL query after creation
    - _Requirements: 2.1, 3.1 (G1), 5.1, 5.3, 5.4, 5.5, 5.6, 6.1–6.8, 7.1, 7.5, 8.1–8.7, 9.1–9.4, 10.1–10.4, 11.1–11.3, 12.1, 12.5_

  - [x] 2.2 Create `mental-wellbeing-curriculum/create_g2_sleep_hygiene.py` — G2 beginner curriculum on sleep hygiene and rest
    - Build complete content JSON with 4 sessions, 12 vocab words: insomnia, fatigue, routine, nap, restful, drowsy, pillow, alarm, habit, refresh, recharge, snore
    - Same 4-session beginner structure as G1
    - Description tone: `surprising_fact` (different from adjacent G1)
    - Farewell tone: `quiet awe` (different from adjacent G1)
    - Inline `validate()`, query series ID, add to series, set display_order=1, set price=49
    - _Requirements: 2.1, 3.1 (G2), 3.3, 5.1, 5.3–5.6, 6.1–6.8, 7.1, 7.2, 7.5, 8.1–8.7, 9.1–9.4, 10.1–10.4, 11.1–11.3, 12.1, 12.5_

- [x] 3. Create general-audience preintermediate/intermediate curriculums (G3–G5)
  - [x] 3.1 Create `mental-wellbeing-curriculum/create_g3_stress_management.py` — G3 preintermediate curriculum on stress management
    - Build complete content JSON with 5 sessions, 18 vocab words: anxiety, tension, burnout, coping, resilience, therapy, meditation, journal, boundary, self-care, trigger, symptom, recovery, wellness, mindfulness, gratitude, perspective, overwhelm
    - Session structure: Phần 1/2/3 (6 words each), Ôn tập (all 18), Đọc toàn bài
    - Activity pattern per learning session adds `vocabLevel3` after `vocabLevel2`
    - Review session adds `vocabLevel3`
    - Description tone: `provocative_question` (different from adjacent G2)
    - Farewell tone: `introspective guide` (different from adjacent G2)
    - Inline `validate()`, query series ID, add to series, set display_order=2, set price=49
    - _Requirements: 2.1, 3.1 (G3), 3.3, 5.2, 5.3–5.6, 6.1–6.8, 7.1, 7.2, 7.5, 8.1–8.7, 9.1–9.4, 10.1–10.4, 11.1–11.3, 12.2, 12.5_

  - [x] 3.2 Create `mental-wellbeing-curriculum/create_g4_healthy_relationships.py` — G4 intermediate curriculum on healthy relationships
    - Build complete content JSON with 5 sessions, 18 vocab words: empathy, attachment, vulnerability, assertive, conflict, compromise, trust, intimacy, resentment, codependent, communicate, validate, supportive, toxic, reciprocal, forgive, nurture, compassion
    - Same 5-session intermediate structure as G3
    - Description tone: `vivid_scenario` (different from adjacent G3)
    - Farewell tone: `team-building energy` (different from adjacent G3)
    - Inline `validate()`, query series ID, add to series, set display_order=3, set price=49
    - _Requirements: 2.1, 3.1 (G4), 3.2, 3.3, 5.2, 5.3–5.6, 6.1–6.8, 7.1, 7.2, 7.5, 8.1–8.7, 9.1–9.4, 10.1–10.4, 11.1–11.3, 12.3, 12.5_

  - [x] 3.3 Create `mental-wellbeing-curriculum/create_g5_positive_thinking.py` — G5 intermediate curriculum on positive thinking and cognitive reframing
    - Build complete content JSON with 5 sessions, 18 vocab words: optimism, pessimism, reframe, cognitive, distortion, affirmation, self-talk, catastrophize, ruminate, growth, mindset, setback, persevere, resilient, flourish, thrive, perseverance, determination
    - Same 5-session intermediate structure
    - Description tone: `metaphor_led` (different from adjacent G4)
    - Farewell tone: `practical momentum` (different from adjacent G4)
    - Inline `validate()`, query series ID, add to series, set display_order=4, set price=49
    - _Requirements: 2.1, 3.1 (G5), 3.2, 3.3, 5.2, 5.3–5.6, 6.1–6.8, 7.1, 7.2, 7.5, 8.1–8.7, 9.1–9.4, 10.1–10.4, 11.1–11.3, 12.3, 12.5_

- [x] 4. Checkpoint — General audience series complete
  - Ensure all 5 general-audience scripts ran successfully and all curriculums are in the series with correct display orders. Ask the user if questions arise.

- [x] 5. Create medical-student beginner curriculum (M1)
  - [x] 5.1 Create `mental-wellbeing-curriculum/create_m1_med_student_intro.py` — M1 beginner curriculum on intro to mental health for med students
    - Build complete content JSON with 4 sessions, 12 vocab words: stress, pressure, exam, exhaustion, support, counselor, schedule, priority, overwhelm, cope, balance, wellbeing
    - Same 4-session beginner structure as G1/G2
    - Description tone: `bold_declaration` (different from G5 and adjacent M2)
    - Farewell tone: `quiet awe` (different from adjacent M2)
    - Inline `validate()`, query medical series ID, add to series, set display_order=0, set price=49
    - _Requirements: 2.2, 4.1 (M1), 4.2, 5.1, 5.3–5.6, 6.1–6.8, 7.1, 7.5, 8.1–8.7, 9.1–9.4, 10.1–10.4, 11.1–11.3, 12.1, 12.4, 12.5_

- [x] 6. Create medical-student preintermediate curriculums (M2–M3)
  - [x] 6.1 Create `mental-wellbeing-curriculum/create_m2_academic_burnout.py` — M2 preintermediate curriculum on academic burnout
    - Build complete content JSON with 5 sessions, 18 vocab words: burnout, fatigue, procrastination, perfectionism, deadline, motivation, discipline, self-compassion, isolation, peer, mentor, debrief, workload, symptom, chronic, recovery, boundary, recharge
    - 5-session preintermediate structure with vocabLevel3
    - Description tone: `empathetic_observation` (different from adjacent M1 and M3)
    - Farewell tone: `introspective guide` (different from adjacent M1 and M3)
    - Inline `validate()`, query medical series ID, add to series, set display_order=1, set price=49
    - _Requirements: 2.2, 4.1 (M2), 4.2, 4.3, 5.2, 5.3–5.6, 6.1–6.8, 7.1, 7.2, 7.5, 8.1–8.7, 9.1–9.4, 10.1–10.4, 11.1–11.3, 12.2, 12.4, 12.5_

  - [x] 6.2 Create `mental-wellbeing-curriculum/create_m3_compassion_fatigue.py` — M3 preintermediate curriculum on compassion fatigue
    - Build complete content JSON with 5 sessions, 18 vocab words: compassion, empathy, detachment, clinical, patient, caregiver, emotional, drain, vicarious, trauma, supervision, self-care, threshold, absorb, professional, distress, regulate, resilience
    - 5-session preintermediate structure with vocabLevel3
    - Description tone: `provocative_question` (different from adjacent M2 and M4)
    - Farewell tone: `warm accountability` (different from adjacent M2 and M4)
    - Inline `validate()`, query medical series ID, add to series, set display_order=2, set price=49
    - _Requirements: 2.2, 4.1 (M3), 4.2, 4.3, 5.2, 5.3–5.6, 6.1–6.8, 7.1, 7.2, 7.5, 8.1–8.7, 9.1–9.4, 10.1–10.4, 11.1–11.3, 12.2, 12.4, 12.5_

- [x] 7. Create medical-student intermediate curriculums (M4–M5)
  - [x] 7.1 Create `mental-wellbeing-curriculum/create_m4_clinical_psychology.py` — M4 intermediate curriculum on clinical psychology vocabulary
    - Build complete content JSON with 5 sessions, 18 vocab words: diagnosis, disorder, therapy, cognitive, behavioral, anxiety, depression, screening, intervention, prognosis, comorbidity, psychosomatic, referral, assessment, acute, remission, psychiatric, holistic
    - 5-session intermediate structure with vocabLevel3
    - Description tone: `surprising_fact` (different from adjacent M3 and M5)
    - Farewell tone: `practical momentum` (different from adjacent M3 and M5)
    - Inline `validate()`, query medical series ID, add to series, set display_order=3, set price=49
    - _Requirements: 2.2, 4.1 (M4), 4.2, 4.3, 5.2, 5.3–5.6, 6.1–6.8, 7.1, 7.2, 7.5, 8.1–8.7, 9.1–9.4, 10.1–10.4, 11.1–11.3, 12.3, 12.4, 12.5_

  - [x] 7.2 Create `mental-wellbeing-curriculum/create_m5_patient_communication.py` — M5 intermediate curriculum on patient communication about mental health
    - Build complete content JSON with 5 sessions, 18 vocab words: disclosure, stigma, confidential, consent, rapport, reassure, empathize, prescribe, compliance, follow-up, counseling, advocate, diagnose, wellbeing, coping, nurture, validate, communicate
    - 5-session intermediate structure with vocabLevel3
    - Description tone: `vivid_scenario` (different from adjacent M4)
    - Farewell tone: `team-building energy` (different from adjacent M4)
    - Inline `validate()`, query medical series ID, add to series, set display_order=4, set price=49
    - _Requirements: 2.2, 4.1 (M5), 4.2, 4.3, 5.2, 5.3–5.6, 6.1–6.8, 7.1, 7.2, 7.5, 8.1–8.7, 9.1–9.4, 10.1–10.4, 11.1–11.3, 12.3, 12.4, 12.5_

- [x] 8. Checkpoint — All 10 curriculums created
  - Ensure all 10 scripts ran successfully. Verify all curriculums are in their correct series with correct display orders, prices, and no duplicates. Ask the user if questions arise.

- [x] 9. Post-creation verification and cleanup
  - [x] 9.1 Run SQL verification queries to confirm all 10 curriculums, series membership, display orders, prices, and no duplicates
    - Verify general series has 5 curriculums with display_orders 0–4
    - Verify medical series has 5 curriculums with display_orders 0–4
    - Verify all prices are 49
    - Verify no duplicates exist (by title + uid)
    - Verify collection has both series with display_orders 0 and 1
    - Verify nothing is public (`is_public = false`)
    - _Requirements: 9.1, 9.3, 10.4, 10.5, 1.6_

  - [x] 9.2 Create `mental-wellbeing-curriculum/README.md` documenting all results
    - Collection ID, both series IDs
    - All 10 curriculum IDs with titles, levels, vocab lists
    - Tone assignments (description tone + farewell tone per curriculum)
    - Display order mapping for both series
    - SQL verification queries for finding and verifying all content
    - Recreation instructions (spec location, auth pattern, API details)
    - _Requirements: 11.4_

  - [x] 9.3 Delete all Python scripts from `mental-wellbeing-curriculum/` (only README.md remains)
    - Delete `create_setup.py` and all 10 `create_*.py` scripts
    - _Requirements: 11.5_

- [x] 10. Final checkpoint — Verify clean state
  - Ensure only README.md remains in `mental-wellbeing-curriculum/`. Ensure all SQL verification queries pass. Ask the user if questions arise.

## Notes

- All scripts use `api_helpers.py` from the repo root for API calls — no direct HTTP calls in scripts
- All IDs (collection, series) are queried from the database at runtime via MCP postgres — no hardcoded IDs
- Each script's `validate()` function enforces all 3 correctness properties (content structure, lowercase vocabList, no strip-keys) before any API call
- No PBT library is used — correctness is enforced through inline validation and post-creation SQL verification
- All content is hand-written per curriculum — no templating, string interpolation, or shared skeleton patterns
- Checkpoints ensure incremental validation after each major phase
- Each task references specific requirements for traceability
