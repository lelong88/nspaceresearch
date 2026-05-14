# Requirements Document

## Introduction

Create 3 new English-learning curriculums for Vietnamese speakers at the **preintermediate** level, themed around **having fun on the beach**. These follow the same 4-session speaking-focus pattern as the customer-psychology series (series ID `zf2y1xqc`) and the salmon-cooking curriculum (ID `yMq70CXQiBV27WEu`), with 15 vocabulary words per curriculum (5 per session 1–3, all 15 in session 4 review). Each curriculum provides approximately 2–3 hours of content.

Language pair: `userLanguage="vi"`, `language="en"`. Target audience: Vietnamese English learners who want to talk about beach trips, holidays by the sea, and seaside fun in everyday English.

### The 3 Curriculum Topics

The "having fun on the beach" theme is broken into three distinct sub-topics that progress across a typical beach day:

1. **Beach Activities & Sports** — playful, active fun on the sand and in the water (swimming, surfing, beach volleyball, sandcastles, frisbee, snorkeling)
2. **Beach Food & Relaxation** — picnicking, snacks, sunbathing, lounging, and slow afternoons under an umbrella
3. **Sunset & Evening Beach Fun** — bonfires, sunsets, stargazing, music, and shared evening moments by the shore

### What This Spec Covers

- 3 individually crafted curriculums for vi-en preintermediate learners
- 4-session speaking-focus structure (identical to customer-psychology pattern)
- 15 vocabulary words per curriculum (5 per session 1–3, all 15 in session 4 review) — sized for ~2–3 hours of content
- First-person narrative reading passages about real beach fun moments
- Vietnamese introAudio scripts teaching English vocabulary in beach-day contexts
- Series creation to group the 3 curriculums together
- Post-creation verification and cleanup

### What This Spec Does NOT Cover

- Beach safety, lifeguarding, or marine biology curriculums (these are about *fun*, not safety or science)
- Travel-booking or hotel English (focus is on the beach experience itself)
- Client-side UI changes
- Content generation pipeline (audio, illustrations) — curriculums are created private
- Advanced or upper-intermediate difficulty levels
- Adding the new series to any existing collection (handled separately if needed)

## Glossary

- **Beach_Activities_Curriculum**: The curriculum focused on active beach fun — swimming, surfing, beach sports, sandcastles, snorkeling. Contains 15 vocabulary words related to playful and physical beach activities.
- **Beach_Food_Curriculum**: The curriculum focused on beach food, sunbathing, and relaxation — picnics, snacks, lounging under umbrellas, dozing in hammocks. Contains 15 vocabulary words related to seaside food and slow-paced beach relaxation.
- **Beach_Evening_Curriculum**: The curriculum focused on sunset and evening beach fun — bonfires, sunsets, stargazing, shared music and stories by the shore. Contains 15 vocabulary words related to evening beach gatherings.
- **Speaking_Focus_Pattern**: The established 4-session curriculum structure: sessions 1–3 each introduce 5 vocab words via introAudio → viewFlashcards → reading → readAlong → speakReading; session 4 reviews all 15 words with introAudio → viewFlashcards → reading (full passage) → readAlong → speakReading.
- **Beach_Fun_Series**: The new series container grouping all 3 beach-fun curriculums together. Series title is in Vietnamese.
- **Creation_Script**: A standalone Python script that calls the helloapi REST API to create a single curriculum. All learner-facing text content is hand-written in the script.
- **Session**: One of 4 ordered segments within each curriculum.
- **Activity**: An individual learning exercise within a session.
- **Strip_Keys**: Auto-generated platform keys that must never appear in new content (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId).
- **API**: The helloapi.step.is REST API used for all CRUD operations.
- **Display_Order**: Integer field controlling sort position of curriculums within a series.
- **Persuasive_Copy**: The required emotional sales copy style for all learner-facing marketing text, defined in `CURRICULUM_QUALITY_STANDARDS.md`.
- **Tone_Palette**: The 6 rhetorical opener types: provocative_question, bold_declaration, vivid_scenario, empathetic_observation, surprising_fact, metaphor_led.
- **Farewell_Palette**: The 5 emotional registers for farewell introAudio scripts: introspective_guide, warm_accountability, team_building_energy, quiet_awe, practical_momentum.
- **Language_Pair**: userLanguage="vi", language="en" — Vietnamese speakers learning English.
- **UID**: The authenticated user ID used for all API calls — `zs5AMpVfqkcfDf8CJ9qrXdH58d73`.

## Requirements

### Requirement 1: Session Structure — Speaking-Focus Pattern

**User Story:** As a content manager, I want each curriculum to follow the established 4-session speaking-focus pattern, so that the structure is consistent with the customer-psychology and salmon-cooking curriculums and learners experience a familiar progression.

#### Acceptance Criteria

