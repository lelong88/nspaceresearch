# Requirements Document

## Introduction

This feature creates a second fiction novel curriculum series at the preintermediate level for Vietnamese-Chinese (vi-zh) learners. An original Chinese mystery novel is written specifically for this audience, then each chapter is converted into a structured curriculum with vocabulary flashcards, reading passages, and read-along activities. The series is added to the existing vi-zh Fiction collection "Truyện (小说)" (ID: 7nf5wi1d), which already contains the first vi-zh novel series "味道的记忆 (Ký Ức Hương Vị)". The structural template is the existing vi-zh series (series ID: uq7ezeuh), but with a completely different story in the mystery/detective genre — distinct from the culinary/slice-of-life genre of the first novel. Vocabulary flashcards are quick refreshers of familiar HSK2-3 level words — the focus is on immersive reading practice, not new vocabulary acquisition.

## Glossary

- **Novel**: The original Chinese mystery fiction story written specifically for this curriculum series
- **Chapter**: A single narrative unit of the Novel; each Chapter maps 1:1 to a Curriculum
- **Curriculum**: A structured learning unit containing a title, preview, description, and learning sessions with activities
- **Series**: A named grouping of Curriculums representing the full Novel, stored via the curriculum-series API
- **Collection**: A top-level organizational shelf; this series is added to the EXISTING vi-zh Fiction Collection "Truyện (小说)" (ID: 7nf5wi1d)
- **Learning_Session**: An ordered sequence of activities within a Curriculum; each Chapter Curriculum has 6 Learning_Sessions
- **Activity**: A single learning step within a Learning_Session; types used are viewFlashcards, reading, and readAlong
- **Vocab_List**: An array of Chinese vocabulary words (characters) attached to a viewFlashcards Activity
- **Reading_Passage**: An original Chinese fiction text (~100-150 characters per passage) attached to a reading or readAlong Activity
- **Preview**: A Vietnamese-language text (~150 words) with vivid hooks that introduces the Chapter
- **Display_Order**: An integer controlling the position of a Curriculum within a Series, matching the Chapter number
- **Strip_Keys**: The set of auto-generated keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId) that must never appear in new Curriculum content
- **Creation_Script**: A Python script that calls the curriculum API to create a single Chapter Curriculum
- **Series_Script**: A Python script that creates the Series, adds all Curriculums to the Series, adds the Series to the existing Collection, and sets Display_Orders
- **Bilingual_Text**: Text that includes both Vietnamese and Chinese, required for all user-facing content at preintermediate level
- **Audio_Speed**: A numeric value (-0.2) controlling playback speed for viewFlashcards and reading activities
- **HSK**: Hanyu Shuiping Kaoshi (Chinese proficiency test); HSK2-3 level words are the target vocabulary difficulty for this series

## Requirements

### Requirement 1: Original Novel Creation

**User Story:** As a curriculum creator, I want an original Chinese mystery novel written for preintermediate Vietnamese-Chinese learners, so that the story provides engaging context for reading practice with familiar vocabulary in a genre different from the existing culinary novel.

#### Acceptance Criteria

1. THE Novel SHALL consist of 10 Chapters, each forming a complete narrative arc segment while contributing to an overarching mystery story.
2. THE Novel SHALL use vocabulary and sentence structures appropriate for preintermediate Chinese learners (HSK2-3 range).
3. WHEN writing each Chapter, THE Novel SHALL use 15 Chinese vocabulary words that are already familiar to preintermediate learners, serving as quick review rather than new learning.
4. THE Novel SHALL tell a cohesive, engaging mystery story with characters, clues, suspense, and resolution that motivates continued reading across all 10 Chapters.
5. THE Novel SHALL be in the mystery/detective genre — entirely different from the culinary/slice-of-life genre of "味道的记忆 (Ký Ức Hương Vị)" and entirely different from the coastal bookshop story of "The Little Bookshop by the Sea".
6. THE Novel SHALL minimize vocabulary overlap between Chapters (at most 2 shared words between any two Chapters), except for recurring character names and essential plot terms.
7. WHEN selecting vocabulary words, THE Novel SHALL target HSK2-3 Chinese words that a preintermediate learner already knows, prioritizing a smooth reading experience over new vocabulary acquisition.
8. THE Novel SHALL be written entirely in simplified Chinese characters.
9. WHEN writing Reading_Passages, THE Novel SHALL target approximately 100-150 Chinese characters per passage (5 passages per Chapter, each passage corresponding to one Learning_Session).

### Requirement 2: Chapter Curriculum Structure

**User Story:** As a curriculum creator, I want each chapter converted into a structured curriculum matching the existing vi-zh novel series format, so that learners experience consistent session flow across all novel series.

#### Acceptance Criteria

