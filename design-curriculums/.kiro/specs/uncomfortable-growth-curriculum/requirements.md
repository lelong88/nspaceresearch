# Requirements Document

## Introduction

Create 4 mini `balanced_skills` curriculums built around the theme "Get comfortable being uncomfortable is the essence of language learning." Each curriculum targets a different language pair: en-en (English speaker learning English), en-zh (English speaker learning Chinese), vi-zh (Vietnamese speaker learning Chinese), vi-en (Vietnamese speaker learning English). All 4 curriculums are placed in the appropriate feature collections on the platform.

These are gateway curriculums — compact experiences designed to introduce learners to the mindset of embracing discomfort as the engine of language learning. The goal is not to exhaustively teach the topic, but to give learners a genuine taste of the discomfort-to-growth arc: enough vocabulary and content that they actually feel the awkwardness, push through it, and experience the payoff of comprehension on the other side. The experience should leave learners thinking "that was hard but I grew" and motivated to continue with other courses on the platform.

The theme explores the psychology of discomfort as a growth mechanism — how embracing awkwardness, making mistakes, tolerating ambiguity, and pushing past the "comfort zone" are not obstacles to language learning but the actual engine of it. Each curriculum teaches vocabulary related to growth mindset, resilience, and the psychology of learning through discomfort — adapted to the target language and audience.

### Curriculum Type: mini balanced_skills

The mini `balanced_skills` type is a compact variant of the standard balanced_skills curriculum, designed for gateway/introductory experiences. It has two structural variants:

**Single-language mini variant (en-en):** 5 vocabulary words, 2 sessions. S1: teach all 5 words with full skill coverage (intro, flashcards, reading, writing). S2: review all 5 words + full article + farewell. Activity counts per session: S1 = 8, S2 = 6. Activities include introAudio, viewFlashcards, speakFlashcards, vocabLevel1, reading, speakReading, readAlong, writingSentence, writingParagraph.

**Bilingual mini variant (en-zh, vi-zh, vi-en):** 6 vocabulary words, 2 sessions. S1: teach all 6 words with full skill coverage (intro, flashcards, vocab drills, reading, writing). S2: review all 6 words + full reading + farewell. Activity counts per session: S1 = 9, S2 = 5. Activities include introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence.

### Why Mini — Pedagogical Rationale

A gateway curriculum must thread the needle: small enough to complete in a single focused sitting, but substantial enough that the learner genuinely experiences the discomfort-to-growth arc. With 5-6 vocabulary words, learners face a real cognitive load — enough unfamiliar territory to feel the discomfort the theme promises. The 2-session structure creates a natural emotional arc: Session 1 is the push (new words, new concepts, the uncomfortable stretch), Session 2 is the payoff (review, the full article where everything clicks, the farewell that names what they just accomplished). This mirrors the theme itself — you have to go through the discomfort to reach the growth.

### The 4 Curriculums

1. **en-en** — Single-language mini, English speaker learning advanced English vocabulary about growth through discomfort. 5 words, 2 sessions. All text in English.
2. **en-zh** — Bilingual mini, English speaker learning Chinese. 6 Chinese vocabulary words about embracing discomfort in learning. 2 sessions. User-facing text in English, reading passages in Chinese.
3. **vi-zh** — Bilingual mini, Vietnamese speaker learning Chinese. 6 Chinese vocabulary words about the psychology of uncomfortable growth. 2 sessions. User-facing text in Vietnamese, reading passages in Chinese.
4. **vi-en** — Bilingual mini, Vietnamese speaker learning English. 6 English vocabulary words about stepping outside the comfort zone. 2 sessions. User-facing text in Vietnamese, reading passages in English.

### Feature Collections

Each curriculum is placed in the feature collection appropriate for its language pair. The existing feature collections on the platform house specialized curriculum types organized by language pair. These 4 mini balanced_skills curriculums will be added to the appropriate existing feature collections or new ones created as needed, depending on what collections already exist for each language pair. The database must be queried at runtime to determine the correct placement.

### What This Spec Covers