1. THE Beach_Activities_Curriculum SHALL contain exactly 4 sessions, numbered 1 through 4 in sequential order with no gaps or duplicates.
2. THE Beach_Food_Curriculum SHALL contain exactly 4 sessions, numbered 1 through 4 in sequential order with no gaps or duplicates.
3. THE Beach_Evening_Curriculum SHALL contain exactly 4 sessions, numbered 1 through 4 in sequential order with no gaps or duplicates.
4. EACH curriculum SHALL contain exactly 15 vocabulary words divided into 3 non-overlapping groups of exactly 5 words each (W1 assigned to Session 1, W2 assigned to Session 2, W3 assigned to Session 3), where the union of W1, W2, and W3 equals the full 15-word set with no duplicates across groups.
5. WHEN Session 1 is created, THE Session SHALL contain exactly 5 activities in this exact order with no additional, missing, or reordered activities: `introAudio` → `viewFlashcards` (containing exactly the 5 words of W1) → `reading` → `readAlong` → `speakReading`.
6. WHEN Session 2 is created, THE Session SHALL contain exactly 5 activities in this exact order with no additional, missing, or reordered activities: `introAudio` → `viewFlashcards` (containing exactly the 5 words of W2) → `reading` → `readAlong` → `speakReading`.
7. WHEN Session 3 is created, THE Session SHALL contain exactly 5 activities in this exact order with no additional, missing, or reordered activities: `introAudio` → `viewFlashcards` (containing exactly the 5 words of W3) → `reading` → `readAlong` → `speakReading`.
8. WHEN Session 4 (review) is created, THE Session SHALL contain exactly 5 activities in this exact order with no additional, missing, or reordered activities: `introAudio` (recap/farewell) → `viewFlashcards` (containing exactly all 15 words from W1 ∪ W2 ∪ W3) → `reading` (a single combined passage that incorporates all 15 words) → `readAlong` → `speakReading`.
9. IF any curriculum's session count, activity sequence, activity type, or vocabulary group assignment deviates from criteria 1-8, THEN THE Creation_Script SHALL reject the curriculum with an error indicating which criterion was violated and which session or vocabulary group is non-compliant, and SHALL NOT persist the curriculum.

### Requirement 2: Reading Passages — First-Person Beach Day Narratives

**User Story:** As a content manager, I want every reading passage to be a first-person narrative about a real beach-fun moment, so that learners practice realistic English they can use when describing their own beach trips and holidays.

#### Acceptance Criteria

1. THE reading passage in each session 1–3 SHALL contain between 2 and 4 sentences inclusive, where each sentence has between 6 and 20 words inclusive.
2. THE reading passage SHALL begin with the token `I ` or `My ` (case-sensitive, including the trailing space) and SHALL use only the first-person pronoun set {I, me, my, mine, myself} with no second- or third-person narrators throughout.
3. THE reading passage in the Beach_Activities_Curriculum SHALL describe situations involving active beach play (swimming, surfing, beach sports, sandcastles, snorkeling, paddling, frisbee) and SHALL NOT contain references to picnics, sunbathing, lounging, hammocks, bonfires, sunsets, stargazing, lanterns, or evening gatherings.
4. THE reading passage in the Beach_Food_Curriculum SHALL describe situations involving beach picnics, snacks, sunbathing, lounging, dozing under an umbrella, or other slow-paced beachside relaxation, and SHALL NOT contain references to surfing, snorkeling, beach sports, bonfires, sunsets, stargazing, or evening gatherings.
5. THE reading passage in the Beach_Evening_Curriculum SHALL describe situations involving sunset, bonfires, stargazing, evening music, lanterns, or shared evening moments by the shore, and SHALL NOT contain references to surfing, snorkeling, beach sports, picnic baskets, sunscreen, or sunbathing.
6. THE reading passage SHALL incorporate every one of the 5 vocabulary words for that session at least once via case-insensitive whole-word match, with standard English inflections (`-s`, `-es`, `-ed`, `-ing`) accepted as valid matches.
7. THE Session 4 reading passage SHALL contain between 6 and 12 sentences inclusive (each 6–20 words), SHALL begin with `I ` or `My `, SHALL use only the first-person pronoun set, SHALL combine the narrative threads of Sessions 1–3, and SHALL incorporate every one of the 15 vocabulary words at least once via case-insensitive whole-word match (with `-s`, `-es`, `-ed`, `-ing` inflections accepted).
8. THE reading passage SHALL contain zero quoted dialogue lines (no characters `"` or `'` used to delimit speech, no other-person utterances) and SHALL NOT exceed the per-session sentence cap defined in criterion 1 or 7.
9. THE reading passages SHALL NOT reference drowning, jellyfish stings, sunburn injuries, rip currents, lost children, medical emergencies, severe weather, or any other distressing or unsafe beach scenario.

### Requirement 3: Vocabulary Selection — Beach Fun English

**User Story:** As a content manager, I want vocabulary words to be practical preintermediate English terms about beach fun, so that Vietnamese learners build immediately useful vocabulary for talking about holidays by the sea.

#### Acceptance Criteria

