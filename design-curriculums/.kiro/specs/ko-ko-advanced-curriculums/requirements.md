# Requirements Document

## Introduction

Create 20 ko-ko advanced-level curriculums for Korean native speakers learning advanced Korean vocabulary. The language pair is `language="ko"`, `userLanguage="ko"` (single-language — all text in Korean). Each curriculum has 5 sessions with 6+ vocabulary words per session (30+ total per curriculum), following the ja-ja advanced pair structural template.

The 20 curriculums are organized into logical series (3-5 curriculums per series), with series grouped into collections. This follows the Collection → Series → Curriculums hierarchy.

### Language & Level

- **Language pair:** ko-ko (`language: "ko"`, `userLanguage: "ko"`)
- **Level:** Advanced (single-language only — all text in Korean)
- **contentTypeTags:** `[]` (concept-based, no media source)

### Curriculum Structure (All 20 Curriculums)

Each curriculum has 5 learning sessions with balanced skills (reading, listening, speaking, writing) in every session:

- **30+ vocabulary words total per curriculum** (6+ per session)
- **Long reading passages** (800-1200+ words equivalent in Korean)
- **Multiple writing activities per session** (both sentence-level and paragraph-level)
- **Extended introAudio scripts** (500-800 words equivalent for vocabulary teaching)
- **Balanced activity types in every session:** introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence, writingParagraph, introAudio (farewell)

### Topic Diversity (20 Curriculums across 5 Series)

The 20 curriculums cover diverse topics appropriate for Korean native speakers expanding their advanced vocabulary:

**Series A: 비즈니스·전문 한국어 (Business & Professional Korean)** — 4 curriculums
1. 협상과 설득 (Negotiation & Persuasion)
2. 조직 리더십 (Organizational Leadership)
3. 전략적 의사결정 (Strategic Decision-Making)
4. 기업 윤리와 지배구조 (Corporate Ethics & Governance)

**Series B: 학술·사상 (Academic & Intellectual Thought)** — 4 curriculums
5. 인식론과 지식의 구조 (Epistemology & the Structure of Knowledge)
6. 정치철학 (Political Philosophy)
7. 언어와 사고 (Language & Thought)
8. 과학철학과 방법론 (Philosophy of Science & Methodology)

**Series C: 문화·예술 (Culture & Arts)** — 4 curriculums
9. 문학비평과 해석 (Literary Criticism & Interpretation)
10. 한국 미학과 예술론 (Korean Aesthetics & Art Theory)
11. 현대 미디어와 서사 (Contemporary Media & Narrative)
12. 공연예술과 무대 (Performing Arts & the Stage)

**Series D: 사회·심리 (Society & Psychology)** — 4 curriculums
13. 사회심리학 (Social Psychology)
14. 자기성찰과 정체성 (Self-Reflection & Identity)
15. 도시와 공간의 사회학 (Sociology of Cities & Space)
16. 세대론과 문화 갈등 (Generational Theory & Cultural Conflict)

**Series E: 과학·기술·건강 (Science, Technology & Health)** — 4 curriculums
17. 인공지능과 인간 (AI & Humanity)
18. 기후변화와 환경윤리 (Climate Change & Environmental Ethics)
19. 뇌과학과 인지 (Neuroscience & Cognition)
20. 예방의학과 웰니스 (Preventive Medicine & Wellness)

### Organization Hierarchy

- **1 Collection:** 한국어 고급 어휘 마스터 (Advanced Korean Vocabulary Mastery)
- **5 Series:** A through E (4 curriculums each)
- **20 Curriculums:** Distributed across the 5 series

### What This Spec Covers

- Creation of 20 new ko-ko advanced curriculums
- One Python script per curriculum
- One orchestrator script for collection/series/displayOrder setup
- Persuasive copy descriptions with 6-tone palette variety (all in Korean)
- Post-creation verification and duplicate checking
- Source cleanup after successful creation (keep only README.md)

### What This Spec Does NOT Cover

