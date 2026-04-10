# Requirements Document

## Introduction

Expand the vi-en (Vietnamese learners studying English) curriculum catalog by 100 new curriculums. The current catalog has 153 curriculums with significant gaps: beginner level is severely underrepresented (7 out of 153), `writing_focus` skillFocusTags is completely missing, `vocab_acquisition` is nearly nonexistent (1), `speaking_focus` is underrepresented (11), music and movie content types are sparse, and there are no podcast or story curriculums at several difficulty levels. Topic coverage is also skewed toward science/tech, economics, and health, with many everyday and cultural domains untouched.

This spec defines the distribution, topic selection, structural requirements, and quality standards for 100 new curriculums that fill these gaps across difficulty levels, skillFocusTags, contentTypeTags, and topics. Each curriculum is created via a standalone Python script calling the helloapi REST API, organized into new and existing series/collections.

### What This Spec Covers

- Distribution plan for 100 new curriculums across difficulty levels, skill focus types, content types, and topics
- New topic areas not currently covered in the catalog
- Series and collection organization for the new curriculums
- Structural and quality requirements for each curriculum type
- Creation workflow, verification, and documentation

### What This Spec Does NOT Cover

- Changes to existing 153 curriculums
- Client-side UI changes
- Content generation pipeline (audio, illustrations) — curriculums are created private and go through the pipeline separately
- Other language pairs (en-en, vi-zh, en-zh, etc.)

## Glossary

- **Catalog**: The full set of vi-en curriculums in the platform database (currently 153, target 253 after this expansion).
- **Collection**: A top-level organizational container that holds one or more Series. Stored in `curriculum_collections`.
- **Series**: A thematic grouping of Curriculums within a Collection. Has a title, description (≤ 255 chars), and display order. Stored in `curriculum_series`.
- **Curriculum**: A single learning unit containing a title, preview, description, and learning sessions with ordered activities. Stored in `curriculum` with content as JSONB.
- **Learning_Session**: An ordered group of activities within a Curriculum.
- **Activity**: A single learning step within a session (e.g., introAudio, viewFlashcards, reading, writingSentence).
- **Platform**: The language-learning application at helloapi.step.is.
- **Balanced_Skills**: Curriculum type distributing time across reading, listening, speaking, and writing. Uses 18 words across 3 learning sessions + review + final reading.
- **Writing_Focus**: Curriculum type where writing is the centerpiece. Drops speakFlashcards, speakReading, vocabLevel3. Uses 10 words across 2 sessions with escalating writing prompts.
- **Speaking_Focus**: Curriculum type emphasizing speaking practice with additional speakReading activities and pronunciation-focused introAudio.
- **Vocab_Acquisition**: Curriculum type focused on rapid vocabulary building with extra vocab drill levels and spaced repetition across sessions.
- **Reader**: Curriculum type for extensive reading practice. Content is mostly comprehensible at the target level; vocabulary words are familiar refreshers, not new learning targets.
- **Persuasive_Copy**: The multi-paragraph Vietnamese marketing text style required for curriculum descriptions, following the 5-beat structure.
- **Tone_Palette**: The six rhetorical opener types: provocative_question, bold_declaration, vivid_scenario, empathetic_observation, surprising_fact, metaphor_led.
- **contentTypeTags**: JSON array field on curriculum content: `["movie"]`, `["music"]`, `["podcast"]`, `["story"]`, or `[]`.
- **difficultyTags**: Difficulty level metadata: beginner, preintermediate, intermediate, upperintermediate, advanced.
- **Creation_Script**: A standalone Python script that calls the helloapi REST API to create a curriculum.
- **Strip_Keys**: Auto-generated platform keys that must never appear in new content.

## Requirements

### Requirement 1: Distribution Across Difficulty Levels

**User Story:** As a content manager, I want the 100 new curriculums distributed to address the current level imbalance, so that learners at every proficiency level have adequate content choices.

#### Acceptance Criteria

