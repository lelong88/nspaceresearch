# Requirements Document

## Introduction

Create a vi-en curriculum series inspired by the viral Vietnamese social media trend "Nếu cả cuộc đời này không rực rỡ thì sao?" (What if your whole life isn't brilliant?). The series targets Vietnamese office workers (nhân viên bình thường) at the intermediate English level who may feel stuck or question their career path.

### Critical Framing

This curriculum is NOT about accepting an ordinary life or resignation. The philosophy is: **accurate self-awareness → identify core values → grow from there**. It's about seeing yourself clearly, understanding what truly matters to you, and using that clarity as a launchpad for meaningful growth. The Vietnamese trend is the cultural entry point, but the content draws from Western psychology, Eastern philosophy, and real workplace scenarios.

### Curriculum Topics (6 Curriculums)

1. **Tự Nhận Thức (Self-Awareness vs. Self-Deception)** — How cognitive biases, defense mechanisms, and social comparison distort self-perception. Drawing from Daniel Kahneman, Tasha Eurich, and the Johari Window model. The foundation: you can't grow from a place you can't see clearly.

2. **Giá Trị Cốt Lõi (Core Values vs. External Expectations)** — How to distinguish your authentic values from family pressure, social media comparison, and cultural "should"s. Drawing from Brené Brown, Acceptance and Commitment Therapy (ACT), and Vietnamese cultural dynamics around filial piety and collective success.

3. **Hài Lòng vs. Tự Mãn (Contentment vs. Complacency)** — The critical difference between healthy satisfaction and stagnation. Drawing from Stoic philosophy (Seneca, Marcus Aurelius), Buddhist concept of santuṭṭhi, and modern positive psychology research on hedonic adaptation.

4. **Tư Duy Phát Triển Trung Thực (Growth Mindset Rooted in Honest Self-Assessment)** — Why growth mindset without self-honesty becomes toxic positivity. Drawing from Carol Dweck's nuanced later work, Kristin Neff's self-compassion research, and the Japanese concept of hansei (反省).

5. **Ý Nghĩa Trong Công Việc (Finding Meaning in Work Without Being "Extraordinary")** — How ordinary work becomes meaningful through craftsmanship, connection, and contribution. Drawing from Viktor Frankl, Amy Wrzesniewski's job crafting research, and the Japanese concept of ikigai as daily purpose (not grand destiny).

6. **Góc Nhìn Văn Hóa (Cultural Perspectives on Success and Fulfillment)** — How Vietnamese, Western, and East Asian cultures define success differently, and how to build a personal definition. Drawing from cross-cultural psychology, Hofstede's dimensions, and real contrasts between Vietnamese collectivism and Western individualism.

### Language Pair & Level

- **Language pair:** vi-en (`language: "en"`, `userLanguage: "vi"`)
- **Level:** Intermediate — Vietnamese office workers with some English ability
- **User-facing text:** Vietnamese (title, description, preview.text, introAudio scripts, writing prompts, activity titles/descriptions)
- **Reading passages:** English (intermediate level — words they'd encounter in TED talks, business books, self-help content, professional development)
- **contentTypeTags:** `[]` (empty — not movie/music/podcast/story)

### Curriculum Structure (All 6 Curriculums)

Each curriculum has 18 vocabulary words in 3 groups of 6, spread across 4 sessions. Activity counts per session: 12, 12, 12, 9.

**Sessions 1-3 (teaching sessions):** Each teaches 1 group of 6 words. Activity order: introAudio (topic intro), introAudio (vocabulary teaching, 500-800 words), viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence, writingSentence, writingParagraph.

**Session 4 (review + farewell):** 9 activities — introAudio (review intro), viewFlashcards (all 18), speakFlashcards (all 18), reading (full article combining all themes), speakReading, readAlong, writingSentence, writingParagraph, introAudio (farewell reviewing 5-6 key words).

### Series Organization

The 6 curriculums are organized into a single series with a Vietnamese title and description (≤ 255 chars). The series is NOT made public — it needs content generation first.

### Vocabulary Philosophy

Words should be practical and intellectually enriching — the kind Vietnamese office workers would encounter in TED talks, business books, self-help podcasts, and professional development content. Think: "introspection", "complacency", "resilience", "authenticity" — not academic jargon, but words that upgrade both thinking and English ability.

### What This Spec Covers

- Creation of 6 vi-en curriculums (one per topic)
- Creation of 1 series to group all 6 curriculums
- Display order assignment for all curriculums within the series
- Post-creation verification and duplicate checking
- Source material cleanup after successful creation
- README documentation

### What This Spec Does NOT Cover

- Making any curriculum or series public
- Adding to existing collections (to be determined after creation)
- Client-side UI changes
- Content generation pipeline (audio, illustrations)
- en-en versions of these curriculums

## Glossary

- **Curriculum**: A single learning unit with vocabulary words, sessions, and activities, stored as JSON content in the database.
- **Series**: A grouping of related curriculums within a collection. Has title (≤ 255 chars) and description (≤ 255 chars).
- **Session**: An ordered segment within a curriculum containing a sequence of activities.
- **Activity**: An individual learning exercise within a session (introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence, writingParagraph).
- **Creation_Script**: A standalone Python script that calls the helloapi REST API to create a single curriculum.
- **Strip_Keys**: The set of auto-generated platform keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId) that must never appear in new content.
- **Display_Order**: Integer field controlling sort position of curriculums within a series or collections within the platform.
- **Persuasive_Copy**: The required emotional sales copy style for all learner-facing text, following the 5-beat structure defined in CURRICULUM_QUALITY_STANDARDS.md.
- **VocabList**: An array of lowercase strings on vocab activities listing the vocabulary words for that activity.
- **Ordinary_Life_Philosophy**: The curriculum's core framing — not resignation or acceptance of mediocrity, but accurate self-awareness leading to values-driven growth. Rooted in the Vietnamese trend "Nếu cả cuộc đời này không rực rỡ thì sao?"
- **Office_Worker_Learner**: The target audience — Vietnamese nhân viên bình thường (regular office workers), not managers, in the middle of their careers, intermediate English level.

## Requirements

### Requirement 1: Self-Awareness vs. Self-Deception Curriculum

**User Story:** As a Vietnamese office worker learning English, I want to explore the psychology of self-awareness through English vocabulary, so that I can see myself more clearly while building language skills I'd use in TED talks and professional development content.

#### Acceptance Criteria

1. THE Curriculum SHALL contain exactly 18 English vocabulary words in 3 groups of 6, all related to self-awareness, cognitive biases, defense mechanisms, and honest self-perception. Words SHALL be at the intermediate level — practical vocabulary found in TED talks, business books, and self-help content (e.g., "introspection", "bias", "denial", "perception", "rationalize", "authentic").
2. THE Curriculum SHALL contain exactly 4 sessions with activity counts: S1 = 12, S2 = 12, S3 = 12, S4 = 9.
3. WHEN Sessions 1-3 are created, EACH Session SHALL contain activities in this exact order: introAudio (topic intro), introAudio (vocabulary teaching, 500-800 words), viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence, writingSentence, writingParagraph.
4. WHEN Session 4 is created, THE Session SHALL contain activities in this exact order: introAudio (review intro), viewFlashcards (all 18 words), speakFlashcards (all 18 words), reading (full article), speakReading, readAlong, writingSentence, writingParagraph, introAudio (farewell reviewing 5-6 key words).
5. THE Curriculum content SHALL include `contentTypeTags: []` (empty array).
6. THE Curriculum SHALL set `language: "en"` and `userLanguage: "vi"` as top-level body parameters in the API call.
7. THE Curriculum SHALL use Vietnamese for user-facing text (title, description, preview, introAudio scripts, writing prompts, activity titles/descriptions) and English for reading passages and vocabulary target words.
8. THE Reading passages SHALL draw from concepts by Daniel Kahneman (cognitive biases), Tasha Eurich (self-awareness research), and the Johari Window model, written as original educational content at intermediate English level.
9. THE Reading passages SHALL use workplace scenarios that resonate with Vietnamese office workers — performance reviews, team dynamics, career decisions, comparing yourself to colleagues.
10. THE Curriculum description SHALL frame self-awareness as the foundation for growth (not self-criticism), consistent with the Ordinary_Life_Philosophy.

### Requirement 2: Core Values vs. External Expectations Curriculum

**User Story:** As a Vietnamese office worker learning English, I want to explore how to distinguish my authentic values from external pressures through English vocabulary, so that I can make clearer life decisions while building professional English skills.

#### Acceptance Criteria

1. THE Curriculum SHALL contain exactly 18 English vocabulary words in 3 groups of 6, all related to personal values, authenticity, external pressure, and values-driven decision-making. Words SHALL be at the intermediate level (e.g., "authenticity", "conformity", "expectation", "autonomy", "compromise", "fulfillment").
2. THE Curriculum SHALL contain exactly 4 sessions with activity counts: S1 = 12, S2 = 12, S3 = 12, S4 = 9.
3. WHEN Sessions 1-3 are created, EACH Session SHALL contain activities in this exact order: introAudio (topic intro), introAudio (vocabulary teaching, 500-800 words), viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence, writingSentence, writingParagraph.
4. WHEN Session 4 is created, THE Session SHALL contain activities in this exact order: introAudio (review intro), viewFlashcards (all 18 words), speakFlashcards (all 18 words), reading (full article), speakReading, readAlong, writingSentence, writingParagraph, introAudio (farewell reviewing 5-6 key words).
5. THE Curriculum content SHALL include `contentTypeTags: []` (empty array).
6. THE Curriculum SHALL set `language: "en"` and `userLanguage: "vi"` as top-level body parameters in the API call.
7. THE Curriculum SHALL use Vietnamese for user-facing text and English for reading passages and vocabulary target words.
8. THE Reading passages SHALL draw from Brené Brown's authenticity research, Acceptance and Commitment Therapy (ACT) values work, and Vietnamese cultural dynamics around filial piety (hiếu thảo) and collective success expectations.
9. THE Reading passages SHALL include scenarios specific to Vietnamese office workers — family pressure to choose "stable" careers, comparing salaries with peers, social media highlight reels, the tension between personal dreams and family obligations.
10. THE Curriculum description SHALL frame values clarification as empowering (not rebellious against family/culture), consistent with the Ordinary_Life_Philosophy.

### Requirement 3: Contentment vs. Complacency Curriculum

**User Story:** As a Vietnamese office worker learning English, I want to understand the difference between healthy satisfaction and stagnation through English vocabulary, so that I can find peace without losing ambition while improving my English.

#### Acceptance Criteria

1. THE Curriculum SHALL contain exactly 18 English vocabulary words in 3 groups of 6, all related to contentment, complacency, satisfaction, ambition, and the psychology of enough. Words SHALL be at the intermediate level (e.g., "complacency", "contentment", "stagnation", "gratitude", "ambition", "adaptation").
2. THE Curriculum SHALL contain exactly 4 sessions with activity counts: S1 = 12, S2 = 12, S3 = 12, S4 = 9.
3. WHEN Sessions 1-3 are created, EACH Session SHALL contain activities in this exact order: introAudio (topic intro), introAudio (vocabulary teaching, 500-800 words), viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence, writingSentence, writingParagraph.
4. WHEN Session 4 is created, THE Session SHALL contain activities in this exact order: introAudio (review intro), viewFlashcards (all 18 words), speakFlashcards (all 18 words), reading (full article), speakReading, readAlong, writingSentence, writingParagraph, introAudio (farewell reviewing 5-6 key words).
5. THE Curriculum content SHALL include `contentTypeTags: []` (empty array).
6. THE Curriculum SHALL set `language: "en"` and `userLanguage: "vi"` as top-level body parameters in the API call.
7. THE Curriculum SHALL use Vietnamese for user-facing text and English for reading passages and vocabulary target words.
8. THE Reading passages SHALL draw from Stoic philosophy (Seneca, Marcus Aurelius), the Buddhist concept of santuṭṭhi (contentment), and modern positive psychology research on hedonic adaptation.
9. THE Reading passages SHALL include workplace scenarios — the colleague who got promoted while you stayed, the question of whether "good enough" is actually good enough, the Sunday-night dread cycle.
10. THE Curriculum description SHALL frame contentment as a strategic choice (not laziness), and complacency as the real danger, consistent with the Ordinary_Life_Philosophy.

### Requirement 4: Growth Mindset Rooted in Honest Self-Assessment Curriculum

**User Story:** As a Vietnamese office worker learning English, I want to explore why growth mindset without self-honesty becomes toxic positivity, so that I can pursue genuine improvement while building English vocabulary for professional contexts.

#### Acceptance Criteria

1. THE Curriculum SHALL contain exactly 18 English vocabulary words in 3 groups of 6, all related to growth mindset, self-compassion, honest assessment, and the difference between toxic positivity and genuine growth. Words SHALL be at the intermediate level (e.g., "resilience", "vulnerability", "compassion", "accountability", "feedback", "plateau").
2. THE Curriculum SHALL contain exactly 4 sessions with activity counts: S1 = 12, S2 = 12, S3 = 12, S4 = 9.
3. WHEN Sessions 1-3 are created, EACH Session SHALL contain activities in this exact order: introAudio (topic intro), introAudio (vocabulary teaching, 500-800 words), viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence, writingSentence, writingParagraph.
4. WHEN Session 4 is created, THE Session SHALL contain activities in this exact order: introAudio (review intro), viewFlashcards (all 18 words), speakFlashcards (all 18 words), reading (full article), speakReading, readAlong, writingSentence, writingParagraph, introAudio (farewell reviewing 5-6 key words).
5. THE Curriculum content SHALL include `contentTypeTags: []` (empty array).
6. THE Curriculum SHALL set `language: "en"` and `userLanguage: "vi"` as top-level body parameters in the API call.
7. THE Curriculum SHALL use Vietnamese for user-facing text and English for reading passages and vocabulary target words.
8. THE Reading passages SHALL draw from Carol Dweck's nuanced later work (the "false growth mindset" problem), Kristin Neff's self-compassion research, and the Japanese concept of hansei (反省 — critical self-reflection).
9. THE Reading passages SHALL include scenarios like receiving harsh feedback at work, failing a project, watching motivational content but feeling worse, the gap between "I can do anything" and "I need to honestly assess where I am."
10. THE Curriculum description SHALL frame honest self-assessment as the prerequisite for real growth (not the enemy of confidence), consistent with the Ordinary_Life_Philosophy.

### Requirement 5: Finding Meaning in Work Without Being "Extraordinary" Curriculum

**User Story:** As a Vietnamese office worker learning English, I want to explore how ordinary work becomes meaningful through craftsmanship and connection, so that I can find purpose in my daily work while building English vocabulary.

#### Acceptance Criteria

1. THE Curriculum SHALL contain exactly 18 English vocabulary words in 3 groups of 6, all related to meaning-making, craftsmanship, purpose, contribution, and the psychology of meaningful work. Words SHALL be at the intermediate level (e.g., "craftsmanship", "contribution", "purpose", "mundane", "significance", "vocation").
2. THE Curriculum SHALL contain exactly 4 sessions with activity counts: S1 = 12, S2 = 12, S3 = 12, S4 = 9.
3. WHEN Sessions 1-3 are created, EACH Session SHALL contain activities in this exact order: introAudio (topic intro), introAudio (vocabulary teaching, 500-800 words), viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence, writingSentence, writingParagraph.
4. WHEN Session 4 is created, THE Session SHALL contain activities in this exact order: introAudio (review intro), viewFlashcards (all 18 words), speakFlashcards (all 18 words), reading (full article), speakReading, readAlong, writingSentence, writingParagraph, introAudio (farewell reviewing 5-6 key words).
5. THE Curriculum content SHALL include `contentTypeTags: []` (empty array).
6. THE Curriculum SHALL set `language: "en"` and `userLanguage: "vi"` as top-level body parameters in the API call.
7. THE Curriculum SHALL use Vietnamese for user-facing text and English for reading passages and vocabulary target words.
8. THE Reading passages SHALL draw from Viktor Frankl's logotherapy, Amy Wrzesniewski's job crafting research, and the Japanese concept of ikigai as daily purpose (not the oversimplified Venn diagram version, but the original meaning of finding joy in everyday activities).
9. THE Reading passages SHALL include scenarios like the data entry clerk who finds meaning in accuracy, the accountant who sees their work as protecting families, the difference between "dream job" mythology and finding depth in the job you have.
10. THE Curriculum description SHALL frame meaning as something you build (not something you find by quitting your job), consistent with the Ordinary_Life_Philosophy.

### Requirement 6: Cultural Perspectives on Success and Fulfillment Curriculum

**User Story:** As a Vietnamese office worker learning English, I want to explore how different cultures define success, so that I can build my own definition while learning cross-cultural English vocabulary.

#### Acceptance Criteria

1. THE Curriculum SHALL contain exactly 18 English vocabulary words in 3 groups of 6, all related to cross-cultural psychology, definitions of success, collectivism vs. individualism, and building a personal philosophy. Words SHALL be at the intermediate level (e.g., "collectivism", "individualism", "fulfillment", "prestige", "hierarchy", "aspiration").
2. THE Curriculum SHALL contain exactly 4 sessions with activity counts: S1 = 12, S2 = 12, S3 = 12, S4 = 9.
3. WHEN Sessions 1-3 are created, EACH Session SHALL contain activities in this exact order: introAudio (topic intro), introAudio (vocabulary teaching, 500-800 words), viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence, writingSentence, writingParagraph.
4. WHEN Session 4 is created, THE Session SHALL contain activities in this exact order: introAudio (review intro), viewFlashcards (all 18 words), speakFlashcards (all 18 words), reading (full article), speakReading, readAlong, writingSentence, writingParagraph, introAudio (farewell reviewing 5-6 key words).
5. THE Curriculum content SHALL include `contentTypeTags: []` (empty array).
6. THE Curriculum SHALL set `language: "en"` and `userLanguage: "vi"` as top-level body parameters in the API call.
7. THE Curriculum SHALL use Vietnamese for user-facing text and English for reading passages and vocabulary target words.
8. THE Reading passages SHALL draw from cross-cultural psychology (Hofstede's cultural dimensions), real contrasts between Vietnamese collectivism and Western individualism, East Asian concepts like the Chinese "face" (面子), Korean "nunchi" (눈치), and Japanese "ikigai."
9. THE Reading passages SHALL include scenarios like a Vietnamese worker comparing their life to an American LinkedIn influencer, the pressure of Tết family gatherings ("Con làm ở đâu? Lương bao nhiêu?"), and the realization that "success" looks different in Hanoi, Tokyo, and San Francisco.
10. THE Curriculum description SHALL frame cultural awareness as liberating (you get to choose which definition of success fits you), consistent with the Ordinary_Life_Philosophy.

### Requirement 7: Series Organization

**User Story:** As a content manager, I want all 6 curriculums grouped into a single vi-en series, so that learners can discover the full "ordinary life philosophy" journey in one place.

#### Acceptance Criteria

1. THE Series SHALL be created with a Vietnamese title that captures the Ordinary_Life_Philosophy theme without using difficulty level labels. The title SHALL be concise and evocative (e.g., "Nếu Đời Không Rực Rỡ Thì Sao?").
2. THE Series SHALL have a Vietnamese description of 255 characters or fewer, using one of the 6 tones from the description tone palette, written as a short persuasive hook.
3. THE Series SHALL contain exactly 6 curriculums, one for each topic in the curriculum plan.
4. WHEN curriculums are added to the series, THE Creation_Script SHALL call `curriculum/setDisplayOrder` to assign sequential display order values reflecting the intended learning progression: self-awareness → core values → contentment vs. complacency → honest growth mindset → meaning in work → cultural perspectives.
5. THE Series SHALL maintain language homogeneity: all 6 curriculums SHALL have `language: "en"` and `user_language: "vi"`.
6. THE Series SHALL NOT be made public — it needs content generation first.

### Requirement 8: VocabList Compliance

**User Story:** As a content manager, I want every vocab-related activity to have a properly formatted vocabList, so that the platform can correctly track vocabulary progress.

#### Acceptance Criteria

1. WHEN a `viewFlashcards`, `speakFlashcards`, `vocabLevel1`, or `vocabLevel2` activity is created, THE Activity SHALL include a `vocabList` field containing an array of lowercase strings listing the vocabulary words for that activity.
2. WHEN a Session 1-3 vocab activity is created, THE `vocabList` SHALL contain exactly 6 words (matching the group for that session).
3. WHEN a Session 4 vocab activity is created, THE `vocabList` SHALL contain all 18 words for the curriculum.
4. THE `vocabList` SHALL use the field name `vocabList` — never `words`.
5. THE `vocabList` values SHALL be lowercase strings — never objects, numbers, or mixed case.
6. THE `viewFlashcards` and `speakFlashcards` activities within the same session SHALL have identical `vocabList` arrays.

### Requirement 9: Activity and Session Metadata

**User Story:** As a content manager, I want every activity and session to have proper title and description fields in Vietnamese, so that the platform displays correctly for Vietnamese learners.

#### Acceptance Criteria

1. THE Activity SHALL include `title` and `description` fields for every activity in every session.
2. WHEN a `viewFlashcards`, `speakFlashcards`, `vocabLevel1`, or `vocabLevel2` activity is created, THE Activity title SHALL follow the format "Flashcards: <chủ đề>" and the description SHALL list the words being learned in Vietnamese (e.g., "Học 6 từ: word1, word2, ...").
3. WHEN a `reading` or `speakReading` activity is created, THE Activity title SHALL follow the format "Đọc: <chủ đề>".
4. WHEN a `readAlong` activity is created, THE Activity title SHALL follow the format "Nghe: <chủ đề>".
5. WHEN an `introAudio` activity is created, THE Activity title SHALL be a descriptive Vietnamese label (e.g., "Giới thiệu bài học", "Giới thiệu từ vựng") and the description SHALL be a brief Vietnamese summary.
6. WHEN a `writingSentence` or `writingParagraph` activity is created, THE Activity title SHALL follow the format "Viết: <chủ đề>".
7. THE Session object SHALL include a `title` field in Vietnamese (e.g., "Phần 1", "Phần 2", "Phần 3", "Ôn tập").
8. EVERY activity SHALL have a `data` field (object) containing the activity's content. Content fields SHALL be inside `data`, NOT inline on the activity.
9. EVERY activity SHALL use `activityType` as the type field name — never `type`.

### Requirement 10: Content Quality — Persuasive Copy and Tone Variety

**User Story:** As a content manager, I want all learner-facing text to follow the persuasive copy style with tone variety, so that Vietnamese learners feel emotionally engaged and the series avoids monotonous descriptions.

#### Acceptance Criteria

1. THE Curriculum description SHALL follow the 5-beat persuasive copy structure in Vietnamese: bold ALL-CAPS headline, concrete personal examples, vivid metaphor, transformation promise, and dual growth tie-in (language + thinking).
2. THE Curriculum preview (~150 words) SHALL open with a vivid hook in Vietnamese, name the 18 vocabulary words, describe the learning journey, and read as compelling marketing copy.
3. WHEN introAudio vocabulary teaching scripts are created (Sessions 1-3, activity index 1), EACH script (500-800 words in Vietnamese) SHALL teach each of the 6 words individually with part of speech, full definition, example sentence from the reading context, and smooth transitions between words.
4. WHEN farewell introAudio scripts are created (Session 4, last activity), EACH script SHALL review 5-6 key vocabulary words with definitions and fresh example sentences, connect words back to the curriculum theme, and close with a warm personal sign-off in Vietnamese.
5. THE 6 curriculum descriptions SHALL use varied tones from the 6-tone palette (provocative_question, bold_declaration, vivid_scenario, empathetic_observation, surprising_fact, metaphor_led). Adjacent curriculums within the series SHALL use different tones. No single tone SHALL exceed 30% of the 6 descriptions (i.e., max 2 curriculums per tone).
6. THE 6 farewell introAudio scripts SHALL use varied emotional registers (introspective guide, warm accountability, team-building energy, quiet awe, practical momentum). Adjacent curriculums within the series SHALL use different farewell tones.
7. ALL learner-facing text SHALL be individually hand-crafted for each curriculum topic — no templated content, no string interpolation patterns, no generic fill-in-the-blank approaches.

### Requirement 11: Strip-Keys Compliance

**User Story:** As a content manager, I want new curriculum content to never include auto-generated platform keys, so that the platform correctly generates fresh metadata after upload.

#### Acceptance Criteria

1. THE Curriculum content SHALL NOT include any of the following auto-generated keys: `mp3Url`, `illustrationSet`, `chapterBookmarks`, `segments`, `whiteboardItems`, `userReadingId`, `lessonUniqueId`, `curriculumTags`, `taskId`, `imageId`.
2. IF an existing curriculum is fetched via API to use as a structural template, THEN THE Creation_Script SHALL run `strip_keys()` on the fetched content before using it as input for `curriculum/create`.

### Requirement 12: Privacy — All Curriculums Created Private

**User Story:** As a content manager, I want all newly created curriculums to remain private, so that they go through content generation (audio, illustrations) before being exposed to learners.

#### Acceptance Criteria

1. WHEN a curriculum is created via `curriculum/create`, THE Curriculum SHALL have `is_public: false` (the platform default).
2. THE Creation_Script SHALL NOT call `curriculum/setPublic` with `isPublic: true` on any newly created curriculum.
3. THE Series SHALL NOT be made public via `curriculum-series/setIsPublic`.

### Requirement 13: Script Organization and Cleanup

**User Story:** As a content manager, I want one Python script per curriculum with proper cleanup after creation, so that each curriculum's content is self-contained and the workspace stays clean.

#### Acceptance Criteria

1. THE Creation_Script architecture SHALL use one Python script per curriculum (6 scripts total), each containing all hand-written text content inline.
2. WHEN all 6 curriculums and the series are successfully created and verified, THE Creation_Script files SHALL be deleted from the workspace.
3. AFTER successful creation, THE Creation_Script SHALL create a README.md in the `ordinary-life-philosophy-curriculum/` folder documenting: all curriculum IDs, series ID, SQL queries to find them, vocabulary lists, recreation context.
4. EACH Creation_Script SHALL authenticate via `firebase_token.get_firebase_id_token(UID)` with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`.
5. EACH Creation_Script SHALL call `curriculum/create` with `language: "en"` and `userLanguage: "vi"` as top-level body parameters alongside the `content` JSON string.

### Requirement 14: Duplicate Check After Creation

**User Story:** As a content manager, I want to verify no duplicate curriculums were created, so that the database stays clean.

#### Acceptance Criteria

1. AFTER each curriculum is created, THE Creation_Script SHALL check for duplicates by querying: `SELECT id, title, created_at FROM curriculum WHERE title = '<title>' AND uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73' ORDER BY created_at`.
2. IF duplicates are found, THE Creation_Script SHALL keep the earliest record and delete the extras.
3. IF a duplicate curriculum is in a series, THE Creation_Script SHALL remove it from the series before deleting it.

### Requirement 15: Reading Passage Quality for Vietnamese Office Workers

**User Story:** As a Vietnamese office worker, I want reading passages that feel relevant to my daily life and career situation, so that I stay engaged and see the connection between the philosophy and my real experience.

#### Acceptance Criteria

1. THE Reading passages SHALL be written at intermediate English level — comprehensible to Vietnamese office workers with some English ability, using vocabulary they would encounter in TED talks, business books, and professional development content.
2. THE Reading passages SHALL include workplace scenarios specific to Vietnamese office workers: open-plan offices, team lunches, performance reviews, overtime culture, the commute on xe máy, comparing yourself to the colleague who just got promoted.
3. THE Reading passages SHALL reference cultural touchpoints that Vietnamese readers recognize: Tết family gatherings, the pressure of "ổn định" (stability), social media comparison on Facebook/Zalo, the gap between LinkedIn profiles and real feelings.
4. THE Reading passages SHALL balance Western psychological frameworks with Eastern philosophical perspectives, never presenting one as superior to the other.
5. THE Reading passages SHALL maintain the Ordinary_Life_Philosophy framing throughout: self-awareness is the starting point, not the destination. The goal is always growth from a place of clarity.
