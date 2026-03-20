# Movie-Based Vocab Series

## Collection: Học Từ Vựng Qua Điện Ảnh (Learn Vocabulary Through Cinema)

- **Collection ID**: `if1zlu2q`
- **Series ID**: `vy5wp4qk` (display_order: 100)
- **Language**: vi-en (Vietnamese speakers learning English)
- **Level**: A2-B1 (Pre-intermediate to Intermediate)

## Curriculums

| # | Movie | Curriculum ID | YouTube URL |
|---|---|---|---|
| 0 | Forrest Gump (1994) — Bus bench "Life is like a box of chocolates" | `5MsWSZwcWGYpfnrO` | https://www.youtube.com/watch?v=vdtqSaJO-iM |
| 1 | The Shawshank Redemption (1994) — Andy & Red "Get busy living or get busy dying" | `yCj2EZKIPTkFNqtS` | https://www.youtube.com/watch?v=kotNxb2YApk |
| 2 | Dead Poets Society (1989) — Keating's "Carpe Diem" first class | `LLy5qjuLk0VZ7SIi` | https://www.youtube.com/watch?v=vi0Lbjs5ECI |
| 3 | The Pursuit of Happyness (2006) — Basketball & Dreams "You got a dream, you gotta protect it" | `XjJRTMHxnBXFiA31` | https://www.youtube.com/watch?v=bMfOMBGNfMo |

## How Content Was Created

Each curriculum was created by a standalone Python script (`create_movie_N_<movie>.py`) that:
1. Defined 18 vocabulary words (3 groups of 6) drawn from verbatim movie dialogue
2. Wrote 5 learning sessions: 3 learning sessions (12 activities each), 1 review session (4 activities), 1 full dialogue reading + farewell (5 activities)
3. All learner-facing text (descriptions, previews, introAudio scripts, writing prompts) hand-written in Vietnamese
4. Validated structural properties (18 unique words, correct activity sequences, no strip keys, youtubeUrl present, vocab in dialogue, etc.) before upload
5. Called `curriculum/create` API with `language="en"`, `userLanguage="vi"`

An orchestrator script (`create_movie_series.py`) created the collection and series, wired them together, and set display orders.

All scripts were deleted after successful creation and verification.

## SQL Queries

```sql
-- Find the cinema collection
SELECT id, title, description, is_public
FROM curriculum_collections
WHERE id = 'if1zlu2q';

-- Find the movie series and its curriculums
SELECT c.id, c.content->>'title' as title, c.display_order,
       c.content->>'youtubeUrl' as youtube_url, c.is_public
FROM curriculum c
JOIN curriculum_series_items csi ON csi.curriculum_id = c.id
WHERE csi.curriculum_series_id = 'vy5wp4qk'
ORDER BY c.display_order;

-- Verify language homogeneity
SELECT * FROM curriculum_series_language_list
WHERE id = 'vy5wp4qk';

-- Get full content for any curriculum
SELECT content FROM curriculum WHERE id = '5MsWSZwcWGYpfnrO';
```

## Recreation

To recreate, write new Python scripts following the same pattern as the song-based-vocab-series. Each script needs:
- 18 vocabulary words from verbatim movie dialogue (A2-B1 level)
- 5 sessions matching the exact activity type sequences
- Hand-written Vietnamese descriptions, previews, introAudio, and writing prompts
- Inline `validate()` and `strip_keys()` functions
- YouTube URL for the scene clip