1. THE Catalog expansion SHALL include at minimum 20 beginner-level curriculums, bringing the beginner total from 7 to at least 27.
2. THE Catalog expansion SHALL include at minimum 20 preintermediate-level curriculums.
3. THE Catalog expansion SHALL include at minimum 20 intermediate-level curriculums.
4. THE Catalog expansion SHALL include at minimum 15 upperintermediate-level curriculums.
5. THE Catalog expansion SHALL include at minimum 15 advanced-level curriculums.
6. THE Catalog expansion SHALL produce exactly 100 new curriculums in total across all difficulty levels.

### Requirement 2: Distribution Across Skill Focus Types

**User Story:** As a content manager, I want the 100 new curriculums to fill gaps in skill focus coverage, so that learners can choose curriculums optimized for their specific learning goals (writing, speaking, vocabulary building, reading, or balanced practice).

#### Acceptance Criteria

1. THE Catalog expansion SHALL include at minimum 15 curriculums with `writing_focus` skillFocusTags, introducing this previously missing type to the vi-en catalog.
2. THE Catalog expansion SHALL include at minimum 12 curriculums with `vocab_acquisition` skillFocusTags, expanding from the current 1.
3. THE Catalog expansion SHALL include at minimum 12 curriculums with `speaking_focus` skillFocusTags, expanding from the current 11.
4. THE Catalog expansion SHALL include at minimum 10 curriculums with `reader` skillFocusTags.
5. THE remaining curriculums SHALL use `balanced_skills` skillFocusTags.
6. Each skillFocusTags type SHALL appear across at least 3 different difficulty levels.

### Requirement 3: Distribution Across Content Types

**User Story:** As a content manager, I want the 100 new curriculums to expand content type variety, so that learners can study English through movies, music, podcasts, and stories in addition to topic-based content.

#### Acceptance Criteria

1. THE Catalog expansion SHALL include at minimum 8 curriculums with `["movie"]` contentTypeTags, covering movies not already in the catalog.
2. THE Catalog expansion SHALL include at minimum 8 curriculums with `["music"]` contentTypeTags, covering songs not already in the catalog.
3. THE Catalog expansion SHALL include at minimum 8 curriculums with `["podcast"]` contentTypeTags, including at least 2 at beginner level and 2 at preintermediate level (currently zero at these levels).
4. THE Catalog expansion SHALL include at minimum 8 curriculums with `["story"]` contentTypeTags, including at least 3 at upperintermediate or advanced level (currently near-zero at these levels).
5. THE remaining curriculums SHALL use `[]` (general/topic-based) contentTypeTags.
6. WHEN a movie-based curriculum is created, THE reading passages SHALL be adapted from or inspired by the movie's themes, dialogue, and cultural context — not a plot summary.
7. WHEN a music-based curriculum is created, THE reading passages SHALL explore the song's lyrics, themes, cultural significance, and the artist's message.
8. WHEN a podcast-based curriculum is created, THE reading passages SHALL be adapted from or inspired by the podcast episode's content and key ideas.
9. WHEN a story-based curriculum is created, THE reading passages SHALL follow the Reader curriculum rules: content is mostly comprehensible at the target level, vocabulary words are familiar refreshers.

### Requirement 4: New Topic Areas

**User Story:** As a content manager, I want the 100 new curriculums to cover topics not already saturated in the catalog, so that learners have fresh, diverse content rather than more of the same science/tech/economics themes.

#### Acceptance Criteria

1. THE Catalog expansion SHALL introduce curriculums in the following underrepresented or missing topic areas:
   - Daily life and practical English (shopping, cooking, housing, transportation, banking)
   - Relationships and social skills (friendship, conflict resolution, dating, family dynamics)
   - Arts and creativity (painting, photography, design, architecture, fashion)
   - Sports and fitness (specific sports, Olympic history, extreme sports, team dynamics)
   - History and civilization (ancient civilizations, world wars, revolutions, historical figures)
   - Law and justice (legal systems, human rights, crime and punishment, ethics)
   - Food and gastronomy (world cuisines, food science, restaurant culture, food sustainability)
   - Psychology and emotions (emotional intelligence, cognitive biases, motivation, stress management)
   - Technology and digital life (social media impact, cybersecurity, digital privacy, AI ethics)
   - Vietnamese culture in English (Vietnamese festivals, cuisine, history, traditions explained in English)
