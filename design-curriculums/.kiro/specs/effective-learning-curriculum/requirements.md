# Requirements Document

## Introduction

Create 10 curriculums across 2 language pairs (en-en, vi-en) covering 5 learning science topics, then organize them with 2 existing "Get Comfortable Being Uncomfortable" curriculums into 2 themed collections about effective learning.

### The 5 Topics

1. **Angela Duckworth's "Grit" TED Talk** — Podcast-based curriculum built from the YouTube TED Talk (https://www.youtube.com/watch?v=H14bBuluwB8). Must have `youtubeUrl` in content and `contentTypeTags: ["podcast"]`.
2. **Growth Mindset** — Concept by Carol Dweck. Non-podcast, concept-based. `contentTypeTags: []`.
3. **Desirable Difficulties** — Concept by Robert Bjork. Non-podcast, concept-based. `contentTypeTags: []`.
4. **Productive Struggle** — Concept by Manu Kapur. Non-podcast, concept-based. `contentTypeTags: []`.
5. **Zone of Proximal Development** — Concept by Lev Vygotsky. Non-podcast, concept-based. `contentTypeTags: []`.

### Language Pairs

- **en-en** (upperintermediate): All text in English. Single-language. `language: "en"`, `userLanguage: "en"`.
- **vi-en** (intermediate): User-facing text (titles, descriptions, introAudio, writing prompts) in Vietnamese. Reading passages in English. `language: "en"`, `userLanguage: "vi"`.

### Curriculum Structure (All 10 Curriculums)

Each curriculum has 18 vocabulary words in 3 groups of 6, spread across 5 sessions. Activity counts per session: 12, 12, 12, 4, 5.

**Sessions 1-3 (teaching sessions):** Each teaches 1 group of 6 words. Activity order: introAudio (topic intro), introAudio (vocabulary teaching, 500-800 words), viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence, writingSentence, writingParagraph.

**Session 4 (review):** 4 activities — introAudio (review intro), reading (full article), speakReading, readAlong.

**Session 5 (farewell):** 5 activities — introAudio (final reading intro), reading (full article variant or continuation), speakReading, readAlong, introAudio (farewell — reviews all 18 words with definitions and fresh examples).

### Podcast vs. Concept-Based Distinction

- **Podcast (Topic 1 — Grit):** Has `youtubeUrl` at content top-level, `contentTypeTags: ["podcast"]`. Reading passages drawn from/inspired by the TED Talk transcript.
- **Concept-based (Topics 2-5):** No `youtubeUrl`, `contentTypeTags: []`. Reading passages are original educational content about the concept.

### Collections

The 10 new curriculums + 2 existing "Get Comfortable Being Uncomfortable" curriculums are organized into 2 collections (6 curriculums each):

- **en-en collection:** "How to Learn Effectively" (or similar). 6 curriculums. `display_order: -999` (immediately after Featured at -1000). Level: upperintermediate.
- **vi-en collection:** "Học Cách Học Hiệu Quả" (or similar). 6 curriculums. `display_order: -999` (immediately after Featured at -1000). Level: intermediate.

### Podcast Collection Cross-Listing

The Grit podcast curriculums are also added to existing podcast collections:
- en-en Grit → "Learn Vocabulary Through Podcasts" collection (id: `mqdqxuyp`, currently 4 curriculums at display_order 0-3). New curriculum gets display_order 4.
- vi-en Grit → "Học Từ Vựng Qua Podcast" collection (id: `1pspi6gt`, currently 6 curriculums). New curriculum gets the next available display_order.

### Existing Curriculums to Include

- en-en: `VdgEbnzAassbpRPa` — "Get Comfortable Being Uncomfortable" (mini, 5-6 words, 2 sessions)
- vi-en: `2hcxuPuBD1g1F3Zk` — "Bước Ra Khỏi Vùng An Toàn" (mini, 6 words, 2 sessions)