1. THE Beach_Activities_Curriculum vocabList SHALL contain exactly 15 unique English words selected from the active beach fun pool: surf, swim, snorkel, paddle, dive, sandcastle, frisbee, volleyball, kite, splash, wave, board, fin, goggles, float.
2. THE Beach_Food_Curriculum vocabList SHALL contain exactly 15 unique English words selected from the beach food, sunbathing, and relaxation pool: picnic, grill, coconut, smoothie, sunscreen, towel, umbrella, lounge, tan, doze, breeze, basket, snack, sandals, hammock.
3. THE Beach_Evening_Curriculum vocabList SHALL contain exactly 15 unique English words selected from the sunset and evening beach fun pool: bonfire, sunset, marshmallow, lantern, guitar, stargaze, tide, shore, gather, glow, blanket, laughter, firelight, drift, twilight.
4. THE vocabulary words SHALL be at the preintermediate CEFR level (A2-B1), defined as concrete, single-word, beach-themed English nouns or verbs of 1 to 12 characters that a Vietnamese English learner has likely encountered in receptive contexts but needs practice producing in speech.
5. EACH vocabulary entry in the `vocabList` field SHALL be a lowercase ASCII string containing only letters a-z (no spaces, digits, punctuation, uppercase letters, objects, numbers, or other types).
6. THE three curriculums (Beach_Activities_Curriculum, Beach_Food_Curriculum, Beach_Evening_Curriculum) SHALL collectively contain exactly 45 unique vocabulary words with zero overlap between any two curriculums' vocabLists.
7. WHEN the design phase completes, THE final vocabulary lists for all three curriculums SHALL be documented verbatim in design.md as locked lists before any Creation_Script is written.
8. IF any Creation_Script is written or executed before the locked vocabulary lists appear in design.md, THEN THE design process SHALL halt and report a missing-prerequisite error indicating that vocabulary lock is required before script creation.

### Requirement 4: Curriculum Topics and Titles

**User Story:** As a content manager, I want clear, minimal Vietnamese titles that communicate each beach sub-topic without redundancy, so that learners can quickly identify what each curriculum teaches.

#### Acceptance Criteria

1. THE Beach_Activities_Curriculum title SHALL be a Vietnamese title between 3 and 8 words inclusive describing the active-beach-fun topic, written in Vietnamese with diacritics, using Title Case for content words (e.g., "Vui Chơi & Thể Thao Bãi Biển").
2. THE Beach_Food_Curriculum title SHALL be a Vietnamese title between 3 and 8 words inclusive describing the beach-food-and-relaxation topic, written in Vietnamese with diacritics, using Title Case for content words (e.g., "Ăn Uống & Thư Giãn Bên Biển").
3. THE Beach_Evening_Curriculum title SHALL be a Vietnamese title between 3 and 8 words inclusive describing the sunset/evening-beach-fun topic, written in Vietnamese with diacritics, using Title Case for content words (e.g., "Hoàng Hôn & Lửa Trại Bên Biển").
4. THE curriculum titles SHALL NOT include difficulty level descriptors (e.g., "Beginner", "Intermediate", "Sơ Cấp", "Trung Cấp"), the parent series name or its translation, content type prefixes (e.g., "Curriculum:", "Lesson:", "Bài Học:"), skill-focus labels (e.g., "Vocabulary", "Speaking", "Từ Vựng"), or audience suffixes (e.g., "for Kids", "cho Trẻ Em").
5. IF a curriculum title contains any token listed in criterion 4, THEN THE Creation_Script SHALL reject the title and return an error indicating which disallowed token category was matched, and the title SHALL NOT be saved.
6. THE curriculum titles SHALL each be unique across the three beach sub-topic curriculums when compared case-insensitively after trimming surrounding whitespace.
7. THE curriculum titles SHALL NOT repeat the exact wording of the parent series title, and SHALL each contain at least one Vietnamese content word distinct from the other two beach sub-topic titles.

### Requirement 5: Content Quality — Persuasive Copy and Tone Variety

**User Story:** As a content manager, I want all learner-facing marketing text to follow the persuasive copy style with varied tones, so that Vietnamese learners feel emotionally engaged and motivated to learn beach-fun English.

#### Acceptance Criteria

1. WHEN the Beach_Fun_Series is created, THE series description SHALL be a Vietnamese persuasive hook between 40 and 255 characters inclusive, using exactly one of the 6 Tone_Palette tones: `provocative_question`, `bold_declaration`, `vivid_scenario`, `empathetic_observation`, `surprising_fact`, or `metaphor_led`.
2. THE curriculum description SHALL be in Vietnamese, SHALL contain at least 3 paragraphs separated by blank lines, and SHALL open with an ALL-CAPS Vietnamese headline of 3 to 12 words on its own line, where the headline reflects exactly one tone from the Tone_Palette.
3. THE 3 curriculum descriptions SHALL each use a different Tone_Palette tone for their ALL-CAPS headline openers, where no two adjacent curriculums (by display order) use the same tone and no single tone is used by more than 1 of the 3 curriculums.
4. THE curriculum preview (`preview.text`) SHALL be a Vietnamese passage between 120 and 250 words inclusive, SHALL open in its first sentence with a vivid hook about a beach moment naming at least one beach setting element (sand, wave, sunset, picnic, etc.), SHALL name all 15 vocabulary words for that curriculum verbatim, and SHALL describe the speaking progression across all 4 sessions in display order (Session 1 → Session 2 → Session 3 → Session 4).
5. IF a curriculum preview is missing the opening hook, fewer than all 15 vocabulary words, or fewer than all 4 sessions referenced in display order, THEN THE Creation_Script SHALL reject the preview and indicate the missing element; the curriculum SHALL NOT be persisted.
6. THE curriculum description SHALL be written in Vietnamese (with embedded English vocabulary words and example sentences allowed verbatim).
7. THE Beach_Fun_Series description SHALL use a Tone_Palette tone different from the headline tone of the curriculum at display order 1.