2. THE Catalog expansion SHALL NOT create more than 5 curriculums in any single topic area already well-covered (science/tech, economics/finance, health/wellness, environment).
3. Each new topic area listed in criterion 1 SHALL have at minimum 3 curriculums across different difficulty levels.
4. THE Catalog expansion SHALL ensure no two curriculums within the same series have substantially overlapping vocabulary lists.

### Requirement 5: Beginner-Level Curriculum Structure

**User Story:** As a content manager, I want beginner-level curriculums to use simpler structures with more scaffolding, so that absolute beginners are not overwhelmed by complex activity sequences.

#### Acceptance Criteria

1. WHEN a beginner-level balanced_skills curriculum is created, THE Curriculum SHALL contain 12 vocabulary words divided into 2 groups of 6 (not 18 words across 3 sessions).
2. WHEN a beginner-level curriculum is created, THE Curriculum SHALL have 4 sessions: 2 learning sessions, 1 review session, and 1 final reading session.
3. WHEN a beginner-level curriculum is created, THE reading passages SHALL use simple sentences (under 15 words average), present tense primarily, and high-frequency vocabulary beyond the target words.
4. WHEN a beginner-level curriculum is created, THE introAudio scripts SHALL be fully bilingual with Vietnamese explanations for every English concept.
5. WHEN a beginner-level curriculum is created, THE writingSentence prompts SHALL provide heavy scaffolding: full Vietnamese instructions, a complete English example sentence, and a clear pattern for the learner to follow.
6. WHEN a beginner-level curriculum is created, THE Curriculum SHALL NOT include `writingParagraph` activities (too advanced for beginners).
7. WHEN a beginner-level curriculum is created, THE Curriculum SHALL NOT include `vocabLevel3` activities (to reduce cognitive load).

### Requirement 6: Preintermediate-to-Intermediate Curriculum Structure

**User Story:** As a content manager, I want preintermediate and intermediate curriculums to follow the established 18-word, 5-session structure, so that they are consistent with the existing catalog.

#### Acceptance Criteria

1. WHEN a preintermediate or intermediate balanced_skills curriculum is created, THE Curriculum SHALL contain 18 vocabulary words divided into 3 groups of 6.
2. WHEN a preintermediate or intermediate balanced_skills curriculum is created, THE Curriculum SHALL have 5 sessions: 3 learning sessions, 1 review session, and 1 final reading session.
3. Each learning session SHALL include activities in order: introAudio, introAudio (vocab teaching), viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, introAudio (grammar/usage), reading, speakReading, readAlong, writingSentence.
4. THE review session SHALL include: introAudio (review intro), viewFlashcards (all 18 words), speakFlashcards (all 18 words), vocabLevel1, vocabLevel2, writingSentence.
5. THE final reading session SHALL include: introAudio (full reading intro), reading (full article), speakReading, readAlong, writingParagraph, introAudio (farewell).
6. All user-facing text SHALL be bilingual (Vietnamese instructions, English reading passages).

### Requirement 7: Upper-Intermediate and Advanced Curriculum Structure

**User Story:** As a content manager, I want upper-intermediate and advanced curriculums to challenge learners with longer passages, more complex vocabulary, and less scaffolding, so that they build toward real-world English fluency.

#### Acceptance Criteria

1. WHEN an upperintermediate or advanced balanced_skills curriculum is created, THE Curriculum SHALL contain 18 vocabulary words divided into 3 groups of 6.
2. WHEN an upperintermediate curriculum is created, THE Curriculum MAY use bilingual or single-language content, per the platform language policy.
3. WHEN an advanced curriculum is created, THE Curriculum SHALL use single-language (English-only) content for all user-facing text.
4. WHEN an advanced curriculum is created, THE reading passages SHALL use complex sentence structures, academic vocabulary, and domain-specific terminology appropriate for advanced learners.
5. WHEN an upperintermediate or advanced curriculum is created, THE writingParagraph prompts SHALL require analytical or argumentative responses (not simple summaries).

