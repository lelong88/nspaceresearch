# Requirements Document

## Introduction

Create a speaking-focus curriculum series for Vietnamese nail professionals learning to communicate with English-speaking customers. The series follows the established speaking-focus pattern (series ID `ui33faux`) but is adapted specifically for nail salon customer interactions.

Each curriculum contains 4 sessions with 15 vocabulary words total (5 per session 1–3). The learner speaks in first person ("I...") throughout — every reading passage and speaking activity is a mini-speech of 2–4 sentences that the nail technician would actually say to a customer. This is not conversational dialogue or long monologue — it is short, practical, first-person speech.

The series covers the full arc of a nail salon interaction: greeting customers, asking about preferences, describing services, handling issues, making small talk, and processing payment. Each curriculum focuses on one scenario cluster so the learner builds fluency in that specific context.

### What This Spec Covers

- Definition of the nail-professional speaking-focus curriculum series (vi-en, preintermediate to intermediate)
- Session structure following the established speaking-focus pattern
- Creation of multiple curriculums covering distinct nail salon interaction scenarios
- Series setup and organization
- Post-creation verification and cleanup

### What This Spec Does NOT Cover

- Single-language (en-en) variant — this series is bilingual vi-en only
- Changes to the existing speaking-focus series (`ui33faux`)
- Client-side UI changes

## Glossary

- **Nail_Professional_Series**: A curriculum series for Vietnamese nail technicians learning English for customer interactions. Language pair vi-en, level preintermediate to intermediate. Follows the speaking-focus pattern with first-person mini-speeches.
- **Mini_Speech**: A short first-person speech of 2–4 sentences that the nail technician would say to a customer in a specific situation. Not a dialogue, not a monologue — a practical, self-contained speech act (e.g., greeting, explaining a service, responding to a complaint).
- **Speaking_Focus_Pattern**: The established 4-session curriculum structure: sessions 1–3 each introduce 5 vocab words via introAudio → viewFlashcards → reading → readAlong → speakReading; session 4 reviews all 15 words with introAudio → viewFlashcards → reading (full story) → readAlong → speakReading.
- **Nail_Technician**: The learner persona — a Vietnamese-speaking nail professional working in an English-speaking country who needs to communicate with customers during appointments.
- **Customer_Interaction_Scenario**: A specific situation in a nail salon where the technician needs to speak English (e.g., greeting, service description, complaint handling, payment).
- **Creation_Script**: A standalone Python script that calls the helloapi REST API to create a single curriculum.
- **Series**: The curriculum series container that groups all nail-professional curriculums together.
- **Session**: One of 4 ordered segments within each curriculum.
- **Activity**: An individual learning exercise within a session.
- **Strip_Keys**: Auto-generated platform keys that must never appear in new content.
- **API**: The helloapi.step.is REST API used for all CRUD operations.
- **Display_Order**: Integer field controlling sort position of curriculums within a series.
- **Persuasive_Copy**: The required emotional sales copy style for all learner-facing text.

## Requirements

### Requirement 1: Session Structure — Speaking-Focus Pattern for Nail Professionals

**User Story:** As a content manager, I want each nail-professional curriculum to follow the established 4-session speaking-focus pattern, so that the structure is consistent with the existing speaking-focus series and learners experience a familiar progression.

#### Acceptance Criteria

1. THE Nail_Professional_Series curriculum SHALL contain exactly 4 sessions per curriculum.
2. THE Nail_Professional_Series curriculum SHALL contain exactly 15 vocabulary words divided into 3 groups of 5 (W1 for Session 1, W2 for Session 2, W3 for Session 3).
3. WHEN Session 1 is created, THE Session SHALL contain activities in this exact order: `introAudio` → `viewFlashcards` (5 words) → `reading` → `readAlong` → `speakReading`.
4. WHEN Session 2 is created, THE Session SHALL contain activities in this exact order: `introAudio` → `viewFlashcards` (5 words) → `reading` → `readAlong` → `speakReading`.
5. WHEN Session 3 is created, THE Session SHALL contain activities in this exact order: `introAudio` → `viewFlashcards` (5 words) → `reading` → `readAlong` → `speakReading`.
6. WHEN Session 4 (review) is created, THE Session SHALL contain activities in this exact order: `introAudio` (recap all 15 words) → `viewFlashcards` (all 15 words) → `reading` (full combined passage) → `readAlong` → `speakReading`.

