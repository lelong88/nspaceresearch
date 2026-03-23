# Requirements Document

## Introduction

Add a new curriculum type `audio_guide` to the language-learning platform. Unlike the existing `balanced_skills` type (which distributes time across reading, listening, speaking, and writing), `audio_guide` makes `introAudio` the centerpiece — delivering content like a podcast or audiobook. Learners absorb language primarily through extended audio lessons, with minimal reading, no writing, and no speaking. The `introAudio` scripts are 2× longer than normal (800-1000 words vs 400-600), and multiple `introAudio` activities appear per session.

The platform already supports `balanced_skills`, `reader`, `vocab_acquisition`, `speaking_focus`, and `writing_focus` curriculum types. This spec adds `audio_guide` as the sixth type, then creates 4 initial curriculums to demonstrate it — uploaded to the platform via standalone Python scripts.

### Two Variants

1. **Single-language (en-en)** — For upper-intermediate to advanced learners. 4 sessions. Each session features 2 `introAudio` activities — the audio IS the lesson, not just the intro. `introAudio` scripts are 800-1000 words each (deep dives into topic, rich vocabulary teaching with etymology, examples, anecdotes). No speaking activities, no writing activities. `vocabLevel2` only in S3 (review session). No `vocabLevel3` anywhere. `readAlong` replaces `reading` + `speakReading` in S1-S2. S4 is the only session with a `reading` activity.

2. **Bilingual (vi-en)** — For beginner to intermediate learners. 4 sessions. Even more audio-heavy: 3 `introAudio` per learning session (S1-S2). The third `introAudio` is a mini-story in target_language using the session's vocabulary — comprehensible input at slow pace. No speaking activities, no writing activities. `vocabLevel2` only in S3. No `vocabLevel3` anywhere.

### Proposed Collection & Series

**Collection:** A new top-level collection for audio-guide curriculums.

**Series:** Two series within the collection (since bilingual and single-language cannot be mixed in the same series):
- Series 1: 2 single-language (en-en) audio_guide curriculums at advanced level
- Series 2: 2 bilingual (vi-en) audio_guide curriculums at intermediate level

### What This Spec Covers

- Definition of the `audio_guide` curriculum type (both single-language and bilingual variants)
- Session structures and activity sequences for both variants
- Creation of 4 initial curriculums (2 en-en advanced, 2 vi-en intermediate)
- Collection and series setup (1 collection, 2 series)
- Post-creation verification and cleanup

### What This Spec Does NOT Cover

- Changes to existing curriculum types
- Client-side UI changes for the new curriculum type

## Glossary

- **Audio_Guide_Curriculum**: A curriculum where `introAudio` is the centerpiece activity. Learners absorb content primarily through extended audio lessons (800-1000 words each). No speaking activities (`speakFlashcards`, `speakReading`, `speak`), no writing activities (`writingSentence`, `writingParagraph`). Multiple `introAudio` per session. The content model is closer to a podcast with flashcard reinforcement.
- **Single_Language_Variant**: The `audio_guide` variant for upper-intermediate to advanced learners (e.g., en-en). 4 sessions, 10 vocab words across S1-S2, 2 `introAudio` per learning session (S1-S2), extended `introAudio` scripts (800-1000 words). No `vocabLevel2` except in S3 review. No `vocabLevel3`.
- **Bilingual_Variant**: The `audio_guide` variant for beginner to intermediate learners (e.g., vi-en). 4 sessions, 10 vocab words across S1-S2, 3 `introAudio` per learning session (S1-S2) — the third being a mini-story in target_language. `vocabLevel2` only in S3. No `vocabLevel3`.
- **Extended_IntroAudio**: An `introAudio` script of 800-1000 words (2× the normal 400-600 words). Used in S1-S2 as the primary teaching vehicle — deep dive into topic, rich vocabulary teaching with etymology, real-world examples, and anecdotes.
- **Supplementary_IntroAudio**: A second `introAudio` in S1-S2 that provides additional context — real-world anecdotes and usage patterns (single-language) or usage tips, common mistakes, and cultural context (bilingual).
- **Mini_Story_IntroAudio**: A third `introAudio` in bilingual S1-S2 that tells a short story in target_language using the session's vocabulary at slow pace — comprehensible input for beginners.
- **Collection**: Top-level organizational shelf in the platform.
- **Series**: A thematic grouping within a collection, containing multiple curriculums.
- **Curriculum**: A single learning unit with vocabulary words, sessions, and activities.
- **Session**: One of 4 ordered segments within an audio_guide curriculum.
- **Activity**: An individual learning exercise within a session.
- **Creation_Script**: A standalone Python script that calls the helloapi REST API to create a curriculum.
- **Strip_Keys**: The set of auto-generated platform keys that must never appear in new content.
- **API**: The helloapi.step.is REST API used for all CRUD operations.
- **Display_Order**: Integer field controlling sort position of curriculums within a series and series within a collection.
- **Persuasive_Copy**: The required emotional sales copy style for all learner-facing text.

