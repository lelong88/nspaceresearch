# Requirements Document

## Introduction

Design and create a new collection of Medical English curriculums for Vietnamese-speaking university medical students learning English at the preintermediate-to-intermediate level. The collection covers clinical vocabulary, patient communication, medical research literacy, anatomy terminology, and other domains essential for healthcare professionals. Each curriculum follows the platform's established 18-word, 5-session structure with bilingual (Vietnamese/English) content, persuasive Vietnamese marketing copy, and English reading passages grounded in authentic medical contexts.

## Glossary

- **Collection**: A top-level organizational container that holds one or more Series. Stored in `curriculum_collections`.
- **Series**: A thematic grouping of Curriculums within a Collection. Has a title, description (≤ 255 chars), and display order. Stored in `curriculum_series`.
- **Curriculum**: A single learning unit containing a title, preview, description, and learning sessions with ordered activities. Stored in `curriculum` with content as JSONB.
- **Learning_Session**: An ordered group of activities within a Curriculum (e.g., "Phần 1", "Phần 2", "Ôn tập").
- **Activity**: A single learning step within a session (e.g., introAudio, viewFlashcards, reading, writingSentence).
- **Platform**: The language-learning application at helloapi.step.is that serves curriculums to learners.
- **Medical_Student**: A Vietnamese-speaking student enrolled at a University of Medicine, learning English at preintermediate-to-intermediate level.
- **Persuasive_Copy**: The multi-paragraph Vietnamese marketing text style required for curriculum descriptions, following the 5-beat structure (bold headline, concrete examples, vivid metaphor, transformation promise, learning tie-in).
- **Tone_Palette**: The six rhetorical opener types used for description variety: provocative_question, bold_declaration, vivid_scenario, empathetic_observation, surprising_fact, metaphor_led.
- **contentTypeTags**: A JSON array field on curriculum content indicating content source type. Must be `[]` for topic-based curriculums.

## Requirements

### Requirement 1: New Collection for Medical English

**User Story:** As a content manager, I want a dedicated collection for Medical English curriculums, so that medical students can find all relevant medical vocabulary content in one place, separate from general health & wellness topics.

#### Acceptance Criteria

1. THE Platform SHALL have a new collection with a Vietnamese title and English subtitle identifying it as Medical English for healthcare professionals.
2. THE Collection SHALL have a neutral, informative description summarizing its contents (not persuasive copy, per collection description rules).
3. THE Collection SHALL be separate from the existing "Sức Khỏe & Lối Sống (Health & Wellness)" collection, which covers general wellness topics.
4. THE Collection SHALL contain only vi-en curriculums at preintermediate-to-intermediate level.

### Requirement 2: Series Organization by Medical Domain

**User Story:** As a medical student, I want curriculums organized into thematic series by medical domain, so that I can focus on the vocabulary area most relevant to my current studies.

#### Acceptance Criteria

1. THE Collection SHALL contain multiple Series, each covering a distinct medical English domain.
2. THE following Series SHALL be created to cover core medical education areas:
   - **Series A — Anatomy & Body Systems**: Vocabulary for organ systems, anatomical structures, and physiological processes.
   - **Series B — Clinical Skills & Patient Communication**: Vocabulary for history-taking, physical examination, explaining diagnoses, and bedside manner in English.
   - **Series C — Diseases & Pathology**: Vocabulary for common diseases, symptoms, diagnostic terms, and pathological processes.
   - **Series D — Pharmacology & Treatment**: Vocabulary for drug classes, dosage, side effects, treatment protocols, and therapeutic terminology.
   - **Series E — Medical Research & Evidence-Based Medicine**: Vocabulary for reading journal articles, understanding study designs, statistical terms, and research methodology.
3. Each Series SHALL have a description of 255 characters or fewer.
4. Each Series description SHALL use a tone from the Tone_Palette, and no two adjacent Series within the Collection SHALL use the same tone.
5. No single tone SHALL exceed 30% of the total Series descriptions in the Collection.

### Requirement 3: Curriculum Structure and Content Standards

**User Story:** As a medical student, I want each curriculum to teach 18 medical English vocabulary words through a structured multi-session format, so that I can learn clinical terminology through reading, listening, speaking, and writing practice.

#### Acceptance Criteria

1. Each Curriculum SHALL contain exactly 18 vocabulary words divided into 3 groups of 6 words each.
2. Each Curriculum SHALL have 5 learning sessions: 3 learning sessions (one per word group), 1 review session, and 1 full-reading session.
3. Each learning session SHALL include the following activities in order: introAudio (welcome/vocab intro), viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, vocabLevel3, reading, speakReading, readAlong, writingSentence.
4. THE review session (Session 3) SHALL include introAudio (review intro), viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, vocabLevel3 for all 18 words, plus writingSentence.
5. THE full-reading session (Session 4 or 5) SHALL include introAudio (full reading intro), reading, speakReading, readAlong, writingParagraph, and a farewell introAudio.
6. Each Curriculum SHALL set `contentTypeTags` to `[]`.
7. Each Curriculum SHALL set `language` to `'en'` and `userLanguage` to `'vi'`.

