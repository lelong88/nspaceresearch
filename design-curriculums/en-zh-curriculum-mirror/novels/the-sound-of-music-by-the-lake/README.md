# En-Zh Novel: The Sound of Music by the Lake (湖边的琴声)

Collection: **Fiction (小说)** (`<COLLECTION_ID>`) — shared across all 3 novels
Series: **The Sound of Music by the Lake (湖边的琴声)** (`<SERIES_ID>`)
Language pair: en-zh | 10 chapters | Level: pre-intermediate (HSK2-HSK3)

## Curriculums in series

| Ch | En-Zh ID | Title | Vi-Zh Source ID | Chinese Chapter Title |
|---|---|---|---|---|
| 1 | `<TBD>` | The Sound of Music by the Lake (湖边的琴声) — Chapter 1: The Lakeside Town (湖边的小镇) | `oBbLBgdhhB92sw1W` | 湖边的小镇 |
| 2 | `<TBD>` | The Sound of Music by the Lake (湖边的琴声) — Chapter 2: The Little Tea House (小茶馆) | `0gDfBmaaILFsybhn` | 小茶馆 |
| 3 | `<TBD>` | The Sound of Music by the Lake (湖边的琴声) — Chapter 3: The Boy by the Lake (湖边的男孩) | `BnexmG0Eew9ly0Q5` | 湖边的男孩 |
| 4 | `<TBD>` | The Sound of Music by the Lake (湖边的琴声) — Chapter 4: Learning the Instrument (学琴) | `PIkkeQwiHyZTLdW8` | 学琴 |
| 5 | `<TBD>` | The Sound of Music by the Lake (湖边的琴声) — Chapter 5: The Summer Festival (夏天的节日) | `uDnmKGnd1rBxtC0R` | 夏天的节日 |
| 6 | `<TBD>` | The Sound of Music by the Lake (湖边的琴声) — Chapter 6: Xiaojie's Secret (小杰的秘密) | `NuTdMMGAJMUEWaTu` | 小杰的秘密 |
| 7 | `<TBD>` | The Sound of Music by the Lake (湖边的琴声) — Chapter 7: Grandfather (爷爷) | `WH6TuntirAt9amdj` | 爷爷 |
| 8 | `<TBD>` | The Sound of Music by the Lake (湖边的琴声) — Chapter 8: A Rainy Day (下雨天) | `6Mlkss6aQIoPWw2S` | 下雨天 |
| 9 | `<TBD>` | The Sound of Music by the Lake (湖边的琴声) — Chapter 9: The Farewell Performance (告别演出) | `SkKxWR6p5klRiWFR` | 告别演出 |
| 10 | `<TBD>` | The Sound of Music by the Lake (湖边的琴声) — Chapter 10: The Sound of Music by the Lake (湖边的琴声) | `32kDXxWAmeH6qwSZ` | 湖边的琴声 |

## Vi-Zh Source

- Collection: `7nf5wi1d` — "Truyện (小说)"
- Series: `z6xddztr` — "Tiếng Đàn Bên Hồ (湖边的琴声)"
- Display orders: 1–10

## How content was created

Each en-zh chapter curriculum was derived from its vi-zh source via a standalone Python script:

1. **Fetch** the vi-zh source curriculum via `curriculum/getOne`
2. **Strip** auto-generated keys (`mp3Url`, `illustrationSet`, `chapterBookmarks`, `segments`, `whiteboardItems`, `userReadingId`, `lessonUniqueId`, `curriculumTags`, `taskId`, `imageId`) using `strip_keys()`
3. **Transform** all Vietnamese user-facing text to hand-written English — titles, descriptions (with narrative hooks/cliffhangers), previews, introAudio scripts, writing prompts, activity titles/descriptions, session titles, vocabulary definitions
4. **Upload** via `curriculum/create` with `language="zh"`, `userLanguage="en"`

The orchestrator script (`create_en_zh_lake_series.py`) created the Sound of Music by the Lake series, wired it to the existing en-zh Fiction collection (created by the Memories of Flavor orchestrator), added all 10 chapter curriculums to the series, and set display orders 1–10. Series display order: 0 (matching vi-zh source).

The Fiction collection (`<COLLECTION_ID>`) is shared across all 3 novel series:
- Memories of Flavor (味道的记忆)
- The Vanishing Painting (消失的画)
- The Sound of Music by the Lake (湖边的琴声)

Structure per chapter curriculum:
- Vocabulary drawn from the chapter text, HSK2-HSK3 level
- Multiple sessions: learning sessions + review + full chapter reading with farewell
- Original Chinese fiction text used as reading passages
- introAudio scripts include pinyin when teaching vocabulary
- Writing prompts include pinyin in parentheses and Chinese example sentences
- `language="zh"`, `userLanguage="en"` as top-level API params
- All curriculums are private (`is_public = false`)

All creation scripts were deleted after successful creation and verification. Content is fully recoverable via `curriculum/getOne` with each curriculum ID.

## SQL queries

```sql
-- Find en-zh Fiction collection (shared across all 3 novels)
SELECT * FROM curriculum_collections WHERE id = '<COLLECTION_ID>';

-- Find en-zh series in Fiction collection
SELECT cs.*
FROM curriculum_series cs
JOIN curriculum_collection_series ccs ON ccs.curriculum_series_id = cs.id
WHERE ccs.curriculum_collection_id = '<COLLECTION_ID>';

-- Find en-zh Sound of Music by the Lake chapters
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
WHERE csi.curriculum_series_id = 'z6xddztr'
ORDER BY c.display_order;
```
