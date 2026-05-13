# Requirements Document

## Introduction

Create 10 English-learning curriculums for Vietnamese speakers (userLanguage="vi", language="en") on the topic of the Digital Economy (Kinh Tế Số). Difficulty levels span preintermediate to intermediate, requiring bilingual text throughout.

Each curriculum focuses on a specific Digital Economy subtopic — e-commerce, digital payments, the gig economy, startup founders, cryptocurrency, social media marketing, remote work, AI in business, cybersecurity, and Vietnam's cashless transition. The 10 curriculums provide variety in pedagogical focus: some are story-reading focused (founder stories, narrative accounts of Vietnam's digital transformation), some are speaking focused (heavy on speakFlashcards, speakReading for everyday digital-economy conversations), and some offer balanced skills (mix of all activity types for core conceptual topics).

Each curriculum is approximately 3 hours of learner time, with 4 learning sessions of about 45 minutes each. Each session introduces 5 new vocabulary words, for a total of 20 unique words per curriculum.

### What This Spec Covers

- 10 individually crafted curriculums for Vietnamese speakers learning English through Digital Economy content
- Variety in skill focus: story-reading (3), speaking (3), and balanced-skills (4) curriculums
- 10 distinct Digital Economy subtopics, each with its own vocabulary, reading material, and angle
- Level span: 5 preintermediate + 5 intermediate (max 1-level gap within each series)
- 4 sessions per curriculum, 5 vocabulary words per session, 20 unique vocab words total per curriculum
- Approximately 3 hours of learner time per curriculum
- Collection and series organization (1 collection, 3 series by skill focus)
- Pricing per workspace guidelines (49 credits for preintermediate/intermediate full curriculums)
- Description tone variety (6-tone palette, ≤30% per tone, no adjacent duplicates)
- Farewell register variety (5-register palette across all 10 curriculums)
- Creation workflow, validation, documentation, and cleanup
- contentTypeTags: `["story"]` for story-reading focused curriculums, `[]` for others

### What This Spec Does NOT Cover

- Changes to the existing `digital-economy-onboarding-curriculum` (the standalone onboarding/demo lesson)
- Changes to other existing vi-en curriculums
- Curriculums for other language pairs
- Content generation pipeline (audio, illustrations) — curriculums are created private
- Beginner or advanced difficulty levels
- Investment advice, crypto trading guidance, or any non-educational financial content — content is educational/contextual only

## Glossary

- **Digital_Economy_Curriculum**: A curriculum teaching English vocabulary and skills through a specific Digital Economy subtopic. Designed for Vietnamese adult learners at preintermediate or intermediate level.
- **Curriculum_Creator**: The system of standalone Python scripts that generate curriculum JSON content and upload it via the REST API.
- **Content_Validator**: Validation logic that checks curriculum JSON against the Content Corruption Detection Rules before upload.
- **Collection_Organizer**: The orchestrator script that creates collections, series, wires them together, and sets display orders via the REST API.
- **Tone_Assigner**: The logic that assigns description tones and farewell tones to each curriculum and series, ensuring variety constraints are met.
- **Language_Pair**: userLanguage="vi", language="en" — Vietnamese speakers learning English.
- **Story_Reading_Curriculum**: A curriculum focused on reading practice with `contentTypeTags: ["story"]`. Heavy on reading, speakReading, and readAlong activities. Reading passages are longer narrative texts (founder journeys, cashless-transition narratives, Vietnamese tech ecosystem stories). Vocabulary supports comprehension of the story.
- **Speaking_Curriculum**: A curriculum focused on speaking practice with `contentTypeTags: []`. Heavy on speakFlashcards, speakReading activities. Includes more repetition of spoken output. Reading passages are shorter and serve as speaking prompts.
- **Balanced_Curriculum**: A curriculum with equal emphasis on all skill areas with `contentTypeTags: []`. Includes reading, speaking, listening, and writing activities in balanced proportion.
- **Persuasive_Copy**: The required writing style for curriculum descriptions — emotional sales copy with bold ALL-CAPS headline opener, concrete examples, vivid metaphor, transformation promise, and personal/career growth tie-in.
- **Tone_Palette**: The 6 rhetorical opener types: provocative_question, bold_declaration, vivid_scenario, empathetic_observation, surprising_fact, metaphor_led.
- **Farewell_Palette**: The 5 emotional registers for farewell introAudio scripts: introspective_guide, warm_accountability, team_building_energy, quiet_awe, practical_momentum.
- **Strip_Keys**: Auto-generated platform keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId) that must never be included in new curriculum content.
- **Preintermediate_Curriculum**: A 4-session curriculum with 20 vocabulary words (5 per session), priced at 49 credits. Bilingual text required.
- **Intermediate_Curriculum**: A 4-session curriculum with 20 vocabulary words (5 per session), priced at 49 credits. Bilingual text required.
- **Session_Vocab_Group**: The 5 vocabulary words introduced in a single session. Each curriculum has 4 Session_Vocab_Groups for a total of 20 unique words.
- **Digital_Economy**: The topic domain covering e-commerce, fintech and digital payments, the gig and platform economy, startups and venture funding, cryptocurrency and blockchain, digital marketing and social media, remote and hybrid work, cloud and SaaS, AI and automation in business, cybersecurity and data privacy.

