# Requirements Document

## Introduction

This feature expands the language-learning platform to 6 new language pairs by creating ~460 curriculums organized into collections and series. The expansion covers 4 bilingual pairs (vi-fr, vi-de, en-fr, en-de) for beginner-to-intermediate learners and 2 single-language pairs (fr-fr, de-de) for upper-intermediate/advanced learners. Each curriculum follows the established 18-word, 5-session structure with multi-activity learning sequences. Content is created via standalone Python scripts calling the REST API, following all existing quality standards for persuasive copy, tone variety, and structural correctness.

## Glossary

- **Curriculum_Creator**: The system of standalone Python scripts that generate curriculum JSON content and upload it via the REST API
- **Content_Validator**: The validation logic (inline in each script) that checks curriculum JSON against the Content Corruption Detection Rules before upload
- **Collection_Organizer**: The orchestrator scripts that create collections, series, wire them together, and set display orders via the REST API
- **Tone_Assigner**: The logic that assigns description tones and farewell tones to each curriculum, series, and collection, ensuring variety constraints are met
- **Language_Pair**: A combination of `userLanguage` (the learner's native language) and `language` (the target language being learned), expressed as `{userLanguage}-{language}` using ISO 639-1 codes
- **Bilingual_Curriculum**: A curriculum where user-facing text (titles, descriptions, introAudio, writing prompts) is in the learner's native language and reading passages are in the target language
- **Single_Language_Curriculum**: A curriculum where all text — user-facing and reading passages — is in a single language, suitable for upper-intermediate/advanced learners
- **Session**: One learning unit within a curriculum, containing ordered activities. Standard structure: 3 learning sessions + 1 review session + 1 final reading session
- **Activity**: A single learning exercise within a session (introAudio, viewFlashcards, speakFlashcards, vocabLevel1/2/3, reading, speakReading, readAlong, writingSentence, writingParagraph)
- **Persuasive_Copy**: The required writing style for all learner-facing marketing text — emotional sales copy with bold headline, concrete examples, vivid metaphor, transformation promise, and personal growth tie-in
- **Tone_Palette**: The 6 rhetorical opener types used for description variety: provocative_question, bold_declaration, vivid_scenario, empathetic_observation, surprising_fact, metaphor_led
- **Farewell_Palette**: The 5 emotional registers for farewell introAudio scripts: introspective_guide, warm_accountability, team_building_energy, quiet_awe, practical_momentum
- **Strip_Keys**: Auto-generated platform keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId) that must never be included in new curriculum content

## Requirements

### Requirement 1: Language Pair Coverage and Curriculum Counts

**User Story:** As a platform owner, I want to create curriculums for 6 new language pairs with specific volume targets, so that learners across Vietnamese, English, French, and German language backgrounds have comprehensive learning content.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL produce approximately 100 curriculums for the vi-fr language pair (userLanguage=vi, language=fr) as Bilingual_Curriculums
2. THE Curriculum_Creator SHALL produce approximately 100 curriculums for the vi-de language pair (userLanguage=vi, language=de) as Bilingual_Curriculums
3. THE Curriculum_Creator SHALL produce approximately 100 curriculums for the en-fr language pair (userLanguage=en, language=fr) as Bilingual_Curriculums
4. THE Curriculum_Creator SHALL produce approximately 100 curriculums for the en-de language pair (userLanguage=en, language=de) as Bilingual_Curriculums
5. THE Curriculum_Creator SHALL produce approximately 30 curriculums for the fr-fr language pair (userLanguage=fr, language=fr) as Single_Language_Curriculums
6. THE Curriculum_Creator SHALL produce approximately 30 curriculums for the de-de language pair (userLanguage=de, language=de) as Single_Language_Curriculums
7. WHEN creating a Bilingual_Curriculum, THE Curriculum_Creator SHALL write user-facing text (titles, descriptions, previews, introAudio scripts, writing prompts, activity titles, activity descriptions, session titles) in the learner's native language and reading passages in the target language
8. WHEN creating a Single_Language_Curriculum, THE Curriculum_Creator SHALL write all text — user-facing and reading passages — in the single language (French for fr-fr, German for de-de)

### Requirement 2: Topic and Theme Organization

**User Story:** As a platform owner, I want diverse, well-organized topic coverage across all language pairs, so that learners encounter varied and engaging subject matter.

