# Requirements Document

## Introduction

Create 20 English-learning curriculums for Vietnamese speakers (userLanguage="vi", language="en") on the topic of Buddhism, meditation, and mindfulness. Difficulty levels span preintermediate to intermediate, requiring bilingual text throughout.

The 20 curriculums provide variety in pedagogical focus: some are story-reading focused (reading passages about Buddhist stories, meditation narratives), some are speaking focused (heavy on speakFlashcards, speakReading), and some offer balanced skills (mix of all activity types). Topics span Buddha's life, Buddhist philosophy, meditation techniques, mindfulness practices, Buddhist temples, monks' daily life, and related spiritual concepts.

### What This Spec Covers

- 20 individually crafted curriculums for Vietnamese speakers learning English through Buddhist/meditation content
- Variety in skill focus: story-reading, speaking, and balanced-skills curriculums
- Topics spanning Buddhism, meditation, mindfulness, temple life, and spiritual practice
- Collection and series organization
- Pricing per guidelines (49 credits for preintermediate/intermediate full curriculums)
- Creation workflow, validation, and documentation
- contentTypeTags: `["story"]` for story-reading focused curriculums, `[]` for others

### What This Spec Does NOT Cover

- Changes to existing vi-en curriculums
- Curriculums for other language pairs
- Content generation pipeline (audio, illustrations) — curriculums are created private
- Beginner or advanced difficulty levels
- Religious instruction or proselytizing — content is educational/cultural

## Glossary

- **Buddhism_Curriculum**: A curriculum teaching English vocabulary and skills through Buddhist, meditation, or mindfulness content. Designed for Vietnamese adult learners at preintermediate or intermediate level.
- **Curriculum_Creator**: The system of standalone Python scripts that generate curriculum JSON content and upload it via the REST API.
- **Content_Validator**: Validation logic that checks curriculum JSON against the Content Corruption Detection Rules before upload.
- **Collection_Organizer**: The orchestrator script that creates collections, series, wires them together, and sets display orders via the REST API.
- **Tone_Assigner**: The logic that assigns description tones and farewell tones to each curriculum and series, ensuring variety constraints are met.
- **Language_Pair**: userLanguage="vi", language="en" — Vietnamese speakers learning English.
- **Story_Reading_Curriculum**: A curriculum focused on reading practice with `contentTypeTags: ["story"]`. Heavy on reading, speakReading, and readAlong activities. Reading passages are longer narrative texts (Buddhist stories, meditation journeys, temple life narratives). Vocabulary is introduced to support comprehension of the story.
- **Speaking_Curriculum**: A curriculum focused on speaking practice with `contentTypeTags: []`. Heavy on speakFlashcards, speakReading activities. Includes more repetition of spoken output. Reading passages are shorter and serve as speaking prompts.
- **Balanced_Curriculum**: A curriculum with equal emphasis on all skill areas with `contentTypeTags: []`. Includes reading, speaking, listening, and writing activities in balanced proportion.
- **Persuasive_Copy**: The required writing style for marketing text — emotional sales copy with bold headline, concrete examples, vivid metaphor, transformation promise, and personal growth tie-in.
- **Tone_Palette**: The 6 rhetorical opener types: provocative_question, bold_declaration, vivid_scenario, empathetic_observation, surprising_fact, metaphor_led.
- **Farewell_Palette**: The 5 emotional registers for farewell introAudio scripts: introspective_guide, warm_accountability, team_building_energy, quiet_awe, practical_momentum.
- **Strip_Keys**: Auto-generated platform keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId) that must never be included in new curriculum content.
- **Preintermediate_Curriculum**: A 4-session curriculum with 10-14 vocabulary words, priced at 49 credits. Bilingual text required.
- **Intermediate_Curriculum**: A 4-session curriculum with 12-16 vocabulary words, priced at 49 credits. Bilingual text required.

## Requirements

### Requirement 1: Curriculum Count, Levels, and Skill Focus Distribution

