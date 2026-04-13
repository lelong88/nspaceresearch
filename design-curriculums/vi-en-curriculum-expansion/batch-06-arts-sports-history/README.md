# Batch 06 — Arts, Sports, History (12 curriculums)

Vi-en curriculum expansion, batch 6: 12 curriculums covering arts & creativity, sports & fitness, and history & civilization. Mix of balanced_skills and vocab_acquisition across preintermediate through advanced levels.

## Curriculum IDs (12 total)

| # | Title | ID | Level | Skill Focus | Content Type | Topic | Series |
|---|-------|----|-------|-------------|--------------|-------|--------|
| 65 | Street Art Revolution | `jlb8VgloZJr5B5En` | preintermediate | balanced_skills | [] | Arts | Sáng Tạo |
| 66 | Fashion Through the Decades | `fa23o4P5QEK2nF7M` | intermediate | balanced_skills | [] | Arts | Sáng Tạo |
| 67 | Architecture That Changed Cities | `mKaAh9q4pwbl7tBE` | upperintermediate | balanced_skills | [] | Arts | Nghệ Thuật Nâng Cao |
| 68 | Football Legends | `yizq2viFSbnn6olE` | beginner | vocab_acquisition | [] | Sports | Thể Thao Cơ Bản |
| 69 | Olympic History | `sBNrqGMxLvLerNhB` | preintermediate | balanced_skills | [] | Sports | Thể Thao Cơ Bản |
| 70 | Extreme Sports | `KO2VYvsZng79olIT` | intermediate | vocab_acquisition | [] | Sports | Thể Thao Chuyên Sâu |
| 71 | Team Dynamics in Sports | `Z4tyzbWu02YM0Vku` | upperintermediate | balanced_skills | [] | Sports | Thể Thao Chuyên Sâu |
| 72 | Ancient Egypt | `G85YK4Afa8lxd3k4` | preintermediate | vocab_acquisition | [] | History | Lịch Sử Thế Giới |
| 73 | The Silk Road | `ZKAogWwwpAcHQFcM` | intermediate | balanced_skills | [] | History | Lịch Sử Thế Giới |
| 74 | World War II Turning Points | `hNmvpYHzvk2qpTuN` | upperintermediate | balanced_skills | [] | History | Lịch Sử Nâng Cao |
| 75 | Revolutions That Shaped the World | `S8d5ZsViEmV4n91P` | advanced | balanced_skills | [] | History | Lịch Sử Nâng Cao |
| 76 | Photography Basics | `e64w0jzSP18V3WzM` | preintermediate | vocab_acquisition | [] | Arts | Sáng Tạo |

## Series IDs (6 total — all new)

| Series ID | Title | Collection | Curriculums | Levels |
|-----------|-------|------------|-------------|--------|
| `chj86wk9` | Sáng Tạo | Nghệ Thuật & Sáng Tạo | #65 Street Art, #66 Fashion, #76 Photography | preint-int |
| `eul07lvd` | Nghệ Thuật Nâng Cao | Nghệ Thuật & Sáng Tạo | #67 Architecture | upperint |
| `abohljc5` | Thể Thao Cơ Bản | Thể Thao & Sức Khỏe | #68 Football, #69 Olympic | beg-preint |
| `0fodkwcb` | Thể Thao Chuyên Sâu | Thể Thao & Sức Khỏe | #70 Extreme Sports, #71 Team Dynamics | int-upperint |
| `4msmmlpx` | Lịch Sử Thế Giới | Lịch Sử & Văn Minh | #72 Egypt, #73 Silk Road | preint-int |
| `q0bfo63x` | Lịch Sử Nâng Cao | Lịch Sử & Văn Minh | #74 WWII, #75 Revolutions | upperint-adv |

## Collection IDs (3 total — all new)

| Collection ID | Title |
|---------------|-------|
| `4r96ta1c` | Nghệ Thuật & Sáng Tạo |
| `vkabvemz` | Thể Thao & Sức Khỏe |
| `eiconkgc` | Lịch Sử & Văn Minh |

## Distribution Summary

- **Level**: 1 beginner, 4 preintermediate, 3 intermediate, 3 upperintermediate, 1 advanced
- **Skill focus**: 8 balanced_skills, 4 vocab_acquisition
- **Content type**: 12 general ([])
- **Topics**: 4 Arts, 4 Sports, 4 History

## How Content Was Created

- Each curriculum created via standalone Python script calling `POST https://helloapi.step.is/curriculum/create`
- Scripts validated content before upload using `validate_curriculum.py` shared helper
- Series and collections created via `create_batch_06_series.py` orchestrator script
- All scripts deleted after verification (only this README remains)
- Language: `en` (target), `vi` (user) — bilingual (beginner through upperintermediate), English-only (advanced)

### Curriculum Types in This Batch