### Requirement 6: introAudio Content — Teaching Vocabulary in Beach Fun Context

**User Story:** As a content manager, I want introAudio scripts to teach vocabulary in real beach-fun contexts, so that learners understand how each English word connects to the moments they actually want to talk about.

#### Acceptance Criteria

1. WHEN an introAudio is created for Sessions 1–3, THE script SHALL teach each of the 5 vocabulary words for that session with: (a) part of speech labeled in Vietnamese, (b) a Vietnamese definition between 8 and 40 words inclusive, (c) exactly one English example sentence between 6 and 20 words inclusive showing the word used in a beach-fun context, and (d) pronunciation guidance written either as Vietnamese phonetic respelling or as IPA.
2. WHEN an introAudio is created for Session 4 (review), THE script SHALL recap between 5 and 6 of the 15 vocabulary words inclusive with Vietnamese definitions (8–40 words each) and fresh English example sentences (6–20 words each) that are not character-for-character identical to any Sessions 1–3 example, plus a 1–3 sentence Vietnamese closing connecting the recap back to the curriculum's theme.
3. THE introAudio scripts SHALL be written in Vietnamese for all explanatory prose, with English vocabulary words and English example sentences embedded inline as English (not transliterated, not translated).
4. WHEN the farewell introAudio is created for Session 4, THE script SHALL contain all four of: (a) a recap of 5–6 vocabulary words with Vietnamese definitions and fresh English examples, (b) a Vietnamese summary of the 4-session speaking progression, (c) a warm Vietnamese farewell encouraging the learner to use the words on a real beach trip, and (d) at least one named Vietnamese beach context. The target word count is 400–600 words; IF the word count falls outside 400–600 but all four elements are present, THEN the script SHALL be accepted.
5. THE 3 curriculums SHALL each use a different farewell register from the Farewell_Palette (`introspective_guide`, `warm_accountability`, `team_building_energy`, `quiet_awe`, `practical_momentum`); exactly 3 of the 5 registers SHALL be selected, each used exactly once across the series.
6. THE introAudio scripts SHALL collectively reference at least one realistic Vietnamese beach context per curriculum (Đà Nẵng, Nha Trang, Phú Quốc, Vũng Tàu, family trips, friend gatherings) across its 4 sessions, and any single script SHALL contain at most 3 such references.
7. IF any introAudio script references drownings, accidents, severe weather emergencies, jellyfish stings, sunburn injuries, rip currents, lost children, or other distressing scenarios, THEN THE Creation_Script SHALL reject the script and indicate the offending scenario; the curriculum SHALL NOT be persisted.

### Requirement 7: Activity Metadata and Schema Compliance

**User Story:** As a content manager, I want every activity to have proper metadata and follow the content schema, so that the platform renders correctly and no corruption occurs.

#### Acceptance Criteria

1. THE Activity SHALL include a non-empty `title` field (string, 1 to 200 characters) and a non-empty `description` field (string, 1 to 500 characters) for every activity in every session, with no null, missing, or whitespace-only values.
2. WHEN a `viewFlashcards` activity is created, THE Activity title SHALL match the exact format `"Flashcards: <topic>"` where `<topic>` is a non-empty string of 1 to 180 characters, AND the description SHALL match the exact format `"Học N từ: word1, word2, ..."` where `N` is the integer count of words in `data.vocabList` and the comma-separated word list contains every word in `data.vocabList` in the same order.
3. WHEN a `reading` or `speakReading` activity is created, THE Activity title SHALL match the exact format `"Đọc: <topic>"` where `<topic>` is a non-empty string of 1 to 180 characters, AND the description SHALL contain the first 80 characters of `data.text` (or the entire text if shorter than 80 characters), with a tolerance of plus or minus 5 characters to allow word-boundary trimming.
4. WHEN a `readAlong` activity is created, THE Activity title SHALL match the exact format `"Nghe: <topic>"` where `<topic>` is a non-empty string of 1 to 180 characters, AND the description SHALL be exactly the string `"Nghe đoạn văn vừa đọc và theo dõi."`.
5. WHEN an `introAudio` activity is created, THE Activity title SHALL be a non-empty descriptive label (string, 1 to 100 characters, drawn from the set including but not limited to "Giới thiệu bài học", "Giới thiệu từ vựng", "Lời tạm biệt"), AND the description SHALL be a non-empty summary string of 10 to 300 characters.
6. THE Session object SHALL include a non-empty `title` field (string, 1 to 100 characters) such as "Phần 1", "Phần 2", "Phần 3", or "Ôn tập".
7. THE Activity SHALL use `activityType` as the field name for the activity type identifier, AND IF the field `type` appears at the activity object root, THEN THE Creation_Script SHALL treat the activity as schema-non-compliant and reject it with an error indicating the disallowed field name.
8. THE Activity SHALL place all content fields inside a `data` object, AND IF any content field appears inline at the activity object root instead of inside `data`, THEN THE Creation_Script SHALL treat the activity as schema-non-compliant and reject it with an error indicating the misplaced field.
9. THE `viewFlashcards` activity SHALL use `vocabList` as the field name for the word array inside `data`, AND IF the field `words` appears inside `data` for a `viewFlashcards` activity, THEN THE Creation_Script SHALL treat the activity as schema-non-compliant and reject it with an error indicating the disallowed field name.
10. THE `reading`, `speakReading`, and `readAlong` activities SHALL include a `data.text` field containing a non-empty passage string of 1 to 10000 characters.
11. THE `introAudio` activity SHALL include a `data.text` field containing a non-empty script string of 1 to 5000 characters.
12. IF any activity in any session is missing a required field defined in criteria 1 through 11, or contains a disallowed field name, or places a content field outside `data`, THEN THE Creation_Script SHALL reject the curriculum with a validation error identifying the offending session index, activity index, and the specific schema violation.

