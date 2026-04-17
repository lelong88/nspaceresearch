# Product Overview

This is a content management and creation toolkit for a language-learning platform (helloapi.step.is). The platform teaches vocabulary across many language pairs through structured multi-session curriculums that combine reading, listening, speaking, and writing activities.

Use `firebase_token.py` to generate `firebaseIdToken` for API calls. See `server` (symlink to helloapi server code) for endpoint details.

## Content Model

A curriculum has: title, preview text, description, and one or more learning sessions with ordered activities. Activity types: `introAudio`, `viewFlashcards`, `speakFlashcards`, `vocabLevel1`, `vocabLevel2`, `reading`, `speakReading`, `readAlong`, `writingSentence`, `writingParagraph`.

### contentTypeTags
Top-level curriculum content JSON must include `"contentTypeTags"`: `["movie"]`, `["music"]`, `["podcast"]`, `["story"]`, or `[]` (empty). Always include the field — never omit it.

## Strip-Keys Rule

Auto-generated keys (`mp3Url`, `illustrationSet`, `chapterBookmarks`, `segments`, `whiteboardItems`, `userReadingId`, `lessonUniqueId`, `curriculumTags`, `taskId`, `imageId` — defined in `strip-keys.json`):
- New curriculums: NEVER include these keys
- Using existing curriculum as template: ALWAYS strip before using as input for `curriculum/create`
- Updating existing curriculum: PRESERVE all generated keys — only modify targeted fields

## Newly Created Curriculums Must Be Private

Do not call `curriculum/setPublic` with `isPublic: true` on newly created curriculums. They need content generation first.

## Collections & Series Organization

Two-level hierarchy: Collections → Series → Curriculums. Query current state from DB in real-time (MCP postgres or API).

## Deleted Curriculums

Ignore any curriculum whose `uid` ends with `_deleted`. These are soft-deleted records and should be excluded from queries, listings, and any processing.

## No Ephemeral Code

No hardcoded IDs or static ID-to-name mappings. Query MCP postgres in real-time. Delete one-time scripts after execution. Source materials deleted after import — only README remains.

## Language Rules

- Always use 2-character ISO 639-1 codes (`en`, `vi`, `zh`, etc.). Pairs: `{user_language}-{target_language}`.
- Beginner/Preintermediate/Intermediate: bilingual text. Upper-intermediate: bilingual or single-language. Advanced: single-language only.
- **Preview text language**: `preview.text` must match the bilingual rules above. For non-advanced curriculums, preview text must be written primarily in the user's language (e.g., Vietnamese for vi-en). Only advanced-level curriculums may have English-only preview text. This applies to all user-facing text fields: `title`, `description`, `preview.text`.
- Each series/collection must have homogeneous `language` and `user_language`. Check via `curriculum_series_language_list` and `curriculum_collections_language_list` views.
- No mixing bilingual and single-language content in the same series/collection.
- Max 1 level gap within a series/collection. Check via `curriculum_series_level_gap` and `curriculum_collections_level_gap` views.
- No difficulty level in titles (level is metadata, not title content).

## Description Tone Variety

All descriptions (series, collection, curriculum) must use varied rhetorical approaches. Six tones: `provocative_question`, `bold_declaration`, `vivid_scenario`, `empathetic_observation`, `surprising_fact`, `metaphor_led`. Rules:
- Adjacent items in the same parent must use different tones
- No single tone may exceed 30% of a batch
- Series descriptions: ≤ 255 chars, short persuasive hooks using the 6-tone palette
- Collection descriptions: short category summaries (not persuasive copy), varied angle but not palette-bound
- Curriculum descriptions: full multi-paragraph persuasive copy with tone-assigned ALL-CAPS headline opener
- Farewell introAudio scripts: vary emotional register (introspective, warm accountability, team energy, quiet awe, practical momentum); each reviews 5-6 vocab words with definitions and fresh examples

Full rules in `CURRICULUM_QUALITY_STANDARDS.md` under "Description Tone Variety."

## Detailed Rules (in repo root — read when relevant to the task)

- `CURRICULUM_CREATION_RULES.md` — activity schema requirements, DB column limits, story-oriented rules. Read when creating new curriculums.
- `CURRICULUM_QUALITY_STANDARDS.md` — persuasive copy style, description tone variety, introAudio scripts, writing prompts, farewell quality. Read when writing learner-facing content.
- `CURRICULUM_UPDATE_RULES.md` — what to preserve, what to strip when rewriting. Read when editing existing curriculums.

## Check for curriulum corruptions
- Always verify against the content-corruption.md rules after creating / editing curriculums