These are added to the new collections but are NOT modified.

### What This Spec Covers

- Creation of 10 new curriculums (5 topics × 2 language pairs)
- Creation of 2 new collections with display_order -999
- Adding all 12 curriculums (10 new + 2 existing) to the appropriate collections
- Cross-listing the 2 Grit podcast curriculums into existing podcast collections
- Display order assignment for all curriculums within collections
- Post-creation verification and duplicate checking
- Source material cleanup after successful creation

### What This Spec Does NOT Cover

- Modifications to the 2 existing "Get Comfortable Being Uncomfortable" curriculums
- Modifications to existing podcast collections (beyond adding the new Grit curriculums)
- Client-side UI changes
- Content generation pipeline (audio, illustrations) — all curriculums created private
- Making any curriculum or collection public

## Glossary

- **Curriculum**: A single learning unit with vocabulary words, sessions, and activities, stored as JSON content in the database.
- **Collection**: A top-level grouping that organizes curriculums for display to learners. Has `display_order` controlling its position relative to other collections.
- **Session**: An ordered segment within a curriculum containing a sequence of activities.
- **Activity**: An individual learning exercise within a session (introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence, writingParagraph).
- **Podcast_Curriculum**: A curriculum with `contentTypeTags: ["podcast"]` and a `youtubeUrl` field at the content top-level, built around a specific audio/video talk.
- **Concept_Curriculum**: A curriculum with `contentTypeTags: []` (empty array) and no `youtubeUrl`, built around an educational concept with original reading passages.
- **Creation_Script**: A standalone Python script that calls the helloapi REST API to create a single curriculum.
- **Strip_Keys**: The set of auto-generated platform keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId) that must never appear in new content.
- **Display_Order**: Integer field controlling sort position of curriculums within a collection or collections within the platform.
- **Persuasive_Copy**: The required emotional sales copy style for all learner-facing text, following the 5-beat structure defined in CURRICULUM_QUALITY_STANDARDS.md.
- **Featured_Collection**: The existing collection with `display_order: -1000` that appears first in the platform. New collections are placed immediately after it.
- **Cross_Listing**: Adding a curriculum to multiple collections (e.g., the Grit podcast curriculum appears in both the effective learning collection and the podcast collection).
- **VocabList**: An array of lowercase strings on vocab activities listing the vocabulary words for that activity.

## Requirements

### Requirement 1: en-en Grit Podcast Curriculum

**User Story:** As a content manager, I want to create an en-en podcast curriculum based on Angela Duckworth's "Grit" TED Talk, so that English-speaking learners can build vocabulary through an engaging talk about perseverance and passion.

#### Acceptance Criteria

1. THE Curriculum SHALL contain exactly 18 English vocabulary words in 3 groups of 6, all drawn from or closely related to Angela Duckworth's "Grit" TED Talk.
2. THE Curriculum SHALL contain exactly 5 sessions with activity counts: S1 = 12, S2 = 12, S3 = 12, S4 = 4, S5 = 5.
3. WHEN Sessions 1-3 are created, EACH Session SHALL contain activities in this exact order: introAudio (talk/topic intro), introAudio (vocabulary teaching, 500-800 words), viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence, writingSentence, writingParagraph.
4. WHEN Session 4 is created, THE Session SHALL contain activities in this exact order: introAudio (review intro), reading (full article), speakReading, readAlong.
5. WHEN Session 5 is created, THE Session SHALL contain activities in this exact order: introAudio (final reading intro), reading (full article variant or continuation), speakReading, readAlong, introAudio (farewell reviewing all 18 words).
6. THE Curriculum content SHALL include `youtubeUrl: "https://www.youtube.com/watch?v=H14bBuluwB8"` at the top level.
7. THE Curriculum content SHALL include `contentTypeTags: ["podcast"]`.
8. THE Curriculum SHALL set `language: "en"` and `userLanguage: "en"` as top-level body parameters in the API call.
9. THE Curriculum SHALL use English for all user-facing text (title, description, preview, introAudio scripts, writing prompts, reading passages).

