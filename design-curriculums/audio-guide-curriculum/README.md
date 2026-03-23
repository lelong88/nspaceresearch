# Audio Guide Curriculum

## Collection
- **ID**: `6lzqqynb`
- **Title**: Audio Guide

## Series 1: Audio Guide (en-en, advanced)
- **ID**: `04kh7nyk`
- **Display Order**: 100

| Order | Curriculum ID | Title |
|---|---|---|
| 0 | `MXlNlggDimQZcviH` | Audio Guide: The Science of Sleep |
| 1 | `D4B3gKKN5SkjH15h` | Audio Guide: The Psychology of Memory |

## Series 2: Học Qua Nghe (vi-en, intermediate)
- **ID**: `r01mrt51`
- **Display Order**: 200

| Order | Curriculum ID | Title |
|---|---|---|
| 0 | `jPizMzWTO4WMr0ru` | Học Qua Nghe: Giao Tiếp Hàng Ngày |
| 1 | `g9GFGaMda5FhOXgG` | Học Qua Nghe: Tiếng Anh Du Lịch |

## How Content Was Created
- Curriculum type: `audio_guide` — introAudio as the centerpiece (800-1000 words, 2× normal), multiple introAudio per session, no speaking, no writing, pure receptive learning
- Single-language variant (en-en): 4 sessions (5, 5, 4, 4 activities), 2 introAudio per learning session (extended + supplementary), readAlong replaces reading in S1-S2, reading only in S4
- Bilingual variant (vi-en): 4 sessions (6, 6, 5, 4 activities), 3 introAudio per learning session (bilingual vocab teaching + supplementary + mini-story), quiz-style introAudio in S3
- 10 vocab words per curriculum (2 groups of 5), no speakFlashcards/speakReading/speak/writingSentence/writingParagraph/vocabLevel3, vocabLevel2 only in S3
- Each curriculum created via standalone Python script with hand-written content, validated inline (17 structural properties), uploaded via `curriculum/create` API
- Orchestrator script created collection + 2 series, wired everything, set display orders
- All scripts deleted after verification

## SQL Queries

```sql
-- Find the collection
SELECT id, title, is_public FROM curriculum_collections WHERE id = '6lzqqynb';

-- Find both series
SELECT cs.id, cs.title, cs.display_order
FROM curriculum_series cs
JOIN curriculum_collection_series ccs ON ccs.curriculum_series_id = cs.id
WHERE ccs.curriculum_collection_id = '6lzqqynb'
ORDER BY cs.display_order;

-- Find all curriculums
SELECT c.id, c.content->>'title' as title, c.display_order, c.language, c.user_language
FROM curriculum c
JOIN curriculum_series_items csi ON csi.curriculum_id = c.id
WHERE csi.curriculum_series_id IN ('04kh7nyk', 'r01mrt51')
ORDER BY csi.curriculum_series_id, c.display_order;

-- Verify language homogeneity
SELECT * FROM curriculum_series_language_list WHERE id IN ('04kh7nyk', 'r01mrt51');
```

## Recreation
To recreate, write 4 Python scripts following the `audio_guide` curriculum type spec in `.kiro/specs/audio-guide-curriculum/`. Each script needs: 10 vocab words (2×5), readAlong passages (or mini-stories for bilingual), FULL_ARTICLE, 4 sessions with hand-written extended introAudio scripts (800-1000 words each), inline validate() function, and API call to `curriculum/create`. Then run an orchestrator to create collection + 2 series + wire everything.
