# Requirements Document

## Introduction

Create 2 new English-learning curriculums for Vietnamese speakers at the preintermediate level, following the same 4-session speaking-focus pattern as the nail-professional-speaking-curriculum series (series ID `mdntfeac`). Language pair: userLanguage="vi", language="en".

These curriculums cover general daily-life topics about describing people:
1. **Tính Cách** (Describing Personalities) — vocabulary and mini-speeches for describing people's character traits
2. **Ngoại Hình** (Describing Appearances) — vocabulary and mini-speeches for describing how people look

Unlike the nail-professional series (which targets nail technicians speaking to customers), these curriculums target general Vietnamese English learners describing friends, family, and colleagues in everyday conversation. The reading passages are first-person descriptions of people the learner knows.

### What This Spec Covers

- 2 individually crafted curriculums for vi-en preintermediate learners
- 4-session speaking-focus structure (identical to nail-professional pattern)
- 15 vocabulary words per curriculum (5 per session 1–3, all 15 in session 4 review)
- First-person mini-speech reading passages (describing people you know)
- Vietnamese introAudio scripts teaching vocab in context of describing people
- Optional series creation to group the 2 curriculums together
- Post-creation verification and cleanup

### What This Spec Does NOT Cover

- Changes to the existing nail-professional series
- Nail salon or professional English context (these are general daily life)
- Client-side UI changes
- Content generation pipeline (audio, illustrations) — curriculums are created private
- Advanced or intermediate difficulty levels

## Glossary

- **Personality_Curriculum**: The curriculum focused on describing people's character traits (tính cách). Contains 15 vocabulary words related to personality adjectives and character descriptions.
- **Appearance_Curriculum**: The curriculum focused on describing people's physical appearance (ngoại hình). Contains 15 vocabulary words related to how people look.
- **Speaking_Focus_Pattern**: The established 4-session curriculum structure: sessions 1–3 each introduce 5 vocab words via introAudio → viewFlashcards → reading → readAlong → speakReading; session 4 reviews all 15 words with introAudio → viewFlashcards → reading (full passage) → readAlong → speakReading.
- **Mini_Speech**: A short first-person speech of 2–4 sentences describing a person the learner knows (friend, family member, colleague). Not a dialogue, not a monologue — a practical, self-contained descriptive speech act.
- **Creation_Script**: A standalone Python script that calls the helloapi REST API to create a single curriculum. All text content is hand-written in the script.
- **Series**: An optional curriculum series container that groups the 2 personality/appearance curriculums together.
- **Session**: One of 4 ordered segments within each curriculum.
- **Activity**: An individual learning exercise within a session.
- **Strip_Keys**: Auto-generated platform keys that must never appear in new content (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId).
- **API**: The helloapi.step.is REST API used for all CRUD operations.
- **Display_Order**: Integer field controlling sort position of curriculums within a series.
- **Persuasive_Copy**: The required emotional sales copy style for all learner-facing marketing text.
- **Tone_Palette**: The 6 rhetorical opener types: provocative_question, bold_declaration, vivid_scenario, empathetic_observation, surprising_fact, metaphor_led.
- **Farewell_Palette**: The 5 emotional registers for farewell introAudio scripts: introspective_guide, warm_accountability, team_building_energy, quiet_awe, practical_momentum.
- **Language_Pair**: userLanguage="vi", language="en" — Vietnamese speakers learning English.

## Requirements

### Requirement 1: Session Structure — Speaking-Focus Pattern

**User Story:** As a content manager, I want each curriculum to follow the established 4-session speaking-focus pattern, so that the structure is consistent with the nail-professional series and learners experience a familiar progression.

#### Acceptance Criteria