### Requirement 2: vi-en Grit Podcast Curriculum

**User Story:** As a content manager, I want to create a vi-en podcast curriculum based on Angela Duckworth's "Grit" TED Talk, so that Vietnamese-speaking learners of English can build vocabulary through an engaging talk about perseverance and passion.

#### Acceptance Criteria

1. THE Curriculum SHALL contain exactly 18 English vocabulary words in 3 groups of 6, all drawn from or closely related to Angela Duckworth's "Grit" TED Talk.
2. THE Curriculum SHALL contain exactly 5 sessions with activity counts: S1 = 12, S2 = 12, S3 = 12, S4 = 4, S5 = 5.
3. WHEN Sessions 1-3 are created, EACH Session SHALL contain activities in this exact order: introAudio (talk/topic intro), introAudio (vocabulary teaching, 500-800 words), viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence, writingSentence, writingParagraph.
4. WHEN Session 4 is created, THE Session SHALL contain activities in this exact order: introAudio (review intro), reading (full article), speakReading, readAlong.
5. WHEN Session 5 is created, THE Session SHALL contain activities in this exact order: introAudio (final reading intro), reading (full article variant or continuation), speakReading, readAlong, introAudio (farewell reviewing all 18 words).
6. THE Curriculum content SHALL include `youtubeUrl: "https://www.youtube.com/watch?v=H14bBuluwB8"` at the top level.
7. THE Curriculum content SHALL include `contentTypeTags: ["podcast"]`.
8. THE Curriculum SHALL set `language: "en"` and `userLanguage: "vi"` as top-level body parameters in the API call.
9. THE Curriculum SHALL use Vietnamese for user-facing text (title, description, preview, introAudio scripts, writing prompts) and English for reading passages and vocabulary target words.

### Requirement 3: en-en Growth Mindset Concept Curriculum

**User Story:** As a content manager, I want to create an en-en concept curriculum about Carol Dweck's Growth Mindset, so that English-speaking learners can build vocabulary while learning about the power of believing abilities can be developed.

#### Acceptance Criteria

1. THE Curriculum SHALL contain exactly 18 English vocabulary words in 3 groups of 6, all related to Carol Dweck's Growth Mindset concept.
2. THE Curriculum SHALL contain exactly 5 sessions with activity counts: S1 = 12, S2 = 12, S3 = 12, S4 = 4, S5 = 5.
3. WHEN Sessions 1-3 are created, EACH Session SHALL contain activities in this exact order: introAudio (concept intro), introAudio (vocabulary teaching, 500-800 words), viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence, writingSentence, writingParagraph.
4. THE Curriculum content SHALL include `contentTypeTags: []` (empty array).
5. THE Curriculum content SHALL NOT include a `youtubeUrl` field.
6. THE Curriculum SHALL set `language: "en"` and `userLanguage: "en"` as top-level body parameters in the API call.
7. THE Curriculum SHALL use English for all user-facing text and reading passages.
8. THE Reading passages SHALL be original educational content about Growth Mindset, not transcripts of any specific talk.

### Requirement 4: vi-en Growth Mindset Concept Curriculum

**User Story:** As a content manager, I want to create a vi-en concept curriculum about Carol Dweck's Growth Mindset, so that Vietnamese-speaking learners of English can build vocabulary while learning about the power of believing abilities can be developed.

#### Acceptance Criteria

