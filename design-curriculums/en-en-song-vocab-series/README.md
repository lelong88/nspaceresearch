# en-en Song Vocab Series

## Collection: Learn Vocabulary Through Music

- **Collection ID**: `v110f265`
- **Language**: en-en (English speakers learning English)

## Curriculums

| # | Song | Curriculum ID | vi-en Source ID |
|---|---|---|---|
| 0 | Heal the World — Michael Jackson | `1pCFaeWBC3q0HCxf` | `qVv18hr5L4sTQs6i` |
| 1 | Imagine — John Lennon | `OF2KsbbWNR9ztUVB` | `jHM7Pekp6LtLjqok` |
| 2 | Lean on Me — Bill Withers | `K7rNg7e9vyW7xLeD` | `4Ho0bZURRPz2TiJA` |
| 3 | What a Wonderful World — Louis Armstrong | `SOzUrZZCAbwfpDFy` | `5WdGkIlyRDO4dzsL` |

## How Content Was Created

Each curriculum was created by a mirror script (`create_song_N_<song>.py`) that:
1. Fetched the corresponding vi-en source curriculum via `curriculum/getOne`
2. Ran `strip_keys()` to remove auto-generated keys
3. Transformed all Vietnamese user-facing text to hand-written English (titles, descriptions, previews, introAudio scripts, writing prompts, activity titles/descriptions, session titles, vocabulary definitions)
4. Validated structural properties (18 unique words, correct activity sequences, no strip keys, youtubeUrl present, contentTypeTags=["music"]) before upload
5. Called `curriculum/create` API with `language="en"`, `userLanguage="en"`
6. All curriculums created as private (`is_public = false`)

The same 4 songs and youtubeUrls are shared with the vi-en song series. Each en-en curriculum mirrors its vi-en counterpart with English UI text instead of Vietnamese.

An orchestrator script (`create_en_en_song_collection.py`) created the collection and added all 4 curriculums directly to it (no series intermediary), then set display orders 0–3.

All scripts were deleted after successful creation and verification.

## SQL Queries

```sql
-- Find the collection
SELECT id, title, description, is_public
FROM curriculum_collections
WHERE id = 'v110f265';

-- Find curriculums in collection
SELECT c.id, c.content->>'title' as title, c.display_order,
       c.content->>'youtubeUrl' as youtube_url, c.is_public
FROM curriculum c
JOIN curriculum_collection_items cci ON cci.curriculum_id = c.id
WHERE cci.curriculum_collection_id = 'v110f265'
ORDER BY c.display_order;

-- Get full content for any curriculum
SELECT content FROM curriculum WHERE id = '1pCFaeWBC3q0HCxf';
```

## Recreation

To recreate, write new mirror scripts following the same pattern. Each script needs:
- Fetch vi-en source via `curriculum/getOne` with the source ID
- `strip_keys()` to remove auto-generated keys
- Hand-written English translations of all Vietnamese user-facing text
- 18 vocabulary words, 5 sessions (12, 12, 12, 4, 5 activities)
- Inline `validate()` and `strip_keys()` functions
- `language="en"`, `userLanguage="en"` as top-level API params
- `contentTypeTags=["music"]` and `youtubeUrl` at top level of content JSON
- `is_public = false`

Content is fully recoverable via `curriculum/getOne` with each curriculum ID.
