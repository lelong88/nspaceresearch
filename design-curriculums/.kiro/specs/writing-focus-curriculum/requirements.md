# Requirements Document

## Introduction

Add a new curriculum type `writing_focus` to the language-learning platform. Unlike the existing `balanced_skills` type (which distributes time across reading, listening, speaking, and writing), `writing_focus` makes writing the centerpiece — trading speaking activities (`speakFlashcards`, `speakReading`) and deep vocab drill (`vocabLevel3`) for sustained, progressive writing practice via `writingSentence` and `writingParagraph`.

The platform already supports `balanced_skills`, `reader`, `vocab_acquisition`, and `speaking_focus` curriculum types. This spec adds `writing_focus` as the fifth type, then creates 4 initial curriculums to demonstrate it — uploaded to the platform via standalone Python scripts.

### Two Variants

1. **Single-language (en-en)** — For upper-intermediate to advanced learners. 4 sessions. Writing dominates: `writingParagraph` appears in every session, prompts escalate from paragraph response → compare/contrast → analytical essay → argumentative/persuasive capstone. Vocab is minimal scaffolding (10 words across S1-S2, no `vocabLevel3`). No speaking activities.

2. **Bilingual (vi-en / vi-zh)** — For beginner to intermediate learners. 4 sessions. Writing is scaffolded more heavily: `writingSentence` dominates S1-S3, `writingParagraph` appears only in S3-S4. Prompts are in `user_language`, responses in `target_language`. No speaking activities.

### Proposed Collection & Series

**Collection:** A new top-level collection for writing-focus curriculums (or added to an existing skills-focused collection if appropriate).

**Series:** A new series containing 4 initial curriculums demonstrating the `writing_focus` type. The initial batch includes a mix of single-language and bilingual curriculums to demonstrate both variants.

### What This Spec Covers

- Definition of the `writing_focus` curriculum type (both single-language and bilingual variants)
- Session structures and activity sequences for both variants
- Creation of 4 initial curriculums uploaded to the platform
- Collection and series setup for the new curriculums
- Post-creation verification and cleanup

### What This Spec Does NOT Cover

- `speaking_focus` and `audio_guide` curriculum types (separate specs)
- Changes to existing `balanced_skills` curriculums
- Client-side UI changes for the new curriculum type

## Glossary

- **Writing_Focus_Curriculum**: A curriculum where writing is the centerpiece activity. Speaking activities (`speakFlashcards`, `speakReading`) and deep vocab drill (`vocabLevel3`) are dropped. `writingParagraph` and/or `writingSentence` appear in every learning session.
- **Single_Language_Variant**: The `writing_focus` variant for upper-intermediate to advanced learners (e.g., en-en). 4 sessions, 10 vocab words across S1-S2, `writingParagraph` in every session, prompts escalate in complexity.
- **Bilingual_Variant**: The `writing_focus` variant for beginner to intermediate learners (e.g., vi-en, vi-zh). 4 sessions, 10 vocab words across S1-S2, `writingSentence` dominates S1-S3, `writingParagraph` introduced at S3. Writing prompts in `user_language`, responses in `target_language`.
- **Model_Text**: A reading passage provided in S1-S2 that the learner reads before writing a response. The model text sets the topic and provides vocabulary in context.
- **Prompt_Escalation**: The progressive increase in writing complexity across sessions: sentence-level → paragraph response → compare/contrast → analytical essay → argumentative/persuasive capstone (single-language) or sentence-level → guided paragraph → independent paragraph (bilingual).
- **Collection**: Top-level organizational shelf in the platform.
- **Series**: A thematic grouping within a collection, containing multiple curriculums.
- **Curriculum**: A single learning unit with vocabulary words, sessions, and activities.
- **Session**: One of 4 ordered segments within a writing_focus curriculum.
- **Activity**: An individual learning exercise within a session.
- **Creation_Script**: A standalone Python script that calls the helloapi REST API to create a curriculum.
- **Strip_Keys**: The set of auto-generated platform keys that must never appear in new content.
- **API**: The helloapi.step.is REST API used for all CRUD operations.
- **Display_Order**: Integer field controlling sort position of curriculums within a series and series within a collection.
- **Persuasive_Copy**: The required emotional sales copy style for all learner-facing text.

