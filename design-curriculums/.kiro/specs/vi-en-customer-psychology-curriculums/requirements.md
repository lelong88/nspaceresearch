# Requirements Document

## Introduction

Create 5 new English-learning curriculums for Vietnamese speakers at the preintermediate-to-intermediate level, focused on **customer psychology for sales and service**. These follow the same 4-session speaking-focus pattern as the salmon-cooking curriculum (ID `yMq70CXQiBV27WEu`) with 15 vocabulary words per curriculum (5 per session 1–3, all 15 in session 4 review).

Language pair: `userLanguage="vi"`, `language="en"`. Target audience: Vietnamese business owners, salespeople, and service professionals who want to learn English vocabulary about psychological principles that help them understand and serve customers better.

### The 5 Curriculum Topics

1. **First Impressions & Anchoring** — How initial perceptions and reference points shape customer decisions
2. **Social Proof & Herd Mentality** — How people follow the crowd when making purchasing decisions
3. **Loss Aversion & Urgency** — Why customers fear losing more than they desire gaining
4. **Emotional Triggers & Storytelling** — How emotions and narratives drive sales conversations
5. **Trust & Reciprocity** — How giving first and building credibility creates loyal customers

### What This Spec Covers

- 5 individually crafted curriculums for vi-en preintermediate/intermediate learners
- 4-session speaking-focus structure (identical to salmon-cooking pattern)
- 15 vocabulary words per curriculum (5 per session 1–3, all 15 in session 4 review)
- First-person narrative reading passages about applying psychology in real business situations
- Vietnamese introAudio scripts teaching English vocab in context of customer psychology
- Series creation to group the 5 curriculums together
- Post-creation verification and cleanup

### What This Spec Does NOT Cover

- Changes to the existing "Chủ Doanh Nghiệp" series (85d6512e)
- Client-side UI changes
- Content generation pipeline (audio, illustrations) — curriculums are created private
- Advanced difficulty levels
- General business English unrelated to customer psychology

## Glossary

- **Anchoring_Curriculum**: The curriculum focused on first impressions and the anchoring effect in sales. Contains 15 vocabulary words related to initial perceptions and reference-point pricing.
- **Social_Proof_Curriculum**: The curriculum focused on social proof and herd mentality in purchasing decisions. Contains 15 vocabulary words related to conformity, testimonials, and crowd behavior.
- **Loss_Aversion_Curriculum**: The curriculum focused on loss aversion and urgency in customer behavior. Contains 15 vocabulary words related to scarcity, fear of missing out, and deadline-driven decisions.
- **Emotional_Triggers_Curriculum**: The curriculum focused on emotional triggers and storytelling in sales. Contains 15 vocabulary words related to narrative persuasion, empathy, and emotional connection.
- **Trust_Curriculum**: The curriculum focused on building trust and the reciprocity principle. Contains 15 vocabulary words related to credibility, generosity, loyalty, and relationship-building.
- **Speaking_Focus_Pattern**: The established 4-session curriculum structure: sessions 1–3 each introduce 5 vocab words via introAudio → viewFlashcards → reading → readAlong → speakReading; session 4 reviews all 15 words with introAudio → viewFlashcards → reading (full passage) → readAlong → speakReading.
- **Customer_Psychology_Series**: The new series container grouping all 5 customer psychology curriculums together.
- **Creation_Script**: A standalone Python script that calls the helloapi REST API to create a single curriculum. All text content is hand-written in the script.
- **Session**: One of 4 ordered segments within each curriculum.
- **Activity**: An individual learning exercise within a session.
- **Strip_Keys**: Auto-generated platform keys that must never appear in new content (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId).
- **API**: The helloapi.step.is REST API used for all CRUD operations.
- **Display_Order**: Integer field controlling sort position of curriculums within a series.
- **Persuasive_Copy**: The required emotional sales copy style for all learner-facing marketing text.
- **Tone_Palette**: The 6 rhetorical opener types: provocative_question, bold_declaration, vivid_scenario, empathetic_observation, surprising_fact, metaphor_led.
- **Farewell_Palette**: The 5 emotional registers for farewell introAudio scripts: introspective_guide, warm_accountability, team_building_energy, quiet_awe, practical_momentum.
- **Language_Pair**: userLanguage="vi", language="en" — Vietnamese speakers learning English.

