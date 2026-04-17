# Requirements Document

## Introduction

Create 60 short, beginner-level, single-session curriculums for Vietnamese learners: 30 for vi-en (Vietnamese learners studying English) and 30 for vi-zh (Vietnamese learners studying Chinese). Each curriculum is a self-contained ~15-30 minute learning experience with 3-5 vocabulary words and a single learning session. Priced at 9 credits each.

This is a new curriculum format — "short single-session" — distinct from the standard 5-session, 18-word structure. The short format targets beginners who want bite-sized, focused practice on a specific skill (speaking, writing, vocabulary, or reading) within a single topic. The 60 curriculums span diverse topics and vary across skillFocusTags types so that the resulting catalog offers a mix of speaking-focused, writing-focused, vocab-focused, reading-focused, and balanced-skills short lessons.

The skillFocusTags are auto-computed by the platform based on activity composition (>55% of non-audio practice minutes in one skill group = that skill's tag). The curriculum designer controls the tag outcome by choosing which activities to include and in what proportion.

### What This Spec Covers

- Definition of the short single-session curriculum format for beginner level
- 4 activity-sequence templates (one per skillFocusTags target) that produce the desired auto-classification
- Topic plan for 30 vi-en and 30 vi-zh curriculums with varied topics and skill focuses
- Collection and series organization for both language pairs
- Pricing at 9 credits per curriculum
- Creation workflow, validation, verification, and documentation

### What This Spec Does NOT Cover

- Changes to existing curriculums
- Standard 5-session curriculum creation
- Content generation pipeline (audio, illustrations) — curriculums are created private
- Other language pairs beyond vi-en and vi-zh

## Glossary

- **Short_Curriculum**: A single-session curriculum with 3-5 vocabulary words designed for a ~15-30 minute learning experience. Contains exactly 1 learning session with ordered activities.
- **Curriculum_Creator**: The system of standalone Python scripts that generate curriculum JSON content and upload it via the REST API.
- **Content_Validator**: Validation logic that checks curriculum JSON against the Content Corruption Detection Rules before upload, adapted for the short single-session format.
- **Collection_Organizer**: The orchestrator scripts that create collections, series, wire them together, and set display orders via the REST API.
- **Tone_Assigner**: The logic that assigns description tones and farewell tones to each curriculum and series, ensuring variety constraints are met.
- **Language_Pair**: A combination of `userLanguage` and `language` using ISO 639-1 codes. This spec covers vi-en (userLanguage=vi, language=en) and vi-zh (userLanguage=vi, language=zh).
- **Skill_Focus_Target**: The intended skillFocusTags classification for a curriculum, achieved by designing the activity sequence so that the dominant skill group exceeds 55% of non-audio practice minutes. Valid targets: balanced_skills, speaking_focus, writing_lover, reader.
- **Activity_Template**: A predefined activity sequence for a Short_Curriculum that produces a specific Skill_Focus_Target when the platform auto-computes skillFocusTags.
- **Persuasive_Copy**: The required writing style for all learner-facing marketing text — emotional sales copy with bold headline, concrete examples, vivid metaphor, transformation promise, and personal growth tie-in.
- **Tone_Palette**: The 6 rhetorical opener types: provocative_question, bold_declaration, vivid_scenario, empathetic_observation, surprising_fact, metaphor_led.
- **Farewell_Palette**: The 5 emotional registers for farewell introAudio scripts: introspective_guide, warm_accountability, team_building_energy, quiet_awe, practical_momentum.
- **Strip_Keys**: Auto-generated platform keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId) that must never be included in new curriculum content.

## Requirements

### Requirement 1: Short Single-Session Curriculum Format

**User Story:** As a platform owner, I want a new short curriculum format with a single learning session and 3-5 vocabulary words, so that beginners can complete a focused learning experience in ~15-30 minutes without committing to a multi-session curriculum.

#### Acceptance Criteria