| Type | Word Count | Sessions | Key Constraints |
|------|-----------|----------|-----------------|
| balanced_skills (preint/int) | 18 words (3×6) | 5 (3 learning + 1 review + 1 final reading) | Standard activity sequence, bilingual |
| balanced_skills (upperint) | 18 words (3×6) | 5 | Bilingual, analytical writingParagraph prompts |
| balanced_skills (advanced) | 18 words (3×6) | 5 | English-only, complex sentences, domain-specific terminology |
| vocab_acquisition (beginner) | 24 words (4×6) | 6 (4 learning + 1 review + 1 final reading) | vocabLevel1-3 every learning session, no writingParagraph, bilingual |
| vocab_acquisition (preint/int) | 24 words (4×6) | 6 | vocabLevel1-3 every learning session, no writingParagraph, bilingual |

## SQL Queries

```sql
-- Find all batch-06 curriculums by ID
SELECT c.id, c.content->>'title' AS title, c.display_order, c.language, c.user_language,
       c.content->>'contentTypeTags' AS content_type,
       c.created_at
FROM curriculum c
WHERE c.id IN (
    'jlb8VgloZJr5B5En', 'fa23o4P5QEK2nF7M', 'mKaAh9q4pwbl7tBE',
    'yizq2viFSbnn6olE', 'sBNrqGMxLvLerNhB', 'KO2VYvsZng79olIT',
    'Z4tyzbWu02YM0Vku', 'G85YK4Afa8lxd3k4', 'ZKAogWwwpAcHQFcM',
    'hNmvpYHzvk2qpTuN', 'S8d5ZsViEmV4n91P', 'e64w0jzSP18V3WzM'
)
ORDER BY c.display_order;

-- Find all batch-06 series
SELECT cs.id, cs.title, cs.description, cs.is_public
FROM curriculum_series cs
WHERE cs.id IN ('chj86wk9', 'eul07lvd', 'abohljc5', '0fodkwcb', '4msmmlpx', 'q0bfo63x')
ORDER BY cs.title;

-- Find all batch-06 collections
SELECT cc.id, cc.title, cc.is_public
FROM curriculum_collections cc
WHERE cc.id IN ('4r96ta1c', 'vkabvemz', 'eiconkgc');

-- Find curriculums within each series (with series membership)
SELECT cs.title AS series_title, c.id, c.content->>'title' AS title, c.display_order
FROM curriculum c
JOIN curriculum_series_items csi ON csi.curriculum_id = c.id
JOIN curriculum_series cs ON cs.id = csi.curriculum_series_id
WHERE csi.curriculum_series_id IN ('chj86wk9', 'eul07lvd', 'abohljc5', '0fodkwcb', '4msmmlpx', 'q0bfo63x')
ORDER BY cs.title, c.display_order;

-- Find series within each collection
SELECT cc.title AS collection_title, cs.id AS series_id, cs.title AS series_title
FROM curriculum_series cs
JOIN curriculum_collection_series ccs ON ccs.curriculum_series_id = cs.id
JOIN curriculum_collections cc ON cc.id = ccs.curriculum_collection_id
WHERE ccs.curriculum_collection_id IN ('4r96ta1c', 'vkabvemz', 'eiconkgc')
ORDER BY cc.title, cs.title;

-- Verify language homogeneity across series
SELECT * FROM curriculum_series_language_list
WHERE id IN ('chj86wk9', 'eul07lvd', 'abohljc5', '0fodkwcb', '4msmmlpx', 'q0bfo63x');

-- Duplicate check for all batch-06 titles
SELECT id, content->>'title' AS title, created_at
FROM curriculum
WHERE uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'
  AND content->>'title' IN (
    'Street Art Revolution',
    'Fashion Through the Decades',
    'Architecture That Changed Cities',
    'Football Legends',
    'Olympic History',
    'Extreme Sports',
    'Team Dynamics in Sports',
    'Ancient Egypt',
    'The Silk Road',
    'World War II Turning Points',
    'Revolutions That Shaped the World',
    'Photography Basics'
  )
ORDER BY content->>'title', created_at;
```

## Recreation

To recreate this batch: write 12 standalone Python scripts (one per curriculum) following the vi-en-curriculum-expansion spec in `.kiro/specs/vi-en-curriculum-expansion/`. Each script needs hand-written learner-facing content (no templates), structural validation via `validate_curriculum.py`, and API call to `curriculum/create` with `language: "en"`, `userLanguage: "vi"`. Then run an orchestrator to create 6 series (Sáng Tạo, Nghệ Thuật Nâng Cao, Thể Thao Cơ Bản, Thể Thao Chuyên Sâu, Lịch Sử Thế Giới, Lịch Sử Nâng Cao), create 3 collections (Nghệ Thuật & Sáng Tạo, Thể Thao & Sức Khỏe, Lịch Sử & Văn Minh), wire curriculums to series, set display orders, and add series to collections. Mix of balanced_skills (18 words, 3×6, 5 sessions) and vocab_acquisition (24 words, 4×6, 6 sessions). Bilingual for beginner through upperintermediate, English-only for advanced.