### Requirement 8: Writing_Focus Curriculum Structure

**User Story:** As a content manager, I want writing_focus curriculums to follow the established writing_focus structure, so that the new writing-centric curriculums are consistent with the platform's writing_focus type definition.

#### Acceptance Criteria

1. THE Writing_Focus curriculum SHALL contain 10 vocabulary words divided into 2 groups of 5.
2. THE Writing_Focus curriculum SHALL have 4 sessions with escalating writing demands.
3. THE Writing_Focus curriculum SHALL NOT include speakFlashcards, speakReading, or vocabLevel3 activities.
4. THE Writing_Focus curriculum SHALL include writingParagraph in every session of the single-language variant and in sessions 3-4 of the bilingual variant.
5. THE Writing_Focus curriculum SHALL include writingSentence in sessions 1-3 of the bilingual variant.
6. WHEN a bilingual writing_focus curriculum is created, THE writing prompts SHALL be in Vietnamese with English example sentences and responses.

### Requirement 9: Speaking_Focus Curriculum Structure

**User Story:** As a content manager, I want speaking_focus curriculums to emphasize pronunciation and oral fluency, so that learners who prioritize speaking get targeted practice.

#### Acceptance Criteria

1. THE Speaking_Focus curriculum SHALL contain 18 vocabulary words divided into 3 groups of 6.
2. THE Speaking_Focus curriculum SHALL include speakFlashcards and speakReading in every learning session.
3. THE Speaking_Focus curriculum SHALL include additional pronunciation-focused introAudio segments explaining common pronunciation challenges for Vietnamese speakers.
4. THE Speaking_Focus curriculum SHALL NOT include writingParagraph activities (writing is not the focus).
5. THE Speaking_Focus curriculum SHALL include writingSentence only in the final session as a light reinforcement activity.

### Requirement 10: Vocab_Acquisition Curriculum Structure

**User Story:** As a content manager, I want vocab_acquisition curriculums to maximize vocabulary throughput with intensive drill, so that learners focused on building word count get the most efficient practice.

#### Acceptance Criteria

1. THE Vocab_Acquisition curriculum SHALL contain 24 vocabulary words divided into 4 groups of 6.
2. THE Vocab_Acquisition curriculum SHALL have 6 sessions: 4 learning sessions, 1 review session, and 1 final reading session.
3. Each learning session SHALL include viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, and vocabLevel3 for intensive drill.
4. THE Vocab_Acquisition curriculum SHALL include shorter reading passages focused on using all 6 session words in context, prioritizing vocabulary exposure over extended reading.
5. THE Vocab_Acquisition curriculum SHALL NOT include writingParagraph activities (focus is on recognition and recall, not composition).

### Requirement 11: Reader Curriculum Structure

**User Story:** As a content manager, I want reader curriculums to provide extensive reading practice with comprehensible input, so that learners build fluency and confidence through volume of reading.

#### Acceptance Criteria

1. THE Reader curriculum SHALL follow the story-oriented rules: content is mostly comprehensible at the target level, vocabulary words are familiar refreshers.
2. THE Reader curriculum SHALL contain 12-18 vocabulary words that the learner has likely encountered before at or below their level.
3. THE Reader curriculum SHALL include longer reading passages than balanced_skills curriculums, with the full article in the final session being at least 500 words.
4. THE Reader curriculum SHALL prioritize readAlong activities in every session for listening-while-reading practice.
5. WHEN a reader curriculum uses `["story"]` contentTypeTags, THE reading passages SHALL tell a cohesive narrative across sessions.

### Requirement 12: Content Quality — Persuasive Copy

**User Story:** As a content manager, I want all 100 new curriculums to meet the platform's persuasive copy standards, so that learners feel emotionally engaged and motivated.

#### Acceptance Criteria