#### Acceptance Criteria

1. THE Collection_Organizer SHALL organize each bilingual language pair (vi-fr, vi-de, en-fr, en-de) into 4 collections of 25 curriculums each, with each collection containing 5 series of 5 curriculums
2. THE Collection_Organizer SHALL organize each single-language pair (fr-fr, de-de) into 2 collections of 15 curriculums each, with each collection containing 3 series of 5 curriculums
3. THE Collection_Organizer SHALL assign thematic domains to collections covering these categories across the bilingual pairs: Daily Life and Travel, Business and Professional, Academic and Intellectual, Culture and Society
4. THE Collection_Organizer SHALL assign thematic domains to collections for the single-language pairs covering: Literature and Advanced Culture, Professional Mastery
5. WHEN organizing vi-fr curriculums, THE Collection_Organizer SHALL use Vietnamese titles for collections and series, with French topic labels in parentheses where appropriate
6. WHEN organizing vi-de curriculums, THE Collection_Organizer SHALL use Vietnamese titles for collections and series, with German topic labels in parentheses where appropriate
7. WHEN organizing en-fr curriculums, THE Collection_Organizer SHALL use English titles for collections and series, with French topic labels in parentheses where appropriate
8. WHEN organizing en-de curriculums, THE Collection_Organizer SHALL use English titles for collections and series, with German topic labels in parentheses where appropriate
9. WHEN organizing fr-fr curriculums, THE Collection_Organizer SHALL use French titles for collections and series
10. WHEN organizing de-de curriculums, THE Collection_Organizer SHALL use German titles for collections and series


### Requirement 3: Topic Plan for Bilingual Pairs (vi-fr, vi-de, en-fr, en-de)

**User Story:** As a platform owner, I want a concrete topic plan for each bilingual language pair, so that content creators know exactly what to build and topics are culturally relevant to each learner audience.

#### Acceptance Criteria

1. THE Collection_Organizer SHALL define the following 4 collections for each bilingual pair, each containing 5 series of 5 curriculums (25 per collection, 100 total):

   **Collection A — Daily Life and Travel (25 curriculums)**
   - Series A1: Food and Dining (5 curriculums — ordering, cooking vocabulary, restaurant culture, dietary preferences, street food/markets)
   - Series A2: City Navigation and Transport (5 curriculums — directions, public transit, accommodation, airport/station, local customs)
   - Series A3: Shopping and Services (5 curriculums — clothing, electronics, banking, healthcare visits, home services)
   - Series A4: Social Life and Relationships (5 curriculums — introductions, invitations, family gatherings, celebrations, conflict resolution)
   - Series A5: Health and Wellness (5 curriculums — fitness, nutrition, mental health, medical emergencies, pharmacy/self-care)

   **Collection B — Business and Professional (25 curriculums)**
   - Series B1: Workplace Communication (5 curriculums — emails, meetings, presentations, phone calls, team collaboration)
   - Series B2: Job Search and Career (5 curriculums — CV/resume, interviews, salary negotiation, networking, career transitions)
   - Series B3: Industry-Specific Vocabulary (5 curriculums — technology, hospitality, manufacturing, retail, logistics)
   - Series B4: Business Operations (5 curriculums — project management, budgeting, reporting, compliance, customer service)
   - Series B5: International Business (5 curriculums — trade terminology, contracts, cross-cultural negotiation, import/export, business law basics)

   **Collection C — Academic and Intellectual (25 curriculums)**
   - Series C1: Science and Technology (5 curriculums — biology, physics, computer science, environmental science, mathematics)
   - Series C2: Economics and Finance (5 curriculums — microeconomics, macroeconomics, personal finance, investment, banking)
   - Series C3: History and Politics (5 curriculums — modern history, political systems, international relations, human rights, media and journalism)
   - Series C4: Psychology and Education (5 curriculums — cognitive psychology, learning theories, child development, social psychology, educational systems)
   - Series C5: Philosophy and Critical Thinking (5 curriculums — ethics, logic, existentialism, aesthetics, argumentation)

   **Collection D — Culture and Society (25 curriculums)**
   - Series D1: Arts and Literature (5 curriculums — visual arts, music, cinema, literary genres, theater/performance)
   - Series D2: Architecture and Design (5 curriculums — historical architecture, interior design, urban planning, sustainable design, fashion)
   - Series D3: Environment and Sustainability (5 curriculums — climate change, renewable energy, conservation, waste management, sustainable living)
   - Series D4: Sports and Recreation (5 curriculums — team sports, individual sports, outdoor activities, fitness culture, competitive events)
   - Series D5: Traditions and Festivals (5 curriculums — national holidays, religious celebrations, culinary traditions, folk arts, modern cultural events)