- Making any curriculum public
- Audio/illustration generation pipeline
- Client-side UI changes
- Pricing

## Glossary

- **Curriculum**: A single learning unit with vocabulary words, sessions, and activities, stored as JSON content in the database.
- **Session**: An ordered segment within a curriculum containing a sequence of activities.
- **Activity**: An individual learning exercise within a session (introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence, writingParagraph).
- **Collection**: A top-level organizational container that groups related series together.
- **Series**: A mid-level organizational container that groups related curriculums together within a collection.
- **Creation_Script**: A standalone Python script that calls the helloapi REST API to create a single curriculum.
- **Orchestrator_Script**: A Python script that creates collections, series, wires them together, and sets display orders.
- **Strip_Keys**: The set of auto-generated platform keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId) that must never appear in new content.
- **Persuasive_Copy**: The required emotional sales copy style for all learner-facing text, following the 5-beat structure defined in CURRICULUM_QUALITY_STANDARDS.md.
- **VocabList**: An array of lowercase strings on vocab activities listing the vocabulary words for that activity.
- **Balanced_Skills**: The requirement that each session includes reading, listening (readAlong/introAudio), speaking (speakFlashcards/speakReading), and writing (writingSentence/writingParagraph) activities.
- **Tone_Palette**: The 6 rhetorical opener types (provocative_question, bold_declaration, vivid_scenario, empathetic_observation, surprising_fact, metaphor_led) used to vary description style.
- **Farewell_Tone**: The 5 emotional registers for farewell scripts (introspective_guide, warm_accountability, team_building_energy, quiet_awe, practical_momentum).

## Requirements

### Requirement 1: Collection and Series Organization

**User Story:** As a content manager, I want the 20 ko-ko advanced curriculums organized into a clear Collection → Series → Curriculums hierarchy, so that learners can browse topics logically and the catalog is well-structured.

#### Acceptance Criteria

1. THE Orchestrator_Script SHALL create exactly 1 collection with a Korean title and informative Korean description.
2. THE Orchestrator_Script SHALL create exactly 5 series, each with a Korean title and a Korean description of 255 characters or fewer.
3. THE Orchestrator_Script SHALL wire all 5 series to the collection using the `curriculum-collection/addSeriesToCollection` API.
4. THE Orchestrator_Script SHALL set display orders on the collection (1), on each series (1-5), and on each curriculum within its series (1-4).
5. WHEN curriculums are added to series, THE Orchestrator_Script SHALL call `curriculum/setDisplayOrder` for each curriculum to set its position within the series.
6. THE Series descriptions SHALL use varied tones from the 6-tone palette, with no two adjacent series sharing the same tone.
7. THE Collection description SHALL be a short informative Korean summary (not persuasive copy).

### Requirement 2: Curriculum Content Structure

**User Story:** As a content manager, I want each of the 20 ko-ko curriculums to follow the established 5-session, 11-activity-per-session structure, so that learners get consistent, balanced skills practice across all curriculums.

#### Acceptance Criteria

1. EACH Curriculum SHALL contain exactly 5 learningSessions, each with Balanced_Skills coverage (reading, listening, speaking, and writing activities).
2. WHEN each session is created, THE Session SHALL include exactly 11 activities in this order: introAudio (vocabulary teaching), viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence, writingParagraph, introAudio (farewell/wrap-up).
3. EACH Curriculum SHALL contain at least 30 Korean vocabulary words distributed across 5 sessions (6+ words per session).
4. THE Curriculum content SHALL include `contentTypeTags: []` (empty array).
5. THE Curriculum content SHALL NOT include a `youtubeUrl` field.
6. THE Curriculum SHALL set `language: "ko"` and `userLanguage: "ko"` as top-level body parameters in the API call.
7. THE Curriculum SHALL use Korean for all user-facing text (title, description, preview, introAudio scripts, writing prompts, reading passages).
8. THE Session titles SHALL follow the pattern "세션 1", "세션 2", etc.

