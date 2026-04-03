# Requirements Document

## Introduction

All descriptions across curriculums, series, and collections on the platform currently follow a monotonous pattern — most start with "Did you know..." or similar template-like openers. The same monotony affects the farewell introAudio scripts (the last `introAudio` activity in each curriculum), which all follow the same formulaic sign-off pattern. While the persuasive copy style is the right quality bar, the lack of tonal variety makes the content feel repetitive and factory-produced when a learner browses multiple items or completes multiple curriculums. This feature rewrites every description across all three content levels (curriculums, series, collections) AND every farewell introAudio script to maintain the persuasive engagement standard but with varied tones, hooks, and rhetorical approaches so no two items feel like they came from the same template.

## Glossary

- **Curriculum_Description**: The `description` field inside a curriculum's JSON content blob, stored in the `curriculum.content` jsonb column. No varchar limit.
- **Series_Description**: The `description` column on the `curriculum_series` table. varchar(255) max.
- **Collection_Description**: The `description` column on the `curriculum_collections` table. text type, no limit.
- **Update_Script**: A standalone Python script that queries the database for current IDs and descriptions, then calls the appropriate API endpoint to update descriptions.
- **Tone_Palette**: The set of varied rhetorical approaches used across descriptions — e.g., provocative question, bold declaration, vivid scenario, empathetic observation, surprising statistic, metaphor-led, challenge/dare, story hook.
- **Persuasive_Copy_Style**: The existing quality standard requiring emotional sales copy with a bold headline, concrete examples, vivid metaphor, and transformation promise.
- **MCP_Postgres**: The MCP-based PostgreSQL query tool used to query the database in real-time for current IDs, titles, and descriptions.
- **Generated_Keys**: Auto-generated keys (`mp3Url`, `illustrationSet`, `chapterBookmarks`, `segments`, `whiteboardItems`, `userReadingId`, `lessonUniqueId`, `curriculumTags`, `taskId`, `imageId`) that must be preserved when updating existing curriculums.
- **Farewell_IntroAudio**: The last `introAudio` activity in a curriculum's final session — typically a review of vocabulary and a warm sign-off. The `text` field inside this activity is the farewell script that needs rewriting. The `mp3Url` on this activity must be stripped so audio is regenerated from the new text.

## Requirements

### Requirement 1: Inventory All Descriptions

**User Story:** As a content manager, I want to query all current descriptions across curriculums, series, and collections, so that I know the full scope of what needs rewriting.

#### Acceptance Criteria

1. WHEN the Update_Script for any content level is executed, THE Update_Script SHALL query MCP_Postgres in real-time to retrieve current IDs, titles, and descriptions — no hardcoded IDs
2. THE Update_Script SHALL query `curriculum_series` for all series IDs, titles, and current descriptions
3. THE Update_Script SHALL query `curriculum_collections` for all collection IDs, titles, and current descriptions
4. THE Update_Script SHALL query `curriculum` for all curriculum IDs, titles, and the `description` field extracted from the `content` jsonb column

### Requirement 2: Rewrite Curriculum Descriptions

**User Story:** As a content manager, I want all curriculum descriptions rewritten with varied tones, so that learners browsing multiple curriculums encounter fresh, engaging copy each time.

#### Acceptance Criteria

1. WHEN the Update_Script rewrites a curriculum description, THE Update_Script SHALL follow the Persuasive_Copy_Style standard (bold headline, concrete examples, vivid metaphor, transformation promise)
2. WHEN the Update_Script rewrites curriculum descriptions, THE Update_Script SHALL vary the opening hook across the Tone_Palette — no two curriculums in the same series or collection SHALL use the same rhetorical opener type
3. WHEN the Update_Script updates a curriculum via `curriculum/update`, THE Update_Script SHALL modify only the `description` field inside the content JSON and preserve all other keys including Generated_Keys
4. WHEN the Update_Script updates a curriculum, THE Update_Script SHALL send the full content JSON with only the `description` field changed — the Update_Script SHALL fetch the current content via `curriculum/getOne`, replace the description, and push the entire content back
5. THE Update_Script SHALL authenticate using `firebase_token.get_firebase_id_token` with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`
6. THE Update_Script SHALL craft each description individually — no template functions, string interpolation, or fill-in-the-blank generation

### Requirement 3: Rewrite Series Descriptions

**User Story:** As a content manager, I want all series descriptions rewritten with varied tones, so that the series listing page feels dynamic rather than repetitive.

#### Acceptance Criteria

1. WHEN the Update_Script rewrites a series description, THE Update_Script SHALL follow the Persuasive_Copy_Style standard adapted for the 255-character varchar limit — concise but emotionally compelling
2. WHEN the Update_Script rewrites series descriptions, THE Update_Script SHALL vary the tone across the Tone_Palette so that adjacent series in the same collection use different rhetorical approaches
3. WHEN the Update_Script updates a series via `curriculum-series/update`, THE Update_Script SHALL send `id` and `description` in the request body along with `firebaseIdToken`
4. THE Update_Script SHALL ensure every rewritten series description is 255 characters or fewer
5. THE Update_Script SHALL authenticate using `firebase_token.get_firebase_id_token` with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`
6. THE Update_Script SHALL craft each series description individually — no templated generation

