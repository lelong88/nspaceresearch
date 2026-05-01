# Requirements Document

## Introduction

Create 10 English-learning curriculums specifically designed for Vietnamese-speaking children aged 6-10. Language pair: userLanguage="vi", language="en". Difficulty levels: beginner (6 curriculums) and preintermediate (4 curriculums).

The existing vi-en catalog has 61 beginner and 59 preintermediate curriculums, but none are designed for children. All existing content targets adult or general-audience learners. These 10 curriculums fill a critical gap by providing age-appropriate, child-friendly English learning experiences with topics that resonate with Vietnamese children — animals, colors, playground, toys, school life, family activities, and nature.

### What This Spec Covers

- 10 individually crafted curriculums for Vietnamese children aged 6-10 learning English
- Child-friendly topics, vocabulary, and activity design
- Age-appropriate persuasive copy (written for parents, since parents purchase)
- Collection and series organization for the children's curriculum line
- Pricing per the beginner/preintermediate guidelines
- Creation workflow, validation, and documentation

### What This Spec Does NOT Cover

- Changes to existing vi-en curriculums
- Children's curriculums for other language pairs (vi-zh, en-en, etc.)
- Content generation pipeline (audio, illustrations) — curriculums are created private
- Advanced or intermediate difficulty levels (not appropriate for ages 6-10)

## Glossary

- **Children_Curriculum**: A curriculum designed for Vietnamese children aged 6-10 learning English. Uses simpler vocabulary (3-5 words for mini, 8-10 words for short), shorter reading passages, playful tone, and age-appropriate topics. All user-facing marketing text targets parents (the purchasers).
- **Curriculum_Creator**: The system of standalone Python scripts that generate curriculum JSON content and upload it via the REST API.
- **Content_Validator**: Validation logic that checks curriculum JSON against the Content Corruption Detection Rules before upload.
- **Collection_Organizer**: The orchestrator script that creates collections, series, wires them together, and sets display orders via the REST API.
- **Tone_Assigner**: The logic that assigns description tones and farewell tones to each curriculum and series, ensuring variety constraints are met.
- **Language_Pair**: userLanguage="vi", language="en" — Vietnamese children learning English.
- **Parent_Copy**: Persuasive marketing text written for Vietnamese parents who are purchasing the curriculum for their child. Uses the standard 5-beat persuasive copy structure but addresses parental aspirations and concerns about their child's English education.
- **Child_Content**: Learner-facing content (introAudio scripts, reading passages, writing prompts) written in a warm, playful, encouraging tone appropriate for children aged 6-10. Uses simple Vietnamese explanations and child-friendly English vocabulary.
- **Persuasive_Copy**: The required writing style for marketing text — emotional sales copy with bold headline, concrete examples, vivid metaphor, transformation promise, and personal growth tie-in.
- **Tone_Palette**: The 6 rhetorical opener types: provocative_question, bold_declaration, vivid_scenario, empathetic_observation, surprising_fact, metaphor_led.
- **Farewell_Palette**: The 5 emotional registers for farewell introAudio scripts: introspective_guide, warm_accountability, team_building_energy, quiet_awe, practical_momentum.
- **Strip_Keys**: Auto-generated platform keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId) that must never be included in new curriculum content.
- **Mini_Curriculum**: A single-session curriculum with 3-5 vocabulary words, priced at 9 credits (beginner).
- **Short_Curriculum**: A 4-session curriculum with 8-10 vocabulary words, priced at 19 credits (beginner) or 49 credits (preintermediate).

## Requirements

### Requirement 1: Children's Curriculum Format and Structure