## Requirements

### Requirement 1: Session Structure — Speaking-Focus Pattern

**User Story:** As a content manager, I want each curriculum to follow the established 4-session speaking-focus pattern, so that the structure is consistent with the salmon-cooking curriculum and learners experience a familiar progression.

#### Acceptance Criteria

1. THE Anchoring_Curriculum SHALL contain exactly 4 sessions.
2. THE Social_Proof_Curriculum SHALL contain exactly 4 sessions.
3. THE Loss_Aversion_Curriculum SHALL contain exactly 4 sessions.
4. THE Emotional_Triggers_Curriculum SHALL contain exactly 4 sessions.
5. THE Trust_Curriculum SHALL contain exactly 4 sessions.
6. EACH curriculum SHALL contain exactly 15 vocabulary words divided into 3 groups of 5 (W1 for Session 1, W2 for Session 2, W3 for Session 3).
7. WHEN Session 1 is created, THE Session SHALL contain activities in this exact order: `introAudio` → `viewFlashcards` (5 words) → `reading` → `readAlong` → `speakReading`.
8. WHEN Session 2 is created, THE Session SHALL contain activities in this exact order: `introAudio` → `viewFlashcards` (5 words) → `reading` → `readAlong` → `speakReading`.
9. WHEN Session 3 is created, THE Session SHALL contain activities in this exact order: `introAudio` → `viewFlashcards` (5 words) → `reading` → `readAlong` → `speakReading`.
10. WHEN Session 4 (review) is created, THE Session SHALL contain activities in this exact order: `introAudio` (recap/farewell) → `viewFlashcards` (all 15 words) → `reading` (full combined passage) → `readAlong` → `speakReading`.

### Requirement 2: Reading Passages — First-Person Business Narratives

**User Story:** As a content manager, I want every reading passage to be a first-person narrative about applying customer psychology in a real business situation, so that learners practice realistic English they can use when discussing sales and service strategies.

#### Acceptance Criteria

