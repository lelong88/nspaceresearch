# Requirements Document

## Introduction

Design and create a new collection of Economics English curriculums for Vietnamese-speaking students at the University of Economics (Đại Học Kinh Tế), at the preintermediate-to-intermediate level. The collection covers academic economics topics that university students encounter in their coursework — microeconomics, macroeconomics, international trade, accounting, marketing, management, and related disciplines — with vocabulary and reading passages directly relevant to their studies.

This is distinct from the existing vi-en economics/business content:
- **"Kinh Tế & Tài Chính Cá Nhân"** series covers personal finance topics (investing, inflation, gig economy, behavioral economics)
- **"Chủ Doanh Nghiệp"** series covers small business/entrepreneurship topics (opportunity cost, customer demand, profit, branding)

The new collection focuses on **academic economics** — the theoretical frameworks, analytical tools, and disciplinary vocabulary that economics majors study in university courses. Each curriculum is created via a standalone Python script calling the helloapi REST API.

### What This Spec Covers

- A new collection with multiple series organized by economics subdiscipline
- Curriculum topics, vocabulary selection, and content structure for each series
- Series and collection organization, tone assignments, and display ordering
- Creation workflow, verification, and documentation

### What This Spec Does NOT Cover

- Changes to existing economics/business curriculums
- Client-side UI changes
- Content generation pipeline (audio, illustrations) — curriculums are created private
- Other language pairs

## Glossary

- **Collection**: A top-level organizational container that holds one or more Series. Stored in `curriculum_collections`.
- **Series**: A thematic grouping of Curriculums within a Collection. Has a title, description (≤ 255 chars), and display order. Stored in `curriculum_series`.
- **Curriculum**: A single learning unit containing a title, preview, description, and learning sessions with ordered activities. Stored in `curriculum` with content as JSONB.
- **Learning_Session**: An ordered group of activities within a Curriculum.
- **Activity**: A single learning step within a session (e.g., introAudio, viewFlashcards, reading, writingSentence).
- **Platform**: The language-learning application at helloapi.step.is.
- **Econ_Student**: A Vietnamese-speaking student enrolled at the University of Economics, learning English at preintermediate-to-intermediate level.
- **Persuasive_Copy**: The multi-paragraph Vietnamese marketing text style required for curriculum descriptions, following the 5-beat structure (bold headline, concrete examples, vivid metaphor, transformation promise, learning tie-in).
- **Tone_Palette**: The six rhetorical opener types: provocative_question, bold_declaration, vivid_scenario, empathetic_observation, surprising_fact, metaphor_led.
- **contentTypeTags**: A JSON array field on curriculum content. Must be `[]` for these curriculums.
- **Creation_Script**: A standalone Python script that calls the helloapi REST API to create a curriculum.
- **Strip_Keys**: Auto-generated platform keys that must never appear in new content (mp3Url, illustrationSet, segments, etc.).

## Requirements

### Requirement 1: New Collection for University Economics English

**User Story:** As a content manager, I want a dedicated collection for University Economics English curriculums, so that economics students can find all relevant academic economics vocabulary content in one place, separate from the existing personal finance and business owner content.

#### Acceptance Criteria

1. THE Platform SHALL have a new collection with a Vietnamese title identifying it as Economics English for university students.
2. THE Collection SHALL have a neutral, informative description summarizing its contents (not persuasive copy, per collection description rules).
3. THE Collection SHALL be separate from the existing "Học Từ Vựng Theo Chủ Đề" collection that houses the personal finance and business owner series.
4. THE Collection SHALL contain only vi-en curriculums at preintermediate-to-intermediate level.

### Requirement 2: Series Organization by Economics Subdiscipline

**User Story:** As an economics student, I want curriculums organized into thematic series by economics subdiscipline, so that I can focus on the vocabulary area most relevant to my current courses.

#### Acceptance Criteria

