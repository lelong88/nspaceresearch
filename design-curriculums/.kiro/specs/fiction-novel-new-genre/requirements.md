# Requirements Document

## Introduction

This document defines the requirements for creating a new original fiction novel curriculum series for the Vietnamese-English bilingual language-learning platform. The novel follows the same structural template as "The Little Bookshop by the Sea" (10 chapters, 6 sessions each, 15 vocab words per chapter) but uses a different genre and an entirely new plot. The genre chosen is **mystery/detective** — a compelling genre for language learners because it naturally drives page-turning engagement, contextualizes vocabulary through clues and investigation, and sustains a story arc across 10 chapters.

The novel tells the story of a young Vietnamese-Australian journalist, Mai Nguyen, who returns to a small mountain town in rural England to write a travel article, only to discover that the town's beloved clocktower has stopped — and the elderly clockmaker has vanished. Over 10 chapters, Mai investigates the disappearance, uncovers the town's secrets, and solves the mystery.

## Glossary

- **Novel**: The complete 10-chapter original English fiction story
- **Chapter**: One of 10 installments of the novel, each converted into one curriculum
- **Curriculum**: A single uploadable learning unit in the platform, corresponding to one chapter
- **Series**: A grouping of 10 chapter curriculums under one novel title in the platform
- **Collection**: The top-level shelf (Truyện / Fiction) that contains the series
- **Session**: One of 6 learning sessions within a chapter curriculum (Phần 1–5 + Ôn tập)
- **Passage**: One of 5 reading passage segments within a chapter (~150–200 words each)
- **Vocab_Word**: One of 15 A2-B1 English vocabulary words per chapter, used as contextual refreshers
- **Content_Module**: A Python file (`chapterN_content.py`) exporting the curriculum dict for one chapter
- **Creation_Script**: A Python script that uploads a chapter curriculum via the API
- **Validation_Script**: A Python script (`validate_content.py`) that checks all correctness properties before upload
- **Strip_Keys**: The process of removing auto-generated platform keys from curriculum JSON
- **Platform**: The helloapi.step.is language-learning application
- **Learner**: A Vietnamese-speaking user learning English at preintermediate level
- **audioSpeed**: The playback speed modifier for audio activities (set to -0.2)

## Requirements

### Requirement 1: Novel Concept and Story Arc

**User Story:** As a curriculum designer, I want a complete 10-chapter mystery novel with a coherent story arc, so that learners stay engaged across the entire series.

#### Acceptance Criteria

1. THE Novel SHALL consist of exactly 10 chapters, each advancing a single continuous mystery plot
2. THE Novel SHALL use the mystery/detective genre with a central disappearance or puzzle driving the narrative
3. THE Novel SHALL feature a protagonist who is relatable to Vietnamese learners and operates in an English-speaking setting
4. THE Novel SHALL include a cast of supporting characters introduced progressively across chapters, with each character serving a narrative purpose
5. THE Novel SHALL follow a classic story arc: setup (chapters 1–2), rising action and investigation (chapters 3–7), climax (chapter 8–9), and resolution (chapter 10)
6. THE Novel SHALL resolve all major plot threads by the end of chapter 10
7. THE Novel SHALL use simple, natural English prose appropriate for A2-B1 (preintermediate) readers

### Requirement 2: Chapter Structure

**User Story:** As a curriculum designer, I want each chapter to follow a consistent internal structure, so that the learning experience is predictable and the content modules are uniform.

#### Acceptance Criteria

1. THE Chapter SHALL contain exactly 5 reading passage segments
2. THE Chapter SHALL use exactly 15 distinct A2-B1 vocabulary words, with 3 words assigned to each of the 5 passages
3. WHEN a passage is written, THE Chapter SHALL naturally incorporate its 3 assigned vocabulary words in context within the prose
4. THE Chapter SHALL have a total reading length of approximately 750–1000 words across all 5 passages (approximately 150–200 words per passage)
5. THE Chapter SHALL have a Vietnamese title and an English title, formatted as: "[Vietnamese Title] ([English Title])"
6. THE Chapter SHALL advance the mystery plot meaningfully, introducing new clues, characters, or revelations

### Requirement 3: Vocabulary Selection

**User Story:** As a curriculum designer, I want each chapter's 15 vocabulary words to be familiar A2-B1 words used as contextual refreshers, so that learners reinforce known vocabulary through fiction.

