# Requirements Document

## Introduction

Create 1-to-1 equivalent en-zh language pair curriculums for every existing vi-zh language pair curriculum. There are 61 vi-zh curriculums across 7 series and 5 collections. Each en-zh curriculum is derived from its vi-zh source by changing `userLanguage` from `vi` to `en` while keeping all Chinese content (reading passages, vocabulary words, song lyrics, movie dialogue, novel text) identical. All user-facing text — titles, descriptions, previews, introAudio scripts, writing prompts, activity titles/descriptions, session titles — is rewritten in English instead of Vietnamese.

New en-zh collections and series must be created to mirror the vi-zh organizational structure, because the language homogeneity rule prohibits mixing `userLanguage: "vi"` and `userLanguage: "en"` content in the same collection or series. The en-zh collections/series mirror the vi-zh hierarchy: same number of series per collection, same number of curriculums per series, same display orders.

The transformation workflow for each curriculum is: (1) fetch the vi-zh source from the database, (2) strip auto-generated keys, (3) rewrite all Vietnamese user-facing text to English, (4) upload via `curriculum/create` with `userLanguage: "en"` and `language: "zh"`.

### Inventory of vi-zh Content to Mirror

**Song-Based Vocab (4 curriculums):**
- Collection: "Học Từ Vựng Tiếng Trung Qua Âm Nhạc (通过音乐学中文词汇)" (ID: `jqmkzvf5`)
- Series: "Học Từ Vựng Tiếng Trung Qua Bài Hát (通过歌曲学中文词汇)" (ID: `sjv8b9r7`)
- 4 curriculums: 月亮代表我的心, 朋友, 甜蜜蜜, 童话

**Movie-Based Vocab (4 curriculums):**
- Collection: "Học Từ Vựng Tiếng Trung Qua Điện Ảnh (通过电影学中文词汇)" (ID: `x8cakjtw`)
- Series: "Học Từ Vựng Tiếng Trung Qua Phim (通过电影学中文词汇)" (ID: `v7a70y0u`)
- 4 curriculums: 功夫, 少林足球, 大话西游, 让子弹飞

**Fiction Novel — 味道的记忆 (10 chapters):**
- Collection: "Truyện (小说)" (ID: `7nf5wi1d`)
- Series: "味道的记忆 (Ký Ức Hương Vị)" (ID: `uq7ezeuh`)

**Fiction Novel — 消失的画 (10 chapters):**
- Collection: "Truyện (小说)" (ID: `7nf5wi1d`)
- Series: "Bức Tranh Biến Mất (消失的画)" (ID: `wlzqfag8`)

**Fiction Novel — 湖边的琴声 (10 chapters):**
- Collection: "Truyện (小说)" (ID: `7nf5wi1d`)
- Series: "Tiếng Đàn Bên Hồ (湖边的琴声)" (ID: `z6xddztr`)

**Textbook — Hán Ngữ Phổ Thông Sơ cấp 2 (25 curriculums):**
- Collection: "Sơ Cấp 2 (初级二)" (ID: `64fb68f8`)
- Series: "Hán Ngữ Phổ Thông - Sơ cấp 2" (ID: `dqce6wbh`)

**Chinese Wisdom — Triết Lý Trong Chữ Hán (4 curriculums):**
- Collection: "Sơ Cấp 2 (初级二)" (ID: `64fb68f8`)
- Series: "Triết Lý Trong Chữ Hán (汉字中的智慧)" (ID: `vxvh04b5`)

**Travel — Khám Phá Trung Quốc (4 curriculums):**
- Collection: "Học Từ Vựng Theo Chủ Đề (主题词汇)" (ID: `q9j66zxj`)
- Series: "Khám Phá Trung Quốc (探索中国)" (ID: `yjwuyhtk`)

**Total: 61 vi-zh curriculums → 61 en-zh curriculums**

## Glossary