### Requirement 8: Top-Level Curriculum Content Structure

**User Story:** As a content manager, I want the top-level curriculum content JSON to include all required fields, so that the platform can display and process the curriculum correctly.

#### Acceptance Criteria

1. THE curriculum content JSON SHALL include a non-empty `title` field (Vietnamese string, 1 to 255 characters, no leading/trailing whitespace).
2. THE curriculum content JSON SHALL include a non-empty `description` field of at least 200 characters in Vietnamese, containing at least 2 paragraphs separated by blank lines, opening with an ALL-CAPS Vietnamese headline as defined in Requirement 5 criterion 2.
3. THE curriculum content JSON SHALL include a `preview` object with a non-empty `text` field in Vietnamese between 120 and 250 words inclusive (matching Requirement 5 criterion 4).
4. THE curriculum content JSON SHALL include a `learningSessions` array containing exactly 4 session objects.
5. THE curriculum content JSON SHALL include a `contentTypeTags` field whose value is exactly the empty array `[]`.
6. THE curriculum content JSON SHALL include a `lengthTags` field whose value is exactly the array `["medium"]`.
7. THE curriculum content JSON SHALL include a `skillFocusTags` field whose value is exactly the array `["speaking_focus"]`.
8. THE curriculum content JSON SHALL include a `difficultyTags` field whose value is exactly the array `["preintermediate", "vocab_preintermediate", "reading_preintermediate"]` in that exact order with that exact casing.
9. IF any field defined in criteria 1–8 is missing, null, of the wrong type, or fails its bound or value check, THEN THE Creation_Script SHALL abort the upload and emit an error indicating the offending field name and the specific bound or value that was violated.

### Requirement 9: Strip-Keys Compliance

**User Story:** As a content manager, I want new curriculum content to never include auto-generated platform keys, so that the platform correctly generates fresh metadata after upload.

#### Acceptance Criteria

1. THE curriculum content SHALL NOT include any of the following auto-generated keys at any nesting depth in the JSON tree (including keys on objects nested inside arrays): `mp3Url`, `illustrationSet`, `chapterBookmarks`, `segments`, `whiteboardItems`, `userReadingId`, `lessonUniqueId`, `curriculumTags`, `taskId`, `imageId`.
2. WHEN the Creation_Script has assembled the content JSON and before it issues the `curriculum/create` API call, THE Creation_Script SHALL traverse every object and array in the content JSON to full tree depth and check each property name against the Strip_Keys list defined in `strip-keys.json`.
3. IF one or more Strip_Keys are detected during the recursive check, THEN THE Creation_Script SHALL remove every occurrence of those keys (along with their associated values) from the content JSON in-place, leaving all other fields and values unchanged, and SHALL proceed with the `curriculum/create` call using the cleaned JSON.
4. WHEN the Creation_Script completes the Strip_Keys removal step, THE Creation_Script SHALL re-verify that zero Strip_Keys remain in the content JSON before invoking `curriculum/create`.
5. IF any Strip_Key still remains in the content JSON after the removal step, THEN THE Creation_Script SHALL abort the `curriculum/create` call and emit an error identifying which keys were not successfully stripped, without modifying any data on the server.

### Requirement 10: Series Creation and Organization

**User Story:** As a content manager, I want the 3 beach-fun curriculums organized in a new series, so that learners can discover and progress through all sub-topics together in a logical sequence.

#### Acceptance Criteria

