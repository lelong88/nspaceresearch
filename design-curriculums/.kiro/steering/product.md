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

Two-level hierarchy: Collections → Series → Curriculums. Query current state from DB in real-time (MCP postgres or API). After adding a curriculum to a series, always call `curriculum/setDisplayOrder`. Do not leave `displayOrder` unset.

### Minimal Curriculum Titles
Titles must be as short as possible — the series/collection provides context. Never repeat series/collection name, content type prefix, skill-focus label, or audience suffix in the curriculum title.

## Document Every Curriculum Creation

After creating any curriculum: (1) create README.md with curriculum ID, collection/series membership, creation method, SQL queries, recreation context; (2) delete all temporary files (scripts, JSON, intermediate data).

## No Ephemeral Code

No hardcoded IDs or static ID-to-name mappings. Query MCP postgres in real-time. Delete one-time scripts after execution. Source materials deleted after import — only README remains.

## Language Rules

- Always use 2-character ISO 639-1 codes (`en`, `vi`, `zh`, etc.). Pairs: `{user_language}-{target_language}`.
- Beginner/Preintermediate/Intermediate: bilingual text. Upper-intermediate: bilingual or single-language. Advanced: single-language only.
- Each series/collection must have homogeneous `language` and `user_language`. Check via `curriculum_series_language_list` and `curriculum_collections_language_list` views.
- No mixing bilingual and single-language content in the same series/collection.
- Max 1 level gap within a series/collection. Check via `curriculum_series_level_gap` and `curriculum_collections_level_gap` views.
- No difficulty level in titles (level is metadata, not title content).

## Duplicate Check After Creation

Always check for duplicates after creating curriculums:
```sql
SELECT id, title, created_at FROM curriculum
WHERE title = '<title>' AND uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73' ORDER BY created_at;
```
Keep earliest, delete extras. Remove duplicate series entries before deleting curriculum.

## Detailed Rules (in repo root — read when relevant to the task)

- `CURRICULUM_CREATION_RULES.md` — activity schema requirements, DB column limits, story-oriented rules. Read when creating new curriculums.
- `CURRICULUM_QUALITY_STANDARDS.md` — persuasive copy style, introAudio scripts, writing prompts. Read when writing learner-facing content.
- `CURRICULUM_UPDATE_RULES.md` — what to preserve, what to strip when rewriting. Read when editing existing curriculums.
