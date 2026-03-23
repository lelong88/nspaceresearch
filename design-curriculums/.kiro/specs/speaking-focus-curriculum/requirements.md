# Requirements Document

## Introduction

Formalize the `speaking_focus` curriculum type for the language-learning platform. Unlike the existing `balanced_skills` type (which distributes time across reading, listening, speaking, and writing), `speaking_focus` maximizes time spent producing speech — trading writing activities (`writingSentence`, `writingParagraph`) and deep vocab drill (`vocabLevel2`, `vocabLevel3`) for open-ended `speak` activities with escalating prompts and conversational scenarios.

The platform already supports `balanced_skills`, `reader`, `vocab_acquisition`, and one experimental `speaking_focus` curriculum. This spec formalizes the type definition, then creates 4 initial curriculums to demonstrate it — uploaded to the platform via standalone Python scripts.

### Two Variants

1. **Single-language (en-en)** — For upper-intermediate to advanced learners. 4 sessions. `speak` activities (open-ended speech production) appear in every session — 2 per session. `speakFlashcards` and `speakReading` are kept as pronunciation scaffolding. No `writingSentence` or `writingParagraph`. `vocabLevel2`/`vocabLevel3` dropped — recognition is enough, production happens through speech. `speak` prompts escalate: explain → role-play → monologue → debate → presentation.

2. **Bilingual (vi-en / vi-zh)** — For beginner to intermediate learners. 4 sessions. Speaking is more scaffolded — `speakFlashcards` and `speakReading` do more heavy lifting. `speak` appears once per session in S1/S2 (not twice). `vocabLevel2` is kept for bilingual (unlike single-language which drops it). `speak` prompts are simpler: sentence-level, with examples provided in the prompt. Bilingual `introAudio` gives pronunciation guidance in `user_language`.

### Proposed Collection & Series

**Collection:** A new top-level collection for speaking-focus curriculums.

**Series:** Two series within the collection (since bilingual and single-language cannot be mixed in the same series):
- Series 1: 2 single-language (en-en) speaking_focus curriculums at advanced level
- Series 2: 2 bilingual (vi-en) speaking_focus curriculums at intermediate level

### What This Spec Covers

- Definition of the `speaking_focus` curriculum type (both single-language and bilingual variants)
- Session structures and activity sequences for both variants
- Creation of 4 initial curriculums (2 en-en advanced, 2 vi-en intermediate)
- Collection and series setup (1 collection, 2 series)
- Post-creation verification and cleanup

### What This Spec Does NOT Cover

- `writing_focus` and `audio_guide` curriculum types (separate specs)
- Changes to existing `balanced_skills` curriculums
- Client-side UI changes for the new curriculum type

## Glossary

- **Speaking_Focus_Curriculum**: A curriculum where speech production is the centerpiece activity. Writing activities (`writingSentence`, `writingParagraph`) are dropped entirely. `speak` activities with open-ended prompts appear in every session. `speakFlashcards` and `speakReading` are kept as pronunciation scaffolding.
- **Single_Language_Variant**: The `speaking_focus` variant for upper-intermediate to advanced learners (e.g., en-en). 4 sessions, 10 vocab words across S1-S2, 2 `speak` activities per session, prompts escalate in complexity. No `vocabLevel2`/`vocabLevel3`.
- **Bilingual_Variant**: The `speaking_focus` variant for beginner to intermediate learners (e.g., vi-en). 4 sessions, 10 vocab words across S1-S2, 1 `speak` activity per session in S1-S2 (2 in S3-S4). `vocabLevel2` is kept. `speak` prompts are simpler with examples.
- **Speak_Activity**: An open-ended speech production activity where the learner responds to a prompt by speaking. Data shape: `{ text: string, audioSpeed: -0.3 }` where `text` is the speaking prompt. Distinct from `speakFlashcards` (repeat after model) and `speakReading` (read aloud).
- **Prompt_Escalation**: The progressive increase in speaking complexity across sessions. Single-language: explain → role-play → summarize → debate → monologue → counter-argument → present → impromptu response. Bilingual: guided sentence → describe with words → describe scenario → answer question → summarize.
- **Collection**: Top-level organizational shelf in the platform.
- **Series**: A thematic grouping within a collection, containing multiple curriculums.
- **Curriculum**: A single learning unit with vocabulary words, sessions, and activities.
- **Session**: One of 4 ordered segments within a speaking_focus curriculum.
- **Activity**: An individual learning exercise within a session.
- **Creation_Script**: A standalone Python script that calls the helloapi REST API to create a curriculum.
- **Strip_Keys**: The set of auto-generated platform keys that must never appear in new content.
- **API**: The helloapi.step.is REST API used for all CRUD operations.
- **Display_Order**: Integer field controlling sort position of curriculums within a series and series within a collection.
- **Persuasive_Copy**: The required emotional sales copy style for all learner-facing text.