### Requirement 3: Vocabulary Requirements

**User Story:** As a content manager, I want each curriculum to have a distinct set of advanced Korean vocabulary words with no overlap within the same series, so that learners build a broad vocabulary without redundancy.

#### Acceptance Criteria

1. WHEN a `viewFlashcards`, `speakFlashcards`, `vocabLevel1`, or `vocabLevel2` activity is created, THE Activity SHALL include a `vocabList` field containing an array of lowercase strings listing the vocabulary words for that activity.
2. THE `vocabList` field SHALL contain at least 6 words per activity (matching the vocabulary group for that session).
3. THE `vocabList` SHALL use the field name `vocabList` — never `words`.
4. THE `vocabList` values SHALL be lowercase strings (Korean words in hangul).
5. WHEN viewFlashcards and speakFlashcards appear in the same session, THE Activities SHALL have identical vocabList arrays.
6. THE Vocabulary words within the same series SHALL NOT overlap — each curriculum in a series SHALL have a completely distinct vocabulary set.
7. THE Vocabulary words SHALL be advanced-level Korean appropriate for native speakers expanding their formal, academic, or specialized vocabulary.

### Requirement 4: Activity Metadata and Titles

**User Story:** As a content manager, I want every activity to have proper Korean titles and descriptions following consistent naming patterns, so that the platform displays activities correctly in Korean.

#### Acceptance Criteria

1. THE Activity SHALL include `title` and `description` fields for every activity in every session.
2. WHEN a `viewFlashcards`, `speakFlashcards`, `vocabLevel1`, or `vocabLevel2` activity is created, THE Activity title SHALL follow the format "플래시카드: 〈topic〉" and the description SHALL list the words being learned.
3. WHEN a `reading` or `speakReading` activity is created, THE Activity title SHALL follow the format "읽기: 〈topic〉" and the description SHALL summarize the passage content.
4. WHEN a `readAlong` activity is created, THE Activity title SHALL follow the format "듣기: 〈topic〉" and the description SHALL indicate the learner is listening to the passage.
5. WHEN an `introAudio` activity is created, THE Activity title SHALL be a descriptive Korean label and the description SHALL be a brief Korean summary.
6. WHEN a `writingSentence` or `writingParagraph` activity is created, THE Activity title SHALL follow the format "쓰기: 〈topic〉" and the description SHALL summarize the writing task.
7. THE Session object SHALL include a `title` field following the pattern "세션 1", "세션 2", etc.

### Requirement 5: Content Quality — Persuasive Copy in Korean

**User Story:** As a content manager, I want all learner-facing text to follow the persuasive copy style with tone variety, written entirely in Korean, so that Korean-speaking learners feel emotionally engaged.

#### Acceptance Criteria

1. THE Curriculum description SHALL follow the 5-beat persuasive copy structure in Korean: bold ALL-CAPS-equivalent headline (using emphasis markers), concrete personal examples, vivid metaphor, transformation promise, and dual growth tie-in (vocabulary + thinking).
2. THE Curriculum preview (~150 words equivalent in Korean) SHALL open with a vivid hook, name the vocabulary words, describe the learning journey, and read as compelling Korean marketing copy.
3. WHEN introAudio vocabulary teaching scripts are created (one per session), EACH script (500-800 words equivalent) SHALL teach each vocabulary word individually with part of speech, definition, example sentence from the reading context, and smooth transitions — all in Korean.
4. WHEN the final session's farewell introAudio script is created, THE script SHALL review 5-6 key vocabulary words with definitions and fresh example sentences, connect words back to the curriculum theme, and close with a warm personal sign-off — all in Korean.
5. THE 20 curriculum descriptions SHALL use all 6 tones from the Tone_Palette distributed evenly (no single tone exceeding 30% of the 20 descriptions).
6. THE 20 farewell introAudio scripts SHALL use all 5 Farewell_Tone registers distributed across the curriculums.
7. WITHIN each series, adjacent curriculum descriptions SHALL use different tones.