1. THE Collection SHALL contain multiple Series, each covering a distinct economics subdiscipline.
2. THE following Series SHALL be created to cover core university economics areas:
   - **Series A — Kinh Tế Vi Mô (Microeconomics)**: Vocabulary for supply and demand, market structures, consumer theory, production costs, and price mechanisms.
   - **Series B — Kinh Tế Vĩ Mô (Macroeconomics)**: Vocabulary for GDP, unemployment, fiscal policy, economic growth, and business cycles.
   - **Series C — Thương Mại Quốc Tế & Toàn Cầu Hóa (International Trade & Globalization)**: Vocabulary for trade theory, tariffs, exchange rates, trade agreements, and global supply chains.
   - **Series D — Kế Toán & Tài Chính Doanh Nghiệp (Accounting & Corporate Finance)**: Vocabulary for financial statements, auditing, capital budgeting, corporate governance, and financial analysis.
   - **Series E — Marketing & Quản Trị (Marketing & Management)**: Vocabulary for market research, branding strategy, organizational behavior, human resources, and strategic planning.
3. Each Series SHALL have a description of 255 characters or fewer.
4. Each Series description SHALL use a tone from the Tone_Palette, and no two adjacent Series within the Collection SHALL use the same tone.
5. No single tone SHALL exceed 30% of the total Series descriptions in the Collection.

### Requirement 3: Curriculum Structure and Content Standards

**User Story:** As an economics student, I want each curriculum to teach 18 economics English vocabulary words through a structured multi-session format, so that I can learn academic terminology through reading, listening, speaking, and writing practice.

#### Acceptance Criteria

1. Each Curriculum SHALL contain exactly 18 vocabulary words divided into 3 groups of 6 words each.
2. Each Curriculum SHALL have 5 learning sessions: 3 learning sessions (one per word group), 1 review session, and 1 full-reading session.
3. Each learning session SHALL include the following activities in order: introAudio (welcome/vocab intro), viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, vocabLevel3, reading, speakReading, readAlong, writingSentence.
4. THE review session SHALL include introAudio (review intro), viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, vocabLevel3 for all 18 words, plus writingSentence.
5. THE full-reading session SHALL include introAudio (full reading intro), reading, speakReading, readAlong, writingParagraph, and a farewell introAudio.
6. Each Curriculum SHALL set `contentTypeTags` to `[]`.
7. Each Curriculum SHALL set `language` to `'en'` and `userLanguage` to `'vi'`.

### Requirement 4: Vocabulary Selection for Academic Economics Context

**User Story:** As an economics student, I want vocabulary words that are genuinely used in academic economics courses and textbooks, so that the English I learn is directly applicable to my university studies and future career.

#### Acceptance Criteria

1. Each Curriculum's 18 vocabulary words SHALL be drawn from authentic academic economics usage in the subdiscipline covered by its parent Series.
2. Vocabulary words SHALL be appropriate for preintermediate-to-intermediate learners — core economics terms that a university student encounters in textbooks, lectures, and academic papers, not rare specialist jargon.
3. WHEN a Curriculum belongs to Series A (Microeconomics), THE vocabulary SHALL include terms for market analysis, consumer behavior, and firm theory (e.g., "equilibrium", "elasticity", "marginal", "surplus", "monopoly", "scarcity").
4. WHEN a Curriculum belongs to Series B (Macroeconomics), THE vocabulary SHALL include terms for national economic analysis and policy (e.g., "aggregate", "recession", "fiscal", "deficit", "stimulus", "inflation").
5. WHEN a Curriculum belongs to Series C (International Trade), THE vocabulary SHALL include terms for global commerce and trade policy (e.g., "tariff", "quota", "comparative", "bilateral", "subsidy", "depreciation").
6. WHEN a Curriculum belongs to Series D (Accounting & Corporate Finance), THE vocabulary SHALL include terms for financial reporting and corporate decision-making (e.g., "liability", "equity", "depreciation", "audit", "dividend", "leverage").
7. WHEN a Curriculum belongs to Series E (Marketing & Management), THE vocabulary SHALL include terms for business strategy and organizational management (e.g., "segmentation", "positioning", "stakeholder", "delegation", "retention", "benchmark").
8. Vocabulary words SHALL NOT duplicate across curriculums within the same Series.
9. Vocabulary words SHALL NOT substantially overlap with the existing "Kinh Tế & Tài Chính Cá Nhân" or "Chủ Doanh Nghiệp" series vocabulary.