## Requirements

### Requirement 1: Single-Language Variant — Session Structure (en-en, Upper-Intermediate → Advanced)

**User Story:** As a content manager, I want the single-language audio_guide variant to have a clear 4-session structure centered on extended audio lessons, so that advanced learners absorb content primarily through listening — like a podcast with flashcard reinforcement.

#### Acceptance Criteria

1. THE Audio_Guide_Curriculum (single-language) SHALL contain exactly 4 sessions.
2. THE Audio_Guide_Curriculum (single-language) SHALL contain exactly 10 vocabulary words divided into 2 groups of 5 (W1 for S1, W2 for S2).
3. WHEN Session 1 is created, THE Session SHALL contain activities in this exact order: `introAudio` (extended: 800-1000 words — deep dive into topic + teach 5 words with rich context, examples, etymology), `introAudio` (supplementary: real-world anecdotes and usage patterns for the 5 words), `viewFlashcards`, `vocabLevel1`, `readAlong` (listen to a short passage that uses the words).
4. WHEN Session 2 is created, THE Session SHALL contain activities in this exact order: `introAudio` (extended: 800-1000 words — second angle on topic + teach 5 more words, recap S1 words), `introAudio` (supplementary: compare/contrast S1 and S2 words, usage nuances), `viewFlashcards`, `vocabLevel1`, `readAlong`.
5. WHEN Session 3 is created, THE Session SHALL contain activities in this exact order: `introAudio` (extended review: walk through all 10 words with fresh examples and deeper analysis), `viewFlashcards` (all 10), `vocabLevel1` (all 10), `vocabLevel2` (all 10).
6. WHEN Session 4 is created, THE Session SHALL contain activities in this exact order: `introAudio` (recap the full learning journey — what was covered, why it matters), `reading` (full article), `readAlong` (listen to full article), `introAudio` (farewell — review each word one final time with a fresh example).

### Requirement 2: Bilingual Variant — Session Structure (vi-en, Beginner → Intermediate)

**User Story:** As a content manager, I want the bilingual audio_guide variant to be even more audio-heavy with 3 introAudio per learning session, so that beginner-to-intermediate learners benefit from repeated listening and comprehensible input in the target language.

#### Acceptance Criteria

1. THE Audio_Guide_Curriculum (bilingual) SHALL contain exactly 4 sessions.
2. THE Audio_Guide_Curriculum (bilingual) SHALL contain exactly 10 vocabulary words divided into 2 groups of 5 (W1 for S1, W2 for S2).
3. WHEN Session 1 is created, THE Session SHALL contain activities in this exact order: `introAudio` (bilingual: explain topic in user_language, teach 5 words with pronunciation, definitions in both languages, 3 example sentences each), `introAudio` (supplementary: usage tips, common mistakes, cultural context — in user_language), `introAudio` (mini-story using all 5 words — in target_language, slow pace), `viewFlashcards`, `vocabLevel1`, `readAlong` (listen to the mini-story again).
4. WHEN Session 2 is created, THE Session SHALL contain activities in this exact order: `introAudio` (teach 5 more words, brief recap of S1), `introAudio` (supplementary), `introAudio` (mini-story with S2 words), `viewFlashcards`, `vocabLevel1`, `readAlong`.
5. WHEN Session 3 is created, THE Session SHALL contain activities in this exact order: `introAudio` (review all 10 words in user_language with fresh examples), `introAudio` (quiz-style: "What word means...?" with pauses for thinking), `viewFlashcards` (all 10), `vocabLevel1`, `vocabLevel2`.
6. WHEN Session 4 is created, THE Session SHALL contain activities in this exact order: `introAudio` (recap journey), `reading` (full text — bilingual), `readAlong` (listen to full text), `introAudio` (farewell — each word reviewed with a fresh sentence).

