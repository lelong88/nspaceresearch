# Requirements Document

## Introduction

This feature brings 6 bilingual language pairs to parity with vi-en (the reference bilingual pair) at beginner, preintermediate, and intermediate difficulty levels. The reference pair vi-en (userLanguage=vi, language=en) has 60 beginner, 59 preintermediate, and 63 intermediate public curriculums. Each target pair has significant gaps that must be filled with new curriculums.

### Target Pairs and Gap Analysis

| Pair | userLanguage | language (target) | Beginner Gap | Preintermediate Gap | Intermediate Gap | Total Gap |
|------|-------------|-------------------|-------------|---------------------|------------------|-----------|
| vi-zh | vi | zh | 31 | 22 | 26 | 79 |
| en-zh | en | zh | 60 | 23 | 28 | 111 |
| en-de | en | de | 59 | 52 | 38 | 149 |
| vi-de | vi | de | 60 | 56 | 39 | 155 |
| en-fr | en | fr | 58 | 51 | 29 | 138 |
| vi-fr | vi | fr | 60 | 55 | 26 | 141 |
| **Total** | | | **328** | **259** | **186** | **~773** |

### What This Spec Covers

- Creation of ~773 new curriculums across 6 bilingual language pairs
- Three difficulty levels: beginner, preintermediate, intermediate
- Collection and series infrastructure for organizing new curriculums
- Content validation, verification, and documentation workflow
- Reuse of existing shared modules (validate_content.py, api_helpers.py)

### What This Spec Does NOT Cover

- Single-language pairs (en-en, de-de, fr-fr, zh-zh) — explicitly out of scope
- Changes to existing curriculums
- Upper-intermediate or advanced difficulty levels
- Client-side UI changes
- Content generation pipeline (audio, illustrations)
- The ~460 curriculums already created by the multilingual-curriculum-expansion spec (vi-fr, vi-de, en-fr, en-de, fr-fr, de-de)

## Glossary

- **Reference_Pair**: The vi-en language pair (userLanguage=vi, language=en), which serves as the benchmark for curriculum count parity at each difficulty level
- **Parity**: Having at least as many public curriculums as the Reference_Pair at a given difficulty level
- **Curriculum**: A structured learning unit containing sessions with ordered activities (introAudio, flashcards, vocab drills, reading, writing)
- **Beginner_Curriculum**: A curriculum with difficultyTags ["beginner"], 12 vocabulary words in 2 groups of 6, 4 sessions (2 learning + 1 review + 1 final), no writingParagraph, no vocabLevel3
- **Standard_Curriculum**: A curriculum at preintermediate or intermediate level with 18 vocabulary words in 3 groups of 6, 5 sessions (3 learning + 1 review + 1 final), full activity set including writingParagraph and vocabLevel3
- **Collection**: A top-level organizational container that holds Series
- **Series**: A group of related curriculums within a Collection, with homogeneous language pair and max 1 difficulty level gap between members
- **Tone_Palette**: The 6 rhetorical opener types used for description variety: provocative_question, bold_declaration, vivid_scenario, empathetic_observation, surprising_fact, metaphor_led
- **Farewell_Palette**: The 5 emotional registers for farewell introAudio scripts: introspective_guide, warm_accountability, team_building_energy, quiet_awe, practical_momentum
- **User_Language**: The learner's native language — the **first** code in a pair. For `vi-zh`, User_Language is `vi` (Vietnamese). Maps to `userLanguage` in the API.
- **Target_Language**: The language being learned — the **second** code in a pair. For `vi-zh`, Target_Language is `zh` (Chinese). Maps to `language` in the API.
- **Validator**: The validate_content.py module that checks curriculum JSON structure before upload
- **API_Helper**: The api_helpers.py module that wraps REST API calls to helloapi.step.is
- **Orchestrator**: A per-language-pair Python script that creates collections, series, and wires the hierarchy
- **Display_Order**: An integer that determines the sort position of a curriculum within a series, or a series within a collection

## Requirements

### Requirement 1: Language Pair Coverage

**User Story:** As a platform operator, I want all 6 bilingual pairs brought to parity with vi-en, so that learners across all supported bilingual combinations have equivalent content depth.

#### Acceptance Criteria