- **Source_Curriculum**: An existing vi-zh curriculum in the database that serves as the source for deriving an en-zh curriculum. The Source_Curriculum is fetched via `curriculum/getOne` or SQL query.
- **Mirror_Curriculum**: The new en-zh curriculum derived from a Source_Curriculum. The Mirror_Curriculum has `userLanguage: "en"` and `language: "zh"`, with all Chinese content identical to the source and all user-facing text rewritten in English.
- **Chinese_Content**: All content in simplified Chinese characters that remains identical between Source_Curriculum and Mirror_Curriculum. Includes: reading passages, vocabulary words (characters, pinyin, definitions), song lyrics, movie dialogue, novel text, readAlong text, and vocabulary in viewFlashcards/speakFlashcards/vocabLevel activities.
- **User_Facing_Text**: All text written in the user's language (Vietnamese in source, English in mirror). Includes: curriculum title, description, preview, introAudio scripts, writingSentence prompts, writingParagraph prompts, activity titles, activity descriptions, and session titles.
- **Collection**: Top-level organizational shelf. New en-zh collections mirror the vi-zh collection structure but are separate entities.
- **Series**: A thematic grouping within a collection. New en-zh series mirror the vi-zh series structure.
- **Curriculum**: A single learning unit containing sessions with activities.
- **Strip_Keys**: The set of auto-generated keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId) that must be removed from fetched Source_Curriculum content before creating a Mirror_Curriculum.
- **Persuasive_Copy**: The required emotional sales copy style for all learner-facing text. For en-zh curriculums, this copy targets English-speaking learners of Chinese with the same emotional structure as the vi-zh originals but written natively in English.
- **Display_Order**: Integer field controlling sort position. Mirror_Curriculums use the same display orders as their Source_Curriculums.
- **Creation_Script**: A Python script that fetches a Source_Curriculum, strips keys, transforms Vietnamese text to English, and uploads the Mirror_Curriculum via the API.
- **Orchestrator_Script**: A Python script that creates en-zh collections and series, adds Mirror_Curriculums to series, adds series to collections, and sets display orders.
- **API**: The helloapi.step.is REST API used for all CRUD operations.
- **HSK**: Hanyu Shuiping Kaoshi, the standardized Chinese proficiency test. Content targets HSK2-HSK3 level.
- **Pinyin**: The romanization system for Mandarin Chinese pronunciation.
- **Language_Homogeneity**: The rule that all curriculums in a series or collection must share the same `language` and `userLanguage` values.

## Requirements

### Requirement 1: En-Zh Collection and Series Creation (Mirroring Vi-Zh Structure)

**User Story:** As a content manager, I want new en-zh collections and series that mirror the vi-zh organizational structure, so that English-speaking learners of Chinese have the same content catalog as Vietnamese-speaking learners.

#### Acceptance Criteria

1. THE Orchestrator_Script SHALL create 5 new en-zh collections, one for each vi-zh collection being mirrored, via `curriculum-collection/create` with English titles, English descriptions, and `isPublic: true`.
2. THE Orchestrator_Script SHALL create 7 new en-zh series, one for each vi-zh series being mirrored, via `curriculum-series/create` with English titles, English descriptions (under 255 characters), and `isPublic: true`.
3. WHEN an en-zh series is created, THE Orchestrator_Script SHALL call `curriculum-collection/addSeriesToCollection` to add the series to its corresponding en-zh collection.
4. THE Orchestrator_Script SHALL assign the same `display_order` values to en-zh series within their collections as the vi-zh series have within their vi-zh collections.
5. WHEN all en-zh series are fully populated, THE en-zh organizational structure SHALL contain exactly 61 Mirror_Curriculums distributed across 7 series and 5 collections, matching the vi-zh distribution.

### Requirement 2: En-Zh Collection Title and Description Mapping

**User Story:** As a content manager, I want en-zh collection titles and descriptions to be the English equivalents of the vi-zh originals, so that English-speaking learners understand the content categories.

#### Acceptance Criteria

1. THE en-zh collection mirroring "Học Từ Vựng Tiếng Trung Qua Âm Nhạc (通过音乐学中文词汇)" SHALL have a bilingual English-Chinese title, e.g., "Learn Chinese Vocabulary Through Music (通过音乐学中文词汇)".
2. THE en-zh collection mirroring "Học Từ Vựng Tiếng Trung Qua Điện Ảnh (通过电影学中文词汇)" SHALL have a bilingual English-Chinese title, e.g., "Learn Chinese Vocabulary Through Cinema (通过电影学中文词汇)".
3. THE en-zh collection mirroring "Truyện (小说)" SHALL have a bilingual English-Chinese title, e.g., "Fiction (小说)".
4. THE en-zh collection mirroring "Sơ Cấp 2 (初级二)" SHALL have a bilingual English-Chinese title, e.g., "Elementary 2 (初级二)".
5. THE en-zh collection mirroring "Học Từ Vựng Theo Chủ Đề (主题词汇)" SHALL have a bilingual English-Chinese title, e.g., "Thematic Vocabulary (主题词汇)".
6. THE en-zh collection descriptions SHALL be written in English with the same persuasive copy structure as the vi-zh originals, adapted for English-speaking learners of Chinese.