1. THE Personality_Curriculum SHALL contain exactly 4 sessions.
2. THE Appearance_Curriculum SHALL contain exactly 4 sessions.
3. EACH curriculum SHALL contain exactly 15 vocabulary words divided into 3 groups of 5 (W1 for Session 1, W2 for Session 2, W3 for Session 3).
4. WHEN Session 1 is created, THE Session SHALL contain activities in this exact order: `introAudio` → `viewFlashcards` (5 words) → `reading` → `readAlong` → `speakReading`.
5. WHEN Session 2 is created, THE Session SHALL contain activities in this exact order: `introAudio` → `viewFlashcards` (5 words) → `reading` → `readAlong` → `speakReading`.
6. WHEN Session 3 is created, THE Session SHALL contain activities in this exact order: `introAudio` → `viewFlashcards` (5 words) → `reading` → `readAlong` → `speakReading`.
7. WHEN Session 4 (review) is created, THE Session SHALL contain activities in this exact order: `introAudio` (recap all 15 words) → `viewFlashcards` (all 15 words) → `reading` (full combined passage) → `readAlong` → `speakReading`.

### Requirement 2: Mini-Speech Reading Passages — First Person, Describing People

**User Story:** As a content manager, I want every reading passage to be a short first-person mini-speech describing a person the learner knows, so that learners practice realistic, immediately usable English for daily conversation.

#### Acceptance Criteria