### Requirement 6: Writing Activities — Sentence and Paragraph

**User Story:** As a content manager, I want writing activities to have properly structured data with Korean prompts, so that the platform can present clear writing exercises to Korean learners.

#### Acceptance Criteria

1. WHEN a `writingSentence` activity is created, THE Activity data SHALL include `vocabList` (array of lowercase strings), and `items` (array where each item has `prompt` and `targetVocab` fields, all in Korean).
2. WHEN a `writingParagraph` activity is created, THE Activity data SHALL include `vocabList` (array of lowercase strings), `instructions` (non-empty Korean string), and `prompts` (array of Korean strings with length >= 2).
3. THE writingSentence prompts SHALL specify context for using the target word in Korean and include a Korean example sentence showing correct usage.
4. THE writingParagraph prompts SHALL be specific to the session's topic and guide the learner to use vocabulary in meaningful analytical writing in Korean.

### Requirement 7: Reading and Audio Activities

**User Story:** As a content manager, I want reading and audio activities to have substantial Korean text content, so that learners get extended exposure to vocabulary in context.

#### Acceptance Criteria

1. WHEN a `reading`, `speakReading`, or `readAlong` activity is created, THE Activity data SHALL include a `text` field containing a non-empty Korean string.
2. WHEN an `introAudio` activity is created, THE Activity data SHALL include a `text` field containing a non-empty Korean string.
3. THE reading activity text SHALL be 800-1200+ words equivalent of original Korean content relevant to the session's theme.
4. THE speakReading and readAlong activities in the same session SHALL use the same text as the reading activity.

### Requirement 8: Strip-Keys Compliance

**User Story:** As a content manager, I want new curriculum content to never include auto-generated platform keys, so that the platform correctly generates fresh metadata after upload.

#### Acceptance Criteria

1. THE Curriculum content SHALL NOT include any of the following auto-generated keys: `mp3Url`, `illustrationSet`, `chapterBookmarks`, `segments`, `whiteboardItems`, `userReadingId`, `lessonUniqueId`, `curriculumTags`, `taskId`, `imageId`.
2. IF an existing curriculum is fetched via API to use as a structural template, THEN THE Creation_Script SHALL strip all auto-generated keys from the fetched content before using it as input for `curriculum/create`.

### Requirement 9: Privacy — All Curriculums Created Private

**User Story:** As a content manager, I want all newly created curriculums to be private by default, so that they go through content generation (audio, illustrations) before being exposed to learners.

#### Acceptance Criteria

1. WHEN a curriculum is created via `curriculum/create`, THE Curriculum SHALL have `is_public: false` (the platform default).
2. THE Creation_Script SHALL NOT call `curriculum/setPublic` with `isPublic: true` on any newly created curriculum.

### Requirement 10: Script Organization and Cleanup

**User Story:** As a content manager, I want one Python script per curriculum plus one orchestrator script, with proper cleanup after creation, so that each curriculum's content is self-contained and the workspace stays clean.

#### Acceptance Criteria

1. THE Creation_Script architecture SHALL use one Python script per curriculum with all text content hand-written in that script.
2. THE Creation_Script SHALL NOT use template functions, string interpolation, or loops to generate learner-facing text content.
3. THE workspace SHALL contain a dedicated folder `ko-ko-advanced-curriculums/` for the project.
4. THE workspace SHALL contain one orchestrator script (`orchestrator.py`) that creates the collection, series, wires them together, and sets display orders.
5. WHEN all 20 curriculums are successfully created and verified in the database, THE source Python scripts SHALL be deleted, leaving only a README.md with creation method, curriculum IDs, SQL queries, and recreation context.

### Requirement 11: No Templated Content

**User Story:** As a content manager, I want every piece of learner-facing text to be individually crafted per curriculum, so that each curriculum reads as if written by a Korean subject-matter expert who deeply understands the specific topic.

#### Acceptance Criteria

