# Requirements Document

## Introduction

This feature creates a new fiction novel curriculum series at the preintermediate level for Vietnamese-Chinese (vi-zh) learners. An original Chinese novel is written specifically for this audience, then each chapter is converted into a structured curriculum with vocabulary flashcards, reading passages, and read-along activities. Because the existing "Truyện (Fiction)" collection (ID: 97cee550) contains vi-en content (language=en), and the language homogeneity rule requires all curriculums in a collection to target the same language, this series requires a new vi-zh Fiction collection. The structural template is the existing vi-en series "Tiệm Sách Nhỏ Bên Biển (The Little Bookshop by the Sea)" (series ID: n4y9zm3v), but with a completely different story, and Chinese as the target language instead of English. Vocabulary flashcards are quick refreshers of familiar HSK2-3 level words — the focus is on immersive reading practice, not new vocabulary acquisition.

## Glossary

- **Novel**: The original Chinese fiction story written specifically for this curriculum series
- **Chapter**: A single narrative unit of the Novel; each Chapter maps 1:1 to a Curriculum
- **Curriculum**: A structured learning unit containing a title, preview, description, and learning sessions with activities
- **Series**: A named grouping of Curriculums representing the full Novel, stored via the curriculum-series API
- **Collection**: A top-level organizational shelf; this series requires a NEW vi-zh Fiction Collection (separate from the existing vi-en Fiction Collection)
- **Learning_Session**: An ordered sequence of activities within a Curriculum; each Chapter Curriculum has 6 Learning_Sessions
- **Activity**: A single learning step within a Learning_Session; types used are viewFlashcards, reading, and readAlong
- **Vocab_List**: An array of Chinese vocabulary words (characters) attached to a viewFlashcards Activity
- **Reading_Passage**: An original Chinese fiction text (~100-150 characters per passage) attached to a reading or readAlong Activity
- **Preview**: A Vietnamese-language text (~150 words) with vivid hooks that introduces the Chapter
- **Display_Order**: An integer controlling the position of a Curriculum within a Series, matching the Chapter number
- **Strip_Keys**: The set of auto-generated keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId) that must never appear in new Curriculum content
- **Creation_Script**: A Python script that calls the curriculum API to create a single Chapter Curriculum
- **Series_Script**: A Python script that creates the Series, adds all Curriculums to the Series, creates the Collection, adds the Series to the Collection, and sets Display_Orders
- **Bilingual_Text**: Text that includes both Vietnamese and Chinese, required for all user-facing content at preintermediate level
- **Audio_Speed**: A numeric value (-0.2) controlling playback speed for viewFlashcards and reading activities
- **HSK**: Hanyu Shuiping Kaoshi (Chinese proficiency test); HSK2-3 level words are the target vocabulary difficulty for this series

## Requirements

### Requirement 1: Original Novel Creation

**User Story:** As a curriculum creator, I want an original Chinese fiction novel written for preintermediate Vietnamese-Chinese learners, so that the story provides engaging context for reading practice with familiar vocabulary.

#### Acceptance Criteria

1. THE Novel SHALL consist of 10 Chapters, each forming a complete narrative arc segment while contributing to an overarching story.
2. THE Novel SHALL use vocabulary and sentence structures appropriate for preintermediate Chinese learners (HSK2-3 range).
3. WHEN writing each Chapter, THE Novel SHALL use 15 Chinese vocabulary words that are already familiar to preintermediate learners, serving as quick review rather than new learning.
4. THE Novel SHALL tell a cohesive, engaging story with characters, conflict, and resolution that motivates continued reading across all 10 Chapters — and the story SHALL be entirely different from "The Little Bookshop by the Sea" (the existing vi-en novel).
5. THE Novel SHALL minimize vocabulary overlap between Chapters (at most 2 shared words between any two Chapters), except for recurring character names and essential plot terms.
6. WHEN selecting vocabulary words, THE Novel SHALL target HSK2-3 Chinese words that a preintermediate learner already knows, prioritizing a smooth reading experience over new vocabulary acquisition.
7. THE Novel SHALL be written entirely in simplified Chinese characters.
8. WHEN writing Reading_Passages, THE Novel SHALL target approximately 100-150 Chinese characters per passage (5 passages per Chapter, each passage corresponding to one Learning_Session).