### Requirement 5: Bilingual Content and Language Rules

**User Story:** As a Vietnamese-speaking economics student at preintermediate level, I want user-facing text in Vietnamese and reading passages in English, so that I can understand instructions while building my English academic reading skills.

#### Acceptance Criteria

1. THE Curriculum title SHALL be bilingual, with an English economics topic followed by a Vietnamese subtitle.
2. THE Curriculum description, preview text, introAudio scripts, and activity titles/descriptions SHALL be written in Vietnamese.
3. THE reading passages (reading, speakReading, readAlong activities) SHALL be written in English at a level comprehensible to preintermediate-to-intermediate learners.
4. THE writingSentence prompts SHALL be in Vietnamese, with English example sentences.
5. THE writingParagraph instructions and prompts SHALL be in Vietnamese, guiding the learner to write in English.
6. THE Curriculum title SHALL NOT include a difficulty level label.
7. THE Curriculum title SHALL be minimal — the series and collection provide context.

### Requirement 6: Persuasive Marketing Copy for Curriculum Descriptions

**User Story:** As a content manager, I want each curriculum's description and preview to follow the platform's persuasive copy standards with economics-student-specific hooks, so that the content feels compelling and personally relevant to the target audience.

#### Acceptance Criteria

1. Each Curriculum description SHALL follow the 5-beat Persuasive_Copy structure: ALL-CAPS headline, concrete examples, vivid metaphor, transformation promise, and learning tie-in.
2. Each Curriculum description SHALL use a tone from the Tone_Palette for its headline opener.
3. WITHIN a Series, no two adjacent Curriculum descriptions SHALL use the same tone.
4. No single tone SHALL exceed 30% of all Curriculum descriptions across the Collection.
5. THE Persuasive_Copy SHALL reference economics-student-specific pain points and aspirations (e.g., struggling to read English economics textbooks, wanting to understand international research papers, preparing for careers at multinational firms or international organizations).
6. Each Curriculum preview (~150 words) SHALL name the 18 vocabulary words, describe the learning journey, and use vivid economics-context hooks.

### Requirement 7: Reading Passages Grounded in Academic Economics Contexts

**User Story:** As an economics student, I want reading passages that cover real economics topics relevant to my coursework, so that I learn vocabulary in meaningful academic contexts rather than generic texts.

#### Acceptance Criteria

1. Each reading passage SHALL be topically aligned with the Curriculum's economics subdiscipline and vocabulary words.
2. WHEN a Curriculum covers microeconomics, THE reading passages SHALL describe market mechanisms, consumer decisions, firm behavior, or price theory using the session's 6 vocabulary words.
3. WHEN a Curriculum covers macroeconomics, THE reading passages SHALL describe national economic indicators, policy debates, or economic cycles using the session's vocabulary.
4. WHEN a Curriculum covers international trade, THE reading passages SHALL describe trade relationships, globalization dynamics, or trade policy scenarios using the session's vocabulary.
5. WHEN a Curriculum covers accounting and corporate finance, THE reading passages SHALL describe financial reporting, corporate decisions, or investment analysis using the session's vocabulary.
6. WHEN a Curriculum covers marketing and management, THE reading passages SHALL describe market strategies, organizational challenges, or management frameworks using the session's vocabulary.
7. Each reading passage SHALL be written at a level where a preintermediate-to-intermediate learner can understand approximately 95% of the text, with the 6 vocabulary words providing the remaining challenge.

### Requirement 8: Curriculum Topic Plan per Series

**User Story:** As a content manager, I want a defined list of curriculum topics for each series, so that the collection provides comprehensive coverage of university economics domains without gaps or overlaps with existing content.

#### Acceptance Criteria