1. THE Curriculum SHALL contain exactly 18 English vocabulary words in 3 groups of 6, all related to Carol Dweck's Growth Mindset concept.
2. THE Curriculum SHALL contain exactly 5 sessions with activity counts: S1 = 12, S2 = 12, S3 = 12, S4 = 4, S5 = 5.
3. WHEN Sessions 1-3 are created, EACH Session SHALL contain activities in this exact order: introAudio (concept intro), introAudio (vocabulary teaching, 500-800 words), viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence, writingSentence, writingParagraph.
4. THE Curriculum content SHALL include `contentTypeTags: []` (empty array).
5. THE Curriculum content SHALL NOT include a `youtubeUrl` field.
6. THE Curriculum SHALL set `language: "en"` and `userLanguage: "vi"` as top-level body parameters in the API call.
7. THE Curriculum SHALL use Vietnamese for user-facing text and English for reading passages and vocabulary target words.
8. THE Reading passages SHALL be original educational content about Growth Mindset, not transcripts of any specific talk.

### Requirement 5: en-en Desirable Difficulties Concept Curriculum

**User Story:** As a content manager, I want to create an en-en concept curriculum about Robert Bjork's Desirable Difficulties, so that English-speaking learners can build vocabulary while learning why making learning harder can make it more effective.

#### Acceptance Criteria

1. THE Curriculum SHALL contain exactly 18 English vocabulary words in 3 groups of 6, all related to Robert Bjork's Desirable Difficulties concept.
2. THE Curriculum SHALL contain exactly 5 sessions with activity counts: S1 = 12, S2 = 12, S3 = 12, S4 = 4, S5 = 5.
3. WHEN Sessions 1-3 are created, EACH Session SHALL contain activities in this exact order: introAudio (concept intro), introAudio (vocabulary teaching, 500-800 words), viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence, writingSentence, writingParagraph.
4. THE Curriculum content SHALL include `contentTypeTags: []` (empty array).
5. THE Curriculum content SHALL NOT include a `youtubeUrl` field.
6. THE Curriculum SHALL set `language: "en"` and `userLanguage: "en"` as top-level body parameters in the API call.
7. THE Curriculum SHALL use English for all user-facing text and reading passages.

### Requirement 6: vi-en Desirable Difficulties Concept Curriculum

**User Story:** As a content manager, I want to create a vi-en concept curriculum about Robert Bjork's Desirable Difficulties, so that Vietnamese-speaking learners of English can build vocabulary while learning why making learning harder can make it more effective.

#### Acceptance Criteria

1. THE Curriculum SHALL contain exactly 18 English vocabulary words in 3 groups of 6, all related to Robert Bjork's Desirable Difficulties concept.
2. THE Curriculum SHALL contain exactly 5 sessions with activity counts: S1 = 12, S2 = 12, S3 = 12, S4 = 4, S5 = 5.
3. WHEN Sessions 1-3 are created, EACH Session SHALL contain activities in this exact order: introAudio (concept intro), introAudio (vocabulary teaching, 500-800 words), viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence, writingSentence, writingParagraph.
4. THE Curriculum content SHALL include `contentTypeTags: []` (empty array).
5. THE Curriculum content SHALL NOT include a `youtubeUrl` field.
6. THE Curriculum SHALL set `language: "en"` and `userLanguage: "vi"` as top-level body parameters in the API call.
7. THE Curriculum SHALL use Vietnamese for user-facing text and English for reading passages and vocabulary target words.

### Requirement 7: en-en Productive Struggle Concept Curriculum

**User Story:** As a content manager, I want to create an en-en concept curriculum about Manu Kapur's Productive Struggle (Productive Failure), so that English-speaking learners can build vocabulary while learning how struggling before being taught leads to deeper understanding.

#### Acceptance Criteria

1. THE Curriculum SHALL contain exactly 18 English vocabulary words in 3 groups of 6, all related to Manu Kapur's Productive Struggle concept.
2. THE Curriculum SHALL contain exactly 5 sessions with activity counts: S1 = 12, S2 = 12, S3 = 12, S4 = 4, S5 = 5.
3. WHEN Sessions 1-3 are created, EACH Session SHALL contain activities in this exact order: introAudio (concept intro), introAudio (vocabulary teaching, 500-800 words), viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence, writingSentence, writingParagraph.
4. THE Curriculum content SHALL include `contentTypeTags: []` (empty array).
5. THE Curriculum content SHALL NOT include a `youtubeUrl` field.
6. THE Curriculum SHALL set `language: "en"` and `userLanguage: "en"` as top-level body parameters in the API call.
7. THE Curriculum SHALL use English for all user-facing text and reading passages.

