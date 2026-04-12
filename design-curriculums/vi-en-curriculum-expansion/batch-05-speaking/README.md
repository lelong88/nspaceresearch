# Batch 05 — Speaking Focus (12 curriculums)

Vi-en curriculum expansion, batch 5: 12 speaking_focus curriculums spanning beginner through advanced. Topics: Food, Daily life, Relationships, Vietnamese culture, Psychology, Arts, Sports, Tech/digital life, Law, History. All curriculums have 18 words (3 groups of 6), 5 sessions, speakFlashcards + speakReading in every learning session, no writingParagraph.

## Curriculum IDs (12 total)

| # | Title | ID | Level | Skill Focus | Content Type |
|---|-------|----|-------|-------------|--------------|
| 1 | Ordering Food | `QAJJ2sZUL3c0tsWV` | beginner | speaking_focus | [] |
| 2 | Asking for Directions | `3TXcGwGByJJECai7` | beginner | speaking_focus | [] |
| 3 | Introducing Yourself | `rmTSVijOq1LbYdUx` | preintermediate | speaking_focus | [] |
| 4 | Describing Your Hometown | `lnlSt1K9cQjahiis` | preintermediate | speaking_focus | [] |
| 5 | Giving Opinions | `D3Ub6lbI3QcZJZbF` | preintermediate | speaking_focus | [] |
| 6 | Telling a Story | `GPPdt20hrEABjIjZ` | intermediate | speaking_focus | [] |
| 7 | Debating Sports Rules | `Nm9hUWT8DGIVtRVf` | intermediate | speaking_focus | [] |
| 8 | Job Interview Practice | `IPp6ywp29TaJOd3o` | intermediate | speaking_focus | [] |
| 9 | Presenting an Idea | `6JNVxEAKaDHW5d5V` | upperintermediate | speaking_focus | [] |
| 10 | Negotiating a Deal | `kKp8LSndyBqDsNU1` | upperintermediate | speaking_focus | [] |
| 11 | Defending a Position | `VWokcRfKFhHjcEYv` | advanced | speaking_focus | [] |
| 12 | Impromptu Speech | `4nsJJiDERfBR1V3r` | advanced | speaking_focus | ["podcast"] |

## Series IDs (3 total — 1 existing updated, 2 new)

| Series ID | Title | Curriculums | Levels | Status |
|-----------|-------|-------------|--------|--------|
| `k51natol` | Luyện Nói — Cơ Bản | Talking About My Day (batch 1), #1 Ordering Food, #2 Directions | beg | Updated (+2) |
| `0k2jg92t` | Luyện Nói — Trung Cấp | #3 Introducing, #4 Hometown, #5 Opinions, #6 Story, #7 Sports, #8 Interview | preint-int | New |
| `ur8qvn0c` | Luyện Nói — Nâng Cao | #9 Presenting, #10 Negotiating, #11 Defending, #12 Impromptu | upperint-adv | New |

## Collection IDs (1 existing)

| Collection ID | Title | Series | Status |
|---------------|-------|--------|--------|
| `7i71l2wu` | Luyện Nói | Luyện Nói — Cơ Bản (`k51natol`), Luyện Nói — Trung Cấp (`0k2jg92t`), Luyện Nói — Nâng Cao (`ur8qvn0c`) | Existing |

## Distribution Summary

- **Level**: 2 beginner, 3 preintermediate, 3 intermediate, 2 upperintermediate, 2 advanced
- **Skill focus**: All 12 are speaking_focus
- **Content type**: 11 general ([]), 1 podcast (["podcast"] — Impromptu Speech)

## How Content Was Created

- Each curriculum created via standalone Python script calling `POST https://helloapi.step.is/curriculum/create`
- Series orchestrator script created 2 new series (Luyện Nói — Trung Cấp, Luyện Nói — Nâng Cao), added 2 curriculums to existing Luyện Nói — Cơ Bản series, set display orders, added new series to existing Luyện Nói collection
- All scripts deleted after verification (only this README remains)
- Language: `en` (target), `vi` (user) — bilingual (beginner through upperintermediate), English-only (advanced)

### Curriculum Type in This Batch