### Requirement 3: Audio_Guide Type Differentiation from Balanced_Skills

**User Story:** As a content manager, I want the audio_guide type to be clearly differentiated from balanced_skills, so that the curriculum structure enforces the listening-centric, receptive-only pedagogy.

#### Acceptance Criteria

1. THE Audio_Guide_Curriculum SHALL NOT include `speakFlashcards` activities in any session.
2. THE Audio_Guide_Curriculum SHALL NOT include `speakReading` activities in any session.
3. THE Audio_Guide_Curriculum SHALL NOT include `speak` activities in any session.
4. THE Audio_Guide_Curriculum SHALL NOT include `writingSentence` activities in any session.
5. THE Audio_Guide_Curriculum SHALL NOT include `writingParagraph` activities in any session.
6. THE Audio_Guide_Curriculum SHALL NOT include `vocabLevel3` activities in any session.
7. THE Audio_Guide_Curriculum SHALL include `vocabLevel2` only in Session 3 (review session) — not in S1, S2, or S4.
8. THE Audio_Guide_Curriculum SHALL include multiple `introAudio` activities per session — 2 per session for single-language S1-S2, 3 per session for bilingual S1-S2.
9. THE Audio_Guide_Curriculum SHALL use `readAlong` instead of `reading` + `speakReading` in S1-S2 — learners listen, not read-then-speak.
10. THE Audio_Guide_Curriculum SHALL include a `reading` activity only in S4 (the only session with a reading activity in both variants).
11. THE Audio_Guide_Curriculum SHALL use vocabulary as scaffolding for listening comprehension (10 words across 2 sessions) rather than as the primary learning goal.

### Requirement 4: Extended IntroAudio Scripts

**User Story:** As a content manager, I want introAudio scripts in audio_guide curriculums to be 2× longer than normal, so that the audio IS the lesson — delivering rich, podcast-quality content that teaches vocabulary through deep context, etymology, and real-world examples.

#### Acceptance Criteria

1. WHEN an Extended_IntroAudio is created for S1 or S2 (single-language), THE script SHALL be 800-1000 words — a deep dive into the topic that teaches 5 vocabulary words with rich context, multiple examples, etymology where relevant, and real-world usage patterns.
2. WHEN an Extended_IntroAudio is created for S1 or S2 (bilingual), THE script SHALL be 800-1000 words — teaching in user_language with pronunciation guidance, definitions in both languages, and 3 example sentences per word.
3. WHEN a Supplementary_IntroAudio is created for S1 or S2 (single-language), THE script SHALL provide real-world anecdotes and usage patterns for the session's vocabulary words — extending the teaching beyond definitions into lived usage.
4. WHEN a Supplementary_IntroAudio is created for S1 or S2 (bilingual), THE script SHALL provide usage tips, common mistakes, and cultural context for the session's vocabulary — delivered in user_language.
5. WHEN a Mini_Story_IntroAudio is created for bilingual S1 or S2, THE script SHALL tell a short story in target_language using all 5 of the session's vocabulary words at slow pace — providing comprehensible input.
6. WHEN the S3 review introAudio is created, THE script SHALL walk through all 10 vocabulary words with fresh examples and deeper analysis (single-language) or review all 10 words in user_language with fresh examples (bilingual).
7. WHEN the S3 second introAudio is created (bilingual), THE script SHALL use a quiz-style format ("What word means...?") with pauses for thinking.
8. WHEN the S4 recap introAudio is created, THE script SHALL recap the full learning journey — what was covered and why it matters.
9. WHEN the S4 farewell introAudio is created, THE script (400-600 words) SHALL review each vocabulary word one final time with a fresh example sentence and provide a warm farewell.