### Requirement 8: vi-en Productive Struggle Concept Curriculum

**User Story:** As a content manager, I want to create a vi-en concept curriculum about Manu Kapur's Productive Struggle, so that Vietnamese-speaking learners of English can build vocabulary while learning how struggling before being taught leads to deeper understanding.

#### Acceptance Criteria

1. THE Curriculum SHALL contain exactly 18 English vocabulary words in 3 groups of 6, all related to Manu Kapur's Productive Struggle concept.
2. THE Curriculum SHALL contain exactly 5 sessions with activity counts: S1 = 12, S2 = 12, S3 = 12, S4 = 4, S5 = 5.
3. WHEN Sessions 1-3 are created, EACH Session SHALL contain activities in this exact order: introAudio (concept intro), introAudio (vocabulary teaching, 500-800 words), viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence, writingSentence, writingParagraph.
4. THE Curriculum content SHALL include `contentTypeTags: []` (empty array).
5. THE Curriculum content SHALL NOT include a `youtubeUrl` field.
6. THE Curriculum SHALL set `language: "en"` and `userLanguage: "vi"` as top-level body parameters in the API call.
7. THE Curriculum SHALL use Vietnamese for user-facing text and English for reading passages and vocabulary target words.

### Requirement 9: en-en Zone of Proximal Development Concept Curriculum

**User Story:** As a content manager, I want to create an en-en concept curriculum about Vygotsky's Zone of Proximal Development, so that English-speaking learners can build vocabulary while learning about the sweet spot between what a learner can do alone and what they can do with guidance.

#### Acceptance Criteria

1. THE Curriculum SHALL contain exactly 18 English vocabulary words in 3 groups of 6, all related to Vygotsky's Zone of Proximal Development concept.
2. THE Curriculum SHALL contain exactly 5 sessions with activity counts: S1 = 12, S2 = 12, S3 = 12, S4 = 4, S5 = 5.
3. WHEN Sessions 1-3 are created, EACH Session SHALL contain activities in this exact order: introAudio (concept intro), introAudio (vocabulary teaching, 500-800 words), viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence, writingSentence, writingParagraph.
4. THE Curriculum content SHALL include `contentTypeTags: []` (empty array).
5. THE Curriculum content SHALL NOT include a `youtubeUrl` field.
6. THE Curriculum SHALL set `language: "en"` and `userLanguage: "en"` as top-level body parameters in the API call.
7. THE Curriculum SHALL use English for all user-facing text and reading passages.

### Requirement 10: vi-en Zone of Proximal Development Concept Curriculum

**User Story:** As a content manager, I want to create a vi-en concept curriculum about Vygotsky's Zone of Proximal Development, so that Vietnamese-speaking learners of English can build vocabulary while learning about the sweet spot between what a learner can do alone and what they can do with guidance.

#### Acceptance Criteria

1. THE Curriculum SHALL contain exactly 18 English vocabulary words in 3 groups of 6, all related to Vygotsky's Zone of Proximal Development concept.
2. THE Curriculum SHALL contain exactly 5 sessions with activity counts: S1 = 12, S2 = 12, S3 = 12, S4 = 4, S5 = 5.
3. WHEN Sessions 1-3 are created, EACH Session SHALL contain activities in this exact order: introAudio (concept intro), introAudio (vocabulary teaching, 500-800 words), viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence, writingSentence, writingParagraph.
4. THE Curriculum content SHALL include `contentTypeTags: []` (empty array).
5. THE Curriculum content SHALL NOT include a `youtubeUrl` field.
6. THE Curriculum SHALL set `language: "en"` and `userLanguage: "vi"` as top-level body parameters in the API call.
7. THE Curriculum SHALL use Vietnamese for user-facing text and English for reading passages and vocabulary target words.