**User Story:** As a platform owner, I want 20 English-learning curriculums on Buddhism/meditation/mindfulness with varied skill focuses, so that Vietnamese learners can choose the learning style that suits them best.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL produce exactly 20 Buddhism_Curriculums for the vi-en language pair.
2. THE Curriculum_Creator SHALL create curriculums spanning preintermediate and intermediate levels (approximately 10 preintermediate and 10 intermediate).
3. THE Curriculum_Creator SHALL distribute skill focus across the 20 curriculums as follows: 7 Story_Reading_Curriculums, 6 Speaking_Curriculums, and 7 Balanced_Curriculums.
4. WHEN a Story_Reading_Curriculum is created, THE curriculum SHALL include `contentTypeTags: ["story"]` at the top level of the content JSON.
5. WHEN a Speaking_Curriculum or Balanced_Curriculum is created, THE curriculum SHALL include `contentTypeTags: []` at the top level of the content JSON.
6. THE Buddhism_Curriculum SHALL never include Strip_Keys in the content JSON.
7. THE Curriculum_Creator SHALL set `language: "en"` and `userLanguage: "vi"` as top-level body parameters in the `curriculum/create` API call.

### Requirement 2: Topic Plan for 20 Curriculums

**User Story:** As a platform owner, I want diverse topics spanning Buddhism, meditation, and mindfulness, so that learners explore the full breadth of this subject area while building English skills.

#### Acceptance Criteria

1. THE 20 Buddhism_Curriculums SHALL cover the following topics, each individually crafted:

   **Story-Reading Focus (7 curriculums, contentTypeTags: ["story"]):**
   - Curriculum 1 (preintermediate): "Con Đường Giác Ngộ" — The story of Siddhartha Gautama's journey from prince to Buddha. Vocab: enlightenment, renounce, suffering, meditation, awakening, compassion, path, wisdom, serenity, liberation
   - Curriculum 2 (preintermediate): "Ngôi Chùa Trong Sương" — A narrative about daily life in a Vietnamese Buddhist temple at dawn. Vocab: temple, incense, chant, monk, prayer, bell, offering, devotion, silence, ritual
   - Curriculum 3 (intermediate): "Câu Chuyện Thiền Sư" — Stories of famous Zen masters and their teachings through parables. Vocab: parable, disciple, insight, paradox, detachment, mindful, stillness, impermanence, awareness, transcend, koan, contemplation
   - Curriculum 4 (intermediate): "Hành Trình Chánh Niệm" — A first-person narrative of someone discovering mindfulness practice. Vocab: mindfulness, breath, anchor, present, observe, acceptance, wandering, intention, clarity, equanimity, cultivate, surrender
   - Curriculum 5 (preintermediate): "Những Bài Học Từ Hoa Sen" — Buddhist moral stories using the lotus flower as metaphor. Vocab: lotus, bloom, mud, purity, patience, growth, resilience, beauty, emerge, transform
   - Curriculum 6 (intermediate): "Mùa An Cư" — Narrative about the Buddhist rain retreat season and monks' intensive practice. Vocab: retreat, discipline, solitude, reflection, vow, perseverance, community, harmony, simplicity, gratitude, renewal, dedication
   - Curriculum 7 (intermediate): "Ánh Sáng Từ Bi" — Stories illustrating the Buddhist concept of loving-kindness (metta). Vocab: compassion, empathy, forgiveness, generosity, kindness, selfless, benevolence, reconciliation, altruism, unconditional, embrace, nurture

   **Speaking Focus (6 curriculums, contentTypeTags: []):**
   - Curriculum 8 (preintermediate): "Thiền Cho Người Mới" — Practical meditation vocabulary for beginners. Vocab: breathe, focus, relax, posture, inhale, exhale, calm, gentle, steady, release
   - Curriculum 9 (preintermediate): "Nói Về Chánh Niệm" — Conversational phrases for discussing mindfulness in English. Vocab: awareness, moment, attention, distraction, grounding, sensation, acknowledge, respond, pause, balance
   - Curriculum 10 (intermediate): "Đối Thoại Về Phật Giáo" — Vocabulary for discussing Buddhist concepts in English conversations. Vocab: philosophy, reincarnation, karma, nirvana, dharma, sangha, enlighten, meditate, spiritual, doctrine, scripture, monastery
   - Curriculum 11 (intermediate): "Chia Sẻ Trải Nghiệm Thiền" — Expressing personal meditation experiences in English. Vocab: profound, transformative, peaceful, restless, breakthrough, struggle, consistent, progress, insight, revelation, surrender, blissful
   - Curriculum 12 (preintermediate): "Tại Khóa Tu" — Vocabulary for participating in an English-language meditation retreat. Vocab: schedule, session, instructor, guidance, practice, technique, beginner, intermediate, silent, mindful
   - Curriculum 13 (intermediate): "Phật Giáo Và Đời Sống Hiện Đại" — Discussing how Buddhism applies to modern life in English. Vocab: integrate, contemporary, stress, anxiety, therapeutic, holistic, secular, wellness, resilience, sustainable, intentional, flourish

   **Balanced Skills (7 curriculums, contentTypeTags: []):**
   - Curriculum 14 (preintermediate): "Bát Chánh Đạo" — The Noble Eightfold Path explained through vocabulary and practice. Vocab: righteous, speech, action, livelihood, effort, concentration, understanding, intention, ethical, conduct
   - Curriculum 15 (preintermediate): "Thiền Định Mỗi Ngày" — Daily meditation practice vocabulary and routines. Vocab: routine, habit, morning, evening, duration, timer, cushion, comfortable, consistent, benefit
   - Curriculum 16 (intermediate): "Tứ Diệu Đế" — The Four Noble Truths explored through reading, speaking, and writing. Vocab: truth, suffering, origin, cessation, noble, craving, attachment, liberation, diagnosis, prescription, remedy, realization
   - Curriculum 17 (preintermediate): "Chánh Niệm Trong Ăn Uống" — Mindful eating vocabulary and practices. Vocab: savor, texture, aroma, gratitude, nourish, chew, appreciate, portion, mindful, conscious
   - Curriculum 18 (intermediate): "Thiền Hành" — Walking meditation vocabulary and the art of mindful movement. Vocab: stride, pace, deliberate, sensation, grounding, rhythm, awareness, surroundings, footstep, synchronize, embodiment, presence
   - Curriculum 19 (preintermediate): "Không Gian Thiền" — Vocabulary for creating and describing meditation spaces. Vocab: sanctuary, candle, cushion, altar, tranquil, atmosphere, minimal, natural, sacred, arrange
   - Curriculum 20 (intermediate): "Tâm Từ Và Thiền Tâm Từ" — Loving-kindness meditation (metta) practice and vocabulary. Vocab: radiate, wellbeing, boundless, extend, recipient, phrase, visualize, warmth, genuine, universal, infinite, intention

