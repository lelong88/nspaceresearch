# Requirements Document

## Introduction

This feature creates a new original fiction novel curriculum series at the upper-intermediate (B2) level for English-only (en-en) learners. The novel is 20 chapters long, following the same structural template as "The Last Light of Alder House" (series ID: 70b5bb22) — 6 sessions per chapter, 4 vocab words per session 1–5, 20 vocab per chapter review, reading passages of ~150–290 words each. However, this novel uses a completely different genre and plot from Alder House (which is mystery/gothic). The genre chosen is **science fiction / near-future** — a compelling genre for upper-intermediate readers because it introduces speculative concepts through accessible prose, naturally contextualizes sophisticated vocabulary, and sustains curiosity across a longer arc.

Since this is en-en (English only), all user-facing text — titles, descriptions, previews, session titles, activity titles — is written entirely in English. There is no bilingual content. Per the platform's language policy, upper-intermediate content may be single-language (target language only), and we exercise that option here.

The novel cannot be placed in the existing "Truyện (Fiction)" collection (ID: 97cee550) because that collection contains vi-en content. Per the language homogeneity rule, an en-en novel requires its own collection (or an existing en-en fiction collection). The creation script must create or find an appropriate en-en fiction collection at runtime.

## Glossary

- **Novel**: The complete 20-chapter original English science fiction story
- **Chapter**: One of 20 installments of the Novel, each converted into one Curriculum
- **Curriculum**: A single uploadable learning unit in the platform, corresponding to one Chapter
- **Series**: A grouping of 20 Chapter Curriculums under one novel title in the platform
- **Collection**: A top-level shelf that contains the Series; must be an en-en collection (not the vi-en Fiction collection)
- **Session**: One of 6 learning sessions within a Chapter Curriculum (Session 1–5 + Review)
- **Passage**: One of 5 reading passage segments within a Chapter (~150–290 words each)
- **Vocab_Word**: One of 20 B2-level English vocabulary words per Chapter, used as contextual refreshers
- **Content_Module**: A Python file (`chapterN_content.py`) exporting the curriculum dict for one Chapter
- **Creation_Script**: A Python script (`create_all_chapters.py`) that uploads all Chapter Curriculums, creates the Series, and attaches it to the Collection
- **Validation_Script**: A Python script (`validate_content.py`) that checks all correctness properties before upload
- **Strip_Keys**: Auto-generated platform keys that must never appear in new content (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId)
- **Platform**: The helloapi.step.is language-learning application
- **Learner**: An English-speaking user reading at upper-intermediate (B2) level
- **audioSpeed**: The playback speed modifier for audio activities (set to -0.2)
- **en-en**: English target language with English user language — single-language, no bilingual content

## Requirements

### Requirement 1: Novel Concept and Story Arc

**User Story:** As a curriculum designer, I want a complete 20-chapter science fiction novel with a coherent story arc, so that upper-intermediate learners stay engaged across the entire series.

#### Acceptance Criteria

1. THE Novel SHALL consist of exactly 20 Chapters, each advancing a single continuous science fiction plot
2. THE Novel SHALL use the science fiction / near-future genre — entirely different from the mystery/gothic genre of "The Last Light of Alder House" and the mystery/detective genre of "The Silent Clocktower"
3. THE Novel SHALL feature a protagonist and setting that are accessible and relatable to a general English-reading audience
4. THE Novel SHALL include a cast of supporting characters introduced progressively across Chapters, with each character serving a narrative purpose
5. THE Novel SHALL follow a multi-act story arc: setup (chapters 1–4), rising action (chapters 5–10), midpoint shift (chapters 11–13), escalation (chapters 14–17), climax (chapters 18–19), and resolution (chapter 20)
6. THE Novel SHALL resolve all major plot threads by the end of Chapter 20
7. THE Novel SHALL use clear, natural English prose appropriate for upper-intermediate (B2) readers — more complex sentence structures and vocabulary than preintermediate, but still ~95% comprehensible without a dictionary

### Requirement 2: Chapter Structure

**User Story:** As a curriculum designer, I want each chapter to follow a consistent internal structure matching the Alder House template, so that the learning experience is predictable and the content modules are uniform.