### Requirement 3: En-Zh Series Title and Description Mapping

**User Story:** As a content manager, I want en-zh series titles and descriptions to be the English equivalents of the vi-zh originals, so that English-speaking learners can navigate the series.

#### Acceptance Criteria

1. THE en-zh series mirroring "Học Từ Vựng Tiếng Trung Qua Bài Hát (通过歌曲学中文词汇)" SHALL have a bilingual English-Chinese title, e.g., "Learn Chinese Vocabulary Through Songs (通过歌曲学中文词汇)".
2. THE en-zh series mirroring "Học Từ Vựng Tiếng Trung Qua Phim (通过电影学中文词汇)" SHALL have a bilingual English-Chinese title, e.g., "Learn Chinese Vocabulary Through Film (通过电影学中文词汇)".
3. THE en-zh series mirroring "味道的记忆 (Ký Ức Hương Vị)" SHALL have a bilingual English-Chinese title, e.g., "Memories of Flavor (味道的记忆)".
4. THE en-zh series mirroring "Bức Tranh Biến Mất (消失的画)" SHALL have a bilingual English-Chinese title, e.g., "The Vanishing Painting (消失的画)".
5. THE en-zh series mirroring "Tiếng Đàn Bên Hồ (湖边的琴声)" SHALL have a bilingual English-Chinese title, e.g., "The Sound of Music by the Lake (湖边的琴声)".
6. THE en-zh series mirroring "Hán Ngữ Phổ Thông - Sơ cấp 2" SHALL have an English title, e.g., "Standard Chinese — Elementary 2".
7. THE en-zh series mirroring "Triết Lý Trong Chữ Hán (汉字中的智慧)" SHALL have a bilingual English-Chinese title, e.g., "Wisdom in Chinese Characters (汉字中的智慧)".
8. THE en-zh series mirroring "Khám Phá Trung Quốc (探索中国)" SHALL have a bilingual English-Chinese title, e.g., "Explore China (探索中国)".
9. THE en-zh series descriptions SHALL be written in English (under 255 characters), with the same persuasive tone as the vi-zh originals adapted for English-speaking learners.

### Requirement 4: Source Curriculum Fetching and Key Stripping

**User Story:** As a content manager, I want each Mirror_Curriculum to be derived from its Source_Curriculum with auto-generated keys stripped, so that the platform generates fresh metadata for the new en-zh curriculum.

#### Acceptance Criteria

1. THE Creation_Script SHALL fetch each Source_Curriculum's full content from the database via `curriculum/getOne` or SQL query using the known vi-zh curriculum ID.
2. WHEN a Source_Curriculum is fetched, THE Creation_Script SHALL strip all auto-generated keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId) from the content at all nesting levels before using it as input for the Mirror_Curriculum.
3. THE Creation_Script SHALL verify that no stripped keys remain in the content dict after stripping, before calling `curriculum/create`.

### Requirement 5: Chinese Content Preservation

**User Story:** As a content manager, I want all Chinese content to remain identical between the Source_Curriculum and Mirror_Curriculum, so that English-speaking learners study the exact same Chinese material as Vietnamese-speaking learners.

#### Acceptance Criteria

