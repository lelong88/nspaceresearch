# Requirements Document

## Introduction

The platform supports 4 language pairs (vi-en, vi-zh, en-zh, en-en), each of which should offer media-based vocabulary curriculums across 3 content types: movie, music, and podcast. The vi-en pair is the most complete reference with 4 curriculums per content type, all organized directly under collections. The other 3 language pairs have gaps — missing curriculums, missing collection organization, or both. This feature closes all gaps so every language pair has full parity across all 3 media content types, with proper collection organization.

## Glossary

- **Curriculum**: A structured multi-session learning unit containing vocabulary, reading passages, and activities, stored as a JSON content blob in the database
- **Collection**: A top-level organizational shelf that contains curriculums directly (no series intermediary)
- **Language_Pair**: A combination of `userLanguage` (the learner's native language) and `language` (the target language being learned), written as `{userLanguage}-{language}` (e.g., vi-en = Vietnamese speaker learning English)
- **Content_Type_Tag**: A tag on a curriculum's `contentTypeTags` field indicating the media source — one of `movie`, `music`, or `podcast`
- **Display_Order**: An integer field on a curriculum that determines its sort position within a collection
- **Creation_Script**: A standalone Python script that builds a single curriculum's content dict, validates it, and uploads it via the `curriculum/create` API
- **Orchestrator_Script**: A Python script that creates collection infrastructure and adds curriculums directly to collections
- **Strip_Keys**: The process of removing auto-generated keys (`mp3Url`, `illustrationSet`, `chapterBookmarks`, `segments`, `whiteboardItems`, `userReadingId`, `lessonUniqueId`, `curriculumTags`, `taskId`, `imageId`) from curriculum content before upload
- **Parity_Matrix**: The grid of language pairs × content types showing which cells have the expected 4 curriculums in an organized collection

## Requirements

### Requirement 1: en-zh Music Collection Organization

**User Story:** As a content manager, I want the 4 existing en-zh music curriculums organized into a collection, so that English-speaking Chinese learners can discover them in the app's browse UI.

#### Acceptance Criteria

1. WHEN the Orchestrator_Script for en-zh music is executed, THE Orchestrator_Script SHALL create a new Collection with a bilingual English/Chinese title following the naming convention of existing en-zh collections (e.g., "Learn Chinese Vocabulary Through Music (通过音乐学中文词汇)")
2. WHEN the Collection is created, THE Orchestrator_Script SHALL add all 4 existing en-zh music curriculums (IDs: HLLOA8bahIraa6rR, MX6Yw2Qrkiry1ylN, CbYWQ16GXWxNiol4, 9jRr2DrofNwyQZ1Z) directly to the Collection via `curriculum-collection/addCurriculum`
3. WHEN each curriculum is added to the Collection, THE Orchestrator_Script SHALL call `curriculum/setDisplayOrder` to assign display orders 0, 1, 2, 3 to the 4 curriculums

### Requirement 2: vi-zh Podcast Curriculums

**User Story:** As a content manager, I want 4 podcast-based vocabulary curriculums for Vietnamese speakers learning Chinese, so that the vi-zh pair has podcast content matching the other content types.

#### Acceptance Criteria

1. WHEN a vi-zh podcast Creation_Script is executed, THE Creation_Script SHALL create a curriculum with `language="zh"`, `userLanguage="vi"`, and `contentTypeTags` containing `podcast`
2. THE Creation_Script SHALL produce a curriculum with 18 vocabulary words (3 groups of 6) drawn from Chinese-language podcast or talk content at HSK2-HSK3 level
3. THE Creation_Script SHALL produce a curriculum with 5 sessions: 3 learning sessions (12 activities each), 1 review session (4 activities), and 1 full reading plus farewell session (5 activities)
4. THE Creation_Script SHALL include a `youtubeUrl` at the top level of the content JSON pointing to the source Chinese-language talk
5. THE Creation_Script SHALL write all user-facing text (titles, descriptions, previews, introAudio scripts, writing prompts, activity titles, session titles, vocabulary definitions) in Vietnamese, following the persuasive copy style
6. THE Creation_Script SHALL strip all auto-generated keys before upload and set `is_public = false`
7. THE Creation_Script SHALL include `practiceMinutes`, `title`, and `description` on every activity
8. WHEN all 4 vi-zh podcast curriculums are created, THE Orchestrator_Script SHALL create a Collection with a bilingual Vietnamese/Chinese title, add all 4 curriculums directly to the Collection via `curriculum-collection/addCurriculum`, and set display orders 0 through 3
9. IF a Creation_Script is run more than once, THEN THE Creation_Script SHALL check for duplicate curriculums by title and language, and the operator SHALL delete extras keeping the earliest-created one
10. WHEN all curriculums are verified in the database, THE operator SHALL delete all Creation_Scripts and the Orchestrator_Script, leaving only a README documenting how the content was created, SQL queries to find it, and recreation instructions

### Requirement 3: en-zh Podcast Curriculums

**User Story:** As a content manager, I want 4 podcast-based vocabulary curriculums for English speakers learning Chinese, so that the en-zh pair has podcast content.

#### Acceptance Criteria

1. WHEN an en-zh podcast Creation_Script is executed, THE Creation_Script SHALL create a curriculum with `language="zh"`, `userLanguage="en"`, and `contentTypeTags` containing `podcast`
2. THE Creation_Script SHALL produce a curriculum with 18 vocabulary words (3 groups of 6) drawn from the same Chinese-language podcast or talk content used for the vi-zh podcasts (Requirement 2), at HSK2-HSK3 level
3. THE Creation_Script SHALL produce a curriculum with 5 sessions: 3 learning sessions (12 activities each), 1 review session (4 activities), and 1 full reading plus farewell session (5 activities)
4. THE Creation_Script SHALL include a `youtubeUrl` at the top level of the content JSON pointing to the source Chinese-language talk
5. THE Creation_Script SHALL write all user-facing text in English, following the persuasive copy style
6. THE Creation_Script SHALL include pinyin in introAudio scripts when teaching vocabulary and in writing prompts with Chinese example sentences
7. THE Creation_Script SHALL strip all auto-generated keys before upload and set `is_public = false`
8. THE Creation_Script SHALL include `practiceMinutes`, `title`, and `description` on every activity
9. WHEN all 4 en-zh podcast curriculums are created, THE Orchestrator_Script SHALL create a Collection with a bilingual English/Chinese title, add all 4 curriculums directly to the Collection via `curriculum-collection/addCurriculum`, and set display orders 0 through 3
10. IF a Creation_Script is run more than once, THEN THE Creation_Script SHALL check for duplicate curriculums by title and language, and the operator SHALL delete extras keeping the earliest-created one
11. WHEN all curriculums are verified in the database, THE operator SHALL delete all Creation_Scripts and the Orchestrator_Script, leaving only a README

### Requirement 4: en-en Movie Curriculums

**User Story:** As a content manager, I want 4 movie-based vocabulary curriculums for English speakers learning English, so that the en-en pair has movie content mirroring the vi-en reference.

#### Acceptance Criteria

1. WHEN an en-en movie Creation_Script is executed, THE Creation_Script SHALL create a curriculum with `language="en"`, `userLanguage="en"`, and `contentTypeTags` containing `movie`
2. THE Creation_Script SHALL use the same 4 movies as the vi-en reference: Forrest Gump, The Shawshank Redemption, Dead Poets Society, and The Pursuit of Happyness
3. THE Creation_Script SHALL fetch the corresponding vi-en curriculum via `curriculum/getOne`, strip all auto-generated keys, and transform all Vietnamese user-facing text to hand-written English
4. THE Creation_Script SHALL produce a curriculum with 18 vocabulary words (3 groups of 6), 5 sessions (12, 12, 12, 4, 5 activities), and a `youtubeUrl` at the top level
5. THE Creation_Script SHALL write all user-facing text in English following the persuasive copy style
6. THE Creation_Script SHALL set `is_public = false` and include `practiceMinutes`, `title`, and `description` on every activity
7. WHEN all 4 en-en movie curriculums are created, THE Orchestrator_Script SHALL create a Collection with an English title (e.g., "Learn Vocabulary Through Cinema"), add all 4 curriculums directly to the Collection via `curriculum-collection/addCurriculum`, and set display orders 0 through 3
8. IF a Creation_Script is run more than once, THEN THE Creation_Script SHALL check for duplicate curriculums by title and language, and the operator SHALL delete extras keeping the earliest-created one
9. WHEN all curriculums are verified in the database, THE operator SHALL delete all Creation_Scripts and the Orchestrator_Script, leaving only a README

### Requirement 5: en-en Song Curriculums

**User Story:** As a content manager, I want 4 song-based vocabulary curriculums for English speakers learning English, so that the en-en pair has music content mirroring the vi-en reference.

#### Acceptance Criteria

1. WHEN an en-en song Creation_Script is executed, THE Creation_Script SHALL create a curriculum with `language="en"`, `userLanguage="en"`, and `contentTypeTags` containing `music`
2. THE Creation_Script SHALL use the same 4 songs as the vi-en reference: Heal the World (Michael Jackson), Imagine (John Lennon), Lean on Me (Bill Withers), and What a Wonderful World (Louis Armstrong)
3. THE Creation_Script SHALL fetch the corresponding vi-en curriculum via `curriculum/getOne`, strip all auto-generated keys, and transform all Vietnamese user-facing text to hand-written English
4. THE Creation_Script SHALL produce a curriculum with 18 vocabulary words (3 groups of 6), 5 sessions (12, 12, 12, 4, 5 activities), and a `youtubeUrl` at the top level
5. THE Creation_Script SHALL write all user-facing text in English following the persuasive copy style
6. THE Creation_Script SHALL set `is_public = false` and include `practiceMinutes`, `title`, and `description` on every activity
7. WHEN all 4 en-en song curriculums are created, THE Orchestrator_Script SHALL create a Collection with an English title (e.g., "Learn Vocabulary Through Music"), add all 4 curriculums directly to the Collection via `curriculum-collection/addCurriculum`, and set display orders 0 through 3
8. IF a Creation_Script is run more than once, THEN THE Creation_Script SHALL check for duplicate curriculums by title and language, and the operator SHALL delete extras keeping the earliest-created one
9. WHEN all curriculums are verified in the database, THE operator SHALL delete all Creation_Scripts and the Orchestrator_Script, leaving only a README

### Requirement 6: en-en Podcast Curriculums

**User Story:** As a content manager, I want 4 podcast-based vocabulary curriculums for English speakers learning English, so that the en-en pair has podcast content mirroring the vi-en reference.

#### Acceptance Criteria

1. WHEN an en-en podcast Creation_Script is executed, THE Creation_Script SHALL create a curriculum with `language="en"`, `userLanguage="en"`, and `contentTypeTags` containing `podcast`
2. THE Creation_Script SHALL use the same 4 TED Talks as the vi-en reference: Tim Urban ("Inside the Mind of a Master Procrastinator"), Amy Cuddy ("Your Body Language May Shape Who You Are"), Julian Treasure ("How to Speak So That People Want to Listen"), and Brené Brown ("The Power of Vulnerability")
3. THE Creation_Script SHALL fetch the corresponding vi-en curriculum via `curriculum/getOne`, strip all auto-generated keys, and transform all Vietnamese user-facing text to hand-written English
4. THE Creation_Script SHALL produce a curriculum with 18 vocabulary words (3 groups of 6), 5 sessions (12, 12, 12, 4, 5 activities), and a `youtubeUrl` at the top level
5. THE Creation_Script SHALL write all user-facing text in English following the persuasive copy style
6. THE Creation_Script SHALL set `is_public = false` and include `practiceMinutes`, `title`, and `description` on every activity
7. WHEN all 4 en-en podcast curriculums are created, THE Orchestrator_Script SHALL create a Collection with an English title (e.g., "Learn Vocabulary Through Podcasts"), add all 4 curriculums directly to the Collection via `curriculum-collection/addCurriculum`, and set display orders 0 through 3
8. IF a Creation_Script is run more than once, THEN THE Creation_Script SHALL check for duplicate curriculums by title and language, and the operator SHALL delete extras keeping the earliest-created one
9. WHEN all curriculums are verified in the database, THE operator SHALL delete all Creation_Scripts and the Orchestrator_Script, leaving only a README

### Requirement 7: Chinese-Language Podcast Content Selection

**User Story:** As a content manager, I want the vi-zh and en-zh podcast curriculums to use Chinese-language talks (not English TED Talks), so that the target-language content is appropriate for learners studying Chinese.

#### Acceptance Criteria

1. THE vi-zh and en-zh podcast curriculums (Requirements 2 and 3) SHALL use 4 Chinese-language talks or podcasts as source material — not the English TED Talks used by vi-en and en-en
2. THE vi-zh and en-zh podcast curriculums SHALL use the same 4 Chinese-language source talks, differing only in user-facing language (Vietnamese for vi-zh, English for en-zh)
3. WHEN selecting Chinese-language talks, THE content manager SHALL choose talks with clear Mandarin speech, available on YouTube, and suitable for HSK2-HSK3 vocabulary extraction
4. THE Creation_Scripts SHALL include the YouTube URL for each Chinese-language talk at the top level of the content JSON

### Requirement 8: Parity Verification

**User Story:** As a content manager, I want to verify that all 4 language pairs have complete media content coverage after all gaps are filled, so that I can confirm the feature is complete.

#### Acceptance Criteria

1. WHEN all gap-filling work is complete, THE operator SHALL query the database to produce a Parity_Matrix showing the count of curriculums per language pair per content type
2. THE Parity_Matrix SHALL show exactly 4 curriculums for every cell (4 language pairs × 3 content types = 12 cells, 48 total curriculums)
3. WHEN verifying each language pair's content, THE operator SHALL confirm that every curriculum with a `movie`, `music`, or `podcast` content type tag belongs to exactly one Collection (directly, not via series)
4. THE operator SHALL verify that no duplicate curriculums exist by checking for multiple curriculums with the same title, language, and user_language owned by the same UID

### Requirement 9: Content Quality Consistency

**User Story:** As a content manager, I want all new curriculums to meet the same quality standards as the vi-en reference, so that learners across all language pairs have a consistent experience.

#### Acceptance Criteria

1. THE Creation_Script for each new curriculum SHALL produce content where every `description` and `preview` field follows the persuasive copy style with a bold headline, concrete examples, vivid metaphor, and transformation promise
2. THE Creation_Script SHALL produce introAudio scripts of 500-800 words for learning sessions, with individual word teaching (definition, example sentence, context explanation)
3. THE Creation_Script SHALL produce `writingSentence` items with detailed prompts specifying context and an example sentence showing correct usage
4. THE Creation_Script SHALL produce `writingParagraph` prompts that reference specific concepts from the source material and guide analytical writing using session vocabulary
5. THE Creation_Script SHALL ensure no templated content generation — all text SHALL be individually crafted per curriculum topic
6. WHILE the target language is Chinese (zh), THE Creation_Script SHALL include pinyin in introAudio vocabulary teaching and in writing prompt example sentences