1. WHEN the Beach_Fun_Series is created, THE Creation_Script SHALL invoke `curriculum-series/create` with a Vietnamese title between 1 and 100 characters inclusive, and a Vietnamese description between 40 and 255 characters inclusive using exactly one of the 6 Tone_Palette tones: `provocative_question`, `bold_declaration`, `vivid_scenario`, `empathetic_observation`, `surprising_fact`, or `metaphor_led`.
2. IF the `curriculum-series/create` call returns a non-2xx status or no series id, THEN THE Creation_Script SHALL halt the run and emit an error identifying the endpoint and response.
3. WHEN a curriculum is added to the series via `curriculum-series/addCurriculum`, THE Creation_Script SHALL immediately invoke `curriculum/setDisplayOrder` to assign the integer display order: Beach_Activities_Curriculum=1, Beach_Food_Curriculum=2, Beach_Evening_Curriculum=3, completing both the add call and the setDisplayOrder call for one curriculum before proceeding to the next.
4. IF either the `curriculum-series/addCurriculum` or `curriculum/setDisplayOrder` call returns a non-2xx status, THEN THE Creation_Script SHALL halt the run and emit an error identifying the endpoint, the curriculum id, and the response.
5. THE series SHALL contain exactly 3 curriculums, all with `language: "en"` and `userLanguage: "vi"`, verified by the `curriculum_series_language_list` view returning a single homogeneous row for the series.
6. THE series SHALL contain curriculums with at most a 1-level difficulty gap, verified by the `curriculum_series_level_gap` view (all 3 are preintermediate, so the gap is 0).
7. THE display order SHALL follow a logical day-progression: active beach fun (morning/midday) at order 1, beach food and relaxation (afternoon) at order 2, sunset and evening beach fun (evening) at order 3.
8. WHILE not every member curriculum has been added and ordered, THE series SHALL remain at `isPublic: false` (the Creation_Script SHALL NOT call `curriculum-series/setIsPublic` with `isPublic: true` within this spec).

### Requirement 11: API Call Compliance

**User Story:** As a content manager, I want all API calls to follow the platform's requirements, so that curriculum creation succeeds without errors.

#### Acceptance Criteria