2. THE Curriculum_Creator SHALL select vocabulary words that are relevant to the Buddhist/meditation/mindfulness domain and appropriate for the target difficulty level.
3. THE Curriculum_Creator SHALL minimize vocabulary overlap across the 20 curriculums — no more than 2 shared words between any two curriculums.
4. WHEN creating reading passages, THE Curriculum_Creator SHALL use sentence complexity appropriate to the level: preintermediate (average 10-14 words per sentence), intermediate (average 12-18 words per sentence).

### Requirement 3: Activity Templates by Skill Focus

**User Story:** As a platform owner, I want distinct activity sequences for each skill focus type, so that story-reading curriculums emphasize reading, speaking curriculums emphasize oral production, and balanced curriculums cover all skills.

#### Acceptance Criteria

1. WHEN a Story_Reading_Curriculum is created, THE 4 sessions SHALL follow this structure:
   - Session 1: introAudio (welcome + teach words group 1), viewFlashcards (group 1), speakFlashcards (group 1), reading (narrative passage 150-200 words using group 1 words), speakReading, readAlong, introAudio (session wrap-up)
   - Session 2: introAudio (recap group 1 + teach words group 2), viewFlashcards (group 2), speakFlashcards (group 2), reading (narrative passage 150-200 words using group 2 words), speakReading, readAlong, introAudio (session wrap-up)
   - Session 3 (Review): introAudio (review intro), viewFlashcards (all words), speakFlashcards (all words), vocabLevel1 (all words), reading (continuation of the story using all words, 200-250 words), speakReading, readAlong, introAudio (review wrap-up)
   - Session 4 (Final): introAudio (final reading intro), reading (story conclusion using all words, 250-300 words), speakReading, readAlong, writingSentence (3-4 items reflecting on the story), introAudio (farewell with vocab review)

