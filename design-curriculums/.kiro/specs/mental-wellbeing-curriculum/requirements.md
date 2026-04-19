# Requirements Document

## Introduction

Create 10 vi-en curriculums on mental well-being, spanning beginner to intermediate levels with balanced_skills focus. The curriculums are organized into 2 themes:

1. **Mental Well-being for General Audience** (5 curriculums) — everyday mental health topics accessible to any Vietnamese learner of English
2. **Mental Well-being for University of Medicine Students** (5 curriculums) — mental health topics tailored to medical students aged ~18-22, using clinical/academic vocabulary appropriate to their field

Each theme becomes a separate series within a single collection. All curriculums follow the established vi-en patterns: Vietnamese titles/descriptions/preview text, bilingual content, `contentTypeTags: []`, `skillFocusTags: ["balanced_skills"]`, and no difficulty level in titles.

### Database Context (queried via MCP postgres)

**Existing related vi-en curriculums:**
- "Cảm xúc và tâm trạng" (beginner, 1 session, balanced_skills) — basic emotions vocabulary in series "Gia đình và các mối quan hệ"
- "Stress Management" (upperintermediate, 5 sessions) — standalone, not in a series
- "Emotional Intelligence" (upperintermediate, 5 sessions) — standalone
- "Cognitive Biases" (advanced, 5 sessions) — standalone
- "Motivation Science" (advanced, 5 sessions) — standalone
- "Mental Health & Neuroplasticity" (advanced, 5 sessions) — in "Sức Khỏe & Lối Sống" series
- "Stress, Cortisol & Resilience" (upperintermediate, 5 sessions) — in "Sức Khỏe & Lối Sống" series
- "Inside Out 2 — Cảm Xúc Bên Trong" (preintermediate, 4 sessions) — movie-based
- "Từ Vựng Cảm Xúc — Tâm Lý Học" (preintermediate, 6 sessions, vocab_acquisition)

**Gap identified:** No beginner-to-intermediate mental well-being curriculums exist. All existing psychology/mental health content is upperintermediate or advanced. This collection fills the beginner-to-intermediate gap.

**Existing structural patterns for vi-en balanced_skills:**
- Beginner 4-session: 12 vocab (6 per learning session), sessions = [Phần 1, Phần 2, Ôn tập, Đọc toàn bài]
- Beginner/Preintermediate 5-session: 18 vocab (6 per learning session), sessions = [Phần 1, Phần 2, Phần 3, Ôn tập, Đọc toàn bài]
- Intermediate 5-session: 18 vocab (6 per learning session), sessions = [Phần 1, Phần 2, Phần 3, Ôn tập, Đọc toàn bài]
- Activity pattern per learning session: introAudio → viewFlashcards → speakFlashcards → vocabLevel1 → vocabLevel2 → reading → speakReading → readAlong → writingSentence
- Review session (Ôn tập): introAudio → viewFlashcards → speakFlashcards → vocabLevel1 → vocabLevel2 → writingSentence
- Final session (Đọc toàn bài): introAudio → reading → speakReading → readAlong → writingParagraph → introAudio (farewell)

**Existing collections/series in the mental health space:**
- Collection "Tâm Lý & Cảm Xúc" (id: xtuzctz9, not public) — contains upperintermediate/advanced content
- Series "Sức Khỏe & Lối Sống" (id: e24f29c4, public) — 8 curriculums, all upperintermediate/advanced
- Series "Tâm Lý & Phát Triển Bản Thân" (id: 6k2ij0ut, public) — 5 curriculums, upperintermediate/advanced

**Pricing reference:**
- Beginner 4-session balanced_skills: 49 credits (standard)
- Preintermediate/Intermediate 5-session: 49 credits (standard)
- Academic/professional content: always 49 credits per PRICING_GUIDELINES.md

## Glossary

