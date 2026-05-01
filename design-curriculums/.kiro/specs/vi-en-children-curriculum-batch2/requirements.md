# Requirements Document

## Introduction

Create 10 MORE English-learning curriculums for Vietnamese-speaking children aged 6-10 (Batch 2). Language pair: userLanguage="vi", language="en". Difficulty levels: beginner (6 curriculums) and preintermediate (4 curriculums).

This is the second batch of children's curriculums, expanding the existing collection "Tiếng Anh Cho Bé 6-10 Tuổi" (ID: `uyw1ywsg`). Batch 1 already created 10 curriculums across 2 series covering colors, pets, toys, playground, zoo, school, nature, family, superheroes, and festivals. Batch 2 adds 10 new curriculums with completely different topics (vehicles, fruits, body parts, weather, food, clothing, numbers, shapes, ocean animals, sports) and zero vocabulary overlap with Batch 1.

### What This Spec Covers

- 10 individually crafted NEW curriculums for Vietnamese children aged 6-10 learning English
- New child-friendly topics: vehicles, fruits, body parts, weather, food, clothing, numbers, shapes, ocean animals, sports
- Addition to the EXISTING collection and series (no new collection/series creation)
- Zero vocabulary overlap with the 10 Batch 1 curriculums
- Same formats, pricing, activity schemas, and quality standards as Batch 1
- Reuse of existing `vi-en-children-curriculum/validate_content.py` and root-level `api_helpers.py`
- Display orders continuing from where Batch 1 left off

### What This Spec Does NOT Cover

- Changes to existing Batch 1 curriculums
- Creation of new collections or series (reuses existing ones)
- Children's curriculums for other language pairs
- Content generation pipeline (audio, illustrations) — curriculums are created private
- Advanced or intermediate difficulty levels

### Existing Infrastructure (from Batch 1)

| Entity | ID | Title |
|---|---|---|
| Collection | `uyw1ywsg` | Tiếng Anh Cho Bé 6-10 Tuổi |
| Series 1 | `8ncwoino` | Bước Đầu Tiên (beginner, currently 6 curriculums, display orders 1-6) |
| Series 2 | `l8l9bexl` | Khám Phá Thêm (preintermediate, currently 4 curriculums, display orders 1-4) |

### Batch 1 Vocabulary (MUST NOT overlap)

All words from Batch 1 that are off-limits for Batch 2:
- red, blue, green, yellow, orange
- dog, cat, fish, bird, rabbit
- ball, doll, car, kite, puzzle
- swing, slide, climb, jump, run, sand, friend, play, turn, share
- elephant, monkey, lion, giraffe, tiger, bear, penguin, snake, zebra, parrot
- teacher, student, book, pencil, desk, lunch, recess, homework, classroom, backpack
- forest, river, mountain, butterfly, flower, leaf, rainbow, cloud, sunshine, rain, nest, seed
- breakfast, dinner, weekend, picnic, garden, bicycle, story, bedtime, together, celebrate, grandparent, cousin
- brave, kind, strong, help, rescue, protect, team, power, dream, believe, adventure, hero
- spring, summer, autumn, winter, festival, lantern, firework, gift, costume, parade, tradition, celebrate

## Glossary

- **Children_Curriculum**: A curriculum designed for Vietnamese children aged 6-10 learning English. Uses simpler vocabulary (3-5 words for mini, 8-10 words for short), shorter reading passages, playful tone, and age-appropriate topics. All user-facing marketing text targets parents (the purchasers).
- **Curriculum_Creator**: The system of standalone Python scripts that generate curriculum JSON content and upload it via the REST API.
- **Content_Validator**: The existing `vi-en-children-curriculum/validate_content.py` module that checks curriculum JSON against format rules before upload. Reused from Batch 1 without modification.
- **Batch1_Vocabulary**: The complete set of vocabulary words used across all 10 Batch 1 curriculums (listed above). No word from this set may appear in any Batch 2 curriculum's vocabList.
- **Tone_Assigner**: The logic that assigns description tones and farewell tones to each curriculum, ensuring variety constraints are met across the new batch AND adjacency constraints within each series (considering existing Batch 1 curriculums' final tones).
- **Language_Pair**: userLanguage="vi", language="en" — Vietnamese children learning English.
- **Parent_Copy**: Persuasive marketing text written for Vietnamese parents who are purchasing the curriculum for their child. Uses the standard 5-beat persuasive copy structure but addresses parental aspirations.
- **Child_Content**: Learner-facing content (introAudio scripts, reading passages, writing prompts) written in a warm, playful, encouraging tone appropriate for children aged 6-10.
- **Persuasive_Copy**: The required writing style for marketing text — emotional sales copy with bold headline, concrete examples, vivid metaphor, transformation promise, and personal growth tie-in.
- **Tone_Palette**: The 6 rhetorical opener types: provocative_question, bold_declaration, vivid_scenario, empathetic_observation, surprising_fact, metaphor_led.
- **Farewell_Palette**: The 5 emotional registers for farewell introAudio scripts: introspective_guide, warm_accountability, team_building_energy, quiet_awe, practical_momentum.
- **Strip_Keys**: Auto-generated platform keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId) that must never be included in new curriculum content.
- **Mini_Curriculum**: A single-session curriculum with 3-5 vocabulary words, priced at 9 credits (beginner).
- **Short_Curriculum**: A 4-session curriculum with 8-10 vocabulary words, priced at 19 credits (beginner) or 49 credits (preintermediate).

