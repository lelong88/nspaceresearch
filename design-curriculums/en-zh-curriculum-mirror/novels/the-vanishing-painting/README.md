# En-Zh Novel: The Vanishing Painting (消失的画)

Collection: **Fiction (小说)** (`<COLLECTION_ID>`) — shared across all 3 novels
Series: **The Vanishing Painting (消失的画)** (`<SERIES_ID>`)
Language pair: en-zh | 10 chapters | Level: pre-intermediate (HSK2-HSK3)

## Curriculums in series

| Ch | En-Zh ID | Title | Vi-Zh Source ID | Chinese Chapter Title |
|---|---|---|---|---|
| 1 | `<TBD>` | The Vanishing Painting (消失的画) — Chapter 1: A New Beginning (新的开始) | `U8nEjKpNVMw9VYZ1` | 新的开始 |
| 2 | `<TBD>` | The Vanishing Painting (消失的画) — Chapter 2: The Vanishing Painting (消失的画) | `6iPbBhBurzqovSVr` | 消失的画 |
| 3 | `<TBD>` | The Vanishing Painting (消失的画) — Chapter 3: The First Clue (第一个线索) | `7NUMvLypRZCRfhNw` | 第一个线索 |
| 4 | `<TBD>` | The Vanishing Painting (消失的画) — Chapter 4: The Suspicious Person (可疑的人) | `si3UEHDthdTFejwk` | 可疑的人 |
| 5 | `<TBD>` | The Vanishing Painting (消失的画) — Chapter 5: The Basement (地下室) | `KQqX7Y0uAus7bBFQ` | 地下室 |
| 6 | `<TBD>` | The Vanishing Painting (消失的画) — Chapter 6: Grandfather's Story (爷爷的故事) | `UBIVG8FJDqOP2DfK` | 爷爷的故事 |
| 7 | `<TBD>` | The Vanishing Painting (消失的画) — Chapter 7: Going South (去南方) | `5GoypASiFMsTp7Wj` | 去南方 |
| 8 | `<TBD>` | The Vanishing Painting (消失的画) — Chapter 8: The Truth (真相) | `teUUsSbTCmo6NSvy` | 真相 |
| 9 | `<TBD>` | The Vanishing Painting (消失的画) — Chapter 9: Back to the Small Town (回到小镇) | `IVEdJbUdlOmXHYMs` | 回到小镇 |
| 10 | `<TBD>` | The Vanishing Painting (消失的画) — Chapter 10: A Beautiful Summer (美丽的夏天) | `cELrsm8undLuHLl6` | 美丽的夏天 |

## Vi-Zh Source

- Collection: `7nf5wi1d` — "Truyện (小说)"
- Series: `wlzqfag8` — "Bức Tranh Biến Mất (消失的画)"
- Display orders: 1–10

## How content was created

Each en-zh chapter curriculum was derived from its vi-zh source via a standalone Python script:

1. **Fetch** the vi-zh source curriculum via `curriculum/getOne`
2. **Strip** auto-generated keys (`mp3Url`, `illustrationSet`, `chapterBookmarks`, `segments`, `whiteboardItems`, `userReadingId`, `lessonUniqueId`, `curriculumTags`, `taskId`, `imageId`) using `strip_keys()`
3. **Transform** all Vietnamese user-facing text to hand-written English — titles, descriptions (with narrative hooks/cliffhangers), previews, introAudio scripts, writing prompts, activity titles/descriptions, session titles, vocabulary definitions
4. **Upload** via `curriculum/create` with `language="zh"`, `userLanguage="en"`

The orchestrator script (`create_en_zh_vanishing_series.py`) created the Vanishing Painting series, wired it to the existing en-zh Fiction collection (created by the Memories of Flavor orchestrator), added all 10 chapter curriculums to the series, and set display orders 1–10. Series display order: 0 (matching vi-zh source).

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

-- Find en-zh Vanishing Painting chapters
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
WHERE csi.curriculum_series_id = 'wlzqfag8'
ORDER BY c.display_order;
```