- **Curriculum**: A structured learning unit containing sessions with activities (flashcards, reading, speaking, writing)
- **Collection**: Top-level organizational container that groups related series
- **Series**: A group of related curriculums within a collection
- **Session**: A subdivision of a curriculum containing ordered activities
- **Activity**: A single learning exercise (introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, vocabLevel3, reading, speakReading, readAlong, writingSentence, writingParagraph)
- **balanced_skills**: Skill focus tag indicating the curriculum covers reading, speaking, listening, and writing equally
- **vocabList**: Array of lowercase English vocabulary strings attached to flashcard and vocab activities
- **Preview**: Marketing text shown before purchase, written in Vietnamese for vi-en non-advanced curriculums
- **Persuasive_Copy_Style**: The required multi-paragraph emotional sales copy format for descriptions (bold headline, concrete examples, vivid metaphor, transformation promise, learning tie-in)
- **EARS**: Easy Approach to Requirements Syntax — structured requirement patterns
- **Display_Order**: Integer controlling the sort position of a curriculum within a series
- **Content_Corruption**: Structural defects in curriculum JSON (wrong field names, missing data, inline fields)
- **Strip_Keys**: Auto-generated keys (mp3Url, illustrationSet, segments, etc.) that must never be included in new curriculums

## Requirements

### Requirement 1: Collection Structure

**User Story:** As a content manager, I want the 10 mental well-being curriculums organized into a single collection with 2 series, so that learners can browse them by theme.

#### Acceptance Criteria

1. THE System SHALL create one collection titled "Sức Khỏe Tinh Thần (Mental Well-being)" with a neutral informative description summarizing both themes.
2. THE System SHALL create a series titled "Sức Khỏe Tinh Thần — Đời Sống (Everyday Mental Well-being)" for the 5 general-audience curriculums.
3. THE System SHALL create a series titled "Sức Khỏe Tinh Thần — Sinh Viên Y Khoa (Mental Well-being for Medical Students)" for the 5 medical-student curriculums.
4. THE System SHALL add both series to the collection and set display orders (general audience series first at order 0, medical student series at order 1).
5. WHEN a series is created, THE System SHALL set a description of 255 characters or fewer using one of the 6 description tones, with different tones for the two series.
6. THE System SHALL NOT call setPublic with isPublic: true on any newly created curriculum, series, or collection.

### Requirement 2: Curriculum Level Distribution

**User Story:** As a content designer, I want the 10 curriculums to span beginner through intermediate levels, so that learners at different proficiency levels find appropriate content.

#### Acceptance Criteria

1. THE System SHALL create the following level distribution for the general-audience series (5 curriculums):
   - 2 curriculums at beginner level (4 sessions each, 12 vocab words)
   - 1 curriculum at preintermediate level (5 sessions, 18 vocab words)
   - 2 curriculums at intermediate level (5 sessions, 18 vocab words)
2. THE System SHALL create the following level distribution for the medical-student series (5 curriculums):
   - 1 curriculum at beginner level (4 sessions, 12 vocab words)
   - 2 curriculums at preintermediate level (5 sessions, 18 vocab words)
   - 2 curriculums at intermediate level (5 sessions, 18 vocab words)
3. THE System SHALL ensure no more than a 1-level gap between adjacent curriculums within each series (beginner → preintermediate → intermediate).
4. THE System SHALL set display orders within each series to reflect ascending difficulty (lowest difficulty first).

### Requirement 3: General-Audience Curriculum Topics

**User Story:** As a Vietnamese English learner, I want mental well-being curriculums on everyday topics I can relate to, so that I learn useful English vocabulary while exploring personally relevant themes.

#### Acceptance Criteria

1. THE System SHALL create 5 general-audience curriculums covering these topics (titles in Vietnamese, no difficulty level in title):
   - **G1 (beginner):** "Cảm Xúc Hàng Ngày — Hiểu Mình Hơn" — daily emotions and self-awareness (12 vocab: e.g., anxious, calm, overwhelmed, grateful, frustrated, mood, emotion, stress, relax, breathe, balance, mindful)
   - **G2 (beginner):** "Giấc Ngủ Ngon — Bí Quyết Nghỉ Ngơi" — sleep hygiene and rest (12 vocab: e.g., insomnia, fatigue, routine, nap, restful, drowsy, pillow, alarm, habit, refresh, recharge, snore)
   - **G3 (preintermediate):** "Vượt Qua Căng Thẳng — Sống Khỏe Mỗi Ngày" — stress management for daily life (18 vocab: e.g., anxiety, tension, burnout, coping, resilience, therapy, meditation, journal, boundary, self-care, overwhelm, trigger, symptom, recovery, wellness, mindfulness, gratitude, perspective)
   - **G4 (intermediate):** "Mối Quan Hệ Lành Mạnh — Kết Nối Thật Sự" — healthy relationships and emotional boundaries (18 vocab: e.g., empathy, boundary, attachment, vulnerability, assertive, conflict, compromise, trust, intimacy, resentment, codependent, communicate, validate, supportive, toxic, reciprocal, forgive, nurture)
   - **G5 (intermediate):** "Tư Duy Tích Cực — Sức Mạnh Của Suy Nghĩ" — positive thinking and cognitive reframing (18 vocab: e.g., optimism, pessimism, reframe, cognitive, distortion, affirmation, self-talk, catastrophize, ruminate, growth, mindset, setback, persevere, gratitude, resilient, perspective, flourish, thrive)
