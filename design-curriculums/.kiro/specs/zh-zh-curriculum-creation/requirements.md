# Requirements Document

## Introduction

Create the first ZH-ZH (Chinese speaker learning Chinese) curriculum content for the platform. ZH-ZH mirrors the EN-EN "Power English" model: native speakers learning advanced vocabulary in their own language through intellectually stimulating topic-based content. Where EN-EN serves English speakers expanding their English vocabulary through articles on sleep science, crowd psychology, and market failures, ZH-ZH serves Chinese speakers expanding their Chinese vocabulary through articles on equivalent intellectually rich topics — written entirely in Chinese.

The EN-EN "Power English" collection (id: 72d8f528) contains 6 series with 52 topic-based curriculums. Each curriculum follows a 4-session pattern: Sessions 1–2 each introduce 5 vocabulary words through a full teaching flow (introAudio, flashcards, vocab exercises, reading, speaking, writing); Session 3 reviews all 10 words; Session 4 presents the full article with a farewell review. All user-facing text is in the target language only (English for EN-EN, Chinese for ZH-ZH) since both language and userLanguage are the same.

The ZH-ZH initiative starts with one collection containing 2 initial series of 4 curriculums each (8 curriculums total), establishing the pattern for future expansion. Topics are chosen for their intellectual depth and vocabulary richness in Chinese — domains where educated Chinese speakers encounter sophisticated 成语, 书面语, and specialized terminology worth mastering.

### Proposed Structure

**Collection:** "中文进阶" (Advanced Chinese) — the ZH-ZH equivalent of "Power English"

**Series 1: "思维与认知" (Thinking & Cognition)** — 4 curriculums:
1. 认知偏差的隐形陷阱 (The Hidden Traps of Cognitive Bias)
2. 决策的艺术与科学 (The Art and Science of Decision-Making)
3. 记忆的建筑学 (The Architecture of Memory)
4. 注意力经济学 (The Economics of Attention)

**Series 2: "社会与文明" (Society & Civilization)** — 4 curriculums:
1. 语言如何塑造思维 (How Language Shapes Thought)
2. 城市的隐秘逻辑 (The Hidden Logic of Cities)
3. 信任的崩塌与重建 (The Collapse and Reconstruction of Trust)
4. 算法时代的伦理困境 (Ethical Dilemmas in the Age of Algorithms)

Each curriculum contains 10 advanced Chinese vocabulary words (成语、书面语、专业术语) across 4 sessions, with a full-length Chinese article as the culminating reading.

## Glossary

- **ZH-ZH_Curriculum**: A curriculum with `language: "zh"` and `userLanguage: "zh"`, where all content — titles, descriptions, previews, introAudio scripts, reading passages, writing prompts, activity metadata — is written entirely in simplified Chinese.
- **EN-EN_Curriculum**: The reference model. A curriculum with `language: "en"` and `userLanguage: "en"`, where all content is in English. The "Power English" collection is the primary reference.
- **Collection**: Top-level organizational shelf. The new ZH-ZH collection "中文进阶" is the Chinese equivalent of "Power English".
- **Series**: A thematic grouping within a collection containing multiple curriculums.
- **Curriculum**: A single learning unit with 10 vocabulary words, 4 sessions, and a fixed activity pattern.
- **Session**: One of 4 ordered segments within a curriculum. Sessions 1–2 are learning sessions, Session 3 is review, Session 4 is full article + farewell.
- **Activity**: An individual learning exercise within a session (e.g., introAudio, viewFlashcards, reading, writingParagraph).
- **Vocab_Word**: An advanced Chinese vocabulary item — may be a 成语 (chengyu/idiom), 书面语 (literary/formal term), or specialized domain term. Each curriculum has 10 words split into 2 groups of 5.
- **Article**: The full-length Chinese reading passage (~800–1200 words) that incorporates all 10 vocabulary words. Presented in Session 4.
- **Reading_Excerpt**: A portion of the Article used in Sessions 1–2, containing the 5 vocabulary words for that session.
- **Strip_Keys**: Auto-generated platform keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId) that must never appear in new curriculum content.
- **Persuasive_Copy**: The required emotional sales copy style for all learner-facing text. For ZH-ZH, this copy is written entirely in Chinese targeting Chinese speakers.
- **Display_Order**: Integer field controlling sort position of curriculums within a series and series within a collection.
- **Creation_Script**: A Python script that calls the helloapi REST API to create a curriculum.
- **Orchestrator_Script**: A Python script that creates the collection, series, adds curriculums to series, adds series to collection, and sets display orders.
- **API**: The helloapi.step.is REST API used for all CRUD operations.
- **learningSessions**: The JSON key used for the sessions array in the curriculum content (not `sessions`).
- **practiceMinutes**: Required integer field on every activity specifying expected duration.