### Requirement 4: Vocabulary Selection for Medical Context

**User Story:** As a medical student, I want vocabulary words that are genuinely used in clinical and academic medical settings, so that the English I learn is directly applicable to my medical education and future practice.

#### Acceptance Criteria

1. Each Curriculum's 18 vocabulary words SHALL be drawn from authentic medical English usage in the domain covered by its parent Series.
2. Vocabulary words SHALL be appropriate for preintermediate-to-intermediate learners — common medical terms that a medical student encounters in textbooks, ward rounds, and journal abstracts, not rare specialist jargon.
3. WHEN a Curriculum belongs to Series A (Anatomy & Body Systems), THE vocabulary SHALL include anatomical terms, organ names, and physiological process words (e.g., "cardiovascular", "respiratory", "inflammation", "tissue").
4. WHEN a Curriculum belongs to Series B (Clinical Skills & Patient Communication), THE vocabulary SHALL include consultation and communication terms (e.g., "symptom", "diagnosis", "prognosis", "consent").
5. WHEN a Curriculum belongs to Series C (Diseases & Pathology), THE vocabulary SHALL include disease names, symptom descriptors, and pathological terms (e.g., "chronic", "acute", "malignant", "infection").
6. WHEN a Curriculum belongs to Series D (Pharmacology & Treatment), THE vocabulary SHALL include drug-related and treatment terms (e.g., "dosage", "adverse", "prescription", "therapy").
7. WHEN a Curriculum belongs to Series E (Medical Research), THE vocabulary SHALL include research methodology and evidence-based medicine terms (e.g., "hypothesis", "placebo", "randomized", "efficacy").
8. Vocabulary words SHALL NOT duplicate across curriculums within the same Series.

### Requirement 5: Bilingual Content and Language Rules

**User Story:** As a Vietnamese-speaking medical student at preintermediate level, I want user-facing text in Vietnamese and reading passages in English, so that I can understand instructions while building my English medical reading skills.

#### Acceptance Criteria

1. THE Curriculum title SHALL be bilingual, with an English medical topic followed by a Vietnamese subtitle (e.g., "Cardiovascular System – Hệ Tim Mạch").
2. THE Curriculum description, preview text, introAudio scripts, and activity titles/descriptions SHALL be written in Vietnamese.
3. THE reading passages (reading, speakReading, readAlong activities) SHALL be written in English at a level comprehensible to preintermediate-to-intermediate learners.
4. THE writingSentence prompts SHALL be in Vietnamese, with English example sentences.
5. THE writingParagraph instructions and prompts SHALL be in Vietnamese, guiding the learner to write in English.
6. THE Curriculum title SHALL NOT include a difficulty level label.

### Requirement 6: Persuasive Marketing Copy for Curriculum Descriptions

**User Story:** As a content manager, I want each curriculum's description and preview to follow the platform's persuasive copy standards with medical-student-specific hooks, so that the content feels compelling and personally relevant to the target audience.

#### Acceptance Criteria

1. Each Curriculum description SHALL follow the 5-beat Persuasive_Copy structure: ALL-CAPS headline, concrete examples, vivid metaphor, transformation promise, and learning tie-in.
2. Each Curriculum description SHALL use a tone from the Tone_Palette for its headline opener.
3. WITHIN a Series, no two adjacent Curriculum descriptions SHALL use the same tone.
4. No single tone SHALL exceed 30% of all Curriculum descriptions across the Collection.
5. THE Persuasive_Copy SHALL reference medical-student-specific pain points and aspirations (e.g., struggling to read English textbooks, wanting to communicate with international colleagues, preparing for clinical rotations).
6. Each Curriculum preview (~150 words) SHALL name the 18 vocabulary words, describe the learning journey, and use vivid medical-context hooks.

### Requirement 7: Reading Passages Grounded in Medical Contexts

**User Story:** As a medical student, I want reading passages that cover real medical topics relevant to my studies, so that I learn vocabulary in meaningful clinical and scientific contexts rather than generic texts.

#### Acceptance Criteria