2. WHEN a Speaking_Curriculum is created, THE 4 sessions SHALL follow this structure:
   - Session 1: introAudio (welcome + teach words group 1), viewFlashcards (group 1), speakFlashcards (group 1), vocabLevel1 (group 1), speakFlashcards (group 1 — second round), reading (short passage 80-100 words), speakReading, introAudio (session wrap-up)
   - Session 2: introAudio (recap group 1 + teach words group 2), viewFlashcards (group 2), speakFlashcards (group 2), vocabLevel1 (group 2), speakFlashcards (group 2 — second round), reading (short passage 80-100 words), speakReading, introAudio (session wrap-up)
   - Session 3 (Review): introAudio (review intro), speakFlashcards (all words), vocabLevel1 (all words), vocabLevel2 (all words), speakFlashcards (all words — second round), reading (passage 100-120 words), speakReading, introAudio (review wrap-up)
   - Session 4 (Final): introAudio (final session intro), speakFlashcards (all words), vocabLevel2 (all words), reading (passage 120-150 words), speakReading, readAlong, writingSentence (2-3 items), introAudio (farewell with vocab review)

3. WHEN a Balanced_Curriculum is created, THE 4 sessions SHALL follow this structure:
   - Session 1: introAudio (welcome + teach words group 1), viewFlashcards (group 1), speakFlashcards (group 1), vocabLevel1 (group 1), reading (passage 120-150 words), speakReading, readAlong, introAudio (session wrap-up)
   - Session 2: introAudio (recap group 1 + teach words group 2), viewFlashcards (group 2), speakFlashcards (group 2), vocabLevel1 (group 2), reading (passage 120-150 words), speakReading, readAlong, introAudio (session wrap-up)
   - Session 3 (Review): introAudio (review intro), viewFlashcards (all words), speakFlashcards (all words), vocabLevel1 (all words), vocabLevel2 (all words), reading (passage 150-180 words), speakReading, readAlong, writingSentence (4-5 items), introAudio (review wrap-up)
   - Session 4 (Final): introAudio (final reading intro), reading (full passage using all words, 200-250 words), speakReading, readAlong, writingSentence (3-4 items), writingParagraph (1 prompt), introAudio (farewell with vocab review)

4. THE Curriculum_Creator SHALL ensure all 20 curriculums have exactly 4 learning sessions each.

### Requirement 4: Reading Passage Content Standards

**User Story:** As a content quality owner, I want reading passages that are culturally authentic, engaging, and appropriate for the Buddhist/meditation topic, so that learners gain both language skills and meaningful content knowledge.

#### Acceptance Criteria

