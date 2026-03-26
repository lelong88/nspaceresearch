# En-Zh Novel: Memories of Flavor (味道的记忆)

Collection: **Fiction (小说)** (`<COLLECTION_ID>`) — shared across all 3 novels
Series: **Memories of Flavor (味道的记忆)** (`<SERIES_ID>`)
Language pair: en-zh | 10 chapters | Level: pre-intermediate (HSK2-HSK3)

## Curriculums in series

| Ch | En-Zh ID | Title | Vi-Zh Source ID | Chinese Chapter Title |
|---|---|---|---|---|
| 1 | `<TBD>` | Memories of Flavor (味道的记忆) — Chapter 1: Arrived in Kunming (到昆明了) | `j8uZc8utufTIOeya` | 到昆明了 |
| 2 | `<TBD>` | Memories of Flavor (味道的记忆) — Chapter 2: First Day of Class (第一天上课) | `GueXhwE9pHcN9Mtv` | 第一天上课 |
| 3 | `<TBD>` | Memories of Flavor (味道的记忆) — Chapter 3: The Vegetable Market (菜市场) | `ZEYjyl0k3az6LpST` | 菜市场 |
| 4 | `<TBD>` | Memories of Flavor (味道的记忆) — Chapter 4: Daming's Noodle Shop (大明的面馆) | `rn072heXsgS0WcoN` | 大明的面馆 |
| 5 | `<TBD>` | Memories of Flavor (味道的记忆) — Chapter 5: Homesick (想家) | `XMzuS1c9lEgmdHoY` | 想家 |
| 6 | `<TBD>` | Memories of Flavor (味道的记忆) — Chapter 6: An Idea (一个主意) | `CsQtnqpS8u8ngrDg` | 一个主意 |
| 7 | `<TBD>` | Memories of Flavor (味道的记忆) — Chapter 7: Failed (失败了) | `zVEZ7DVm4nZ1JBgT` | 失败了 |
| 8 | `<TBD>` | Memories of Flavor (味道的记忆) — Chapter 8: Try Again (再试一次) | `nIPy1OC6qqhuUR4c` | 再试一次 |
| 9 | `<TBD>` | Memories of Flavor (味道的记忆) — Chapter 9: Competition Day (比赛的那天) | `UCUog8LyPpiOGHwJ` | 比赛的那天 |
| 10 | `<TBD>` | Memories of Flavor (味道的记忆) — Chapter 10: A New Beginning (新的开始) | `S5AzV7UrPaauNy3E` | 新的开始 |

## Vi-Zh Source

- Collection: `7nf5wi1d` — "Truyện (小说)"
- Series: `uq7ezeuh` — "味道的记忆 (Ký Ức Hương Vị)"
- Display orders: 1–10

## How content was created

Each en-zh chapter curriculum was derived from its vi-zh source via a standalone Python script:

1. **Fetch** the vi-zh source curriculum via `curriculum/getOne`
2. **Strip** auto-generated keys (`mp3Url`, `illustrationSet`, `chapterBookmarks`, `segments`, `whiteboardItems`, `userReadingId`, `lessonUniqueId`, `curriculumTags`, `taskId`, `imageId`) using `strip_keys()`
3. **Transform** all Vietnamese user-facing text to hand-written English — titles, descriptions (with narrative hooks/cliffhangers), previews, introAudio scripts, writing prompts, activity titles/descriptions, session titles, vocabulary definitions
4. **Upload** via `curriculum/create` with `language="zh"`, `userLanguage="en"`

The orchestrator script (`create_en_zh_memories_series.py`) created the shared en-zh Fiction collection and the Memories of Flavor series, wired them together, added all 10 chapter curriculums to the series, and set display orders 1–10. Series display order: 0 (matching vi-zh source).

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

-- Find en-zh Memories of Flavor chapters
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
WHERE csi.curriculum_series_id = 'uq7ezeuh'
ORDER BY c.display_order;
```