### Requirement 11: en-en "How to Learn Effectively" Collection

**User Story:** As a content manager, I want to create an en-en collection grouping all 6 effective learning curriculums, so that English-speaking learners can discover the full learning science series in one place.

#### Acceptance Criteria

1. THE Collection SHALL be created with a title such as "How to Learn Effectively" (concise, descriptive, no difficulty level in title).
2. THE Collection SHALL contain exactly 6 curriculums: the 5 new en-en curriculums (Grit, Growth Mindset, Desirable Difficulties, Productive Struggle, ZPD) plus the existing en-en "Get Comfortable Being Uncomfortable" curriculum (`VdgEbnzAassbpRPa`).
3. THE Collection SHALL have `display_order: -999` to place it immediately after the Featured collection (display_order -1000).
4. WHEN curriculums are added to the collection, THE Creation_Script SHALL call `curriculum/setDisplayOrder` to assign sequential display order values for each curriculum within the collection.
5. THE Collection SHALL have a short, informative description (not persuasive copy — collection descriptions are neutral category summaries).
6. THE Collection SHALL maintain language homogeneity: all 6 curriculums must have `language: "en"` and `user_language: "en"`.

### Requirement 12: vi-en "Học Cách Học Hiệu Quả" Collection

**User Story:** As a content manager, I want to create a vi-en collection grouping all 6 effective learning curriculums, so that Vietnamese-speaking learners of English can discover the full learning science series in one place.

#### Acceptance Criteria

1. THE Collection SHALL be created with a title such as "Học Cách Học Hiệu Quả" (concise, descriptive, in Vietnamese, no difficulty level in title).
2. THE Collection SHALL contain exactly 6 curriculums: the 5 new vi-en curriculums (Grit, Growth Mindset, Desirable Difficulties, Productive Struggle, ZPD) plus the existing vi-en "Bước Ra Khỏi Vùng An Toàn" curriculum (`2hcxuPuBD1g1F3Zk`).
3. THE Collection SHALL have `display_order: -999` to place it immediately after the Featured collection (display_order -1000).
4. WHEN curriculums are added to the collection, THE Creation_Script SHALL call `curriculum/setDisplayOrder` to assign sequential display order values for each curriculum within the collection.
5. THE Collection SHALL have a short, informative description in Vietnamese (not persuasive copy — collection descriptions are neutral category summaries).
6. THE Collection SHALL maintain language homogeneity: all 6 curriculums must have `language: "en"` and `user_language: "vi"`.

### Requirement 13: Grit Podcast Cross-Listing to Existing Podcast Collections

**User Story:** As a content manager, I want the Grit podcast curriculums added to the existing podcast collections, so that learners browsing podcast-based content can also discover the Grit curriculum.

#### Acceptance Criteria

1. WHEN the en-en Grit podcast curriculum is created, THE Creation_Script SHALL add it to the existing "Learn Vocabulary Through Podcasts" collection (id: `mqdqxuyp`) via `curriculum-collection/addCurriculum`.
2. WHEN the en-en Grit curriculum is added to the podcast collection, THE Creation_Script SHALL set its display_order to 4 (the next position after the existing 4 curriculums at positions 0-3).
3. WHEN the vi-en Grit podcast curriculum is created, THE Creation_Script SHALL add it to the existing "Học Từ Vựng Qua Podcast" collection (id: `1pspi6gt`) via `curriculum-collection/addCurriculum`.
4. WHEN the vi-en Grit curriculum is added to the podcast collection, THE Creation_Script SHALL set its display_order to the next available position after existing curriculums in that collection.