### Requirement 2: Mini-Speech Reading Passages — First Person, 2–4 Sentences

**User Story:** As a content manager, I want every reading passage to be a short first-person mini-speech that a nail technician would actually say to a customer, so that learners practice realistic, immediately usable English.

#### Acceptance Criteria

1. THE reading passage in each session (1–3) SHALL be a first-person mini-speech of 2–4 sentences written from the nail technician's perspective speaking to a customer.
2. THE reading passage SHALL use "I" as the subject throughout — the learner speaks as themselves, not narrating about someone else.
3. THE reading passage SHALL be situationally specific to the curriculum's Customer_Interaction_Scenario (e.g., greeting a walk-in, explaining gel options, responding to a complaint about nail shape).
4. THE reading passage SHALL incorporate all 5 vocabulary words for that session naturally within the 2–4 sentences.
5. THE Session 4 reading passage SHALL combine the scenario threads from Sessions 1–3 into a cohesive first-person mini-speech of 6–12 sentences that uses all 15 vocabulary words.
6. THE reading passage SHALL NOT be a dialogue (no customer lines), a long monologue (more than 4 sentences per session 1–3), or a third-person narrative.

### Requirement 3: Vocabulary Selection — Nail Salon Professional English

**User Story:** As a content manager, I want vocabulary words to be practical English terms that nail technicians actually need when speaking to customers, so that learners build immediately useful professional vocabulary.

#### Acceptance Criteria

1. THE vocabulary words SHALL be English words and phrases that a nail technician uses when communicating with customers during appointments.
2. THE vocabulary words SHALL be at the preintermediate to intermediate level — familiar refreshers that a Vietnamese nail professional has likely encountered but needs practice producing in speech.
3. THE vocabulary words SHALL be relevant to the specific Customer_Interaction_Scenario of the curriculum (e.g., a curriculum about nail services uses words like "gel", "polish", "shape", "file"; a curriculum about greetings uses words like "welcome", "appointment", "prefer", "seat").
4. THE vocabulary words SHALL be lowercase strings in the `vocabList` field — never objects, numbers, or other types.
5. THE Nail_Professional_Series SHALL NOT repeat vocabulary words across curriculums within the series — each curriculum introduces 15 unique words.

### Requirement 4: Curriculum Topics — Nail Salon Interaction Scenarios

**User Story:** As a content manager, I want the series to cover the full arc of nail salon customer interactions across multiple curriculums, so that learners can handle any common situation they encounter at work.

#### Acceptance Criteria

1. THE Nail_Professional_Series SHALL contain multiple curriculums, each focused on a distinct Customer_Interaction_Scenario.
2. THE curriculum topics SHALL cover the following interaction categories across the series: greeting and seating customers, asking about nail preferences and styles, describing nail services and options, handling customer concerns or complaints, making small talk during appointments, and processing payment and checkout.
3. THE curriculum titles SHALL be minimal — the series title provides context, so individual curriculum titles only name the specific scenario (e.g., "Chào Khách và Hỏi Ý", "Tư Vấn Dịch Vụ", "Xử Lý Phàn Nàn").
4. THE curriculum titles SHALL NOT include difficulty level descriptors, series name repetition, content type prefixes, skill-focus labels, or audience suffixes.

### Requirement 5: Content Quality — Persuasive Copy and Tone Variety

**User Story:** As a content manager, I want all learner-facing text to follow the persuasive copy style with varied tones, so that nail professionals feel emotionally engaged and motivated to improve their English speaking skills.

#### Acceptance Criteria

1. THE series description SHALL be a short persuasive hook of 255 characters or fewer, using one of the 6 tones from the tone palette.
2. THE curriculum description SHALL follow the 5-beat persuasive copy structure: bold headline, concrete examples from nail salon life, vivid metaphor, promise of transformation, and tie to personal growth.
3. THE curriculum description SHALL use one of the 6 tones from the tone palette for its ALL-CAPS headline opener, and adjacent curriculums within the series SHALL use different tones.
4. THE curriculum preview (~150 words) SHALL open with a vivid hook about the nail professional's communication challenge, name the 15 vocabulary words, and describe the speaking progression across sessions.
5. WHEN an introAudio activity is created, THE introAudio script SHALL be written in Vietnamese, teaching vocabulary with pronunciation guidance and connecting words to the specific nail salon scenario.
6. THE farewell introAudio in Session 4 SHALL vary in emotional register across curriculums (using introspective guide, warm accountability, team-building energy, quiet awe, or practical momentum), review 5–6 key vocabulary words with definitions and fresh example sentences, and close with a warm personal sign-off.