## Requirements

### Requirement 1: Single-Language Variant — Session Structure (en-en, Upper-Intermediate → Advanced)

**User Story:** As a content manager, I want the single-language writing_focus variant to have a clear 4-session structure with escalating writing demands, so that advanced learners progressively build sustained composition skills.

#### Acceptance Criteria

1. THE Writing_Focus_Curriculum (single-language) SHALL contain exactly 4 sessions.
2. THE Writing_Focus_Curriculum (single-language) SHALL contain exactly 10 vocabulary words divided into 2 groups of 5 (W1 for S1, W2 for S2).
3. WHEN Session 1 is created, THE Session SHALL contain activities in this exact order: `introAudio` (teach 5 words + explain writing task), `viewFlashcards`, `vocabLevel1`, `vocabLevel2`, `reading` (model text), `readAlong`, `writingSentence` (5 targeted sentences), `writingParagraph` (respond to model text).
4. WHEN Session 2 is created, THE Session SHALL contain activities in this exact order: `introAudio` (teach 5 more words + recap S1 writing), `viewFlashcards`, `vocabLevel1`, `vocabLevel2`, `reading` (second passage, different angle on same topic), `readAlong`, `writingSentence` (5 sentences), `writingParagraph` (compare/contrast the two passages).
5. WHEN Session 3 is created, THE Session SHALL contain activities in this exact order: `introAudio` (review all 10 words), `viewFlashcards` (all 10 words), `vocabLevel1`, `vocabLevel2`, `writingParagraph` (analytical essay prompt using all vocab, 6-8 sentences, more demanding rubric).
6. WHEN Session 4 is created, THE Session SHALL contain activities in this exact order: `introAudio` (recap journey), `reading` (full article), `readAlong`, `writingParagraph` (argumentative/persuasive response — the capstone), `introAudio` (farewell).

### Requirement 2: Bilingual Variant — Session Structure (vi-en / vi-zh, Beginner → Intermediate)

**User Story:** As a content manager, I want the bilingual writing_focus variant to scaffold writing more heavily with sentence-level practice before introducing paragraphs, so that beginner-to-intermediate learners build writing confidence gradually.

#### Acceptance Criteria

1. THE Writing_Focus_Curriculum (bilingual) SHALL contain exactly 4 sessions.
2. THE Writing_Focus_Curriculum (bilingual) SHALL contain exactly 10 vocabulary words divided into 2 groups of 5 (W1 for S1, W2 for S2).
3. WHEN Session 1 is created, THE Session SHALL contain activities in this exact order: `introAudio`, `introAudio` (bilingual vocab teaching), `viewFlashcards`, `vocabLevel1`, `vocabLevel2`, `introAudio` (reading intro), `reading`, `readAlong`, `writingSentence` (5 sentences with bilingual prompts).
4. WHEN Session 2 is created, THE Session SHALL contain activities in this exact order: `introAudio`, `introAudio` (bilingual vocab teaching), `viewFlashcards`, `vocabLevel1`, `vocabLevel2`, `introAudio` (reading intro), `reading`, `readAlong`, `writingSentence` (5 sentences, slightly less scaffolding).
5. WHEN Session 3 is created, THE Session SHALL contain activities in this exact order: `introAudio`, `introAudio` (review all vocab), `viewFlashcards` (all 10 words), `vocabLevel1`, `vocabLevel2`, `writingSentence` (3 sentences combining S1+S2 vocab), `writingParagraph` (guided paragraph — prompt gives structure in `user_language`).
6. WHEN Session 4 is created, THE Session SHALL contain activities in this exact order: `introAudio`, `reading` (full text), `readAlong`, `writingParagraph` (less scaffolded — learner writes independently), `introAudio` (farewell).

### Requirement 3: Writing_Focus Type Differentiation from Balanced_Skills

**User Story:** As a content manager, I want the writing_focus type to be clearly differentiated from balanced_skills, so that the curriculum structure enforces the writing-centric pedagogy.