### Requirement 2: Chapter Curriculum Structure

**User Story:** As a curriculum creator, I want each chapter converted into a structured curriculum matching the vi-en novel series format, so that learners experience consistent session flow across the series.

#### Acceptance Criteria

1. THE Curriculum SHALL contain exactly 6 Learning_Sessions per Chapter.
2. WHEN constructing Learning_Sessions 1 through 5, THE Curriculum SHALL include exactly 3 Activities in order: viewFlashcards, reading, readAlong.
3. WHEN constructing Learning_Session 6 (review session), THE Curriculum SHALL include exactly 2 Activities in order: viewFlashcards, readAlong.
4. THE viewFlashcards Activity SHALL contain a Vocab_List array of Chinese words and an Audio_Speed value of -0.2.
5. THE reading Activity SHALL contain a text field with the Chinese Reading_Passage and an Audio_Speed value of -0.2.
6. THE readAlong Activity SHALL contain a text field with the same Chinese Reading_Passage as the corresponding reading Activity in the same Learning_Session.
7. WHEN constructing Learning_Session 6, THE readAlong Activity SHALL contain the full Chapter text (all Reading_Passages from Sessions 1-5 concatenated).
8. WHEN constructing Learning_Session 6, THE viewFlashcards Activity SHALL contain all vocabulary words from the Chapter (the union of Vocab_Lists from Sessions 1-5).

### Requirement 3: Bilingual Content

**User Story:** As a Vietnamese-Chinese learner, I want all user-facing text in both Vietnamese and Chinese, so that I can navigate and understand the curriculum in my native language.

#### Acceptance Criteria

1. THE Curriculum title SHALL be Bilingual_Text following the format: "[Vietnamese Novel Title] ([Chinese Novel Title]) — Chương N: [Vietnamese Chapter Title] ([Chinese Chapter Title])".
2. THE Curriculum description SHALL be written in Vietnamese, describing the Chapter content and learning objectives.
3. THE Curriculum Preview SHALL be written in Vietnamese (~150 words), opening with vivid hooks, naming vocabulary words, and describing the learning journey.
4. THE Series title SHALL be Bilingual_Text containing both the Vietnamese and Chinese novel title.
5. THE Series description SHALL be written in Vietnamese, summarizing the novel and the learning journey.
6. THE Curriculum title SHALL NOT include any difficulty level descriptor (e.g., "preintermediate", "sơ trung cấp", "初级", "中级").
7. THE Collection title SHALL be Bilingual_Text containing both Vietnamese and Chinese (e.g., "Truyện (小说)").

### Requirement 4: Vocabulary Quality

**User Story:** As a preintermediate learner, I want vocabulary words that match my level, so that I am challenged but not overwhelmed.

#### Acceptance Criteria

1. THE Vocab_List for each Chapter SHALL contain exactly 15 Chinese words.
2. THE Vocab_List words SHALL be familiar to preintermediate Chinese learners (HSK2-3 level) — words they already know, serving as a quick refresher before reading.
3. THE Vocab_List words SHALL be distributed across Learning_Sessions 1-5, with each session's viewFlashcards containing exactly 3 words.
4. WHEN a vocabulary word appears in a Reading_Passage, THE Reading_Passage SHALL use the word in a context that makes its meaning clear.
5. THE Vocab_List SHALL minimize overlap with other Chapters' Vocab_Lists (at most 2 shared words between any two Chapters), except for essential recurring plot terms.

### Requirement 5: Reading Passage Quality

**User Story:** As a learner, I want reading passages that tell an engaging story while reinforcing vocabulary, so that I stay motivated and learn through context.

#### Acceptance Criteria

1. THE Reading_Passage for each Learning_Session SHALL be original Chinese fiction text that advances the Chapter narrative.
2. THE Reading_Passage SHALL use sentence structures appropriate for preintermediate Chinese learners (shorter sentences, common grammatical patterns, HSK2-3 grammar).
3. THE Reading_Passage SHALL incorporate all Vocab_List words from the corresponding Learning_Session's viewFlashcards Activity.
4. WHEN writing Reading_Passages across Sessions 1-5, THE Curriculum SHALL distribute the Chapter narrative so that each session's passage is a coherent segment of approximately equal length (~100-150 Chinese characters each).

