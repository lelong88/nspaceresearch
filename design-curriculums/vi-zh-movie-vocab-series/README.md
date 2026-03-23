# Vi-Zh Movie-Based Vocabulary Series

Collection: **Học Từ Vựng Tiếng Trung Qua Điện Ảnh (通过电影学中文词汇)** (`x8cakjtw`)
Series: **Học Từ Vựng Tiếng Trung Qua Phim (通过电影学中文词汇)** (`v7a70y0u`)
Language pair: vi-zh | 18 words each | 5 sessions | Level: pre-intermediate to intermediate (HSK2-HSK3)

## Curriculums in series

| # | ID | Title | Movie | Scene |
|---|---|---|---|---|
| 0 | `3j80e3IpKczh26B0` | Học Qua Phim: '功夫' – Cảnh đối đầu ở Hẻm Heo | 功夫 (Kung Fu Hustle, 2004) | Axe Gang confrontation at Pig Sty Alley |
| 1 | `PUABCeIlJ2uEg5rE` | Học Qua Phim: '少林足球' – Cảnh gặp gỡ giữa Tinh Tinh và Phong Ca | 少林足球 (Shaolin Soccer, 2001) | Sing meets Fung — recruiting scene |
| 2 | `EjvrQRIPPUPQW5Gt` | Học Qua Phim: '大话西游' – Cảnh tỏ tình một vạn năm | 大话西游 (A Chinese Odyssey, 1995) | "10,000 years" love confession |
| 3 | `uEciL1GTo1OFZbbm` | Học Qua Phim: '让子弹飞' – Cảnh đối đầu trên bàn tiệc ở Nga Thành | 让子弹飞 (Let the Bullets Fly, 2010) | Dinner confrontation at Goose Town |

## YouTube URLs

| Movie | URL |
|---|---|
| 功夫 | https://www.youtube.com/watch?v=sSMbyG4f5DI |
| 少林足球 | https://www.youtube.com/watch?v=qdVLSjNJmk8 |
| 大话西游 | https://www.youtube.com/watch?v=8jLTkNMPaWI |
| 让子弹飞 | https://www.youtube.com/watch?v=3MgpCmGVzis |

## How content was created

Each curriculum was created via a standalone Python script that built the content dict with hand-written Vietnamese/Chinese text, validated it against 12 structural properties, and uploaded via `curriculum/create`. The orchestrator script (`create_zh_movie_series.py`) created the collection and series, wired them together, and set display orders.

Structure per curriculum:
- 18 vocabulary words (6 per session) drawn from the movie dialogue, HSK2-HSK3 level
- 5 sessions: 3 learning + 1 review + 1 full dialogue reading with farewell
- Verbatim movie dialogue in simplified Chinese used as reading passages
- introAudio scripts include pinyin when teaching vocabulary
- Writing prompts include pinyin in parentheses and Chinese example sentences
- `youtubeUrl` at top level of content JSON
- `language="zh"`, `userLanguage="vi"` as top-level API params
- All curriculums are private (`is_public = false`)

Content is fully recoverable via `curriculum/getOne` with each curriculum ID.

## SQL queries

```sql
-- Find collection
SELECT * FROM curriculum_collections WHERE id = 'x8cakjtw';

-- Find series in collection
SELECT cs.*
FROM curriculum_series cs
JOIN curriculum_collection_series ccs ON ccs.curriculum_series_id = cs.id
WHERE ccs.curriculum_collection_id = 'x8cakjtw';

-- Find curriculums in series
SELECT c.id, c.content->>'title' as title, c.display_order,
       c.content->>'youtubeUrl' as youtube_url
FROM curriculum c
JOIN curriculum_series_items csi ON csi.curriculum_id = c.id
WHERE csi.curriculum_series_id = 'v7a70y0u'
ORDER BY c.display_order;

-- Check language homogeneity
SELECT * FROM curriculum_series_language_list WHERE id = 'v7a70y0u';
```