1. Series A (Microeconomics) SHALL contain curriculums covering at minimum: supply and demand fundamentals, market structures and competition, consumer choice and utility, production costs and firm decisions, and market failure and externalities.
2. Series B (Macroeconomics) SHALL contain curriculums covering at minimum: GDP and economic indicators, unemployment and labor markets, fiscal policy and government spending, monetary policy and central banking, and economic growth and development.
3. Series C (International Trade & Globalization) SHALL contain curriculums covering at minimum: comparative advantage and trade theory, tariffs, quotas, and trade barriers, foreign exchange markets, international trade organizations, and global supply chains and logistics.
4. Series D (Accounting & Corporate Finance) SHALL contain curriculums covering at minimum: financial statements and reporting, cost accounting and budgeting, auditing and compliance, capital structure and investment, and corporate governance and ethics.
5. Series E (Marketing & Management) SHALL contain curriculums covering at minimum: market research and consumer behavior, branding and product strategy, organizational behavior and leadership, human resource management, and strategic planning and competitive analysis.
6. Each Curriculum topic SHALL be distinct and SHALL NOT substantially overlap with another Curriculum in the same Series.
7. Each Curriculum topic SHALL NOT overlap with existing "Kinh Tế & Tài Chính Cá Nhân" topics (investing, inflation/monetary policy, gig economy, behavioral economics) or "Chủ Doanh Nghiệp" topics (opportunity cost, customer/demand, profit/expense, branding/competition).
8. All curriculums within a Series SHALL maintain a consistent difficulty level with a maximum of 1 level gap (preintermediate to intermediate).

### Requirement 9: Farewell Scripts with Vocabulary Review

**User Story:** As an economics student, I want the farewell audio at the end of each curriculum to review key vocabulary with fresh economics examples, so that I reinforce what I learned before moving on.

#### Acceptance Criteria

1. Each Curriculum's farewell introAudio SHALL review 5-6 key vocabulary words with definitions and fresh example sentences drawn from economics contexts.
2. Each farewell script SHALL connect the reviewed words back to the Curriculum's economics theme.
3. Each farewell script SHALL close with a warm, encouraging sign-off in Vietnamese.
4. WITHIN a Series, farewell scripts SHALL vary in emotional register, using different farewell tones (introspective guide, warm accountability, team-building energy, quiet awe, practical momentum).
5. No two adjacent Curriculums in a Series SHALL use the same farewell tone.

### Requirement 10: introAudio Quality Standards

**User Story:** As an economics student, I want introAudio scripts to be individually crafted for each curriculum's economics topic, so that I receive rich, contextual vocabulary teaching rather than generic templates.

#### Acceptance Criteria

1. WHEN a Session 1 introAudio is created, THE script SHALL welcome the learner, set the scene with vivid context related to the economics topic, and list all vocabulary words for the session.
2. WHEN a vocabulary-teaching introAudio is created, THE script SHALL teach each word individually with: part of speech, full definition, example sentence from the reading context, and explanation of how the word appears in the article.
3. WHEN a Session 2+ introAudio is created, THE script SHALL recap previous session words before introducing new ones.
4. WHEN a review session introAudio is created, THE script SHALL congratulate the learner, briefly recap all previous sessions, and explain the review format.
5. WHEN a farewell introAudio is created, THE script (400-600 words) SHALL review 5-6 key vocabulary words with definitions and fresh example sentences, summarize the learning journey, and close with a warm sign-off.
6. WITHIN a Series, farewell scripts SHALL vary in emotional register using different farewell tones.
7. No two adjacent Curriculums in a Series SHALL use the same farewell tone.

### Requirement 11: Writing Activity Quality Standards

**User Story:** As an economics student, I want writingSentence and writingParagraph activities to have detailed, topic-specific prompts, so that I produce meaningful writing using economics vocabulary rather than filling in blanks.

#### Acceptance Criteria

1. WHEN a writingSentence activity is created, THE Activity SHALL include items with: a `targetVocab` field, a detailed `prompt` specifying context for using the word, and an example sentence showing correct usage.
2. WHEN a bilingual writingSentence is created, THE prompt SHALL be in Vietnamese with the example sentence in English.
3. WHEN a writingParagraph activity is created, THE Activity SHALL include: a `vocabList` of words to use, `instructions` describing the writing task, and `prompts` (array of at least 2 strings) providing specific guiding questions.
4. THE writingParagraph prompts SHALL reference specific concepts from the curriculum's reading passages and require analytical or argumentative responses relevant to economics.

### Requirement 12: Activity Schema Compliance