2. WHEN creating each curriculum, THE System SHALL use vocabulary appropriate to the stated difficulty level (beginner vocab uses common, high-frequency words; intermediate vocab introduces more abstract/nuanced terms).
3. THE System SHALL ensure no vocabulary word is repeated across curriculums within the same series.

### Requirement 4: Medical-Student Curriculum Topics

**User Story:** As a Vietnamese medical student (18-22 years old), I want mental well-being curriculums that connect to my studies and student life, so that I learn English vocabulary relevant to both my personal well-being and my future medical career.

#### Acceptance Criteria

1. THE System SHALL create 5 medical-student curriculums covering these topics (titles in Vietnamese, no difficulty level in title):
   - **M1 (beginner):** "Sức Khỏe Tinh Thần Sinh Viên Y — Những Bước Đầu Tiên" — intro to mental health for med students (12 vocab: e.g., stress, pressure, exam, exhaustion, support, counselor, schedule, priority, overwhelm, cope, balance, wellbeing)
   - **M2 (preintermediate):** "Kiệt Sức Học Đường — Nhận Diện và Vượt Qua" — academic burnout recognition and recovery (18 vocab: e.g., burnout, fatigue, procrastination, perfectionism, deadline, motivation, discipline, self-compassion, isolation, peer, mentor, debrief, workload, symptom, chronic, recovery, boundary, recharge)
   - **M3 (preintermediate):** "Đồng Cảm Không Kiệt Sức — Kỹ Năng Cho Sinh Viên Y" — compassion fatigue and empathy in clinical settings (18 vocab: e.g., compassion, empathy, detachment, clinical, patient, caregiver, emotional, drain, vicarious, trauma, debrief, supervision, self-care, threshold, absorb, professional, distress, regulate)
   - **M4 (intermediate):** "Tâm Lý Lâm Sàng — Ngôn Ngữ Của Sức Khỏe Tinh Thần" — clinical psychology vocabulary for medical contexts (18 vocab: e.g., diagnosis, disorder, therapy, cognitive, behavioral, anxiety, depression, screening, intervention, prognosis, comorbidity, psychosomatic, referral, assessment, symptom, chronic, acute, remission)
   - **M5 (intermediate):** "Giao Tiếp Với Bệnh Nhân — Sức Khỏe Tinh Thần Trong Phòng Khám" — patient communication about mental health (18 vocab: e.g., disclosure, stigma, confidential, consent, rapport, reassure, empathize, diagnose, prescribe, compliance, follow-up, holistic, wellbeing, counseling, psychiatric, resilience, coping, advocate)
2. WHEN creating medical-student curriculums, THE System SHALL use vocabulary that bridges everyday English with clinical/academic terminology appropriate to the stated level.
3. THE System SHALL ensure no vocabulary word is repeated across curriculums within the same series.

### Requirement 5: Curriculum Content Structure

**User Story:** As a content manager, I want each curriculum to follow the established vi-en balanced_skills content structure, so that the learning experience is consistent with existing curriculums.

#### Acceptance Criteria

1. WHEN creating a beginner curriculum (4 sessions, 12 vocab), THE System SHALL structure sessions as:
   - Session 1 "Phần 1": introAudio, viewFlashcards (6 words), speakFlashcards (6 words), vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence
   - Session 2 "Phần 2": introAudio, viewFlashcards (6 words), speakFlashcards (6 words), vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence
   - Session 3 "Ôn tập": introAudio, viewFlashcards (all 12 words), speakFlashcards (all 12 words), vocabLevel1, vocabLevel2, writingSentence
   - Session 4 "Đọc toàn bài": introAudio, reading, speakReading, readAlong, writingParagraph, introAudio (farewell)