2. WHEN creating vi-fr or vi-de curriculums, THE Curriculum_Creator SHALL tailor reading passages and examples to contexts relevant to Vietnamese learners (Vietnamese professionals abroad, Vietnamese students in France/Germany, Vietnamese cultural comparisons)
3. WHEN creating en-fr or en-de curriculums, THE Curriculum_Creator SHALL tailor reading passages and examples to contexts relevant to English-speaking learners (expats, international students, business travelers, cultural exchange)
4. THE Curriculum_Creator SHALL select 18 vocabulary words per curriculum that are specific to the target language (French or German) and appropriate for the preintermediate-to-intermediate level
5. WHILE creating curriculums within the same series, THE Curriculum_Creator SHALL ensure vocabulary words do not repeat across curriculums (90 unique words per series)

### Requirement 4: Topic Plan for Single-Language Pairs (fr-fr, de-de)

**User Story:** As a platform owner, I want a concrete topic plan for the single-language advanced pairs, so that French and German native speakers have content that deepens their mastery of their own language.

#### Acceptance Criteria

1. THE Collection_Organizer SHALL define the following 2 collections for each single-language pair, each containing 3 series of 5 curriculums (15 per collection, 30 total):

   **Collection E — Literature and Advanced Culture (15 curriculums)**
   - Series E1: Literary Analysis (5 curriculums — narrative techniques, poetic forms, rhetorical devices, literary criticism, comparative literature)
   - Series E2: Philosophy and Intellectual History (5 curriculums — Enlightenment thought, existentialism, phenomenology, political philosophy, contemporary debates)
   - Series E3: Art, Cinema, and Cultural Criticism (5 curriculums — art movements, film theory, music criticism, cultural identity, media analysis)

   **Collection F — Professional Mastery (15 curriculums)**
   - Series F1: Advanced Business and Law (5 curriculums — corporate law, financial analysis, strategic management, labor law, entrepreneurship)
   - Series F2: Science and Innovation (5 curriculums — research methodology, biotechnology, artificial intelligence, climate science, medical advances)
   - Series F3: Media, Journalism, and Public Discourse (5 curriculums — investigative journalism, editorial writing, public speaking, debate techniques, digital media)

2. WHEN creating fr-fr curriculums, THE Curriculum_Creator SHALL select vocabulary from formal/literary French registers (soutenu, littéraire) appropriate for upper-intermediate to advanced learners
3. WHEN creating de-de curriculums, THE Curriculum_Creator SHALL select vocabulary from formal/academic German registers (Bildungssprache, Fachsprache) appropriate for upper-intermediate to advanced learners
4. THE Curriculum_Creator SHALL write all content for fr-fr curriculums entirely in French, including introAudio scripts, descriptions, previews, writing prompts, and reading passages
5. THE Curriculum_Creator SHALL write all content for de-de curriculums entirely in German, including introAudio scripts, descriptions, previews, writing prompts, and reading passages

### Requirement 5: Curriculum Structure and Activity Schema

**User Story:** As a platform developer, I want every curriculum to follow the established 5-session, 18-word structure with correct activity schemas, so that the content pipeline processes them without errors.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL structure each curriculum with exactly 5 sessions: 3 learning sessions, 1 review session, and 1 final reading session
2. THE Curriculum_Creator SHALL distribute 18 vocabulary words across the 3 learning sessions as 6 words per session
3. WHEN creating a learning session (sessions 1-3), THE Curriculum_Creator SHALL include activities in this order: introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, vocabLevel3, reading, speakReading, readAlong, writingSentence
4. WHEN creating the review session (session 4), THE Curriculum_Creator SHALL include activities covering all 18 words with a comprehensive reading passage
5. WHEN creating the final session (session 5), THE Curriculum_Creator SHALL include a full reading with all 18 words, a readAlong, a writingParagraph, and a farewell introAudio
6. THE Curriculum_Creator SHALL include `activityType`, `title`, `description`, and `data` fields on every activity object
7. THE Curriculum_Creator SHALL use `vocabList` (array of lowercase strings) on all viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, and vocabLevel3 activities
8. THE Curriculum_Creator SHALL ensure viewFlashcards and speakFlashcards within the same session have identical vocabList arrays
9. THE Curriculum_Creator SHALL include `contentTypeTags` at the top level of every curriculum content JSON (use `[]` for general content)
10. THE Curriculum_Creator SHALL never include Strip_Keys in new curriculum content JSON
11. IF the Content_Validator detects a structural violation (missing activityType, inline data fields, wrong vocabList field name, mismatched vocabLists), THEN THE Curriculum_Creator SHALL abort the upload and report the specific violation