- Creation of 4 mini balanced_skills curriculums (one per language pair) on the theme of uncomfortable growth
- Vocabulary selection tailored to each language pair and audience (5 words single-language, 6 words bilingual)
- Placement into appropriate feature collections and series
- Post-creation verification, duplicate checking, and display order assignment
- Source material cleanup after successful import

### What This Spec Does NOT Cover

- Changes to existing curriculums or collections
- Client-side UI changes
- Content generation pipeline (audio, illustrations) — curriculums are created private

## Glossary

- **Mini_Balanced_Skills_Curriculum**: A compact gateway variant of the balanced_skills curriculum type. Single-language: 5 words, 2 sessions (activity counts 8, 6). Bilingual: 6 words, 2 sessions (activity counts 9, 5). Designed as an introductory experience that plants the seed of embracing discomfort.
- **Single_Language_Mini_Variant**: The mini balanced_skills variant for single-language pairs (en-en). 5 vocabulary words taught in 1 group, 2 sessions with activity counts 8, 6.
- **Bilingual_Mini_Variant**: The mini balanced_skills variant for cross-language pairs (en-zh, vi-zh, vi-en). 6 vocabulary words taught in 1 group, 2 sessions with activity counts 9, 5.
- **Gateway_Curriculum**: A curriculum designed as an entry point — compact enough to complete quickly, substantial enough to deliver a genuine learning experience that motivates continuation with other courses.
- **Feature_Collection**: A top-level collection on the platform that houses curriculums organized by language pair and curriculum type. Queried from the database at runtime.
- **Series**: A thematic grouping within a collection, containing multiple curriculums sharing the same language pair.
- **Curriculum**: A single learning unit with vocabulary words, sessions, and activities.
- **Session**: An ordered segment within a curriculum containing a sequence of activities.
- **Activity**: An individual learning exercise (introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence, writingParagraph).
- **Creation_Script**: A standalone Python script that calls the helloapi REST API to create a curriculum.
- **Strip_Keys**: The set of auto-generated platform keys (mp3Url, illustrationSet, segments, etc.) that must never appear in new content.
- **API**: The helloapi.step.is REST API used for all CRUD operations.
- **Display_Order**: Integer field controlling sort position of curriculums within a series.
- **Persuasive_Copy**: The required emotional sales copy style for all learner-facing text.

## Requirements

### Requirement 1: en-en Curriculum — Single-Language Mini Balanced Skills (English Speaker Learning English)

**User Story:** As a content manager, I want to create a mini en-en balanced_skills curriculum on the theme of uncomfortable growth, so that English-speaking learners get a compact gateway experience that introduces them to the mindset of embracing discomfort as a growth mechanism.

#### Acceptance Criteria

1. THE Curriculum SHALL contain exactly 5 vocabulary words in a single group, all related to growth through discomfort, resilience, and the psychology of learning.
2. THE Curriculum SHALL contain exactly 2 sessions with activity counts: S1 = 8, S2 = 6.
3. WHEN Session 1 is created, THE Session SHALL contain activities in this exact order: introAudio (welcome + teach all 5 words), viewFlashcards (5 words), speakFlashcards (5 words), vocabLevel1 (5 words), reading (passage about discomfort as growth), speakReading, readAlong, writingSentence (5 items using all 5 words).
4. WHEN Session 2 is created, THE Session SHALL contain activities in this exact order: introAudio (review all 5 words + set up full article), reading (full article combining and expanding on S1 content), speakReading, readAlong, writingParagraph (capstone composition using all vocab), introAudio (farewell — reviewing all 5 words with fresh examples).
5. THE Curriculum SHALL set `language: "en"` and `userLanguage: "en"` as top-level body parameters in the API call.
6. THE Curriculum SHALL use English for all user-facing text (title, description, preview, introAudio scripts, writing prompts).

### Requirement 2: en-zh Curriculum — Bilingual Mini Balanced Skills (English Speaker Learning Chinese)