1. WHEN the expansion is complete, THE System SHALL have created new curriculums for vi-zh such that the total public curriculum count at beginner, preintermediate, and intermediate levels each meets or exceeds the Reference_Pair counts
2. WHEN the expansion is complete, THE System SHALL have created new curriculums for en-zh such that the total public curriculum count at beginner, preintermediate, and intermediate levels each meets or exceeds the Reference_Pair counts
3. WHEN the expansion is complete, THE System SHALL have created new curriculums for en-de such that the total public curriculum count at beginner, preintermediate, and intermediate levels each meets or exceeds the Reference_Pair counts
4. WHEN the expansion is complete, THE System SHALL have created new curriculums for vi-de such that the total public curriculum count at beginner, preintermediate, and intermediate levels each meets or exceeds the Reference_Pair counts
5. WHEN the expansion is complete, THE System SHALL have created new curriculums for en-fr such that the total public curriculum count at beginner, preintermediate, and intermediate levels each meets or exceeds the Reference_Pair counts
6. WHEN the expansion is complete, THE System SHALL have created new curriculums for vi-fr such that the total public curriculum count at beginner, preintermediate, and intermediate levels each meets or exceeds the Reference_Pair counts
7. THE System SHALL create approximately 773 new curriculums in total across all 6 pairs and 3 difficulty levels

### Requirement 2: Beginner Curriculum Structure

**User Story:** As a beginner learner, I want curriculums designed for my level with simpler structure and fewer words, so that I can learn without being overwhelmed.

#### Acceptance Criteria

1. THE Beginner_Curriculum SHALL contain exactly 12 vocabulary words organized into 2 groups of 6
2. THE Beginner_Curriculum SHALL contain exactly 4 sessions: 2 learning sessions, 1 review session, and 1 final reading session
3. THE Beginner_Curriculum SHALL include difficultyTags set to ["beginner"] in the content JSON
4. THE Beginner_Curriculum SHALL exclude writingParagraph activities from all sessions
5. THE Beginner_Curriculum SHALL exclude vocabLevel3 activities from all sessions
6. WHEN a Beginner_Curriculum learning session is created, THE System SHALL include the following activities in order: introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence
7. THE Beginner_Curriculum SHALL use simple reading passages with average sentence length under 15 words

### Requirement 3: Standard Curriculum Structure (Preintermediate and Intermediate)

**User Story:** As a preintermediate or intermediate learner, I want curriculums with the full activity set and more vocabulary, so that I can build deeper language skills.

#### Acceptance Criteria

1. THE Standard_Curriculum SHALL contain exactly 18 vocabulary words organized into 3 groups of 6
2. THE Standard_Curriculum SHALL contain exactly 5 sessions: 3 learning sessions, 1 review session, and 1 final reading session
3. THE Standard_Curriculum SHALL include difficultyTags set to ["preintermediate"] or ["intermediate"] in the content JSON
4. WHEN a Standard_Curriculum learning session is created, THE System SHALL include the following activities in order: introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, vocabLevel3, reading, speakReading, readAlong, writingSentence
5. THE Standard_Curriculum final session SHALL include a writingParagraph activity

### Requirement 4: Bilingual Content Language Rules

**User Story:** As a bilingual learner, I want user-facing text in my native language and reading passages in my target language, so that I can understand the curriculum context while practicing the language I am learning.

#### Acceptance Criteria

1. THE Curriculum SHALL have its title written in the User_Language
2. THE Curriculum SHALL have its description written in the User_Language
3. THE Curriculum SHALL have its preview.text written in the User_Language
4. THE Curriculum SHALL have its introAudio text written in the User_Language
5. THE Curriculum SHALL have its reading passages written in the Target_Language
6. THE Curriculum SHALL have its writingSentence prompts written in the User_Language with target vocabulary from the Target_Language
7. THE Curriculum SHALL have its writingParagraph prompts written in the User_Language referencing Target_Language vocabulary
8. WHEN a curriculum is created via the API, THE System SHALL pass the Target_Language as the `language` parameter and the User_Language as the `userLanguage` parameter as top-level body fields

### Requirement 5: Activity Schema Compliance

**User Story:** As a platform operator, I want all curriculum content to follow the established activity schema, so that the client app can render activities correctly.

#### Acceptance Criteria

1. THE Curriculum SHALL have a non-null, non-empty title, description, and preview.text at the top level
2. THE Curriculum SHALL include a contentTypeTags field at the top level set to one of: ["movie"], ["music"], ["podcast"], ["story"], or []
3. THE Curriculum SHALL have each activity use the field name activityType (never type)
4. THE Curriculum SHALL have each activity include title, description, and data fields
5. THE Curriculum SHALL have each activityType value be one of the 11 valid types: introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, vocabLevel3, reading, speakReading, readAlong, writingSentence, writingParagraph
6. THE Curriculum SHALL have all content fields (text, vocabList, items, instructions, prompts) inside the data object, not inline on the activity
7. THE Curriculum SHALL have vocabList on vocab activities (viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, vocabLevel3) as a non-empty array of lowercase strings
8. THE Curriculum SHALL use the field name vocabList (never words) on all activities that carry vocabulary
9. WHEN a session contains both viewFlashcards and speakFlashcards activities, THE Curriculum SHALL have identical vocabList arrays on both activities
10. THE Curriculum SHALL exclude all auto-generated strip keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId) from the content JSON