## Requirements

### Requirement 1: Curriculum Count, Levels, and Skill Focus Distribution

**User Story:** As a platform owner, I want 10 English-learning curriculums on Digital Economy subtopics with varied skill focuses, so that Vietnamese learners can choose the learning style that fits their goals — reading about Vietnamese tech founders, practicing everyday digital-economy conversations, or building balanced English skills around modern business concepts.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL produce exactly 10 Digital_Economy_Curriculums for the vi-en Language_Pair (userLanguage="vi", language="en").
2. THE Curriculum_Creator SHALL create exactly 5 Preintermediate_Curriculums and 5 Intermediate_Curriculums across the 10 Digital_Economy_Curriculums.
3. THE Curriculum_Creator SHALL distribute skill focus across the 10 curriculums as exactly 3 Story_Reading_Curriculums, 3 Speaking_Curriculums, and 4 Balanced_Curriculums (totaling 10).
4. THE Curriculum_Creator SHALL distribute difficulty levels across skill focuses as exactly: 1 Preintermediate_Curriculum and 2 Intermediate_Curriculums among the Story_Reading_Curriculums; 3 Preintermediate_Curriculums and 0 Intermediate_Curriculums among the Speaking_Curriculums; 1 Preintermediate_Curriculum and 3 Intermediate_Curriculums among the Balanced_Curriculums.
5. WHEN a Story_Reading_Curriculum is created, THE Curriculum_Creator SHALL include the field `contentTypeTags` with the exact value `["story"]` at the top level of the content JSON.
6. WHEN a Speaking_Curriculum or Balanced_Curriculum is created, THE Curriculum_Creator SHALL include the field `contentTypeTags` with the exact value `[]` (empty array) at the top level of the content JSON.
7. THE Digital_Economy_Curriculum SHALL never include any Strip_Keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId) at any nesting depth in the content JSON.
8. WHEN calling the `curriculum/create` API, THE Curriculum_Creator SHALL set `language: "en"` and `userLanguage: "vi"` as top-level body parameters alongside the `content` parameter.
9. WHEN a Digital_Economy_Curriculum is created via the `curriculum/create` API, THE Curriculum_Creator SHALL leave the curriculum private and SHALL NOT call `curriculum/setPublic` with `isPublic: true` on the newly created curriculum.

### Requirement 2: Topic Plan for 10 Curriculums

**User Story:** As a platform owner, I want each curriculum to cover a distinct Digital Economy subtopic with vocabulary, reading material, and angle tailored to that subtopic, so that learners can pick the digital-economy area most relevant to their work or interest without encountering repeated content.

#### Acceptance Criteria

1. THE 10 Digital_Economy_Curriculums SHALL cover the following subtopics, each individually crafted:

   **Story-Reading Focus (3 curriculums, contentTypeTags: ["story"]):**
   - **Curriculum 1 — Preintermediate:** "Hành Trình Của Shopee" — A narrative account of how e-commerce platforms transformed Vietnamese shopping habits, told through the daily life of a small shop owner in Hanoi who moves her business online. Subtopic: e-commerce. Vocab (20 words across 4 sessions, examples): platform, shopper, browse, listing, cart, checkout, deliver, package, review, rating, seller, customer, discount, voucher, shipping, return, refund, inventory, profit, growth.
   - **Curriculum 2 — Intermediate:** "Câu Chuyện Khởi Nghiệp Việt" — Story-driven curriculum about Vietnamese tech founders and their journey building unicorns and notable startups (VNG, Tiki, MoMo, VinFast). Subtopic: startups and the founder journey. Vocab (examples): founder, venture, capital, funding, pivot, scale, valuation, milestone, ambition, perseverance, mentor, ecosystem, innovation, breakthrough, expansion, investor, equity, prototype, market, traction.
   - **Curriculum 3 — Intermediate:** "Từ Tiền Mặt Đến Ví Số" — Narrative chronicling Vietnam's transition from a cash-dominant economy to digital wallets, through the eyes of a street vendor adopting MoMo and VNPay. Subtopic: cashless transition and fintech adoption. Vocab (examples): cashless, wallet, transfer, scan, balance, transaction, fintech, adoption, generation, convenience, trust, regulation, banking, deposit, withdrawal, peer-to-peer, instant, secure, ledger, settlement.

   **Speaking Focus (3 curriculums, contentTypeTags: []):**
   - **Curriculum 4 — Preintermediate:** "Mua Sắm Trực Tuyến" — Conversational vocabulary for talking about online shopping experiences in English (Shopee, Lazada, Tiki). Subtopic: e-commerce conversation. Vocab (examples): order, item, deliver, package, return, refund, review, rating, discount, voucher, coupon, shipping, address, payment, confirm, cancel, track, arrive, damaged, satisfied.
   - **Curriculum 5 — Preintermediate:** "Thanh Toán Không Tiền Mặt" — Speaking practice for digital payment scenarios (MoMo, VNPay, ZaloPay, QR codes). Subtopic: digital payments conversation. Vocab (examples): scan, wallet, transfer, balance, top-up, recharge, fee, receipt, confirm, link, account, code, amount, charge, send, receive, instant, history, statement, secure.
   - **Curriculum 6 — Preintermediate:** "Làm Việc Từ Xa" — Conversational English for remote work, video meetings, and digital collaboration. Subtopic: remote work conversation. Vocab (examples): remote, online, meeting, video, microphone, mute, share, screen, schedule, deadline, project, task, team, manager, colleague, message, reply, available, focus, break.

   **Balanced Skills (4 curriculums, contentTypeTags: []):**
   - **Curriculum 7 — Preintermediate:** "Mạng Xã Hội Và Tiếp Thị Số" — Digital marketing and social media basics in the Vietnamese context (TikTok, Facebook, Instagram, YouTube). Subtopic: social media and digital marketing. Vocab (examples): post, share, like, follow, comment, viral, content, audience, brand, advertise, campaign, influencer, engagement, reach, target, click, banner, promote, channel, trend.
   - **Curriculum 8 — Intermediate:** "Tiền Mã Hoá Và Blockchain" — Foundational concepts in cryptocurrency and blockchain technology, presented as educational context, never as financial advice. Subtopic: crypto and blockchain. Vocab (examples): cryptocurrency, blockchain, decentralized, token, mining, exchange, wallet, address, transaction, ledger, smart, contract, volatile, speculative, regulation, custody, protocol, validate, network, consensus.
   - **Curriculum 9 — Intermediate:** "Trí Tuệ Nhân Tạo Trong Kinh Doanh" — AI and automation applied to business operations and customer service. Subtopic: AI in business. Vocab (examples): artificial, intelligence, automate, algorithm, model, predict, dataset, training, chatbot, recommendation, efficiency, productivity, machine, learning, generate, analyze, insight, decision, augment, deploy.
   - **Curriculum 10 — Intermediate:** "An Ninh Mạng Và Quyền Riêng Tư" — Cybersecurity and data privacy fundamentals for digital economy participants. Subtopic: cybersecurity and data privacy. Vocab (examples): cyber, security, password, encryption, privacy, breach, hacker, phishing, malware, firewall, authentication, vulnerable, protect, identity, leak, scam, fraud, sensitive, consent, regulation.