1. Each Curriculum description SHALL follow the 5-beat Persuasive_Copy structure: ALL-CAPS headline, concrete examples, vivid metaphor, transformation promise, and learning tie-in.
2. Each Curriculum description SHALL use a tone from the Tone_Palette for its headline opener.
3. WITHIN a Series, no two adjacent Curriculum descriptions SHALL use the same tone.
4. No single tone SHALL exceed 30% of all Curriculum descriptions within a Series.
5. Each Curriculum preview (~150 words) SHALL open with a vivid hook, name the vocabulary words, and describe the learning journey.
6. THE Persuasive_Copy SHALL reference topic-specific pain points and aspirations relevant to Vietnamese learners.

### Requirement 13: introAudio Quality Standards

**User Story:** As a content manager, I want introAudio scripts to be individually crafted for each curriculum's topic, so that learners receive rich, contextual vocabulary teaching rather than generic templates.

#### Acceptance Criteria

1. WHEN a Session 1 introAudio is created, THE script SHALL welcome the learner, set the scene with vivid context related to the topic, and list all vocabulary words for the session.
2. WHEN a vocabulary-teaching introAudio is created, THE script SHALL teach each word individually with: part of speech, full definition, example sentence from the reading context, and explanation of how the word appears in the article.
3. WHEN a Session 2+ introAudio is created, THE script SHALL recap previous session words before introducing new ones.
4. WHEN a review session introAudio is created, THE script SHALL congratulate the learner, briefly recap all previous sessions, and explain the review format.
5. WHEN a farewell introAudio is created, THE script (400-600 words) SHALL review 5-6 key vocabulary words with definitions and fresh example sentences, summarize the learning journey, and close with a warm sign-off.
6. WITHIN a Series, farewell scripts SHALL vary in emotional register using different farewell tones (introspective guide, warm accountability, team-building energy, quiet awe, practical momentum).
7. No two adjacent Curriculums in a Series SHALL use the same farewell tone.

### Requirement 14: Writing Activity Quality Standards

**User Story:** As a content manager, I want writingSentence and writingParagraph activities to have detailed, topic-specific prompts, so that learners produce meaningful writing rather than filling in blanks.

#### Acceptance Criteria

1. WHEN a writingSentence activity is created, THE Activity SHALL include items with: a `targetVocab` field, a detailed `prompt` specifying context for using the word, and an example sentence showing correct usage.
2. WHEN a bilingual writingSentence is created, THE prompt SHALL be in Vietnamese with the example sentence in English.
3. WHEN a writingParagraph activity is created, THE Activity SHALL include: a `vocabList` of words to use, `instructions` describing the writing task, and `prompts` (array of at least 2 strings) providing specific guiding questions.
4. THE writingParagraph prompts SHALL reference specific concepts from the curriculum's reading passages.

### Requirement 15: Activity Schema Compliance

**User Story:** As a content manager, I want all activities to comply with the platform's content schema, so that the client app renders them correctly without errors.

#### Acceptance Criteria

1. Each Activity SHALL include `activityType`, `title`, `description`, and `data` fields.
2. THE `activityType` field SHALL use one of the valid values: introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, vocabLevel3, reading, speakReading, readAlong, writingSentence, writingParagraph.
3. WHEN a viewFlashcards or speakFlashcards activity is created for the same session, THE two activities SHALL have identical `vocabList` arrays.
4. THE `vocabList` field SHALL be an array of lowercase strings — never objects, numbers, or the field name `words`.
5. All content data SHALL be inside the `data` object — never inline on the activity object.
6. THE Curriculum content SHALL NOT include any Strip_Keys: mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId.
7. THE Curriculum content SHALL include `contentTypeTags` as a top-level field.

### Requirement 16: Series and Collection Organization

**User Story:** As a content manager, I want the 100 new curriculums organized into logical series and collections, so that learners can browse and discover content by theme.

#### Acceptance Criteria