## Requirements

### Requirement 1: Single-Language Variant — Session Structure (en-en, Upper-Intermediate → Advanced)

**User Story:** As a content manager, I want the single-language speaking_focus variant to have a clear 4-session structure with escalating speaking demands, so that advanced learners progressively build real-time productive speaking skills.

#### Acceptance Criteria

1. THE Speaking_Focus_Curriculum (single-language) SHALL contain exactly 4 sessions.
2. THE Speaking_Focus_Curriculum (single-language) SHALL contain exactly 10 vocabulary words divided into 2 groups of 5 (W1 for S1, W2 for S2).
3. WHEN Session 1 is created, THE Session SHALL contain activities in this exact order: `introAudio` (teach 5 words with pronunciation emphasis), `viewFlashcards`, `speakFlashcards`, `vocabLevel1`, `reading` (short passage — context for speaking), `speakReading`, `speak` (open-ended: explain a concept using new words), `speak` (role-play: conversational scenario).
4. WHEN Session 2 is created, THE Session SHALL contain activities in this exact order: `introAudio` (teach 5 more words, recap S1), `viewFlashcards`, `speakFlashcards`, `vocabLevel1`, `reading`, `speakReading`, `speak` (summarize both passages orally), `speak` (debate prompt: argue for/against a position from the text).
5. WHEN Session 3 is created, THE Session SHALL contain activities in this exact order: `introAudio` (review all 10 words), `viewFlashcards` (all 10), `speakFlashcards` (all 10), `vocabLevel1`, `speak` (2-minute monologue on the topic), `speak` (respond to a counter-argument).
6. WHEN Session 4 is created, THE Session SHALL contain activities in this exact order: `introAudio` (recap), `reading` (full article), `speakReading`, `readAlong`, `speak` (present a 2-minute summary of the article), `speak` (impromptu response to a follow-up question), `introAudio` (farewell).

### Requirement 2: Bilingual Variant — Session Structure (vi-en, Beginner → Intermediate)

**User Story:** As a content manager, I want the bilingual speaking_focus variant to scaffold speaking more heavily with pronunciation practice before introducing open-ended prompts, so that beginner-to-intermediate learners build speaking confidence gradually.

#### Acceptance Criteria

1. THE Speaking_Focus_Curriculum (bilingual) SHALL contain exactly 4 sessions.
2. THE Speaking_Focus_Curriculum (bilingual) SHALL contain exactly 10 vocabulary words divided into 2 groups of 5 (W1 for S1, W2 for S2).
3. WHEN Session 1 is created, THE Session SHALL contain activities in this exact order: `introAudio`, `introAudio` (bilingual vocab teaching with pronunciation), `viewFlashcards`, `speakFlashcards`, `vocabLevel1`, `vocabLevel2`, `introAudio` (reading intro), `reading`, `speakReading`, `readAlong`, `speak` (guided: say a sentence using a word, with example provided).
4. WHEN Session 2 is created, THE Session SHALL contain activities in this exact order: `introAudio`, `introAudio` (bilingual vocab teaching), `viewFlashcards`, `speakFlashcards`, `vocabLevel1`, `vocabLevel2`, `introAudio` (reading intro), `reading`, `speakReading`, `readAlong`, `speak` (slightly less scaffolded: describe a topic using 2-3 new words).
5. WHEN Session 3 is created, THE Session SHALL contain activities in this exact order: `introAudio`, `introAudio` (review all vocab), `viewFlashcards` (all 10), `speakFlashcards` (all 10), `vocabLevel1`, `vocabLevel2`, `speak` (describe a picture/scenario using vocab), `speak` (answer a question about the topic).
6. WHEN Session 4 is created, THE Session SHALL contain activities in this exact order: `introAudio`, `reading` (full text), `speakReading`, `readAlong`, `speak` (summarize what you read in 3-4 sentences), `introAudio` (farewell).

