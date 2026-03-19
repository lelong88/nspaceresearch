# Requirements Document

## Introduction

Expand the "Học Từ Vựng Theo Chủ Đề (Topic-Based Vocabulary)" collection (279d6843) with 4 new thematic series, each containing 4 curriculums. The new series sit alongside the existing "Tâm Lý & Phát Triển Bản Thân" and "Sức Khỏe & Lối Sống" series as peer topic domains. All content targets Vietnamese speakers learning English (vi-en), follows the established 18-word / 5-session structure, and adheres to the platform's persuasive copy and quality standards.

### Proposed Series

1. **Khoa Học & Công Nghệ (Science & Technology)** — Curriculums exploring AI, space exploration, genetic engineering, and quantum computing
2. **Kinh Tế & Tài Chính Cá Nhân (Economics & Personal Finance)** — Curriculums on behavioral economics, investing fundamentals, inflation/monetary policy, and the gig economy
3. **Môi Trường & Phát Triển Bền Vững (Environment & Sustainability)** — Curriculums on climate change, ocean conservation, renewable energy, and sustainable agriculture
4. **Văn Hóa & Xã Hội (Culture & Society)** — Curriculums on social media psychology, cultural intelligence, urbanization, and the future of work

## Glossary

- **Collection**: Top-level organizational shelf in the platform. The target collection is "Học Từ Vựng Theo Chủ Đề" (279d6843).
- **Series**: A thematic grouping within a collection, containing multiple curriculums. Each new series is a peer to the existing Health & Wellness series.
- **Curriculum**: A single learning unit with 18 vocabulary words, 5 sessions (3 learning + 1 review + 1 full reading), and a fixed activity pattern.
- **Session**: One of 5 ordered segments within a curriculum. Learning sessions contain: introAudio ×3, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, vocabLevel3, reading, speakReading, readAlong, writingSentence.
- **Activity**: An individual learning exercise within a session (e.g., introAudio, viewFlashcards, reading).
- **Display_Order**: Integer field controlling the sort position of curriculums within a series and series within a collection.
- **Creation_Script**: A Python script that calls the helloapi REST API to create a curriculum, add it to a series, and set its display order.
- **Strip_Keys**: The process of removing auto-generated platform keys (mp3Url, illustrationSet, segments, etc.) from curriculum content before upload.
- **Persuasive_Copy**: The required emotional sales copy style for all learner-facing text (descriptions, previews, introAudio scripts).
- **API**: The helloapi.step.is REST API used for all CRUD operations on curriculums, series, and collections.

## Requirements

### Requirement 1: Series Creation

**User Story:** As a content manager, I want to create 4 new curriculum series in the Topic-Based Vocabulary collection, so that learners have a broader range of thematic vocabulary domains to explore.

#### Acceptance Criteria

1. WHEN a new series is created, THE API SHALL be called via `curriculum-series/create` with a bilingual title (Vietnamese + English), a persuasive Vietnamese description (under 255 characters), and `isPublic: true`.
2. WHEN a series is created, THE Creation_Script SHALL call `curriculum-collection/addSeriesToCollection` with `curriculumCollectionId: 279d6843` and the new series ID.
3. THE Creation_Script SHALL assign `display_order` values to the 4 new series that place them after the existing series (display_order > 200) via `curriculum-series/setDisplayOrder`.
4. WHEN all 4 series are created, THE Collection SHALL contain exactly 6 series total: the 2 existing series plus the 4 new series.

### Requirement 2: Curriculum Structure Compliance

**User Story:** As a content manager, I want each new curriculum to follow the established 18-word / 5-session structure, so that the learning experience is consistent across the entire collection.

#### Acceptance Criteria

1. THE Curriculum SHALL contain exactly 18 vocabulary words, divided into 3 groups of 6 words across 3 learning sessions.
2. THE Curriculum SHALL contain exactly 5 sessions: Session 1 (learning, words 1–6), Session 2 (learning, words 7–12), Session 3 (learning, words 13–18), Session 4 (review of all 18 words), Session 5 (full reading with all 18 words).
3. WHEN a learning session (Sessions 1–3) is created, THE Session SHALL contain activities in this exact order: introAudio, introAudio, introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, vocabLevel3, reading, speakReading, readAlong, writingSentence.
4. THE Curriculum SHALL set `language: "en"` and `userLanguage: "vi"` as top-level body parameters in the `curriculum/create` API call.
5. WHEN a curriculum is created, THE Creation_Script SHALL pass `language` and `userLanguage` as separate top-level body fields alongside `content`, not only inside the content JSON.

### Requirement 3: Content Quality — Persuasive Copy

**User Story:** As a content manager, I want all learner-facing text to follow the persuasive copy style, so that learners feel emotionally engaged and motivated to start each curriculum.

#### Acceptance Criteria