**User Story:** As a platform owner, I want 10 English-learning curriculums designed specifically for Vietnamese children aged 6-10, so that young learners have age-appropriate content that makes learning English fun and engaging.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL produce exactly 10 Children_Curriculums for the vi-en language pair.
2. THE Curriculum_Creator SHALL create 6 beginner-level curriculums and 4 preintermediate-level curriculums.
3. WHEN a beginner mini Children_Curriculum is created, THE curriculum SHALL contain exactly 1 learning session with 3-5 vocabulary words.
4. WHEN a beginner short Children_Curriculum is created, THE curriculum SHALL contain 4 learning sessions with 8-10 vocabulary words divided into 2 groups.
5. WHEN a preintermediate Children_Curriculum is created, THE curriculum SHALL contain 4 learning sessions with 10-12 vocabulary words divided into 2-3 groups.
6. THE Children_Curriculum SHALL include `contentTypeTags: []` at the top level of the content JSON (topic-based).
7. THE Children_Curriculum SHALL never include Strip_Keys in the content JSON.
8. THE Curriculum_Creator SHALL set `language: "en"` and `userLanguage: "vi"` as top-level body parameters in the `curriculum/create` API call.

### Requirement 2: Topic Plan for 10 Children's Curriculums

**User Story:** As a platform owner, I want child-friendly topics that resonate with Vietnamese children aged 6-10, so that young learners are excited to study English through familiar, fun subjects.

#### Acceptance Criteria

1. THE 10 Children_Curriculums SHALL cover the following topics, each individually crafted:

   **Beginner Mini (3-5 words, 1 session, 9 credits) — 3 curriculums:**
   - Curriculum 1: "Thế Giới Màu Sắc" (World of Colors) — colors children see every day: red, blue, green, yellow, orange
   - Curriculum 2: "Bạn Thú Cưng" (Pet Friends) — common pets: dog, cat, fish, bird, rabbit
   - Curriculum 3: "Đồ Chơi Của Em" (My Toys) — toys children play with: ball, doll, car, kite, puzzle

   **Beginner Short (8-10 words, 4 sessions, 19 credits) — 3 curriculums:**
   - Curriculum 4: "Sân Chơi Vui Nhộn" (Fun Playground) — playground vocabulary: swing, slide, climb, jump, run, sand, friend, play, turn, share
   - Curriculum 5: "Vườn Thú Kỳ Diệu" (Amazing Zoo) — zoo animals: elephant, monkey, lion, giraffe, tiger, bear, penguin, snake, zebra, parrot
   - Curriculum 6: "Một Ngày Ở Trường" (A Day at School) — school life: teacher, student, book, pencil, desk, lunch, recess, homework, classroom, backpack

   **Preintermediate Short (10-12 words, 4 sessions, 49 credits) — 4 curriculums:**
   - Curriculum 7: "Khám Phá Thiên Nhiên" (Exploring Nature) — nature vocabulary: forest, river, mountain, butterfly, flower, leaf, rainbow, cloud, sunshine, rain, nest, seed
   - Curriculum 8: "Gia Đình Vui Vẻ" (Happy Family) — family activities: breakfast, dinner, weekend, picnic, garden, bicycle, story, bedtime, together, celebrate, grandparent, cousin
   - Curriculum 9: "Siêu Anh Hùng Nhí" (Little Superheroes) — character traits and actions: brave, kind, strong, help, rescue, protect, team, power, dream, believe, adventure, hero
   - Curriculum 10: "Lễ Hội Và Mùa" (Festivals and Seasons) — Vietnamese and international celebrations: spring, summer, autumn, winter, festival, lantern, firework, gift, costume, parade, tradition, celebrate

2. THE Curriculum_Creator SHALL select vocabulary words that are concrete, high-frequency, and visually representable for children aged 6-10.
3. THE Curriculum_Creator SHALL ensure no two curriculums have overlapping vocabulary lists.
4. WHEN creating reading passages for children, THE Curriculum_Creator SHALL use simple sentences (under 10 words average for beginner, under 12 words for preintermediate), present tense primarily, and vocabulary that a 6-10 year old Vietnamese child can relate to.

### Requirement 3: Age-Appropriate Content Design

**User Story:** As a content quality owner, I want all learner-facing content designed for children aged 6-10, so that young learners feel engaged, safe, and encouraged throughout the learning experience.