### Requirement 3: Speaking_Focus Type Differentiation from Balanced_Skills

**User Story:** As a content manager, I want the speaking_focus type to be clearly differentiated from balanced_skills, so that the curriculum structure enforces the speaking-centric pedagogy.

#### Acceptance Criteria

1. THE Speaking_Focus_Curriculum SHALL NOT include `writingSentence` activities in any session.
2. THE Speaking_Focus_Curriculum SHALL NOT include `writingParagraph` activities in any session.
3. THE Speaking_Focus_Curriculum (single-language) SHALL NOT include `vocabLevel2` or `vocabLevel3` activities in any session.
4. THE Speaking_Focus_Curriculum (bilingual) SHALL NOT include `vocabLevel3` activities in any session.
5. THE Speaking_Focus_Curriculum SHALL include `speak` activities in every session — 2 per session for single-language, 1 per session in S1-S2 and 2 per session in S3-S4 for bilingual.
6. THE Speaking_Focus_Curriculum SHALL retain `speakFlashcards` and `speakReading` as pronunciation scaffolding activities (distinct from the open-ended `speak` activity).
7. THE Speaking_Focus_Curriculum SHALL use vocabulary as a tool for speaking (10 words across 2 sessions) rather than as the primary learning goal.

### Requirement 4: Speak Activity Prompts — Single-Language Escalation

**User Story:** As a content manager, I want speak prompts to escalate in complexity across sessions, so that learners progress from guided explanations to impromptu responses.

#### Acceptance Criteria

1. WHEN Session 1 `speak` activities are created (single-language), THE first Speak_Activity SHALL prompt the learner to explain a concept using at least 3 new vocabulary words, and THE second Speak_Activity SHALL prompt a role-play scenario (e.g., explaining to a colleague who disagrees).
2. WHEN Session 2 `speak` activities are created (single-language), THE first Speak_Activity SHALL prompt the learner to summarize both passages orally, and THE second Speak_Activity SHALL prompt a debate (argue for/against a position from the text).
3. WHEN Session 3 `speak` activities are created (single-language), THE first Speak_Activity SHALL prompt a 2-minute monologue on the topic, and THE second Speak_Activity SHALL prompt a response to a counter-argument.
4. WHEN Session 4 `speak` activities are created (single-language), THE first Speak_Activity SHALL prompt a 2-minute summary presentation of the full article, and THE second Speak_Activity SHALL prompt an impromptu response to a follow-up question.

### Requirement 5: Speak Activity Prompts — Bilingual Scaffolding

**User Story:** As a content manager, I want bilingual speak prompts to provide scaffolding in the learner's native language, so that beginner-to-intermediate learners can focus on producing target-language speech without struggling to understand the prompt itself.

#### Acceptance Criteria

1. WHEN a bilingual `speak` activity is created, THE Speak_Activity prompt text SHALL be written in `user_language` (e.g., Vietnamese) and require the spoken response in `target_language` (e.g., English).
2. WHEN Session 1 `speak` is created (bilingual), THE Speak_Activity SHALL provide a guided prompt with an example sentence (e.g., "Say a sentence using [word]. Example: ...").
3. WHEN Session 2 `speak` is created (bilingual), THE Speak_Activity SHALL provide a slightly less scaffolded prompt (e.g., "Describe [topic] using 2-3 of your new words").
4. WHEN Session 3 `speak` activities are created (bilingual), THE first Speak_Activity SHALL prompt describing a picture or scenario using vocab, and THE second Speak_Activity SHALL prompt answering a question about the topic.
5. WHEN Session 4 `speak` is created (bilingual), THE Speak_Activity SHALL prompt summarizing the reading in 3-4 sentences.

