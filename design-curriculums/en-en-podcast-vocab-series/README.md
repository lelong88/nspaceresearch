# en-en Podcast Vocab Series

## Collection: Learn Vocabulary Through Podcasts

- **Collection ID**: `mqdqxuyp`
- **Language**: en-en (English speakers learning English)

## Curriculums

| # | TED Talk | Curriculum ID | vi-en Source ID |
|---|---|---|---|
| 0 | Tim Urban — "Inside the Mind of a Master Procrastinator" | `MFxuYamWEgfdYo1e` | `lPa8rC1ua4rJrOUl` |
| 1 | Amy Cuddy — "Your Body Language May Shape Who You Are" | `I4tI7E6D0TzljRZx` | `6r63yMCmoRH4AcWr` |
| 2 | Julian Treasure — "How to Speak So That People Want to Listen" | `vgNSnNliznmmarAq` | `DUfee1HEWcBcNEXp` |
| 3 | Brené Brown — "The Power of Vulnerability" | `FuvFhVYNCmdVUJUB` | `z0qB88II5SgkKYrp` |
| 4 | Angela Duckworth — "Grit: The Power of Passion and Perseverance" | `NwGqhGPTLqf86mPv` | — |
| 5 | Richard Cytowic — "Your Brain Wasn't Built for This" (Big Think) | `egmWT6aNQAdb5TUy` | — (speaking focus, original) |

## Curriculum #5: Richard Cytowic (Speaking Focus)

Curriculum `egmWT6aNQAdb5TUy` is a **speaking-focus** curriculum with a reduced activity set:
- `introAudio` (short welcome/recap only)
- `viewFlashcards`
- `speakReading` (transcript sections spoken aloud)
- `writingParagraph` (analytical writing prompts)

No `speakFlashcards`, `vocabLevel*`, `reading`, `readAlong`, or `writingSentence` activities.
Created from the Big Think video transcript (not mirrored from vi-en).
Script: `create_podcast_cytowic_stone_age_brain.py` (deleted after successful creation).

## How Content Was Created

Each curriculum was created by a mirror script (`create_podcast_N_<speaker>.py`) that:
1. Fetched the corresponding vi-en source curriculum via `curriculum/getOne`
2. Ran `strip_keys()` to remove auto-generated keys
3. Transformed all Vietnamese user-facing text to hand-written English (titles, descriptions, previews, introAudio scripts, writing prompts, activity titles/descriptions, session titles, vocabulary definitions)
4. Validated structural properties (18 unique words, correct activity sequences, no strip keys, youtubeUrl present, contentTypeTags=["podcast"]) before upload
5. Called `curriculum/create` API with `language="en"`, `userLanguage="en"`
6. All curriculums created as private (`is_public = false`)

The same 4 TED Talks and youtubeUrls are shared with the vi-en podcast series. Each en-en curriculum mirrors its vi-en counterpart with English UI text instead of Vietnamese.

An orchestrator script (`create_en_en_podcast_collection.py`) created the collection and added all 4 curriculums directly to it (no series intermediary), then set display orders 0–3.

All scripts were deleted after successful creation and verification.

## SQL Queries

```sql
-- Find the collection
SELECT id, title, description, is_public
FROM curriculum_collections
WHERE id = 'mqdqxuyp';

-- Find curriculums in collection
SELECT c.id, c.content->>'title' as title, c.display_order,
       c.content->>'youtubeUrl' as youtube_url, c.is_public
FROM curriculum c
JOIN curriculum_collection_items cci ON cci.curriculum_id = c.id
WHERE cci.curriculum_collection_id = 'mqdqxuyp'
ORDER BY c.display_order;

-- Get full content for any curriculum
SELECT content FROM curriculum WHERE id = 'MFxuYamWEgfdYo1e';
```

## Recreation

To recreate, write new mirror scripts following the same pattern. Each script needs:
- Fetch vi-en source via `curriculum/getOne` with the source ID
- `strip_keys()` to remove auto-generated keys
- Hand-written English translations of all Vietnamese user-facing text
- 18 vocabulary words, 5 sessions (12, 12, 12, 4, 5 activities)
- Inline `validate()` and `strip_keys()` functions
- `language="en"`, `userLanguage="en"` as top-level API params
- `contentTypeTags=["podcast"]` and `youtubeUrl` at top level of content JSON
- `is_public = false`

Content is fully recoverable via `curriculum/getOne` with each curriculum ID.
