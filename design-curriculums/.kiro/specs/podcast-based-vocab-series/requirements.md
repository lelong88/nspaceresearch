# Requirements Document

## Introduction

Create a new collection and podcast-based vocabulary series for learning English vocabulary through popular podcast episodes. Instead of topic-based reading passages, song lyrics, or movie dialogue, each curriculum uses verbatim podcast transcript excerpts as the reading content. Vocabulary words are drawn from the transcripts of carefully selected evergreen or popular podcast episodes that are clear, comprehensible, and appropriate for pre-intermediate to intermediate Vietnamese learners of English.

A brand new collection — "Học Từ Vựng Qua Podcast (Learn Vocabulary Through Podcasts)" — is created via `curriculum-collection/create` to house the podcast series. This collection is separate from the existing music collection, cinema collection, and topic-based vocabulary collection because podcast-based learning is a distinct pedagogical approach that deserves its own top-level shelf.

Each curriculum is built around a single podcast episode. The content JSON includes a `youtubeUrl` field linking to the podcast episode on YouTube. Podcast episodes must be from evergreen or popular podcasts (e.g., TED Talks, well-known educational podcasts), feature clear pronunciation and enunciation, and contain language at the A2-B1 level for pre-intermediate to intermediate vi-en learners. The series follows the same 18-word / 5-session structure as the existing song-based and movie-based vocab series, with the key difference that reading passages are replaced by verbatim podcast transcript excerpts.

### Proposed Collection & Series

**Collection:** "Học Từ Vựng Qua Podcast (Learn Vocabulary Through Podcasts)" — a new top-level collection created via `curriculum-collection/create`.

**Series:** "Học Từ Vựng Qua Podcast (Learn Vocabulary Through Podcasts)" — display_order 100 within the new collection. Each curriculum is one podcast episode, with 4 curriculums in the initial series.

## Glossary

- **Collection**: Top-level organizational shelf in the platform. A new collection "Học Từ Vựng Qua Podcast (Learn Vocabulary Through Podcasts)" is created for this feature via `curriculum-collection/create`.
- **Series**: A thematic grouping within a collection, containing multiple curriculums. The podcast series lives inside the new podcast collection.
- **Curriculum**: A single learning unit with 18 vocabulary words, 5 sessions (3 learning + 1 review + 1 full reading), and a fixed activity pattern. In this series, each curriculum is based on one podcast episode.
- **Session**: One of 5 ordered segments within a curriculum. Learning sessions (1–3) contain 12 activities each; Session 4 (review) contains 4 activities; Session 5 (full reading + farewell) contains 5 activities.
- **Activity**: An individual learning exercise within a session (e.g., introAudio, viewFlashcards, reading).
- **Podcast_Transcript**: The verbatim transcript or excerpt from a specific podcast episode, used as the reading passage content. Transcripts must be sourced accurately and attributed to the correct podcast and episode.
- **YouTube_URL**: A link to the podcast episode on YouTube (many popular podcasts and TED Talks are available on YouTube), included in the curriculum content JSON as a `youtubeUrl` field.
- **Display_Order**: Integer field controlling the sort position of curriculums within a series and series within a collection.
- **Creation_Script**: A Python script that calls the helloapi REST API to create a curriculum, add it to a series, and set its display order.
- **Strip_Keys**: The process of removing auto-generated platform keys (mp3Url, illustrationSet, segments, etc.) from curriculum content before upload.
- **Persuasive_Copy**: The required emotional sales copy style for all learner-facing text (descriptions, previews, introAudio scripts).
- **API**: The helloapi.step.is REST API used for all CRUD operations on curriculums, series, and collections.
- **Evergreen_Podcast_Episode**: A podcast episode that has enduring popularity and educational relevance, not a short-lived trend. Examples: TED Talks, well-known educational podcasts (e.g., TED Radio Hour, Freakonomics, Hidden Brain), informative episodes from established podcast series spanning multiple topics and genres.

## Requirements

### Requirement 1: Collection and Series Creation

**User Story:** As a content manager, I want to create a new collection and a podcast-based vocabulary series within it, so that learners can discover and access podcast-based vocabulary learning as a distinct content category on the platform.

#### Acceptance Criteria

1. WHEN the collection is created, THE API SHALL be called via `curriculum-collection/create` with the title "Học Từ Vựng Qua Podcast (Learn Vocabulary Through Podcasts)", a persuasive Vietnamese description, and `isPublic: true`.
2. WHEN the series is created, THE API SHALL be called via `curriculum-series/create` with the title "Học Từ Vựng Qua Podcast (Learn Vocabulary Through Podcasts)", a persuasive Vietnamese description (under 255 characters), and `isPublic: true`.
3. WHEN the series is created, THE Creation_Script SHALL call `curriculum-collection/addSeriesToCollection` with the newly created collection ID and the new series ID.
4. THE Creation_Script SHALL assign `display_order: 100` to the new series via `curriculum-series/setDisplayOrder`, as the first series in the new collection.
5. WHEN the series is fully populated, THE Series SHALL contain exactly 4 curriculums, each based on a different podcast episode.