2. THE Curriculum_Creator SHALL select 20 vocabulary words per Digital_Economy_Curriculum such that: (a) every word is semantically tied to that curriculum's named subtopic from criterion 1; (b) words for preintermediate curriculums consist of common, concrete, high-frequency everyday terms; (c) words for intermediate curriculums include subtopic-specific terminology and more abstract concepts; and (d) at least 12 of the 20 selected words SHALL come from, or be direct lexical equivalents of, the example vocabulary listed for that curriculum in criterion 1.
3. THE Curriculum_Creator SHALL ensure vocabulary distinctness across the 10 Digital_Economy_Curriculums such that: (a) for any pair of curriculums, the count of identical lowercased vocabulary words appearing in both `vocabList` arrays is at most 2; and (b) no single vocabulary word SHALL appear in the `vocabList` arrays of more than 2 of the 10 curriculums.
4. THE reading and speakReading passages within every Digital_Economy_Curriculum SHALL meet sentence-complexity bounds appropriate to the curriculum's level, computed as the average sentence length across all reading-type activities in the curriculum: preintermediate curriculums SHALL average 10-14 words per sentence; intermediate curriculums SHALL average 12-18 words per sentence.
5. THE Curriculum_Creator SHALL ground each Digital_Economy_Curriculum in Vietnamese cultural and economic context by including, distributed across the union of its reading passages and introAudio scripts: at least 3 explicit mentions of Vietnamese local platforms or brands (selected from Shopee, Lazada, Tiki, MoMo, VNPay, ZaloPay, Grab, Be, VNG, VinFast, FPT, or comparable recognizable Vietnamese tech/economic entities), AND at least 2 references to familiar Vietnamese daily-life situations or locales (e.g., street vendors going cashless, students freelancing online, parents using Shopee, Hanoi, Ho Chi Minh City, Đà Nẵng).

### Requirement 3: Activity Templates by Skill Focus

**User Story:** As a platform owner, I want distinct activity sequences for each skill focus type, so that story-reading curriculums emphasize narrative reading, speaking curriculums emphasize oral production, and balanced curriculums cover all skills evenly.

#### Acceptance Criteria