### Requirement 5: ReadAlong as Primary Listening Activity

**User Story:** As a content manager, I want readAlong to replace reading + speakReading in S1-S2, so that learners listen to passages rather than reading and speaking them — maintaining the audio-first experience.

#### Acceptance Criteria

1. THE Audio_Guide_Curriculum (single-language) SHALL include `readAlong` in S1 and S2 as the only text-based activity — learners listen to a short passage that uses the session's vocabulary words.
2. THE Audio_Guide_Curriculum (bilingual) SHALL include `readAlong` in S1 and S2 — learners listen to the mini-story again (the same content as the Mini_Story_IntroAudio).
3. THE Audio_Guide_Curriculum SHALL include both `reading` and `readAlong` in S4 — the only session where learners both read and listen to the full article.
4. THE Audio_Guide_Curriculum SHALL NOT include `reading` in S1, S2, or S3.

### Requirement 6: Vocabulary Selection and Usage

**User Story:** As a content manager, I want vocabulary to be selected as tools for listening comprehension rather than as standalone learning targets, so that the audio_guide curriculum maintains its listening-centric identity.

#### Acceptance Criteria

1. THE Audio_Guide_Curriculum SHALL select 10 vocabulary words that are useful for understanding the audio lessons — words that appear naturally in the topic and enable the learner to follow the extended introAudio content.
2. THE Audio_Guide_Curriculum SHALL divide vocabulary into 2 groups of 5 words: W1 (taught in S1) and W2 (taught in S2).
3. WHEN Session 3 reviews vocabulary, THE Session SHALL review all 10 words from both S1 and S2 in the `viewFlashcards` activity.
4. THE Audio_Guide_Curriculum SHALL NOT include `vocabLevel3` in any session — vocabulary depth is achieved through repeated audio exposure, not through additional drill levels.
5. THE Audio_Guide_Curriculum SHALL include `vocabLevel2` only in S3 (review session) — S1 and S2 use only `vocabLevel1` for light-touch reinforcement.
6. THE Audio_Guide_Curriculum vocabulary words SHALL appear in the readAlong passages and the S4 reading passage so that learners encounter the words in written context after hearing them in audio.

### Requirement 7: Content Quality — Persuasive Copy

**User Story:** As a content manager, I want all learner-facing text to follow the persuasive copy style, so that learners feel emotionally engaged and motivated to learn through listening.

#### Acceptance Criteria

1. THE Curriculum description SHALL follow the 5-beat persuasive copy structure, adapted to emphasize the audio learning journey — from podcast-style lessons to deep vocabulary mastery through listening.
2. THE Curriculum preview (~150 words) SHALL open with a vivid hook about the power of learning through listening, name the vocabulary words, and describe the audio progression across sessions.
3. WHEN an introAudio activity is created, THE introAudio script SHALL deliver rich, engaging content that feels like a podcast episode — not a dry vocabulary list.
4. THE Curriculum SHALL use English for all user-facing text in single-language curriculums and Vietnamese for bilingual curriculums, consistent with the language policy.

### Requirement 8: Activity Metadata

**User Story:** As a content manager, I want every activity to have proper title and description fields, so that server-side logging and client display work correctly.

#### Acceptance Criteria