1. WHEN the Creation_Script invokes the `curriculum/create` API, THE Creation_Script SHALL include `language: "en"` and `userLanguage: "vi"` as top-level body parameters alongside the `content` parameter, regardless of any pre-existing values inside the content JSON, and SHALL set these top-level values on every `curriculum/create` call.
2. WHEN the Creation_Script prepares any API call to `helloapi.step.is`, THE Creation_Script SHALL obtain a Firebase ID token by invoking `firebase_token.get_firebase_id_token("zs5AMpVfqkcfDf8CJ9qrXdH58d73")` and SHALL include the returned token as `firebaseIdToken` in the JSON request body.
3. IF `firebase_token.get_firebase_id_token("zs5AMpVfqkcfDf8CJ9qrXdH58d73")` raises an exception or returns an empty/null value, THEN THE Creation_Script SHALL abort the run before issuing any API call and emit an error identifying the authentication failure and the UID used.
4. WHEN a curriculum is created via `curriculum/create`, THE Creation_Script SHALL omit any `isPublic` parameter so the curriculum remains at the platform default `is_public: false`.
5. THE Creation_Script SHALL NOT call `curriculum/setPublic` with `isPublic: true` on any curriculum created within the scope of this spec.
6. WHEN the Creation_Script invokes any SuperAuthGuard endpoint (`curriculum-series/create`, `curriculum-series/addCurriculum`, or `curriculum/setDisplayOrder`), THE Creation_Script SHALL authenticate using the UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`.
7. IF any API call returns a non-2xx HTTP status, THEN THE Creation_Script SHALL halt subsequent dependent API calls and emit an error identifying the endpoint, the HTTP status, and the response body returned by the server.

### Requirement 12: Script Organization and Documentation

**User Story:** As a content manager, I want one Python script per curriculum with all text content hand-written, so that each curriculum's content is self-contained and individually crafted.

#### Acceptance Criteria

1. THE Creation_Script architecture SHALL produce exactly 3 per-curriculum Python scripts, one per curriculum (Beach_Activities, Beach_Food, Beach_Evening), each containing the hand-written learner-facing text for that curriculum: `title`, `description`, `preview.text`, all 4 session `introAudio` scripts, all 4 reading passages, and all activity titles/descriptions.
2. THE Creation_Script architecture SHALL include exactly one orchestrator script that performs in this ordered sequence: (a) call `curriculum-series/create`, (b) invoke each per-curriculum creation script to call `curriculum/create`, (c) call `curriculum-series/addCurriculum` for each curriculum, (d) call `curriculum/setDisplayOrder` with integer values 1, 2, 3 for Beach_Activities, Beach_Food, Beach_Evening respectively.
3. THE per-curriculum and orchestrator scripts SHALL NOT use Python f-strings (`f"..."`), `str.format()`, `%`-formatting, `string.Template`, or for/while loops to generate any of the following learner-facing text fields: `title`, `description`, `preview.text`, `introAudio.data.text`, reading/speakReading/readAlong `data.text`, activity `title`, activity `description`.
4. THE Creation_Script MAY define shared helper functions for non-text structure only — assembling activity dicts from already-written text, ordering activities, attaching `data` objects, validating schema — and SHALL NOT route any learner-facing text through a shared template, builder, or substitution helper.
5. WHEN all 3 curriculums are verified in the database (defined as a SQL query on `curriculum_series_items` joined with `curriculum` returning all 3 curriculum ids with non-null `content->>'title'` and `is_public = false`, with `uid` not ending in `_deleted`), THE workspace SHALL contain a `vi-en-beach-fun-curriculums/` folder with a `README.md` containing all of the following non-empty sections: (a) Series ID and Vietnamese title, (b) Curriculum IDs and Vietnamese titles, (c) Display orders, (d) Vocabulary lists per curriculum, (e) Description tone assignments, (f) Farewell tone assignments, (g) Creation method summary, (h) SQL queries to find the curriculums in the DB, (i) Recreation context.
6. THE Creation_Script MAY create or update the `vi-en-beach-fun-curriculums/README.md` at any point during the run; IF the folder does not yet exist, THEN the script SHALL create it before writing the README.
7. WHEN the database verification in criterion 5 returns all 3 curriculum ids with non-null titles, THEN the source per-curriculum and orchestrator Python scripts SHALL be deleted, leaving only the README.
8. IF the database verification in criterion 5 fails to return all 3 curriculums, THEN deletion of source scripts is forbidden and the scripts SHALL remain on disk.

### Requirement 13: No Templated Content

**User Story:** As a content manager, I want every piece of learner-facing text to be individually crafted per beach sub-topic, so that each curriculum reads as if written by someone who has actually had that kind of beach day.

#### Acceptance Criteria

1. THE Creation_Script SHALL NOT use f-string interpolation, `.format()` calls, `string.Template`, shared text skeletons, or any other text-templating mechanism to generate introAudio scripts, descriptions, previews, reading passages, or any other learner-facing text fields.
2. WHEN the Creation_Script generates learner-facing text for a curriculum, THE Creation_Script SHALL write each text field as a literal string unique to that curriculum, with no substring of 8 or more consecutive words shared with the corresponding field of any other curriculum in the requirement set.
3. EACH curriculum's reading passages SHALL be written using the specific sub-topic vocabulary and scenarios of that curriculum, such that every reading passage references at least 3 sub-topic-specific concrete nouns or actions from that curriculum's vocabulary list and contains no generic beach filler text reused across curriculums.
4. THE Beach_Activities_Curriculum's introAudio scripts SHALL teach vocabulary using examples drawn exclusively from active beach fun scenarios (e.g., catching a wave on a board, building a sandcastle, playing volleyball with friends), with each script containing at least 2 such active-scenario examples and no examples drawn from food, picnic, evening, or sunset scenarios.
5. THE Beach_Food_Curriculum's introAudio scripts SHALL teach vocabulary using examples drawn exclusively from slow beach food and rest scenarios (e.g., unpacking a picnic basket, sipping a coconut smoothie, dozing under an umbrella, lounging in a hammock), with each script containing at least 2 such slow-scenario examples and no examples drawn from active sport, evening, or bonfire scenarios.
6. THE Beach_Evening_Curriculum's introAudio scripts SHALL teach vocabulary using examples drawn exclusively from evening beach scenarios (e.g., gathering around a bonfire, watching the sunset paint the sky, stargazing on a blanket, listening to laughter and a guitar by firelight), with each script containing at least 2 such evening-scenario examples and no examples drawn from active daytime sport or food picnic scenarios.
7. IF the Creation_Script detects that any generated learner-facing text field shares an 8-or-more consecutive word substring with the same field in another curriculum, or contains scenario examples from a sub-topic other than its assigned sub-topic, THEN THE Creation_Script SHALL halt before any API upload, emit an error indicating the offending curriculum, field, and conflicting text, and preserve all previously generated content unchanged.

### Requirement 14: Cross-Curriculum Consistency

**User Story:** As a content manager, I want all 3 curriculums to maintain consistent quality and structure while covering distinct sub-topics, so that the series feels cohesive and progressively builds the learner's beach-fun English across a typical beach day.

#### Acceptance Criteria

1. THE series SHALL assign integer `displayOrder` values exclusively as Beach_Activities=1, Beach_Food=2, Beach_Evening=3, ordering curriculums logically across a beach day (morning/midday active fun → afternoon food and relaxation → sunset and evening fun).
2. THE 3 curriculums SHALL maintain identical session structure such that for every session index 1–4 and every activity index within that session, the `activityType` value is identical across all 3 curriculums (matching the Speaking_Focus_Pattern exactly).
3. THE 3 curriculums SHALL collectively contain exactly 45 distinct vocabulary entries, where vocabulary uniqueness is determined by case-insensitive exact-match comparison after trimming whitespace; each curriculum SHALL contribute exactly 15 entries with zero overlap to any other curriculum.
4. THE 3 curriculums SHALL each set `language: "en"`, `userLanguage: "vi"`, and `difficultyTags: ["preintermediate", "vocab_preintermediate", "reading_preintermediate"]` (in that exact order with that exact casing).
5. THE 3 curriculums SHALL select 3 different Tone_Palette tones for their description ALL-CAPS headlines, where no two adjacent curriculums (by displayOrder) use the same tone and each selected tone is used by at most 1 of the 3 curriculums.
6. THE 3 curriculums SHALL select exactly 3 of the 5 Farewell_Palette registers, each register used exactly once across the series.
7. THE design phase SHALL document, in `design.md` before any Creation_Script is written, all 9 entries: the 3 description tone assignments, the 3 farewell tone assignments, and the 3 Vietnamese curriculum titles.
8. IF any of criteria 1–7 is violated when validation runs, THEN THE Creation_Script SHALL abort with an error identifying the violated criterion, the offending curriculum or field, and SHALL preserve any previously generated content on disk.

### Requirement 15: Content Corruption Prevention

**User Story:** As a platform developer, I want every curriculum verified against `content-corruption.md` rules before and after upload, so that no malformed content enters the database.

#### Acceptance Criteria

1. WHEN the Creation_Script begins pre-upload validation of a curriculum content JSON, THE Creation_Script SHALL verify that `title`, `description`, and `preview.text` are present, are strings, are non-null, and contain at least 1 non-whitespace character.
2. WHEN the Creation_Script begins pre-upload validation, THE Creation_Script SHALL verify that `learningSessions` is an array containing exactly 4 elements, where each element has a `title` string of at least 1 non-whitespace character and an `activities` array containing at least 1 element.
3. WHEN the Creation_Script validates each activity within `learningSessions[*].activities`, THE Creation_Script SHALL verify that the activity object contains the keys `activityType`, `title`, `description`, and `data`, that none of these values are null, and that the key `type` is not present.
4. WHEN the Creation_Script validates each activity, THE Creation_Script SHALL verify that the value of `activityType` is exactly one of the strings `introAudio`, `viewFlashcards`, `reading`, `speakReading`, or `readAlong` (case-sensitive).
5. WHEN the Creation_Script validates any field named `vocabList` at any nesting depth, THE Creation_Script SHALL verify that the value is an array in which every element is a string equal to its own `lower()` form, and SHALL verify that no field named `words` is used as a substitute for `vocabList` anywhere in the content JSON.
6. WHEN the Creation_Script begins pre-upload validation, THE Creation_Script SHALL traverse every nested object and array and verify that none of the keys listed in `strip-keys.json` (the Strip_Keys set) appear at any depth.
7. WHEN the Creation_Script begins pre-upload validation, THE Creation_Script SHALL verify that the top-level field `contentTypeTags` is present and that its value is exactly one of `["movie"]`, `["music"]`, `["podcast"]`, `["story"]`, or `[]`.
8. IF any pre-upload validation check defined in criteria 1 through 7 fails for a curriculum, THEN THE Creation_Script SHALL skip the `curriculum/create` API call for that curriculum, print a single message to standard error identifying the curriculum, the failing criterion number, and the offending field path, and exit the process with status code 1 within 5 seconds of the failure being detected.
9. IF the Creation_Script cannot write the violation message to standard error, THEN THE Creation_Script SHALL still exit with status code 1 and SHALL NOT proceed with any further uploads in the same run.
10. WHEN all 3 curriculums have been successfully uploaded via `curriculum/create`, THE Creation_Script SHALL re-run the same checks defined in criteria 1 through 7 against the content JSON returned by `curriculum/getOne` for each created curriculum, print a per-curriculum pass/fail line to standard output, and only delete the source creation scripts if every post-upload check passes.
11. IF any post-upload check in criterion 10 fails for any of the 3 curriculums, THEN THE Creation_Script SHALL leave all source creation scripts on disk, print a message identifying each failing curriculum and criterion to standard error, and exit with status code 1.

### Requirement 16: Duplicate Check After Creation

**User Story:** As a platform developer, I want duplicate detection after creation, so that accidental double-runs don't pollute the database.

#### Acceptance Criteria

1. WHEN a curriculum is created, THE Creation_Script SHALL run a duplicate-check query searching for rows in the `curriculum` table where `uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'`, `uid` does NOT end with `_deleted`, and `content->>'title'` exactly equals the curriculum's title (case-sensitive, after trimming surrounding whitespace).
2. THE duplicate-check query SHALL complete within 30 seconds; IF the query times out or returns a database error, THEN THE Creation_Script SHALL abort the run and emit an error identifying the query and the failure.
3. IF the duplicate-check query returns more than one row, THEN THE Creation_Script SHALL keep the row with the earliest `created_at` timestamp (tie-broken by the smallest `id` lexicographically) and SHALL delete every other row via `curriculum/delete`.
4. WHERE duplicate curriculums are members of the Beach_Fun_Series, THE Creation_Script SHALL invoke `curriculum-series/removeCurriculum` to remove each duplicate from the series before invoking `curriculum/delete` on that duplicate.
5. IF a `curriculum-series/removeCurriculum` call fails, THEN THE Creation_Script SHALL log the failure (endpoint, curriculum id, response) and proceed with the `curriculum/delete` call on that duplicate anyway.
6. IF a `curriculum/delete` call fails, THEN THE Creation_Script SHALL log the failure (endpoint, curriculum id, response) and continue processing remaining duplicates without aborting the run.
7. BEFORE invoking `curriculum-series/create`, THE Creation_Script SHALL run a duplicate-check query for the series title (same case-sensitive, trimmed, non-`_deleted` rules); IF a matching series exists, THEN THE Creation_Script SHALL skip the `curriculum-series/create` call and reuse the existing series id for the remaining steps.
