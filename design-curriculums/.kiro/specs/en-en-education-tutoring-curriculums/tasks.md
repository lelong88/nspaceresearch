# Implementation Plan: EN-EN Education & Tutoring Curriculums

## Overview

Create 2 standalone Python scripts in `en-en-education-tutoring-curriculums/`, each producing one en-en advanced curriculum via the helloapi REST API. Each script contains all hand-crafted English content inline with `build_content()`, `validate_content()`, and `main()` functions. Scripts are run once, verified in DB, then deleted — leaving only a README.

## Tasks

- [x] 1. Create "Education Is Not About Filling a Pail but Lighting a Fire" curriculum
  - [x] 1.1 Write `en-en-education-tutoring-curriculums/create_education_philosophy.py`
    - Hand-write complete curriculum content for education philosophy (en-en, concept-based)
    - Title: "Education Is Not About Filling a Pail but Lighting a Fire"
    - Description tone: `provocative_question` — ALL-CAPS headline opener as a provocative question, followed by 5-beat persuasive copy structure
    - Farewell tone: `introspective_guide` — reflective, contemplative sign-off reviewing vocabulary
    - 30 English vocabulary words across 5 sessions (6 per session):
      - Session 1: pedagogy, didactic, constructivism, scaffolding, metacognition, heuristic
      - Session 2: intrinsic, extrinsic, autonomy, self-efficacy, mastery, engagement
      - Session 3: socratic, dialectical, inquiry, facilitation, elicitation, synthesis
      - Session 4: progressive, holistic, experiential, differentiation, inclusivity, empowerment
      - Session 5: transformative, paradigm, praxis, emancipatory, conscientization, liberation
    - 5 sessions, each with exactly 11 activities in this sequence: introAudio (vocab teaching 500-800 words), viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading (800-1200+ words), speakReading, readAlong, writingSentence, writingParagraph, introAudio (wrap-up/farewell in session 5)
    - Session reading themes:
      - Session 1: The Socratic method and the art of questioning
      - Session 2: Intrinsic motivation vs. extrinsic rewards in education
      - Session 3: Dialectical inquiry and facilitation in the classroom
      - Session 4: Progressive education — Montessori, Dewey, and experiential learning
      - Session 5: Transformative education and critical pedagogy (Freire)
    - Include `contentTypeTags: []` (empty array), NO `youtubeUrl` field
    - Set `language: "en"`, `userLanguage: "en"` as top-level API body params
    - All user-facing text in English (advanced level, single-language)
    - Preview: ~150 words with vivid hook, naming vocabulary words, describing the learning journey
    - writingSentence: 4-6 items per session, each with `prompt` (context + example sentence) and `targetVocab`
    - writingParagraph: `instructions` + 2-3 analytical prompts per session using session vocabulary
    - Implement `build_content()`, `validate_content()`, `main()` functions
    - `validate_content()` checks all structural properties: 5 sessions, 11 activities per session, vocabList consistency, reading text >= 800 words, no strip keys, no youtubeUrl, activity metadata present, writing activity structure
    - Uses `sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")` and `from api_helpers import create_curriculum`
    - Prints duplicate check SQL after creation
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.10, 3.1, 3.2, 3.3, 3.4, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 5.4, 5.5, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2, 7.3, 7.4, 8.1, 8.2, 9.1, 9.2, 10.1, 10.2, 11.1, 11.2, 11.3, 11.4, 13.1, 13.2, 13.3, 13.4_

  - [x] 1.2 Run `create_education_philosophy.py` and verify curriculum exists in DB
    - Execute the script, collect the curriculum ID
    - Query DB to confirm curriculum exists with correct title and uid `zs5AMpVfqkcfDf8CJ9qrXdH58d73`
    - Verify `is_public = false`
    - Check for duplicates by title + uid (keep earliest if duplicates found)
    - Verify content structure via `curriculum/getOne`: 5 sessions, 11 activities each, vocabList arrays correct, reading text present
    - _Requirements: 1.6, 9.1, 9.2, 12.1, 12.2_

- [x] 2. Checkpoint — Education Philosophy curriculum verified
  - Ensure curriculum 1 exists in DB with correct structure, ask the user if questions arise.