#### Acceptance Criteria

1. THE Writing_Focus_Curriculum SHALL NOT include `speakFlashcards` activities in any session.
2. THE Writing_Focus_Curriculum SHALL NOT include `speakReading` activities in any session.
3. THE Writing_Focus_Curriculum SHALL NOT include `vocabLevel3` activities in any session.
4. THE Writing_Focus_Curriculum SHALL include `writingParagraph` in every session of the single-language variant (S1-S4).
5. THE Writing_Focus_Curriculum (bilingual) SHALL include `writingSentence` in every learning session (S1-S3) and `writingParagraph` in S3-S4.
6. THE Writing_Focus_Curriculum SHALL use vocabulary as a tool for writing (10 words across 2 sessions) rather than as the primary learning goal (unlike balanced_skills which uses 18 words across 3 sessions).

### Requirement 4: Writing Prompt Escalation — Single-Language

**User Story:** As a content manager, I want writing prompts to escalate in complexity across sessions, so that learners progress from guided responses to independent argumentative composition.

#### Acceptance Criteria

1. WHEN Session 1 `writingSentence` is created, THE Activity SHALL contain 5 items with targeted sentence prompts that use the session's vocabulary in context related to the model text.
2. WHEN Session 1 `writingParagraph` is created, THE Activity SHALL prompt the learner to write a paragraph responding to the model text (direct response, not comparative).
3. WHEN Session 2 `writingParagraph` is created, THE Activity SHALL prompt the learner to compare and contrast the two passages from S1 and S2.
4. WHEN Session 3 `writingParagraph` is created, THE Activity SHALL prompt the learner to write an analytical essay (6-8 sentences) using all 10 vocabulary words, with a more demanding rubric than S1-S2.
5. WHEN Session 4 `writingParagraph` is created, THE Activity SHALL prompt the learner to write an argumentative or persuasive response as the capstone composition.

### Requirement 5: Writing Prompt Scaffolding — Bilingual

**User Story:** As a content manager, I want bilingual writing prompts to provide scaffolding in the learner's native language, so that beginner-to-intermediate learners can focus on producing target-language text without struggling to understand the prompt itself.

#### Acceptance Criteria

1. WHEN a bilingual `writingSentence` activity is created, THE Activity SHALL present the writing prompt in `user_language` (e.g., Vietnamese) and require the response in `target_language` (e.g., English or Chinese).
2. WHEN Session 1 `writingSentence` is created (bilingual), THE Activity SHALL contain 5 items with bilingual prompts providing full scaffolding (prompt in `user_language`, example in `target_language`).
3. WHEN Session 2 `writingSentence` is created (bilingual), THE Activity SHALL contain 5 items with slightly less scaffolding than S1 (fewer hints, more independence expected).
4. WHEN Session 3 `writingSentence` is created (bilingual), THE Activity SHALL contain 3 items that combine vocabulary from both S1 and S2.
5. WHEN Session 3 `writingParagraph` is created (bilingual), THE Activity SHALL provide a guided paragraph prompt with structural guidance in `user_language` (e.g., suggested paragraph structure, topic sentence hint).
6. WHEN Session 4 `writingParagraph` is created (bilingual), THE Activity SHALL provide a less scaffolded prompt — the learner writes independently with minimal `user_language` guidance.

### Requirement 6: Reading Passages as Model Texts

**User Story:** As a content manager, I want reading passages to serve as model texts that learners respond to in writing, so that reading and writing are tightly integrated rather than separate activities.

#### Acceptance Criteria

1. THE Writing_Focus_Curriculum (single-language) SHALL include a model text reading passage in S1 that introduces the topic and contains the session's vocabulary in context.
2. THE Writing_Focus_Curriculum (single-language) SHALL include a second reading passage in S2 that presents a different angle on the same topic as S1, enabling compare/contrast writing.
3. THE Writing_Focus_Curriculum (single-language) SHALL NOT include a new reading passage in S3 (S3 is a pure writing session — review + composition only).
4. THE Writing_Focus_Curriculum (single-language) SHALL include a full article reading in S4 that combines and extends the S1-S2 passages, serving as the basis for the capstone argumentative response.
5. THE Writing_Focus_Curriculum (bilingual) SHALL include reading passages in S1, S2, and S4 that serve as comprehensible input and model texts for writing responses.
6. THE Writing_Focus_Curriculum (bilingual) SHALL NOT include a new reading passage in S3 (S3 focuses on review + first paragraph writing).

