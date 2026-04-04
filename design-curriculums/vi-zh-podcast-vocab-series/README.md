# vi-zh Podcast Vocab Series

## Collection: Học Từ Vựng Tiếng Trung Qua Podcast (通过播客学中文词汇)

- **Collection ID**: `tbd4oask`
- **Language**: vi-zh (Vietnamese speakers learning Chinese)

## Curriculums

| # | Speaker | Curriculum ID | YouTube URL |
|---|---------|---|---|
| 0 | 陳永儀 (May Chen) — 沒有「負面能量」是好事嗎？ | `eHXasGBazU5N5Ina` | https://www.youtube.com/watch?v=uiJ4zibW8_M |
| 1 | 蔣勳 (Chiang Hsun) — 留十八分鐘給自己 | `8RQxb2FJYEfRmo3j` | https://www.youtube.com/watch?v=6i7RcP39NB0 |
| 2 | 曾之喬 (Joanne Tseng) — 不要太努力 | `DClz5ESU6Bvy08aT` | https://www.youtube.com/watch?v=t7ZI9c6Ze7E |
| 3 | 莊祖宜 (Tzui Chuang) — 吃出更好的未來 | `Fy0Raj6Vko7n79qN` | https://www.youtube.com/watch?v=wcfLMfo6LQc |

## How Content Was Created

Each curriculum was created by a standalone Python script (`create_podcast_N.py`) that:
1. Defined 18 HSK2-HSK3 vocabulary words (3 groups of 6) drawn from Chinese-language TEDx/TED talks
2. Wrote 5 learning sessions: 3 learning sessions (12 activities each), 1 review session (4 activities), 1 full reading + farewell (5 activities)
3. All learner-facing text (descriptions, previews, introAudio scripts, writing prompts, activity titles, session titles, vocabulary definitions) hand-written in Vietnamese
4. Validated structural properties (18 unique words, correct activity sequences, no strip keys, youtubeUrl present, contentTypeTags=["podcast"]) before upload
5. Called `curriculum/create` API with `language="zh"`, `userLanguage="vi"`
6. All curriculums created as private (`is_public = false`)

The same 4 Chinese-language talks are shared with the en-zh podcast series (English UI counterpart). The talks were selected for clear Mandarin speech, YouTube availability, and HSK2-HSK3 vocabulary suitability.

An orchestrator script (`create_vi_zh_podcast_collection.py`) created the collection and added all 4 curriculums directly to it (no series intermediary), then set display orders 0–3.

All scripts and the talk selection document (`CHINESE_TALKS_SELECTION.md`) were deleted after successful creation and verification.

## SQL Queries

```sql
-- Find the collection
SELECT id, title, description, is_public
FROM curriculum_collections
WHERE id = 'tbd4oask';

-- Find curriculums in collection
SELECT c.id, c.content->>'title' as title, c.display_order,
       c.content->>'youtubeUrl' as youtube_url, c.is_public
FROM curriculum c
JOIN curriculum_collection_items cci ON cci.curriculum_id = c.id
WHERE cci.curriculum_collection_id = 'tbd4oask'
ORDER BY c.display_order;

-- Get full content for any curriculum
SELECT content FROM curriculum WHERE id = 'eHXasGBazU5N5Ina';
```

## Recreation

To recreate, write new Python scripts following the same pattern. Each script needs:
- 18 HSK2-HSK3 vocabulary words from the Chinese-language talk (3 groups of 6)
- 5 sessions matching the exact activity type sequences (12, 12, 12, 4, 5 activities)
- Hand-written Vietnamese descriptions, previews, introAudio, writing prompts, activity titles
- Inline `validate()` and `strip_keys()` functions
- `language="zh"`, `userLanguage="vi"` as top-level API params
- `contentTypeTags=["podcast"]` and `youtubeUrl` at top level of content JSON
- `is_public = false`

Content is fully recoverable via `curriculum/getOne` with each curriculum ID.