**User Story:** As a content manager, I want to create a mini en-zh balanced_skills curriculum on the theme of uncomfortable growth, so that English-speaking learners of Chinese get a compact gateway experience that introduces them to embracing discomfort while learning a new language.

#### Acceptance Criteria

1. THE Curriculum SHALL contain exactly 6 Chinese vocabulary words in a single group, all related to growth through discomfort, resilience, and the psychology of learning.
2. THE Curriculum SHALL contain exactly 2 sessions with activity counts: S1 = 9, S2 = 5.
3. WHEN Session 1 is created, THE Session SHALL contain activities in this exact order: introAudio (welcome + teach all 6 words), viewFlashcards (6 words), speakFlashcards (6 words), vocabLevel1 (6 words), vocabLevel2 (6 words), reading (passage in Chinese about embracing discomfort), speakReading, readAlong, writingSentence (6 items using all 6 words).
4. WHEN Session 2 is created, THE Session SHALL contain activities in this exact order: introAudio (review all 6 words + set up full reading), reading (full article in Chinese), speakReading, readAlong, introAudio (farewell — reviewing all 6 words with fresh examples).
5. THE Curriculum SHALL set `language: "zh"` and `userLanguage: "en"` as top-level body parameters in the API call.
6. THE Curriculum SHALL use English for user-facing text (title, description, preview, introAudio scripts, writing prompts) and Chinese for reading passages and vocabulary target words.

### Requirement 3: vi-zh Curriculum — Bilingual Mini Balanced Skills (Vietnamese Speaker Learning Chinese)

**User Story:** As a content manager, I want to create a mini vi-zh balanced_skills curriculum on the theme of uncomfortable growth, so that Vietnamese-speaking learners of Chinese get a compact gateway experience that introduces them to the psychology of stepping outside the comfort zone.

#### Acceptance Criteria

1. THE Curriculum SHALL contain exactly 6 Chinese vocabulary words in a single group, all related to growth through discomfort, resilience, and the psychology of learning.
2. THE Curriculum SHALL contain exactly 2 sessions with activity counts: S1 = 9, S2 = 5.
3. WHEN Session 1 is created, THE Session SHALL contain activities in this exact order: introAudio (welcome + teach all 6 words), viewFlashcards (6 words), speakFlashcards (6 words), vocabLevel1 (6 words), vocabLevel2 (6 words), reading (passage in Chinese about the psychology of uncomfortable growth), speakReading, readAlong, writingSentence (6 items using all 6 words).
4. WHEN Session 2 is created, THE Session SHALL contain activities in this exact order: introAudio (review all 6 words + set up full reading), reading (full article in Chinese), speakReading, readAlong, introAudio (farewell — reviewing all 6 words with fresh examples).
5. THE Curriculum SHALL set `language: "zh"` and `userLanguage: "vi"` as top-level body parameters in the API call.
6. THE Curriculum SHALL use Vietnamese for user-facing text (title, description, preview, introAudio scripts, writing prompts) and Chinese for reading passages and vocabulary target words.

### Requirement 4: vi-en Curriculum — Bilingual Mini Balanced Skills (Vietnamese Speaker Learning English)

**User Story:** As a content manager, I want to create a mini vi-en balanced_skills curriculum on the theme of uncomfortable growth, so that Vietnamese-speaking learners of English get a compact gateway experience that introduces them to embracing discomfort as the engine of language learning.

#### Acceptance Criteria

1. THE Curriculum SHALL contain exactly 6 English vocabulary words in a single group, all related to growth through discomfort, resilience, and the psychology of learning.
2. THE Curriculum SHALL contain exactly 2 sessions with activity counts: S1 = 9, S2 = 5.
3. WHEN Session 1 is created, THE Session SHALL contain activities in this exact order: introAudio (welcome + teach all 6 words), viewFlashcards (6 words), speakFlashcards (6 words), vocabLevel1 (6 words), vocabLevel2 (6 words), reading (passage in English about stepping outside the comfort zone), speakReading, readAlong, writingSentence (6 items using all 6 words).
4. WHEN Session 2 is created, THE Session SHALL contain activities in this exact order: introAudio (review all 6 words + set up full reading), reading (full article in English), speakReading, readAlong, introAudio (farewell — reviewing all 6 words with fresh examples).
5. THE Curriculum SHALL set `language: "en"` and `userLanguage: "vi"` as top-level body parameters in the API call.
6. THE Curriculum SHALL use Vietnamese for user-facing text (title, description, preview, introAudio scripts, writing prompts) and English for reading passages and vocabulary target words.