#### Acceptance Criteria

1. THE Chapter SHALL contain exactly 5 reading Passage segments
2. THE Chapter SHALL use exactly 20 distinct B2-level Vocab_Words, with 4 words assigned to each of the 5 Passages
3. WHEN a Passage is written, THE Chapter SHALL naturally incorporate its 4 assigned Vocab_Words in context within the prose
4. THE Chapter SHALL have a total reading length of approximately 750–1450 words across all 5 Passages (approximately 150–290 words per Passage)
5. THE Chapter SHALL have an English-only title following the format: "[Novel Title] — Chapter N: [Chapter Title]"
6. THE Chapter SHALL advance the science fiction plot meaningfully, introducing new developments, characters, or revelations

### Requirement 3: Vocabulary Selection

**User Story:** As a curriculum designer, I want each chapter's 20 vocabulary words to be familiar B2 words used as contextual refreshers, so that upper-intermediate learners reinforce known vocabulary through fiction.

#### Acceptance Criteria

1. THE Vocab_Word list for each Chapter SHALL contain exactly 20 English words at B2 (upper-intermediate) level
2. THE Vocab_Word list SHALL consist of words that are familiar to upper-intermediate learners, serving as refreshers rather than new introductions
3. THE Vocab_Word list for each Chapter SHALL avoid repeating words used in other Chapters of the same Novel
4. WHEN a Vocab_Word is selected, THE Vocab_Word SHALL be naturally usable within the science fiction narrative context
5. THE Vocab_Word SHALL appear as a simple string in the vocabList array (e.g., ["word1", "word2", "word3", "word4"]) — no translation field, no example sentence field
6. THE Vocab_Word list format SHALL match the Alder House flashcard data structure: a plain array of word strings in the vocabList field

### Requirement 4: Curriculum Structure per Chapter

**User Story:** As a curriculum designer, I want each chapter curriculum to have exactly 6 sessions with the correct activity types matching the Alder House template, so that the learning flow is consistent.

#### Acceptance Criteria

1. THE Curriculum SHALL contain exactly 6 Sessions
2. WHEN Sessions 1 through 5 are created, THE Session SHALL contain exactly 3 Activities in order: viewFlashcards, reading, readAlong
3. WHEN Session 6 is created, THE Session SHALL contain exactly 2 Activities in order: viewFlashcards, readAlong
4. WHEN a viewFlashcards Activity in Sessions 1–5 is created, THE viewFlashcards Activity data SHALL contain a vocabList of exactly 4 vocabulary word strings
5. WHEN the viewFlashcards Activity in Session 6 is created, THE viewFlashcards Activity data SHALL contain a vocabList of all 20 vocabulary word strings from the Chapter
6. WHEN a reading Activity is created, THE reading Activity data SHALL contain the Passage text for that Session's segment
7. WHEN a readAlong Activity in Sessions 1–5 is created, THE readAlong Activity data SHALL contain the same Passage text as the corresponding reading Activity
8. WHEN the readAlong Activity in Session 6 is created, THE readAlong Activity data SHALL contain the full Chapter text (all 5 Passages concatenated)
9. THE Curriculum SHALL set audioSpeed to -0.2 on all viewFlashcards, reading, and readAlong Activities


### Requirement 5: English-Only Content (en-en)

**User Story:** As a curriculum designer, I want all user-facing text written entirely in English with no bilingual content, so that the curriculum serves English-only learners at upper-intermediate level.

#### Acceptance Criteria