### Requirement 6: Series and Collection Organization

**User Story:** As a learner browsing the catalog, I want curriculums organized into thematic series and collections, so that I can find content relevant to my interests.

#### Acceptance Criteria

1. WHEN a new language pair phase begins, THE Orchestrator SHALL create collections with titles in the User_Language
2. WHEN a new language pair phase begins, THE Orchestrator SHALL create series within each collection with titles in the User_Language and Target_Language topic labels where appropriate
3. THE Series SHALL have a description of 255 characters or fewer
4. THE Series SHALL contain curriculums with homogeneous language and userLanguage values
5. THE Series SHALL have a maximum of 1 difficulty level gap between any two member curriculums
6. WHEN a curriculum is added to a series, THE System SHALL call curriculum/setDisplayOrder to set an explicit display order
7. WHEN a series is added to a collection, THE System SHALL call curriculum-series/setDisplayOrder to set an explicit display order
8. THE Collection SHALL have a short informative category summary as its description (not persuasive copy)

### Requirement 7: Content Quality — Persuasive Copy

**User Story:** As a learner, I want curriculum descriptions that are emotionally engaging and make me want to start learning, so that I feel motivated to begin each curriculum.

#### Acceptance Criteria

1. THE Curriculum description SHALL follow the multi-paragraph persuasive copy structure: bold headline, concrete examples, vivid metaphor, transformation promise, and learning-to-growth tie-in
2. THE Curriculum description SHALL open with an ALL-CAPS headline using the assigned Tone_Palette type
3. THE Curriculum preview.text SHALL be approximately 150 words of expanded persuasive copy with vivid hooks and vocabulary word mentions
4. THE Curriculum introAudio for learning sessions SHALL be 500-800 words each, teaching each vocabulary word with part of speech, definition, example sentence, and article context
5. THE Curriculum introAudio for the review session SHALL congratulate the learner, recap previous sessions, and explain the review activities
6. THE Curriculum introAudio farewell script SHALL be 400-600 words, reviewing each vocabulary word with a fresh example sentence and providing a warm sign-off
7. THE Curriculum writingSentence items SHALL include detailed prompts specifying context, the target word, and an example sentence
8. THE Curriculum writingParagraph prompts SHALL reference specific concepts from the reading passages and guide analytical writing using session vocabulary

### Requirement 8: Description Tone Variety

**User Story:** As a learner browsing multiple curriculums, I want varied rhetorical approaches in descriptions, so that the catalog feels fresh and each curriculum has a distinct voice.

#### Acceptance Criteria

1. THE Curriculum description tone SHALL be one of the 6 Tone_Palette types: provocative_question, bold_declaration, vivid_scenario, empathetic_observation, surprising_fact, metaphor_led
2. WHEN two curriculums are adjacent in the same series, THE System SHALL assign different description tones to each
3. WHEN two series are adjacent in the same collection, THE System SHALL assign different description tones to each
4. WHILE assigning tones across a language pair, THE System SHALL ensure no single Tone_Palette type exceeds 30% of total assignments
5. THE Curriculum farewell introAudio tone SHALL be one of the 5 Farewell_Palette registers: introspective_guide, warm_accountability, team_building_energy, quiet_awe, practical_momentum
6. WHEN two curriculums are adjacent in the same series, THE System SHALL assign different farewell tones to each
7. THE Orchestrator SHALL document all tone assignments in comments for tracking

### Requirement 9: Hand-Crafted Content

**User Story:** As a learner, I want each curriculum to feel individually written by a subject-matter expert, so that the content is authentic and engaging rather than formulaic.

#### Acceptance Criteria

1. THE Curriculum SHALL have all learner-facing text (introAudio, reading passages, descriptions, previews, writing prompts, farewell scripts) individually crafted for its specific topic
2. THE Curriculum SHALL avoid template functions, string interpolation patterns, or fill-in-the-blank approaches for generating learner-facing text
3. THE Curriculum SHALL have reading passages that are contextually relevant to the curriculum topic and appropriate for the difficulty level
4. THE Curriculum SHALL have vocabulary words that are thematically related to the curriculum topic
5. THE Curriculum SHALL have no vocabulary word repeats within a series (each series maintains a unique vocabulary set)

### Requirement 10: API Integration

**User Story:** As a platform operator, I want curriculums created through the standard API with correct parameters, so that they integrate properly with the existing platform.

#### Acceptance Criteria