- [x] 3. Create "How to Be a Good Language Tutor" curriculum
  - [x] 3.1 Write `en-en-education-tutoring-curriculums/create_language_tutoring.py`
    - Hand-write complete curriculum content for language tutoring methodology (en-en, concept-based)
    - Title: "How to Be a Good Language Tutor"
    - Description tone: `empathetic_observation` — ALL-CAPS headline opener as an empathetic observation, followed by 5-beat persuasive copy structure
    - Farewell tone: `practical_momentum` — energetic, forward-looking sign-off reviewing vocabulary
    - 30 English vocabulary words across 5 sessions (6 per session), NO overlap with curriculum 1:
      - Session 1: scaffolding, comprehensible, acquisition, proficiency, fluency, interlanguage
      - Session 2: recast, elicitation, corrective, uptake, negotiation, reformulation
      - Session 3: rapport, affective, motivation, inhibition, fossilization, plateau
      - Session 4: formative, summative, rubric, diagnostic, backwash, alignment
      - Session 5: autonomy, metacognitive, self-regulated, differentiated, adaptive, responsive
    - 5 sessions, each with exactly 11 activities in this sequence: introAudio (vocab teaching 500-800 words), viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading (800-1200+ words), speakReading, readAlong, writingSentence, writingParagraph, introAudio (wrap-up/farewell in session 5)
    - Session reading themes:
      - Session 1: Scaffolding and comprehensible input — Krashen's i+1 in tutoring
      - Session 2: Error correction strategies — recasts, elicitation, and explicit correction
      - Session 3: Rapport, affective factors, and overcoming fossilization
      - Session 4: Assessment in one-on-one tutoring — formative vs. summative approaches
      - Session 5: Building learner autonomy and adaptive instruction
    - Include `contentTypeTags: []` (empty array), NO `youtubeUrl` field
    - Set `language: "en"`, `userLanguage: "en"` as top-level API body params
    - All user-facing text in English (advanced level, single-language)
    - Preview: ~150 words with vivid hook, naming vocabulary words, describing the learning journey
    - writingSentence: 4-6 items per session, each with `prompt` (context + example sentence) and `targetVocab`
    - writingParagraph: `instructions` + 2-3 analytical prompts per session using session vocabulary
    - Implement `build_content()`, `validate_content()`, `main()` functions
    - `validate_content()` checks all structural properties (same checks as curriculum 1)
    - Uses `sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")` and `from api_helpers import create_curriculum`
    - Prints duplicate check SQL after creation
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 2.10, 3.1, 3.2, 3.3, 3.4, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 5.4, 5.6, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2, 7.3, 7.4, 8.1, 8.2, 9.1, 9.2, 10.1, 10.2, 11.1, 11.2, 11.3, 11.4, 13.1, 13.2, 13.3, 13.4_

  - [x] 3.2 Run `create_language_tutoring.py` and verify curriculum exists in DB
    - Execute the script, collect the curriculum ID
    - Query DB to confirm curriculum exists with correct title and uid `zs5AMpVfqkcfDf8CJ9qrXdH58d73`
    - Verify `is_public = false`
    - Check for duplicates by title + uid (keep earliest if duplicates found)
    - Verify content structure via `curriculum/getOne`: 5 sessions, 11 activities each, vocabList arrays correct, reading text present
    - _Requirements: 2.6, 9.1, 9.2, 12.1, 12.2_

- [x] 4. Checkpoint — Language Tutoring curriculum verified
  - Ensure curriculum 2 exists in DB with correct structure, ask the user if questions arise.

- [x] 5. Final verification and cleanup
  - [x] 5.1 Run comprehensive verification
    - Verify both curriculums exist with correct structure, language settings (`language: "en"`, `userLanguage: "en"`), and `contentTypeTags: []`
    - Verify no vocabulary overlap between the two curriculums (30 distinct words each, 60 total unique)
    - Verify both are `is_public = false`
    - Verify description tones are different (`provocative_question` vs `empathetic_observation`)
    - Verify farewell tones are different (`introspective_guide` vs `practical_momentum`)
    - Check for any duplicates across both curriculums by title + uid
    - _Requirements: 1.1, 2.1, 5.5, 5.6, 9.1, 11.4, 12.1, 12.2_

  - [x] 5.2 Delete scripts and write README
    - Delete `create_education_philosophy.py` and `create_language_tutoring.py`
    - Create `en-en-education-tutoring-curriculums/README.md` with: creation method, both curriculum IDs, SQL queries to find content in DB, vocabulary lists, tone assignments, recreation context
    - _Requirements: 10.3, 10.4_

- [x] 6. Final checkpoint — EN-EN Education & Tutoring Curriculums complete
  - Ensure both curriculums exist in DB, scripts deleted, README created, ask the user if questions arise.

## Notes

- Each curriculum script is ~800+ lines of hand-written content — no templated generation
- The two curriculums have completely distinct vocabulary sets (no overlap)
- Both curriculums are standalone private — no collection, no series, no display order
- Tone assignments: curriculum 1 uses provocative_question/introspective_guide, curriculum 2 uses empathetic_observation/practical_momentum
- All curriculums are created private (`is_public: false`) — no `setPublic` calls
- Scripts are deleted after verification, leaving only the README
- Activity sequence is identical for all sessions: introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence, writingParagraph, introAudio (11 total)