### Requirement 14: VocabList on Vocab Activities

**User Story:** As a content manager, I want every vocab-related activity to have a properly formatted vocabList, so that the platform can correctly track vocabulary progress.

#### Acceptance Criteria

1. WHEN a `viewFlashcards`, `speakFlashcards`, `vocabLevel1`, or `vocabLevel2` activity is created, THE Activity SHALL include a `vocabList` field containing an array of lowercase strings listing the vocabulary words for that activity.
2. THE `vocabList` field SHALL contain exactly 6 words per activity (matching the group for that session).
3. THE `vocabList` SHALL use the field name `vocabList` — never `words`.
4. THE `vocabList` values SHALL be lowercase strings — never objects, numbers, or mixed case.

### Requirement 15: Activity Metadata

**User Story:** As a content manager, I want every activity and session to have proper title and description fields, so that server-side logging and client display work correctly.

#### Acceptance Criteria

1. THE Activity SHALL include `title` and `description` fields for every activity in every session.
2. WHEN a `viewFlashcards`, `speakFlashcards`, `vocabLevel1`, or `vocabLevel2` activity is created, THE Activity title SHALL follow the format "Flashcards: <topic>" (en-en) or the Vietnamese equivalent (vi-en), and the description SHALL list the words being learned.
3. WHEN a `reading` or `speakReading` activity is created, THE Activity title SHALL follow the format "Read: <topic>" (en-en) or "Đọc: <topic>" (vi-en).
4. WHEN a `readAlong` activity is created, THE Activity title SHALL follow the format "Listen: <topic>" (en-en) or "Nghe: <topic>" (vi-en).
5. WHEN an `introAudio` activity is created, THE Activity title SHALL be a descriptive label and the description SHALL be a brief summary.
6. WHEN a `writingSentence` or `writingParagraph` activity is created, THE Activity title SHALL follow the format "Write: <topic>" (en-en) or "Viết: <topic>" (vi-en).
7. THE Session object SHALL include a `title` field appropriate to the user language.

### Requirement 16: Content Quality — Persuasive Copy

**User Story:** As a content manager, I want all learner-facing text to follow the persuasive copy style with tone variety, so that learners feel emotionally engaged and the collection avoids monotonous descriptions.

#### Acceptance Criteria

1. THE Curriculum description SHALL follow the 5-beat persuasive copy structure: bold ALL-CAPS headline, concrete personal examples, vivid metaphor, transformation promise, and dual growth tie-in (language + thinking).
2. THE Curriculum preview (~150 words) SHALL open with a vivid hook, name the 18 vocabulary words, describe the learning journey, and read as compelling marketing copy.
3. WHEN introAudio vocabulary teaching scripts are created (Sessions 1-3, activity index 1), EACH script (500-800 words) SHALL teach each of the 6 words individually with part of speech, definition, example sentence from the reading context, and smooth transitions.
4. WHEN farewell introAudio scripts are created (Session 5, last activity), EACH script SHALL review 5-6 key vocabulary words with definitions and fresh example sentences, connect words back to the curriculum theme, and close with a warm personal sign-off.
5. THE 10 curriculum descriptions SHALL use varied tones from the 6-tone palette (provocative_question, bold_declaration, vivid_scenario, empathetic_observation, surprising_fact, metaphor_led). Adjacent curriculums within the same collection SHALL use different tones. No single tone SHALL exceed 30% of the 10 descriptions.
6. THE 10 farewell introAudio scripts SHALL use varied emotional registers (introspective guide, warm accountability, team-building energy, quiet awe, practical momentum). Adjacent curriculums within the same collection SHALL use different farewell tones.

### Requirement 17: Strip-Keys Compliance

**User Story:** As a content manager, I want new curriculum content to never include auto-generated platform keys, so that the platform correctly generates fresh metadata after upload.

#### Acceptance Criteria