2. WHEN creating a preintermediate or intermediate curriculum (5 sessions, 18 vocab), THE System SHALL structure sessions as:
   - Sessions 1-3 "Phần 1/2/3": introAudio, viewFlashcards (6 words), speakFlashcards (6 words), vocabLevel1, vocabLevel2, vocabLevel3, reading, speakReading, readAlong, writingSentence
   - Session 4 "Ôn tập": introAudio, viewFlashcards (all 18 words), speakFlashcards (all 18 words), vocabLevel1, vocabLevel2, vocabLevel3, writingSentence
   - Session 5 "Đọc toàn bài": introAudio, reading, speakReading, readAlong, writingParagraph, introAudio (farewell)
3. THE System SHALL set `contentTypeTags` to `[]` (empty array) on every curriculum.
4. THE System SHALL set `skillFocusTags` to `["balanced_skills"]` on every curriculum.
5. THE System SHALL ensure viewFlashcards and speakFlashcards within the same session have identical vocabList arrays.
6. THE System SHALL ensure all vocabList entries are lowercase strings.

### Requirement 6: Bilingual Content and Vietnamese User-Facing Text

**User Story:** As a Vietnamese learner, I want all user-facing text in Vietnamese and reading passages in English, so that I can navigate the curriculum in my language while learning English content.

#### Acceptance Criteria

1. THE System SHALL write all curriculum titles in Vietnamese (with optional English subtitle after an em dash).
2. THE System SHALL write all curriculum descriptions in Vietnamese following the Persuasive_Copy_Style format.
3. THE System SHALL write all preview.text in Vietnamese.
4. THE System SHALL write all session titles in Vietnamese ("Phần 1", "Phần 2", "Phần 3", "Ôn tập", "Đọc toàn bài").
5. THE System SHALL write all activity titles and descriptions in Vietnamese following CURRICULUM_CREATION_RULES patterns (e.g., "Flashcards: <topic>", "Đọc: <topic>", "Viết: <topic>").
6. THE System SHALL write all introAudio scripts in Vietnamese.
7. THE System SHALL write all reading passages in English at the appropriate difficulty level.
8. THE System SHALL write writingSentence prompts and writingParagraph instructions in Vietnamese with English target vocabulary.

### Requirement 7: Description Tone Variety

**User Story:** As a content manager, I want varied description tones across all curriculums and series, so that the catalog avoids monotony and each curriculum feels individually crafted.

#### Acceptance Criteria

1. THE System SHALL assign one of the 6 description tones (provocative_question, bold_declaration, vivid_scenario, empathetic_observation, surprising_fact, metaphor_led) to each curriculum description.
2. THE System SHALL ensure no two adjacent curriculums within the same series share the same description tone.
3. THE System SHALL ensure no single tone exceeds 30% of the total 10 curriculum descriptions (max 3 uses per tone).
4. THE System SHALL assign different description tones to the two series descriptions.
5. THE System SHALL assign varied farewell introAudio tones (introspective guide, warm accountability, team-building energy, quiet awe, practical momentum) across curriculums, with no two adjacent curriculums in the same series sharing the same farewell tone.

### Requirement 8: Content Quality Standards

**User Story:** As a learner, I want high-quality, individually crafted content that engages me emotionally and teaches effectively, so that I stay motivated throughout the curriculum.

#### Acceptance Criteria

1. THE System SHALL write each curriculum description as multi-paragraph persuasive copy with: ALL-CAPS Vietnamese headline, concrete personal examples, vivid metaphor, transformation promise, and learning-growth tie-in.
2. THE System SHALL write each preview.text as ~150 words of compelling Vietnamese marketing copy that names vocabulary words and describes the learning journey.
3. THE System SHALL write each introAudio script as 500-800 words that teaches each vocabulary word individually with part of speech, definition, example sentence, and contextual explanation.
4. THE System SHALL write each reading passage as original English text at the appropriate difficulty level, incorporating all session vocabulary naturally.
5. THE System SHALL write each writingSentence prompt with specific context and an example sentence showing correct usage.
6. THE System SHALL write each writingParagraph with specific instructions and at least 2 prompts referencing curriculum content.
7. THE System SHALL ensure all content is individually crafted per curriculum — no templated generation, string interpolation, or shared skeleton patterns.