#### Acceptance Criteria

1. WHEN Child_Content is created for introAudio scripts, THE scripts SHALL use a warm, playful, encouraging tone — as if a friendly teacher is speaking to a child. Use simple Vietnamese sentences, enthusiastic language, and gentle encouragement.
2. WHEN Child_Content is created for reading passages, THE passages SHALL feature child-relatable scenarios: playing with friends, going to school, visiting the zoo, exploring nature, family activities. No abstract concepts, no adult themes.
3. WHEN Child_Content is created for writingSentence prompts, THE prompts SHALL provide maximum scaffolding: full Vietnamese instructions written simply for a child, a complete English example sentence the child can closely imitate, and a clear fill-in-the-blank or word-substitution pattern requiring only 1 word change.
4. THE Children_Curriculum SHALL NOT include `writingParagraph` activities (too complex for ages 6-10).
5. THE Children_Curriculum SHALL NOT include `vocabLevel3` activities (to reduce cognitive load for young learners).
6. WHEN a beginner mini Children_Curriculum is created, THE curriculum SHALL NOT include `vocabLevel1` or `vocabLevel2` activities (mini format focuses on flashcards, reading, and speaking).
7. THE introAudio farewell scripts SHALL use an especially warm, celebratory tone — praising the child's effort, using phrases like "con giỏi lắm!" (you did great!), and encouraging them to practice with family.

### Requirement 4: Activity Templates for Children's Curriculums

**User Story:** As a platform owner, I want activity sequences optimized for children's attention spans and learning patterns, so that young learners stay engaged throughout each session.

#### Acceptance Criteria

1. WHEN a beginner mini Children_Curriculum is created, THE session SHALL include activities in this order: introAudio (welcome + teach all words with playful context), viewFlashcards, speakFlashcards, reading (short passage, 40-60 words), speakReading, readAlong, introAudio (farewell with vocab review and praise).

2. WHEN a beginner short Children_Curriculum is created, THE 4 sessions SHALL follow this structure:
   - Session 1: introAudio (welcome + teach words group 1), viewFlashcards (group 1), speakFlashcards (group 1), vocabLevel1 (group 1), reading (short passage using group 1 words, 60-80 words), readAlong, introAudio (session wrap-up)
   - Session 2: introAudio (recap group 1 + teach words group 2), viewFlashcards (group 2), speakFlashcards (group 2), vocabLevel1 (group 2), reading (short passage using group 2 words, 60-80 words), readAlong, introAudio (session wrap-up)
   - Session 3 (Review): introAudio (review intro), viewFlashcards (all words), speakFlashcards (all words), vocabLevel1 (all words), vocabLevel2 (all words), writingSentence (3-4 items), introAudio (review wrap-up)
   - Session 4 (Final): introAudio (final reading intro), reading (combined passage using all words, 100-120 words), speakReading, readAlong, writingSentence (2-3 items), introAudio (farewell with full vocab review and celebration)

3. WHEN a preintermediate short Children_Curriculum is created, THE 4 sessions SHALL follow this structure:
   - Session 1: introAudio (welcome + teach words group 1), viewFlashcards (group 1), speakFlashcards (group 1), vocabLevel1 (group 1), vocabLevel2 (group 1), reading (passage using group 1 words, 80-100 words), speakReading, readAlong, introAudio (session wrap-up)
   - Session 2: introAudio (recap group 1 + teach words group 2), viewFlashcards (group 2), speakFlashcards (group 2), vocabLevel1 (group 2), vocabLevel2 (group 2), reading (passage using group 2 words, 80-100 words), speakReading, readAlong, introAudio (session wrap-up)
   - Session 3 (Review): introAudio (review intro), viewFlashcards (all words), speakFlashcards (all words), vocabLevel1 (all words), vocabLevel2 (all words), writingSentence (4-5 items), introAudio (review wrap-up)
   - Session 4 (Final): introAudio (final reading intro), reading (combined passage using all words, 150-180 words), speakReading, readAlong, writingSentence (3-4 items), introAudio (farewell with full vocab review and celebration)