### Requirement 2: Podcast Episode Selection Criteria

**User Story:** As a content manager, I want podcast episodes to be carefully selected for language-learning suitability, so that the transcript serves as effective reading material for pre-intermediate to intermediate Vietnamese learners of English.

#### Acceptance Criteria

1. THE Curriculum SHALL be based on a podcast episode that is evergreen — having enduring popularity and educational relevance beyond a single release cycle.
2. THE Curriculum SHALL be based on a podcast episode with clear pronunciation and enunciation by the speaker(s), excluding episodes with heavy accents, mumbled delivery, or excessive crosstalk that makes the transcript difficult to follow audibly.
3. THE Curriculum SHALL be based on a podcast episode whose transcript is predominantly at the A2-B1 English level — containing clear vocabulary and sentence structures appropriate for pre-intermediate to intermediate learners.
4. THE Curriculum SHALL be based on a podcast episode whose content does not contain excessive profanity, graphic descriptions, or culturally inappropriate content for a language-learning context.
5. THE Curriculum SHALL be based on a podcast episode from a podcast that is well-known enough that learners can find the episode easily on YouTube.
6. THE Curriculum SHALL be based on a podcast episode with sufficient transcript length to yield 18 teachable vocabulary words and provide meaningful reading passages for 3 learning sessions plus a full reading session.
7. THE Curriculum SHALL be based on a podcast episode that is educational, informational, or storytelling in nature — not purely casual conversation or unstructured chat without substantive content.

### Requirement 3: Podcast Transcript as Reading Content

**User Story:** As a content manager, I want each curriculum's reading passages to be the verbatim transcript excerpt from the selected podcast episode, so that learners read and study real podcast text rather than authored articles.

#### Acceptance Criteria

1. THE Curriculum reading activities SHALL use verbatim podcast transcript excerpts as the reading text, not paraphrased or summarized versions.
2. WHEN a learning session (Sessions 1–3) contains a reading activity, THE reading text SHALL be a portion of the podcast transcript corresponding to that session's vocabulary focus (e.g., transcript segments that contain the session's 6 vocabulary words).
3. WHEN Session 4 (review) or Session 5 (full reading) contains a reading activity, THE reading text SHALL be the complete podcast transcript excerpt from beginning to end.
4. THE Curriculum content JSON SHALL include a `youtubeUrl` field at the top level (alongside `title`, `description`, `preview`, `learningSessions`) containing a valid YouTube URL for the podcast episode.
5. THE Podcast_Transcript used in reading activities SHALL be sourced via web search to ensure verbatim accuracy, and SHALL credit the podcast name and episode title in the curriculum title and introAudio scripts.

### Requirement 4: Curriculum Structure Compliance

**User Story:** As a content manager, I want each podcast curriculum to follow the established 18-word / 5-session structure, so that the learning experience is consistent with the rest of the platform.

#### Acceptance Criteria

1. THE Curriculum SHALL contain exactly 18 vocabulary words drawn from the podcast transcript, divided into 3 groups of 6 words (W1, W2, W3) across 3 learning sessions.
2. THE Curriculum SHALL contain exactly 5 sessions: Session 1 (learning, words 1–6), Session 2 (learning, words 7–12), Session 3 (learning, words 13–18), Session 4 (review of all 18 words), Session 5 (full reading with farewell).
3. WHEN a learning session (Sessions 1–3) is created, THE Session SHALL contain activities in this exact order: introAudio, introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, vocabLevel3, introAudio, reading, speakReading, readAlong, writingSentence (12 activities).
4. WHEN Session 4 (review) is created, THE Session SHALL contain activities in this exact order: introAudio, viewFlashcards, vocabLevel1, vocabLevel2 (4 activities).
5. WHEN Session 5 (full reading + farewell) is created, THE Session SHALL contain activities in this exact order: introAudio, reading, speakReading, readAlong, introAudio (5 activities).
6. THE Curriculum SHALL set `language: "en"` and `userLanguage: "vi"` as top-level body parameters in the `curriculum/create` API call.
7. WHEN a curriculum is created, THE Creation_Script SHALL pass `language` and `userLanguage` as separate top-level body fields alongside `content`, not only inside the content JSON.

### Requirement 5: Vocabulary Selection from Transcript

**User Story:** As a content manager, I want vocabulary words to be drawn directly from the podcast transcript, so that learners encounter these words naturally when reading and listening to the episode.