1. THE Short_Curriculum SHALL contain exactly 1 learning session.
2. THE Short_Curriculum SHALL contain between 3 and 5 vocabulary words (inclusive), with the exact count chosen per curriculum based on topic complexity.
3. THE Short_Curriculum session SHALL include an introAudio activity as the first activity that welcomes the learner, introduces the topic, and teaches all vocabulary words with definitions and example sentences.
4. THE Short_Curriculum session SHALL include a farewell introAudio as the last activity that reviews 2-3 key vocabulary words with fresh example sentences and provides a warm sign-off.
5. THE Short_Curriculum SHALL include `contentTypeTags` at the top level of the content JSON (use `[]` for general content).
6. THE Short_Curriculum SHALL never include Strip_Keys in the content JSON.
7. THE Short_Curriculum SHALL set `language` and `userLanguage` as top-level body parameters in the `curriculum/create` API call.
8. WHEN a vi-en Short_Curriculum is created, THE Curriculum_Creator SHALL set `language: "en"` and `userLanguage: "vi"`.
9. WHEN a vi-zh Short_Curriculum is created, THE Curriculum_Creator SHALL set `language: "zh"` and `userLanguage: "vi"`.

### Requirement 2: Activity Templates by Skill Focus Target

**User Story:** As a platform owner, I want 4 distinct activity-sequence templates that each produce a different skillFocusTags classification, so that the 60 curriculums span all skill focus types and learners can filter by their preferred learning style.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL use one of 4 Activity_Templates for each Short_Curriculum, chosen based on the desired Skill_Focus_Target.

2. WHEN the Skill_Focus_Target is `speaking_focus`, THE session SHALL include activities in this order: introAudio (teach all words with pronunciation emphasis), viewFlashcards, speakFlashcards, reading (short passage), speakReading, readAlong, introAudio (farewell with vocab review).

3. WHEN the Skill_Focus_Target is `writing_lover`, THE session SHALL include activities in this order: introAudio (teach all words), viewFlashcards, reading (short model text showing vocabulary in simple sentences), readAlong, writingSentence (one item per vocab word — each with example sentence and substitution pattern), writingParagraph (guided 2-3 sentence fill-in task using vocab), introAudio (farewell with vocab review).

4. WHEN the Skill_Focus_Target is `reader`, THE session SHALL include activities in this order: introAudio (teach all words), viewFlashcards, speakFlashcards, reading (passage, ~100-150 words), readAlong, introAudio (farewell with vocab review).

5. WHEN the Skill_Focus_Target is `balanced_skills`, THE session SHALL include activities in this order: introAudio (teach all words), viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading (passage using words in context), speakReading, readAlong, writingSentence (2-3 items targeting key words), introAudio (farewell with vocab review).

### Requirement 3: Language Pair Coverage and Curriculum Counts

**User Story:** As a platform owner, I want exactly 30 short curriculums per language pair (vi-en and vi-zh), so that both Vietnamese-English and Vietnamese-Chinese learners have equal access to beginner short-format content.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL produce exactly 30 Short_Curriculums for the vi-en language pair.
2. THE Curriculum_Creator SHALL produce exactly 30 Short_Curriculums for the vi-zh language pair.
3. WHEN creating a vi-en Short_Curriculum, THE Curriculum_Creator SHALL write all user-facing text (titles, descriptions, previews, introAudio scripts, writing prompts, activity titles, activity descriptions, session title) in Vietnamese and reading passages in English.
4. WHEN creating a vi-zh Short_Curriculum, THE Curriculum_Creator SHALL write all user-facing text in Vietnamese and reading passages in Chinese.
5. THE Curriculum_Creator SHALL ensure vocabulary words for vi-en curriculums are common English words appropriate for beginner-level Vietnamese learners.
6. THE Curriculum_Creator SHALL ensure vocabulary words for vi-zh curriculums are common Chinese words (in simplified characters) appropriate for beginner-level Vietnamese learners.

### Requirement 4: Skill Focus Distribution

**User Story:** As a platform owner, I want the 30 curriculums per language pair distributed across all 5 skill focus types, so that learners can choose short lessons optimized for their preferred learning style.

#### Acceptance Criteria

1. WITHIN each language pair (vi-en and vi-zh), THE 30 Short_Curriculums SHALL be distributed across Skill_Focus_Targets as follows: 8 speaking_focus, 8 writing_lover, 7 reader, 7 balanced_skills.
2. THE Tone_Assigner SHALL ensure no two adjacent curriculums within the same series share the same Skill_Focus_Target.
3. Each Skill_Focus_Target SHALL appear across at least 3 different topic areas within each language pair.