### Requirement 6: introAudio Content for Nail Professional Curriculums

**User Story:** As a content manager, I want introAudio scripts to teach vocabulary in the context of nail salon work, so that learners understand how each word connects to their daily professional interactions.

#### Acceptance Criteria

1. WHEN an introAudio is created for Sessions 1–3, THE script SHALL teach the 5 vocabulary words for that session with: part of speech, definition in Vietnamese, an example sentence showing the word used in a nail salon context, and pronunciation guidance.
2. WHEN an introAudio is created for Session 4 (review), THE script SHALL recap all 15 vocabulary words, connecting them back to the full Customer_Interaction_Scenario covered in the curriculum.
3. THE introAudio scripts SHALL be written in Vietnamese (the learner's native language) with English vocabulary words and example sentences embedded.
4. WHEN the farewell introAudio is created for Session 4, THE script (400–600 words) SHALL review vocabulary with definitions and fresh nail-salon example sentences, summarize the speaking progression, and provide a warm farewell encouraging the learner to use the words at work.

### Requirement 7: Activity Metadata and Schema Compliance

**User Story:** As a content manager, I want every activity to have proper metadata and follow the content schema, so that the platform renders correctly and no corruption occurs.

#### Acceptance Criteria

1. THE Activity SHALL include both a `title` and `description` field for every activity in every session.
2. WHEN a `viewFlashcards` activity is created, THE Activity title SHALL follow the format "Flashcards: <topic>" and the description SHALL follow the format "Học N từ: word1, word2, ...".
3. WHEN a `reading` or `speakReading` activity is created, THE Activity title SHALL follow the format "Đọc: <topic>" and the description SHALL contain the first ~80 characters of the reading text.
4. WHEN a `readAlong` activity is created, THE Activity title SHALL follow the format "Nghe: <topic>" and the description SHALL be "Nghe đoạn văn vừa đọc và theo dõi."
5. WHEN an `introAudio` activity is created, THE Activity title SHALL be a descriptive label (e.g., "Giới thiệu bài học", "Giới thiệu từ vựng") and the description SHALL be a brief summary.
6. THE Session object SHALL include a `title` field (e.g., "Phần 1", "Phần 2", "Phần 3", "Ôn tập").
7. THE Activity SHALL use `activityType` as the field name — never `type`.
8. THE Activity SHALL place all content fields inside a `data` object — never inline on the activity.
9. THE `viewFlashcards` activity SHALL use `vocabList` as the field name for the word array — never `words`.
10. THE `reading`, `speakReading`, and `readAlong` activities SHALL include a `data.text` field containing the passage text.
11. THE `introAudio` activity SHALL include a `data.text` field containing the script text.

### Requirement 8: Top-Level Curriculum Content Structure

**User Story:** As a content manager, I want the top-level curriculum content JSON to include all required fields, so that the platform can display and process the curriculum correctly.

#### Acceptance Criteria

1. THE curriculum content JSON SHALL include a `title` field (non-empty string).
2. THE curriculum content JSON SHALL include a `description` field (non-empty string, multi-paragraph persuasive copy).
3. THE curriculum content JSON SHALL include a `preview` object with a `text` field (non-empty string, ~150 words).
4. THE curriculum content JSON SHALL include a `learningSessions` array with exactly 4 session objects.
5. THE curriculum content JSON SHALL include `"contentTypeTags": []` (empty array).

### Requirement 9: Strip-Keys Compliance

**User Story:** As a content manager, I want new curriculum content to never include auto-generated platform keys, so that the platform correctly generates fresh metadata after upload.

#### Acceptance Criteria

1. THE curriculum content SHALL NOT include any of the following auto-generated keys: `mp3Url`, `illustrationSet`, `chapterBookmarks`, `segments`, `whiteboardItems`, `userReadingId`, `lessonUniqueId`, `curriculumTags`, `taskId`, `imageId`.

### Requirement 10: Series Creation and Organization

**User Story:** As a content manager, I want the nail-professional curriculums organized in a series, so that learners can discover and progress through the full set of nail salon interaction scenarios.

#### Acceptance Criteria

1. WHEN the series is created, THE API SHALL be called via `curriculum-series/create` with a Vietnamese title, a Vietnamese description (under 255 characters using one of the 6 tones), and the series SHALL be kept private until all curriculums are ready.
2. WHEN a curriculum is added to the series via `curriculum-series/addCurriculum`, THE Creation_Script SHALL call `curriculum/setDisplayOrder` to assign a sequential integer display order reflecting the natural progression of nail salon interactions.
3. THE series SHALL contain curriculums with homogeneous `language: "en"` and `userLanguage: "vi"`.
4. THE series SHALL contain curriculums within a maximum 1-level gap from the highest-level curriculum in the series.

### Requirement 11: API Call Compliance

**User Story:** As a content manager, I want all API calls to follow the platform's requirements, so that curriculum creation succeeds without errors.

#### Acceptance Criteria

1. THE Creation_Script SHALL set `language: "en"` and `userLanguage: "vi"` as top-level body parameters in the `curriculum/create` API call (not only inside the content JSON).
2. THE Creation_Script SHALL authenticate using `firebase_token.get_firebase_id_token("zs5AMpVfqkcfDf8CJ9qrXdH58d73")` for all API calls.
3. WHEN a curriculum is created via `curriculum/create`, THE curriculum SHALL have `is_public: false` (the platform default).
4. THE Creation_Script SHALL NOT call `curriculum/setPublic` with `isPublic: true` on any newly created curriculum.

### Requirement 12: Script Organization and Documentation

**User Story:** As a content manager, I want one Python script per curriculum with all text content hand-written, so that each curriculum's content is self-contained and individually crafted.

#### Acceptance Criteria

1. THE Creation_Script architecture SHALL use one Python script per curriculum with all text content hand-written in that script.
2. THE Creation_Script architecture SHALL include one orchestrator script that handles series creation, adding curriculums to the series, and setting display orders.
3. THE Creation_Script SHALL NOT use template functions, string interpolation, or loops to generate learner-facing text content.
4. THE Creation_Script MAY use shared helper functions for activity structure (types, order, data schema) but SHALL hand-write all text content per curriculum.
5. WHEN all curriculums in the series are successfully created, THE workspace SHALL contain a `nail-professional-speaking-curriculum/` folder with a README.md documenting: series ID and title, curriculum IDs and titles, display orders, how content was created, SQL queries to find the curriculums in the DB, and enough context to recreate if needed.
6. WHEN all curriculums are verified in the database, THE source Python scripts SHALL be deleted from the folder, leaving only the README.

### Requirement 13: No Templated Content

**User Story:** As a content manager, I want every piece of learner-facing text to be individually crafted per curriculum topic, so that each curriculum reads as if written by someone who deeply understands that specific nail salon scenario.

#### Acceptance Criteria

1. THE Creation_Script SHALL NOT use `f-string` interpolation, template functions, or shared text skeletons to generate introAudio scripts, descriptions, previews, reading passages, or any learner-facing text.
2. EACH curriculum's reading passages SHALL reflect the specific vocabulary and scenario of that curriculum — not generic nail salon text with words swapped in.
3. EACH curriculum's introAudio scripts SHALL teach vocabulary with scenario-specific examples that a nail technician would recognize from their daily work.

### Requirement 14: Cross-Curriculum Consistency Within the Series

**User Story:** As a content manager, I want all curriculums in the series to maintain consistent quality and structure while covering distinct scenarios, so that the series feels cohesive and progressively builds the learner's professional English.

#### Acceptance Criteria

1. THE Nail_Professional_Series SHALL order curriculums from simpler interactions (greeting, seating) to more complex ones (handling complaints, small talk) via display order.
2. THE Nail_Professional_Series SHALL maintain consistent session structure across all curriculums (same activity types and order per the Speaking_Focus_Pattern).
3. THE Nail_Professional_Series SHALL ensure no vocabulary word is repeated across curriculums within the series.
4. THE Nail_Professional_Series SHALL use the same language pair (`language: "en"`, `userLanguage: "vi"`) and level range (preintermediate to intermediate) across all curriculums.