1. THE Mirror_Curriculum SHALL preserve all reading passage text (Chinese characters) from the Source_Curriculum without modification.
2. THE Mirror_Curriculum SHALL preserve all vocabulary words (Chinese characters, pinyin, definitions in Chinese if present) from the Source_Curriculum without modification.
3. THE Mirror_Curriculum SHALL preserve all song lyrics text (Chinese characters) from the Source_Curriculum without modification, for song-based curriculums.
4. THE Mirror_Curriculum SHALL preserve all movie dialogue text (Chinese characters) from the Source_Curriculum without modification, for movie-based curriculums.
5. THE Mirror_Curriculum SHALL preserve all novel chapter text (Chinese characters) from the Source_Curriculum without modification, for fiction novel curriculums.
6. THE Mirror_Curriculum SHALL preserve all readAlong text from the Source_Curriculum without modification.
7. THE Mirror_Curriculum SHALL preserve all `youtubeUrl` values from the Source_Curriculum without modification, for song-based and movie-based curriculums.
8. THE Mirror_Curriculum SHALL preserve the activity structure (types, order, count per session) from the Source_Curriculum without modification.
9. THE Mirror_Curriculum SHALL preserve the session structure (number of sessions, session order) from the Source_Curriculum without modification.
10. THE Mirror_Curriculum SHALL preserve all `audioSpeed` values from the Source_Curriculum without modification.

### Requirement 6: Vietnamese-to-English Text Transformation

**User Story:** As a content manager, I want all Vietnamese user-facing text rewritten in English, so that English-speaking learners can navigate and understand the curriculum in their native language.

#### Acceptance Criteria

1. THE Mirror_Curriculum title SHALL be rewritten in English, following the same bilingual format (English framing + Chinese content) as the vi-zh original (Vietnamese framing + Chinese content).
2. THE Mirror_Curriculum description SHALL be rewritten in English following the persuasive copy structure, targeting English-speaking learners of Chinese with the same emotional architecture as the vi-zh original.
3. THE Mirror_Curriculum preview SHALL be rewritten in English (~150 words), with vivid hooks, vocabulary word names, and learning journey description adapted for English-speaking learners.
4. WHEN an introAudio activity contains Vietnamese script text, THE Mirror_Curriculum SHALL rewrite the script in English, preserving the same teaching flow, vocabulary explanations, pinyin references, and emotional tone.
5. WHEN a writingSentence activity contains a Vietnamese prompt, THE Mirror_Curriculum SHALL rewrite the prompt in English, preserving the context, example sentence in Chinese, and the format: "Use the word 'X' (pinyin) to talk about [specific context]. Example: [full example sentence in Chinese]."
6. WHEN a writingParagraph activity contains a Vietnamese prompt, THE Mirror_Curriculum SHALL rewrite the prompt in English, preserving the topic-specific guidance and vocabulary references.
7. THE Mirror_Curriculum SHALL rewrite all activity `title` fields from Vietnamese to English (e.g., "Đọc:" → "Read:", "Nghe:" → "Listen:", "Viết:" → "Write:", "Giới thiệu" → "Introduction", "Ôn tập" → "Review").
8. THE Mirror_Curriculum SHALL rewrite all activity `description` fields from Vietnamese to English, except where the description contains Chinese text (which is preserved).
9. THE Mirror_Curriculum SHALL rewrite all session `title` fields from Vietnamese to English (e.g., "Buổi 1:" → "Session 1:", "Ôn tập" → "Review", "Đọc toàn bộ" → "Full Reading").

### Requirement 7: Curriculum Title Transformation Patterns

**User Story:** As a content manager, I want curriculum titles to follow consistent English patterns per content type, so that the en-zh catalog is navigable and professional.

#### Acceptance Criteria

1. WHEN mirroring a song-based curriculum, THE Mirror_Curriculum title SHALL follow the pattern "Learn Through Song: '[Chinese song title]' – [Artist name]", e.g., "Learn Through Song: '月亮代表我的心' – 邓丽君".
2. WHEN mirroring a movie-based curriculum, THE Mirror_Curriculum title SHALL follow the pattern "Learn Through Film: '[Chinese movie title]' – [English scene description]", e.g., "Learn Through Film: '功夫' – The Pig Sty Alley Showdown".
3. WHEN mirroring a fiction novel chapter, THE Mirror_Curriculum title SHALL follow the pattern "[English Novel Title] ([Chinese Novel Title]) — Chapter N: [English Chapter Title] ([Chinese Chapter Title])".
4. WHEN mirroring a textbook curriculum, THE Mirror_Curriculum title SHALL be the English equivalent of the vi-zh title, preserving any Chinese lesson identifiers.
5. WHEN mirroring a Chinese wisdom curriculum, THE Mirror_Curriculum title SHALL follow the pattern "[English Theme] — Characters of [English Concept] ([Chinese radical/theme]篇)", e.g., "Heart Characters — Characters of the Heart (心字篇)".
6. WHEN mirroring a travel curriculum, THE Mirror_Curriculum title SHALL follow the pattern "[Chinese City] — [English tagline] ([Chinese tagline])", e.g., "桂林 — Where Mountains and Rivers Are Finest Under Heaven (桂林山水甲天下)".
7. THE Mirror_Curriculum title SHALL NOT include difficulty level descriptors (e.g., "HSK3", "Intermediate", "Pre-intermediate").