### Requirement 5: Topic Plan for vi-en (30 Curriculums)

**User Story:** As a platform owner, I want a concrete topic plan for the 30 vi-en short curriculums, so that content creators know exactly what to build and topics are relevant to Vietnamese beginners learning English.

#### Acceptance Criteria

1. THE 30 vi-en Short_Curriculums SHALL cover the following topic areas, with each topic area containing 3-5 curriculums of varied Skill_Focus_Targets:

   **Everyday Life (6 curriculums)**
   - Greetings and introductions (balanced_skills)
   - At the market / shopping (speaking_focus)
   - Ordering food and drinks (speaking_focus)
   - Asking for directions (reader)
   - Daily routines (writing_lover)
   - Weather and seasons (balanced_skills)

   **Family and Relationships (6 curriculums)**
   - Family members and roles (reader)
   - Describing people's appearance (writing_lover)
   - Feelings and emotions (balanced_skills)
   - Making friends (speaking_focus)
   - Celebrations and birthdays (reader)
   - Helping at home (writing_lover)

   **School and Work (6 curriculums)**
   - Classroom objects and actions (balanced_skills)
   - My school day (reader)
   - Simple job descriptions (writing_lover)
   - Talking about hobbies (speaking_focus)
   - Numbers, time, and dates (balanced_skills)
   - Writing about yourself (writing_lover)

   **Food and Health (6 curriculums)**
   - Fruits and vegetables (reader)
   - Cooking simple dishes (writing_lover)
   - At the doctor's office (speaking_focus)
   - Healthy habits (balanced_skills)
   - Vietnamese food in English (writing_lover)
   - Body parts and exercise (speaking_focus)

   **Travel and Places (6 curriculums)**
   - At the airport (speaking_focus)
   - Hotel check-in (balanced_skills)
   - Famous places in Vietnam (reader)
   - Transportation vocabulary (speaking_focus)
   - Writing a postcard (writing_lover)
   - At the beach (reader)

2. THE Curriculum_Creator SHALL select 3-5 vocabulary words per curriculum that are high-frequency, concrete, and appropriate for absolute beginners.
3. THE Curriculum_Creator SHALL ensure no two curriculums within the same series have overlapping vocabulary lists.
4. WHEN creating vi-en reading passages, THE Curriculum_Creator SHALL use simple sentences (under 15 words average), present tense primarily, and high-frequency vocabulary beyond the target words.

### Requirement 6: Topic Plan for vi-zh (30 Curriculums)

**User Story:** As a platform owner, I want a concrete topic plan for the 30 vi-zh short curriculums, so that content creators know exactly what to build and topics are relevant to Vietnamese beginners learning Chinese.

#### Acceptance Criteria

1. THE 30 vi-zh Short_Curriculums SHALL cover the following topic areas, with each topic area containing 3-5 curriculums of varied Skill_Focus_Targets:

   **Everyday Life (6 curriculums)**
   - Greetings and self-introduction (balanced_skills)
   - At the store / buying things (speaking_focus)
   - Ordering at a restaurant (speaking_focus)
   - Asking for directions in Chinese (reader)
   - My daily schedule (writing_lover)
   - Weather and clothing (balanced_skills)

   **Family and Relationships (6 curriculums)**
   - Family members (reader)
   - Describing people (writing_lover)
   - Expressing feelings (balanced_skills)
   - Making Chinese friends (speaking_focus)
   - Chinese New Year traditions (reader)
   - Household chores (writing_lover)

   **School and Work (6 curriculums)**
   - School supplies and subjects (balanced_skills)
   - A day at school (reader)
   - Common jobs (writing_lover)
   - Talking about interests (speaking_focus)
   - Numbers and counting (balanced_skills)
   - Writing about my life (writing_lover)

   **Food and Health (6 curriculums)**
   - Common Chinese foods (reader)
   - A simple recipe (writing_lover)
   - Visiting the doctor (speaking_focus)
   - Staying healthy (balanced_skills)
   - Vietnamese vs Chinese cuisine (writing_lover)
   - Parts of the body (speaking_focus)

   **Travel and Places (6 curriculums)**
   - At the train station (speaking_focus)
   - Checking into a hotel (balanced_skills)
   - Famous places in China (reader)
   - Getting around the city (speaking_focus)
   - Writing about a trip (writing_lover)
   - At the park (reader)