### Requirement 6: Speak Activity Data Shape

**User Story:** As a content manager, I want the speak activity to have a well-defined data shape, so that the client can render the speaking interface correctly.

#### Acceptance Criteria

1. THE Speak_Activity SHALL include a `text` field containing the speaking prompt.
2. THE Speak_Activity SHALL include an `audioSpeed` field with value `-0.3`.
3. THE Speak_Activity SHALL NOT include a `lessonUniqueId` field (it is auto-generated by the platform).

### Requirement 7: Reading Passages as Speaking Context

**User Story:** As a content manager, I want reading passages to serve as context for speaking activities, so that learners have substantive content to discuss and respond to in their speech.

#### Acceptance Criteria

1. THE Speaking_Focus_Curriculum (single-language) SHALL include a reading passage in S1 that introduces the topic and contains the session's vocabulary in context.
2. THE Speaking_Focus_Curriculum (single-language) SHALL include a second reading passage in S2 that presents a different angle on the same topic as S1.
3. THE Speaking_Focus_Curriculum (single-language) SHALL NOT include a new reading passage in S3 (S3 is a pure speaking session — review + extended speaking only).
4. THE Speaking_Focus_Curriculum (single-language) SHALL include a full article reading in S4 that combines and extends the S1-S2 passages, serving as the basis for the capstone speaking activities.
5. THE Speaking_Focus_Curriculum (bilingual) SHALL include reading passages in S1, S2, and S4 that serve as comprehensible input and context for speaking responses.
6. THE Speaking_Focus_Curriculum (bilingual) SHALL NOT include a new reading passage in S3 (S3 focuses on review + speaking practice).

### Requirement 8: Vocabulary Selection and Usage

**User Story:** As a content manager, I want vocabulary to be selected as tools for speaking rather than as standalone learning targets, so that the speaking_focus curriculum maintains its speaking-centric identity.

#### Acceptance Criteria

1. THE Speaking_Focus_Curriculum SHALL select 10 vocabulary words that are useful for the speaking tasks in the curriculum — words that enable the learner to express ideas about the topic in their speech.
2. THE Speaking_Focus_Curriculum SHALL divide vocabulary into 2 groups of 5 words: W1 (taught in S1) and W2 (taught in S2).
3. WHEN Session 3 reviews vocabulary, THE Session SHALL review all 10 words from both S1 and S2 in the `viewFlashcards` and `speakFlashcards` activities.
4. THE Speaking_Focus_Curriculum (single-language) SHALL NOT include `vocabLevel2` or `vocabLevel3` in any session — vocabulary depth is achieved through speaking practice, not through additional drill levels.
5. THE Speaking_Focus_Curriculum (bilingual) SHALL include `vocabLevel2` but NOT `vocabLevel3` — bilingual learners need more recognition scaffolding before speaking.
6. THE Speaking_Focus_Curriculum vocabulary words SHALL appear in the reading passages so that learners encounter the words in context before using them in speech.

### Requirement 9: Content Quality — Persuasive Copy

**User Story:** As a content manager, I want all learner-facing text to follow the persuasive copy style, so that learners feel emotionally engaged and motivated to develop their speaking skills.

#### Acceptance Criteria

1. THE Curriculum description SHALL follow the 5-beat persuasive copy structure, adapted to emphasize the speaking journey — from guided pronunciation to impromptu responses.
2. THE Curriculum preview (~150 words) SHALL open with a vivid hook about the power of speaking, name the vocabulary words, and describe the speaking progression across sessions.
3. WHEN an introAudio activity is created, THE introAudio script SHALL reference the topic, explain how vocabulary connects to the speaking tasks, and motivate the learner for the upcoming speaking challenge.
4. THE Curriculum SHALL use English for all user-facing text in single-language curriculums and Vietnamese for bilingual curriculums, consistent with the language policy.

### Requirement 10: Activity Metadata

**User Story:** As a content manager, I want every activity to have proper title and description fields, so that server-side logging and client display work correctly.

#### Acceptance Criteria

