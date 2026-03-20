# Vi-Zh Song-Based Vocabulary Series

Collection: **Học Từ Vựng Tiếng Trung Qua Âm Nhạc (通过音乐学中文词汇)** (`jqmkzvf5`)
Series: **Học Từ Vựng Tiếng Trung Qua Bài Hát (通过歌曲学中文词汇)** (`sjv8b9r7`)
Language pair: vi-zh | 18 words each | 5 sessions | Level: pre-intermediate to intermediate (HSK2-HSK3)

## Curriculums in series

| # | ID | Title | Song | Artist |
|---|---|---|---|---|
| 0 | `Mi4dqOv4sAOb2axi` | Học Qua Bài Hát: '月亮代表我的心' – 邓丽君 | 月亮代表我的心 | 邓丽君 (Teresa Teng) |
| 1 | `4ryQKO4ffbmWJNH4` | Học Qua Bài Hát: '朋友' – 周华健 | 朋友 | 周华健 (Emil Chau) |
| 2 | `5fthZeygE85aSBDS` | Học Qua Bài Hát: '甜蜜蜜' – 邓丽君 | 甜蜜蜜 | 邓丽君 (Teresa Teng) |
| 3 | `b4pH6tU7szEqye74` | Học Qua Bài Hát: '童话' – 光良 | 童话 | 光良 (Michael Wong) |

## YouTube URLs

| Song | URL |
|---|---|
| 月亮代表我的心 | https://www.youtube.com/watch?v=bv_cEeDlop0 |
| 朋友 | https://www.youtube.com/watch?v=oxGkOKajFao |
| 甜蜜蜜 | https://www.youtube.com/watch?v=bYMagMFbMaw |
| 童话 | https://www.youtube.com/watch?v=IBTmypxD2mU |

## How content was created

Each curriculum was created via a standalone Python script that built the content dict with hand-written Vietnamese/Chinese text, validated it against 12 structural properties, and uploaded via `curriculum/create`. The orchestrator script (`create_zh_song_series.py`) created the collection and series, wired them together, and set display orders.

Structure per curriculum:
- 18 vocabulary words (6 per session) drawn from the song lyrics, HSK2-HSK3 level
- 5 sessions: 3 learning + 1 review + 1 full lyrics reading with farewell
- Verbatim song lyrics in simplified Chinese used as reading passages
- introAudio scripts include pinyin when teaching vocabulary
- Writing prompts include pinyin in parentheses and Chinese example sentences
- `youtubeUrl` at top level of content JSON
- `language="zh"`, `userLanguage="vi"` as top-level API params
- All curriculums are private (`is_public = false`)

Content is fully recoverable via `curriculum/getOne` with each curriculum ID.

## SQL queries

```sql
-- Find collection
SELECT * FROM curriculum_collections WHERE id = 'jqmkzvf5';

-- Find series in collection
SELECT cs.*
FROM curriculum_series cs
JOIN curriculum_collection_series ccs ON ccs.curriculum_series_id = cs.id
WHERE ccs.curriculum_collection_id = 'jqmkzvf5';

-- Find curriculums in series
SELECT c.id, c.content->>'title' as title, c.display_order,
       c.content->>'youtubeUrl' as youtube_url
FROM curriculum c
JOIN curriculum_series_items csi ON csi.curriculum_id = c.id
WHERE csi.curriculum_series_id = 'sjv8b9r7'
ORDER BY c.display_order;

-- Check language homogeneity
SELECT * FROM curriculum_series_language_list WHERE id = 'sjv8b9r7';
```