### Requirement 6: Strip-Keys Compliance

**User Story:** As a curriculum creator, I want curriculum content to exclude auto-generated keys, so that the platform generates fresh metadata upon creation.

#### Acceptance Criteria

1. THE Curriculum content SHALL NOT contain any of the following keys: mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId.

### Requirement 7: Creation Scripts

**User Story:** As a curriculum creator, I want Python scripts to automate curriculum creation via the API, so that I can efficiently create all 10 chapter curriculums.

#### Acceptance Criteria

1. THE Creation_Script SHALL call the curriculum create endpoint (POST `https://helloapi.step.is/curriculum/create`) with the correct body: `{ firebaseIdToken, uid, language: "zh", userLanguage: "vi", content: JSON.stringify(curriculumContent) }`.
2. THE Creation_Script SHALL authenticate using `firebase_token.get_firebase_id_token` with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`.
3. THE Creation_Script SHALL NOT hardcode any curriculum IDs, collection IDs, or series IDs.
4. THE Creation_Script SHALL import `firebase_token` via `sys.path` manipulation pointing to the workspace root.
5. WHEN a Creation_Script completes successfully, THE Creation_Script SHALL print the created curriculum ID and title for verification.

### Requirement 8: Series and Collection Organization

**User Story:** As a curriculum creator, I want the series created and organized under a new vi-zh Fiction collection, so that learners can discover the novel in the correct place without violating language homogeneity rules.

#### Acceptance Criteria

1. THE Series_Script SHALL create a new Series via POST `https://helloapi.step.is/curriculum-series/create` with a Bilingual_Text title and Vietnamese description, `isPublic: true`.
2. WHEN all Chapter Curriculums are created, THE Series_Script SHALL add each Curriculum to the Series via POST `https://helloapi.step.is/curriculum-series/addCurriculum`.
3. THE Series_Script SHALL create a new vi-zh Fiction Collection via POST `https://helloapi.step.is/curriculum-collection/create` with a Bilingual_Text title (e.g., "Truyện (小说)") and set it public.
4. THE Series_Script SHALL add the Series to the new vi-zh Fiction Collection via POST `https://helloapi.step.is/curriculum-collection/addSeriesToCollection`.
5. WHEN setting Display_Orders, THE Series_Script SHALL set each Curriculum's Display_Order to match its Chapter number (1-10) via POST `https://helloapi.step.is/curriculum/setDisplayOrder`.
6. THE Series_Script SHALL authenticate using `firebase_token.get_firebase_id_token` with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`.
7. THE Series_Script SHALL NOT add the Series to the existing vi-en "Truyện (Fiction)" Collection (ID: 97cee550), because that Collection contains language=en content and adding language=zh content would violate the language homogeneity rule.
8. THE Series_Script SHALL check at runtime whether a vi-zh Fiction Collection already exists before creating a new one, to avoid duplicates.

### Requirement 9: Post-Import Cleanup and Documentation

**User Story:** As a curriculum creator, I want source materials cleaned up and a README preserved, so that the workspace stays tidy and the content is recoverable.

#### Acceptance Criteria

1. WHEN all Curriculums are successfully imported to the database, THE workspace SHALL delete all source material files (chapter text files, curriculum JSON, content Python files, Creation_Scripts, Series_Script, validation script).
2. THE workspace SHALL retain a README.md in the novel's source folder containing: (a) how the content was created, (b) SQL queries to find the Curriculums, Series, and Collection in the database, (c) enough context to recreate the source materials.
3. THE README.md SHALL include the Series ID, Collection ID, and a SQL query to list all Chapter Curriculums with their titles and Display_Orders.

### Requirement 10: Language and Level Homogeneity

**User Story:** As a platform maintainer, I want the new series and collection to maintain language and level consistency, so that it integrates cleanly with the platform.

#### Acceptance Criteria

1. THE Series SHALL contain only Curriculums with `language: "zh"` and `userLanguage: "vi"`.
2. THE Series SHALL contain only Curriculums at the preintermediate level.
3. THE new vi-zh Fiction Collection SHALL contain only series and curriculums with `language: "zh"` and `userLanguage: "vi"`.
4. THE Series SHALL NOT mix bilingual and single-language Curriculums.