1. THE Activity SHALL include both a `title` and `description` field for every activity in every session.
2. WHEN a `viewFlashcards`, `speakFlashcards`, or `vocabLevel1` activity is created, THE Activity title SHALL follow the format "Flashcards: <topic>" and the description SHALL list the words being learned.
3. WHEN a `vocabLevel2` activity is created (bilingual only), THE Activity title SHALL follow the format "Flashcards: <topic>" and the description SHALL list the words being learned.
4. WHEN a `reading` or `speakReading` activity is created, THE Activity title SHALL follow the format "Đọc: <topic>" (bilingual) or "Read: <topic>" (single-language) and the description SHALL contain the first ~80 characters of the reading text.
5. WHEN a `readAlong` activity is created, THE Activity title SHALL follow the format "Nghe: <topic>" (bilingual) or "Listen: <topic>" (single-language) and the description SHALL be "Nghe bài đọc và theo dõi." (bilingual) or "Listen and follow along." (single-language).
6. WHEN an `introAudio` activity is created, THE Activity title SHALL be a descriptive label and the description SHALL be a brief summary.
7. WHEN a `speak` activity is created, THE Activity title SHALL follow the format "Nói: <topic>" (bilingual) or "Speak: <topic>" (single-language) and the description SHALL briefly summarize the speaking task.
8. THE Session object SHALL include a `title` field (e.g., "Session 1: Vocab + Speak", "Buổi 1: Từ vựng + Nói").

### Requirement 11: Strip-Keys Compliance

**User Story:** As a content manager, I want new curriculum content to never include auto-generated platform keys, so that the platform correctly generates fresh metadata after upload.

#### Acceptance Criteria

1. THE Curriculum content SHALL NOT include any of the following auto-generated keys: `mp3Url`, `illustrationSet`, `chapterBookmarks`, `segments`, `whiteboardItems`, `userReadingId`, `lessonUniqueId`, `curriculumTags`, `taskId`, `imageId`.

### Requirement 12: Collection and Series Creation

**User Story:** As a content manager, I want to create a collection and two series for speaking-focus curriculums, so that learners can discover and access speaking-focused learning as a distinct content category.

#### Acceptance Criteria

1. WHEN the collection is created, THE API SHALL be called via `curriculum-collection/create` with a descriptive title, a persuasive description, and `isPublic: true`.
2. WHEN Series 1 (en-en) is created, THE API SHALL be called via `curriculum-series/create` with an English title, an English description (under 255 characters), and `isPublic: true`.
3. WHEN Series 2 (vi-en) is created, THE API SHALL be called via `curriculum-series/create` with a Vietnamese title, a Vietnamese description (under 255 characters), and `isPublic: true`.
4. WHEN each series is created, THE Creation_Script SHALL call `curriculum-collection/addSeriesToCollection` to wire the series into the collection.
5. THE Creation_Script SHALL assign display_order 100 to Series 1 and display_order 200 to Series 2 via `curriculum-series/setDisplayOrder`.
6. WHEN both series are fully populated, THE Series 1 SHALL contain exactly 2 en-en curriculums and THE Series 2 SHALL contain exactly 2 vi-en curriculums.

### Requirement 13: Display Order and Organization

**User Story:** As a content manager, I want curriculums and the series to have explicit display orders, so that they appear in the intended sequence in the client app.

#### Acceptance Criteria

1. WHEN a curriculum is added to a series via `curriculum-series/addCurriculum`, THE Creation_Script SHALL call `curriculum/setDisplayOrder` to assign a sequential integer display order (0, 1) for the 2 curriculums within each series.
2. WHEN all curriculums are created and ordered, THE Series 1 SHALL contain exactly 2 curriculums sorted by display_order, and THE Series 2 SHALL contain exactly 2 curriculums sorted by display_order.

### Requirement 14: Script Organization

**User Story:** As a content manager, I want one Python script per curriculum plus an orchestrator script for series-level setup, so that each curriculum's content is self-contained and files remain manageable.

#### Acceptance Criteria

1. THE Creation_Script architecture SHALL use one Python script per curriculum with all text content hand-written in that script.
2. THE Creation_Script architecture SHALL include one orchestrator script that handles collection creation, both series creation, adding curriculums to the series, adding the series to the collection, and setting display orders.
3. THE Creation_Script SHALL NOT use template functions, string interpolation, or loops to generate learner-facing text content.
4. WHEN a curriculum is successfully created and verified in the database, THE source script SHALL be deleted, leaving only a README with creation method, SQL queries, and recreation context.