## Requirements

### Requirement 1: Batch 2 Children's Curriculum Format and Structure

**User Story:** As a platform owner, I want 10 MORE English-learning curriculums designed for Vietnamese children aged 6-10, so that the children's catalog expands with fresh topics while maintaining the same quality and format standards.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL produce exactly 10 new Children_Curriculums for the vi-en language pair.
2. THE Curriculum_Creator SHALL create 6 beginner-level curriculums and 4 preintermediate-level curriculums.
3. WHEN a beginner mini Children_Curriculum is created, THE curriculum SHALL contain exactly 1 learning session with 3-5 vocabulary words.
4. WHEN a beginner short Children_Curriculum is created, THE curriculum SHALL contain 4 learning sessions with 8-10 vocabulary words divided into 2 groups.
5. WHEN a preintermediate Children_Curriculum is created, THE curriculum SHALL contain 4 learning sessions with 10-12 vocabulary words divided into 2-3 groups.
6. THE Children_Curriculum SHALL include `contentTypeTags: []` at the top level of the content JSON (topic-based).
7. THE Children_Curriculum SHALL never include Strip_Keys in the content JSON.
8. THE Curriculum_Creator SHALL set `language: "en"` and `userLanguage: "vi"` as top-level body parameters in the `curriculum/create` API call.

### Requirement 2: Topic Plan for 10 New Children's Curriculums (Batch 2)

**User Story:** As a platform owner, I want 10 new child-friendly topics that are completely different from Batch 1, so that the children's catalog offers broad coverage of everyday English vocabulary.

#### Acceptance Criteria