### Requirement 6: Collection and Series Hierarchy

**User Story:** As a platform developer, I want collections and series created with correct hierarchy, language homogeneity, and display ordering, so that the client app renders content correctly.

#### Acceptance Criteria

1. THE Collection_Organizer SHALL create each collection via `curriculum-collection/create` with a title and description
2. THE Collection_Organizer SHALL create each series via `curriculum-series/create` with a title and description (≤255 characters)
3. THE Collection_Organizer SHALL wire each series to its parent collection via `curriculum-collection/addSeriesToCollection`
4. THE Collection_Organizer SHALL add each curriculum to its series via `curriculum-series/addCurriculum`
5. WHEN adding a curriculum to a series, THE Collection_Organizer SHALL call `curriculum/setDisplayOrder` to set the curriculum's position within the series
6. THE Collection_Organizer SHALL call `curriculum-series/setDisplayOrder` to set each series' position within its collection
7. THE Collection_Organizer SHALL call `curriculum-collection/setDisplayOrder` to set each collection's global position
8. THE Collection_Organizer SHALL ensure all curriculums within a single series share the same `language` and `userLanguage` values
9. THE Collection_Organizer SHALL ensure all series within a single collection share the same language pair
10. THE Collection_Organizer SHALL ensure the difficulty level gap between any two curriculums in the same series does not exceed 1 level
11. THE Collection_Organizer SHALL create all new curriculums as private (not call `curriculum/setPublic` with `isPublic: true`)
12. THE Collection_Organizer SHALL pass `language` and `userLanguage` as top-level body parameters in `curriculum/create` calls, not only inside the content JSON

### Requirement 7: Quality Standards Compliance

**User Story:** As a content quality owner, I want all curriculum content to meet the established persuasive copy and tone variety standards, so that learner-facing text is engaging and non-repetitive.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL write every curriculum description following the Persuasive_Copy structure: bold headline, concrete examples, vivid metaphor, transformation promise, and personal growth tie-in
2. THE Curriculum_Creator SHALL write every curriculum preview as expanded persuasive copy (~150 words) with vivid hooks, vocabulary word listing, learning journey description, and compelling closing
3. WHEN writing introAudio for sessions 1 and 2, THE Curriculum_Creator SHALL produce 500-800 word teaching scripts that welcome the learner, list vocabulary, teach each word with definition, example sentence, and article context
4. WHEN writing introAudio for session 2, THE Curriculum_Creator SHALL recap session 1 vocabulary before introducing new words
5. WHEN writing introAudio for the review session, THE Curriculum_Creator SHALL congratulate the learner, recap sessions 1-2, and motivate for the final reading
6. WHEN writing the farewell introAudio, THE Curriculum_Creator SHALL review 5-6 key vocabulary words with definitions and fresh example sentences, summarize the learning journey, and provide a warm sign-off
7. THE Curriculum_Creator SHALL write writingSentence prompts with detailed context, target vocabulary word, and a full example sentence showing correct usage
8. THE Curriculum_Creator SHALL write writingParagraph prompts that reference specific concepts from the curriculum topic and guide analytical writing using vocabulary
9. THE Curriculum_Creator SHALL individually craft every piece of learner-facing text for its specific curriculum topic, without using template functions, string interpolation, or generic fill-in-the-blank patterns
10. THE Curriculum_Creator SHALL keep curriculum titles minimal — never repeating series/collection name, content type prefix, skill-focus label, or audience suffix

### Requirement 8: Description and Farewell Tone Variety

