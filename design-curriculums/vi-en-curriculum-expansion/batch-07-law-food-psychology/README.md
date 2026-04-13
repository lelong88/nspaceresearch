# Batch 07 — Law, Food, Psychology (12 curriculums)

Vi-en curriculum expansion, batch 7: 12 curriculums covering law & justice, food & gastronomy, and psychology & emotions. Mix of balanced_skills and vocab_acquisition across beginner through advanced levels.

## Curriculum IDs (12 total)

| # | Title | ID | Level | Skill Focus | Content Type | Topic | Series |
|---|-------|----|-------|-------------|--------------|-------|--------|
| 77 | Courtroom English | `bSdL8CRdpTqbdSav` | intermediate | balanced_skills | [] | Law | Luật & Đạo Đức |
| 78 | Human Rights | `ebYZGzq0qVhrChSW` | upperintermediate | balanced_skills | [] | Law | Luật & Đạo Đức |
| 79 | Ethics in Everyday Life | `X9ozHV0nvsKsQyCw` | advanced | balanced_skills | [] | Law | Công Lý |
| 80 | Crime & Punishment | `1EjklsMli1qQIgJP` | advanced | balanced_skills | [] | Law | Công Lý |
| 81 | World Cuisines | `V7FGmQSJC8PVyK3H` | preintermediate | balanced_skills | [] | Food | Ẩm Thực Thế Giới |
| 82 | Food Science | `d2jB7kze1Gh3VLQ5` | intermediate | balanced_skills | [] | Food | Ẩm Thực Thế Giới |
| 83 | Restaurant Culture | `WjkKzhEW5ju7FbBQ` | beginner | vocab_acquisition | [] | Food | Ẩm Thực Cơ Bản |
| 84 | Emotional Intelligence | `fqcDButo95moyUht` | preintermediate | balanced_skills | [] | Psychology | Tâm Lý Học |
| 85 | Cognitive Biases | `aSZMmdRiGzm6swFL` | intermediate | balanced_skills | [] | Psychology | Tâm Lý Học |
| 86 | Stress Management | `ZhnmlKsBCPl2WO74` | upperintermediate | balanced_skills | [] | Psychology | Tâm Lý Nâng Cao |
| 87 | Motivation Science | `FaGNlriy1sVXR1Xh` | advanced | balanced_skills | [] | Psychology | Tâm Lý Nâng Cao |
| 88 | Food Sustainability | `r5AWcue2qeMMikW5` | upperintermediate | vocab_acquisition | [] | Food | Ẩm Thực Bền Vững |

## Series IDs (7 total — 5 new, 1 existing, 1 existing)

| Series ID | Title | Collection | Curriculums | Levels | Status |
|-----------|-------|------------|-------------|--------|--------|
| `rcb8hi5t` | Luật & Đạo Đức | Luật Pháp & Công Lý | #77 Courtroom English, #78 Human Rights | int-upperint | NEW |
| `11n8xqaj` | Công Lý | Luật Pháp & Công Lý | #79 Ethics, #80 Crime & Punishment | adv | NEW |
| `3ouiua4h` | Ẩm Thực Cơ Bản | Ẩm Thực & Văn Hóa Ăn Uống | #83 Restaurant Culture | beginner | EXISTING (batch-01) |
| `zpz2x0i6` | Ẩm Thực Thế Giới | Ẩm Thực & Văn Hóa Ăn Uống | #81 World Cuisines, #82 Food Science | preint-int | NEW |
| `y0iznhcb` | Ẩm Thực Bền Vững | Ẩm Thực & Văn Hóa Ăn Uống | #88 Food Sustainability | upperint | NEW |
| `3ucf47g9` | Tâm Lý Học | Tâm Lý & Cảm Xúc | #84 Emotional Intelligence, #85 Cognitive Biases | preint-int | NEW |
| `327ev4ii` | Tâm Lý Nâng Cao | Tâm Lý & Cảm Xúc | #86 Stress Management, #87 Motivation Science | upperint-adv | NEW |

## Collection IDs (3 total — 2 new, 1 existing)

| Collection ID | Title | Status |
|---------------|-------|--------|
| `qld67kxb` | Luật Pháp & Công Lý | NEW |
| `erbl74ej` | Ẩm Thực & Văn Hóa Ăn Uống | EXISTING (batch-01) |
| `xtuzctz9` | Tâm Lý & Cảm Xúc | NEW |

## Distribution Summary

- **Level**: 1 beginner, 2 preintermediate, 3 intermediate, 3 upperintermediate, 3 advanced
- **Skill focus**: 10 balanced_skills, 2 vocab_acquisition
- **Content type**: 12 general ([])
- **Topics**: 4 Law, 4 Food, 4 Psychology

## How Content Was Created

- Each curriculum created via standalone Python script calling `POST https://helloapi.step.is/curriculum/create`
- Scripts validated content before upload using `validate_curriculum.py` shared helper
- Series and collections created via `create_batch_07_series.py` orchestrator script
- All scripts deleted after verification (only this README remains)
- Language: `en` (target), `vi` (user) — bilingual (beginner through upperintermediate), English-only (advanced)

### Curriculum Types in This Batch