#### Acceptance Criteria

1. THE Vocab_Word list for each chapter SHALL contain exactly 15 English words at A2-B1 (preintermediate) level
2. THE Vocab_Word list SHALL consist of words that are common and familiar to preintermediate learners, serving as refreshers rather than new introductions
3. THE Vocab_Word list for each chapter SHALL avoid repeating words used in other chapters of the same novel
4. WHEN a Vocab_Word is selected, THE Vocab_Word SHALL be naturally usable within the mystery/detective narrative context
5. THE Vocab_Word SHALL have a Vietnamese translation provided in the flashcard data
6. THE Vocab_Word SHALL have an example sentence that relates to the chapter's story context

### Requirement 4: Curriculum Structure per Chapter

**User Story:** As a curriculum designer, I want each chapter curriculum to have exactly 6 sessions with the correct activity types, so that the learning flow matches the established novel curriculum pattern.

#### Acceptance Criteria

1. THE Curriculum SHALL contain exactly 6 sessions
2. WHEN sessions 1 through 5 are created, THE Session SHALL contain exactly 3 activities in order: viewFlashcards, reading, readAlong
3. WHEN session 6 is created, THE Session SHALL contain exactly 2 activities in order: viewFlashcards, readAlong
4. WHEN a viewFlashcards activity in sessions 1–5 is created, THE viewFlashcards activity SHALL contain exactly 3 vocabulary words (the 3 words assigned to that passage)
5. WHEN the viewFlashcards activity in session 6 is created, THE viewFlashcards activity SHALL contain all 15 vocabulary words from the chapter
6. WHEN a reading activity is created, THE reading activity SHALL contain the passage text for that session's segment
7. WHEN a readAlong activity in sessions 1–5 is created, THE readAlong activity SHALL contain the same passage text as the corresponding reading activity
8. WHEN the readAlong activity in session 6 is created, THE readAlong activity SHALL contain the full chapter text (all 5 passages concatenated)
9. THE Curriculum SHALL set audioSpeed to -0.2 for all activities that support audio playback

### Requirement 5: Vietnamese Bilingual Content

**User Story:** As a curriculum designer, I want all user-facing metadata in Vietnamese with English where appropriate, so that the curriculum is accessible to Vietnamese-speaking learners.

#### Acceptance Criteria

1. THE Curriculum title SHALL be in Vietnamese with the English title in parentheses, following the format: "[Series Vietnamese Title] ([Series English Title]) — Chương N: [Chapter Vietnamese Title] ([Chapter English Title])"
2. THE Curriculum preview SHALL be written in Vietnamese, approximately 150 words, describing the chapter content with vivid hooks, listing all 15 vocabulary words, and describing the learning journey
3. THE Curriculum description SHALL be a short Vietnamese summary of the chapter
4. WHEN a session title is created for sessions 1–5, THE Session title SHALL be "Phần N" where N is the session number
5. WHEN a session title is created for session 6, THE Session title SHALL be "Ôn tập"
6. THE viewFlashcards activity title SHALL follow the format "Flashcards: [topic]" with description "Học N từ: word1, word2, ..."
7. THE reading activity title SHALL follow the format "Đọc: [topic]" with description containing the first ~80 characters of the reading text
8. THE readAlong activity title for sessions 1–5 SHALL follow the format "Nghe: [topic]" with description "Nghe đoạn văn vừa đọc và theo dõi."
9. THE readAlong activity title for session 6 SHALL use "Nghe: Toàn bộ câu chuyện" or equivalent full-chapter label
10. THE Curriculum SHALL set language to "en" and userLanguage to "vi"

### Requirement 6: Content Module and Script Creation

**User Story:** As a curriculum designer, I want Python content modules and creation scripts for each chapter, so that curriculums can be uploaded to the platform programmatically.

#### Acceptance Criteria

1. WHEN a chapter is prepared for upload, THE Content_Module SHALL export a complete curriculum dict matching the platform's expected JSON structure
2. THE Content_Module SHALL NOT include any auto-generated platform keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId)
3. THE Creation_Script SHALL authenticate using firebase_token.get_firebase_id_token with the standard UID
4. THE Creation_Script SHALL call the curriculum/create API endpoint to upload each chapter
5. WHEN all 10 chapters are uploaded, THE Creation_Script SHALL create a new curriculum series, add all 10 curriculums to the series, and attach the series to the Fiction (Truyện) collection
6. THE Creation_Script SHALL set display_order 1–10 for the 10 chapter curriculums within the series
7. THE Creation_Script SHALL NOT hardcode any curriculum IDs, series IDs, or collection IDs — all IDs SHALL be looked up by title or obtained from API responses at runtime

