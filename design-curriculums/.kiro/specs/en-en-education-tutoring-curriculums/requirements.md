# Requirements Document

## Introduction

Create 2 en-en advanced-level curriculums exploring education and tutoring philosophy, each with 5 substantial learning sessions (5+ hours of content per curriculum). The curriculums are concept-based (no podcast/movie/song source material) and cover:

1. **"Education is not about filling a pail but lighting a fire"** — Exploring the philosophy of education as inspiration vs. information transfer. Examines progressive education theory, intrinsic motivation, Socratic method, constructivism, and the tension between standardized instruction and transformative learning.

2. **"How to be a good language tutor"** — Practical insights on effective language tutoring. Covers scaffolding techniques, error correction strategies, learner autonomy, rapport building, comprehensible input theory, and the art of adaptive instruction.

### Language & Level

- **Language pair:** en-en (`language: "en"`, `userLanguage: "en"`)
- **Level:** Advanced (single-language only — all text in English)
- **contentTypeTags:** `[]` (concept-based, no media source)

### Curriculum Structure (Both Curriculums)

Each curriculum has 5 learning sessions with balanced skills (reading, listening, speaking, writing) in every session. For 5+ hours of content per curriculum, each session must be substantial:

- **30+ vocabulary words total per curriculum** (6+ per session)
- **Long reading passages** (800-1200+ words each)
- **Multiple writing activities per session** (both sentence-level and paragraph-level)
- **Extended introAudio scripts** (500-800 words for vocabulary teaching)
- **Balanced activity types in every session:** introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence, writingParagraph

### What This Spec Covers

- Creation of 2 new en-en advanced curriculums
- One Python script per curriculum
- Persuasive copy descriptions with 6-tone palette variety
- Post-creation verification and duplicate checking
- Source cleanup after successful creation (keep only README.md)

### What This Spec Does NOT Cover

- Collection or series creation (these are standalone curriculums created private)
- Making any curriculum public
- Audio/illustration generation pipeline
- Client-side UI changes

## Glossary

- **Curriculum**: A single learning unit with vocabulary words, sessions, and activities, stored as JSON content in the database.
- **Session**: An ordered segment within a curriculum containing a sequence of activities.
- **Activity**: An individual learning exercise within a session (introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence, writingParagraph).
- **Creation_Script**: A standalone Python script that calls the helloapi REST API to create a single curriculum.
- **Strip_Keys**: The set of auto-generated platform keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId) that must never appear in new content.
- **Persuasive_Copy**: The required emotional sales copy style for all learner-facing text, following the 5-beat structure defined in CURRICULUM_QUALITY_STANDARDS.md.
- **VocabList**: An array of lowercase strings on vocab activities listing the vocabulary words for that activity.
- **Balanced_Skills**: The requirement that each session includes reading, listening (readAlong/introAudio), speaking (speakFlashcards/speakReading), and writing (writingSentence/writingParagraph) activities.
- **Tone_Palette**: The 6 rhetorical opener types (provocative_question, bold_declaration, vivid_scenario, empathetic_observation, surprising_fact, metaphor_led) used to vary description style.

## Requirements

### Requirement 1: "Education Is Not About Filling a Pail but Lighting a Fire" Curriculum

**User Story:** As a content manager, I want to create an en-en advanced curriculum exploring the philosophy of education as inspiration vs. information transfer, so that English-speaking learners can build sophisticated vocabulary while examining transformative education theory.

#### Acceptance Criteria