#### Acceptance Criteria

1. THE Curriculum SHALL select 18 vocabulary words that appear in the podcast transcript and are useful for A2-B1 level Vietnamese learners of English.
2. THE Curriculum SHALL prioritize words that are: (a) genuinely present in the transcript, (b) at the A2-B1 level, (c) broadly useful beyond the podcast context, and (d) teachable with clear definitions and example sentences.
3. THE Curriculum SHALL NOT select function words (articles, prepositions, pronouns) or extremely common words (go, have, make) as vocabulary items unless they appear in an idiomatic or phrasal context worth teaching.

### Requirement 6: Content Quality — Persuasive Copy (Podcast-Adapted)

**User Story:** As a content manager, I want all learner-facing text to follow the persuasive copy style adapted for podcast-based learning, so that learners feel emotionally engaged and excited to learn vocabulary through podcasts.

#### Acceptance Criteria

1. THE Curriculum description SHALL follow the 5-beat persuasive copy structure, adapted to reference the podcast, episode, and the emotional connection between podcast listening and language learning.
2. THE Curriculum preview (~150 words) SHALL open with a vivid hook related to the podcast episode or its themes, name the vocabulary words, and describe the learning journey through the episode's transcript.
3. WHEN an introAudio activity is created for Sessions 1–3, THE introAudio script SHALL reference the podcast name, episode title, and the context of the transcript when teaching vocabulary — explaining how each word appears in the episode and what it means in that context.
4. WHEN an introAudio activity is created for Session 4 (review), THE introAudio script SHALL congratulate the learner, recap the podcast episode's themes and vocabulary from Sessions 1–3, and motivate for the full transcript reading.
5. WHEN an introAudio activity is created for Session 5 (farewell), THE introAudio script (400–600 words) SHALL review each vocabulary word with a fresh example sentence, reference the podcast episode one final time, and provide a warm farewell.
6. THE Curriculum SHALL use Vietnamese for all user-facing text (title, description, preview, introAudio scripts, writing prompts) and English for the podcast transcript in reading activities.

### Requirement 7: Content Quality — Writing Prompts (Podcast-Themed)

**User Story:** As a content manager, I want writing prompts to connect vocabulary to the podcast episode's themes, so that learners practice words in contexts inspired by the content they just studied.

#### Acceptance Criteria

1. THE writingSentence activity SHALL provide a detailed prompt specifying a context related to the podcast episode's themes for using the word, plus an example sentence, in the format: "Sử dụng từ 'X' để nói về [specific context related to the podcast episode's themes]. Ví dụ: [full example sentence]."
2. THE writingSentence prompt SHALL reference the podcast episode's themes, ideas, or narrative — not use generic fill-in-the-blank templates.

### Requirement 8: Activity Metadata

**User Story:** As a content manager, I want every activity to have proper title and description fields, so that server-side logging and client display work correctly.

#### Acceptance Criteria

1. THE Activity SHALL include both a `title` and `description` field for every activity in every session.
2. WHEN a viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, or vocabLevel3 activity is created, THE Activity title SHALL follow the format "Flashcards: <podcast-episode-related topic>" and the description SHALL list the words being learned.
3. WHEN a reading or speakReading activity is created, THE Activity title SHALL follow the format "Đọc: <episode title>" and the description SHALL contain the first ~80 characters of the transcript text.
4. WHEN a readAlong activity is created, THE Activity title SHALL follow the format "Nghe: <episode title>" and the description SHALL be "Nghe podcast và theo dõi."
5. WHEN an introAudio activity is created, THE Activity title SHALL be a descriptive label (e.g., "Giới thiệu podcast", "Giới thiệu từ vựng") and the description SHALL be a brief summary.
6. WHEN a writingSentence activity is created, THE Activity title SHALL follow the format "Viết: <podcast-episode-related topic>" and the description SHALL briefly summarize the writing task.
7. THE Session object SHALL include a `title` field (e.g., "Buổi 1: <transcript topic>", "Ôn tập", "Đọc toàn bộ transcript").

### Requirement 9: Strip-Keys Compliance

**User Story:** As a content manager, I want new curriculum content to never include auto-generated platform keys, so that the platform correctly generates fresh metadata after upload.

#### Acceptance Criteria

1. THE Curriculum content SHALL NOT include any of the following auto-generated keys: `mp3Url`, `illustrationSet`, `chapterBookmarks`, `segments`, `whiteboardItems`, `userReadingId`, `lessonUniqueId`, `curriculumTags`, `taskId`, `imageId`.

### Requirement 10: Display Order and Organization

**User Story:** As a content manager, I want curriculums and the series to have explicit display orders, so that they appear in the intended sequence in the client app.

#### Acceptance Criteria