2. THE Curriculum_Creator SHALL select 3-5 vocabulary words per curriculum using simplified Chinese characters appropriate for absolute beginners.
3. THE Curriculum_Creator SHALL ensure no two curriculums within the same series have overlapping vocabulary lists.
4. WHEN creating vi-zh reading passages, THE Curriculum_Creator SHALL use simple sentences, basic grammar patterns (是, 有, 在, 了, 的), and high-frequency characters beyond the target words.

### Requirement 7: Collection and Series Organization

**User Story:** As a platform owner, I want the 60 short curriculums organized into collections and series with proper hierarchy, so that learners can browse and discover content by topic and language.

#### Acceptance Criteria

1. THE Collection_Organizer SHALL create 1 collection for vi-en short curriculums with a Vietnamese title and informative description.
2. THE Collection_Organizer SHALL create 1 collection for vi-zh short curriculums with a Vietnamese title and informative description.
3. THE Collection_Organizer SHALL organize each collection into 5 series (one per topic area: Everyday Life, Family and Relationships, School and Work, Food and Health, Travel and Places), each containing 6 curriculums.
4. THE Collection_Organizer SHALL create each series via `curriculum-series/create` with a Vietnamese title and description (≤255 characters) using a tone from the Tone_Palette.
5. THE Collection_Organizer SHALL wire each series to its parent collection via `curriculum-collection/addSeriesToCollection`.
6. THE Collection_Organizer SHALL set display orders for all series within each collection via `curriculum-series/setDisplayOrder`.
7. THE Collection_Organizer SHALL set display orders for all curriculums within each series via `curriculum/setDisplayOrder`.
8. THE Collection_Organizer SHALL ensure all curriculums within a single series share the same `language` and `userLanguage` values.
9. WHILE assigning series description tones within a collection, THE Tone_Assigner SHALL ensure no two adjacent series use the same Tone_Palette type.

### Requirement 8: Pricing

**User Story:** As a platform owner, I want all 60 short curriculums priced at 9 credits each, so that the pricing reflects the shorter format compared to standard curriculums.

#### Acceptance Criteria

1. WHEN a Short_Curriculum is created, THE Curriculum_Creator SHALL call `curriculum/setPrice` with `price: 9` for each curriculum.
2. THE Curriculum_Creator SHALL set the price after the curriculum is successfully created and added to its series.

### Requirement 9: Content Quality — Persuasive Copy and Tone Variety

**User Story:** As a content quality owner, I want all learner-facing text to follow the persuasive copy standards with tone variety, so that descriptions are engaging and non-repetitive.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL write every curriculum description following the Persuasive_Copy structure: ALL-CAPS headline, concrete examples, vivid metaphor, transformation promise, and personal growth tie-in.
2. THE Curriculum_Creator SHALL write every curriculum preview as expanded persuasive copy (~100-120 words for short format) with vivid hooks, vocabulary word listing, and learning journey description.
3. THE Tone_Assigner SHALL assign one of the 6 Tone_Palette types to every curriculum description headline and series description.
4. WHILE assigning tones within a series, THE Tone_Assigner SHALL ensure no two adjacent curriculums use the same Tone_Palette type.
5. THE Tone_Assigner SHALL ensure no single Tone_Palette type exceeds 30% of descriptions per language pair.
6. THE Tone_Assigner SHALL assign one of the 5 Farewell_Palette registers to every farewell introAudio script.
7. WHILE assigning farewell tones within a series, THE Tone_Assigner SHALL ensure no two adjacent curriculums use the same Farewell_Palette register.
8. THE Curriculum_Creator SHALL write series descriptions as short persuasive hooks (≤255 characters) using the assigned Tone_Palette type.
9. THE Curriculum_Creator SHALL write collection descriptions as short informative category summaries (not persuasive copy).

### Requirement 10: introAudio Quality for Short Format

**User Story:** As a content quality owner, I want introAudio scripts adapted for the short single-session format, so that learners get a complete vocabulary teaching and farewell experience within one session.

#### Acceptance Criteria