### Requirement 5: Thematic Coherence Across All 4 Curriculums

**User Story:** As a content manager, I want all 4 mini curriculums to explore the same core theme from different cultural and linguistic angles, so that the collection feels unified while each curriculum is uniquely crafted for its audience.

#### Acceptance Criteria

1. THE 4 Curriculums SHALL share the core theme "Get comfortable being uncomfortable is the essence of language learning" but each SHALL explore it through a unique angle appropriate to its language pair and audience.
2. THE en-en Curriculum SHALL explore the theme through advanced English vocabulary about cognitive psychology, neuroplasticity, and growth mindset — targeting learners who want to upgrade their thinking vocabulary.
3. THE en-zh Curriculum SHALL explore the theme through Chinese vocabulary about perseverance, self-cultivation, and the Chinese philosophical tradition of embracing hardship for growth — targeting English speakers learning Chinese.
4. THE vi-zh Curriculum SHALL explore the theme through Chinese vocabulary about resilience, emotional regulation, and the journey of language learning — targeting Vietnamese speakers learning Chinese.
5. THE vi-en Curriculum SHALL explore the theme through English vocabulary about stepping outside the comfort zone, embracing failure, and the science of learning — targeting Vietnamese speakers learning English.
6. THE Vocabulary words across the 4 curriculums SHALL NOT be direct translations of each other — each curriculum SHALL select vocabulary native to its target language that best serves the theme for its specific audience.

### Requirement 6: Gateway Experience — The Discomfort-to-Growth Arc

**User Story:** As a content manager, I want each mini curriculum to deliver a genuine discomfort-to-growth arc despite its compact size, so that learners actually experience the theme rather than just reading about it.

#### Acceptance Criteria

1. THE Session 1 introAudio SHALL explicitly name the discomfort the learner is about to feel — acknowledging that the vocabulary and reading will be challenging — and frame it as intentional and productive.
2. THE Session 1 reading passage SHALL be written at a level that genuinely stretches the learner — the content should feel slightly beyond their comfort zone, creating the productive discomfort the theme promises.
3. THE Session 2 introAudio SHALL acknowledge the growth that happened in Session 1 — naming the shift from "this is hard" to "I can do this" — before setting up the review and full article.
4. THE Session 2 farewell introAudio SHALL explicitly connect the learner's experience in the curriculum to the broader principle: the discomfort they just felt IS the learning, and they can carry this mindset into other courses.
5. THE Curriculum description and preview SHALL position the curriculum as a gateway — a first step that introduces the mindset, with an implicit invitation to continue learning on the platform.

### Requirement 7: Content Quality — Persuasive Copy

**User Story:** As a content manager, I want all learner-facing text to follow the persuasive copy style, so that learners feel emotionally engaged and motivated to embrace the discomfort of language learning.

#### Acceptance Criteria

1. THE Curriculum description SHALL follow the 5-beat persuasive copy structure: bold headline hitting a pain point about the fear of making mistakes or feeling uncomfortable, concrete personal examples of language-learning awkwardness, vivid metaphor about growth through discomfort, transformation promise, and dual growth tie-in.
2. THE Curriculum preview (~150 words) SHALL open with a vivid hook about the discomfort of language learning, name the vocabulary words, describe the learning journey, and read as compelling marketing copy.
3. WHEN the Session 1 introAudio is created, THE introAudio script (400-600 words for mini) SHALL teach each vocabulary word individually with part of speech, definition, example sentence from the reading context, and smooth transitions between words.
4. WHEN the farewell introAudio is created, THE script (300-500 words for mini) SHALL review each vocabulary word with a fresh example sentence and provide a warm farewell that reinforces the theme of embracing discomfort and invites continuation.
5. THE Curriculum SHALL use the appropriate user language for all user-facing text: English for en-en and en-zh, Vietnamese for vi-en and vi-zh.

