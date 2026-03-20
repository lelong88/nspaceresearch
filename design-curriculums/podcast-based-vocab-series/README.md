# Podcast-Based Vocab Series

## Collection: Học Từ Vựng Qua Podcast (Learn Vocabulary Through Podcasts)

- **Collection ID**: `1pspi6gt`
- **Series ID**: `5yvucn5k` (display_order: 100)
- **Language**: vi-en (Vietnamese speakers learning English)
- **Level**: A2-B1 (Pre-intermediate to Intermediate)

## Curriculums

| # | TED Talk | Curriculum ID | YouTube URL |
|---|---|---|---|
| 0 | Tim Urban — "Inside the Mind of a Master Procrastinator" | `lPa8rC1ua4rJrOUl` | https://www.youtube.com/watch?v=arj7oStGLkU |
| 1 | Amy Cuddy — "Your Body Language May Shape Who You Are" | `6r63yMCmoRH4AcWr` | https://www.youtube.com/watch?v=Ks-_Mh1QhMc |
| 2 | Julian Treasure — "How to Speak So That People Want to Listen" | `DUfee1HEWcBcNEXp` | https://www.youtube.com/watch?v=eIho2S0ZahI |
| 3 | Brené Brown — "The Power of Vulnerability" | `z0qB88II5SgkKYrp` | https://www.youtube.com/watch?v=iCvmsMzlF7o |

## How Content Was Created

Each curriculum was created by a standalone Python script (`create_podcast_N_<speaker>.py`) that:
1. Defined 18 vocabulary words (3 groups of 6) drawn from verbatim TED Talk transcripts
2. Wrote 5 learning sessions: 3 learning sessions (12 activities each), 1 review session (4 activities), 1 full transcript reading + farewell (5 activities)
3. All learner-facing text (descriptions, previews, introAudio scripts, writing prompts) hand-written in Vietnamese
4. Validated structural properties (18 unique words, correct activity sequences, no strip keys, youtubeUrl present, vocab in transcript, etc.) before upload
5. Called `curriculum/create` API with `language="en"`, `userLanguage="vi"`

An orchestrator script (`create_podcast_series.py`) created the collection and series, wired them together, and set display orders.

All scripts were deleted after successful creation and verification.

## SQL Queries

```sql
-- Find the podcast collection
SELECT id, title, description, is_public
FROM curriculum_collections
WHERE id = '1pspi6gt';

-- Find the podcast series and its curriculums
SELECT c.id, c.content->>'title' as title, c.display_order,
       c.content->>'youtubeUrl' as youtube_url, c.is_public
FROM curriculum c
JOIN curriculum_series_items csi ON csi.curriculum_id = c.id
WHERE csi.curriculum_series_id = '5yvucn5k'
ORDER BY c.display_order;

-- Verify language homogeneity
SELECT * FROM curriculum_series_language_list
WHERE id = '5yvucn5k';

-- Get full content for any curriculum
SELECT content FROM curriculum WHERE id = 'lPa8rC1ua4rJrOUl';
```

## Recreation

To recreate, write new Python scripts following the same pattern as the movie-based-vocab-series. Each script needs:
- 18 vocabulary words from verbatim TED Talk transcript (A2-B1 level)
- 5 sessions matching the exact activity type sequences (12, 12, 12, 4, 5)
- Hand-written Vietnamese descriptions, previews, introAudio, and writing prompts
- Inline `validate()` and `strip_keys()` functions
- YouTube URL for the TED Talk
- readAlong description: "Nghe podcast và theo dõi."
