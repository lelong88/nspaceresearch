# Batch 04 — Podcast & Story Content (12 curriculums)

Vi-en curriculum expansion, batch 4: 7 podcast-based balanced_skills curriculums (beginner through upperintermediate) and 5 story-based reader curriculums (beginner through advanced). Topics: Daily life, Food, Psychology, Sports, Arts, History, Law.

## Curriculum IDs (12 total)

| # | Title | ID | Level | Skill Focus | Content Type | Topic |
|---|-------|----|-------|-------------|--------------|-------|
| 1 | Easy English: Morning Routines | `dpgKO7C0EOUkW82c` | beginner | balanced_skills | ["podcast"] | Daily life |
| 2 | Easy English: At the Market | `2kfWqXjUslTWNs1N` | beginner | balanced_skills | ["podcast"] | Food |
| 3 | TED-Ed: Why We Sleep | `OS3IWpnuKS2Ikg3D` | preintermediate | balanced_skills | ["podcast"] | Psychology |
| 4 | TED-Ed: The History of Chocolate | `M4qeD5Dkrh0IYo3S` | preintermediate | balanced_skills | ["podcast"] | Food |
| 5 | Freakonomics: Hidden Side of Sports | `fBfwBKS1rOjXUR0i` | intermediate | balanced_skills | ["podcast"] | Sports |
| 6 | Radiolab: Colors | `6u376tO0gWw0tUPm` | intermediate | balanced_skills | ["podcast"] | Arts |
| 7 | 99% Invisible: Design of Cities | `k7UTFR7lh5qLRWNq` | upperintermediate | balanced_skills | ["podcast"] | Arts |
| 8 | The Lost Kite | `Zjns663zWPV8yfYh` | beginner | reader | ["story"] | Daily life |
| 9 | The Market Thief | `vD9WLFnjz5zC2EwY` | preintermediate | reader | ["story"] | Daily life |
| 10 | The Photographer's Eye | `zpTSYxWexFx6zlpV` | intermediate | reader | ["story"] | Arts |
| 11 | The Last Samurai's Garden | `Js3iwIpkLVNCOT0c` | upperintermediate | reader | ["story"] | History |
| 12 | The Interpreter | `Fy4ExwGn2azTm551` | advanced | reader | ["story"] | Law |

## Series IDs (4 total — 3 new, 1 existing updated)

| Series ID | Title | Curriculums | Levels | Status |
|-----------|-------|-------------|--------|--------|
| `ktvlz24y` | Podcast — Cơ Bản | #1 Morning Routines, #2 Market, #3 Sleep, #4 Chocolate | beg-preint | New |
| `6u511q5v` | Podcast — Nâng Cao | #5 Sports, #6 Colors, #7 Cities | int-upperint | New |
| `ztfkvruv` | Truyện Ngắn — Cơ Bản | Bicycle (batch 1), #8 Lost Kite, #9 Market Thief | beg-preint | Updated (+2) |
| `fq9zvs5p` | Truyện Ngắn — Nâng Cao | #10 Photographer, #11 Samurai, #12 Interpreter | int-adv | New |

## Collection IDs (1 new, 1 existing updated)

| Collection ID | Title | Series | Status |
|---------------|-------|--------|--------|
| `pm0hs5ks` | Podcast | Podcast — Cơ Bản (`ktvlz24y`), Podcast — Nâng Cao (`6u511q5v`) | New |
| `fn9q77oq` | Truyện Ngắn | Truyện Ngắn — Cơ Bản (`ztfkvruv`), Truyện Ngắn — Nâng Cao (`fq9zvs5p`) | Updated (+1 series) |

## Series Descriptions & Tones

| Series | Description | Tone |
|--------|-------------|------|
| Podcast — Cơ Bản | Bạn đang đeo tai nghe trên xe buýt — và bỗng nhận ra mình hiểu được cả đoạn hội thoại tiếng Anh về buổi sáng, chợ búa, giấc ngủ, sô-cô-la. | vivid_scenario |
| Podcast — Nâng Cao | Ba podcast, ba góc nhìn — từ kinh tế thể thao đến khoa học màu sắc đến thiết kế đô thị. Tiếng Anh trung-cao cấp qua nội dung thật. | bold_declaration |
| Truyện Ngắn — Nâng Cao | Một nhiếp ảnh gia, một samurai, một phiên dịch viên — ba câu chuyện tiếng Anh trung-cao cấp giúp bạn đọc nhanh hơn mà không cần từ điển. | surprising_fact |

Note: Truyện Ngắn — Cơ Bản description was set in batch 01 (empathetic_observation tone).

## Distribution Summary

- **Level**: 3 beginner, 2 preintermediate, 3 intermediate, 2 upperintermediate, 1 advanced (1 curriculum spans advanced — The Interpreter)
- **Skill focus**: 7 balanced_skills, 5 reader
- **Content type**: 7 podcast (["podcast"]), 5 story (["story"])
- **Topics**: 2 Daily life, 2 Food, 2 Arts, 1 Psychology, 1 Sports, 1 History, 1 Law

## How Content Was Created

- Each curriculum created via standalone Python script calling `POST https://helloapi.step.is/curriculum/create`
- Scripts validated content before upload using `validate_curriculum.py` shared helper
- Series and collections created via `create_batch_04_series.py` orchestrator script
- All scripts deleted after verification (only this README remains)
- Language: `en` (target), `vi` (user) — bilingual (beginner through upperintermediate), English-only (advanced)
- Created: April 11, 2026

