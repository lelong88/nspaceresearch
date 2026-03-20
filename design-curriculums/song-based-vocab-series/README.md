# Song-Based Vocabulary Series

Collection: **Học Từ Vựng Qua Âm Nhạc (Learn Vocabulary Through Music)** (`uuxhatco`)
Series: **Học Từ Vựng Qua Bài Hát (Learn Vocabulary Through Songs)** (`vp6mt6rn`)
Language pair: vi-en | 18 words each | 5 sessions | Level: pre-intermediate to intermediate

## Curriculums in series

| # | ID | Title | Song | Artist |
|---|---|---|---|---|
| 0 | `qVv18hr5L4sTQs6i` | Học Qua Bài Hát: 'Heal the World' – Michael Jackson | Heal the World | Michael Jackson |
| 1 | `u900kHjhKdkWyp8C` | Học Qua Bài Hát: 'Imagine' – John Lennon | Imagine | John Lennon |
| 2 | `4Ho0bZURRPz2TiJA` | Học Qua Bài Hát: 'Lean on Me' – Bill Withers | Lean on Me | Bill Withers |
| 3 | `5WdGkIlyRDO4dzsL` | Học Qua Bài Hát: 'What a Wonderful World' – Louis Armstrong | What a Wonderful World | Louis Armstrong |

## YouTube URLs

| Song | URL |
|---|---|
| Heal the World | https://www.youtube.com/watch?v=nhcG9wqn0gU |
| Imagine | https://www.youtube.com/watch?v=YkgkThdzX-8 |
| Lean on Me | https://www.youtube.com/watch?v=fOZ-MySzAQo |
| What a Wonderful World | https://www.youtube.com/watch?v=A3yCcXgbKrE |

## How content was created

Each curriculum was created via a standalone Python script that built the content dict with hand-written Vietnamese/English text, validated it against 12 structural properties, and uploaded via `curriculum/create`. The orchestrator script (`create_song_series.py`) created the collection and series, wired them together, and set display orders.

Structure per curriculum:
- 18 vocabulary words (6 per session) drawn from the song lyrics
- 5 sessions: 3 learning + 1 review + 1 full lyrics reading with farewell
- Verbatim song lyrics used as reading passages
- `youtubeUrl` at top level of content JSON
- `language="en"`, `userLanguage="vi"` as top-level API params
- All curriculums are private (`is_public = false`)

Content is fully recoverable via `curriculum/getOne` with each curriculum ID.

## SQL queries

```sql
-- Find collection
SELECT * FROM curriculum_collections WHERE id = 'uuxhatco';

-- Find series in collection
SELECT cs.*
FROM curriculum_series cs
JOIN curriculum_collection_series ccs ON ccs.curriculum_series_id = cs.id
WHERE ccs.curriculum_collection_id = 'uuxhatco';

-- Find curriculums in series
SELECT c.id, c.content->>'title' as title, c.display_order,
       c.content->>'youtubeUrl' as youtube_url
FROM curriculum c
JOIN curriculum_series_items csi ON csi.curriculum_id = c.id
WHERE csi.curriculum_series_id = 'vp6mt6rn'
ORDER BY c.display_order;

-- Check language homogeneity
SELECT * FROM curriculum_series_language_list WHERE id = 'vp6mt6rn';
```