### Requirement 7: Vocabulary Selection and Usage

**User Story:** As a content manager, I want vocabulary to be selected as tools for writing rather than as standalone learning targets, so that the writing_focus curriculum maintains its writing-centric identity.

#### Acceptance Criteria

1. THE Writing_Focus_Curriculum SHALL select 10 vocabulary words that are useful for the writing tasks in the curriculum — words that enable the learner to express ideas about the topic in their compositions.
2. THE Writing_Focus_Curriculum SHALL divide vocabulary into 2 groups of 5 words: W1 (taught in S1) and W2 (taught in S2).
3. WHEN Session 3 reviews vocabulary, THE Session SHALL review all 10 words from both S1 and S2 in the `viewFlashcards` activity.
4. THE Writing_Focus_Curriculum SHALL NOT include `vocabLevel3` in any session — vocabulary depth is achieved through writing practice, not through additional drill levels.
5. THE Writing_Focus_Curriculum vocabulary words SHALL appear in the reading passages (model texts) so that learners encounter the words in context before using them in writing.

### Requirement 8: Content Quality — Persuasive Copy

**User Story:** As a content manager, I want all learner-facing text to follow the persuasive copy style, so that learners feel emotionally engaged and motivated to develop their writing skills.

#### Acceptance Criteria

1. THE Curriculum description SHALL follow the 5-beat persuasive copy structure, adapted to emphasize the writing journey — from guided responses to independent composition.
2. THE Curriculum preview (~150 words) SHALL open with a vivid hook about the power of writing, name the vocabulary words, and describe the writing progression across sessions.
3. WHEN an introAudio activity is created, THE introAudio script SHALL reference the topic, explain how vocabulary connects to the writing tasks, and motivate the learner for the upcoming writing challenge.
4. THE Curriculum SHALL use Vietnamese for all user-facing text in bilingual curriculums and English for single-language curriculums, consistent with the language policy.

### Requirement 9: Activity Metadata

**User Story:** As a content manager, I want every activity to have proper title and description fields, so that server-side logging and client display work correctly.

#### Acceptance Criteria

1. THE Activity SHALL include both a `title` and `description` field for every activity in every session.
2. WHEN a `viewFlashcards`, `vocabLevel1`, or `vocabLevel2` activity is created, THE Activity title SHALL follow the format "Flashcards: <topic>" and the description SHALL list the words being learned.
3. WHEN a `reading` activity is created, THE Activity title SHALL follow the format "Đọc: <topic>" (bilingual) or "Read: <topic>" (single-language) and the description SHALL contain the first ~80 characters of the reading text.
4. WHEN a `readAlong` activity is created, THE Activity title SHALL follow the format "Nghe: <topic>" (bilingual) or "Listen: <topic>" (single-language) and the description SHALL be "Nghe bài đọc và theo dõi." (bilingual) or "Listen and follow along." (single-language).
5. WHEN an `introAudio` activity is created, THE Activity title SHALL be a descriptive label and the description SHALL be a brief summary.
6. WHEN a `writingSentence` activity is created, THE Activity title SHALL follow the format "Viết: <topic>" (bilingual) or "Write: <topic>" (single-language) and the description SHALL briefly summarize the writing task.
7. WHEN a `writingParagraph` activity is created, THE Activity title SHALL follow the format "Viết: <topic>" (bilingual) or "Write: <topic>" (single-language) and the description SHALL briefly summarize the composition task.
8. THE Session object SHALL include a `title` field (e.g., "Session 1: Vocab + Model Text", "Buổi 1: Từ vựng + Bài mẫu").

### Requirement 10: Strip-Keys Compliance

**User Story:** As a content manager, I want new curriculum content to never include auto-generated platform keys, so that the platform correctly generates fresh metadata after upload.