1. THE Creation_Script SHALL NOT use `f-string` interpolation, template functions, or shared text skeletons to generate introAudio scripts, reading passages, descriptions, previews, or writing prompts.
2. EACH Curriculum's reading passages SHALL be original Korean content exploring the topic from a unique angle — not adaptations or rewrites of another curriculum's passages.
3. EACH Curriculum's introAudio scripts SHALL be individually crafted to teach vocabulary in a way that resonates with the specific topic's intellectual framework.
4. THE Vocabulary words across curriculums within the same series SHALL NOT overlap — each curriculum SHALL have a distinct vocabulary set.

### Requirement 12: Duplicate Check After Creation

**User Story:** As a content manager, I want to check for duplicate curriculums after creation, so that accidental re-runs of scripts do not create duplicate entries.

#### Acceptance Criteria

1. WHEN a curriculum is created, THE Creation_Script SHALL query the database for curriculums with the same title owned by the same user.
2. IF duplicates are found, THEN THE Creation_Script SHALL report the duplicates and keep the earliest-created one.

### Requirement 13: Content Corruption Compliance

**User Story:** As a content manager, I want all curriculum content to pass the content corruption detection rules, so that the platform renders activities correctly without data integrity issues.

#### Acceptance Criteria

1. THE Curriculum content SHALL have a top-level structure with `title` (non-empty string), `description` (non-empty string), `preview` (object with `text` as non-empty string), and `learningSessions` (array with length = 5).
2. EACH Activity SHALL use the field name `activityType` — never `type`.
3. EACH Activity SHALL have a `data` field (object) containing all content fields — content fields SHALL NOT be placed inline on the activity object.
4. THE `activityType` values SHALL be one of: `introAudio`, `viewFlashcards`, `speakFlashcards`, `vocabLevel1`, `vocabLevel2`, `reading`, `speakReading`, `readAlong`, `writingSentence`, `writingParagraph`.

### Requirement 14: Inline Validation

**User Story:** As a content manager, I want each creation script to validate content structure before uploading, so that malformed content is caught before it reaches the database.

#### Acceptance Criteria

1. EACH Creation_Script SHALL include an inline `validate_content()` function that checks structural integrity before the API call.
2. THE `validate_content()` function SHALL verify: 5 sessions, 11 activities per session in correct order, vocabList consistency between viewFlashcards and speakFlashcards, reading text presence and minimum length, no strip keys, no `youtubeUrl`, `contentTypeTags` is `[]`, all activities have `activityType`/`title`/`description`/`data`.
3. IF validation fails, THEN THE Creation_Script SHALL raise a ValueError with a specific error message and exit before making the API call.

### Requirement 15: Topic Diversity and Series Coherence

**User Story:** As a content manager, I want the 20 curriculums to cover diverse intellectual topics while maintaining coherence within each series, so that the collection appeals to a broad audience of advanced Korean learners.

#### Acceptance Criteria

1. THE 20 curriculums SHALL cover at least 5 distinct topic domains: business/professional, academic/philosophy, culture/arts, society/psychology, and science/technology/health.
2. EACH Series SHALL contain curriculums that share a coherent thematic thread (e.g., all business-related, all arts-related).
3. THE Curriculum titles SHALL be minimal (the series provides context) and SHALL NOT include difficulty level indicators.
4. THE Reading passages across all 20 curriculums SHALL explore diverse themes appropriate for educated Korean adults expanding their formal and specialized vocabulary.

### Requirement 16: Curriculum Title Conventions

**User Story:** As a content manager, I want curriculum titles to be minimal and in Korean, so that the series context provides the framing and titles remain clean.

#### Acceptance Criteria

1. THE Curriculum titles SHALL be written in Korean.
2. THE Curriculum titles SHALL be minimal — the series title provides topic context.
3. THE Curriculum titles SHALL NOT repeat the series name, content type prefix, skill-focus label, or audience suffix.
4. THE Curriculum titles SHALL NOT include difficulty level indicators.