### Requirement 8: Activity Metadata

**User Story:** As a content manager, I want every activity to have proper title and description fields, so that server-side logging and client display work correctly.

#### Acceptance Criteria

1. THE Activity SHALL include `title` and `description` fields for every activity in every session.
2. WHEN a `viewFlashcards`, `speakFlashcards`, `vocabLevel1`, or `vocabLevel2` activity is created, THE Activity title SHALL follow the format "Flashcards: <topic>" (single-language) or the equivalent in the user language (bilingual), and the description SHALL list the words being learned.
3. WHEN a `reading` or `speakReading` activity is created, THE Activity title SHALL follow the format "Read: <topic>" (en-en, en-zh) or "Đọc: <topic>" (vi-en, vi-zh), and the description SHALL contain the first ~80 characters of the reading text.
4. WHEN a `readAlong` activity is created, THE Activity title SHALL follow the format "Listen: <topic>" (en-en, en-zh) or "Nghe: <topic>" (vi-en, vi-zh).
5. WHEN an `introAudio` activity is created, THE Activity title SHALL be a descriptive label and the description SHALL be a brief summary.
6. WHEN a `writingSentence` or `writingParagraph` activity is created, THE Activity title SHALL follow the format "Write: <topic>" (en-en, en-zh) or "Viết: <topic>" (vi-en, vi-zh).
7. THE Session object SHALL include a `title` field appropriate to the user language.

### Requirement 9: Strip-Keys Compliance

**User Story:** As a content manager, I want new curriculum content to never include auto-generated platform keys, so that the platform correctly generates fresh metadata after upload.

#### Acceptance Criteria

1. THE Curriculum content SHALL NOT include any of the following auto-generated keys: `mp3Url`, `illustrationSet`, `chapterBookmarks`, `segments`, `whiteboardItems`, `userReadingId`, `lessonUniqueId`, `curriculumTags`, `taskId`, `imageId`.
2. IF an existing curriculum is fetched via API to use as a structural template, THEN THE Creation_Script SHALL run `strip_keys()` on the fetched content before using it as input for `curriculum/create`.

### Requirement 10: Feature Collection Placement

**User Story:** As a content manager, I want each curriculum placed in the appropriate feature collection for its language pair, so that learners can discover the curriculum alongside other content in their language.

#### Acceptance Criteria

1. WHEN a curriculum is created, THE Creation_Script SHALL query the database to find the appropriate existing feature collection and series for the curriculum's language pair.
2. IF no appropriate collection or series exists for a language pair, THEN THE Creation_Script SHALL create a new collection and/or series with a descriptive title and persuasive description.
3. WHEN a curriculum is added to a series, THE Creation_Script SHALL call `curriculum/setDisplayOrder` to assign the next appropriate display order value based on existing curriculums in the series.
4. THE Creation_Script SHALL verify language homogeneity after adding each curriculum — the series must contain only curriculums with the same `language` and `user_language`.

### Requirement 11: Newly Created Curriculums Must Be Private

**User Story:** As a content manager, I want all newly created curriculums to be private by default, so that they go through content generation (audio, illustrations) before being exposed to learners.

#### Acceptance Criteria

1. WHEN a curriculum is created via `curriculum/create`, THE Curriculum SHALL have `is_public: false` (the platform default).
2. THE Creation_Script SHALL NOT call `curriculum/setPublic` with `isPublic: true` on any newly created curriculum.

### Requirement 12: Script Organization

**User Story:** As a content manager, I want one Python script per curriculum, so that each curriculum's content is self-contained and files remain manageable.

#### Acceptance Criteria