### Requirement 7: Content Validation

**User Story:** As a curriculum designer, I want all content validated against correctness properties before upload, so that structural and content errors are caught early.

#### Acceptance Criteria

1. THE Validation_Script SHALL verify that each chapter curriculum contains exactly 6 sessions
2. THE Validation_Script SHALL verify that sessions 1–5 each contain exactly 3 activities (viewFlashcards, reading, readAlong) in the correct order
3. THE Validation_Script SHALL verify that session 6 contains exactly 2 activities (viewFlashcards, readAlong) in the correct order
4. THE Validation_Script SHALL verify that each session 1–5 viewFlashcards activity contains exactly 3 vocabulary words
5. THE Validation_Script SHALL verify that the session 6 viewFlashcards activity contains exactly 15 vocabulary words
6. THE Validation_Script SHALL verify that the session 6 readAlong text equals the concatenation of all 5 passage texts
7. THE Validation_Script SHALL verify that each passage contains its 3 assigned vocabulary words in the text
8. THE Validation_Script SHALL verify that no auto-generated platform keys are present in the curriculum JSON
9. THE Validation_Script SHALL verify that all activities have non-empty title and description fields
10. THE Validation_Script SHALL verify that the curriculum title, preview, and description are in Vietnamese (contain Vietnamese characters)
11. THE Validation_Script SHALL verify that reading passages are in English
12. THE Validation_Script SHALL verify that audioSpeed is set to -0.2 for all applicable activities
13. THE Validation_Script SHALL verify that no vocabulary word is repeated across chapters within the novel
14. IF the Validation_Script detects a violation, THEN THE Validation_Script SHALL report the specific chapter, session, activity, and nature of the violation

### Requirement 8: Series Organization

**User Story:** As a curriculum designer, I want the novel series properly organized in the platform's collection hierarchy, so that learners can discover and navigate the novel.

#### Acceptance Criteria

1. THE Series SHALL be created with a Vietnamese title containing the English title in parentheses
2. THE Series SHALL be added to the existing Fiction (Truyện) collection (ID: 97cee550)
3. THE Series SHALL contain all 10 chapter curriculums in display_order 1–10
4. THE Series SHALL have language "en" and userLanguage "vi" consistent across all curriculums
5. THE Series SHALL be set to public visibility after all chapters are uploaded and validated
6. THE Series title SHALL NOT include any difficulty level descriptor

### Requirement 9: Source Material Management

**User Story:** As a curriculum designer, I want source materials managed according to workspace conventions, so that the workspace stays clean and content is recoverable.

#### Acceptance Criteria

1. WHEN all chapters are successfully uploaded to the database, THE Creation_Script source files (Python content modules, creation scripts, validation scripts) SHALL be deleted from the workspace
2. THE Novel folder SHALL retain only a README.md file after successful upload
3. THE README.md SHALL document: how the content was created, the series ID, the collection it belongs to, SQL queries to find all chapter curriculums in the database, a novel summary, and enough context to recreate the source materials
4. THE README.md SHALL include a SQL query that retrieves all chapter curriculums by series ID with title and display_order

### Requirement 10: Reading Passage Quality

**User Story:** As a curriculum designer, I want reading passages that are engaging, level-appropriate, and serve the mystery narrative, so that learners enjoy reading while reinforcing vocabulary.

#### Acceptance Criteria

1. THE Passage SHALL use simple, natural English prose at A2-B1 level (short sentences, common grammar structures, limited use of complex clauses)
2. THE Passage SHALL advance the chapter's plot segment meaningfully — each passage moves the story forward
3. THE Passage SHALL incorporate its 3 assigned vocabulary words naturally in context, not forced or artificial
4. THE Passage SHALL be approximately 150–200 words in length
5. THE Passage SHALL use concrete, visual language that helps learners build mental images of the scene
6. THE Passage SHALL avoid culturally obscure references, idioms, or slang that preintermediate learners would not understand
7. WHEN dialogue is used in a Passage, THE Passage SHALL use simple, natural conversational English appropriate for A2-B1 level