### Curriculum Types in This Batch

| Type | Word Count | Sessions | Key Constraints |
|------|-----------|----------|-----------------|
| balanced_skills (beginner) | 12 words (2×6) | 4 (2 learning + 1 review + 1 final reading) | No writingParagraph, no vocabLevel3, simple sentences <15 words avg |
| balanced_skills (preint/int) | 18 words (3×6) | 5 (3 learning + 1 review + 1 final reading) | writingParagraph in S5, bilingual |
| balanced_skills (upperint) | 18 words (3×6) | 5 | Bilingual, writingParagraph requires analytical responses |
| reader (beginner) | 12 words | 4 | readAlong every session, cohesive narrative, final reading ≥500 words |
| reader (preint/int) | 12-18 words | 4 | readAlong every session, story-based narrative |
| reader (upperint) | 12-18 words | 4 | Bilingual, longer passages, cohesive narrative |
| reader (advanced) | 12-18 words | 4 | English-only, complex vocabulary, cohesive narrative |

## SQL Queries

```sql
-- Find all batch-04 curriculums by ID
SELECT c.id, c.content->>'title' AS title, c.display_order, c.language, c.user_language,
       c.content->>'contentTypeTags' AS content_type,
       c.created_at
FROM curriculum c
WHERE c.id IN (
    'dpgKO7C0EOUkW82c', '2kfWqXjUslTWNs1N', 'OS3IWpnuKS2Ikg3D',
    'M4qeD5Dkrh0IYo3S', 'fBfwBKS1rOjXUR0i', '6u376tO0gWw0tUPm',
    'k7UTFR7lh5qLRWNq', 'Zjns663zWPV8yfYh', 'vD9WLFnjz5zC2EwY',
    'zpTSYxWexFx6zlpV', 'Js3iwIpkLVNCOT0c', 'Fy4ExwGn2azTm551'
)
ORDER BY c.display_order;

-- Find all batch-04 series (3 new + 1 existing)
SELECT cs.id, cs.title, cs.description, cs.is_public
FROM curriculum_series cs
WHERE cs.id IN ('ktvlz24y', '6u511q5v', 'ztfkvruv', 'fq9zvs5p')
ORDER BY cs.title;

-- Find batch-04 collections (1 new + 1 existing)
SELECT cc.id, cc.title, cc.is_public
FROM curriculum_collections cc
WHERE cc.id IN ('pm0hs5ks', 'fn9q77oq');

-- Find curriculums within each series (with series membership)
SELECT cs.title AS series_title, c.id, c.content->>'title' AS title, c.display_order
FROM curriculum c
JOIN curriculum_series_items csi ON csi.curriculum_id = c.id
JOIN curriculum_series cs ON cs.id = csi.curriculum_series_id
WHERE csi.curriculum_series_id IN ('ktvlz24y', '6u511q5v', 'ztfkvruv', 'fq9zvs5p')
ORDER BY cs.title, c.display_order;

-- Find series within each collection
SELECT cc.title AS collection_title, cs.id AS series_id, cs.title AS series_title
FROM curriculum_series cs
JOIN curriculum_collection_series ccs ON ccs.curriculum_series_id = cs.id
JOIN curriculum_collections cc ON cc.id = ccs.curriculum_collection_id
WHERE ccs.curriculum_collection_id IN ('pm0hs5ks', 'fn9q77oq')
ORDER BY cc.title, cs.title;

-- Verify language homogeneity across series
SELECT * FROM curriculum_series_language_list
WHERE id IN ('ktvlz24y', '6u511q5v', 'ztfkvruv', 'fq9zvs5p');

-- Duplicate check for all batch-04 titles
SELECT id, content->>'title' AS title, created_at
FROM curriculum
WHERE uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'
  AND content->>'title' IN (
    'Easy English: Morning Routines',
    'Easy English: At the Market',
    'TED-Ed: Why We Sleep',
    'TED-Ed: The History of Chocolate',
    'Freakonomics: Hidden Side of Sports',
    'Radiolab: Colors',
    '99% Invisible: Design of Cities',
    'The Lost Kite',
    'The Market Thief',
    'The Photographer''s Eye',
    'The Last Samurai''s Garden',
    'The Interpreter'
  )
ORDER BY content->>'title', created_at;
```

## Recreation

To recreate this batch: write 12 standalone Python scripts (7 podcast + 5 story, one per curriculum) following the vi-en-curriculum-expansion spec in `.kiro/specs/vi-en-curriculum-expansion/`. Each script needs hand-written learner-facing content (no templates), structural validation via `validate_curriculum.py`, and API call to `curriculum/create` with `language: "en"`, `userLanguage: "vi"`. Then run an orchestrator to create 3 new series (Podcast Cơ Bản, Podcast Nâng Cao, Truyện Ngắn Nâng Cao), add 2 curriculums to existing Truyện Ngắn Cơ Bản series, create 1 new Podcast collection, add story advanced series to existing Truyện Ngắn collection, and set display orders. Podcast curriculums are balanced_skills (beginner through upperintermediate, all bilingual). Story curriculums are reader type (beginner through advanced, bilingual except advanced which is English-only).