1. THE Curriculum SHALL contain exactly 6 Learning_Sessions per Chapter.
2. WHEN constructing Learning_Sessions 1 through 5, THE Curriculum SHALL include exactly 3 Activities in order: viewFlashcards, reading, readAlong.
3. WHEN constructing Learning_Session 6 (review session), THE Curriculum SHALL include exactly 2 Activities in order: viewFlashcards, readAlong.
4. THE viewFlashcards Activity SHALL contain a Vocab_List array of Chinese words and an Audio_Speed value of -0.2.
5. THE reading Activity SHALL contain a text field with the Chinese Reading_Passage and an Audio_Speed value of -0.2.
6. THE readAlong Activity SHALL contain a text field with the same Chinese Reading_Passage as the corresponding reading Activity in the same Learning_Session.
7. WHEN constructing Learning_Session 6, THE readAlong Activity SHALL contain the full Chapter text (all Reading_Passages from Sessions 1-5 concatenated).
8. WHEN constructing Learning_Session 6, THE viewFlashcards Activity SHALL contain all vocabulary words from the Chapter (the union of Vocab_Lists from Sessions 1-5).

### Requirement 3: Activity Titles and Descriptions

**User Story:** As a platform user, I want every activity and session to have descriptive titles and descriptions, so that the learning interface is navigable and informative.

#### Acceptance Criteria

1. THE viewFlashcards Activity SHALL have a title field (e.g., "Flashcards: [topic]") and a description field (e.g., "Học 3 từ: word1, word2, word3").
2. THE reading Activity SHALL have a title field (e.g., "Đọc: [topic]") and a description field containing the first ~80 characters of the reading text.
3. THE readAlong Activity SHALL have a title field (e.g., "Nghe: [topic]") and a description field (e.g., "Nghe đoạn văn vừa đọc và theo dõi.").
4. WHEN constructing Learning_Session 6, THE readAlong Activity title SHALL use "Ôn tập" and the description SHALL reference "Toàn bộ câu chuyện".
5. WHEN constructing Learning_Session 6, THE viewFlashcards Activity description SHALL list all 15 vocabulary words.
6. THE Learning_Session object SHALL have a title field (e.g., "Phần 1", "Phần 2", ... "Ôn tập" for session 6).

### Requirement 4: Bilingual Content

**User Story:** As a Vietnamese-Chinese learner, I want all user-facing text in both Vietnamese and Chinese, so that I can navigate and understand the curriculum in my native language.

#### Acceptance Criteria

1. THE Curriculum title SHALL be Bilingual_Text following the format: "[Vietnamese Novel Title] ([Chinese Novel Title]) — Chương N: [Vietnamese Chapter Title] ([Chinese Chapter Title])".
2. THE Curriculum description SHALL be written in Vietnamese, describing the Chapter content and learning objectives.
3. THE Curriculum Preview SHALL be written in Vietnamese (~150 words), opening with vivid hooks, naming vocabulary words, and describing the learning journey.
4. THE Series title SHALL be Bilingual_Text containing both the Vietnamese and Chinese novel title.
5. THE Series description SHALL be written in Vietnamese, summarizing the novel and the learning journey.
6. THE Curriculum title SHALL NOT include any difficulty level descriptor (e.g., "preintermediate", "sơ trung cấp", "初级", "中级").
7. THE Collection title SHALL be Bilingual_Text containing both Vietnamese and Chinese (the existing collection "Truyện (小说)" already satisfies this).

### Requirement 5: Vocabulary Quality

**User Story:** As a preintermediate learner, I want vocabulary words that match my level, so that I am challenged but not overwhelmed.

#### Acceptance Criteria

1. THE Vocab_List for each Chapter SHALL contain exactly 15 Chinese words.
2. THE Vocab_List words SHALL be familiar to preintermediate Chinese learners (HSK2-3 level) — words they already know, serving as a quick refresher before reading.
3. THE Vocab_List words SHALL be distributed across Learning_Sessions 1-5, with each session's viewFlashcards containing exactly 3 words.
4. WHEN a vocabulary word appears in a Reading_Passage, THE Reading_Passage SHALL use the word in a context that makes its meaning clear.
5. THE Vocab_List SHALL minimize overlap with other Chapters' Vocab_Lists (at most 2 shared words between any two Chapters), except for essential recurring plot terms.

### Requirement 6: Reading Passage Quality

**User Story:** As a learner, I want reading passages that tell an engaging mystery story while reinforcing vocabulary, so that I stay motivated and learn through context.

#### Acceptance Criteria

1. THE Reading_Passage for each Learning_Session SHALL be original Chinese fiction text that advances the Chapter narrative.
2. THE Reading_Passage SHALL use sentence structures appropriate for preintermediate Chinese learners (shorter sentences, common grammatical patterns, HSK2-3 grammar).
3. THE Reading_Passage SHALL incorporate all Vocab_List words from the corresponding Learning_Session's viewFlashcards Activity.
4. WHEN writing Reading_Passages across Sessions 1-5, THE Curriculum SHALL distribute the Chapter narrative so that each session's passage is a coherent segment of approximately equal length (~100-150 Chinese characters each).