1. THE Curriculum description SHALL follow the 5-beat persuasive copy structure: bold headline, concrete personal examples, vivid metaphor, transformation promise, and dual growth tie-in.
2. THE Curriculum preview (~150 words) SHALL open with a vivid imaginative hook, name the vocabulary words, describe the learning journey, and read as compelling marketing copy.
3. WHEN an introAudio activity is created for Sessions 1 or 2, THE introAudio script (500–800 words) SHALL teach each vocabulary word individually with part of speech, definition, example sentence from the reading context, and smooth transitions between words.
4. WHEN an introAudio activity is created for Session 3 (review), THE introAudio script SHALL congratulate the learner, recap Sessions 1 and 2 content, explain the review format, and motivate for the full reading.
5. WHEN an introAudio activity is created for Session 5 (farewell), THE introAudio script (400–600 words) SHALL review each vocabulary word with a fresh example sentence and provide a warm farewell.
6. THE Curriculum SHALL use Vietnamese for all user-facing text (title, description, preview, introAudio scripts, writing prompts) and English for reading passages.

### Requirement 4: Content Quality — Writing Prompts

**User Story:** As a content manager, I want writing prompts to be specific and contextual, so that learners practice vocabulary in meaningful, topic-relevant sentences.

#### Acceptance Criteria

1. THE writingSentence activity SHALL provide a detailed prompt specifying the context for using the word, plus an example sentence showing correct usage, in the format: "Use the word 'X' in a sentence about [specific context]. Example: [full example sentence]."
2. THE writingSentence prompt SHALL reference the specific curriculum topic and reading passage context, not use generic fill-in-the-blank templates.

### Requirement 5: Activity Metadata

**User Story:** As a content manager, I want every activity to have proper title and description fields, so that server-side logging and client display work correctly.

#### Acceptance Criteria

1. THE Activity SHALL include both a `title` and `description` field for every activity in every session.
2. WHEN a viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, or vocabLevel3 activity is created, THE Activity title SHALL follow the format "Flashcards: <topic>" and the description SHALL list the words being learned.
3. WHEN a reading or speakReading activity is created, THE Activity title SHALL follow the format "Đọc: <topic>" and the description SHALL contain the first ~80 characters of the reading text.
4. WHEN a readAlong activity is created, THE Activity title SHALL follow the format "Nghe: <topic>" and the description SHALL be "Nghe đoạn văn vừa đọc và theo dõi."
5. WHEN an introAudio activity is created, THE Activity title SHALL be a descriptive label (e.g., "Giới thiệu bài học", "Giới thiệu từ vựng") and the description SHALL be a brief summary.
6. WHEN a writingSentence activity is created, THE Activity title SHALL follow the format "Viết: <topic>" and the description SHALL briefly summarize the writing task.
7. THE Session object SHALL include a `title` field (e.g., "Phần 1", "Phần 2", "Ôn tập").

### Requirement 6: Strip-Keys Compliance

**User Story:** As a content manager, I want new curriculum content to never include auto-generated platform keys, so that the platform correctly generates fresh metadata after upload.

#### Acceptance Criteria

1. THE Curriculum content SHALL NOT include any of the following auto-generated keys: `mp3Url`, `illustrationSet`, `chapterBookmarks`, `segments`, `whiteboardItems`, `userReadingId`, `lessonUniqueId`, `curriculumTags`, `taskId`, `imageId`.
2. IF an existing curriculum is fetched via API to use as a structural template, THEN THE Creation_Script SHALL run `strip_keys()` on the fetched content before using it as input for `curriculum/create`.

### Requirement 7: Display Order and Organization

**User Story:** As a content manager, I want curriculums and series to have explicit display orders, so that they appear in the intended sequence in the client app.

#### Acceptance Criteria

1. WHEN a curriculum is added to a series via `curriculum-series/addCurriculum`, THE Creation_Script SHALL call `curriculum/setDisplayOrder` to assign a sequential integer display order (0, 1, 2, 3) for the 4 curriculums within each series.
2. THE Creation_Script SHALL assign display_order values to the 4 new series (300, 400, 500, 600) so they sort after the existing series (display_order 100 and 200).
3. WHEN all curriculums are created and ordered, THE Series SHALL contain exactly 4 curriculums each, sorted by display_order.

### Requirement 8: Script Organization

**User Story:** As a content manager, I want one Python script per curriculum plus an orchestrator script for series-level setup, so that each curriculum's content is self-contained and files remain manageable.

#### Acceptance Criteria

1. THE Creation_Script architecture SHALL use one Python script per curriculum (e.g., `create_science_1_ai.py`, `create_science_2_space.py`) with all text content hand-written in that script.
2. THE Creation_Script architecture SHALL include one orchestrator script per series that handles series creation, adding curriculums to the series, adding the series to the collection, and setting display orders.
3. THE Creation_Script SHALL NOT use template functions, string interpolation, or loops to generate learner-facing text content.
4. WHEN a curriculum is successfully created and verified in the database, THE source script SHALL be deleted, leaving only a README with creation method, SQL queries, and recreation context.

### Requirement 9: No Templated Content