**User Story:** As a content quality owner, I want tone variety enforced across all descriptions and farewell scripts, so that adjacent content never feels repetitive.

#### Acceptance Criteria

1. THE Tone_Assigner SHALL assign one of the 6 Tone_Palette types to every series description, curriculum description headline, and collection description angle
2. WHILE assigning tones within a series, THE Tone_Assigner SHALL ensure no two adjacent curriculums use the same Tone_Palette type
3. WHILE assigning tones within a collection, THE Tone_Assigner SHALL ensure no two adjacent series use the same Tone_Palette type
4. THE Tone_Assigner SHALL ensure no single Tone_Palette type exceeds 30% of descriptions in any batch (per language pair)
5. THE Tone_Assigner SHALL assign one of the 5 Farewell_Palette registers to every farewell introAudio script
6. WHILE assigning farewell tones within a series, THE Tone_Assigner SHALL ensure no two adjacent curriculums use the same Farewell_Palette register
7. THE Tone_Assigner SHALL document all tone assignments in comments within each creation script and in the series README
8. THE Curriculum_Creator SHALL write series descriptions as short persuasive hooks (≤255 characters) using the assigned Tone_Palette type
9. THE Curriculum_Creator SHALL write collection descriptions as short informative category summaries (not persuasive copy) with varied angles

### Requirement 9: Script Architecture and Execution Workflow

**User Story:** As a developer, I want a clear, repeatable workflow for creating ~460 curriculums at scale, so that the process is manageable, traceable, and recoverable.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL produce one standalone Python script per curriculum (approximately 460 scripts total)
2. THE Curriculum_Creator SHALL produce one orchestrator script per language pair that creates collections, series, wires them together, and sets display orders
3. THE Curriculum_Creator SHALL organize scripts into directories by language pair (e.g., `vi-fr/`, `vi-de/`, `en-fr/`, `en-de/`, `fr-fr/`, `de-de/`)
4. WHEN a curriculum script executes successfully, THE Curriculum_Creator SHALL record the curriculum ID in a tracking log
5. WHEN all curriculums in a series are created and verified, THE Curriculum_Creator SHALL delete the creation scripts, leaving only the README
6. THE Curriculum_Creator SHALL authenticate all API calls using `firebase_token.get_firebase_id_token` with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`
7. THE Curriculum_Creator SHALL use `https://helloapi.step.is` as the API base URL for all REST calls
8. IF a curriculum creation API call fails, THEN THE Curriculum_Creator SHALL log the error with the curriculum title and series context, and continue with the next curriculum
9. WHEN all curriculums for a language pair are created, THE Curriculum_Creator SHALL run a duplicate check query for each curriculum title and resolve any duplicates (keep earliest, delete extras)

### Requirement 10: Batch Execution Strategy

**User Story:** As a developer, I want a phased execution plan for creating ~460 curriculums, so that I can manage the workload incrementally and catch issues early.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL execute creation in 6 phases, one per language pair, in this order: vi-fr, vi-de, en-fr, en-de, fr-fr, de-de
2. WHEN starting a new language pair phase, THE Curriculum_Creator SHALL first create the orchestrator infrastructure (collections, series, wiring) before creating any curriculums
3. WHEN completing a series (5 curriculums), THE Curriculum_Creator SHALL verify the series by querying the database to confirm all 5 curriculums exist with correct display orders, language values, and non-empty content
4. WHEN completing a collection (25 curriculums for bilingual, 15 for single-language), THE Curriculum_Creator SHALL verify language homogeneity via the `curriculum_series_language_list` view and level gap via the `curriculum_series_level_gap` view
5. IF verification reveals missing or malformed curriculums, THEN THE Curriculum_Creator SHALL recreate the affected curriculums before proceeding to the next series
6. THE Curriculum_Creator SHALL produce a README per language pair directory documenting all collection IDs, series IDs, curriculum IDs, tone assignments, vocabulary lists, and SQL verification queries

### Requirement 11: Content Validation and Corruption Prevention

**User Story:** As a platform developer, I want every curriculum validated against the Content Corruption Detection Rules before upload, so that no corrupted content enters the database.

#### Acceptance Criteria