## Requirements

### Requirement 1: Collection and Series Creation

**User Story:** As a content manager, I want to create a new ZH-ZH collection with 2 series, so that Chinese-speaking learners have a dedicated space for advanced Chinese vocabulary content.

#### Acceptance Criteria

1. THE Orchestrator_Script SHALL create one new collection via `curriculum-collection/create` with title "中文进阶", a Chinese description, and `isPublic: false`.
2. THE Orchestrator_Script SHALL create 2 new series via `curriculum-series/create` with Chinese titles ("思维与认知" and "社会与文明"), Chinese descriptions (under 255 characters each), and `isPublic: false`.
3. WHEN a series is created, THE Orchestrator_Script SHALL call `curriculum-collection/addSeriesToCollection` to add the series to the "中文进阶" collection.
4. THE Orchestrator_Script SHALL assign `display_order` values to the 2 series (e.g., 100 and 200) via `curriculum-series/setDisplayOrder`.
5. WHEN all curriculums are created and added, THE Collection SHALL contain exactly 2 series with 4 curriculums each (8 total).

### Requirement 2: Language Parameters

**User Story:** As a content manager, I want each ZH-ZH curriculum created with the correct language parameters, so that the platform correctly identifies the content as Chinese-for-Chinese-speakers.

#### Acceptance Criteria