1. WHEN the welcome introAudio is created, THE script (300-500 words) SHALL welcome the learner, set the scene with vivid context, list all vocabulary words, and teach each word with: part of speech, definition in Vietnamese, example sentence in the target language, and brief usage explanation.
2. WHEN the farewell introAudio is created, THE script (200-400 words) SHALL review 2-3 key vocabulary words with definitions and fresh example sentences, summarize what the learner accomplished, and close with a warm sign-off using the assigned Farewell_Palette register.
3. THE introAudio scripts SHALL be fully bilingual with Vietnamese explanations for every concept in the target language.
4. THE Curriculum_Creator SHALL individually craft every introAudio script for its specific curriculum topic, without using template functions or string interpolation.

### Requirement 11: Beginner-Level Content Standards

**User Story:** As a content quality owner, I want all content calibrated for absolute beginners, so that Vietnamese learners with no prior English/Chinese knowledge can follow along without frustration.

#### Acceptance Criteria

1. WHEN a vi-en reading passage is created, THE passage SHALL use simple sentences (under 15 words average), present tense primarily, and high-frequency vocabulary.
2. WHEN a vi-zh reading passage is created, THE passage SHALL use simple sentences, basic grammar patterns, and high-frequency characters.
3. WHEN writingSentence prompts are created, THE prompts SHALL provide maximum scaffolding for beginners: full Vietnamese instructions, a complete example sentence in the target language that the learner can closely imitate, the target vocabulary word highlighted, and a fill-in-the-blank or substitution pattern so the learner only needs to change 1-2 words from the example.
4. WHEN a writingParagraph prompt is created (writing_lover template), THE prompt SHALL be a guided 2-3 sentence writing task (not a full paragraph): provide a Vietnamese-language template with blanks to fill using the target vocabulary, a completed example in the target language to model the expected output, and explicit instructions in Vietnamese on which words to substitute. The task should feel like structured fill-in rather than free composition.
5. THE Short_Curriculum SHALL NOT include `vocabLevel3` activities (to reduce cognitive load for beginners).
6. THE Short_Curriculum SHALL NOT include `vocabLevel1` or `vocabLevel2` in the reader, speaking_focus, or writing_lover templates (these templates prioritize other skills over vocab drill; only balanced_skills includes vocab levels).

### Requirement 12: Activity Schema Compliance

**User Story:** As a platform developer, I want every activity to comply with the platform's content schema, so that the content pipeline processes them without errors.

#### Acceptance Criteria

1. Each Activity SHALL include `activityType`, `title`, `description`, and `data` fields.
2. THE `activityType` field SHALL use one of the valid values: introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence, writingParagraph.
3. THE `vocabList` field SHALL be an array of lowercase strings, using the field name `vocabList` (never `words`).
4. WHEN viewFlashcards and speakFlashcards appear in the same session, THE two activities SHALL have identical `vocabList` arrays.
5. All content data SHALL be inside the `data` object, not inline on the activity object.
6. WHEN a writingSentence activity is created, THE activity SHALL have `data.vocabList`, `data.items` (non-empty array), and each item SHALL have `prompt` (Vietnamese instructions with example sentence and substitution pattern) and `targetVocab` fields.
7. WHEN a writingParagraph activity is created, THE activity SHALL have `data.vocabList`, `data.instructions` (non-empty string in Vietnamese with a completed model text and fill-in guidance), and `data.prompts` (array of strings, length ≥ 2, each prompt a guided substitution task rather than open-ended composition).
8. THE Curriculum_Creator SHALL follow the activity title/description conventions: viewFlashcards/speakFlashcards/vocabLevel* use "Flashcards: <topic>"; reading/speakReading use "Đọc: <topic>"; readAlong uses "Nghe: <topic>"; introAudio uses descriptive labels; writingSentence/writingParagraph use "Viết: <topic>".

### Requirement 13: Content Validation

**User Story:** As a platform developer, I want every curriculum validated before upload, so that no corrupted content enters the database.

#### Acceptance Criteria

