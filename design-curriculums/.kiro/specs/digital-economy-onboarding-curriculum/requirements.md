# Requirements Document

## Introduction

Create a single onboarding/demo English-learning curriculum for Vietnamese speakers (userLanguage="vi", language="en") on the topic of "Digital Economy" (Kinh Tế Số). This is a short (<30 minute) curriculum with 1 learning session, balanced_skills type, at the preintermediate level.

The curriculum serves as an onboarding/demo lesson to familiarize new users with the app's features — flashcards, reading, speaking, listening, and writing activities — all within a single compact session. The topic of digital economy is chosen for its relevance to modern Vietnamese professionals and students.

### What This Spec Covers

- 1 individually crafted curriculum for Vietnamese speakers learning English through digital economy content
- Balanced skills type: mix of flashcards, reading, speaking, listening, and writing activities in 1 session
- Preintermediate level with bilingual text (Vietnamese for user-facing text)
- Short duration (<30 minutes)
- Onboarding/demo purpose: showcases all major app activity types
- contentTypeTags: `[]` (not movie/music/podcast/story)
- Pricing: free (0 credits) — onboarding/trial curriculum
- Creation workflow, validation, and documentation
- Curriculum created as private (no setPublic call)

### What This Spec Does NOT Cover

- Changes to existing vi-en curriculums
- Curriculums for other language pairs
- Content generation pipeline (audio, illustrations) — curriculum is created private
- Collection/series organization (standalone onboarding curriculum)
- Advanced or beginner difficulty levels

## Glossary

- **Onboarding_Curriculum**: A short, single-session curriculum designed to introduce new users to the app's learning features through the topic of digital economy. Language pair: vi-en, level: preintermediate.
- **Curriculum_Creator**: The standalone Python script that generates curriculum JSON content and uploads it via the REST API.
- **Content_Validator**: Validation logic that checks curriculum JSON against the Content Corruption Detection Rules before upload.
- **Language_Pair**: userLanguage="vi", language="en" — Vietnamese speakers learning English.
- **Balanced_Skills_Session**: A learning session with equal emphasis on all skill areas: flashcards (view + speak), reading, speaking, listening (readAlong), and writing activities.
- **Persuasive_Copy**: The required writing style for marketing text — emotional sales copy with bold headline, concrete examples, vivid metaphor, transformation promise, and personal growth tie-in.
- **Tone_Palette**: The 6 rhetorical opener types: provocative_question, bold_declaration, vivid_scenario, empathetic_observation, surprising_fact, metaphor_led.
- **Strip_Keys**: Auto-generated platform keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId) that must never be included in new curriculum content.
- **Digital_Economy**: The topic domain covering e-commerce, fintech, digital transformation, online platforms, and the broader shift to technology-driven economic activity.

## Requirements

### Requirement 1: Curriculum Structure and Purpose

**User Story:** As a platform owner, I want a short onboarding curriculum that demonstrates all app features within a single session, so that new users can experience the full learning flow before committing to paid content.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL produce exactly 1 Onboarding_Curriculum for the vi-en language pair on the topic of digital economy.
2. THE Onboarding_Curriculum SHALL have exactly 1 learning session of type balanced_skills.
3. THE Onboarding_Curriculum SHALL be completable in under 30 minutes.
4. THE Onboarding_Curriculum SHALL include `contentTypeTags: []` at the top level of the content JSON.
5. THE Onboarding_Curriculum SHALL never include Strip_Keys in the content JSON.
6. THE Curriculum_Creator SHALL set `language: "en"` and `userLanguage: "vi"` as top-level body parameters in the `curriculum/create` API call.
7. THE Onboarding_Curriculum SHALL be at the preintermediate difficulty level with bilingual text throughout.

### Requirement 2: Vocabulary Selection

**User Story:** As a content quality owner, I want vocabulary words that are relevant to the digital economy topic and appropriate for preintermediate learners, so that users learn practical English while exploring a modern, relevant topic.

#### Acceptance Criteria

1. THE Onboarding_Curriculum SHALL include exactly 5 vocabulary words related to the digital economy domain.
2. THE vocabulary words SHALL be appropriate for preintermediate level — common enough to be useful but not so basic that they feel trivial.
3. THE vocabulary words SHALL cover core digital economy concepts such as: platform, transaction, digital, startup, innovation, or similar terms relevant to the Vietnamese digital economy context.
4. THE `vocabList` field SHALL be an array of lowercase strings using the field name `vocabList` (never `words`).

### Requirement 3: Activity Sequence for Balanced Skills Onboarding

**User Story:** As a platform owner, I want the single session to showcase all major activity types in a logical learning flow, so that new users experience flashcards, reading, speaking, listening, and writing within one compact session.

