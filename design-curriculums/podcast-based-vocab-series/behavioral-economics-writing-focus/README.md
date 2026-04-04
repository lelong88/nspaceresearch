# Behavioral Economics – Tại Sao Bạn Luôn Quyết Định Sai? (Viết Chuyên Sâu)

## Curriculum

- **Curriculum ID**: `gTfankai2As4mWKZ`
- **Collection**: `1pspi6gt` (Học Từ Vựng Qua Podcast)
- **Display Order**: 5
- **Language**: vi-en (Vietnamese speakers learning English)
- **Based on**: `rkgaIEVr1QByTjzE` (original Behavioral Economics curriculum)

## What Changed From the Original

This is a writing-focused variant of the original Behavioral Economics curriculum. Two structural changes:

1. **Removed all `speakReading` activities** — from sessions 1, 2, 3, 4 (review), and 5 (final reading)
2. **Added `writingParagraph` after each `writingSentence`** — in sessions 1, 2, and 3

Everything else (introAudio, flashcards, vocab levels, reading, readAlong, review session structure) is identical to the original.

### Activity Sequence Per Learning Session (1-3)

Original: introAudio → introAudio → introAudio → viewFlashcards → speakFlashcards → vocabLevel1 → vocabLevel2 → vocabLevel3 → reading → **speakReading** → readAlong → writingSentence

New: introAudio → introAudio → introAudio → viewFlashcards → speakFlashcards → vocabLevel1 → vocabLevel2 → vocabLevel3 → reading → readAlong → writingSentence → **writingParagraph**

### Writing Paragraph Prompts

- Session 1: Analyze how an e-commerce company could use anchoring, framing, and nudge to design product pages, discussing the ethics of exploiting loss aversion in marketing
- Session 2: Analyze a startup's sunk cost fallacy through the lens of confirmation bias and endowment effect, proposing better decision-making using bounded rationality and prospect theory
- Session 3: Design a government retirement savings program using libertarian paternalism and choice architecture, discussing the ethical boundary between nudge and manipulation

## How Content Was Created

1. Fetched original curriculum `rkgaIEVr1QByTjzE` via `curriculum/getOne`
2. Stripped generated keys (mp3Url, illustrationSet, segments, etc.)
3. Removed all `speakReading` activities from every session
4. Added hand-written `writingParagraph` activities after each `writingSentence` in sessions 1-3
5. Updated title, description, and preview to indicate writing focus
6. Created via `curriculum/create` API, added to collection `1pspi6gt` at display order 5

Script deleted after successful creation.

## SQL Queries

```sql
-- Find this curriculum
SELECT id, content->>'title' as title, display_order, is_public
FROM curriculum
WHERE id = 'gTfankai2As4mWKZ';

-- Verify activity types per session
SELECT
  s.value->>'title' as session_title,
  jsonb_agg(a.value->>'activityType' ORDER BY a.ordinality) as activity_types
FROM curriculum c,
  jsonb_array_elements(c.content->'learningSessions') WITH ORDINALITY s(value, session_ord),
  jsonb_array_elements(s.value->'activities') WITH ORDINALITY a(value, ordinality)
WHERE c.id = 'gTfankai2As4mWKZ'
GROUP BY s.session_ord, s.value->>'title'
ORDER BY s.session_ord;

-- Compare with original
SELECT id, content->>'title' as title FROM curriculum
WHERE id IN ('rkgaIEVr1QByTjzE', 'gTfankai2As4mWKZ');
```

## Recreation

To recreate, fetch the original curriculum `rkgaIEVr1QByTjzE`, strip generated keys, remove `speakReading` activities, add `writingParagraph` after each `writingSentence` in sessions 1-3 with topic-specific prompts, and upload via `curriculum/create`.