1. THE Curriculum SHALL contain at least 30 English vocabulary words distributed across 5 sessions (6+ words per session), all related to education philosophy, pedagogy, intrinsic motivation, and transformative learning.
2. THE Curriculum SHALL contain exactly 5 learningSessions, each with Balanced_Skills coverage (reading, listening, speaking, and writing activities).
3. WHEN each session is created, THE Session SHALL include at minimum: introAudio (topic introduction), introAudio (vocabulary teaching, 500-800 words), viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading (800-1200+ words), speakReading, readAlong, writingSentence, and writingParagraph.
4. THE Curriculum content SHALL include `contentTypeTags: []` (empty array).
5. THE Curriculum content SHALL NOT include a `youtubeUrl` field.
6. THE Curriculum SHALL set `language: "en"` and `userLanguage: "en"` as top-level body parameters in the API call.
7. THE Curriculum SHALL use English for all user-facing text (title, description, preview, introAudio scripts, writing prompts, reading passages).
8. THE Reading passages SHALL be original educational content exploring themes such as: the Socratic method, constructivism vs. direct instruction, intrinsic vs. extrinsic motivation, Montessori and progressive education, the role of curiosity, student-centered learning, and the limits of standardized testing.
9. THE Curriculum content SHALL provide 5+ hours of learning material through substantial reading passages, extended vocabulary teaching scripts, and multiple writing activities per session.
10. WHEN viewFlashcards and speakFlashcards appear in the same session, THE Activities SHALL have identical vocabList arrays.

### Requirement 2: "How to Be a Good Language Tutor" Curriculum

**User Story:** As a content manager, I want to create an en-en advanced curriculum on effective language tutoring practices, so that English-speaking learners can build sophisticated vocabulary while gaining practical insights into the art and science of language instruction.

#### Acceptance Criteria