1. WHEN reading passages are created for Story_Reading_Curriculums, THE passages SHALL be narrative in style — telling stories, describing scenes, or following characters through Buddhist-themed experiences.
2. WHEN reading passages are created for Speaking_Curriculums, THE passages SHALL be conversational or instructional — describing how to do something, explaining a concept simply, or presenting a dialogue scenario.
3. WHEN reading passages are created for Balanced_Curriculums, THE passages SHALL be expository — explaining concepts, describing practices, or presenting information about Buddhist culture and mindfulness.
4. THE reading passages SHALL be written in English with vocabulary and grammar appropriate to the target level (preintermediate or intermediate).
5. THE reading passages SHALL present Buddhism and meditation in a respectful, educational, culturally sensitive manner — never dismissive, never proselytizing.
6. THE reading passages SHALL incorporate Vietnamese Buddhist cultural context where appropriate (Vietnamese temples, Thich Nhat Hanh's teachings, Vu Lan festival, etc.) to create cultural resonance for Vietnamese learners.

### Requirement 5: Marketing Copy and Preview Text

**User Story:** As a content quality owner, I want all marketing text to resonate with Vietnamese adults interested in Buddhism and personal growth, so that learners feel drawn to explore these curriculums.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL write curriculum descriptions as Persuasive_Copy following the 5-beat structure, connecting English learning to spiritual growth, inner peace, and the ability to access Buddhist wisdom in English.
2. THE Curriculum_Creator SHALL write curriculum previews (~150 words) with vivid hooks about the learner's spiritual/mindfulness journey, vocabulary word listing, and what the learner will be able to discuss or read in English after completing the curriculum.
3. THE Curriculum_Creator SHALL write all titles, descriptions, and preview text primarily in Vietnamese (as required for preintermediate/intermediate vi-en curriculums).
4. THE Tone_Assigner SHALL assign one of the 6 Tone_Palette types to every curriculum description headline.
5. WHILE assigning tones within a series, THE Tone_Assigner SHALL ensure no two adjacent curriculums use the same Tone_Palette type.
6. THE Tone_Assigner SHALL ensure no single Tone_Palette type exceeds 30% of the 20 curriculum descriptions (max 6 uses per tone).
7. THE Persuasive_Copy SHALL connect English learning to the learner's spiritual aspirations — the ability to read Buddhist texts in English, discuss meditation with international practitioners, or access mindfulness resources in English.

### Requirement 6: introAudio Quality Standards

**User Story:** As a content quality owner, I want introAudio scripts that are contemplative, warm, and educational, so that learners feel guided through both language learning and spiritual exploration.

#### Acceptance Criteria

1. WHEN a welcome introAudio is created, THE script (500-800 words) SHALL greet the learner warmly, introduce the topic with a reflective hook connecting to the learner's interest in Buddhism/meditation, list all vocabulary words for the session, and teach each word with: the English word, Vietnamese meaning, a contextual example sentence, and an explanation of how the word connects to the Buddhist/meditation theme.
2. WHEN a session recap introAudio is created (sessions 2+), THE script SHALL briefly recap previous session's words with a connecting thread before introducing new vocabulary.
3. WHEN a farewell introAudio is created (400-600 words), THE script SHALL review 5-6 key vocabulary words with definitions and fresh example sentences, connect the words back to the curriculum's Buddhist/meditation theme, and close with a warm, contemplative sign-off.
4. THE introAudio scripts SHALL be bilingual — Vietnamese explanations for English vocabulary and concepts.
5. THE Curriculum_Creator SHALL individually craft every introAudio script for its specific curriculum topic, without using template functions or string interpolation.
6. THE Tone_Assigner SHALL assign one of the 5 Farewell_Palette registers to every farewell introAudio.
7. WHILE assigning farewell tones across the 20 curriculums, THE Tone_Assigner SHALL ensure no two adjacent curriculums within the same series use the same Farewell_Palette register.
8. THE Tone_Assigner SHALL ensure each Farewell_Palette register is used 3-5 times across the 20 curriculums (balanced distribution).

### Requirement 7: Pricing

**User Story:** As a platform owner, I want all Buddhism/meditation curriculums priced according to the standard pricing guidelines, so that pricing is consistent with the rest of the catalog.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL call `curriculum/setPrice` with `price: 49` for every Buddhism_Curriculum (all are preintermediate or intermediate with 4 sessions).
2. THE Curriculum_Creator SHALL set the price after the curriculum is successfully created and added to its series.

### Requirement 8: Collection and Series Organization

**User Story:** As a platform owner, I want the 20 Buddhism/meditation curriculums organized into a logical collection and series structure, so that learners can browse by sub-topic and skill focus.

#### Acceptance Criteria

1. THE Collection_Organizer SHALL create 1 collection with a Vietnamese title related to Buddhism, meditation, and mindfulness learning, with a neutral informative Vietnamese description.
2. THE Collection_Organizer SHALL organize the 20 curriculums into 3 series:
   - Series 1: Story-reading focused (7 curriculums) — Vietnamese title, description ≤255 chars using a Tone_Palette type.
   - Series 2: Speaking focused (6 curriculums) — Vietnamese title, description ≤255 chars using a different Tone_Palette type.
   - Series 3: Balanced skills (7 curriculums) — Vietnamese title, description ≤255 chars using a third Tone_Palette type.
3. THE Collection_Organizer SHALL wire each series to the collection via `curriculum-collection/addSeriesToCollection`.
4. THE Collection_Organizer SHALL set display orders for all 3 series within the collection via `curriculum-series/setDisplayOrder`.
5. THE Collection_Organizer SHALL set display orders for all curriculums within each series via `curriculum/setDisplayOrder`.
6. THE Collection_Organizer SHALL ensure all curriculums within each series share `language: "en"` and `userLanguage: "vi"`.
7. WHILE assigning series description tones, THE Tone_Assigner SHALL ensure all 3 series use different Tone_Palette types.
8. THE Collection_Organizer SHALL order curriculums within each series by difficulty (preintermediate before intermediate) and then by topic progression.

### Requirement 9: Activity Schema Compliance

**User Story:** As a platform developer, I want every activity to comply with the platform's content schema, so that the content pipeline processes these curriculums without errors.

#### Acceptance Criteria

1. Each Activity SHALL include `activityType`, `title`, `description`, and `data` fields.
2. THE `activityType` field SHALL use one of the valid values: introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence, writingParagraph.
3. THE `vocabList` field SHALL be an array of lowercase strings, using the field name `vocabList` (never `words`).
4. WHEN viewFlashcards and speakFlashcards appear in the same session, THE two activities SHALL have identical `vocabList` arrays.
5. All content data SHALL be inside the `data` object, not inline on the activity object.
6. WHEN a writingSentence activity is created, THE activity SHALL have `data.vocabList`, `data.items` (non-empty array), and each item SHALL have `prompt` and `targetVocab` fields.
7. WHEN a writingParagraph activity is created, THE activity SHALL have `data.vocabList` (array of strings), `data.instructions` (non-empty string), and `data.prompts` (array of strings, length ≥ 2).
8. THE Curriculum_Creator SHALL follow the activity title/description conventions: viewFlashcards/speakFlashcards/vocabLevel* use "Flashcards: <topic>"; reading/speakReading use "Đọc: <topic>"; readAlong uses "Nghe: <topic>"; introAudio uses descriptive labels; writingSentence uses "Viết: <topic>"; writingParagraph uses "Viết: <topic>".

### Requirement 10: Content Validation

**User Story:** As a platform developer, I want every Buddhism/meditation curriculum validated before upload, so that no corrupted content enters the database.

#### Acceptance Criteria

1. THE Content_Validator SHALL verify that every Buddhism_Curriculum content JSON has non-null, non-empty `title`, `description`, and `preview.text` fields.
2. THE Content_Validator SHALL verify that `learningSessions` is a non-empty array with exactly 4 sessions, each having a non-empty `title` and `activities` array.
3. THE Content_Validator SHALL verify that every activity has `activityType` (not `type`), `title`, `description`, and `data` fields, with content fields inside `data`.
4. THE Content_Validator SHALL verify that `activityType` values are valid.
5. THE Content_Validator SHALL verify that vocabList fields contain arrays of lowercase strings using the field name `vocabList`.
6. THE Content_Validator SHALL verify that viewFlashcards and speakFlashcards in the same session have identical vocabList arrays.
7. THE Content_Validator SHALL verify writingSentence data structures (vocabList, items with prompt and targetVocab).
8. THE Content_Validator SHALL verify writingParagraph data structures (vocabList, instructions, prompts with length ≥ 2).
9. THE Content_Validator SHALL verify that no Strip_Keys appear anywhere in the content JSON.
10. THE Content_Validator SHALL verify that `contentTypeTags` is `["story"]` for Story_Reading_Curriculums and `[]` for Speaking_Curriculums and Balanced_Curriculums.
11. IF any validation check fails, THEN THE Content_Validator SHALL abort the upload and print the specific rule violation.

### Requirement 11: Script Architecture and Workflow

**User Story:** As a developer, I want a clear, repeatable workflow for creating 20 Buddhism/meditation curriculums, so that the process is manageable and traceable.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL produce one standalone Python script per curriculum (20 scripts total).
2. THE Curriculum_Creator SHALL produce one orchestrator script that creates the collection, series, wires them together, sets display orders, and sets prices.
3. THE Curriculum_Creator SHALL organize scripts into a directory `vi-en-buddhism-meditation/`.
4. THE Curriculum_Creator SHALL authenticate all API calls using `firebase_token.get_firebase_id_token` with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`.
5. THE Curriculum_Creator SHALL use `https://helloapi.step.is` as the API base URL.
6. THE Curriculum_Creator SHALL individually craft every piece of learner-facing text for its specific curriculum topic, without using template functions, string interpolation, or generic fill-in-the-blank patterns.
7. THE Curriculum_Creator MAY use shared helper functions for activity structure (types, order, data schema) but SHALL hand-write all text content per curriculum.
8. IF a curriculum creation API call fails, THEN THE Curriculum_Creator SHALL log the error with the curriculum title and continue with the next curriculum.

### Requirement 12: Newly Created Curriculums Must Be Private

**User Story:** As a platform owner, I want all newly created Buddhism/meditation curriculums to be private by default, so that they go through content generation (audio, illustrations) before being exposed to learners.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL NOT call `curriculum/setPublic` with `isPublic: true` on any newly created Buddhism_Curriculum.

### Requirement 13: Curriculum Titles

**User Story:** As a content quality owner, I want curriculum titles to be minimal, evocative, and in Vietnamese, so that they work well within the series/collection context and attract learners interested in Buddhist content.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL keep curriculum titles minimal — never repeating series/collection name, content type prefix, skill-focus label, difficulty level, or audience suffix.
2. THE Curriculum_Creator SHALL write curriculum titles in Vietnamese.
3. THE curriculum titles SHALL NOT include difficulty level indicators (e.g., "intermediate", "trung cấp").
4. THE curriculum titles SHALL be evocative and contemplative — using language that resonates with Vietnamese Buddhist culture and spiritual aspiration.

### Requirement 14: Documentation and Cleanup

**User Story:** As a developer, I want proper documentation after all curriculums are created, so that the content is traceable and reproducible.

#### Acceptance Criteria

1. WHEN all 20 curriculums are created and verified, THE Curriculum_Creator SHALL create a README.md documenting: collection ID, all series IDs, all curriculum IDs with titles and display orders, vocabulary lists per curriculum, skill focus assignments, tone assignments (description and farewell), pricing, and SQL verification queries.
2. WHEN all curriculums are verified in the database, THE source Python scripts SHALL be deleted, leaving only the README.
3. THE Curriculum_Creator SHALL run a duplicate check query for each curriculum title after creation and resolve any duplicates (keep earliest, delete extras).

### Requirement 15: Execution Order

**User Story:** As a developer, I want a phased execution plan, so that I can create the infrastructure first and then add curriculums incrementally.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL execute creation in this order: (1) create collection and series via orchestrator, (2) create Story_Reading_Curriculums (7 scripts), (3) create Speaking_Curriculums (6 scripts), (4) create Balanced_Curriculums (7 scripts).
2. WHEN each curriculum is created, THE Curriculum_Creator SHALL immediately add it to the appropriate series, set its display order, and set its price.
3. WHEN all 20 curriculums are created, THE Curriculum_Creator SHALL verify the complete set by querying the database to confirm all curriculums exist with correct display orders, language values, prices, and non-empty content.
4. IF verification reveals missing or malformed curriculums, THEN THE Curriculum_Creator SHALL recreate the affected curriculums before finalizing documentation.

### Requirement 16: Writing Activity Standards

**User Story:** As a content quality owner, I want writing activities that connect language practice to Buddhist/meditation reflection, so that learners engage deeply with both the language and the content.

#### Acceptance Criteria

1. WHEN writingSentence items are created, THE prompts SHALL provide detailed context connecting the vocabulary word to a Buddhist/meditation scenario, include a full example sentence, and specify the format: "Dùng từ 'X' để viết một câu về [specific Buddhist/meditation context]. Ví dụ: [full example sentence]."
2. WHEN writingParagraph prompts are created, THE prompts SHALL ask learners to reflect on Buddhist/meditation concepts using the session's vocabulary — connecting personal experience with the spiritual/philosophical content.
3. THE writingParagraph instructions SHALL guide learners to write 3-5 sentences using at least 3-4 vocabulary words from the session.
4. THE writing activities SHALL appear only in Session 3 (review) and Session 4 (final) of each curriculum.
