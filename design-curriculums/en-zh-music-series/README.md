# en-zh Music Series

## Collection: Learn Chinese Vocabulary Through Music (通过音乐学中文词汇)

- **Collection ID**: `l9r2lg0q`
- **Language**: en-zh (English speakers learning Chinese)

## Curriculums

| # | Curriculum ID | Notes |
|---|---|---|
| 0 | `HLLOA8bahIraa6rR` | Existing curriculum, organized into collection |
| 1 | `MX6Yw2Qrkiry1ylN` | Existing curriculum, organized into collection |
| 2 | `CbYWQ16GXWxNiol4` | Existing curriculum, organized into collection |
| 3 | `9jRr2DrofNwyQZ1Z` | Existing curriculum, organized into collection |

## How Content Was Created

These 4 en-zh music curriculums already existed in the database. They were created previously as standalone curriculums. The only work done here was organizational: an orchestrator script (`create_en_zh_music_collection.py`) created the collection and added all 4 curriculums directly to it (no series intermediary), then set display orders 0–3.

The orchestrator script was deleted after successful creation and verification.

## SQL Queries

```sql
-- Find the collection
SELECT id, title, description, is_public
FROM curriculum_collections
WHERE id = 'l9r2lg0q';

-- Find curriculums in collection
SELECT c.id, c.content->>'title' as title, c.display_order,
       c.language, c.user_language, c.is_public
FROM curriculum c
JOIN curriculum_collection_items cci ON cci.curriculum_id = c.id
WHERE cci.curriculum_collection_id = 'l9r2lg0q'
ORDER BY c.display_order;

-- Get full content for any curriculum
SELECT content FROM curriculum WHERE id = 'HLLOA8bahIraa6rR';
```

## Recreation

To recreate the collection organization:
1. Create a new collection via `curriculum-collection/create` with title "Learn Chinese Vocabulary Through Music (通过音乐学中文词汇)"
2. Add each curriculum via `curriculum-collection/addCurriculum` with the collection ID and each curriculum ID
3. Set display orders 0–3 via `curriculum/setDisplayOrder`

The 4 curriculums themselves are pre-existing and do not need recreation.