**User Story:** As a content manager, I want all activities to comply with the platform's content schema, so that the client app renders them correctly without errors.

#### Acceptance Criteria

1. Each Activity SHALL include `activityType`, `title`, `description`, and `data` fields.
2. THE `activityType` field SHALL use one of the valid values: introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, vocabLevel3, reading, speakReading, readAlong, writingSentence, writingParagraph.
3. WHEN a viewFlashcards or speakFlashcards activity is created for the same session, THE two activities SHALL have identical `vocabList` arrays.
4. THE `vocabList` field SHALL be an array of lowercase strings — never objects, numbers, or the field name `words`.
5. All content data SHALL be inside the `data` object — never inline on the activity object.
6. THE Curriculum content SHALL NOT include any Strip_Keys: mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId.
7. THE Curriculum content SHALL include `contentTypeTags` as a top-level field set to `[]`.

### Requirement 13: Series Display Order and Collection Assembly

**User Story:** As a content manager, I want all series and curriculums to have explicit display orders and be properly linked to the collection, so that the content appears in a logical sequence in the client app.

#### Acceptance Criteria

1. Each Series SHALL have an explicit display order within the Collection.
2. Each Curriculum SHALL have an explicit display order within its Series.
3. THE Series display order SHALL follow a logical pedagogical progression: Microeconomics → Macroeconomics → International Trade → Accounting & Corporate Finance → Marketing & Management.
4. WITHIN each Series, Curriculums SHALL be ordered from foundational topics to more specialized topics.
5. WHEN a Curriculum is added to a Series, THE Platform SHALL set its display order via the `curriculum/setDisplayOrder` endpoint.

### Requirement 14: Creation Workflow and No Templated Content

**User Story:** As a content manager, I want each curriculum created via a separate Python script with no templated content, so that every piece of learner-facing text is individually crafted for its specific economics topic.

#### Acceptance Criteria

1. Each Curriculum SHALL be created via a separate standalone Python script.
2. Each script SHALL use `firebase_token.get_firebase_id_token()` for authentication and the `curriculum/create` API endpoint.
3. THE `curriculum/create` call SHALL include `language` and `userLanguage` as top-level body parameters (not only inside content JSON).
4. THE Creation_Script SHALL NOT use template functions, string interpolation, or loops to generate learner-facing text (introAudio, descriptions, previews, reading passages, writing prompts).
5. THE Creation_Script MAY use shared helper functions for activity structure (types, order, data schema).
6. Newly created curriculums SHALL remain private (no call to `setPublic` with `isPublic: true`).
7. WHEN all curriculums in a Series are created, an orchestrator script SHALL create the Series, add curriculums, set display orders, and add the Series to the Collection.

### Requirement 15: Post-Creation Verification

**User Story:** As a content manager, I want each curriculum verified against content corruption rules after creation, so that no malformed content reaches the platform.

#### Acceptance Criteria

1. WHEN a curriculum is created, THE Creation_Script SHALL verify the response contains a valid curriculum ID.
2. WHEN a curriculum is created, THE Creation_Script SHALL check for duplicates by querying: `SELECT id, title, created_at FROM curriculum WHERE title = '<title>' AND uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73' ORDER BY created_at`.
3. IF duplicates are found, THE Creation_Script SHALL keep the earliest and delete extras.
4. THE Creation_Script SHALL verify the created content against corruption rules: correct `activityType` field names, `vocabList` not `words`, data inside `data` object, matching vocabLists for viewFlashcards/speakFlashcards in the same session.

### Requirement 16: Documentation and Cleanup

**User Story:** As a content manager, I want proper documentation after all curriculums are created, so that the content is traceable and reproducible.

#### Acceptance Criteria

1. WHEN all curriculums in the collection are created, THE workspace SHALL contain a README.md documenting: collection ID, all series IDs, all curriculum IDs and titles, creation method, SQL queries for retrieval, and recreation context.
2. WHEN all curriculums are verified in the database, THE source Python scripts SHALL be deleted from the workspace, leaving only the README.
3. THE README SHALL include the full topic plan: which curriculums belong to which series, with their display orders.