1. THE reading passage in each session (1–3) SHALL be a first-person Mini_Speech of 2–4 sentences describing a person the learner knows (friend, family member, colleague, neighbor).
2. THE reading passage SHALL use "I" or "My" as the starting perspective — the learner speaks about someone they know, not narrating abstractly.
3. THE reading passage in the Personality_Curriculum SHALL describe character traits and behaviors of people (e.g., "My friend is very outgoing. She always smiles and talks to everyone...").
4. THE reading passage in the Appearance_Curriculum SHALL describe physical features and how people look (e.g., "My brother is tall and slim. He has short curly hair...").
5. THE reading passage SHALL incorporate all 5 vocabulary words for that session naturally within the 2–4 sentences.
6. THE Session 4 reading passage SHALL combine the descriptive threads from Sessions 1–3 into a cohesive first-person passage of 6–12 sentences that uses all 15 vocabulary words.
7. THE reading passage SHALL NOT be a dialogue (no other person's lines), a long monologue (more than 4 sentences per session 1–3), or a third-person narrative.

### Requirement 3: Vocabulary Selection — Describing People

**User Story:** As a content manager, I want vocabulary words to be practical English terms for describing personalities and appearances, so that learners build immediately useful vocabulary for daily conversation about people.

#### Acceptance Criteria

1. THE Personality_Curriculum vocabulary words SHALL be English adjectives and verbs used to describe character traits and behaviors (e.g., outgoing, shy, generous, patient, stubborn, honest, cheerful, calm, confident, creative, reliable, thoughtful, ambitious, easygoing, sensitive).
2. THE Appearance_Curriculum vocabulary words SHALL be English adjectives and nouns used to describe physical features (e.g., tall, slim, curly, straight, freckles, muscular, pale, tan, beard, bald, chubby, elegant, wrinkles, dimples, broad).
3. THE vocabulary words SHALL be at the preintermediate level — words a Vietnamese English learner has likely encountered but needs practice producing in speech.
4. THE vocabulary words SHALL be lowercase strings in the `vocabList` field — never objects, numbers, or other types.
5. THE 2 curriculums SHALL NOT share any vocabulary words with each other — each curriculum introduces 15 unique words.

### Requirement 4: Curriculum Topics and Titles

**User Story:** As a content manager, I want clear, minimal Vietnamese titles that communicate the topic without redundancy, so that learners can quickly identify what each curriculum teaches.

#### Acceptance Criteria

1. THE Personality_Curriculum title SHALL be a short Vietnamese title describing the personality/character topic (e.g., "Miêu Tả Tính Cách").
2. THE Appearance_Curriculum title SHALL be a short Vietnamese title describing the appearance topic (e.g., "Miêu Tả Ngoại Hình").
3. THE curriculum titles SHALL NOT include difficulty level descriptors, series name repetition, content type prefixes, skill-focus labels, or audience suffixes.
4. THE curriculum titles SHALL be minimal — if placed in a series, the series title provides context.

### Requirement 5: Content Quality — Persuasive Copy and Tone Variety

**User Story:** As a content manager, I want all learner-facing marketing text to follow the persuasive copy style with varied tones, so that Vietnamese learners feel emotionally engaged and motivated to improve their English speaking skills.

#### Acceptance Criteria

1. IF a series is created, THE series description SHALL be a short persuasive hook of 255 characters or fewer, using one of the 6 tones from the Tone_Palette.
2. THE curriculum description SHALL follow the 5-beat Persuasive_Copy structure: bold headline, concrete examples from daily life describing people, vivid metaphor, promise of transformation, and tie to personal growth.
3. THE 2 curriculum descriptions SHALL use different tones from the Tone_Palette for their ALL-CAPS headline openers.
4. THE curriculum preview (~150 words) SHALL open with a vivid hook about the learner's communication challenge when describing people, name the 15 vocabulary words, and describe the speaking progression across sessions.
5. THE preview text SHALL be written in Vietnamese (as required for preintermediate vi-en curriculums).
6. THE curriculum description SHALL be written in Vietnamese.

### Requirement 6: introAudio Content — Teaching Vocabulary in Context

**User Story:** As a content manager, I want introAudio scripts to teach vocabulary in the context of describing people the learner knows, so that learners understand how each word connects to their daily conversations about friends, family, and colleagues.

#### Acceptance Criteria

1. WHEN an introAudio is created for Sessions 1–3, THE script SHALL teach the 5 vocabulary words for that session with: part of speech, definition in Vietnamese, an example sentence showing the word used to describe a real person (friend, family member, colleague), and pronunciation guidance.
2. WHEN an introAudio is created for Session 4 (review), THE script SHALL recap all 15 vocabulary words, connecting them back to the full topic of describing people.
3. THE introAudio scripts SHALL be written in Vietnamese (the learner's native language) with English vocabulary words and example sentences embedded.
4. WHEN the farewell introAudio is created for Session 4, THE script (400–600 words) SHALL review vocabulary with definitions and fresh example sentences about describing people, summarize the speaking progression, and provide a warm farewell encouraging the learner to use the words in daily conversation.
5. THE 2 curriculums SHALL use different Farewell_Palette registers for their farewell introAudio scripts.
6. THE introAudio scripts SHALL NOT reference nail salons, professional contexts, or customer interactions — all examples SHALL be about describing people in everyday life.

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

1. THE curriculum content JSON SHALL include a `title` field (non-empty string, in Vietnamese).
2. THE curriculum content JSON SHALL include a `description` field (non-empty string, multi-paragraph Persuasive_Copy in Vietnamese).
3. THE curriculum content JSON SHALL include a `preview` object with a `text` field (non-empty string, ~150 words in Vietnamese).
4. THE curriculum content JSON SHALL include a `learningSessions` array with exactly 4 session objects.
5. THE curriculum content JSON SHALL include `"contentTypeTags": []` (empty array).
6. THE curriculum content JSON SHALL include `"lengthTags": ["short"]`.
7. THE curriculum content JSON SHALL include `"skillFocusTags": ["balanced_skills"]`.
8. THE curriculum content JSON SHALL include `"difficultyTags": ["beginner", "vocab_preintermediate", "reading_preintermediate"]`.

### Requirement 9: Strip-Keys Compliance

**User Story:** As a content manager, I want new curriculum content to never include auto-generated platform keys, so that the platform correctly generates fresh metadata after upload.

#### Acceptance Criteria

1. THE curriculum content SHALL NOT include any of the following auto-generated keys: `mp3Url`, `illustrationSet`, `chapterBookmarks`, `segments`, `whiteboardItems`, `userReadingId`, `lessonUniqueId`, `curriculumTags`, `taskId`, `imageId`.

### Requirement 10: Series Creation and Organization

**User Story:** As a content manager, I want the 2 personality/appearance curriculums organized in a series, so that learners can discover and progress through both topics together.

#### Acceptance Criteria

1. WHEN the series is created, THE API SHALL be called via `curriculum-series/create` with a Vietnamese title, a Vietnamese description (under 255 characters using one of the 6 tones), and the series SHALL be kept private until all curriculums are ready.
2. WHEN a curriculum is added to the series via `curriculum-series/addCurriculum`, THE Creation_Script SHALL call `curriculum/setDisplayOrder` to assign a sequential integer display order (Personality = 1, Appearance = 2).
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

1. THE Creation_Script architecture SHALL use one Python script per curriculum (2 scripts total) with all text content hand-written in that script.
2. THE Creation_Script architecture SHALL include one orchestrator script that handles series creation, adding curriculums to the series, and setting display orders.
3. THE Creation_Script SHALL NOT use template functions, string interpolation, or loops to generate learner-facing text content.
4. THE Creation_Script MAY use shared helper functions for activity structure (types, order, data schema) but SHALL hand-write all text content per curriculum.
5. WHEN all curriculums in the series are successfully created, THE workspace SHALL contain a `vi-en-personality-appearance-curriculums/` folder with a README.md documenting: series ID and title, curriculum IDs and titles, display orders, vocabulary lists, tone assignments, how content was created, SQL queries to find the curriculums in the DB, and enough context to recreate if needed.
6. WHEN all curriculums are verified in the database, THE source Python scripts SHALL be deleted from the folder, leaving only the README.

### Requirement 13: No Templated Content

**User Story:** As a content manager, I want every piece of learner-facing text to be individually crafted per curriculum topic, so that each curriculum reads as if written by someone who deeply understands that specific topic.

#### Acceptance Criteria

1. THE Creation_Script SHALL NOT use `f-string` interpolation, template functions, or shared text skeletons to generate introAudio scripts, descriptions, previews, reading passages, or any learner-facing text.
2. EACH curriculum's reading passages SHALL reflect the specific vocabulary and topic of that curriculum — not generic text with words swapped in.
3. THE Personality_Curriculum's introAudio scripts SHALL teach vocabulary with examples of real people's character traits that a Vietnamese learner would recognize from their daily life (describing friends, family, colleagues).
4. THE Appearance_Curriculum's introAudio scripts SHALL teach vocabulary with examples of describing how people look in everyday situations (meeting someone new, describing a friend to someone else, talking about family members).

### Requirement 14: Cross-Curriculum Consistency

**User Story:** As a content manager, I want both curriculums to maintain consistent quality and structure while covering distinct topics, so that the pair feels cohesive and progressively builds the learner's descriptive English.

#### Acceptance Criteria

1. THE series SHALL order curriculums logically: Personality first (display order 1), then Appearance (display order 2) — personality traits are more abstract and conversational, appearance is more concrete and visual.
2. THE 2 curriculums SHALL maintain identical session structure (same activity types and order per the Speaking_Focus_Pattern).
3. THE 2 curriculums SHALL ensure no vocabulary word is repeated between them.
4. THE 2 curriculums SHALL use the same language pair (`language: "en"`, `userLanguage: "vi"`) and difficulty tags (`["beginner", "vocab_preintermediate", "reading_preintermediate"]`).
5. THE 2 curriculums SHALL use different description tones from the Tone_Palette.
6. THE 2 curriculums SHALL use different farewell tones from the Farewell_Palette.

### Requirement 15: Content Corruption Prevention

**User Story:** As a platform developer, I want every curriculum verified against content corruption rules before upload, so that no malformed content enters the database.

#### Acceptance Criteria

1. THE Creation_Script SHALL verify that the curriculum content JSON has non-null, non-empty `title`, `description`, and `preview.text` fields before upload.
2. THE Creation_Script SHALL verify that `learningSessions` is an array of exactly 4 sessions, each with a non-empty `title` and `activities` array.
3. THE Creation_Script SHALL verify that every activity has `activityType` (not `type`), `title`, `description`, and `data` fields.
4. THE Creation_Script SHALL verify that `activityType` values are valid (introAudio, viewFlashcards, reading, speakReading, readAlong).
5. THE Creation_Script SHALL verify that `vocabList` fields contain arrays of lowercase strings using the field name `vocabList` (never `words`).
6. THE Creation_Script SHALL verify that no Strip_Keys appear anywhere in the content JSON.
7. IF any validation check fails, THEN THE Creation_Script SHALL abort the upload and print the specific rule violation.

### Requirement 16: Duplicate Check After Creation

**User Story:** As a platform developer, I want duplicate detection after creation, so that accidental double-runs don't pollute the database.

#### Acceptance Criteria

1. WHEN a curriculum is created, THE Creation_Script SHALL run a duplicate check query for that curriculum title.
2. IF duplicates are found, THEN THE Creation_Script SHALL keep the earliest record and delete extras.
3. THE Creation_Script SHALL remove duplicate series entries before deleting duplicate curriculums.