1. THE Creation_Script architecture SHALL use one Python script per curriculum with all text content hand-written in that script.
2. THE Creation_Script SHALL NOT use template functions, string interpolation, or loops to generate learner-facing text content.
3. THE Creation_Script MAY use shared helper functions for activity structure (types, order, data schema) but SHALL hand-write all text content per curriculum.
4. WHEN a curriculum is successfully created and verified in the database, THE source script SHALL be deleted, leaving only a README with creation method, SQL queries, and recreation context.

### Requirement 13: No Templated Content

**User Story:** As a content manager, I want every piece of learner-facing text to be individually crafted per curriculum, so that each curriculum reads as if written by someone who deeply understands the theme from that specific cultural and linguistic perspective.

#### Acceptance Criteria

1. THE Creation_Script SHALL NOT use `f-string` interpolation, template functions, or shared text skeletons to generate introAudio scripts, reading passages, descriptions, previews, or writing prompts.
2. EACH Curriculum's reading passages SHALL be original content exploring the uncomfortable growth theme from the unique perspective of its target audience — not translations or adaptations of the other curriculums' passages.
3. EACH Curriculum's introAudio scripts SHALL be individually crafted to teach vocabulary in a way that resonates with the specific audience (e.g., Chinese philosophical references for en-zh, Vietnamese cultural context for vi-zh).

### Requirement 14: Writing Prompts

**User Story:** As a content manager, I want writing prompts to be specific and contextual, so that learners practice vocabulary in meaningful sentences and paragraphs about the theme of uncomfortable growth.

#### Acceptance Criteria

1. THE `writingSentence` activity SHALL provide a detailed prompt specifying the context for using the word, plus an example sentence showing correct usage.
2. WHEN a bilingual `writingSentence` prompt is created, THE prompt SHALL be written in the user language with the example sentence in the target language.
3. WHEN a single-language `writingSentence` prompt is created, THE prompt SHALL be written entirely in the target language with context and example.
4. WHEN a `writingParagraph` activity is created (en-en S2 only), THE activity SHALL include a `prompt` field with a clear composition task that references the theme of uncomfortable growth and specifies the expected scope, and a `vocabList` field containing the vocabulary words the learner is expected to use.

### Requirement 15: Duplicate Check After Creation

**User Story:** As a content manager, I want to check for duplicate curriculums after creation, so that accidental re-runs of scripts don't create duplicate entries.

#### Acceptance Criteria

1. WHEN a curriculum is created, THE Creation_Script SHALL query the database for curriculums with the same title and language owned by the same user.
2. IF duplicates are found, THEN THE Creation_Script SHALL delete the extras (keeping the earliest-created one) and verify series membership is correct.

### Requirement 16: Folder and README Structure

**User Story:** As a content manager, I want the uncomfortable-growth series to have its own folder with a README tracking creation details, so that content is recoverable and auditable.

#### Acceptance Criteria

1. THE workspace SHALL contain a dedicated folder `uncomfortable-growth-curriculum/` for the series.
2. WHEN all 4 curriculums are successfully created, THE folder SHALL contain a README.md documenting: which collections and series each curriculum was placed in (with IDs), curriculum IDs and titles for all 4, how content was created, SQL queries to find the curriculums in the DB, and enough context to recreate if needed.
3. WHEN all curriculums are verified in the database, THE source Python scripts SHALL be deleted from the folder, leaving only the README.

### Requirement 17: Language and Level Compliance

**User Story:** As a content manager, I want all curriculums to comply with the platform's language policy, so that text is in the correct language for each audience.

#### Acceptance Criteria

1. THE en-en Curriculum SHALL use English for all text (single-language, advanced level).
2. THE en-zh Curriculum SHALL use English for user-facing text and Chinese for reading passages and vocabulary (bilingual).
3. THE vi-zh Curriculum SHALL use Vietnamese for user-facing text and Chinese for reading passages and vocabulary (bilingual).
4. THE vi-en Curriculum SHALL use Vietnamese for user-facing text and English for reading passages and vocabulary (bilingual).
5. THE Curriculum title SHALL NOT include difficulty level descriptors (e.g., "Beginner", "Intermediate", "Advanced").