1. WHEN creating a curriculum, THE System SHALL POST to https://helloapi.step.is/curriculum/create with firebaseIdToken, language, userLanguage, and content (JSON string) as top-level body parameters
2. WHEN creating a curriculum, THE System SHALL authenticate using UID zs5AMpVfqkcfDf8CJ9qrXdH58d73
3. WHEN a curriculum is created, THE System SHALL NOT call curriculum/setPublic (newly created curriculums remain private)
4. WHEN an API call fails, THE System SHALL log the error with context (curriculum title, series, operation) and continue
5. THE System SHALL use a 30-second timeout on all API requests

### Requirement 11: Content Validation

**User Story:** As a platform operator, I want all curriculum content validated before upload, so that corrupted or malformed content never reaches the database.

#### Acceptance Criteria

1. WHEN a curriculum script runs, THE Validator SHALL check the content JSON before any API call is made
2. IF the Validator detects a structural violation, THEN THE Validator SHALL raise a ValueError with a message identifying the specific violation
3. IF the Validator detects a violation, THEN THE System SHALL abort the upload for that curriculum (no partial uploads)
4. THE Validator SHALL check top-level structure: non-null, non-empty title, description, preview.text, contentTypeTags, learningSessions
5. THE Validator SHALL check session structure: correct session count (4 for beginner, 5 for standard), each with non-empty title and activities array
6. THE Validator SHALL check activity structure: activityType field (not type), valid activityType value, title, description, data fields present
7. THE Validator SHALL check vocabList format: non-empty array of lowercase strings, field name is vocabList (never words)
8. THE Validator SHALL check viewFlashcards and speakFlashcards in the same session have identical vocabList arrays
9. THE Validator SHALL check vocabulary count: 12 unique words for beginner (6 per learning session), 18 unique words for standard (6 per learning session)
10. THE Validator SHALL check no strip keys appear anywhere in the JSON tree
11. THE Validator SHALL check writing activity structure: writingSentence has vocabList, items with prompt and targetVocab; writingParagraph has vocabList, instructions, and prompts array with length 2 or more

### Requirement 12: Verification and Documentation

**User Story:** As a platform operator, I want each language pair phase verified and documented, so that I can audit the content and recreate it if needed.

#### Acceptance Criteria

1. WHEN a language pair phase is complete, THE System SHALL run duplicate check queries for all curriculum titles created in that phase
2. WHEN a language pair phase is complete, THE System SHALL verify each series has the expected number of curriculums with correct display orders
3. WHEN a language pair phase is complete, THE System SHALL verify language homogeneity via the curriculum_series_language_list view
4. WHEN a language pair phase is complete, THE System SHALL verify level gap compliance via the curriculum_series_level_gap view
5. WHEN a language pair phase is complete, THE System SHALL create a README.md with all collection IDs, series IDs, curriculum IDs, display orders, vocabulary lists, tone assignments, SQL verification queries, and recreation instructions
6. WHEN a language pair phase is complete, THE System SHALL delete all create_*.py scripts (only README.md and shared modules remain)

### Requirement 13: Phased Execution

**User Story:** As a platform operator, I want the expansion executed in phases with verification gates, so that I can catch issues early before they propagate across all language pairs.

#### Acceptance Criteria

1. THE System SHALL execute language pair phases in a defined order with verification gates between each phase
2. WHEN a phase is complete, THE System SHALL pause for verification before proceeding to the next phase
3. THE System SHALL reuse the existing shared modules (validate_content.py, api_helpers.py) from the multilingual-curriculum-expansion spec, adapting the validator to support both beginner (4-session, 12-word) and standard (5-session, 18-word) structures
4. IF a verification gate reveals issues, THEN THE System SHALL resolve the issues before proceeding to the next phase

### Requirement 14: Pricing

**User Story:** As a platform operator, I want curriculums priced according to the established pricing guidelines, so that pricing is consistent across the catalog.

#### Acceptance Criteria

1. THE Beginner_Curriculum with 4 sessions SHALL be priced at 19 credits (beginner short-length with 4 sessions)
2. THE Standard_Curriculum with 5 sessions at preintermediate or intermediate level SHALL be priced at 49 credits
3. THE System SHALL call curriculum/setPrice with the appropriate price after creating each curriculum

### Requirement 15: Curriculum Title Rules

**User Story:** As a learner, I want concise curriculum titles that don't repeat information already visible from the series or collection context.

#### Acceptance Criteria

1. THE Curriculum title SHALL be as short as possible, relying on the series and collection for context
2. THE Curriculum title SHALL NOT repeat the series name, collection name, content type prefix, skill-focus label, or audience suffix
3. THE Curriculum title SHALL NOT include the difficulty level