**User Story:** As a content manager, I want every piece of learner-facing text to be individually crafted, so that each curriculum reads as if written by a subject-matter expert for that specific topic.

#### Acceptance Criteria

1. THE Creation_Script SHALL NOT use `f-string` interpolation, template functions, or shared text skeletons to generate introAudio scripts, reading passages, descriptions, previews, or writing prompts.
2. THE Creation_Script MAY use shared helper functions for activity structure (types, order, data schema) but SHALL hand-write all text content per curriculum.

### Requirement 10: Language and Level Homogeneity

**User Story:** As a content manager, I want all curriculums in the new series to share the same language pair and similar difficulty levels, so that the collection remains internally consistent.

#### Acceptance Criteria

1. THE Curriculum SHALL set `language: "en"` and `userLanguage: "vi"` for every curriculum across all 4 new series.
2. THE Series SHALL contain curriculums within a maximum 1-level gap from the highest-level curriculum in that series.
3. THE Series title and description SHALL be written in Vietnamese with English topic names, consistent with the bilingual convention for vi-en content.

### Requirement 11: Series Content — Khoa Học & Công Nghệ (Science & Technology)

**User Story:** As a learner, I want a Science & Technology vocabulary series, so that I can learn English vocabulary related to cutting-edge scientific and technological topics.

#### Acceptance Criteria

1. THE Series SHALL contain 4 curriculums covering: (a) Artificial Intelligence & Machine Learning, (b) Space Exploration & The New Space Race, (c) Genetic Engineering & CRISPR, (d) Quantum Computing & The Future of Processing.
2. THE Series title SHALL be "Khoa Học & Công Nghệ (Science & Technology)" with a description under 255 characters.
3. WHEN each curriculum is created, THE Curriculum SHALL contain 18 domain-specific English vocabulary words relevant to the specific sub-topic.

### Requirement 12: Series Content — Kinh Tế & Tài Chính Cá Nhân (Economics & Personal Finance)

**User Story:** As a learner, I want an Economics & Personal Finance vocabulary series, so that I can learn English vocabulary related to economic concepts and financial literacy.

#### Acceptance Criteria

1. THE Series SHALL contain 4 curriculums covering: (a) Behavioral Economics & Decision-Making, (b) Investing Fundamentals & Compound Growth, (c) Inflation, Central Banks & Monetary Policy, (d) The Gig Economy & Future of Employment.
2. THE Series title SHALL be "Kinh Tế & Tài Chính Cá Nhân (Economics & Personal Finance)" with a description under 255 characters.
3. WHEN each curriculum is created, THE Curriculum SHALL contain 18 domain-specific English vocabulary words relevant to the specific sub-topic.

### Requirement 13: Series Content — Môi Trường & Phát Triển Bền Vững (Environment & Sustainability)

**User Story:** As a learner, I want an Environment & Sustainability vocabulary series, so that I can learn English vocabulary related to environmental science and sustainable development.

#### Acceptance Criteria

1. THE Series SHALL contain 4 curriculums covering: (a) Climate Change & The Carbon Cycle, (b) Ocean Conservation & Marine Ecosystems, (c) Renewable Energy & The Grid Transition, (d) Sustainable Agriculture & Food Systems.
2. THE Series title SHALL be "Môi Trường & Phát Triển Bền Vững (Environment & Sustainability)" with a description under 255 characters.
3. WHEN each curriculum is created, THE Curriculum SHALL contain 18 domain-specific English vocabulary words relevant to the specific sub-topic.

### Requirement 14: Series Content — Văn Hóa & Xã Hội (Culture & Society)

**User Story:** As a learner, I want a Culture & Society vocabulary series, so that I can learn English vocabulary related to social dynamics, cultural phenomena, and modern life.

#### Acceptance Criteria

1. THE Series SHALL contain 4 curriculums covering: (a) Social Media Psychology & Digital Wellbeing, (b) Cultural Intelligence & Cross-Cultural Communication, (c) Urbanization & The Future of Cities, (d) The Future of Work & Automation.
2. THE Series title SHALL be "Văn Hóa & Xã Hội (Culture & Society)" with a description under 255 characters.
3. WHEN each curriculum is created, THE Curriculum SHALL contain 18 domain-specific English vocabulary words relevant to the specific sub-topic.

### Requirement 15: Folder and README Structure

**User Story:** As a content manager, I want each series to have its own folder with a README tracking creation details, so that content is recoverable and auditable.

#### Acceptance Criteria

1. WHEN a new series is created, THE workspace SHALL contain a dedicated folder for that series (e.g., `science-technology-series/`, `economics-finance-series/`).
2. WHEN all curriculums in a series are successfully created, THE folder SHALL contain a README.md documenting: series ID, curriculum IDs and titles, how content was created, SQL queries to find the curriculums in the DB, and enough context to recreate if needed.
3. WHEN all curriculums are verified in the database, THE source Python scripts SHALL be deleted from the folder, leaving only the README.