| Type | Word Count | Sessions | Key Constraints |
|------|-----------|----------|-----------------|
| balanced_skills (preint/int) | 18 words (3×6) | 5 (3 learning + 1 review + 1 final reading) | Standard activity sequence, bilingual |
| balanced_skills (upperint) | 18 words (3×6) | 5 | Bilingual, analytical writingParagraph prompts |
| balanced_skills (advanced) | 18 words (3×6) | 5 | English-only, complex sentences, domain-specific terminology |
| vocab_acquisition (beginner) | 24 words (4×6) | 6 (4 learning + 1 review + 1 final reading) | vocabLevel1-3 every learning session, no writingParagraph, bilingual |
| vocab_acquisition (upperint) | 24 words (4×6) | 6 | vocabLevel1-3 every learning session, no writingParagraph, bilingual |

## SQL Queries

```sql
-- Find all batch-07 curriculums by ID
SELECT c.id, c.content->>'title' AS title, c.display_order, c.language, c.user_language,
       c.content->>'contentTypeTags' AS content_type,
       c.created_at
FROM curriculum c
WHERE c.id IN (
    'bSdL8CRdpTqbdSav', 'ebYZGzq0qVhrChSW', 'X9ozHV0nvsKsQyCw',
    '1EjklsMli1qQIgJP', 'V7FGmQSJC8PVyK3H', 'd2jB7kze1Gh3VLQ5',
    'WjkKzhEW5ju7FbBQ', 'fqcDButo95moyUht', 'aSZMmdRiGzm6swFL',
    'ZhnmlKsBCPl2WO74', 'FaGNlriy1sVXR1Xh', 'r5AWcue2qeMMikW5'
)
ORDER BY c.display_order;

-- Find all batch-07 series
SELECT cs.id, cs.title, cs.description, cs.is_public
FROM curriculum_series cs
WHERE cs.id IN ('rcb8hi5t', '11n8xqaj', '3ouiua4h', 'zpz2x0i6', 'y0iznhcb', '3ucf47g9', '327ev4ii')
ORDER BY cs.title;

-- Find all batch-07 collections
SELECT cc.id, cc.title, cc.is_public
FROM curriculum_collections cc
WHERE cc.id IN ('qld67kxb', 'erbl74ej', 'xtuzctz9');

-- Find curriculums within each series (with series membership)
SELECT cs.title AS series_title, c.id, c.content->>'title' AS title, c.display_order
FROM curriculum c
JOIN curriculum_series_items csi ON csi.curriculum_id = c.id
JOIN curriculum_series cs ON cs.id = csi.curriculum_series_id
WHERE csi.curriculum_series_id IN ('rcb8hi5t', '11n8xqaj', '3ouiua4h', 'zpz2x0i6', 'y0iznhcb', '3ucf47g9', '327ev4ii')
ORDER BY cs.title, c.display_order;

-- Find series within each collection
SELECT cc.title AS collection_title, cs.id AS series_id, cs.title AS series_title
FROM curriculum_series cs
JOIN curriculum_collection_series ccs ON ccs.curriculum_series_id = cs.id
JOIN curriculum_collections cc ON cc.id = ccs.curriculum_collection_id
WHERE ccs.curriculum_collection_id IN ('qld67kxb', 'erbl74ej', 'xtuzctz9')
ORDER BY cc.title, cs.title;

-- Verify language homogeneity across series
SELECT * FROM curriculum_series_language_list
WHERE id IN ('rcb8hi5t', '11n8xqaj', '3ouiua4h', 'zpz2x0i6', 'y0iznhcb', '3ucf47g9', '327ev4ii');

-- Duplicate check for all batch-07 titles
SELECT id, content->>'title' AS title, created_at
FROM curriculum
WHERE uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'
  AND content->>'title' IN (
    'Courtroom English',
    'Human Rights',
    'Ethics in Everyday Life',
    'Crime & Punishment',
    'World Cuisines',
    'Food Science',
    'Restaurant Culture',
    'Emotional Intelligence',
    'Cognitive Biases',
    'Stress Management',
    'Motivation Science',
    'Food Sustainability'
  )
ORDER BY content->>'title', created_at;
```

## Recreation

To recreate this batch: write 12 standalone Python scripts (one per curriculum) following the vi-en-curriculum-expansion spec in `.kiro/specs/vi-en-curriculum-expansion/`. Each script needs hand-written learner-facing content (no templates), structural validation via `validate_curriculum.py`, and API call to `curriculum/create` with `language: "en"`, `userLanguage: "vi"`. Then run an orchestrator to create 5 new series (Luật & Đạo Đức, Công Lý, Ẩm Thực Thế Giới, Ẩm Thực Bền Vững, Tâm Lý Học, Tâm Lý Nâng Cao), reuse 1 existing series (Ẩm Thực Cơ Bản from batch-01), create 2 new collections (Luật Pháp & Công Lý, Tâm Lý & Cảm Xúc), reuse 1 existing collection (Ẩm Thực & Văn Hóa Ăn Uống from batch-01), wire curriculums to series, set display orders, and add series to collections. Mix of balanced_skills (18 words, 3×6, 5 sessions) and vocab_acquisition (24 words, 4×6, 6 sessions). Bilingual for beginner through upperintermediate, English-only for advanced.