1. THE Curriculum title SHALL be in English only, following the format: "[Novel Title] — Chapter N: [Chapter Title]"
2. THE Curriculum preview SHALL be written in English (~150 words), describing the chapter content with vivid hooks, listing all 20 vocabulary words, and describing the learning journey
3. THE Curriculum description SHALL be a short English summary of the Chapter
4. WHEN a Session title is created for Sessions 1–5, THE Session title SHALL be "Session N" where N is the Session number (e.g., "Session 1", "Session 2")
5. WHEN a Session title is created for Session 6, THE Session title SHALL be "Review"
6. THE viewFlashcards Activity title SHALL follow the format "Flashcards: [topic]" with description "Learn 4 words: word1, word2, word3, word4" for Sessions 1–5, and "Learn 20 words: word1, word2, ..." for Session 6
7. THE reading Activity title SHALL follow the format "Read: [topic]" with description containing the first ~80 characters of the reading text
8. THE readAlong Activity title for Sessions 1–5 SHALL follow the format "Listen: [topic]" with description "Listen to the passage and follow along."
9. THE readAlong Activity title for Session 6 SHALL use "Listen: Full Chapter" with description "Listen to the full chapter and follow along."
10. THE Curriculum SHALL set language to "en" and userLanguage to "en"
11. THE Curriculum SHALL NOT contain any Vietnamese, Chinese, or other non-English text in any field

### Requirement 6: Content Module and Script Creation

**User Story:** As a curriculum designer, I want Python content modules and a single creation script for all 20 chapters, so that curriculums can be uploaded to the platform programmatically.

#### Acceptance Criteria

1. WHEN a Chapter is prepared for upload, THE Content_Module SHALL export a complete curriculum dict via a `get_curriculum()` function matching the platform's expected JSON structure
2. THE Content_Module SHALL NOT include any Strip_Keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId)
3. THE Creation_Script SHALL authenticate using firebase_token.get_firebase_id_token with UID zs5AMpVfqkcfDf8CJ9qrXdH58d73
4. THE Creation_Script SHALL call the curriculum/create API endpoint to upload each Chapter
5. WHEN all 20 Chapters are uploaded, THE Creation_Script SHALL create a new curriculum Series, add all 20 Curriculums to the Series with display_order 1–20, and attach the Series to an en-en fiction Collection
6. THE Creation_Script SHALL look up or create an en-en fiction Collection at runtime — the existing "Truyện (Fiction)" collection (ID: 97cee550) contains vi-en content and cannot be used due to language homogeneity rules
7. THE Creation_Script SHALL NOT hardcode any curriculum IDs, series IDs, or collection IDs — all IDs SHALL be looked up by title or obtained from API responses at runtime

### Requirement 7: Content Validation

**User Story:** As a curriculum designer, I want all content validated against correctness properties before upload, so that structural and content errors are caught early.

#### Acceptance Criteria

1. THE Validation_Script SHALL verify that each Chapter Curriculum contains exactly 6 Sessions
2. THE Validation_Script SHALL verify that Sessions 1–5 each contain exactly 3 Activities (viewFlashcards, reading, readAlong) in the correct order
3. THE Validation_Script SHALL verify that Session 6 contains exactly 2 Activities (viewFlashcards, readAlong) in the correct order
4. THE Validation_Script SHALL verify that each Session 1–5 viewFlashcards Activity data contains a vocabList of exactly 4 word strings
5. THE Validation_Script SHALL verify that the Session 6 viewFlashcards Activity data contains a vocabList of exactly 20 word strings
6. THE Validation_Script SHALL verify that the Session 6 readAlong text equals the concatenation of all 5 Passage texts
7. THE Validation_Script SHALL verify that each Passage contains its 4 assigned Vocab_Words (case-insensitive) in the text
8. THE Validation_Script SHALL verify that no Strip_Keys are present in the curriculum dict (recursively)
9. THE Validation_Script SHALL verify that all Activities have non-empty title and description fields
10. THE Validation_Script SHALL verify that all user-facing text (title, preview, description, session titles, activity titles, activity descriptions) is in English only — no Vietnamese or other non-English characters
11. THE Validation_Script SHALL verify that audioSpeed is set to -0.2 for all viewFlashcards, reading, and readAlong Activities
12. THE Validation_Script SHALL verify that no Vocab_Word is repeated across Chapters within the Novel
13. THE Validation_Script SHALL verify that language is "en" and userLanguage is "en" on each Curriculum
14. IF the Validation_Script detects a violation, THEN THE Validation_Script SHALL report the specific Chapter, Session, Activity, and nature of the violation

### Requirement 8: Series and Collection Organization

**User Story:** As a curriculum designer, I want the novel series properly organized in the platform's collection hierarchy with correct language homogeneity, so that learners can discover and navigate the novel.