1. THE Activity SHALL include both a `title` and `description` field for every activity in every session.
2. WHEN a `viewFlashcards` or `vocabLevel1` activity is created, THE Activity title SHALL follow the format "Flashcards: <topic>" and the description SHALL list the words being learned.
3. WHEN a `vocabLevel2` activity is created (S3 only), THE Activity title SHALL follow the format "Flashcards: <topic>" and the description SHALL list the words being reviewed.
4. WHEN a `reading` activity is created (S4 only), THE Activity title SHALL follow the format "Đọc: <topic>" (bilingual) or "Read: <topic>" (single-language) and the description SHALL contain the first ~80 characters of the reading text.
5. WHEN a `readAlong` activity is created, THE Activity title SHALL follow the format "Nghe: <topic>" (bilingual) or "Listen: <topic>" (single-language) and the description SHALL be "Nghe bài nghe và theo dõi." (bilingual) or "Listen and follow along." (single-language).
6. WHEN an `introAudio` activity is created, THE Activity title SHALL be a descriptive label and the description SHALL be a brief summary.
7. THE Session object SHALL include a `title` field (e.g., "Session 1: Audio Lesson + Light Vocab", "Buổi 1: Bài nghe + Từ vựng").

### Requirement 9: Strip-Keys Compliance

**User Story:** As a content manager, I want new curriculum content to never include auto-generated platform keys, so that the platform correctly generates fresh metadata after upload.

#### Acceptance Criteria

1. THE Curriculum content SHALL NOT include any of the following auto-generated keys: `mp3Url`, `illustrationSet`, `chapterBookmarks`, `segments`, `whiteboardItems`, `userReadingId`, `lessonUniqueId`, `curriculumTags`, `taskId`, `imageId`.

### Requirement 10: Collection and Series Creation

**User Story:** As a content manager, I want to create a collection and two series for audio-guide curriculums, so that learners can discover and access audio-focused learning as a distinct content category.

#### Acceptance Criteria

1. WHEN the collection is created, THE API SHALL be called via `curriculum-collection/create` with a descriptive title, a persuasive description, and `isPublic: true`.
2. WHEN Series 1 (en-en) is created, THE API SHALL be called via `curriculum-series/create` with an English title, an English description (under 255 characters), and `isPublic: true`.
3. WHEN Series 2 (vi-en) is created, THE API SHALL be called via `curriculum-series/create` with a Vietnamese title, a Vietnamese description (under 255 characters), and `isPublic: true`.
4. WHEN each series is created, THE Creation_Script SHALL call `curriculum-collection/addSeriesToCollection` to wire the series into the collection.
5. THE Creation_Script SHALL assign display_order 100 to Series 1 and display_order 200 to Series 2 via `curriculum-series/setDisplayOrder`.
6. WHEN both series are fully populated, THE Series 1 SHALL contain exactly 2 en-en curriculums and THE Series 2 SHALL contain exactly 2 vi-en curriculums.

### Requirement 11: Display Order and Organization

**User Story:** As a content manager, I want curriculums and the series to have explicit display orders, so that they appear in the intended sequence in the client app.

#### Acceptance Criteria

1. WHEN a curriculum is added to a series via `curriculum-series/addCurriculum`, THE Creation_Script SHALL call `curriculum/setDisplayOrder` to assign a sequential integer display order (0, 1) for the 2 curriculums within each series.
2. WHEN all curriculums are created and ordered, THE Series 1 SHALL contain exactly 2 curriculums sorted by display_order, and THE Series 2 SHALL contain exactly 2 curriculums sorted by display_order.

### Requirement 12: Script Organization

**User Story:** As a content manager, I want one Python script per curriculum plus an orchestrator script for series-level setup, so that each curriculum's content is self-contained and files remain manageable.

#### Acceptance Criteria

1. THE Creation_Script architecture SHALL use one Python script per curriculum with all text content hand-written in that script.
2. THE Creation_Script architecture SHALL include one orchestrator script that handles collection creation, both series creation, adding curriculums to the series, adding the series to the collection, and setting display orders.
3. THE Creation_Script SHALL NOT use template functions, string interpolation, or loops to generate learner-facing text content.
4. WHEN a curriculum is successfully created and verified in the database, THE source script SHALL be deleted, leaving only a README with creation method, SQL queries, and recreation context.

### Requirement 13: No Templated Content