1. THE Creation_Script SHALL call `curriculum/create` with `language: "zh"` and `userLanguage: "zh"` as top-level body parameters alongside `content`.
2. THE Creation_Script SHALL authenticate using `firebase_token.get_firebase_id_token` with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`.
3. THE Creation_Script SHALL pass `content` as a JSON string in the `curriculum/create` body.
4. WHEN a ZH-ZH_Curriculum is created, THE Creation_Script SHALL print the created curriculum ID and title for verification.

### Requirement 3: 4-Session Curriculum Structure (Mirroring EN-EN Pattern)

**User Story:** As a content manager, I want each ZH-ZH curriculum to follow the EN-EN 4-session pattern with 10 vocabulary words, so that the learning experience mirrors the proven "Power English" structure.

#### Acceptance Criteria

1. THE ZH-ZH_Curriculum SHALL contain exactly 10 Vocab_Words, divided into 2 groups of 5 (W1 for Session 1, W2 for Session 2).
2. THE ZH-ZH_Curriculum SHALL contain exactly 4 sessions in the `learningSessions` array.
3. WHEN Session 1 is created, THE Session SHALL contain activities in this exact order: introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, vocabLevel3, reading, speakReading, readAlong, writingSentence, writingParagraph.
4. WHEN Session 2 is created, THE Session SHALL contain activities in this exact order: introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, vocabLevel3, reading, speakReading, readAlong, writingSentence, writingParagraph.
5. WHEN Session 3 (review) is created, THE Session SHALL contain activities in this exact order: introAudio, viewFlashcards, vocabLevel1, vocabLevel2, vocabLevel3, writingParagraph.
6. WHEN Session 4 (full article) is created, THE Session SHALL contain activities in this exact order: introAudio, reading, speakReading, readAlong, writingParagraph, introAudio (farewell).
7. THE Session 1 introAudio SHALL introduce and teach the 5 W1 vocabulary words.
8. THE Session 2 introAudio SHALL recap Session 1 words before introducing and teaching the 5 W2 vocabulary words.
9. THE Session 3 introAudio SHALL congratulate the learner and recap all 10 words for review.
10. THE Session 4 first introAudio SHALL welcome the learner to the full article and recap the learning journey.
11. THE Session 4 farewell introAudio SHALL review each of the 10 vocabulary words with a fresh example and provide a warm farewell.

### Requirement 4: Vocabulary Selection — Advanced Chinese

**User Story:** As a content manager, I want each curriculum's 10 vocabulary words to be genuinely advanced Chinese terms that educated native speakers would benefit from mastering, so that the content provides real value to Chinese-speaking learners.

#### Acceptance Criteria

1. THE Vocab_Word list for each curriculum SHALL contain exactly 10 Chinese vocabulary items at an advanced level.
2. THE Vocab_Word list SHALL include a mix of: 成语 (four-character idioms), 书面语 (formal/literary terms), and specialized domain terminology relevant to the curriculum topic.
3. THE Vocab_Word list SHALL consist of words that educated Chinese speakers may recognize but do not actively use — the vocabulary equivalent of "passive to active" promotion.
4. THE Vocab_Word list for each curriculum SHALL avoid repeating words used in other curriculums within the same series.
5. WHEN a Vocab_Word is selected, THE Vocab_Word SHALL be naturally usable within the curriculum's topic and Article context.
6. THE viewFlashcards data SHALL include vocabulary items with the word, definition, and example sentence — all in Chinese.

### Requirement 5: All-Chinese Content (Single-Language)

**User Story:** As a content manager, I want all user-facing text written entirely in Chinese, so that the curriculum serves Chinese speakers learning advanced Chinese vocabulary without any foreign language scaffolding.

#### Acceptance Criteria

1. THE ZH-ZH_Curriculum title SHALL be in Chinese only (e.g., "认知偏差的隐形陷阱").
2. THE ZH-ZH_Curriculum description SHALL be written in Chinese following the persuasive copy structure.
3. THE ZH-ZH_Curriculum preview SHALL be written in Chinese (~150 words equivalent).
4. THE introAudio scripts SHALL be written entirely in Chinese.
5. THE reading passages (Reading_Excerpts and full Article) SHALL be written entirely in simplified Chinese.
6. THE writingSentence prompts and writingParagraph prompts SHALL be written entirely in Chinese.
7. THE activity titles and descriptions SHALL be written in Chinese.
8. THE session titles SHALL be written in Chinese (e.g., "第一课", "第二课", "复习", "全文阅读").
9. THE ZH-ZH_Curriculum SHALL NOT contain any English, Vietnamese, pinyin, or other non-Chinese text in any learner-facing field.

### Requirement 6: Content Quality — Persuasive Copy in Chinese

**User Story:** As a content manager, I want all learner-facing marketing text to follow the persuasive copy style written natively in Chinese, so that Chinese-speaking learners feel emotionally engaged and motivated.

#### Acceptance Criteria

1. THE ZH-ZH_Curriculum description SHALL follow the 5-beat persuasive copy structure: bold headline (provocative question/statement), concrete personal examples, vivid metaphor revealing the hidden mechanism, transformation promise, and dual growth tie-in (升级思维 + 提升语言能力).
2. THE ZH-ZH_Curriculum preview SHALL open with a vivid imaginative hook, name the vocabulary words, describe the learning journey, and read as compelling marketing copy — all in Chinese.
3. WHEN an introAudio activity is created for Session 1 or 2, THE introAudio script (500–800 Chinese characters) SHALL teach each vocabulary word individually with: word category (成语/书面语/术语), full definition, example sentence from the Article context, and explanation of how the word is used in the reading.
4. WHEN an introAudio activity is created for Session 3 (review), THE introAudio script SHALL congratulate the learner, recap Sessions 1 and 2 content with specific references, explain the review format, and motivate for the full article.
5. WHEN an introAudio activity is created for Session 4 (farewell), THE introAudio script (400–600 Chinese characters) SHALL review each vocabulary word with a fresh example sentence and provide a warm, encouraging farewell.
6. THE persuasive copy SHALL NOT read as translated English — each piece of text SHALL be written natively in Chinese with natural phrasing, 成语 usage, and cultural references appropriate for Chinese speakers.

### Requirement 7: Content Quality — Reading Passages

**User Story:** As a content manager, I want the reading passages to be intellectually stimulating Chinese articles that naturally incorporate the vocabulary words, so that learners encounter advanced vocabulary in meaningful context.

#### Acceptance Criteria

1. THE Article (~800–1200 Chinese characters) SHALL be an original, intellectually rich Chinese essay on the curriculum's topic, written at an advanced level appropriate for educated Chinese speakers.
2. THE Article SHALL naturally incorporate all 10 Vocab_Words in context — each word appearing at least once in a way that demonstrates its meaning.
3. THE Reading_Excerpt for Session 1 SHALL be a portion of the Article containing the 5 W1 vocabulary words.
4. THE Reading_Excerpt for Session 2 SHALL be a portion of the Article containing the 5 W2 vocabulary words.
5. THE Session 4 reading activity SHALL contain the full Article text.
6. THE Article SHALL use sophisticated Chinese prose — varied sentence structures, rhetorical devices, and the kind of writing found in quality Chinese publications (如《三联生活周刊》、《读书》杂志的文风).
7. THE Article SHALL NOT be a translation of any English source — the content SHALL be conceived and written natively in Chinese.

### Requirement 8: Content Quality — Writing Prompts

**User Story:** As a content manager, I want writing prompts to be specific and contextual in Chinese, so that learners practice vocabulary in meaningful, topic-relevant sentences and paragraphs.

#### Acceptance Criteria

1. THE writingSentence activity SHALL provide a detailed Chinese prompt specifying the context for using the word, plus an example sentence showing correct usage, in the format: "请用「X」造一个关于[具体语境]的句子。示例：[完整示例句]。"
2. THE writingSentence prompt SHALL reference the specific curriculum topic and reading passage context.
3. THE writingParagraph prompts SHALL guide the learner to use vocabulary in meaningful analytical writing about the curriculum topic, referencing specific concepts from the Article.
4. THE writingParagraph prompt for Session 3 (review) SHALL require the learner to use vocabulary from both W1 and W2 groups in an integrated response.
5. THE writingParagraph prompt for Session 4 SHALL be a culminating writing task that synthesizes the full Article's themes.

### Requirement 9: Activity Metadata

**User Story:** As a content manager, I want every activity to have proper Chinese title and description fields, so that server-side logging and client display work correctly.

#### Acceptance Criteria

1. THE Activity SHALL include both a `title` and `description` field for every activity in every session.
2. WHEN a viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, or vocabLevel3 activity is created, THE Activity title SHALL follow the format "词卡：<主题>" and the description SHALL list the words being learned (e.g., "学习5个词：词1、词2、词3、词4、词5").
3. WHEN a reading or speakReading activity is created, THE Activity title SHALL follow the format "阅读：<主题>" and the description SHALL contain the first ~80 characters of the reading text.
4. WHEN a readAlong activity is created, THE Activity title SHALL follow the format "听读：<主题>" and the description SHALL be "听文章朗读并跟随阅读。"
5. WHEN an introAudio activity is created, THE Activity title SHALL be a descriptive Chinese label (e.g., "课程介绍", "词汇讲解", "复习总结") and the description SHALL be a brief Chinese summary.
6. WHEN a writingSentence activity is created, THE Activity title SHALL follow the format "造句：<主题>" and the description SHALL briefly summarize the writing task in Chinese.
7. WHEN a writingParagraph activity is created, THE Activity title SHALL follow the format "写作：<主题>" and the description SHALL briefly summarize the writing task in Chinese.
8. THE Session object SHALL include a `title` field in Chinese (e.g., "第一课", "第二课", "复习", "全文阅读").
9. THE Activity SHALL include a `practiceMinutes` field with appropriate values: introAudio (3), viewFlashcards (6), speakFlashcards (6), vocabLevel1 (10), vocabLevel2 (10), vocabLevel3 (10), reading (5), speakReading (5), readAlong (3), writingSentence (10), writingParagraph (10).

### Requirement 10: Strip-Keys Compliance

**User Story:** As a content manager, I want new ZH-ZH curriculum content to never include auto-generated platform keys, so that the platform correctly generates fresh metadata after upload.

#### Acceptance Criteria

1. THE ZH-ZH_Curriculum content SHALL NOT include any of the following auto-generated keys at any nesting level: `mp3Url`, `illustrationSet`, `chapterBookmarks`, `segments`, `whiteboardItems`, `userReadingId`, `lessonUniqueId`, `curriculumTags`, `taskId`, `imageId`.
2. IF an existing EN-EN curriculum is fetched via API to use as a structural template, THEN THE Creation_Script SHALL run `strip_keys()` on the fetched content before using it as input.

### Requirement 11: Newly Created Curriculums Must Be Private

**User Story:** As a content manager, I want all newly created ZH-ZH curriculums to be private by default, so that they go through content generation before being exposed to learners.

#### Acceptance Criteria

1. WHEN a ZH-ZH_Curriculum is created via `curriculum/create`, THE ZH-ZH_Curriculum SHALL have `is_public: false` (the platform default).
2. THE Creation_Script SHALL NOT call `curriculum/setPublic` with `isPublic: true` on any newly created ZH-ZH_Curriculum.
3. THE Orchestrator_Script SHALL create the collection and series with `isPublic: false`.

### Requirement 12: Display Order and Organization

**User Story:** As a content manager, I want curriculums and series to have explicit display orders, so that they appear in the intended sequence in the client app.

#### Acceptance Criteria

1. WHEN a curriculum is added to a series via `curriculum-series/addCurriculum`, THE Orchestrator_Script SHALL call `curriculum/setDisplayOrder` to assign a sequential integer display order (0, 1, 2, 3) for the 4 curriculums within each series.
2. THE Orchestrator_Script SHALL assign display_order values to the 2 series (100 and 200) within the collection via `curriculum-series/setDisplayOrder`.
3. THE Orchestrator_Script SHALL assign a display_order to the collection via `curriculum-collection/setDisplayOrder`.
4. WHEN all curriculums are created and ordered, THE Series SHALL contain exactly 4 curriculums each, sorted by display_order.

### Requirement 13: Script Architecture

**User Story:** As a content manager, I want one Python script per curriculum plus an orchestrator script, so that each curriculum's content is self-contained and files remain manageable.

#### Acceptance Criteria

1. THE script architecture SHALL use one Python script per curriculum (e.g., `create_thinking_1_cognitive_bias.py`, `create_thinking_2_decision_making.py`) with all Chinese text content hand-written in that script.
2. THE script architecture SHALL include one orchestrator script that handles collection creation, series creation, adding curriculums to series, adding series to the collection, and setting display orders.
3. THE Creation_Script SHALL import `firebase_token` via `sys.path` manipulation pointing to the workspace root.
4. THE Creation_Script SHALL implement a `strip_keys()` function (inline) that recursively removes all auto-generated keys, used only if fetching an existing curriculum as structural reference.
5. WHEN a curriculum is successfully created and verified in the database, THE source script SHALL be deleted, leaving only a README with creation method, SQL queries, and recreation context.

### Requirement 14: No Templated Content

**User Story:** As a content manager, I want every piece of Chinese learner-facing text to be individually crafted per curriculum, so that each curriculum reads as if written by a Chinese subject-matter expert for that specific topic.

#### Acceptance Criteria

1. THE Creation_Script SHALL NOT use `f-string` interpolation, template functions, or shared text skeletons to generate introAudio scripts, reading passages, descriptions, previews, or writing prompts.
2. THE Creation_Script MAY use shared helper functions for activity structure (types, order, data schema) but SHALL hand-write all Chinese text content per curriculum.
3. THE Chinese text SHALL NOT read as translated English — each piece of text SHALL be written natively in Chinese with natural phrasing, appropriate 成语 usage, and cultural references familiar to Chinese speakers.

### Requirement 15: Language Homogeneity

**User Story:** As a content manager, I want the ZH-ZH collection and series to maintain language homogeneity, so that the platform's language consistency rules are satisfied.

#### Acceptance Criteria

1. THE "中文进阶" collection SHALL contain only series and curriculums with `language: "zh"` and `userLanguage: "zh"`.
2. THE ZH-ZH series SHALL contain only curriculums with `language: "zh"` and `userLanguage: "zh"`.
3. THE ZH-ZH series SHALL NOT be added to any existing EN-EN, EN-ZH, or VI-EN collection.
4. THE ZH-ZH curriculums SHALL NOT be added to any existing non-ZH-ZH series.

### Requirement 16: Series Content — 思维与认知 (Thinking & Cognition)

**User Story:** As a Chinese-speaking learner, I want a Thinking & Cognition vocabulary series, so that I can master advanced Chinese vocabulary related to psychology, decision-making, memory, and attention.

#### Acceptance Criteria

1. THE Series SHALL contain 4 curriculums covering: (a) 认知偏差的隐形陷阱, (b) 决策的艺术与科学, (c) 记忆的建筑学, (d) 注意力经济学.
2. THE Series title SHALL be "思维与认知" with a Chinese description under 255 characters.
3. WHEN each curriculum is created, THE Curriculum SHALL contain 10 advanced Chinese vocabulary words relevant to the specific sub-topic.
4. THE vocabulary words across the 4 curriculums SHALL NOT repeat — 40 unique advanced Chinese words total for the series.

### Requirement 17: Series Content — 社会与文明 (Society & Civilization)

**User Story:** As a Chinese-speaking learner, I want a Society & Civilization vocabulary series, so that I can master advanced Chinese vocabulary related to language, urbanism, trust, and technology ethics.

#### Acceptance Criteria

1. THE Series SHALL contain 4 curriculums covering: (a) 语言如何塑造思维, (b) 城市的隐秘逻辑, (c) 信任的崩塌与重建, (d) 算法时代的伦理困境.
2. THE Series title SHALL be "社会与文明" with a Chinese description under 255 characters.
3. WHEN each curriculum is created, THE Curriculum SHALL contain 10 advanced Chinese vocabulary words relevant to the specific sub-topic.
4. THE vocabulary words across the 4 curriculums SHALL NOT repeat — 40 unique advanced Chinese words total for the series.

### Requirement 18: Workspace Organization

**User Story:** As a content manager, I want the ZH-ZH curriculum work organized in a dedicated workspace folder, so that it is separate from other language pair folders and easy to navigate.

#### Acceptance Criteria

1. THE workspace SHALL contain a dedicated top-level folder for the ZH-ZH curriculum work (e.g., `zh-zh-advanced-chinese/`).
2. WHEN all curriculums are successfully created and verified, THE folder SHALL contain only a README.md documenting: collection ID and title, series IDs and titles, curriculum IDs and titles with display orders, how content was created, SQL queries to find the curriculums in the DB, and enough context to recreate if needed.
3. WHEN all curriculums are verified in the database, THE source Python scripts SHALL be deleted from the workspace, leaving only the README.

### Requirement 19: Post-Creation Verification

**User Story:** As a content manager, I want each ZH-ZH curriculum verified after creation, so that the structure and language parameters are correct.

#### Acceptance Criteria

1. WHEN a ZH-ZH_Curriculum is created, THE Creation_Script SHALL fetch the created curriculum back via `curriculum/getOne` and verify that `language` is `"zh"` and `user_language` is `"zh"`.
2. WHEN a ZH-ZH_Curriculum is created, THE Creation_Script SHALL verify that the number of sessions is 4 and the activity count per session matches the expected pattern (11, 11, 6, 6).
3. WHEN a ZH-ZH_Curriculum is created, THE Creation_Script SHALL verify that no auto-generated keys are present in the created content.
4. THE Creation_Script SHALL check for duplicate curriculums with the same title after creation and delete extras if found.

### Requirement 20: Duplicate Check After Creation

**User Story:** As a content manager, I want duplicate curriculums detected and cleaned up after creation, so that accidental re-runs do not pollute the database.

#### Acceptance Criteria

1. WHEN a curriculum is created, THE Creation_Script SHALL query the database for curriculums with the same title and `uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'`.
2. IF more than one curriculum with the same title is found, THEN THE Creation_Script SHALL keep the earliest-created one and delete the duplicates.
3. WHEN deleting a duplicate, THE Creation_Script SHALL first remove the duplicate from any series membership before calling `curriculum/delete`.
