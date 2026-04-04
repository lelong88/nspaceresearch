# en-zh Podcast Vocab Series

## Collection: Learn Chinese Vocabulary Through Podcasts (通过播客学中文词汇)

- **Collection ID**: `h3i65ykf`
- **Language**: en-zh (English speakers learning Chinese)

## Curriculums

| # | Speaker | Curriculum ID | YouTube URL |
|---|---------|---|---|
| 0 | 陳永儀 (May Chen) — 沒有「負面能量」是好事嗎？ | `UMXagwItTkqbLCtg` | https://www.youtube.com/watch?v=uiJ4zibW8_M |
| 1 | 蔣勳 (Chiang Hsun) — 留十八分鐘給自己 | `uoFdPLtAQumH1Kmg` | https://www.youtube.com/watch?v=6i7RcP39NB0 |
| 2 | 曾之喬 (Joanne Tseng) — 不要太努力 | `co657nAhEzlPs1CB` | https://www.youtube.com/watch?v=t7ZI9c6Ze7E |
| 3 | 莊祖宜 (Tzui Chuang) — 吃出更好的未來 | `Wdur6rGTWuxF1gpl` | https://www.youtube.com/watch?v=wcfLMfo6LQc |

## How Content Was Created

Each curriculum was created by a standalone Python script (`create_podcast_N.py`) that:
1. Defined 18 HSK2-HSK3 vocabulary words (3 groups of 6) drawn from Chinese-language TEDx/TED talks
2. Wrote 5 learning sessions: 3 learning sessions (12 activities each), 1 review session (4 activities), 1 full reading + farewell (5 activities)
3. All learner-facing text (descriptions, previews, introAudio scripts, writing prompts, activity titles, session titles, vocabulary definitions) hand-written in English with pinyin included in introAudio vocabulary teaching and writing prompts
4. Validated structural properties (18 unique words, correct activity sequences, no strip keys, youtubeUrl present, contentTypeTags=["podcast"]) before upload
5. Called `curriculum/create` API with `language="zh"`, `userLanguage="en"`
6. All curriculums created as private (`is_public = false`)

The same 4 Chinese-language talks are shared with the vi-zh podcast series (Vietnamese UI counterpart). Each en-zh curriculum uses the same youtubeUrl and vocabulary words as its vi-zh counterpart, differing only in user-facing language (English vs Vietnamese) and the inclusion of pinyin.

An orchestrator script (`create_en_zh_podcast_collection.py`) created the collection and added all 4 curriculums directly to it (no series intermediary), then set display orders 0–3.

All scripts were deleted after successful creation and verification.

## SQL Queries

```sql
-- Find the collection
SELECT id, title, description, is_public
FROM curriculum_collections
WHERE id = 'h3i65ykf';

-- Find curriculums in collection
SELECT c.id, c.content->>'title' as title, c.display_order,
       c.content->>'youtubeUrl' as youtube_url, c.is_public
FROM curriculum c
JOIN curriculum_collection_items cci ON cci.curriculum_id = c.id
WHERE cci.curriculum_collection_id = 'h3i65ykf'
ORDER BY c.display_order;

-- Verify youtubeUrls match vi-zh counterparts
SELECT c.id, c.user_language, c.content->>'youtubeUrl' as youtube_url
FROM curriculum c
WHERE c.language = 'zh'
  AND c.content->>'contentTypeTags' LIKE '%podcast%'
  AND c.uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'
  AND c.uid NOT LIKE '%_deleted'
ORDER BY c.user_language, c.display_order;

-- Get full content for any curriculum
SELECT content FROM curriculum WHERE id = 'UMXagwItTkqbLCtg';
```

## Recreation

To recreate, write new Python scripts following the same pattern. Each script needs:
- 18 HSK2-HSK3 vocabulary words from the Chinese-language talk (3 groups of 6)
- 5 sessions matching the exact activity type sequences (12, 12, 12, 4, 5 activities)
- Hand-written English descriptions, previews, introAudio, writing prompts, activity titles — with pinyin in introAudio vocabulary teaching and writing prompt example sentences
- Inline `validate()` and `strip_keys()` functions
- `language="zh"`, `userLanguage="en"` as top-level API params
- `contentTypeTags=["podcast"]` and `youtubeUrl` at top level of content JSON
- `is_public = false`

Content is fully recoverable via `curriculum/getOne` with each curriculum ID.