#### Acceptance Criteria

1. THE Curriculum content SHALL NOT include any of the following auto-generated keys: `mp3Url`, `illustrationSet`, `chapterBookmarks`, `segments`, `whiteboardItems`, `userReadingId`, `lessonUniqueId`, `curriculumTags`, `taskId`, `imageId`.

### Requirement 11: Collection and Series Creation

**User Story:** As a content manager, I want to create a collection and series for writing-focus curriculums, so that learners can discover and access writing-focused learning as a distinct content category.

#### Acceptance Criteria

1. WHEN the collection is created, THE API SHALL be called via `curriculum-collection/create` with a descriptive title, a persuasive Vietnamese description, and `isPublic: true`.
2. WHEN the series is created, THE API SHALL be called via `curriculum-series/create` with a descriptive title, a persuasive Vietnamese description (under 255 characters), and `isPublic: true`.
3. WHEN the series is created, THE Creation_Script SHALL call `curriculum-collection/addSeriesToCollection` to wire the series into the collection.
4. THE Creation_Script SHALL assign a display_order to the series via `curriculum-series/setDisplayOrder`.
5. WHEN the series is fully populated, THE Series SHALL contain exactly 4 curriculums.

### Requirement 12: Display Order and Organization

**User Story:** As a content manager, I want curriculums and the series to have explicit display orders, so that they appear in the intended sequence in the client app.

#### Acceptance Criteria

1. WHEN a curriculum is added to the series via `curriculum-series/addCurriculum`, THE Creation_Script SHALL call `curriculum/setDisplayOrder` to assign a sequential integer display order (0, 1, 2, 3) for the 4 curriculums within the series.
2. WHEN all curriculums are created and ordered, THE Series SHALL contain exactly 4 curriculums, sorted by display_order.

### Requirement 13: Script Organization

**User Story:** As a content manager, I want one Python script per curriculum plus an orchestrator script for series-level setup, so that each curriculum's content is self-contained and files remain manageable.

#### Acceptance Criteria

1. THE Creation_Script architecture SHALL use one Python script per curriculum with all text content hand-written in that script.
2. THE Creation_Script architecture SHALL include one orchestrator script that handles collection creation, series creation, adding curriculums to the series, adding the series to the collection, and setting display orders.
3. THE Creation_Script SHALL NOT use template functions, string interpolation, or loops to generate learner-facing text content.
4. WHEN a curriculum is successfully created and verified in the database, THE source script SHALL be deleted, leaving only a README with creation method, SQL queries, and recreation context.

### Requirement 14: No Templated Content

**User Story:** As a content manager, I want every piece of learner-facing text to be individually crafted per curriculum topic, so that each curriculum reads as if written by someone who deeply understands that specific topic.

#### Acceptance Criteria

1. THE Creation_Script SHALL NOT use `f-string` interpolation, template functions, or shared text skeletons to generate introAudio scripts, descriptions, previews, or writing prompts.
2. THE Creation_Script MAY use shared helper functions for activity structure (types, order, data schema) but SHALL hand-write all text content per curriculum.

### Requirement 15: Language and Level Compliance

**User Story:** As a content manager, I want all curriculums to comply with the platform's language policy and level consistency rules, so that the series is internally consistent.

#### Acceptance Criteria

1. THE Curriculum SHALL set `language` and `userLanguage` as top-level body parameters in the `curriculum/create` API call (not only inside the content JSON).
2. WHEN a single-language curriculum is created, THE Curriculum SHALL set `language: "en"` and `userLanguage: "en"`.
3. WHEN a bilingual vi-en curriculum is created, THE Curriculum SHALL set `language: "en"` and `userLanguage: "vi"`.
4. THE Series SHALL contain curriculums within a maximum 1-level gap from the highest-level curriculum in the series.
5. THE Curriculum title SHALL NOT include difficulty level descriptors (e.g., "Upper-Intermediate", "Advanced", "Beginner").

### Requirement 16: Newly Created Curriculums Must Be Private

**User Story:** As a content manager, I want all newly created curriculums to be private by default, so that they go through content generation (audio, illustrations) before being exposed to learners.