1. THE 100 new curriculums SHALL be organized into series, with each series containing 3-5 curriculums of related topics.
2. Each Series SHALL have a Vietnamese title and a description of 255 characters or fewer using a tone from the Tone_Palette.
3. No two adjacent Series within the same Collection SHALL use the same description tone.
4. Each Series SHALL contain curriculums within a maximum 1-level difficulty gap (e.g., beginner + preintermediate is OK, beginner + intermediate is not).
5. Each Series SHALL contain curriculums with homogeneous `language` and `userLanguage` values.
6. Series SHALL be added to existing or new Collections as appropriate for the topic area.
7. WHEN a new Collection is created, THE Collection SHALL have a neutral, informative description (not persuasive copy).

### Requirement 17: Display Order

**User Story:** As a content manager, I want all new series and curriculums to have explicit display orders, so that content appears in the intended sequence in the client app.

#### Acceptance Criteria

1. WHEN a curriculum is added to a series, THE Creation_Script SHALL call `curriculum/setDisplayOrder` to assign a sequential integer display order.
2. WHEN a series is added to a collection, THE Creation_Script SHALL call `curriculum-series/setDisplayOrder` to assign a display order.
3. THE display order SHALL be determined by querying existing curriculums in the series to find the next appropriate value.

### Requirement 18: Creation Workflow

**User Story:** As a content manager, I want each curriculum created via a separate Python script with no templated content, so that every piece of learner-facing text is individually crafted.

#### Acceptance Criteria

1. Each Curriculum SHALL be created via a separate standalone Python script.
2. Each script SHALL use `firebase_token.get_firebase_id_token()` for authentication and the `curriculum/create` API endpoint.
3. THE `curriculum/create` call SHALL include `language` and `userLanguage` as top-level body parameters (not only inside content JSON).
4. THE Creation_Script SHALL NOT use template functions, string interpolation, or loops to generate learner-facing text (introAudio, descriptions, previews, reading passages, writing prompts).
5. THE Creation_Script MAY use shared helper functions for activity structure (types, order, data schema).
6. Newly created curriculums SHALL remain private (no call to `setPublic` with `isPublic: true`).

### Requirement 19: Post-Creation Verification

**User Story:** As a content manager, I want each curriculum verified against content corruption rules after creation, so that no malformed content reaches the platform.

#### Acceptance Criteria

1. WHEN a curriculum is created, THE Creation_Script SHALL verify the response contains a valid curriculum ID.
2. WHEN a curriculum is created, THE Creation_Script SHALL check for duplicates by querying: `SELECT id, title, created_at FROM curriculum WHERE title = '<title>' AND uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73' ORDER BY created_at`.
3. IF duplicates are found, THE Creation_Script SHALL keep the earliest and delete extras.
4. THE Creation_Script SHALL verify the created content against corruption rules: correct `activityType` field names, `vocabList` not `words`, data inside `data` object, matching vocabLists for viewFlashcards/speakFlashcards in the same session.

### Requirement 20: Documentation and Cleanup

**User Story:** As a content manager, I want proper documentation after all curriculums are created, so that the content is traceable and reproducible.

#### Acceptance Criteria

1. WHEN all curriculums in a series are created, THE workspace SHALL contain a README.md documenting: collection ID, series ID, all curriculum IDs and titles, creation method, SQL queries for retrieval, and recreation context.
2. WHEN all curriculums are verified in the database, THE source Python scripts SHALL be deleted from the workspace, leaving only the README.
3. THE README SHALL include the distribution summary: how many curriculums at each difficulty level, skill focus, and content type.

### Requirement 21: Batch Organization by Implementation Priority

**User Story:** As a content manager, I want the 100 curriculums organized into implementation batches, so that the highest-gap areas are filled first and progress can be tracked.

#### Acceptance Criteria

1. THE implementation SHALL be organized into batches, with each batch containing 10-15 curriculums.
2. Batch 1 SHALL prioritize beginner-level curriculums (the largest gap) across multiple topic areas.
3. Batch 2 SHALL prioritize writing_focus and vocab_acquisition curriculums (completely missing or near-missing types).
4. Batch 3 SHALL prioritize movie, music, and podcast content types at underrepresented difficulty levels.
5. Subsequent batches SHALL fill remaining gaps in topic diversity and skill focus distribution.
6. Each batch SHALL be independently verifiable — all curriculums in a batch are created, verified, and documented before the next batch begins.