#### Acceptance Criteria

1. THE single Balanced_Skills_Session SHALL follow this activity sequence:
   - introAudio (welcome + teach all vocabulary words)
   - viewFlashcards (all words)
   - speakFlashcards (all words)
   - vocabLevel1 (all words)
   - reading (expository passage 60-70 words about digital economy in Vietnam)
   - speakReading
   - readAlong
   - writingSentence (2-3 items using vocabulary words)
   - introAudio (farewell with vocab review)

2. WHEN viewFlashcards and speakFlashcards appear in the same session, THE two activities SHALL have identical `vocabList` arrays.
3. THE activity sequence SHALL demonstrate the app's core feature set: visual learning (flashcards), active recall (vocabLevel), reading comprehension, speaking practice, listening practice (readAlong), and writing production.

### Requirement 4: Activity Schema Compliance

**User Story:** As a platform developer, I want every activity to comply with the platform's content schema, so that the content pipeline processes this curriculum without errors.

#### Acceptance Criteria

1. Each Activity SHALL include `activityType`, `title`, `description`, and `data` fields.
2. THE `activityType` field SHALL use one of the valid values: introAudio, viewFlashcards, speakFlashcards, vocabLevel1, reading, speakReading, readAlong, writingSentence.
3. All content data SHALL be inside the `data` object, not inline on the activity object.
4. WHEN a writingSentence activity is created, THE activity SHALL have `data.vocabList`, `data.items` (non-empty array), and each item SHALL have `prompt` and `targetVocab` fields.
5. THE Curriculum_Creator SHALL follow the activity title/description conventions:
   - viewFlashcards/speakFlashcards/vocabLevel1: title = "Flashcards: <topic>", description = "Học N từ: word1, word2, ..."
   - reading/speakReading: title = "Đọc: <topic>", description = first ~80 chars of the reading text
   - readAlong: title = "Nghe: <topic>", description = "Nghe đoạn văn vừa đọc và theo dõi."
   - introAudio: title = descriptive label (e.g. "Giới thiệu bài học", "Tổng kết bài học"), description = brief summary
   - writingSentence: title = "Viết: <topic>", description = brief summary of the writing task
6. THE learning session object SHALL have a `title` field (e.g. "Khám phá Kinh Tế Số").

### Requirement 5: Reading Passage Content

**User Story:** As a content quality owner, I want the reading passage to be engaging, relevant to Vietnamese learners, and appropriate for preintermediate level, so that users get a satisfying reading experience in their first session.

#### Acceptance Criteria

1. THE reading passage SHALL be expository in style — explaining digital economy concepts in a way that connects to Vietnamese daily life (Grab, Shopee, MoMo, VNPay, etc.).
2. THE reading passage SHALL be 60-70 words in English with vocabulary and grammar appropriate for preintermediate level (average 10-14 words per sentence).
3. THE reading passage SHALL incorporate all vocabulary words from the curriculum naturally.
4. THE reading passage SHALL present the digital economy topic in a way that feels relevant and exciting to Vietnamese professionals and students.

### Requirement 6: Marketing Copy and Preview Text

**User Story:** As a content quality owner, I want marketing text that excites Vietnamese users about learning digital economy English, so that they feel motivated to try the onboarding lesson.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL write the curriculum description as Persuasive_Copy following the 5-beat structure, connecting English learning to career advancement in Vietnam's booming digital economy.
2. THE Curriculum_Creator SHALL write the curriculum preview (~150 words) with vivid hooks about the learner's career in the digital age, vocabulary word listing, and what the learner will be able to discuss in English after completing the lesson.
3. THE Curriculum_Creator SHALL write the title, description, and preview text primarily in Vietnamese (as required for preintermediate vi-en curriculums).
4. THE description headline SHALL use one of the 6 Tone_Palette types (recommended: `surprising_fact` or `provocative_question` for digital economy relevance).
5. THE curriculum title SHALL be minimal — no difficulty level, no series name, no content type prefix. Example: "Kinh Tế Số" or "Thời Đại Số".

### Requirement 7: introAudio Quality Standards

**User Story:** As a content quality owner, I want introAudio scripts that are energetic, modern, and educational, so that learners feel guided through both language learning and digital economy exploration.

#### Acceptance Criteria