1. THE Curriculum SHALL contain at least 30 English vocabulary words distributed across 5 sessions (6+ words per session), all related to language pedagogy, tutoring methodology, scaffolding, error correction, and learner autonomy.
2. THE Curriculum SHALL contain exactly 5 learningSessions, each with Balanced_Skills coverage (reading, listening, speaking, and writing activities).
3. WHEN each session is created, THE Session SHALL include at minimum: introAudio (topic introduction), introAudio (vocabulary teaching, 500-800 words), viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading (800-1200+ words), speakReading, readAlong, writingSentence, and writingParagraph.
4. THE Curriculum content SHALL include `contentTypeTags: []` (empty array).
5. THE Curriculum content SHALL NOT include a `youtubeUrl` field.
6. THE Curriculum SHALL set `language: "en"` and `userLanguage: "en"` as top-level body parameters in the API call.
7. THE Curriculum SHALL use English for all user-facing text (title, description, preview, introAudio scripts, writing prompts, reading passages).
8. THE Reading passages SHALL be original educational content exploring themes such as: scaffolding and the zone of proximal development in tutoring, comprehensible input (Krashen's i+1), error correction strategies (recasts, elicitation, explicit correction), building learner autonomy, rapport and affective factors, adaptive instruction, and formative assessment in one-on-one settings.
9. THE Curriculum content SHALL provide 5+ hours of learning material through substantial reading passages, extended vocabulary teaching scripts, and multiple writing activities per session.
10. WHEN viewFlashcards and speakFlashcards appear in the same session, THE Activities SHALL have identical vocabList arrays.

### Requirement 3: VocabList on Vocab Activities

**User Story:** As a content manager, I want every vocab-related activity to have a properly formatted vocabList, so that the platform can correctly track vocabulary progress.

#### Acceptance Criteria

1. WHEN a `viewFlashcards`, `speakFlashcards`, `vocabLevel1`, or `vocabLevel2` activity is created, THE Activity SHALL include a `vocabList` field containing an array of lowercase strings listing the vocabulary words for that activity.
2. THE `vocabList` field SHALL contain at least 6 words per activity (matching the vocabulary group for that session).
3. THE `vocabList` SHALL use the field name `vocabList` — never `words`.
4. THE `vocabList` values SHALL be lowercase strings — never objects, numbers, or mixed case.

### Requirement 4: Activity Metadata

**User Story:** As a content manager, I want every activity and session to have proper title and description fields, so that server-side logging and client display work correctly.

#### Acceptance Criteria

1. THE Activity SHALL include `title` and `description` fields for every activity in every session.
2. WHEN a `viewFlashcards`, `speakFlashcards`, `vocabLevel1`, or `vocabLevel2` activity is created, THE Activity title SHALL follow the format "Flashcards: <topic>" and the description SHALL list the words being learned.
3. WHEN a `reading` or `speakReading` activity is created, THE Activity title SHALL follow the format "Read: <topic>" and the description SHALL summarize the passage content.
4. WHEN a `readAlong` activity is created, THE Activity title SHALL follow the format "Listen: <topic>" and the description SHALL indicate the learner is listening to the passage.
5. WHEN an `introAudio` activity is created, THE Activity title SHALL be a descriptive label and the description SHALL be a brief summary.
6. WHEN a `writingSentence` or `writingParagraph` activity is created, THE Activity title SHALL follow the format "Write: <topic>" and the description SHALL summarize the writing task.
7. THE Session object SHALL include a `title` field (e.g., "Session 1", "Session 2", etc.).

### Requirement 5: Content Quality — Persuasive Copy

**User Story:** As a content manager, I want all learner-facing text to follow the persuasive copy style with tone variety, so that learners feel emotionally engaged and the descriptions avoid monotonous patterns.

#### Acceptance Criteria

1. THE Curriculum description SHALL follow the 5-beat persuasive copy structure: bold ALL-CAPS headline, concrete personal examples, vivid metaphor, transformation promise, and dual growth tie-in (language + thinking).
2. THE Curriculum preview (~150 words) SHALL open with a vivid hook, name the vocabulary words, describe the learning journey, and read as compelling marketing copy.
3. WHEN introAudio vocabulary teaching scripts are created (one per session), EACH script (500-800 words) SHALL teach each vocabulary word individually with part of speech, definition, example sentence from the reading context, and smooth transitions.
4. WHEN the final session's farewell introAudio script is created, THE script SHALL review 5-6 key vocabulary words with definitions and fresh example sentences, connect words back to the curriculum theme, and close with a warm personal sign-off.
5. THE 2 curriculum descriptions SHALL use different tones from the 6-tone palette (provocative_question, bold_declaration, vivid_scenario, empathetic_observation, surprising_fact, metaphor_led).
6. THE 2 farewell introAudio scripts SHALL use different emotional registers (introspective guide, warm accountability, team-building energy, quiet awe, practical momentum).

### Requirement 6: Writing Activities — Sentence and Paragraph

**User Story:** As a content manager, I want writing activities to have properly structured data, so that the platform can present clear prompts and track vocabulary usage in writing.

#### Acceptance Criteria

1. WHEN a `writingSentence` activity is created, THE Activity data SHALL include `vocabList` (array of lowercase strings), and `items` (array where each item has `prompt` and `targetVocab` fields).
2. WHEN a `writingParagraph` activity is created, THE Activity data SHALL include `vocabList` (array of lowercase strings), `instructions` (non-empty string), and `prompts` (array of strings with length >= 2).
3. THE writingSentence prompts SHALL specify context for using the target word and include an example sentence showing correct usage.
4. THE writingParagraph prompts SHALL be specific to the session's topic and guide the learner to use vocabulary in meaningful analytical writing.

### Requirement 7: Reading and Audio Activities

**User Story:** As a content manager, I want reading and audio activities to have substantial text content, so that learners get extended exposure to vocabulary in context.

#### Acceptance Criteria

1. WHEN a `reading`, `speakReading`, or `readAlong` activity is created, THE Activity data SHALL include a `text` field containing a non-empty string.
2. WHEN an `introAudio` activity is created, THE Activity data SHALL include a `text` field containing a non-empty string.
3. THE reading activity text SHALL be 800-1200+ words of original educational content relevant to the session's theme.
4. THE speakReading and readAlong activities in the same session SHALL use the same text as the reading activity (the learner speaks/listens to what they read).

### Requirement 8: Strip-Keys Compliance

**User Story:** As a content manager, I want new curriculum content to never include auto-generated platform keys, so that the platform correctly generates fresh metadata after upload.

#### Acceptance Criteria

1. THE Curriculum content SHALL NOT include any of the following auto-generated keys: `mp3Url`, `illustrationSet`, `chapterBookmarks`, `segments`, `whiteboardItems`, `userReadingId`, `lessonUniqueId`, `curriculumTags`, `taskId`, `imageId`.
2. IF an existing curriculum is fetched via API to use as a structural template, THEN THE Creation_Script SHALL strip all auto-generated keys from the fetched content before using it as input for `curriculum/create`.

### Requirement 9: Privacy — All Curriculums Created Private

**User Story:** As a content manager, I want all newly created curriculums to be private by default, so that they go through content generation (audio, illustrations) before being exposed to learners.

#### Acceptance Criteria

1. WHEN a curriculum is created via `curriculum/create`, THE Curriculum SHALL have `is_public: false` (the platform default).
2. THE Creation_Script SHALL NOT call `curriculum/setPublic` with `isPublic: true` on any newly created curriculum.

### Requirement 10: Script Organization and Cleanup

**User Story:** As a content manager, I want one Python script per curriculum with proper cleanup after creation, so that each curriculum's content is self-contained and the workspace stays clean.

#### Acceptance Criteria

1. THE Creation_Script architecture SHALL use one Python script per curriculum with all text content hand-written in that script.
2. THE Creation_Script SHALL NOT use template functions, string interpolation, or loops to generate learner-facing text content.
3. WHEN both curriculums are successfully created and verified in the database, THE source Python scripts SHALL be deleted, leaving only a README.md with creation method, curriculum IDs, SQL queries, and recreation context.
4. THE workspace SHALL contain a dedicated folder `en-en-education-tutoring-curriculums/` for the project.

### Requirement 11: No Templated Content

**User Story:** As a content manager, I want every piece of learner-facing text to be individually crafted per curriculum, so that each curriculum reads as if written by a subject-matter expert who deeply understands the specific topic.

#### Acceptance Criteria

1. THE Creation_Script SHALL NOT use `f-string` interpolation, template functions, or shared text skeletons to generate introAudio scripts, reading passages, descriptions, previews, or writing prompts.
2. EACH Curriculum's reading passages SHALL be original content exploring the topic from a unique angle — not adaptations or rewrites of the other curriculum's passages.
3. EACH Curriculum's introAudio scripts SHALL be individually crafted to teach vocabulary in a way that resonates with the specific topic's intellectual framework.
4. THE "Education as Inspiration" curriculum SHALL NOT reuse vocabulary words from the "Good Language Tutor" curriculum — each SHALL have a distinct vocabulary set.

### Requirement 12: Duplicate Check After Creation

**User Story:** As a content manager, I want to check for duplicate curriculums after creation, so that accidental re-runs of scripts do not create duplicate entries.

#### Acceptance Criteria

1. WHEN a curriculum is created, THE Creation_Script SHALL query the database for curriculums with the same title owned by the same user.
2. IF duplicates are found, THEN THE Creation_Script SHALL report the duplicates and keep the earliest-created one.

### Requirement 13: Content Corruption Compliance

**User Story:** As a content manager, I want all curriculum content to pass the content corruption detection rules, so that the platform renders activities correctly without data integrity issues.

#### Acceptance Criteria

1. THE Curriculum content SHALL have a top-level structure with `title` (non-empty string), `description` (non-empty string), `preview` (object with `text` as non-empty string), and `learningSessions` (array with length = 5).
2. EACH Activity SHALL use the field name `activityType` — never `type`.
3. EACH Activity SHALL have a `data` field (object) containing all content fields — content fields SHALL NOT be placed inline on the activity object.
4. THE `activityType` values SHALL be one of: `introAudio`, `viewFlashcards`, `speakFlashcards`, `vocabLevel1`, `vocabLevel2`, `reading`, `speakReading`, `readAlong`, `writingSentence`, `writingParagraph`.
