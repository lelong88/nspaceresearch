# En-Zh Wisdom in Chinese Characters (汉字中的智慧)

Collection: **Elementary 2 (初级二)** (`<COLLECTION_ID>`) — shared with Textbook series
Series: **Wisdom in Chinese Characters (汉字中的智慧)** (`<SERIES_ID>`)
Language pair: en-zh | 4 curriculums | Level: elementary (HSK2-HSK3)

## Curriculums in series

| # | En-Zh ID | Title | Vi-Zh Source ID | Chinese Theme |
|---|---|---|---|---|
| 0 | `<TBD>` | Heart Characters — Characters of the Heart (心字篇) | `QOvwYvTVMi6OkkWp` | 心字篇 |
| 1 | `<TBD>` | Human Characters — Characters of Humanity (人字篇) | `cPjQO2MkPgWdMvlv` | 人字篇 |
| 2 | `<TBD>` | Home Characters — Characters of Home (家字篇) | `tepW8yNMEOWiKnkC` | 家字篇 |
| 3 | `<TBD>` | Action Characters — Characters of Strength (力字篇) | `DSsoTpLVsaE4ktmJ` | 力字篇 |

## Vi-Zh Source

- Collection: `64fb68f8` — "Sơ Cấp 2 (初级二)"
- Series: `vxvh04b5` — "Triết Lý Trong Chữ Hán (汉字中的智慧)"
- Display orders: 0, 1, 2, 3
- Series display order: 1

## How content was created

Each en-zh curriculum was derived from its vi-zh source via a standalone Python script:

1. **Fetch** the vi-zh source curriculum via `curriculum/getOne`
2. **Strip** auto-generated keys (`mp3Url`, `illustrationSet`, `chapterBookmarks`, `segments`, `whiteboardItems`, `userReadingId`, `lessonUniqueId`, `curriculumTags`, `taskId`, `imageId`) using `strip_keys()`
3. **Transform** all Vietnamese user-facing text to hand-written English — titles, descriptions, previews, introAudio scripts (explaining Chinese character etymology and philosophy), writing prompts, activity titles/descriptions, session titles, vocabulary definitions
4. **Upload** via `curriculum/create` with `language="zh"`, `userLanguage="en"`

The orchestrator script (`create_en_zh_wisdom_series.py`) created the Wisdom in Chinese Characters series, wired it to the existing en-zh Elementary 2 collection (created by the textbook orchestrator), added all 4 curriculums to the series, and set display orders 0, 1, 2, 3. Series display order: 1 (matching vi-zh source).

The Elementary 2 collection (`<COLLECTION_ID>`) is shared with the Standard Chinese — Elementary 2 textbook series.

Structure per curriculum:
- Vocabulary drawn from Chinese character radicals and etymology, HSK2-HSK3 level
- Each lesson explores a radical — heart (心), human (人), home (家), strength (力)
- Multiple sessions: learning sessions + review + full reading with farewell
- introAudio scripts include pinyin when teaching vocabulary and explain character philosophy
- Writing prompts include pinyin in parentheses and Chinese example sentences
- `language="zh"`, `userLanguage="en"` as top-level API params
- All curriculums are private (`is_public = false`)

All creation scripts were deleted after successful creation and verification. Content is fully recoverable via `curriculum/getOne` with each curriculum ID.

## SQL queries

```sql
-- Find en-zh Elementary 2 collection (shared with textbook series)
SELECT * FROM curriculum_collections WHERE id = '<COLLECTION_ID>';

-- Find en-zh series in Elementary 2 collection
SELECT cs.*
FROM curriculum_series cs
JOIN curriculum_collection_series ccs ON ccs.curriculum_series_id = cs.id
WHERE ccs.curriculum_collection_id = '<COLLECTION_ID>';

-- Find en-zh wisdom curriculums
SELECT c.id, c.content->>'title' as title, c.display_order
FROM curriculum c
JOIN curriculum_series_items csi ON csi.curriculum_id = c.id
WHERE csi.curriculum_series_id = '<SERIES_ID>'
ORDER BY c.display_order;

-- Check language homogeneity
SELECT * FROM curriculum_series_language_list WHERE id = '<SERIES_ID>';

-- Compare with vi-zh source series
SELECT c.id, c.content->>'title' as title, c.display_order, c.language, c.user_language
FROM curriculum c
JOIN curriculum_series_items csi ON csi.curriculum_id = c.id
WHERE csi.curriculum_series_id = 'vxvh04b5'
ORDER BY c.display_order;
```