1. WHEN the welcome introAudio is created, THE script (500-800 words) SHALL greet the learner warmly, introduce the digital economy topic with a hook connecting to the learner's daily life (ordering on Shopee, paying with MoMo, using Grab), list all vocabulary words, and teach each word with: the English word, Vietnamese meaning, a contextual example sentence, and an explanation of how the word connects to the digital economy.
2. WHEN the farewell introAudio is created (400-600 words), THE script SHALL review all 5 vocabulary words with definitions and fresh example sentences, connect the words back to the digital economy theme, congratulate the learner on completing their first lesson, and encourage them to explore more curriculums.
3. THE introAudio scripts SHALL be bilingual — Vietnamese explanations for English vocabulary and concepts.
4. THE Curriculum_Creator SHALL individually craft every introAudio script for this specific curriculum topic, without using template functions or string interpolation.
5. THE farewell introAudio SHALL use the `practical_momentum` farewell register — action-oriented, giving the learner a sense of what they can do next with their new vocabulary.

### Requirement 8: Pricing

**User Story:** As a platform owner, I want this onboarding curriculum to be free, so that new users can try the app without any barrier.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL NOT call `curriculum/setPrice` for this curriculum (default is free/0 credits), OR SHALL call it with `price: 0`.
2. THE pricing follows the guideline: "onboarding/trial curriculums" are in the Free tier (0 credits).

### Requirement 9: Privacy — No Public Publishing

**User Story:** As a platform owner, I want this newly created curriculum to remain private until content generation is complete, so that learners don't encounter incomplete content.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL NOT call `curriculum/setPublic` with `isPublic: true` on the newly created Onboarding_Curriculum.

### Requirement 10: Content Validation

**User Story:** As a platform developer, I want the curriculum validated before upload, so that no corrupted content enters the database.

#### Acceptance Criteria

1. THE Content_Validator SHALL verify that the curriculum content JSON has non-null, non-empty `title`, `description`, and `preview.text` fields.
2. THE Content_Validator SHALL verify that `learningSessions` is a non-empty array with exactly 1 session, having a non-empty `title` and `activities` array.
3. THE Content_Validator SHALL verify that every activity has `activityType` (not `type`), `title`, `description`, and `data` fields, with content fields inside `data`.
4. THE Content_Validator SHALL verify that `activityType` values are valid.
5. THE Content_Validator SHALL verify that vocabList fields contain arrays of lowercase strings using the field name `vocabList`.
6. THE Content_Validator SHALL verify that viewFlashcards and speakFlashcards in the same session have identical vocabList arrays.
7. THE Content_Validator SHALL verify writingSentence data structures (vocabList, items with prompt and targetVocab).
8. THE Content_Validator SHALL verify that no Strip_Keys appear anywhere in the content JSON.
9. THE Content_Validator SHALL verify that `contentTypeTags` is `[]`.
10. IF any validation check fails, THEN THE Content_Validator SHALL abort the upload and print the specific rule violation.

### Requirement 11: Script Architecture and Workflow

**User Story:** As a developer, I want a clear, simple workflow for creating this single onboarding curriculum, so that the process is straightforward and traceable.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL produce one standalone Python script for the curriculum (e.g. `create_digital_economy_onboarding.py`).
2. THE Curriculum_Creator SHALL organize the script into a directory `digital-economy-onboarding-curriculum/`.
3. THE Curriculum_Creator SHALL authenticate all API calls using `firebase_token.get_firebase_id_token` with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`.
4. THE Curriculum_Creator SHALL use `https://helloapi.step.is` as the API base URL.
5. THE Curriculum_Creator SHALL individually craft every piece of learner-facing text for this specific curriculum topic, without using template functions, string interpolation, or generic fill-in-the-blank patterns.
6. IF the curriculum creation API call fails, THEN THE Curriculum_Creator SHALL log the error with details and exit.

### Requirement 12: Documentation and Cleanup

**User Story:** As a developer, I want proper documentation after the curriculum is created, so that the content is traceable and reproducible.

#### Acceptance Criteria

1. WHEN the curriculum is created and verified, THE Curriculum_Creator SHALL create a README.md documenting: curriculum ID, title, vocabulary list, pricing, and SQL verification queries.
2. WHEN the curriculum is verified in the database, THE source Python script SHALL be deleted, leaving only the README.
3. THE Curriculum_Creator SHALL run a duplicate check query for the curriculum title after creation and resolve any duplicates (keep earliest, delete extras).

### Requirement 13: Curriculum Title

**User Story:** As a content quality owner, I want the curriculum title to be minimal and in Vietnamese, so that it works well as a standalone onboarding lesson.

#### Acceptance Criteria

1. THE curriculum title SHALL be minimal — no difficulty level, no series name, no content type prefix, no audience suffix.
2. THE curriculum title SHALL be in Vietnamese.
3. THE curriculum title SHALL NOT include difficulty level indicators (e.g., "preintermediate", "sơ trung cấp").
4. THE curriculum title SHALL be evocative and modern — using language that resonates with Vietnamese professionals interested in the digital economy.