### Requirement 9: Pricing and Metadata

**User Story:** As a content manager, I want correct pricing and metadata on all curriculums, so that they are properly cataloged and priced.

#### Acceptance Criteria

1. THE System SHALL set the price to 49 credits on all 10 curriculums (standard price for balanced_skills curriculums with 4+ sessions).
2. THE System SHALL set `language` to `"en"` and `userLanguage` to `"vi"` on every curriculum create call.
3. THE System SHALL set display orders on all curriculums within their series (ascending by difficulty, starting from 0).
4. THE System SHALL NOT include any strip-keys (mp3Url, illustrationSet, segments, chapterBookmarks, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId) in new curriculum content.

### Requirement 10: Content Integrity Validation

**User Story:** As a content manager, I want all curriculums validated against corruption rules after creation, so that no structural defects exist in the content.

#### Acceptance Criteria

1. WHEN a curriculum is created, THE System SHALL verify the content JSON against all CONTENT_CORRUPTION_RULES: top-level structure (title, description, preview, learningSessions), session structure (title, activities array), activity structure (activityType not type, valid activityType values, title, description, data field).
2. WHEN a curriculum is created, THE System SHALL verify activity-type-specific data rules: introAudio has data.text, reading/speakReading/readAlong has data.text, flashcard/vocab activities have data.vocabList (not data.words), writingSentence has data.vocabList and data.items with prompt and targetVocab, writingParagraph has data.vocabList, data.instructions, and data.prompts (≥2).
3. WHEN a curriculum is created, THE System SHALL verify cross-field consistency: viewFlashcards and speakFlashcards in the same session have identical vocabList.
4. WHEN a curriculum is created, THE System SHALL check for duplicates by querying: `SELECT id, title, created_at FROM curriculum WHERE title = '<title>' AND uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73' ORDER BY created_at`.
5. IF a duplicate is found, THEN THE System SHALL keep the earliest record and delete extras.

### Requirement 11: Script and Documentation Standards

**User Story:** As a developer, I want one Python script per curriculum and a comprehensive README after creation, so that the work is reproducible and maintainable.

#### Acceptance Criteria

1. THE System SHALL create one standalone Python script per curriculum (10 scripts total), each named descriptively (e.g., `create_g1_daily_emotions.py`, `create_m1_med_student_intro.py`).
2. THE System SHALL use the shared `api_helpers.py` module for all API calls (create_curriculum, add_to_series, set_display_order, set_price).
3. THE System SHALL query all IDs (collection, series) from the database at runtime — no hardcoded IDs in scripts.
4. WHEN all curriculums are successfully created and verified, THE System SHALL create a README.md documenting: collection ID, series IDs, all curriculum IDs with titles, vocabulary lists, tone assignments, SQL queries for verification, and recreation instructions.
5. WHEN all curriculums are successfully created and verified, THE System SHALL delete all Python scripts (only README.md remains).

### Requirement 12: Vocabulary Design Principles

**User Story:** As a curriculum designer, I want vocabulary words carefully selected for each level and theme, so that learners build useful mental health literacy progressively.

#### Acceptance Criteria

1. THE System SHALL select beginner vocabulary from high-frequency, concrete words that learners encounter in everyday contexts (e.g., stress, calm, mood, sleep, tired).
2. THE System SHALL select preintermediate vocabulary that introduces more abstract concepts while remaining accessible (e.g., burnout, resilience, coping, mindfulness, boundary).
3. THE System SHALL select intermediate vocabulary that includes nuanced, analytical terms (e.g., cognitive, empathy, vulnerability, comorbidity, psychosomatic).
4. WHEN selecting vocabulary for medical-student curriculums, THE System SHALL include clinical/academic terms appropriate to the level alongside general mental health vocabulary.
5. THE System SHALL ensure zero vocabulary overlap between curriculums within the same series.
6. THE System SHALL ensure vocabulary overlap between the two series is minimized (some overlap is acceptable for foundational terms like "stress" or "anxiety" that appear at different levels in different contexts).