1. WHEN a Story_Reading_Curriculum is created, THE 4 sessions SHALL follow this structure (each session introduces 5 new words; the curriculum has 20 unique words total):
   - Session 1: introAudio (welcome + teach Session_Vocab_Group 1), viewFlashcards (group 1, 5 words), speakFlashcards (group 1, 5 words), reading (narrative passage 150-200 words featuring group 1 words), speakReading, readAlong, introAudio (session wrap-up).
   - Session 2: introAudio (recap group 1 + teach Session_Vocab_Group 2), viewFlashcards (group 2, 5 words), speakFlashcards (group 2, 5 words), reading (narrative passage 150-200 words featuring group 2 words and continuing the story), speakReading, readAlong, introAudio (session wrap-up).
   - Session 3: introAudio (recap groups 1-2 + teach Session_Vocab_Group 3), viewFlashcards (group 3, 5 words), speakFlashcards (group 3, 5 words), vocabLevel1 (group 3, 5 words), reading (narrative passage 150-200 words featuring group 3 words and advancing the story), speakReading, readAlong, introAudio (session wrap-up).
   - Session 4 (Final): introAudio (recap + teach Session_Vocab_Group 4), viewFlashcards (group 4, 5 words), speakFlashcards (group 4, 5 words), vocabLevel1 (all 20 words for full review), reading (story conclusion 200-250 words integrating all 20 words), speakReading, readAlong, writingSentence (3-4 items reflecting on the story using vocabulary from across all 4 groups), introAudio (farewell with vocab review).

2. WHEN a Speaking_Curriculum is created, THE 4 sessions SHALL follow this structure:
   - Session 1: introAudio (welcome + teach Session_Vocab_Group 1), viewFlashcards (group 1), speakFlashcards (group 1), vocabLevel1 (group 1), speakFlashcards (group 1, second round for repetition), reading (short conversational/instructional passage 80-110 words), speakReading, introAudio (session wrap-up).
   - Session 2: introAudio (recap group 1 + teach Session_Vocab_Group 2), viewFlashcards (group 2), speakFlashcards (group 2), vocabLevel1 (group 2), speakFlashcards (group 2, second round), reading (short passage 80-110 words), speakReading, introAudio (session wrap-up).
   - Session 3: introAudio (recap + teach Session_Vocab_Group 3), viewFlashcards (group 3), speakFlashcards (group 3), vocabLevel1 (group 3), speakFlashcards (group 3, second round), reading (passage 100-130 words), speakReading, introAudio (session wrap-up).
   - Session 4 (Final): introAudio (recap + teach Session_Vocab_Group 4), viewFlashcards (group 4), speakFlashcards (group 4), vocabLevel1 (group 4), vocabLevel2 (all 20 words for cumulative review), speakFlashcards (all 20 words, final speaking round), reading (passage 120-150 words integrating all 20 words), speakReading, readAlong, writingSentence (2-3 items), introAudio (farewell with vocab review).