**User Story:** As a content manager, I want every piece of learner-facing text to be individually crafted per curriculum topic, so that each curriculum reads as if written by someone who deeply understands that specific topic.

#### Acceptance Criteria

1. THE Creation_Script SHALL NOT use `f-string` interpolation, template functions, or shared text skeletons to generate introAudio scripts, descriptions, previews, or any learner-facing text.
2. THE Creation_Script MAY use shared helper functions for activity structure (types, order, data schema) but SHALL hand-write all text content per curriculum.

### Requirement 14: Language and Level Compliance

**User Story:** As a content manager, I want all curriculums to comply with the platform's language policy and level consistency rules, so that the series is internally consistent.

#### Acceptance Criteria

1. THE Curriculum SHALL set `language` and `userLanguage` as top-level body parameters in the `curriculum/create` API call (not only inside the content JSON).
2. WHEN a single-language curriculum is created, THE Curriculum SHALL set `language: "en"` and `userLanguage: "en"`.
3. WHEN a bilingual vi-en curriculum is created, THE Curriculum SHALL set `language: "en"` and `userLanguage: "vi"`.
4. THE Series SHALL contain curriculums within a maximum 1-level gap from the highest-level curriculum in the series.
5. THE Curriculum title SHALL NOT include difficulty level descriptors (e.g., "Upper-Intermediate", "Advanced", "Beginner").

### Requirement 15: Newly Created Curriculums Must Be Private

**User Story:** As a content manager, I want all newly created curriculums to be private by default, so that they go through content generation (audio, illustrations) before being exposed to learners.

#### Acceptance Criteria

1. WHEN a curriculum is created via `curriculum/create`, THE Curriculum SHALL have `is_public: false` (the platform default).
2. THE Creation_Script SHALL NOT call `curriculum/setPublic` with `isPublic: true` on any newly created curriculum.

### Requirement 16: introAudio Content for Audio_Guide

**User Story:** As a content manager, I want introAudio scripts to be the primary teaching vehicle in audio_guide curriculums, so that learners receive rich, podcast-quality content that makes listening the core learning experience.

#### Acceptance Criteria

1. WHEN an Extended_IntroAudio is created for S1 (single-language), THE script SHALL teach the 5 vocabulary words with rich context, examples, etymology, and real-world usage patterns — delivering a 10-15 minute audio lesson experience.
2. WHEN an Extended_IntroAudio is created for S2 (single-language), THE script SHALL teach the 5 new vocabulary words, recap S1 words, and present a second angle on the topic.
3. WHEN a Supplementary_IntroAudio is created for S1 (single-language), THE script SHALL provide real-world anecdotes and usage patterns for the 5 words taught in the Extended_IntroAudio.
4. WHEN a Supplementary_IntroAudio is created for S2 (single-language), THE script SHALL compare and contrast S1 and S2 words, exploring usage nuances.
5. WHEN introAudio activities are created for bilingual sessions, THE scripts SHALL use bilingual delivery (teaching in user_language, examples in target_language, pronunciation guidance in user_language).
6. WHEN a Mini_Story_IntroAudio is created for bilingual S1 or S2, THE script SHALL be a short story in target_language at slow pace, using all 5 of the session's vocabulary words as comprehensible input.
7. WHEN the farewell introAudio is created for S4, THE script (400-600 words) SHALL review each vocabulary word one final time with a fresh example sentence and provide a warm farewell.

### Requirement 17: Folder and README Structure

**User Story:** As a content manager, I want the audio-guide series to have its own folder with a README tracking creation details, so that content is recoverable and auditable.

#### Acceptance Criteria

1. THE workspace SHALL contain a dedicated folder `audio-guide-curriculum/` for the series.
2. WHEN all curriculums in the series are successfully created, THE folder SHALL contain a README.md documenting: collection ID and title, Series 1 ID and title, Series 2 ID and title, curriculum IDs and titles, how content was created, SQL queries to find the curriculums in the DB, and enough context to recreate if needed.
3. WHEN all curriculums are verified in the database, THE source Python scripts SHALL be deleted from the folder, leaving only the README.
