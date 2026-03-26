# En-Zh Travel: Explore China (探索中国)

Collection: **Thematic Vocabulary (主题词汇)** (`<COLLECTION_ID>`)
Series: **Explore China (探索中国)** (`<SERIES_ID>`)
Language pair: en-zh | 4 curriculums | Level: pre-intermediate to intermediate (HSK2-HSK3)

## Curriculums in series

| # | En-Zh ID | Title | Vi-Zh Source ID | City |
|---|---|---|---|---|
| 0 | `<TBD>` | 丽江 — The Ancient Town of Eternal Snow (雪山下的古城) | `x5u34HwpUIvrxOmK` | 丽江 (Lijiang) |
| 1 | `<TBD>` | 桂林 — Where Mountains and Rivers Are Finest Under Heaven (桂林山水甲天下) | `yHoyB8QAHuoPQTHD` | 桂林 (Guilin) |
| 2 | `<TBD>` | 成都 — The Leisurely Capital of the West (悠闲的西部之都) | `Cmb9OPN9alWErMVv` | 成都 (Chengdu) |
| 3 | `<TBD>` | 西安 — Where History Comes Alive (历史在这里活着) | `slq4m8qrLtfCsfvM` | 西安 (Xi'an) |

## Vi-Zh Source

- Collection: `q9j66zxj` — "Học Từ Vựng Theo Chủ Đề (主题词汇)"
- Series: `yjwuyhtk` — "Khám Phá Trung Quốc (探索中国)"
- Display orders: 0, 1, 2, 3

## How content was created

Each en-zh curriculum was derived from its vi-zh source via a standalone Python script:

1. **Fetch** the vi-zh source curriculum via `curriculum/getOne`
2. **Strip** auto-generated keys (`mp3Url`, `illustrationSet`, `chapterBookmarks`, `segments`, `whiteboardItems`, `userReadingId`, `lessonUniqueId`, `curriculumTags`, `taskId`, `imageId`) using `strip_keys()`
3. **Transform** all Vietnamese user-facing text to hand-written English — titles, descriptions (with travel writing hooks and cultural context), previews, introAudio scripts, writing prompts, activity titles/descriptions, session titles, vocabulary definitions
4. **Upload** via `curriculum/create` with `language="zh"`, `userLanguage="en"`

The orchestrator script (`create_en_zh_travel_series.py`) created the en-zh Thematic Vocabulary collection and the Explore China series, wired them together, added all 4 curriculums to the series, and set display orders (0, 1, 2, 3). Series display order: 0 (matching vi-zh source).

Structure per curriculum:
- 18 vocabulary words drawn from travel and cultural context, HSK2-HSK3 level
- 5 sessions: 3 learning + 1 review + 1 full reading with farewell
- Travel-themed reading passages in simplified Chinese
- introAudio scripts include pinyin when teaching vocabulary
- Writing prompts include pinyin in parentheses and Chinese example sentences
- `language="zh"`, `userLanguage="en"` as top-level API params
- All curriculums are private (`is_public = false`)

All creation scripts were deleted after successful creation and verification. Content is fully recoverable via `curriculum/getOne` with each curriculum ID.

## SQL queries

```sql
-- Find en-zh Thematic Vocabulary collection
SELECT * FROM curriculum_collections WHERE id = '<COLLECTION_ID>';

-- Find en-zh series in collection
SELECT cs.*
FROM curriculum_series cs
JOIN curriculum_collection_series ccs ON ccs.curriculum_series_id = cs.id
WHERE ccs.curriculum_collection_id = '<COLLECTION_ID>';

-- Find en-zh travel curriculums
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
WHERE csi.curriculum_series_id = 'yjwuyhtk'
ORDER BY c.display_order;
```