1. THE Curriculum content SHALL NOT include any of the following auto-generated keys: `mp3Url`, `illustrationSet`, `chapterBookmarks`, `segments`, `whiteboardItems`, `userReadingId`, `lessonUniqueId`, `curriculumTags`, `taskId`, `imageId`.
2. IF an existing curriculum is fetched via API to use as a structural template, THEN THE Creation_Script SHALL run `strip_keys()` on the fetched content before using it as input for `curriculum/create`.

### Requirement 18: Privacy — All Curriculums Created Private

**User Story:** As a content manager, I want all newly created curriculums to be private by default, so that they go through content generation (audio, illustrations) before being exposed to learners.

#### Acceptance Criteria

1. WHEN a curriculum is created via `curriculum/create`, THE Curriculum SHALL have `is_public: false` (the platform default).
2. THE Creation_Script SHALL NOT call `curriculum/setPublic` with `isPublic: true` on any newly created curriculum.

### Requirement 19: Script Organization and Cleanup

**User Story:** As a content manager, I want one Python script per curriculum with proper cleanup after creation, so that each curriculum's content is self-contained and the workspace stays clean.

#### Acceptance Criteria

1. THE Creation_Script architecture SHALL use one Python script per curriculum with all text content hand-written in that script.
2. THE Creation_Script SHALL NOT use template functions, string interpolation, or loops to generate learner-facing text content.
3. WHEN all 10 curriculums are successfully created and verified in the database, THE source Python scripts SHALL be deleted, leaving only a README with creation method, curriculum IDs, collection IDs, SQL queries, and recreation context.
4. THE workspace SHALL contain a dedicated folder `effective-learning-curriculum/` for the project.

### Requirement 20: No Templated Content

**User Story:** As a content manager, I want every piece of learner-facing text to be individually crafted per curriculum, so that each curriculum reads as if written by someone who deeply understands the topic from that specific cultural and linguistic perspective.

#### Acceptance Criteria

1. THE Creation_Script SHALL NOT use `f-string` interpolation, template functions, or shared text skeletons to generate introAudio scripts, reading passages, descriptions, previews, or writing prompts.
2. EACH Curriculum's reading passages SHALL be original content exploring the topic from the unique perspective of its target audience — not translations or adaptations of the other language pair's passages.
3. EACH Curriculum's introAudio scripts SHALL be individually crafted to teach vocabulary in a way that resonates with the specific audience.
4. THE vi-en curriculums SHALL NOT be direct translations of the en-en curriculums — each SHALL be written from scratch for its audience.

### Requirement 21: Duplicate Check After Creation

**User Story:** As a content manager, I want to check for duplicate curriculums after creation, so that accidental re-runs of scripts do not create duplicate entries.

#### Acceptance Criteria

1. WHEN a curriculum is created, THE Creation_Script SHALL query the database for curriculums with the same title owned by the same user.
2. IF duplicates are found, THEN THE Creation_Script SHALL report the duplicates and keep the earliest-created one.

### Requirement 22: Thematic Coherence Across the Collection

**User Story:** As a content manager, I want all 5 topics to form a coherent learning science narrative within each collection, so that learners who complete the full collection gain a comprehensive understanding of effective learning principles.

#### Acceptance Criteria

1. THE 5 topics SHALL form a logical progression within each collection: from foundational mindset (Growth Mindset, Get Comfortable Being Uncomfortable) through learning mechanics (Desirable Difficulties, Productive Struggle, ZPD) to sustained effort (Grit).
2. THE Vocabulary words across the 10 curriculums SHALL be distinct — no curriculum SHALL reuse vocabulary words from another curriculum in the same collection.
3. EACH Curriculum's vocabulary SHALL be specifically chosen to illuminate its topic — words that appear in the source material or are essential to understanding the concept.
4. THE en-en and vi-en versions of the same topic SHALL select the same 18 English vocabulary words, so that the two language pairs cover identical vocabulary with different user-facing text.