1. WHEN a curriculum is added to the series via `curriculum-series/addCurriculum`, THE Creation_Script SHALL call `curriculum/setDisplayOrder` to assign a sequential integer display order (0, 1, 2, 3) for the 4 curriculums within the series.
2. THE Creation_Script SHALL assign display_order 100 to the podcast series within the new collection, as the first (and initially only) series.
3. WHEN all curriculums are created and ordered, THE Series SHALL contain exactly 4 curriculums, sorted by display_order.

### Requirement 11: Script Organization

**User Story:** As a content manager, I want one Python script per curriculum plus an orchestrator script for series-level setup, so that each curriculum's content is self-contained and files remain manageable.

#### Acceptance Criteria

1. THE Creation_Script architecture SHALL use one Python script per curriculum (e.g., `create_podcast_1_<podcast>.py`, `create_podcast_2_<podcast>.py`) with all text content hand-written in that script.
2. THE Creation_Script architecture SHALL include one orchestrator script that handles collection creation, series creation, adding curriculums to the series, adding the series to the new collection, and setting display orders.
3. THE Creation_Script SHALL NOT use template functions, string interpolation, or loops to generate learner-facing text content.
4. WHEN a curriculum is successfully created and verified in the database, THE source script SHALL be deleted, leaving only a README with creation method, SQL queries, and recreation context.

### Requirement 12: No Templated Content

**User Story:** As a content manager, I want every piece of learner-facing text to be individually crafted per podcast episode, so that each curriculum reads as if written by someone who deeply understands that specific podcast and its content.

#### Acceptance Criteria

1. THE Creation_Script SHALL NOT use `f-string` interpolation, template functions, or shared text skeletons to generate introAudio scripts, descriptions, previews, or writing prompts.
2. THE Creation_Script MAY use shared helper functions for activity structure (types, order, data schema) but SHALL hand-write all text content per curriculum.

### Requirement 13: Language and Level Homogeneity

**User Story:** As a content manager, I want all curriculums in the podcast series to share the same language pair and similar difficulty levels, so that the series remains internally consistent.

#### Acceptance Criteria

1. THE Curriculum SHALL set `language: "en"` and `userLanguage: "vi"` for every curriculum in the series.
2. THE Series SHALL contain curriculums within a maximum 1-level gap from the highest-level curriculum in the series.
3. THE Series title and description SHALL be written in Vietnamese with English elements, consistent with the bilingual convention for vi-en A2-B1 content.

### Requirement 14: Curriculum Titles — Bilingual with Podcast Attribution

**User Story:** As a content manager, I want curriculum titles to clearly identify the podcast episode and podcast name, so that learners know exactly which episode they will be studying.

#### Acceptance Criteria

1. THE Curriculum title SHALL include both the episode title and podcast name, formatted bilingually (Vietnamese framing + English episode/podcast name), e.g., "Học Qua Podcast: 'Episode Title' – Podcast Name".
2. THE Curriculum title SHALL NOT include difficulty level descriptors (e.g., "Upper-Intermediate").

### Requirement 15: YouTube URL in Content JSON

**User Story:** As a content manager, I want each curriculum's content JSON to include a YouTube link to the podcast episode, so that learners can easily watch and listen to the original episode.

#### Acceptance Criteria

1. THE Curriculum content JSON SHALL include a `youtubeUrl` field at the top level containing a valid YouTube URL for the podcast episode.
2. THE `youtubeUrl` SHALL link to an official upload, well-known channel upload, or high-quality video of the podcast episode on YouTube.
3. THE `youtubeUrl` SHALL be verified via web search to ensure the link is valid and points to the correct podcast episode.

### Requirement 16: Newly Created Curriculums Must Be Private

**User Story:** As a content manager, I want all newly created curriculums to be private by default, so that they go through content generation (audio, illustrations) before being exposed to learners.

#### Acceptance Criteria

1. WHEN a curriculum is created via `curriculum/create`, THE Curriculum SHALL have `is_public: false` (the platform default).
2. THE Creation_Script SHALL NOT call `curriculum/setPublic` with `isPublic: true` on any newly created curriculum.

### Requirement 17: Folder and README Structure

**User Story:** As a content manager, I want the podcast series to have its own folder with a README tracking creation details, so that content is recoverable and auditable.

#### Acceptance Criteria

1. THE workspace SHALL contain a dedicated folder `podcast-based-vocab-series/` for the series.
2. WHEN all curriculums in the series are successfully created, THE folder SHALL contain a README.md documenting: collection ID and title, series ID, curriculum IDs and titles (with podcast/episode), YouTube URLs used, how content was created, SQL queries to find the curriculums in the DB, and enough context to recreate if needed.
3. WHEN all curriculums are verified in the database, THE source Python scripts SHALL be deleted from the folder, leaving only the README.