### Requirement 4: Rewrite Collection Descriptions

**User Story:** As a content manager, I want all collection descriptions rewritten with varied tones, so that the top-level browse experience feels curated and engaging.

#### Acceptance Criteria

1. WHEN the Update_Script rewrites a collection description, THE Update_Script SHALL follow the Persuasive_Copy_Style standard with full multi-paragraph structure (bold headline, concrete examples, vivid metaphor, transformation promise)
2. WHEN the Update_Script rewrites collection descriptions, THE Update_Script SHALL vary the tone across the Tone_Palette so that no two collections use the same rhetorical opener type
3. WHEN the Update_Script updates a collection via `curriculum-collection/update`, THE Update_Script SHALL send `id` and `description` in the request body along with `firebaseIdToken`
4. THE Update_Script SHALL authenticate using `firebase_token.get_firebase_id_token` with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`
5. THE Update_Script SHALL craft each collection description individually — no templated generation

### Requirement 5: Tone Variety Distribution

**User Story:** As a content manager, I want descriptions to use a diverse range of rhetorical approaches, so that the overall browsing experience feels hand-crafted rather than algorithmically generated.

#### Acceptance Criteria

1. THE Update_Script SHALL draw from at least 6 distinct opener types from the Tone_Palette: provocative question, bold declaration, vivid scenario, empathetic observation, surprising fact, and metaphor-led hook
2. WHEN descriptions are written for items within the same series or collection, THE Update_Script SHALL ensure no two adjacent items share the same opener type
3. WHEN descriptions are written across all collections, THE Update_Script SHALL distribute opener types so that no single type accounts for more than 30% of all descriptions at any content level (curriculum, series, collection)
4. THE Update_Script SHALL maintain the language appropriate to each item — Vietnamese for vi-* language pairs at beginner through intermediate levels, English for en-* pairs and advanced-level content, bilingual where the existing content is bilingual

### Requirement 6: Preserve Content Integrity

**User Story:** As a content manager, I want the rewrite process to change only descriptions and nothing else, so that no curriculum content, series metadata, or collection structure is accidentally modified.

#### Acceptance Criteria

1. WHEN the Update_Script updates a curriculum, THE Update_Script SHALL preserve all Generated_Keys, vocabulary lists, reading passages, activity structures, introAudio scripts, writing prompts, and every other field in the content JSON
2. WHEN the Update_Script updates a series, THE Update_Script SHALL send only `id`, `description`, and `firebaseIdToken` — the Update_Script SHALL NOT send `title` or `thumbnail` fields
3. WHEN the Update_Script updates a collection, THE Update_Script SHALL send only `id`, `description`, and `firebaseIdToken` — the Update_Script SHALL NOT send `title` or `thumbnail` fields
4. IF an API call fails during the update process, THEN THE Update_Script SHALL log the error with the item ID and title, skip the failed item, and continue processing remaining items
5. THE Update_Script SHALL log each successful update with the item ID, title, and a snippet of the new description for verification

### Requirement 7: Script Organization

**User Story:** As a content manager, I want the update scripts organized so they can be run independently per content level, so that I can review and approve changes incrementally.

#### Acceptance Criteria

1. THE Update_Script set SHALL consist of separate scripts: one for collections, one for series, and one per series for curriculum descriptions (following the one-script-per-curriculum rule adapted to one-script-per-series-of-curriculums)
2. WHEN a script is executed, THE script SHALL print a summary showing how many items were updated, how many failed, and the total count queried
3. WHEN all descriptions are verified as updated in the database, THE operator SHALL delete all Update_Scripts, leaving only a README documenting what was changed, SQL queries to verify the descriptions, and instructions to re-run if needed

### Requirement 8: Rewrite Farewell IntroAudio Scripts

**User Story:** As a content manager, I want all farewell introAudio scripts rewritten with varied tones, so that learners completing multiple curriculums don't hear the same formulaic sign-off every time.

#### Acceptance Criteria

1. WHEN the Update_Script rewrites a Farewell_IntroAudio, THE Update_Script SHALL identify the last `introAudio` activity in the last session of each curriculum
2. WHEN the Update_Script rewrites a Farewell_IntroAudio, THE Update_Script SHALL rewrite the `text` field with a fresh, individually crafted farewell that reviews vocabulary and provides a warm sign-off — following the quality standard for introAudio Session 4 farewell (~400-600 words)
3. WHEN the Update_Script rewrites farewell scripts, THE Update_Script SHALL vary the tone across the Tone_Palette — no two curriculums in the same series SHALL use the same farewell rhetorical approach
4. WHEN the Update_Script updates a farewell introAudio, THE Update_Script SHALL strip the `mp3Url` from that specific activity so audio is regenerated from the new text
5. WHEN the Update_Script updates a farewell introAudio, THE Update_Script SHALL preserve all other keys on the activity (title, description, practiceMinutes, etc.) and all other activities and fields in the curriculum content JSON
6. THE Update_Script SHALL authenticate using `firebase_token.get_firebase_id_token` with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`
7. THE Update_Script SHALL craft each farewell script individually — no template functions, string interpolation, or fill-in-the-blank generation