| Type | Word Count | Sessions | Key Constraints |
|------|-----------|----------|-----------------|
| speaking_focus (beginner) | 18 words (3×6) | 5 (3 learning + 1 review + 1 final reading) | speakFlashcards + speakReading every learning session, no writingParagraph, pronunciation-focused introAudio, bilingual |
| speaking_focus (preint/int) | 18 words (3×6) | 5 | speakFlashcards + speakReading every learning session, no writingParagraph, bilingual |
| speaking_focus (upperint) | 18 words (3×6) | 5 | speakFlashcards + speakReading every learning session, no writingParagraph, bilingual |
| speaking_focus (advanced) | 18 words (3×6) | 5 | speakFlashcards + speakReading every learning session, no writingParagraph, English-only |

## SQL Queries

```sql
-- Find all batch-05 curriculums by ID
SELECT c.id, c.content->>'title' AS title, c.display_order, c.language, c.user_language,
       c.content->>'contentTypeTags' AS content_type,
       c.created_at
FROM curriculum c
WHERE c.id IN (
    'QAJJ2sZUL3c0tsWV', '3TXcGwGByJJECai7', 'rmTSVijOq1LbYdUx',
    'lnlSt1K9cQjahiis', 'D3Ub6lbI3QcZJZbF', 'GPPdt20hrEABjIjZ',
    'Nm9hUWT8DGIVtRVf', 'IPp6ywp29TaJOd3o', '6JNVxEAKaDHW5d5V',
    'kKp8LSndyBqDsNU1', 'VWokcRfKFhHjcEYv', '4nsJJiDERfBR1V3r'
)
ORDER BY c.display_order;

-- Find all batch-05 series (1 existing + 2 new)
SELECT cs.id, cs.title, cs.description, cs.is_public
FROM curriculum_series cs
WHERE cs.id IN ('k51natol', '0k2jg92t', 'ur8qvn0c')
ORDER BY cs.title;

-- Find batch-05 collection (1 existing)
SELECT cc.id, cc.title, cc.is_public
FROM curriculum_collections cc
WHERE cc.id = '7i71l2wu';

-- Find curriculums within each series (with series membership)
SELECT cs.title AS series_title, c.id, c.content->>'title' AS title, c.display_order
FROM curriculum c
JOIN curriculum_series_items csi ON csi.curriculum_id = c.id
JOIN curriculum_series cs ON cs.id = csi.curriculum_series_id
WHERE csi.curriculum_series_id IN ('k51natol', '0k2jg92t', 'ur8qvn0c')
ORDER BY cs.title, c.display_order;

-- Find series within the collection
SELECT cc.title AS collection_title, cs.id AS series_id, cs.title AS series_title
FROM curriculum_series cs
JOIN curriculum_collection_series ccs ON ccs.curriculum_series_id = cs.id
JOIN curriculum_collections cc ON cc.id = ccs.curriculum_collection_id
WHERE ccs.curriculum_collection_id = '7i71l2wu'
ORDER BY cc.title, cs.title;

-- Verify language homogeneity across series
SELECT * FROM curriculum_series_language_list
WHERE id IN ('k51natol', '0k2jg92t', 'ur8qvn0c');

-- Duplicate check for all batch-05 titles
SELECT id, content->>'title' AS title, created_at
FROM curriculum
WHERE uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'
  AND content->>'title' IN (
    'Ordering Food',
    'Asking for Directions',
    'Introducing Yourself',
    'Describing Your Hometown',
    'Giving Opinions',
    'Telling a Story',
    'Debating Sports Rules',
    'Job Interview Practice',
    'Presenting an Idea',
    'Negotiating a Deal',
    'Defending a Position',
    'Impromptu Speech'
  )
ORDER BY content->>'title', created_at;
```

## Recreation

To recreate this batch: write 12 standalone Python scripts (one per curriculum) following the vi-en-curriculum-expansion spec in `.kiro/specs/vi-en-curriculum-expansion/`. Each script needs hand-written learner-facing content (no templates), structural validation via `validate_curriculum.py`, and API call to `curriculum/create` with `language: "en"`, `userLanguage: "vi"`. Then run an orchestrator to add 2 curriculums to existing Luyện Nói — Cơ Bản series, create 2 new series (Luyện Nói — Trung Cấp, Luyện Nói — Nâng Cao), add new series to existing Luyện Nói collection, and set display orders. All curriculums are speaking_focus (18 words, 3×6, 5 sessions, speakFlashcards + speakReading in every learning session, no writingParagraph). Bilingual for beginner through upperintermediate, English-only for advanced.