#### Acceptance Criteria

1. WHEN a curriculum is created via `curriculum/create`, THE Curriculum SHALL have `is_public: false` (the platform default).
2. THE Creation_Script SHALL NOT call `curriculum/setPublic` with `isPublic: true` on any newly created curriculum.

### Requirement 17: Writing Prompt Format

**User Story:** As a content manager, I want writing prompts to follow a consistent format that provides clear guidance to learners, so that the writing tasks are unambiguous and pedagogically effective.

#### Acceptance Criteria

1. THE `writingSentence` item SHALL include a `targetVocab` field specifying the vocabulary word to use and a `prompt` field with context and an example sentence.
2. WHEN a bilingual `writingSentence` prompt is created, THE prompt SHALL be written in `user_language` with the example sentence in `target_language`, in the format: "[user_language instruction to use the word in a specific context]. Ví dụ: [target_language example sentence]."
3. WHEN a single-language `writingSentence` prompt is created, THE prompt SHALL be written entirely in `target_language` with context and example, in the format: "Use the word 'X' to write about [specific context]. Example: [full example sentence]."
4. THE `writingParagraph` activity SHALL include a `prompt` field with a clear composition task that specifies the expected scope (e.g., number of sentences, whether to compare/contrast, whether to argue a position).

### Requirement 18: Folder and README Structure

**User Story:** As a content manager, I want the writing-focus series to have its own folder with a README tracking creation details, so that content is recoverable and auditable.

#### Acceptance Criteria

1. THE workspace SHALL contain a dedicated folder for the writing-focus curriculum series.
2. WHEN all curriculums in the series are successfully created, THE folder SHALL contain a README.md documenting: collection ID and title, series ID, curriculum IDs and titles, how content was created, SQL queries to find the curriculums in the DB, and enough context to recreate if needed.
3. WHEN all curriculums are verified in the database, THE source Python scripts SHALL be deleted from the folder, leaving only the README.

### Requirement 19: writingParagraph Activity Data Shape

**User Story:** As a content manager, I want the `writingParagraph` activity to have a well-defined data shape, so that the client can render the writing interface correctly.

#### Acceptance Criteria

1. THE `writingParagraph` activity SHALL include a `prompt` field containing the composition task description.
2. THE `writingParagraph` activity SHALL include a `vocabList` field containing the vocabulary words the learner is expected to use in their composition.
3. THE `writingParagraph` activity in S1 (single-language) SHALL reference the model text topic in its prompt and list the S1 vocabulary in `vocabList`.
4. THE `writingParagraph` activity in S3 (single-language) SHALL list all 10 vocabulary words in `vocabList` and specify a more demanding rubric (6-8 sentences, analytical).
5. THE `writingParagraph` activity in S4 (single-language) SHALL specify an argumentative/persuasive task and list all 10 vocabulary words in `vocabList`.

### Requirement 20: introAudio Content for Writing_Focus

**User Story:** As a content manager, I want introAudio scripts to be tailored for the writing_focus curriculum type, so that learners understand the writing-centric nature of the curriculum and are prepared for each session's writing tasks.

#### Acceptance Criteria

1. WHEN an introAudio is created for S1 (single-language), THE script SHALL teach the 5 vocabulary words AND explain the writing task that follows — setting expectations for the model text response.
2. WHEN an introAudio is created for S2 (single-language), THE script SHALL teach the 5 new vocabulary words, recap the S1 writing, AND preview the compare/contrast writing task.
3. WHEN an introAudio is created for S3 (single-language), THE script SHALL review all 10 vocabulary words and explain the analytical essay task with its more demanding rubric.
4. WHEN an introAudio is created for S4 (single-language), THE script SHALL recap the entire writing journey across S1-S3 and set up the capstone argumentative/persuasive composition.
5. WHEN the farewell introAudio is created for S4 (single-language), THE script (400-600 words) SHALL review vocabulary, summarize the writing progression, and provide a warm farewell.
6. WHEN introAudio activities are created for bilingual sessions, THE scripts SHALL use bilingual delivery (teaching in `user_language`, examples in `target_language`).