1. THE reading passage in each session (1–3) SHALL be a first-person narrative of 2–4 sentences describing the learner applying a customer psychology principle in a real business situation.
2. THE reading passage SHALL use "I" or "My" as the starting perspective — the learner speaks about their own experience applying psychology with customers.
3. THE reading passage in the Anchoring_Curriculum SHALL describe situations involving first impressions, price anchoring, or reference-point effects in sales.
4. THE reading passage in the Social_Proof_Curriculum SHALL describe situations involving testimonials, crowd behavior, or social validation in purchasing decisions.
5. THE reading passage in the Loss_Aversion_Curriculum SHALL describe situations involving scarcity, urgency, or fear of missing out in customer behavior.
6. THE reading passage in the Emotional_Triggers_Curriculum SHALL describe situations involving storytelling, emotional connection, or narrative persuasion in sales.
7. THE reading passage in the Trust_Curriculum SHALL describe situations involving credibility-building, reciprocity, or relationship-building with customers.
8. THE reading passage SHALL incorporate all 5 vocabulary words for that session naturally within the 2–4 sentences.
9. THE Session 4 reading passage SHALL combine the narrative threads from Sessions 1–3 into a cohesive first-person passage of 6–12 sentences that uses all 15 vocabulary words.
10. THE reading passage SHALL NOT be a dialogue (no other person's lines), a long monologue (more than 4 sentences per session 1–3), or a third-person narrative.

### Requirement 3: Vocabulary Selection — Customer Psychology English

**User Story:** As a content manager, I want vocabulary words to be practical English terms for discussing customer psychology, so that Vietnamese business owners and salespeople build immediately useful vocabulary for professional conversations about sales and service.

#### Acceptance Criteria

1. THE Anchoring_Curriculum vocabulary words SHALL be English terms related to first impressions and anchoring effects (e.g., anchor, perception, reference, premium, contrast, bias, initial, frame, benchmark, expectation, impression, positioning, threshold, baseline, cognitive).
2. THE Social_Proof_Curriculum vocabulary words SHALL be English terms related to social proof and herd mentality (e.g., testimonial, endorsement, consensus, conform, influence, popularity, bandwagon, credibility, peer, validation, trend, follower, mainstream, viral, recommendation).
3. THE Loss_Aversion_Curriculum vocabulary words SHALL be English terms related to loss aversion and urgency (e.g., scarcity, deadline, urgency, exclusive, limited, hesitation, regret, countdown, shortage, expire, forfeit, opportunity, irreversible, procrastinate, incentive).
4. THE Emotional_Triggers_Curriculum vocabulary words SHALL be English terms related to emotional triggers and storytelling (e.g., narrative, empathy, compelling, resonate, aspiration, nostalgia, curiosity, vulnerable, authentic, relatable, inspire, evoke, tension, climax, transformation).
5. THE Trust_Curriculum vocabulary words SHALL be English terms related to trust and reciprocity (e.g., credibility, transparency, reciprocity, loyalty, guarantee, integrity, rapport, generosity, commitment, consistency, reputation, goodwill, reliable, trustworthy, accountability).
6. THE vocabulary words SHALL be at the preintermediate-to-intermediate level — words a Vietnamese English learner has likely encountered in reading but needs practice producing in speech about business topics.
7. THE vocabulary words SHALL be lowercase strings in the `vocabList` field — never objects, numbers, or other types.
8. THE 5 curriculums SHALL NOT share any vocabulary words with each other — each curriculum introduces 15 unique words (75 unique words total across the series).

### Requirement 4: Curriculum Topics and Titles

**User Story:** As a content manager, I want clear, minimal Vietnamese titles that communicate the customer psychology topic without redundancy, so that learners can quickly identify what each curriculum teaches.

#### Acceptance Criteria

1. THE Anchoring_Curriculum title SHALL be a short Vietnamese title describing the first impressions/anchoring topic (e.g., "Ấn Tượng Đầu & Hiệu Ứng Neo").
2. THE Social_Proof_Curriculum title SHALL be a short Vietnamese title describing the social proof topic (e.g., "Bằng Chứng Xã Hội & Tâm Lý Bầy Đàn").
3. THE Loss_Aversion_Curriculum title SHALL be a short Vietnamese title describing the loss aversion/urgency topic (e.g., "Sợ Mất & Tâm Lý Khẩn Cấp").
4. THE Emotional_Triggers_Curriculum title SHALL be a short Vietnamese title describing the emotional triggers/storytelling topic (e.g., "Cảm Xúc & Nghệ Thuật Kể Chuyện").
5. THE Trust_Curriculum title SHALL be a short Vietnamese title describing the trust/reciprocity topic (e.g., "Xây Dựng Niềm Tin & Nguyên Tắc Có Qua Có Lại").
6. THE curriculum titles SHALL NOT include difficulty level descriptors, series name repetition, content type prefixes, skill-focus labels, or audience suffixes.
7. THE curriculum titles SHALL be minimal — the series title provides context about customer psychology.

### Requirement 5: Content Quality — Persuasive Copy and Tone Variety

**User Story:** As a content manager, I want all learner-facing marketing text to follow the persuasive copy style with varied tones, so that Vietnamese business owners feel emotionally engaged and motivated to improve their English for sales and service.

#### Acceptance Criteria

1. WHEN the Customer_Psychology_Series is created, THE series description SHALL be a short persuasive hook of 255 characters or fewer, using one of the 6 tones from the Tone_Palette.
2. THE curriculum description SHALL follow the 5-beat Persuasive_Copy structure: bold headline, concrete examples from sales/service situations, vivid metaphor about customer psychology, promise of transformation, and tie to personal growth.
3. THE 5 curriculum descriptions SHALL each use a different tone from the Tone_Palette for their ALL-CAPS headline openers — no two adjacent curriculums (by display order) SHALL use the same tone.
4. THE curriculum preview (~150 words) SHALL open with a vivid hook about the learner's challenge in understanding customer psychology in English, name the 15 vocabulary words, and describe the speaking progression across sessions.
5. THE preview text SHALL be written in Vietnamese (as required for preintermediate vi-en curriculums).
6. THE curriculum description SHALL be written in Vietnamese.

### Requirement 6: introAudio Content — Teaching Vocabulary in Customer Psychology Context

**User Story:** As a content manager, I want introAudio scripts to teach vocabulary in the context of customer psychology for sales and service, so that learners understand how each English word connects to real business situations they face daily.

#### Acceptance Criteria

1. WHEN an introAudio is created for Sessions 1–3, THE script SHALL teach the 5 vocabulary words for that session with: part of speech, definition in Vietnamese, an example sentence showing the word used in a customer psychology/sales context, and pronunciation guidance.
2. WHEN an introAudio is created for Session 4 (review), THE script SHALL recap all 15 vocabulary words, connecting them back to the full topic of customer psychology.
3. THE introAudio scripts SHALL be written in Vietnamese (the learner's native language) with English vocabulary words and example sentences embedded.
4. WHEN the farewell introAudio is created for Session 4, THE script (400–600 words) SHALL review vocabulary with definitions and fresh example sentences about customer psychology, summarize the speaking progression, and provide a warm farewell encouraging the learner to apply the words in real sales/service situations.
5. THE 5 curriculums SHALL use all 5 different Farewell_Palette registers for their farewell introAudio scripts — each curriculum uses a unique farewell tone.
6. THE introAudio scripts SHALL reference realistic Vietnamese business scenarios (shop owners, salespeople, service providers interacting with customers) — not abstract academic psychology.

### Requirement 7: Activity Metadata and Schema Compliance

**User Story:** As a content manager, I want every activity to have proper metadata and follow the content schema, so that the platform renders correctly and no corruption occurs.

#### Acceptance Criteria

1. THE Activity SHALL include both a `title` and `description` field for every activity in every session.
2. WHEN a `viewFlashcards` activity is created, THE Activity title SHALL follow the format "Flashcards: <topic>" and the description SHALL follow the format "Học N từ: word1, word2, ...".
3. WHEN a `reading` or `speakReading` activity is created, THE Activity title SHALL follow the format "Đọc: <topic>" and the description SHALL contain the first ~80 characters of the reading text.
4. WHEN a `readAlong` activity is created, THE Activity title SHALL follow the format "Nghe: <topic>" and the description SHALL be "Nghe đoạn văn vừa đọc và theo dõi."
5. WHEN an `introAudio` activity is created, THE Activity title SHALL be a descriptive label (e.g., "Giới thiệu bài học", "Giới thiệu từ vựng") and the description SHALL be a brief summary.
6. THE Session object SHALL include a `title` field (e.g., "Phần 1", "Phần 2", "Phần 3", "Ôn tập").
7. THE Activity SHALL use `activityType` as the field name — never `type`.
8. THE Activity SHALL place all content fields inside a `data` object — never inline on the activity.
9. THE `viewFlashcards` activity SHALL use `vocabList` as the field name for the word array — never `words`.
10. THE `reading`, `speakReading`, and `readAlong` activities SHALL include a `data.text` field containing the passage text.
11. THE `introAudio` activity SHALL include a `data.text` field containing the script text.

### Requirement 8: Top-Level Curriculum Content Structure

**User Story:** As a content manager, I want the top-level curriculum content JSON to include all required fields, so that the platform can display and process the curriculum correctly.

#### Acceptance Criteria

1. THE curriculum content JSON SHALL include a `title` field (non-empty string, in Vietnamese).
2. THE curriculum content JSON SHALL include a `description` field (non-empty string, multi-paragraph Persuasive_Copy in Vietnamese).
3. THE curriculum content JSON SHALL include a `preview` object with a `text` field (non-empty string, ~150 words in Vietnamese).
4. THE curriculum content JSON SHALL include a `learningSessions` array with exactly 4 session objects.
5. THE curriculum content JSON SHALL include `"contentTypeTags": []` (empty array).
6. THE curriculum content JSON SHALL include `"lengthTags": ["medium"]`.
7. THE curriculum content JSON SHALL include `"skillFocusTags": ["speaking_focus"]`.
8. THE curriculum content JSON SHALL include `"difficultyTags": ["preintermediate", "vocab_intermediate", "reading_preintermediate"]`.

### Requirement 9: Strip-Keys Compliance

**User Story:** As a content manager, I want new curriculum content to never include auto-generated platform keys, so that the platform correctly generates fresh metadata after upload.

#### Acceptance Criteria

1. THE curriculum content SHALL NOT include any of the following auto-generated keys: `mp3Url`, `illustrationSet`, `chapterBookmarks`, `segments`, `whiteboardItems`, `userReadingId`, `lessonUniqueId`, `curriculumTags`, `taskId`, `imageId`.

### Requirement 10: Series Creation and Organization

**User Story:** As a content manager, I want the 5 customer psychology curriculums organized in a new series, so that learners can discover and progress through all topics together in a logical sequence.

#### Acceptance Criteria

1. WHEN the Customer_Psychology_Series is created, THE API SHALL be called via `curriculum-series/create` with a Vietnamese title, a Vietnamese description (under 255 characters using one of the 6 tones), and the series SHALL be kept private until all curriculums are ready.
2. WHEN a curriculum is added to the series via `curriculum-series/addCurriculum`, THE Creation_Script SHALL call `curriculum/setDisplayOrder` to assign a sequential integer display order (Anchoring = 1, Social_Proof = 2, Loss_Aversion = 3, Emotional_Triggers = 4, Trust = 5).
3. THE series SHALL contain curriculums with homogeneous `language: "en"` and `userLanguage: "vi"`.
4. THE series SHALL contain curriculums within a maximum 1-level gap from the highest-level curriculum in the series.
5. THE display order SHALL follow a logical learning progression: foundational concepts (anchoring, social proof) → emotional drivers (loss aversion, emotional triggers) → relationship-building (trust/reciprocity).

### Requirement 11: API Call Compliance

**User Story:** As a content manager, I want all API calls to follow the platform's requirements, so that curriculum creation succeeds without errors.

#### Acceptance Criteria

1. THE Creation_Script SHALL set `language: "en"` and `userLanguage: "vi"` as top-level body parameters in the `curriculum/create` API call (not only inside the content JSON).
2. THE Creation_Script SHALL authenticate using `firebase_token.get_firebase_id_token("zs5AMpVfqkcfDf8CJ9qrXdH58d73")` for all API calls.
3. WHEN a curriculum is created via `curriculum/create`, THE curriculum SHALL have `is_public: false` (the platform default).
4. THE Creation_Script SHALL NOT call `curriculum/setPublic` with `isPublic: true` on any newly created curriculum.

### Requirement 12: Script Organization and Documentation

**User Story:** As a content manager, I want one Python script per curriculum with all text content hand-written, so that each curriculum's content is self-contained and individually crafted.

#### Acceptance Criteria

1. THE Creation_Script architecture SHALL use one Python script per curriculum (5 scripts total) with all text content hand-written in that script.
2. THE Creation_Script architecture SHALL include one orchestrator script that handles series creation, adding curriculums to the series, and setting display orders.
3. THE Creation_Script SHALL NOT use template functions, string interpolation, or loops to generate learner-facing text content.
4. THE Creation_Script MAY use shared helper functions for activity structure (types, order, data schema) but SHALL hand-write all text content per curriculum.
5. WHEN all curriculums in the series are successfully created, THE workspace SHALL contain a `vi-en-customer-psychology-curriculums/` folder with a README.md documenting: series ID and title, curriculum IDs and titles, display orders, vocabulary lists, tone assignments, farewell tone assignments, how content was created, SQL queries to find the curriculums in the DB, and enough context to recreate if needed.
6. WHEN all curriculums are verified in the database, THE source Python scripts SHALL be deleted from the folder, leaving only the README.

### Requirement 13: No Templated Content

**User Story:** As a content manager, I want every piece of learner-facing text to be individually crafted per curriculum topic, so that each curriculum reads as if written by someone who deeply understands that specific customer psychology principle.

#### Acceptance Criteria

1. THE Creation_Script SHALL NOT use `f-string` interpolation, template functions, or shared text skeletons to generate introAudio scripts, descriptions, previews, reading passages, or any learner-facing text.
2. EACH curriculum's reading passages SHALL reflect the specific psychology principle and vocabulary of that curriculum — not generic text with words swapped in.
3. THE Anchoring_Curriculum's introAudio scripts SHALL teach vocabulary with examples of anchoring and first impressions in Vietnamese business contexts (e.g., a shop owner setting a high reference price, a salesperson making a strong first impression).
4. THE Social_Proof_Curriculum's introAudio scripts SHALL teach vocabulary with examples of social proof in Vietnamese business contexts (e.g., showing customer reviews, displaying "best-seller" labels, referencing popular choices).
5. THE Loss_Aversion_Curriculum's introAudio scripts SHALL teach vocabulary with examples of loss aversion in Vietnamese business contexts (e.g., limited-time offers, "only 3 left" messaging, deadline-driven promotions).
6. THE Emotional_Triggers_Curriculum's introAudio scripts SHALL teach vocabulary with examples of emotional storytelling in Vietnamese business contexts (e.g., sharing a customer's transformation story, creating curiosity about a product's origin).
7. THE Trust_Curriculum's introAudio scripts SHALL teach vocabulary with examples of trust-building in Vietnamese business contexts (e.g., offering free samples, providing money-back guarantees, being transparent about pricing).

### Requirement 14: Cross-Curriculum Consistency

**User Story:** As a content manager, I want all 5 curriculums to maintain consistent quality and structure while covering distinct psychology topics, so that the series feels cohesive and progressively builds the learner's customer psychology English.

#### Acceptance Criteria

1. THE series SHALL order curriculums logically: Anchoring (1) → Social Proof (2) → Loss Aversion (3) → Emotional Triggers (4) → Trust (5) — progressing from basic perception effects to emotional drivers to relationship-building.
2. THE 5 curriculums SHALL maintain identical session structure (same activity types and order per the Speaking_Focus_Pattern).
3. THE 5 curriculums SHALL ensure no vocabulary word is repeated between them (75 unique words total).
4. THE 5 curriculums SHALL use the same language pair (`language: "en"`, `userLanguage: "vi"`) and difficulty tags (`["preintermediate", "vocab_intermediate", "reading_preintermediate"]`).
5. THE 5 curriculums SHALL use 5 different description tones from the Tone_Palette — no two adjacent curriculums (by display order) use the same tone.
6. THE 5 curriculums SHALL each use a different farewell tone from the Farewell_Palette (all 5 registers used exactly once across the series).

### Requirement 15: Content Corruption Prevention

**User Story:** As a platform developer, I want every curriculum verified against content corruption rules before upload, so that no malformed content enters the database.

#### Acceptance Criteria

1. THE Creation_Script SHALL verify that the curriculum content JSON has non-null, non-empty `title`, `description`, and `preview.text` fields before upload.
2. THE Creation_Script SHALL verify that `learningSessions` is an array of exactly 4 sessions, each with a non-empty `title` and `activities` array.
3. THE Creation_Script SHALL verify that every activity has `activityType` (not `type`), `title`, `description`, and `data` fields.
4. THE Creation_Script SHALL verify that `activityType` values are valid (introAudio, viewFlashcards, reading, speakReading, readAlong).
5. THE Creation_Script SHALL verify that `vocabList` fields contain arrays of lowercase strings using the field name `vocabList` (never `words`).
6. THE Creation_Script SHALL verify that no Strip_Keys appear anywhere in the content JSON.
7. IF any validation check fails, THEN THE Creation_Script SHALL abort the upload and print the specific rule violation.

### Requirement 16: Duplicate Check After Creation

**User Story:** As a platform developer, I want duplicate detection after creation, so that accidental double-runs don't pollute the database.

#### Acceptance Criteria

1. WHEN a curriculum is created, THE Creation_Script SHALL run a duplicate check query for that curriculum title.
2. IF duplicates are found, THEN THE Creation_Script SHALL keep the earliest record and delete extras.
3. THE Creation_Script SHALL remove duplicate series entries before deleting duplicate curriculums.