### Requirement 5: Parent-Facing Marketing Copy

**User Story:** As a content quality owner, I want all marketing text (title, description, preview) to speak to Vietnamese parents, so that parents understand the value and feel confident purchasing these curriculums for their children.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL write curriculum descriptions as Parent_Copy following the Persuasive_Copy 5-beat structure, but addressing parental aspirations: their child's future, early English advantage, confidence building, and fun learning.
2. THE Curriculum_Creator SHALL write curriculum previews (~100-150 words) as Parent_Copy with vivid hooks about the child's learning journey, vocabulary word listing, and what the child will be able to do after completing the curriculum.
3. THE Curriculum_Creator SHALL write all titles, descriptions, and preview text in Vietnamese (as required for beginner/preintermediate vi-en curriculums).
4. THE Tone_Assigner SHALL assign one of the 6 Tone_Palette types to every curriculum description headline.
5. WHILE assigning tones within a series, THE Tone_Assigner SHALL ensure no two adjacent curriculums use the same Tone_Palette type.
6. THE Tone_Assigner SHALL ensure no single Tone_Palette type exceeds 30% of the 10 curriculum descriptions.
7. THE Parent_Copy SHALL NOT use fear-based marketing or shame-based language about children's abilities. The tone SHALL be aspirational, warm, and encouraging — celebrating the child's potential.

### Requirement 6: introAudio Quality for Children

**User Story:** As a content quality owner, I want introAudio scripts crafted specifically for young learners, so that children feel welcomed, engaged, and celebrated throughout the learning experience.

#### Acceptance Criteria

1. WHEN a welcome introAudio is created for a mini curriculum, THE script (200-350 words) SHALL greet the child warmly, introduce the topic with a fun hook (e.g., "Hôm nay chúng ta sẽ khám phá thế giới đầy màu sắc!"), list all vocabulary words, and teach each word with: the English word, Vietnamese meaning, a simple example sentence a child can understand, and a fun fact or association to help remember.
2. WHEN a welcome introAudio is created for a short/preintermediate curriculum, THE script (300-500 words) SHALL follow the same pattern as criterion 1 but with more words and slightly more context per word.
3. WHEN a session recap introAudio is created (sessions 2+), THE script SHALL briefly and playfully recap previous words before introducing new ones — using phrases like "Các bạn còn nhớ không?" (Do you remember?).
4. WHEN a farewell introAudio is created, THE script (200-400 words) SHALL review key vocabulary words with fresh child-friendly example sentences, celebrate the child's achievement with enthusiastic praise, and encourage practicing with family or friends.
5. THE introAudio scripts SHALL be fully bilingual with simple Vietnamese explanations for every English word and concept.
6. THE Curriculum_Creator SHALL individually craft every introAudio script for its specific curriculum topic, without using template functions or string interpolation.
7. THE Tone_Assigner SHALL assign one of the 5 Farewell_Palette registers to every farewell introAudio, adapted for a child audience (e.g., "warm accountability" becomes gentle encouragement to practice, "quiet awe" becomes wonder at what they learned).
8. WHILE assigning farewell tones within a series, THE Tone_Assigner SHALL ensure no two adjacent curriculums use the same Farewell_Palette register.

### Requirement 7: Pricing

**User Story:** As a platform owner, I want children's curriculums priced according to the standard pricing guidelines, so that pricing is consistent with the rest of the catalog.

#### Acceptance Criteria

1. WHEN a beginner mini Children_Curriculum (1 session) is created, THE Curriculum_Creator SHALL call `curriculum/setPrice` with `price: 9`.
2. WHEN a beginner short Children_Curriculum (4 sessions) is created, THE Curriculum_Creator SHALL call `curriculum/setPrice` with `price: 19`.
3. WHEN a preintermediate short Children_Curriculum (4 sessions) is created, THE Curriculum_Creator SHALL call `curriculum/setPrice` with `price: 49`.
4. THE Curriculum_Creator SHALL set the price after the curriculum is successfully created and added to its series.