### Requirement 7: Strip-Keys Compliance

**User Story:** As a curriculum creator, I want curriculum content to exclude auto-generated keys, so that the platform generates fresh metadata upon creation.

#### Acceptance Criteria

1. THE Curriculum content SHALL NOT contain any of the following keys: mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId.

### Requirement 8: Creation Scripts

**User Story:** As a curriculum creator, I want Python scripts to automate curriculum creation via the API, so that I can efficiently create all 10 chapter curriculums.

#### Acceptance Criteria

1. THE Creation_Script SHALL call the curriculum create endpoint (POST `https://helloapi.step.is/curriculum/create`) with the correct body: `{ firebaseIdToken, uid, language: "zh", userLanguage: "vi", content: JSON.stringify(curriculumContent) }`.
2. THE Creation_Script SHALL authenticate using `firebase_token.get_firebase_id_token` with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`.
3. THE Creation_Script SHALL NOT hardcode any curriculum IDs, collection IDs, or series IDs.
4. THE Creation_Script SHALL import `firebase_token` via `sys.path` manipulation pointing to the workspace root.
5. WHEN a Creation_Script completes successfully, THE Creation_Script SHALL print the created curriculum ID and title for verification.

### Requirement 9: Series and Collection Organization

**User Story:** As a curriculum creator, I want the series organized under the existing vi-zh Fiction collection, so that learners can discover both novels in the same place.

#### Acceptance Criteria

1. THE Series_Script SHALL create a new Series via POST `https://helloapi.step.is/curriculum-series/create` with a Bilingual_Text title and Vietnamese description, `isPublic: true`.
2. WHEN all Chapter Curriculums are created, THE Series_Script SHALL add each Curriculum to the Series via POST `https://helloapi.step.is/curriculum-series/addCurriculum`.
3. THE Series_Script SHALL add the Series to the EXISTING vi-zh Fiction Collection "Truyện (小说)" (ID: 7nf5wi1d) via POST `https://helloapi.step.is/curriculum-collection/addSeriesToCollection`.
4. THE Series_Script SHALL check at runtime whether the existing Collection (ID: 7nf5wi1d) is accessible before adding the Series to it, and report a clear error if the Collection is not found.
5. THE Series_Script SHALL NOT create a new Collection — the vi-zh Fiction Collection "Truyện (小说)" already exists.
6. WHEN setting Display_Orders, THE Series_Script SHALL set each Curriculum's Display_Order to match its Chapter number (1-10) via POST `https://helloapi.step.is/curriculum/setDisplayOrder`.
7. THE Series_Script SHALL authenticate using `firebase_token.get_firebase_id_token` with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`.

### Requirement 10: Post-Import Cleanup and Documentation

**User Story:** As a curriculum creator, I want source materials cleaned up and a README preserved, so that the workspace stays tidy and the content is recoverable.

#### Acceptance Criteria

1. WHEN all Curriculums are successfully imported to the database, THE workspace SHALL delete all source material files (chapter text files, curriculum JSON, content Python files, Creation_Scripts, Series_Script, validation script).
2. THE workspace SHALL retain a README.md in the novel's source folder containing: (a) how the content was created, (b) SQL queries to find the Curriculums, Series, and Collection in the database, (c) enough context to recreate the source materials.
3. THE README.md SHALL include the Series ID, Collection ID (7nf5wi1d), and a SQL query to list all Chapter Curriculums with their titles and Display_Orders.

### Requirement 11: Language and Level Homogeneity

**User Story:** As a platform maintainer, I want the new series to maintain language and level consistency with the existing collection, so that it integrates cleanly with the platform.

#### Acceptance Criteria

1. THE Series SHALL contain only Curriculums with `language: "zh"` and `userLanguage: "vi"`.
2. THE Series SHALL contain only Curriculums at the preintermediate level.
3. THE Series SHALL be compatible with the existing vi-zh Fiction Collection (ID: 7nf5wi1d), which contains only `language: "zh"` and `userLanguage: "vi"` content.
4. THE Series SHALL NOT mix bilingual and single-language Curriculums.

### Requirement 12: Novel Source Folder Naming

**User Story:** As a curriculum creator, I want the novel's source folder to have a descriptive name, so that it is easily distinguishable from other novel folders in the workspace.

#### Acceptance Criteria

1. THE Novel's source folder under `original-novels/` SHALL use a descriptive name based on the novel's title or theme (e.g., `vi-zh-mystery-novel` or a romanized version of the title), rather than a generic name like `vi-zh-novel`.
2. THE Novel's source folder name SHALL clearly indicate both the language pair (vi-zh) and the genre or story identity.