### Requirement 8: Persuasive Copy Adaptation for English Speakers

**User Story:** As a content manager, I want the persuasive copy in en-zh curriculums to resonate with English-speaking learners of Chinese, so that the marketing text is culturally appropriate and emotionally engaging for the target audience.

#### Acceptance Criteria

1. THE Mirror_Curriculum description SHALL follow the 5-beat persuasive copy structure (bold headline, concrete examples, vivid metaphor, transformation promise, learning-growth tie-in) written natively in English, not machine-translated from Vietnamese.
2. THE Mirror_Curriculum preview SHALL use English-language hooks, cultural references, and motivational framing appropriate for English-speaking learners of Chinese.
3. THE Mirror_Curriculum introAudio scripts SHALL be written in natural, fluent English with the same teaching depth and emotional warmth as the vi-zh originals.
4. THE Mirror_Curriculum introAudio scripts SHALL include pinyin pronunciations when teaching Chinese vocabulary, just as the vi-zh originals do.
5. THE Mirror_Curriculum farewell introAudio scripts (400-600 words) SHALL review each vocabulary word with pinyin and a fresh English example sentence, matching the vi-zh farewell structure.
6. THE Mirror_Curriculum writing prompts SHALL use English-language contexts and instructions while preserving the Chinese example sentences from the vi-zh originals.

### Requirement 9: Language Parameters and API Compliance

**User Story:** As a content manager, I want each Mirror_Curriculum created with the correct language parameters, so that the platform correctly identifies the content as en-zh.

#### Acceptance Criteria