#### Acceptance Criteria

1. THE Series SHALL be created with an English-only title (the novel title)
2. THE Series SHALL be added to an en-en fiction Collection — NOT the existing "Truyện (Fiction)" collection (ID: 97cee550) which contains vi-en content
3. WHEN no suitable en-en fiction Collection exists, THE Creation_Script SHALL create a new Collection with an English title (e.g., "Fiction") and add the Series to the new Collection
4. WHEN a suitable en-en fiction Collection already exists, THE Creation_Script SHALL look it up by title at runtime and add the Series to the existing Collection
5. THE Series SHALL contain all 20 Chapter Curriculums in display_order 1–20
6. THE Series SHALL have language "en" and userLanguage "en" consistent across all Curriculums
7. THE Series SHALL be set to public visibility after all Chapters are uploaded and validated
8. THE Series title SHALL NOT include any difficulty level descriptor

### Requirement 9: Source Material Management

**User Story:** As a curriculum designer, I want source materials managed according to workspace conventions, so that the workspace stays clean and content is recoverable.

#### Acceptance Criteria

1. WHEN all Chapters are successfully uploaded to the database, THE source files (Python content modules, creation script, validation script) SHALL be deleted from the workspace
2. THE Novel folder SHALL retain only a README.md file after successful upload
3. THE README.md SHALL document: how the content was created, the series ID, the collection it belongs to, SQL queries to find all Chapter Curriculums in the database, a novel summary, and enough context to recreate the source materials
4. THE README.md SHALL include a SQL query that retrieves all Chapter Curriculums by series ID with title and display_order

### Requirement 10: Reading Passage Quality

**User Story:** As a curriculum designer, I want reading passages that are engaging, level-appropriate for B2 readers, and serve the science fiction narrative, so that learners enjoy reading while reinforcing vocabulary.

#### Acceptance Criteria

1. THE Passage SHALL use clear, natural English prose at upper-intermediate (B2) level — varied sentence structures, subordinate clauses, and richer vocabulary than preintermediate, while remaining ~95% comprehensible without a dictionary
2. THE Passage SHALL advance the Chapter's plot segment meaningfully — each Passage moves the story forward
3. THE Passage SHALL incorporate its 4 assigned Vocab_Words naturally in context, not forced or artificial
4. THE Passage SHALL be approximately 150–290 words in length
5. THE Passage SHALL use vivid, descriptive language appropriate for science fiction — world-building details, sensory descriptions, and speculative elements
6. THE Passage SHALL avoid obscure jargon, heavy technical language, or cultural references that would break comprehension for B2 readers
7. WHEN dialogue is used in a Passage, THE Passage SHALL use natural conversational English appropriate for upper-intermediate level

### Requirement 11: Activity Data Structure

**User Story:** As a curriculum designer, I want the activity data structure to match the Alder House reference implementation exactly, so that the platform renders the content correctly.

#### Acceptance Criteria

1. THE viewFlashcards Activity SHALL have an activityType field set to "viewFlashcards" and a data object containing vocabList (array of word strings) and audioSpeed (-0.2)
2. THE reading Activity SHALL have an activityType field set to "reading" and a data object containing text (the passage string) and audioSpeed (-0.2)
3. THE readAlong Activity SHALL have an activityType field set to "readAlong" and a data object containing text (the passage string) and audioSpeed (-0.2)
4. THE Activity object SHALL contain activityType, title, description, practiceMinutes, and data fields
5. THE vocabList in viewFlashcards data SHALL be a simple array of word strings (e.g., ["elaborate", "threshold", "compelling", "ambiguous"]) — no translation objects, no example sentence objects

### Requirement 12: Novel Source Folder Naming

**User Story:** As a curriculum designer, I want the novel's source folder to have a descriptive name, so that it is easily distinguishable from other novel folders in the workspace.

#### Acceptance Criteria

1. THE Novel's source folder under `original-novels/` SHALL use a descriptive name based on the novel's English title (e.g., `the-signal-beyond` or similar), clearly distinguishable from existing folders
2. THE Novel's source folder name SHALL indicate the story identity, not the language pair or level