### Requirement 8: Collection and Series Organization

**User Story:** As a platform owner, I want the 10 children's curriculums organized into a dedicated collection and series, so that parents can easily find and browse all children's English content.

#### Acceptance Criteria

1. THE Collection_Organizer SHALL create 1 collection titled "Tiếng Anh Cho Bé 6-10 Tuổi" (English for Kids 6-10) with a neutral, informative Vietnamese description explaining this is a collection of English curriculums designed for Vietnamese children aged 6-10.
2. THE Collection_Organizer SHALL organize the 10 curriculums into 2 series:
   - Series 1: "Bước Đầu Tiên" (First Steps) — containing the 6 beginner curriculums (3 mini + 3 short). Description ≤255 chars using a Tone_Palette type.
   - Series 2: "Khám Phá Thêm" (Explore More) — containing the 4 preintermediate curriculums. Description ≤255 chars using a different Tone_Palette type.
3. THE Collection_Organizer SHALL wire each series to the collection via `curriculum-collection/addSeriesToCollection`.
4. THE Collection_Organizer SHALL set display orders for both series within the collection via `curriculum-series/setDisplayOrder`.
5. THE Collection_Organizer SHALL set display orders for all curriculums within each series via `curriculum/setDisplayOrder`.
6. THE Collection_Organizer SHALL ensure all curriculums within each series share `language: "en"` and `userLanguage: "vi"`.
7. WHILE assigning series description tones, THE Tone_Assigner SHALL ensure the 2 series use different Tone_Palette types.

### Requirement 9: Activity Schema Compliance

**User Story:** As a platform developer, I want every activity to comply with the platform's content schema, so that the content pipeline processes children's curriculums without errors.

#### Acceptance Criteria

1. Each Activity SHALL include `activityType`, `title`, `description`, and `data` fields.
2. THE `activityType` field SHALL use one of the valid values: introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence.
3. THE `vocabList` field SHALL be an array of lowercase strings, using the field name `vocabList` (never `words`).
4. WHEN viewFlashcards and speakFlashcards appear in the same session, THE two activities SHALL have identical `vocabList` arrays.
5. All content data SHALL be inside the `data` object, not inline on the activity object.
6. WHEN a writingSentence activity is created, THE activity SHALL have `data.vocabList`, `data.items` (non-empty array), and each item SHALL have `prompt` (simple Vietnamese instructions with example sentence and substitution pattern) and `targetVocab` fields.
7. THE Curriculum_Creator SHALL follow the activity title/description conventions: viewFlashcards/speakFlashcards/vocabLevel* use "Flashcards: <topic>"; reading/speakReading use "Đọc: <topic>"; readAlong uses "Nghe: <topic>"; introAudio uses descriptive labels; writingSentence uses "Viết: <topic>".

### Requirement 10: Content Validation

**User Story:** As a platform developer, I want every children's curriculum validated before upload, so that no corrupted content enters the database.

#### Acceptance Criteria

1. THE Content_Validator SHALL verify that every Children_Curriculum content JSON has non-null, non-empty `title`, `description`, and `preview.text` fields.
2. THE Content_Validator SHALL verify that `learningSessions` is a non-empty array, with each session having a non-empty `title` and `activities` array.
3. THE Content_Validator SHALL verify that every activity has `activityType` (not `type`), `title`, `description`, and `data` fields, with content fields inside `data`.
4. THE Content_Validator SHALL verify that `activityType` values are valid.
5. THE Content_Validator SHALL verify that vocabList fields contain arrays of lowercase strings using the field name `vocabList`.
6. THE Content_Validator SHALL verify that viewFlashcards and speakFlashcards in the same session have identical vocabList arrays.
7. THE Content_Validator SHALL verify writingSentence data structures (vocabList, items with prompt and targetVocab).
8. THE Content_Validator SHALL verify that no Strip_Keys appear anywhere in the content JSON.
9. THE Content_Validator SHALL verify that no `writingParagraph` or `vocabLevel3` activities exist in any Children_Curriculum.
10. IF any validation check fails, THEN THE Content_Validator SHALL abort the upload and print the specific rule violation.