1. THE Creation_Script SHALL call `curriculum/create` with `language: "zh"` and `userLanguage: "en"` as top-level body parameters alongside `content`.
2. THE Creation_Script SHALL authenticate using `firebase_token.get_firebase_id_token` with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`.
3. THE Creation_Script SHALL pass `content` as a JSON string in the `curriculum/create` body.
4. WHEN a Mirror_Curriculum is created, THE Creation_Script SHALL print the created curriculum ID and title for verification.

### Requirement 10: Display Order Preservation

**User Story:** As a content manager, I want Mirror_Curriculums to have the same display orders as their Source_Curriculums, so that the en-zh series present content in the same sequence as the vi-zh series.

#### Acceptance Criteria

1. WHEN a Mirror_Curriculum is added to its en-zh series via `curriculum-series/addCurriculum`, THE Orchestrator_Script SHALL call `curriculum/setDisplayOrder` with the same display_order value as the Source_Curriculum has in its vi-zh series.
2. THE Orchestrator_Script SHALL assign the same display_order values to en-zh series within their collections as the vi-zh series have within their vi-zh collections.
3. WHEN all Mirror_Curriculums are created and ordered, THE en-zh series SHALL contain the same number of curriculums as their vi-zh counterparts, sorted by the same display_order values.

### Requirement 11: Strip-Keys Compliance

**User Story:** As a content manager, I want Mirror_Curriculum content to never include auto-generated platform keys, so that the platform correctly generates fresh metadata after upload.

#### Acceptance Criteria

1. THE Mirror_Curriculum content SHALL NOT include any of the following auto-generated keys at any nesting level: `mp3Url`, `illustrationSet`, `chapterBookmarks`, `segments`, `whiteboardItems`, `userReadingId`, `lessonUniqueId`, `curriculumTags`, `taskId`, `imageId`.

### Requirement 12: Newly Created Curriculums Must Be Private

**User Story:** As a content manager, I want all newly created en-zh curriculums to be private by default, so that they go through content generation (audio, illustrations) before being exposed to learners.

#### Acceptance Criteria

1. WHEN a Mirror_Curriculum is created via `curriculum/create`, THE Mirror_Curriculum SHALL have `is_public: false` (the platform default).
2. THE Creation_Script SHALL NOT call `curriculum/setPublic` with `isPublic: true` on any newly created Mirror_Curriculum.

### Requirement 13: No Templated Content

**User Story:** As a content manager, I want every piece of English user-facing text to be individually crafted per curriculum, so that each Mirror_Curriculum reads as if written by a native English speaker who deeply understands the specific content.

#### Acceptance Criteria

1. THE Creation_Script SHALL NOT use `f-string` interpolation, template functions, or shared text skeletons to generate English introAudio scripts, descriptions, previews, or writing prompts.
2. THE Creation_Script MAY use shared helper functions for fetching Source_Curriculums, stripping keys, and managing activity structure, but SHALL hand-write all English text content per curriculum.
3. THE English text SHALL NOT read as machine-translated Vietnamese — each piece of text SHALL be written natively in English with natural phrasing, idioms, and cultural references appropriate for English speakers.

### Requirement 14: Language Homogeneity

**User Story:** As a content manager, I want all en-zh collections and series to maintain language homogeneity, so that the platform's language consistency rules are satisfied.

#### Acceptance Criteria

1. THE en-zh collections SHALL contain only series and curriculums with `language: "zh"` and `userLanguage: "en"`.
2. THE en-zh series SHALL contain only curriculums with `language: "zh"` and `userLanguage: "en"`.
3. THE en-zh series SHALL NOT be added to any existing vi-zh collection.
4. THE en-zh curriculums SHALL NOT be added to any existing vi-zh series.
5. THE en-zh series SHALL contain curriculums within a maximum 1-level gap from the highest-level curriculum in the series.

### Requirement 15: Script Architecture

**User Story:** As a content manager, I want a clear script architecture for creating 61 en-zh curriculums efficiently, so that the mirroring process is organized and manageable.

#### Acceptance Criteria

1. THE script architecture SHALL use one Python script per curriculum for content types with individually crafted text (song-based, movie-based, wisdom, travel curriculums), with all English text hand-written in that script.
2. THE script architecture SHALL allow batch processing for fiction novel chapters and textbook lessons where the transformation pattern is consistent, using per-chapter or per-lesson scripts that each contain hand-written English text.
3. THE script architecture SHALL include orchestrator scripts (one per content type or one overall) that handle en-zh collection creation, series creation, adding curriculums to series, adding series to collections, and setting display orders.
4. THE Creation_Script SHALL import `firebase_token` via `sys.path` manipulation pointing to the workspace root.
5. THE Creation_Script SHALL implement a `strip_keys()` function (inline or imported) that recursively removes all auto-generated keys from the fetched Source_Curriculum content.
6. WHEN a curriculum is successfully created and verified in the database, THE source script SHALL be deleted, leaving only a README with creation method, SQL queries, and recreation context.

### Requirement 16: Workspace Organization

**User Story:** As a content manager, I want the en-zh mirroring work organized in a dedicated workspace folder, so that it is separate from the vi-zh source folders and easy to navigate.

#### Acceptance Criteria

1. THE workspace SHALL contain a dedicated top-level folder for the en-zh curriculum mirror work (e.g., `en-zh-curriculum-mirror/`).
2. THE workspace folder SHALL be organized with subfolders per content type or series (e.g., `songs/`, `movies/`, `novels/memories-of-flavor/`, `novels/the-vanishing-painting/`, `novels/the-sound-of-music-by-the-lake/`, `textbook/`, `wisdom/`, `travel/`).
3. WHEN all Mirror_Curriculums for a content type are successfully created and verified, THE subfolder SHALL contain only a README.md documenting: en-zh collection ID and title, en-zh series ID and title, Mirror_Curriculum IDs and titles, corresponding Source_Curriculum IDs, how content was created, SQL queries to find the curriculums in the DB, and enough context to recreate if needed.
4. WHEN all Mirror_Curriculums are verified in the database, THE source Python scripts SHALL be deleted from the workspace, leaving only READMEs.

### Requirement 17: Vocabulary Definition Language Handling

**User Story:** As a content manager, I want vocabulary definitions adapted for English-speaking learners, so that flashcard definitions are understandable without Vietnamese.

#### Acceptance Criteria

1. WHEN a Source_Curriculum's viewFlashcards vocabulary items contain Vietnamese definitions or translations, THE Mirror_Curriculum SHALL replace the Vietnamese text with English definitions or translations.
2. WHEN a Source_Curriculum's viewFlashcards vocabulary items contain only Chinese and pinyin (no Vietnamese), THE Mirror_Curriculum SHALL preserve the vocabulary items as-is.
3. THE Mirror_Curriculum SHALL preserve all Chinese characters and pinyin in vocabulary items without modification.

### Requirement 18: Activity Metadata Transformation

**User Story:** As a content manager, I want all activity metadata (titles, descriptions) transformed to English, so that server-side logging and client display work correctly for en-zh curriculums.

#### Acceptance Criteria

1. WHEN a viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, or vocabLevel3 activity is mirrored, THE Activity title SHALL follow the format "Flashcards: <topic in English>" and the description SHALL list the Chinese words being learned.
2. WHEN a reading or speakReading activity is mirrored, THE Activity title SHALL follow the format "Read: <topic in English>" and the description SHALL contain the first ~80 characters of the Chinese text.
3. WHEN a readAlong activity is mirrored, THE Activity title SHALL follow the format "Listen: <topic in English>" and the description SHALL be "Listen to the passage and follow along." (or equivalent English for the content type).
4. WHEN an introAudio activity is mirrored, THE Activity title SHALL be a descriptive label in English (e.g., "Introduction to the Song", "Vocabulary Introduction", "Review") and the description SHALL be a brief English summary.
5. WHEN a writingSentence activity is mirrored, THE Activity title SHALL follow the format "Write: <topic in English>" and the description SHALL briefly summarize the writing task in English.
6. WHEN a writingParagraph activity is mirrored, THE Activity title SHALL follow the format "Write: <topic in English>" and the description SHALL briefly summarize the writing task in English.
7. THE Session object `title` field SHALL be rewritten in English (e.g., "Session 1: <topic>", "Review", "Full Reading", "Full Lyrics", "Full Dialogue").

### Requirement 19: Content-Type-Specific Transformation Rules

**User Story:** As a content manager, I want transformation rules specific to each content type, so that the English text is contextually appropriate for songs, movies, novels, textbook lessons, wisdom, and travel curriculums.

#### Acceptance Criteria

1. WHEN mirroring song-based curriculums, THE introAudio scripts SHALL reference the Chinese song title, artist, and lyrical context in English, explaining how each Chinese word appears in the song with pinyin and English meaning.
2. WHEN mirroring movie-based curriculums, THE introAudio scripts SHALL reference the Chinese movie title, scene context, and dialogue in English, explaining how each Chinese word appears in the scene with pinyin and English meaning.
3. WHEN mirroring fiction novel curriculums, THE description and preview SHALL use English-language narrative hooks and cliffhangers appropriate for the chapter's plot, not direct translations of the Vietnamese hooks.
4. WHEN mirroring textbook curriculums, THE introAudio scripts and descriptions SHALL use English pedagogical framing appropriate for English-speaking learners studying Chinese at the elementary level.
5. WHEN mirroring Chinese wisdom curriculums, THE introAudio scripts SHALL explain Chinese character etymology and philosophy in English, making cultural concepts accessible to English-speaking learners.
6. WHEN mirroring travel curriculums, THE descriptions and previews SHALL use English-language travel writing hooks and cultural context appropriate for English-speaking learners interested in Chinese destinations.

### Requirement 20: Post-Creation Verification

**User Story:** As a content manager, I want each Mirror_Curriculum verified after creation, so that the transformation was applied correctly and no data was lost or corrupted.

#### Acceptance Criteria

1. WHEN a Mirror_Curriculum is created, THE Creation_Script SHALL fetch the created curriculum back via `curriculum/getOne` and verify that `language` is `"zh"` and `userLanguage` is `"en"` (by checking the `user_language` field in the response or database).
2. WHEN a Mirror_Curriculum is created, THE Creation_Script SHALL verify that the number of sessions and activities matches the Source_Curriculum.
3. WHEN a Mirror_Curriculum is created, THE Creation_Script SHALL verify that no auto-generated keys (mp3Url, illustrationSet, etc.) are present in the created content.
4. IF a verification check fails, THEN THE Creation_Script SHALL print a clear error message identifying the curriculum and the failed check, and SHALL NOT proceed to add the curriculum to a series.
