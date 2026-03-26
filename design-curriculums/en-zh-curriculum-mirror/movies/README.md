# En-Zh Movie-Based Vocabulary Series

Collection: **Learn Chinese Vocabulary Through Cinema (通过电影学中文词汇)** (`<COLLECTION_ID>`)
Series: **Learn Chinese Vocabulary Through Film (通过电影学中文词汇)** (`<SERIES_ID>`)
Language pair: en-zh | 18 words each | 5 sessions | Level: pre-intermediate to intermediate (HSK2-HSK3)

## Curriculums in series

| # | En-Zh ID | Title | Vi-Zh Source ID | Movie |
|---|---|---|---|---|
| 0 | `<TBD>` | Learn Through Film: '功夫' – The Pig Sty Alley Showdown | `3j80e3IpKczh26B0` | 功夫 (Kung Fu Hustle) |
| 1 | `<TBD>` | Learn Through Film: '少林足球' – The Shaolin Soccer Final | `PUABCeIlJ2uEg5rE` | 少林足球 (Shaolin Soccer) |
| 2 | `<TBD>` | Learn Through Film: '大话西游' – The Moonlight Box | `EjvrQRIPPUPQW5Gt` | 大话西游 (A Chinese Odyssey) |
| 3 | `<TBD>` | Learn Through Film: '让子弹飞' – Let the Bullets Fly | `uEciL1GTo1OFZbbm` | 让子弹飞 (Let the Bullets Fly) |

## Vi-Zh Source

- Collection: `x8cakjtw` — "Học Từ Vựng Tiếng Trung Qua Điện Ảnh (通过电影学中文词汇)"
- Series: `v7a70y0u` — "Học Từ Vựng Tiếng Trung Qua Phim (通过电影学中文词汇)"

## How content was created

Each en-zh curriculum was derived from its vi-zh source via a standalone Python script:

1. **Fetch** the vi-zh source curriculum via `curriculum/getOne`
2. **Strip** auto-generated keys (`mp3Url`, `illustrationSet`, `chapterBookmarks`, `segments`, `whiteboardItems`, `userReadingId`, `lessonUniqueId`, `curriculumTags`, `taskId`, `imageId`) using `strip_keys()`
3. **Transform** all Vietnamese user-facing text to hand-written English — titles, descriptions, previews, introAudio scripts, writing prompts, activity titles/descriptions, session titles, vocabulary definitions
4. **Upload** via `curriculum/create` with `language="zh"`, `userLanguage="en"`

The orchestrator script (`create_en_zh_movie_series.py`) created the en-zh collection and series, wired them together, added all 4 curriculums to the series, and set display orders (0, 1, 2, 3). Series display order: 100 (matching vi-zh source).

Structure per curriculum:
- 18 vocabulary words (6 per session) drawn from movie dialogue, HSK2-HSK3 level
- 5 sessions: 3 learning + 1 review + 1 full dialogue reading with farewell
- Movie dialogue in simplified Chinese used as reading passages
- introAudio scripts include pinyin when teaching vocabulary
- Writing prompts include pinyin in parentheses and Chinese example sentences
- `language="zh"`, `userLanguage="en"` as top-level API params
- All curriculums are private (`is_public = false`)

All creation scripts were deleted after successful creation and verification. Content is fully recoverable via `curriculum/getOne` with each curriculum ID.

## SQL queries

```sql
-- Find en-zh collection
SELECT * FROM curriculum_collections WHERE id = '<COLLECTION_ID>';

-- Find en-zh series in collection
SELECT cs.*
FROM curriculum_series cs
JOIN curriculum_collection_series ccs ON ccs.curriculum_series_id = cs.id
WHERE ccs.curriculum_collection_id = '<COLLECTION_ID>';

-- Find en-zh curriculums in series
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
WHERE csi.curriculum_series_id = 'v7a70y0u'
ORDER BY c.display_order;
```