1. THE Content_Validator SHALL verify that every Short_Curriculum content JSON has non-null, non-empty `title`, `description`, and `preview.text` fields.
2. THE Content_Validator SHALL verify that `learningSessions` is an array of exactly 1 session with a non-empty `title` and `activities` array.
3. THE Content_Validator SHALL verify that every activity has `activityType` (not `type`), `title`, `description`, and `data` fields, with content fields inside `data`.
4. THE Content_Validator SHALL verify that `activityType` values are valid.
5. THE Content_Validator SHALL verify that vocabList fields contain arrays of lowercase strings using the field name `vocabList`.
6. THE Content_Validator SHALL verify that viewFlashcards and speakFlashcards in the same session have identical vocabList arrays.
7. THE Content_Validator SHALL verify writingSentence and writingParagraph data structures.
8. THE Content_Validator SHALL verify that no Strip_Keys appear anywhere in the content JSON.
9. THE Content_Validator SHALL verify that the curriculum contains between 3 and 5 unique vocabulary words.
10. IF any validation check fails, THEN THE Content_Validator SHALL abort the upload and print the specific rule violation.

### Requirement 14: Script Architecture and Workflow

**User Story:** As a developer, I want a clear, repeatable workflow for creating 60 short curriculums, so that the process is manageable and traceable.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL produce one standalone Python script per curriculum (60 scripts total).
2. THE Curriculum_Creator SHALL produce one orchestrator script per language pair that creates collections, series, wires them together, sets display orders, and sets prices.
3. THE Curriculum_Creator SHALL organize scripts into a single directory `vi-beginner-short-curriculums/` with subdirectories `vi-en/` and `vi-zh/`.
4. THE Curriculum_Creator SHALL authenticate all API calls using `firebase_token.get_firebase_id_token` with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`.
5. THE Curriculum_Creator SHALL use `https://helloapi.step.is` as the API base URL.
6. THE Curriculum_Creator SHALL individually craft every piece of learner-facing text for its specific curriculum topic, without using template functions, string interpolation, or generic fill-in-the-blank patterns.
7. THE Curriculum_Creator MAY use shared helper functions for activity structure (types, order, data schema) but SHALL hand-write all text content per curriculum.
8. IF a curriculum creation API call fails, THEN THE Curriculum_Creator SHALL log the error with the curriculum title and series context, and continue with the next curriculum.

### Requirement 15: Newly Created Curriculums Must Be Private

**User Story:** As a platform owner, I want all newly created curriculums to be private by default, so that they go through content generation (audio, illustrations) before being exposed to learners.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL NOT call `curriculum/setPublic` with `isPublic: true` on any newly created Short_Curriculum.

### Requirement 16: Curriculum Titles

**User Story:** As a content quality owner, I want curriculum titles to be minimal and descriptive, so that they work well within the series/collection context without redundancy.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL keep curriculum titles minimal — never repeating series/collection name, content type prefix, skill-focus label, difficulty level, or audience suffix.
2. THE Curriculum_Creator SHALL write curriculum titles in Vietnamese for both vi-en and vi-zh curriculums.

### Requirement 17: Documentation and Cleanup

**User Story:** As a developer, I want proper documentation after all curriculums are created, so that the content is traceable and reproducible.

#### Acceptance Criteria

1. WHEN all curriculums for a language pair are created and verified, THE Curriculum_Creator SHALL create a README.md documenting: collection ID, all series IDs, all curriculum IDs with titles and display orders, vocabulary lists per curriculum, tone assignments (description and farewell), skill focus targets, and SQL verification queries.
2. WHEN all curriculums are verified in the database, THE source Python scripts SHALL be deleted, leaving only the README.
3. THE Curriculum_Creator SHALL run a duplicate check query for each curriculum title after creation and resolve any duplicates (keep earliest, delete extras).

### Requirement 18: Execution Order

**User Story:** As a developer, I want a phased execution plan, so that I can manage the workload incrementally and catch issues early.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL execute creation in 2 phases: vi-en first, then vi-zh.
2. WHEN starting a language pair phase, THE Curriculum_Creator SHALL first create the orchestrator infrastructure (collection, series, wiring) before creating any curriculums.
3. WHEN completing a series (6 curriculums), THE Curriculum_Creator SHALL verify the series by querying the database to confirm all 6 curriculums exist with correct display orders, language values, prices, and non-empty content.
4. WHEN completing a language pair (30 curriculums), THE Curriculum_Creator SHALL verify language homogeneity and display order completeness across all series.
5. IF verification reveals missing or malformed curriculums, THEN THE Curriculum_Creator SHALL recreate the affected curriculums before proceeding.