3. WHEN a Balanced_Curriculum is created, THE 4 sessions SHALL follow this structure:
   - Session 1: introAudio (welcome + teach Session_Vocab_Group 1), viewFlashcards (group 1), speakFlashcards (group 1), vocabLevel1 (group 1), reading (expository passage 100-130 words featuring group 1 words), speakReading, readAlong, introAudio (session wrap-up).
   - Session 2: introAudio (recap group 1 + teach Session_Vocab_Group 2), viewFlashcards (group 2), speakFlashcards (group 2), vocabLevel1 (group 2), reading (passage 100-130 words featuring group 2 words), speakReading, readAlong, introAudio (session wrap-up).
   - Session 3: introAudio (recap + teach Session_Vocab_Group 3), viewFlashcards (group 3), speakFlashcards (group 3), vocabLevel1 (group 3), reading (passage 100-130 words featuring group 3 words), speakReading, readAlong, writingSentence (2-3 items using group 3 vocabulary), introAudio (session wrap-up).
   - Session 4 (Final): introAudio (recap + teach Session_Vocab_Group 4), viewFlashcards (group 4), speakFlashcards (group 4), vocabLevel1 (group 4), vocabLevel2 (all 20 words for cumulative review), reading (synthesis passage 150-200 words integrating all 20 words), speakReading, readAlong, writingSentence (3-4 items), writingParagraph (1 prompt connecting the subtopic to the learner's life or work), introAudio (farewell with vocab review).

4. THE Curriculum_Creator SHALL ensure all 10 curriculums have exactly 4 learning sessions each.
5. THE Curriculum_Creator SHALL ensure each session contains exactly 5 unique new vocabulary words in its Session_Vocab_Group, and the union of all four Session_Vocab_Groups within a curriculum SHALL contain exactly 20 unique words.
6. THE total estimated learner time per curriculum SHALL fall within 2.5 to 3.5 hours, with each individual session estimated between 40 and 55 minutes.
7. THE Curriculum_Creator SHALL include the listed activities in the listed order within each session for the applicable skill focus, and SHALL NOT insert activities not listed in criteria 1, 2, or 3 for that skill focus.
8. IF a created curriculum violates the activity-template structure defined in criteria 1-7, THEN THE Content_Validator SHALL reject the upload and identify the violating session and activity.

### Requirement 4: Reading Passage Content Standards

**User Story:** As a content quality owner, I want reading passages that are factually grounded, culturally authentic, engaging, and appropriate for the Digital Economy topic, so that learners gain both language skills and meaningful content knowledge about Vietnam's digital economy.

#### Acceptance Criteria

1. WHEN reading passages are created for Story_Reading_Curriculums, THE Curriculum_Creator SHALL write narrative passages — telling stories, describing scenes, or following characters through Digital Economy experiences (a shop owner moving online, a founder building a startup, a vendor adopting digital payments).
2. WHEN reading passages are created for Speaking_Curriculums, THE Curriculum_Creator SHALL write conversational or instructional passages — describing how to do something (place an order, scan a QR code, join a video meeting), explaining a concept simply, or presenting a dialogue scenario.
3. WHEN reading passages are created for Balanced_Curriculums, THE Curriculum_Creator SHALL write expository passages — explaining concepts, describing trends, or presenting information about a Digital Economy subtopic in the Vietnamese context.
4. THE reading passages SHALL be written in English with vocabulary and grammar appropriate to the target level (preintermediate or intermediate).
5. THE reading passages SHALL incorporate Vietnamese Digital Economy cultural context — using local platforms (Shopee, Lazada, Tiki, MoMo, VNPay, ZaloPay, Grab, Be, VNG, VinFast, FPT), familiar daily-life examples (Hanoi, Ho Chi Minh City, street vendors, students, freelancers), and recognizable Vietnamese digital-economy milestones.
6. THE reading passages SHALL present cryptocurrency, AI, and similar technical subtopics in an educational, neutral, factual manner — describing how the technology works and how it is used, never giving investment advice, trading recommendations, or speculative claims about returns.
7. THE reading passages within a curriculum SHALL be thematically continuous — Story_Reading_Curriculums tell one connected story across the 4 sessions, while Speaking_Curriculums and Balanced_Curriculums explore facets of the same subtopic across the 4 sessions.

### Requirement 5: Vocabulary Selection and Distribution

**User Story:** As a content quality owner, I want vocabulary words that are relevant to each curriculum's subtopic, appropriate for the target level, and distributed thoughtfully across sessions, so that learners build cumulative knowledge of digital-economy English in a coherent progression.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL select 20 vocabulary words per Digital_Economy_Curriculum, organized into 4 Session_Vocab_Groups of exactly 5 words each.
2. THE vocabulary words SHALL be specific to the curriculum's Digital_Economy subtopic — words for a cybersecurity curriculum SHALL center on security, privacy, and risk; words for an e-commerce curriculum SHALL center on shopping, ordering, and delivery; and so on.
3. THE vocabulary words SHALL be appropriate for the target level — preintermediate words are common, concrete, and high-frequency; intermediate words include more specialized digital-economy terminology and abstract concepts.
4. THE Curriculum_Creator SHALL group the 20 words into 4 Session_Vocab_Groups in a thematically coherent way — each group SHALL focus on a sub-aspect of the curriculum's subtopic, so that the session reading passage feels naturally built around that group's words.
5. THE `vocabList` field SHALL be an array of lowercase strings using the field name `vocabList` (never `words`).
6. WHERE a vocabulary word is multi-word (e.g., "smart contract", "peer-to-peer"), THE Curriculum_Creator SHALL choose a single-word form when possible (e.g., "contract", "peer") to keep vocabulary entries simple, OR SHALL use the multi-word form lowercased exactly as stored.

### Requirement 6: Marketing Copy and Preview Text

**User Story:** As a content quality owner, I want all marketing text to resonate with Vietnamese adults interested in the digital economy and career advancement, so that learners feel drawn to explore these curriculums.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL write curriculum descriptions as Persuasive_Copy following the multi-paragraph structure: a tone-assigned ALL-CAPS Vietnamese headline opener, a vivid scenario or example tied to Vietnamese daily digital life, a transformation promise (what the learner will be able to do), and a personal/career growth tie-in.
2. THE Curriculum_Creator SHALL write curriculum previews (~150 words) with vivid hooks about the learner's career or daily life in the digital age, a vocabulary word listing, and what the learner will be able to discuss or read in English after completing the curriculum.
3. THE Curriculum_Creator SHALL write all titles, descriptions, and preview text primarily in Vietnamese, as required for preintermediate/intermediate vi-en curriculums.
4. THE Tone_Assigner SHALL assign one of the 6 Tone_Palette types to every curriculum description headline.
5. WHILE assigning tones within a series, THE Tone_Assigner SHALL ensure no two adjacent curriculums (by display order) use the same Tone_Palette type.
6. THE Tone_Assigner SHALL ensure no single Tone_Palette type exceeds 30% of the 10 curriculum descriptions (max 3 uses per tone across the 10 curriculums).
7. THE Persuasive_Copy SHALL connect English learning to the learner's career aspirations in Vietnam's digital economy — discussing tech startups with international investors, reading product specifications, participating in remote work with global teams, or understanding global crypto and AI conversations.

### Requirement 7: Curriculum Titles

**User Story:** As a content quality owner, I want curriculum titles to be minimal, evocative, and in Vietnamese, so that they work well within the series/collection context and attract learners interested in modern digital-economy content.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL produce curriculum titles between 2 and 8 words and at most 50 characters in length, and SHALL NOT include the series name, collection name, content type prefix (e.g., "Story:", "Speaking:"), skill-focus label, or audience suffix.
2. THE Curriculum_Creator SHALL write curriculum titles in Vietnamese, allowing internationally recognized brand names and proper nouns (e.g., Shopee, MoMo, VNG, VinFast, AI, Blockchain) to appear in their conventional spelling.
3. THE curriculum titles SHALL NOT include any difficulty level indicator (e.g., "beginner", "preintermediate", "intermediate", "upper-intermediate", "advanced", "sơ cấp", "sơ trung cấp", "trung cấp", "cao trung cấp", "nâng cao", "A1", "A2", "B1", "B2", "C1", "C2").
4. THE curriculum titles SHALL contain at least one concrete subtopic noun drawn from the curriculum's named Digital_Economy subtopic (e.g., "Shopee", "khởi nghiệp", "ví số", "blockchain", "an ninh mạng").
5. THE 10 curriculum titles SHALL be unique across the spec (no two curriculums share the same title).

### Requirement 8: introAudio Quality Standards

**User Story:** As a content quality owner, I want introAudio scripts that are warm, modern, and educational, so that learners feel guided through both language learning and digital-economy exploration.

#### Acceptance Criteria

1. WHEN a welcome introAudio is created, THE script (500-800 words) SHALL greet the learner warmly, introduce the subtopic with a hook tying it to Vietnamese daily digital life (ordering on Shopee, scanning a QR with MoMo, watching TikTok creators, working remotely with global teams), list the 5 vocabulary words for the session, and teach each word with: the English word, Vietnamese meaning, a contextual example sentence, and an explanation of how the word connects to the curriculum's Digital Economy subtopic.
2. WHEN a session recap introAudio is created (sessions 2+), THE script SHALL briefly recap previous sessions' words with a connecting thread before introducing the new Session_Vocab_Group.
3. WHEN a session wrap-up introAudio is created (mid-curriculum sessions 1-3), THE script (200-400 words) SHALL summarize what the learner just practiced and bridge to the next session.
4. WHEN a farewell introAudio is created at the end of session 4 (400-600 words), THE script SHALL review 5-6 key vocabulary words drawn from across the 20-word curriculum vocabulary, with definitions and fresh example sentences, connect the words back to the curriculum's Digital Economy subtopic, congratulate the learner, and close with a tone-assigned sign-off.
5. THE introAudio scripts SHALL be bilingual — Vietnamese explanations for English vocabulary and concepts.
6. THE Curriculum_Creator SHALL individually craft every introAudio script for its specific curriculum subtopic, without using template functions, string interpolation, or generic fill-in-the-blank patterns.
7. THE Tone_Assigner SHALL assign one of the 5 Farewell_Palette registers to every farewell introAudio.
8. WHILE assigning farewell tones across the 10 curriculums, THE Tone_Assigner SHALL ensure no two adjacent curriculums within the same series use the same Farewell_Palette register.
9. THE Tone_Assigner SHALL ensure each Farewell_Palette register is used 1-3 times across the 10 curriculums (balanced distribution).

### Requirement 9: Activity Schema Compliance

**User Story:** As a platform developer, I want every activity to comply with the platform's content schema, so that the content pipeline processes these curriculums without errors.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL include the fields `activityType`, `title`, `description`, and `data` on every activity object, with `title` and `description` as non-empty strings (each between 1 and 255 characters) and `data` as a non-null object.
2. THE `activityType` field SHALL use exactly one of the following values: `introAudio`, `viewFlashcards`, `speakFlashcards`, `vocabLevel1`, `vocabLevel2`, `reading`, `speakReading`, `readAlong`, `writingSentence`, `writingParagraph`.
3. THE `vocabList` field SHALL be a non-empty array of 1 to 20 lowercase strings (each string 1 to 64 characters), using the field name `vocabList` (never `words`).
4. IF both a viewFlashcards activity and a speakFlashcards activity appear within the same learning session, THEN THE Curriculum_Creator SHALL produce identical `data.vocabList` arrays for the two activities (same elements in the same order).
5. THE Curriculum_Creator SHALL place all activity content fields inside the `data` object and SHALL NOT place content fields directly on the activity object.
6. WHEN a writingSentence activity is created, THE Curriculum_Creator SHALL populate `data.vocabList` (per criterion 3), `data.items` (an array of 1 to 10 items), and SHALL populate each item with a non-empty `prompt` string (1 to 500 characters) and a non-empty `targetVocab` string (1 to 64 characters) that exactly matches one entry in `data.vocabList`.
7. WHEN a writingParagraph activity is created, THE Curriculum_Creator SHALL populate `data.vocabList` (per criterion 3), `data.instructions` (a non-empty string of 1 to 1000 characters), and `data.prompts` (an array of 2 to 10 non-empty strings, each 1 to 500 characters).
8. THE Curriculum_Creator SHALL set activity `title` and `description` according to these conventions, where `<topic>` is the session topic in Vietnamese (1 to 100 characters):
   - viewFlashcards / speakFlashcards / vocabLevel1 / vocabLevel2: `title` = `"Flashcards: <topic>"`; `description` = `"Học N từ: word1, word2, ..."` where N equals the count of items in `data.vocabList` and the listed words are the entries of `data.vocabList` in order, joined by `", "`.
   - reading / speakReading: `title` = `"Đọc: <topic>"`; `description` = the first 80 characters of the reading text (truncated at character 80, no ellipsis appended; if the text is shorter than 80 characters, the full text is used).
   - readAlong: `title` = `"Nghe: <topic>"`; `description` = `"Nghe đoạn văn vừa đọc và theo dõi."`.
   - introAudio: `title` = a Vietnamese label of 5 to 60 characters identifying the script's role (e.g., `"Giới thiệu bài học"`, `"Tổng kết phiên"`, `"Tổng kết bài học"`); `description` = a Vietnamese summary of 20 to 200 characters describing the script's content.
   - writingSentence: `title` = `"Viết: <topic>"`; `description` = a Vietnamese summary of 20 to 200 characters describing the writing task.
   - writingParagraph: `title` = `"Viết: <topic>"`; `description` = a Vietnamese summary of 20 to 200 characters describing the writing task.
9. THE Curriculum_Creator SHALL set each learning session's `title` field to a non-empty Vietnamese string of 5 to 150 characters that names the session's focus within the curriculum subtopic (each session's title within a curriculum SHALL be unique).
10. IF any activity or session fails to satisfy criteria 1 through 9, THEN THE Content_Validator SHALL reject the curriculum content prior to upload, indicate the failing field path and rule, and leave the persisted curriculum state unchanged.

### Requirement 10: Content Validation

**User Story:** As a platform developer, I want every Digital Economy curriculum validated before upload, so that no corrupted content enters the database.

#### Acceptance Criteria

1. THE Content_Validator SHALL verify that every Digital_Economy_Curriculum content JSON has non-null, non-empty `title`, `description`, and `preview.text` fields.
2. THE Content_Validator SHALL verify that `learningSessions` is a non-empty array with exactly 4 sessions, each having a non-empty `title` and non-empty `activities` array.
3. THE Content_Validator SHALL verify that every activity has `activityType` (not `type`), `title`, `description`, and `data` fields, with content fields inside `data`.
4. THE Content_Validator SHALL verify that `activityType` values are in the valid set defined in Requirement 9.
5. THE Content_Validator SHALL verify that vocabList fields contain arrays of lowercase strings using the field name `vocabList` (never `words`).
6. THE Content_Validator SHALL verify that viewFlashcards and speakFlashcards in the same session have identical vocabList arrays.
7. THE Content_Validator SHALL verify that each Session_Vocab_Group taught in a session contains exactly 5 unique words.
8. THE Content_Validator SHALL verify that the union of all Session_Vocab_Groups within a curriculum contains exactly 20 unique words.
9. THE Content_Validator SHALL verify writingSentence data structures (vocabList, items with prompt and targetVocab).
10. THE Content_Validator SHALL verify writingParagraph data structures (vocabList, instructions, prompts with length ≥ 2).
11. THE Content_Validator SHALL verify that no Strip_Keys appear anywhere in the content JSON tree.
12. THE Content_Validator SHALL verify that `contentTypeTags` is `["story"]` for Story_Reading_Curriculums and `[]` for Speaking_Curriculums and Balanced_Curriculums.
13. IF any validation check fails, THEN THE Content_Validator SHALL abort the upload and print the specific rule violation.

### Requirement 11: Pricing

**User Story:** As a platform owner, I want all Digital Economy curriculums priced according to the standard pricing guidelines, so that pricing is consistent with the rest of the catalog.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL call `curriculum/setPrice` with `price: 49` for every Digital_Economy_Curriculum, producing exactly 10 successful `curriculum/setPrice` calls across the spec.
2. WHEN setting price, THE Curriculum_Creator SHALL call `curriculum/setPrice` only after the curriculum has been successfully created via `curriculum/create` AND added to its target series via `curriculum-series/addCurriculum`.
3. IF `curriculum/setPrice` fails, THEN THE Curriculum_Creator SHALL retry up to 3 times with at least 1 second between attempts before logging the failure and continuing with the next curriculum.
4. WHEN all 10 curriculums have been created, THE Curriculum_Creator SHALL verify that the stored price equals 49 for all 10 Digital_Economy_Curriculums via DB query or `curriculum/getOne` and SHALL re-attempt `curriculum/setPrice` for any curriculum whose stored price does not equal 49.

### Requirement 12: Newly Created Curriculums Must Be Private

**User Story:** As a platform owner, I want all newly created Digital Economy curriculums to be private by default, so that they go through content generation (audio, illustrations) before being exposed to learners.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL NOT call `curriculum/setPublic` with `isPublic: true` on any Digital_Economy_Curriculum at any point during the creation, series-wiring, pricing, or documentation phases of this spec.
2. WHEN a Digital_Economy_Curriculum is created via `curriculum/create`, THE Curriculum_Creator SHALL leave it in its default-private state without issuing any subsequent `curriculum/setPublic` call within the spec workflow.
3. IF a `curriculum/setPublic` call is required for any reason during the spec workflow (e.g., explicit rollback), THEN THE Curriculum_Creator SHALL pass `isPublic: false`.

### Requirement 13: Collection and Series Organization

**User Story:** As a platform owner, I want the 10 Digital Economy curriculums organized into a logical collection and series structure, so that learners can browse by skill focus while staying within the broader Digital Economy theme.

#### Acceptance Criteria

1. THE Collection_Organizer SHALL create 1 collection with a Vietnamese title related to Digital Economy learning (e.g., "Học Tiếng Anh Qua Kinh Tế Số") and a neutral, informative Vietnamese description summarizing the digital-economy theme.
2. THE Collection_Organizer SHALL organize the 10 curriculums into 3 series by skill focus:
   - **Series 1 — Story-reading focused (3 curriculums):** Vietnamese title evoking digital-economy stories (e.g., "Câu Chuyện Kinh Tế Số"), description ≤255 chars using a Tone_Palette type. Curriculums 1, 2, 3.
   - **Series 2 — Speaking focused (3 curriculums):** Vietnamese title evoking digital-economy conversation (e.g., "Nói Chuyện Kinh Tế Số"), description ≤255 chars using a different Tone_Palette type. Curriculums 4, 5, 6.
   - **Series 3 — Balanced skills (4 curriculums):** Vietnamese title evoking core digital-economy concepts (e.g., "Khám Phá Kinh Tế Số"), description ≤255 chars using a third Tone_Palette type. Curriculums 7, 8, 9, 10.
3. THE Collection_Organizer SHALL wire each series to the collection via `curriculum-collection/addSeriesToCollection`.
4. THE Collection_Organizer SHALL set display orders for all 3 series within the collection via `curriculum-series/setDisplayOrder`.
5. THE Collection_Organizer SHALL set display orders for all curriculums within each series via `curriculum/setDisplayOrder`.
6. THE Collection_Organizer SHALL ensure all curriculums within each series share `language: "en"` and `userLanguage: "vi"`.
7. WHILE assigning series description tones, THE Tone_Assigner SHALL ensure all 3 series use different Tone_Palette types.
8. THE Collection_Organizer SHALL order curriculums within each series by difficulty (preintermediate before intermediate) and then by topic progression.
9. THE Collection_Organizer SHALL ensure no series contains more than a 1-level gap between curriculum levels (preintermediate-to-intermediate is exactly 1 level gap and is permitted).
10. THE Collection_Organizer SHALL NOT set `displayOrder` on the collection itself per workspace rules.

### Requirement 14: Script Architecture and Workflow

**User Story:** As a developer, I want a clear, repeatable workflow for creating 10 Digital Economy curriculums, so that the process is manageable and traceable.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL produce one standalone Python script per curriculum (10 scripts total).
2. THE Curriculum_Creator SHALL produce one orchestrator script that creates the collection, the 3 series, wires them together, sets display orders, and sets prices.
3. THE Curriculum_Creator SHALL organize scripts into a directory `vi-en-digital-economy-curriculums/`.
4. THE Curriculum_Creator SHALL authenticate all API calls using `firebase_token.get_firebase_id_token` with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`.
5. THE Curriculum_Creator SHALL use `https://helloapi.step.is` as the API base URL.
6. THE Curriculum_Creator SHALL individually craft every piece of learner-facing text for its specific curriculum subtopic, without using template functions, string interpolation, or generic fill-in-the-blank patterns.
7. THE Curriculum_Creator MAY use shared helper functions for activity structure (types, order, data schema) but SHALL hand-write all text content per curriculum.
8. IF a curriculum creation API call fails, THEN THE Curriculum_Creator SHALL log the error with the curriculum title and continue with the next curriculum.

### Requirement 15: Documentation and Cleanup

**User Story:** As a developer, I want proper documentation after all curriculums are created, so that the content is traceable and reproducible.

#### Acceptance Criteria

1. WHEN all 10 curriculums are created and verified, THE Curriculum_Creator SHALL create a README.md documenting: collection ID, all 3 series IDs, all 10 curriculum IDs with titles and display orders, vocabulary lists per curriculum (organized by Session_Vocab_Group), skill focus assignments, tone assignments (description and farewell), pricing, and SQL verification queries.
2. WHEN all curriculums are verified in the database, THE source Python scripts SHALL be deleted, leaving only the README.
3. THE Curriculum_Creator SHALL run a duplicate-check query for each curriculum title after creation and resolve any duplicates (keep earliest, delete extras).

### Requirement 16: Execution Order

**User Story:** As a developer, I want a phased execution plan, so that I can create the infrastructure first and then add curriculums incrementally with verification between phases.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL execute creation in this order: (1) create collection and 3 series via the orchestrator, (2) create the 3 Story_Reading_Curriculums (Curriculums 1-3), (3) create the 3 Speaking_Curriculums (Curriculums 4-6), (4) create the 4 Balanced_Curriculums (Curriculums 7-10).
2. WHEN each curriculum is created, THE Curriculum_Creator SHALL immediately add it to the appropriate series, set its display order, and set its price.
3. WHEN all 10 curriculums are created, THE Curriculum_Creator SHALL verify the complete set by querying the database to confirm all curriculums exist with correct display orders, language values, prices, contentTypeTags, and non-empty content.
4. IF verification reveals missing or malformed curriculums, THEN THE Curriculum_Creator SHALL recreate the affected curriculums before finalizing documentation.