1. Each reading passage SHALL be topically aligned with the Curriculum's medical domain and vocabulary words.
2. WHEN a Curriculum covers anatomy, THE reading passages SHALL describe body systems, physiological processes, or anatomical relationships using the session's 6 vocabulary words.
3. WHEN a Curriculum covers clinical skills, THE reading passages SHALL present patient scenarios, consultation dialogues, or clinical reasoning using the session's vocabulary.
4. WHEN a Curriculum covers diseases, THE reading passages SHALL describe disease mechanisms, epidemiology, or case presentations using the session's vocabulary.
5. WHEN a Curriculum covers pharmacology, THE reading passages SHALL describe drug mechanisms, treatment protocols, or pharmacological principles using the session's vocabulary.
6. WHEN a Curriculum covers medical research, THE reading passages SHALL describe study designs, research findings, or evidence-based practice using the session's vocabulary.
7. Each reading passage SHALL be written at a level where a preintermediate-to-intermediate learner can understand approximately 95% of the text, with the 6 vocabulary words providing the remaining challenge.

### Requirement 8: Curriculum Topic Plan per Series

**User Story:** As a content manager, I want a defined list of curriculum topics for each series, so that the collection provides comprehensive coverage of medical English domains without gaps or overlaps.

#### Acceptance Criteria

1. Series A (Anatomy & Body Systems) SHALL contain curriculums covering at minimum: the cardiovascular system, the respiratory system, the digestive system, the nervous system, and the musculoskeletal system.
2. Series B (Clinical Skills & Patient Communication) SHALL contain curriculums covering at minimum: taking a patient history, physical examination vocabulary, explaining a diagnosis, discussing treatment options, and obtaining informed consent.
3. Series C (Diseases & Pathology) SHALL contain curriculums covering at minimum: infectious diseases, cardiovascular diseases, respiratory diseases, cancer and oncology, and diabetes and metabolic disorders.
4. Series D (Pharmacology & Treatment) SHALL contain curriculums covering at minimum: antibiotics and anti-infectives, pain management and analgesics, cardiovascular drugs, psychiatric medications, and surgical procedures and recovery.
5. Series E (Medical Research & Evidence-Based Medicine) SHALL contain curriculums covering at minimum: study design and methodology, clinical trials, biostatistics basics, reading a journal article, and systematic reviews and meta-analyses.
6. Each Curriculum topic SHALL be distinct and SHALL NOT substantially overlap with another Curriculum in the same Series.
7. All curriculums within a Series SHALL maintain a consistent difficulty level with a maximum of 1 level gap (preintermediate to intermediate).

### Requirement 9: Farewell Scripts with Vocabulary Review

**User Story:** As a medical student, I want the farewell audio at the end of each curriculum to review key vocabulary with fresh medical examples, so that I reinforce what I learned before moving on.

#### Acceptance Criteria

1. Each Curriculum's farewell introAudio SHALL review 5-6 key vocabulary words with definitions and fresh example sentences drawn from medical contexts.
2. Each farewell script SHALL connect the reviewed words back to the Curriculum's medical theme.
3. Each farewell script SHALL close with a warm, encouraging sign-off in Vietnamese.
4. WITHIN a Series, farewell scripts SHALL vary in emotional register, using different farewell tones (introspective guide, warm accountability, team-building energy, quiet awe, practical momentum).
5. No two adjacent Curriculums in a Series SHALL use the same farewell tone.

### Requirement 10: Series Display Order and Collection Assembly

**User Story:** As a content manager, I want all series and curriculums to have explicit display orders and be properly linked to the collection, so that the content appears in a logical sequence in the client app.

#### Acceptance Criteria

1. Each Series SHALL have an explicit display order within the Collection.
2. Each Curriculum SHALL have an explicit display order within its Series.
3. THE Series display order SHALL follow a logical pedagogical progression: Anatomy → Clinical Skills → Diseases → Pharmacology → Medical Research.
4. WITHIN each Series, Curriculums SHALL be ordered from foundational topics to more specialized topics.
5. WHEN a Curriculum is added to a Series, THE Platform SHALL set its display order via the `curriculum/setDisplayOrder` endpoint.

### Requirement 11: Creation Workflow and Documentation

**User Story:** As a content manager, I want each curriculum created via a separate Python script with proper documentation, so that the creation process is traceable and reproducible.

#### Acceptance Criteria

1. Each Curriculum SHALL be created via a separate standalone Python script (e.g., `create_anatomy_1_cardiovascular.py`).
2. Each script SHALL use `firebase_token.get_firebase_id_token()` for authentication and the `curriculum/create` API endpoint.
3. WHEN all curriculums in a Series are created, an orchestrator script SHALL create the Series, add curriculums, set display orders, and add the Series to the Collection.
4. WHEN creation is complete, all temporary scripts and JSON files SHALL be deleted.
5. A README.md SHALL be created documenting: all curriculum IDs, collection/series membership, creation method, SQL queries for retrieval, and recreation context.
6. WHEN a Curriculum is created, THE script SHALL verify against content corruption rules (correct `activityType` field names, `vocabList` not `words`, data inside `data` object, matching vocabLists for viewFlashcards/speakFlashcards).
7. Newly created curriculums SHALL remain private (no call to `setPublic` with `isPublic: true`).