1. THE 10 new Children_Curriculums SHALL cover the following topics, each individually crafted:

   **Beginner Mini (3-5 words, 1 session, 9 credits) — 3 curriculums:**
   - Curriculum 11: "Xe Cộ Quanh Em" (Vehicles Around Me) — common vehicles: bus, truck, train, boat, plane
   - Curriculum 12: "Trái Cây Ngon Lành" (Delicious Fruits) — fruits children eat: apple, banana, grape, mango, watermelon
   - Curriculum 13: "Cơ Thể Của Em" (My Body) — body parts: hand, foot, eye, ear, nose

   **Beginner Short (8-10 words, 4 sessions, 19 credits) — 3 curriculums:**
   - Curriculum 14: "Thời Tiết Hôm Nay" (Today's Weather) — weather vocabulary: sunny, rainy, windy, hot, cold, snow, storm, foggy, warm, cool
   - Curriculum 15: "Bữa Ăn Vui Vẻ" (Happy Meals) — food vocabulary: rice, soup, egg, milk, bread, chicken, noodle, cake, cookie, juice
   - Curriculum 16: "Tủ Quần Áo" (My Wardrobe) — clothing vocabulary: shirt, pants, dress, shoes, hat, socks, jacket, skirt, scarf, gloves

   **Preintermediate Short (10-12 words, 4 sessions, 49 credits) — 4 curriculums:**
   - Curriculum 17: "Đếm Và Khám Phá" (Count and Discover) — numbers and math: count, number, add, minus, equal, double, half, pair, dozen, zero, hundred, thousand
   - Curriculum 18: "Hình Dạng Kỳ Thú" (Amazing Shapes) — shapes and spatial concepts: circle, square, triangle, rectangle, star, diamond, oval, cube, sphere, straight, corner, pattern
   - Curriculum 19: "Đại Dương Xanh" (Blue Ocean) — ocean animals and sea life: whale, dolphin, shark, octopus, turtle, crab, jellyfish, seahorse, coral, wave, shell, seaweed
   - Curriculum 20: "Thể Thao Sôi Động" (Active Sports) — sports and exercise: soccer, swim, basketball, tennis, dance, stretch, throw, catch, goal, score, practice, champion

2. THE Curriculum_Creator SHALL select vocabulary words that are concrete, high-frequency, and visually representable for children aged 6-10.
3. THE Curriculum_Creator SHALL ensure no vocabulary word in any Batch 2 curriculum overlaps with any word in Batch1_Vocabulary.
4. THE Curriculum_Creator SHALL ensure no two Batch 2 curriculums have overlapping vocabulary lists with each other.
5. WHEN creating reading passages for children, THE Curriculum_Creator SHALL use simple sentences (under 10 words average for beginner, under 12 words for preintermediate), present tense primarily, and vocabulary that a 6-10 year old Vietnamese child can relate to.

### Requirement 3: Age-Appropriate Content Design

**User Story:** As a content quality owner, I want all learner-facing content designed for children aged 6-10, so that young learners feel engaged, safe, and encouraged throughout the learning experience.

#### Acceptance Criteria

1. WHEN Child_Content is created for introAudio scripts, THE scripts SHALL use a warm, playful, encouraging tone — as if a friendly teacher is speaking to a child. Use simple Vietnamese sentences, enthusiastic language, and gentle encouragement.
2. WHEN Child_Content is created for reading passages, THE passages SHALL feature child-relatable scenarios: riding vehicles, eating fruits, learning about the body, experiencing weather, mealtime, getting dressed, counting objects, discovering shapes, visiting the ocean, playing sports. No abstract concepts, no adult themes.
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
5. WHILE assigning tones within a series, THE Tone_Assigner SHALL ensure no two adjacent curriculums use the same Tone_Palette type (considering the last Batch 1 curriculum in each series as the predecessor).
6. THE Tone_Assigner SHALL ensure no single Tone_Palette type exceeds 30% of the 10 Batch 2 curriculum descriptions.
7. THE Parent_Copy SHALL NOT use fear-based marketing or shame-based language about children's abilities. The tone SHALL be aspirational, warm, and encouraging.

### Requirement 6: introAudio Quality for Children

**User Story:** As a content quality owner, I want introAudio scripts crafted specifically for young learners, so that children feel welcomed, engaged, and celebrated throughout the learning experience.

#### Acceptance Criteria

1. WHEN a welcome introAudio is created for a mini curriculum, THE script (200-350 words) SHALL greet the child warmly, introduce the topic with a fun hook, list all vocabulary words, and teach each word with: the English word, Vietnamese meaning, a simple example sentence a child can understand, and a fun fact or association to help remember.
2. WHEN a welcome introAudio is created for a short/preintermediate curriculum, THE script (300-500 words) SHALL follow the same pattern as criterion 1 but with more words and slightly more context per word.
3. WHEN a session recap introAudio is created (sessions 2+), THE script SHALL briefly and playfully recap previous words before introducing new ones — using phrases like "Các bạn còn nhớ không?" (Do you remember?).
4. WHEN a farewell introAudio is created, THE script (200-400 words) SHALL review key vocabulary words with fresh child-friendly example sentences, celebrate the child's achievement with enthusiastic praise, and encourage practicing with family or friends.
5. THE introAudio scripts SHALL be fully bilingual with simple Vietnamese explanations for every English word and concept.
6. THE Curriculum_Creator SHALL individually craft every introAudio script for its specific curriculum topic, without using template functions or string interpolation.
7. THE Tone_Assigner SHALL assign one of the 5 Farewell_Palette registers to every farewell introAudio, adapted for a child audience.
8. WHILE assigning farewell tones within a series, THE Tone_Assigner SHALL ensure no two adjacent curriculums use the same Farewell_Palette register (considering the last Batch 1 curriculum in each series as the predecessor).

### Requirement 7: Pricing

**User Story:** As a platform owner, I want children's curriculums priced according to the standard pricing guidelines, so that pricing is consistent with the rest of the catalog.

#### Acceptance Criteria

1. WHEN a beginner mini Children_Curriculum (1 session) is created, THE Curriculum_Creator SHALL call `curriculum/setPrice` with `price: 9`.
2. WHEN a beginner short Children_Curriculum (4 sessions) is created, THE Curriculum_Creator SHALL call `curriculum/setPrice` with `price: 19`.
3. WHEN a preintermediate short Children_Curriculum (4 sessions) is created, THE Curriculum_Creator SHALL call `curriculum/setPrice` with `price: 49`.
4. THE Curriculum_Creator SHALL set the price after the curriculum is successfully created and added to its series.

### Requirement 8: Series Integration (Adding to Existing Series)

**User Story:** As a platform owner, I want the 10 new curriculums added to the existing series within the existing collection, so that parents see a growing catalog in a familiar structure.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL add the 6 new beginner curriculums (3 mini + 3 short) to the existing Series 1 "Bước Đầu Tiên" (ID: `8ncwoino`).
2. THE Curriculum_Creator SHALL add the 4 new preintermediate curriculums to the existing Series 2 "Khám Phá Thêm" (ID: `l8l9bexl`).
3. THE Curriculum_Creator SHALL NOT create any new collection or series.
4. THE Curriculum_Creator SHALL set display orders for the new beginner curriculums starting at 7 (continuing after the existing 6 in Series 1): orders 7, 8, 9, 10, 11, 12.
5. THE Curriculum_Creator SHALL set display orders for the new preintermediate curriculums starting at 5 (continuing after the existing 4 in Series 2): orders 5, 6, 7, 8.
6. THE Curriculum_Creator SHALL wire each new curriculum to its series via `curriculum-series/addCurriculum`.
7. THE Curriculum_Creator SHALL ensure all new curriculums share `language: "en"` and `userLanguage: "vi"`.

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

### Requirement 10: Content Validation (Reuse Existing Validator)

**User Story:** As a platform developer, I want every Batch 2 curriculum validated before upload using the same validator from Batch 1, so that no corrupted content enters the database.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL reuse the existing `vi-en-children-curriculum/validate_content.py` without modification.
2. THE Content_Validator SHALL verify that every Children_Curriculum content JSON has non-null, non-empty `title`, `description`, and `preview.text` fields.
3. THE Content_Validator SHALL verify that `learningSessions` is a non-empty array, with each session having a non-empty `title` and `activities` array.
4. THE Content_Validator SHALL verify that every activity has `activityType` (not `type`), `title`, `description`, and `data` fields, with content fields inside `data`.
5. THE Content_Validator SHALL verify that `activityType` values are valid.
6. THE Content_Validator SHALL verify that vocabList fields contain arrays of lowercase strings using the field name `vocabList`.
7. THE Content_Validator SHALL verify that viewFlashcards and speakFlashcards in the same session have identical vocabList arrays.
8. THE Content_Validator SHALL verify writingSentence data structures (vocabList, items with prompt and targetVocab).
9. THE Content_Validator SHALL verify that no Strip_Keys appear anywhere in the content JSON.
10. THE Content_Validator SHALL verify that no `writingParagraph` or `vocabLevel3` activities exist in any Children_Curriculum.
11. IF any validation check fails, THEN THE Content_Validator SHALL abort the upload and print the specific rule violation.

### Requirement 11: No Vocabulary Overlap with Batch 1

**User Story:** As a content quality owner, I want zero vocabulary overlap between Batch 1 and Batch 2, so that children always learn new words and never encounter duplicates across the collection.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL maintain a complete list of Batch1_Vocabulary (all words from the 10 existing curriculums).
2. THE Curriculum_Creator SHALL verify that no word in any Batch 2 curriculum's vocabList appears in the Batch1_Vocabulary list.
3. THE Curriculum_Creator SHALL verify that no two Batch 2 curriculums share any vocabulary word with each other.
4. IF a vocabulary overlap is detected during script development, THEN THE Curriculum_Creator SHALL replace the overlapping word with an appropriate alternative before creation.

### Requirement 12: Script Architecture and Workflow

**User Story:** As a developer, I want a clear, repeatable workflow for creating 10 new children's curriculums that reuses existing infrastructure, so that the process is efficient and traceable.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL produce one standalone Python script per curriculum (10 scripts total).
2. THE Curriculum_Creator SHALL NOT produce an orchestrator script (no new collection/series needed — reuses existing IDs).
3. THE Curriculum_Creator SHALL organize scripts into a directory `vi-en-children-curriculum-batch2/`.
4. THE Curriculum_Creator SHALL authenticate all API calls using `firebase_token.get_firebase_id_token` with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`.
5. THE Curriculum_Creator SHALL use `https://helloapi.step.is` as the API base URL.
6. THE Curriculum_Creator SHALL individually craft every piece of learner-facing text for its specific curriculum topic, without using template functions, string interpolation, or generic fill-in-the-blank patterns.
7. THE Curriculum_Creator MAY use shared helper functions for activity structure (types, order, data schema) but SHALL hand-write all text content per curriculum.
8. IF a curriculum creation API call fails, THEN THE Curriculum_Creator SHALL log the error with the curriculum title and continue with the next curriculum.
9. THE Curriculum_Creator SHALL reuse the root-level `api_helpers.py` for all API calls (create_curriculum, add_to_series, set_display_order, set_price).
10. THE Curriculum_Creator SHALL reuse the existing `vi-en-children-curriculum/validate_content.py` for content validation (importing from the existing path).

### Requirement 13: Newly Created Curriculums Must Be Private

**User Story:** As a platform owner, I want all newly created children's curriculums to be private by default, so that they go through content generation (audio, illustrations) before being exposed to learners.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL NOT call `curriculum/setPublic` with `isPublic: true` on any newly created Children_Curriculum.

### Requirement 14: Curriculum Titles

**User Story:** As a content quality owner, I want curriculum titles to be minimal, child-friendly, and in Vietnamese, so that they work well within the series/collection context.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL keep curriculum titles minimal — never repeating series/collection name, content type prefix, skill-focus label, difficulty level, or audience suffix.
2. THE Curriculum_Creator SHALL write curriculum titles in Vietnamese.
3. THE curriculum titles SHALL NOT include difficulty level indicators (e.g., "beginner", "sơ cấp").
4. THE curriculum titles SHALL be engaging and child-friendly — using playful, imaginative language that appeals to both children and parents.

### Requirement 15: Documentation and Cleanup

**User Story:** As a developer, I want proper documentation after all curriculums are created, so that the content is traceable and reproducible.

#### Acceptance Criteria

1. WHEN all 10 Batch 2 curriculums are created and verified, THE Curriculum_Creator SHALL update the existing `vi-en-children-curriculum/README.md` to include all Batch 2 curriculum IDs, titles, display orders, vocabulary lists, tone assignments, and pricing.
2. WHEN all curriculums are verified in the database, THE Batch 2 source Python scripts SHALL be deleted from `vi-en-children-curriculum-batch2/`, leaving only a README.md in that directory with a pointer to the main README.
3. THE Curriculum_Creator SHALL run a duplicate check query for each curriculum title after creation and resolve any duplicates (keep earliest, delete extras).

### Requirement 16: Execution Order

**User Story:** As a developer, I want a phased execution plan, so that I can create curriculums incrementally and verify each phase.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL execute creation in this order: (1) create beginner mini curriculums (3 scripts), (2) create beginner short curriculums (3 scripts), (3) create preintermediate short curriculums (4 scripts).
2. WHEN each curriculum is created, THE Curriculum_Creator SHALL immediately add it to the appropriate series, set its display order, and set its price.
3. WHEN all 10 curriculums are created, THE Curriculum_Creator SHALL verify the complete set by querying the database to confirm all curriculums exist with correct display orders, language values, prices, and non-empty content.
4. IF verification reveals missing or malformed curriculums, THEN THE Curriculum_Creator SHALL recreate the affected curriculums before finalizing documentation.

### Requirement 17: Tone Adjacency with Batch 1

**User Story:** As a content quality owner, I want tone assignments for Batch 2 to respect adjacency rules relative to the last Batch 1 curriculum in each series, so that the combined catalog reads with natural variety.

#### Acceptance Criteria

1. THE Tone_Assigner SHALL note that the last curriculum in Series 1 (Batch 1) is "Một Ngày Ở Trường" with description tone `bold_declaration` and farewell tone `warm_accountability`. The first Batch 2 curriculum in Series 1 (display order 7) SHALL NOT use `bold_declaration` for its description tone or `warm_accountability` for its farewell tone.
2. THE Tone_Assigner SHALL note that the last curriculum in Series 2 (Batch 1) is "Lễ Hội Và Mùa" with description tone `surprising_fact` and farewell tone `team_building_energy`. The first Batch 2 curriculum in Series 2 (display order 5) SHALL NOT use `surprising_fact` for its description tone or `team_building_energy` for its farewell tone.
3. WHILE assigning tones across the 10 Batch 2 curriculums, THE Tone_Assigner SHALL ensure no single description tone exceeds 30% (max 3 out of 10).
4. WHILE assigning farewell tones across the 10 Batch 2 curriculums, THE Tone_Assigner SHALL distribute them as evenly as possible across the 5 farewell registers (2 each).