### Requirement 11: Script Architecture and Workflow

**User Story:** As a developer, I want a clear, repeatable workflow for creating 10 children's curriculums, so that the process is manageable and traceable.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL produce one standalone Python script per curriculum (10 scripts total).
2. THE Curriculum_Creator SHALL produce one orchestrator script that creates the collection, series, wires them together, sets display orders, and sets prices.
3. THE Curriculum_Creator SHALL organize scripts into a directory `vi-en-children-curriculum/`.
4. THE Curriculum_Creator SHALL authenticate all API calls using `firebase_token.get_firebase_id_token` with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`.
5. THE Curriculum_Creator SHALL use `https://helloapi.step.is` as the API base URL.
6. THE Curriculum_Creator SHALL individually craft every piece of learner-facing text for its specific curriculum topic, without using template functions, string interpolation, or generic fill-in-the-blank patterns.
7. THE Curriculum_Creator MAY use shared helper functions for activity structure (types, order, data schema) but SHALL hand-write all text content per curriculum.
8. IF a curriculum creation API call fails, THEN THE Curriculum_Creator SHALL log the error with the curriculum title and continue with the next curriculum.

### Requirement 12: Newly Created Curriculums Must Be Private

**User Story:** As a platform owner, I want all newly created children's curriculums to be private by default, so that they go through content generation (audio, illustrations) before being exposed to learners.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL NOT call `curriculum/setPublic` with `isPublic: true` on any newly created Children_Curriculum.

### Requirement 13: Curriculum Titles

**User Story:** As a content quality owner, I want curriculum titles to be minimal, child-friendly, and in Vietnamese, so that they work well within the series/collection context.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL keep curriculum titles minimal — never repeating series/collection name, content type prefix, skill-focus label, difficulty level, or audience suffix.
2. THE Curriculum_Creator SHALL write curriculum titles in Vietnamese.
3. THE curriculum titles SHALL NOT include difficulty level indicators (e.g., "beginner", "sơ cấp").
4. THE curriculum titles SHALL be engaging and child-friendly — using playful, imaginative language that appeals to both children and parents.

### Requirement 14: Documentation and Cleanup

**User Story:** As a developer, I want proper documentation after all curriculums are created, so that the content is traceable and reproducible.

#### Acceptance Criteria

1. WHEN all 10 curriculums are created and verified, THE Curriculum_Creator SHALL create a README.md documenting: collection ID, all series IDs, all curriculum IDs with titles and display orders, vocabulary lists per curriculum, tone assignments (description and farewell), pricing, and SQL verification queries.
2. WHEN all curriculums are verified in the database, THE source Python scripts SHALL be deleted, leaving only the README.
3. THE Curriculum_Creator SHALL run a duplicate check query for each curriculum title after creation and resolve any duplicates (keep earliest, delete extras).

### Requirement 15: Execution Order

**User Story:** As a developer, I want a phased execution plan, so that I can create the infrastructure first and then add curriculums incrementally.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL execute creation in this order: (1) create collection and series via orchestrator, (2) create beginner mini curriculums (3 scripts), (3) create beginner short curriculums (3 scripts), (4) create preintermediate short curriculums (4 scripts).
2. WHEN each curriculum is created, THE Curriculum_Creator SHALL immediately add it to the appropriate series, set its display order, and set its price.
3. WHEN all 10 curriculums are created, THE Curriculum_Creator SHALL verify the complete set by querying the database to confirm all curriculums exist with correct display orders, language values, prices, and non-empty content.
4. IF verification reveals missing or malformed curriculums, THEN THE Curriculum_Creator SHALL recreate the affected curriculums before finalizing documentation.