### Requirement 15: No Templated Content

**User Story:** As a content manager, I want every piece of learner-facing text to be individually crafted per curriculum topic, so that each curriculum reads as if written by someone who deeply understands that specific topic.

#### Acceptance Criteria

1. THE Creation_Script SHALL NOT use `f-string` interpolation, template functions, or shared text skeletons to generate introAudio scripts, descriptions, previews, or speak prompts.
2. THE Creation_Script MAY use shared helper functions for activity structure (types, order, data schema) but SHALL hand-write all text content per curriculum.

### Requirement 16: Language and Level Compliance

**User Story:** As a content manager, I want all curriculums to comply with the platform's language policy and level consistency rules, so that the series is internally consistent.

#### Acceptance Criteria

1. THE Curriculum SHALL set `language` and `userLanguage` as top-level body parameters in the `curriculum/create` API call (not only inside the content JSON).
2. WHEN a single-language curriculum is created, THE Curriculum SHALL set `language: "en"` and `userLanguage: "en"`.
3. WHEN a bilingual vi-en curriculum is created, THE Curriculum SHALL set `language: "en"` and `userLanguage: "vi"`.
4. THE Series SHALL contain curriculums within a maximum 1-level gap from the highest-level curriculum in the series.
5. THE Curriculum title SHALL NOT include difficulty level descriptors (e.g., "Upper-Intermediate", "Advanced", "Beginner").

### Requirement 17: Newly Created Curriculums Must Be Private

**User Story:** As a content manager, I want all newly created curriculums to be private by default, so that they go through content generation (audio, illustrations) before being exposed to learners.

#### Acceptance Criteria

1. WHEN a curriculum is created via `curriculum/create`, THE Curriculum SHALL have `is_public: false` (the platform default).
2. THE Creation_Script SHALL NOT call `curriculum/setPublic` with `isPublic: true` on any newly created curriculum.

### Requirement 18: introAudio Content for Speaking_Focus

**User Story:** As a content manager, I want introAudio scripts to be tailored for the speaking_focus curriculum type, so that learners understand the speaking-centric nature of the curriculum and are prepared for each session's speaking tasks.

#### Acceptance Criteria

1. WHEN an introAudio is created for S1 (single-language), THE script SHALL teach the 5 vocabulary words with pronunciation emphasis AND explain the speaking tasks that follow.
2. WHEN an introAudio is created for S2 (single-language), THE script SHALL teach the 5 new vocabulary words, recap S1 speaking, AND preview the debate/summarization speaking tasks.
3. WHEN an introAudio is created for S3 (single-language), THE script SHALL review all 10 vocabulary words and explain the extended speaking tasks (monologue + counter-argument).
4. WHEN an introAudio is created for S4 (single-language), THE script SHALL recap the entire speaking journey across S1-S3 and set up the capstone presentation and impromptu response.
5. WHEN the farewell introAudio is created for S4 (single-language), THE script (400-600 words) SHALL review vocabulary, summarize the speaking progression, and provide a warm farewell.
6. WHEN introAudio activities are created for bilingual sessions, THE scripts SHALL use bilingual delivery (teaching in `user_language`, examples in `target_language`, pronunciation guidance in `user_language`).

### Requirement 19: Folder and README Structure

**User Story:** As a content manager, I want the speaking-focus series to have its own folder with a README tracking creation details, so that content is recoverable and auditable.

#### Acceptance Criteria

1. THE workspace SHALL contain a dedicated folder `speaking-focus-curriculum/` for the series.
2. WHEN all curriculums in the series are successfully created, THE folder SHALL contain a README.md documenting: collection ID and title, Series 1 ID and title, Series 2 ID and title, curriculum IDs and titles, how content was created, SQL queries to find the curriculums in the DB, and enough context to recreate if needed.
3. WHEN all curriculums are verified in the database, THE source Python scripts SHALL be deleted from the folder, leaving only the README.