1. THE Content_Validator SHALL verify that every curriculum content JSON has non-null, non-empty `title`, `description`, and `preview.text` fields
2. THE Content_Validator SHALL verify that `learningSessions` is a non-empty array where each session has a non-empty `title` and `activities` array
3. THE Content_Validator SHALL verify that every activity has `activityType` (not `type`), `title`, `description`, and `data` fields, with content fields inside `data` (not inline on the activity)
4. THE Content_Validator SHALL verify that `activityType` values are one of: introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, vocabLevel3, reading, speakReading, readAlong, writingSentence, writingParagraph
5. THE Content_Validator SHALL verify that vocabList fields contain arrays of lowercase strings (not objects, numbers, or other types) and use the field name `vocabList` (never `words`)
6. THE Content_Validator SHALL verify that viewFlashcards and speakFlashcards in the same session have identical vocabList arrays
7. THE Content_Validator SHALL verify that writingSentence activities have `data.vocabList`, `data.items` (non-empty array), and each item has `prompt` and `targetVocab`
8. THE Content_Validator SHALL verify that writingParagraph activities have `data.vocabList`, `data.instructions`, and `data.prompts` (array of strings, length ≥ 2)
9. THE Content_Validator SHALL verify that no Strip_Keys appear anywhere in the curriculum content JSON
10. THE Content_Validator SHALL verify that the curriculum contains exactly 18 unique vocabulary words across all sessions
11. IF any validation check fails, THEN THE Content_Validator SHALL abort the upload and print the specific rule violation with the curriculum title

### Requirement 12: Language-Specific Content Adaptation

**User Story:** As a content quality owner, I want content adapted to each target language's cultural and linguistic context, so that learners receive authentic, culturally appropriate material.

#### Acceptance Criteria

1. WHEN creating French reading passages (for vi-fr and en-fr), THE Curriculum_Creator SHALL write in natural, contemporary French appropriate for the curriculum's difficulty level
2. WHEN creating German reading passages (for vi-de and en-de), THE Curriculum_Creator SHALL write in natural, contemporary German appropriate for the curriculum's difficulty level
3. WHEN creating fr-fr reading passages, THE Curriculum_Creator SHALL write in formal/literary French with vocabulary from soutenu and littéraire registers
4. WHEN creating de-de reading passages, THE Curriculum_Creator SHALL write in formal/academic German with vocabulary from Bildungssprache and Fachsprache registers
5. WHEN creating Vietnamese user-facing text (for vi-fr and vi-de), THE Curriculum_Creator SHALL follow the same persuasive copy conventions established for existing vi-en curriculums, using Vietnamese rhetorical patterns
6. WHEN creating English user-facing text (for en-fr and en-de), THE Curriculum_Creator SHALL follow the same persuasive copy conventions established for existing en-en curriculums, using English rhetorical patterns
7. WHEN creating French user-facing text (for fr-fr), THE Curriculum_Creator SHALL adapt the persuasive copy conventions to French rhetorical traditions (e.g., French headline conventions, French metaphor patterns)
8. WHEN creating German user-facing text (for de-de), THE Curriculum_Creator SHALL adapt the persuasive copy conventions to German rhetorical traditions (e.g., German headline conventions, German metaphor patterns)
9. THE Curriculum_Creator SHALL ensure vocabulary words for French target curriculums are drawn from standard French (not regional variants) unless the curriculum topic specifically addresses regional language
10. THE Curriculum_Creator SHALL ensure vocabulary words for German target curriculums are drawn from standard High German (Hochdeutsch) unless the curriculum topic specifically addresses regional language

### Requirement 13: Documentation and Traceability

**User Story:** As a developer, I want comprehensive documentation for every language pair, so that content can be verified, debugged, and recreated if needed.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL create one README.md per language pair directory containing: all collection IDs, series IDs, curriculum IDs with display orders, vocabulary lists per curriculum, tone assignments (description and farewell), and SQL verification queries
2. THE Curriculum_Creator SHALL include in each README the recreation instructions: how to regenerate the content if needed, which API endpoints to call, and the authentication pattern
3. THE Curriculum_Creator SHALL delete all Python scripts after successful creation and verification of each language pair, leaving only the README
4. THE Curriculum_Creator SHALL include duplicate-check SQL queries in each README
5. THE Curriculum_Creator SHALL include language homogeneity and level gap verification queries in each README
6. WHEN a curriculum is created, THE Curriculum_Creator SHALL log the curriculum ID, title, series, and collection to stdout for tracking
