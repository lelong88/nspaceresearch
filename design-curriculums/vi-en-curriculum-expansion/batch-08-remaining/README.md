# Batch 08 — Remaining Gaps (12 curriculums)

Vi-en curriculum expansion, batch 8: 12 curriculums covering tech/digital life, Vietnamese culture, daily life, relationships, music, movie, and story. Mix of balanced_skills, vocab_acquisition, and reader across beginner through advanced levels.

## Curriculum IDs (12 total)

| # | Title | ID | Level | Skill Focus | Content Type | Topic | Series |
|---|-------|----|-------|-------------|--------------|-------|--------|
| 89 | Social Media Impact | `3qkSs0QPyiUGSa3O` | preintermediate | balanced_skills | [] | Tech/digital life | Thế Giới Số |
| 90 | Cybersecurity Basics | `pkBkGLMB5fYAYpaD` | intermediate | balanced_skills | [] | Tech/digital life | Thế Giới Số |
| 91 | Digital Privacy | `7Ee1r8QAYTtpgQCb` | upperintermediate | balanced_skills | [] | Tech/digital life | Công Nghệ Nâng Cao |
| 92 | AI Ethics | `MfoMo2NXP0hk4UUp` | advanced | balanced_skills | [] | Tech/digital life | Công Nghệ Nâng Cao |
| 93 | Vietnamese Festivals | `tGZnQkSDmnDS6KWY` | preintermediate | balanced_skills | [] | Vietnamese culture | Việt Nam Qua Tiếng Anh — Nâng Cao |
| 94 | Vietnamese History in English | `kvuLob49xUreF5oi` | intermediate | balanced_skills | [] | Vietnamese culture | Việt Nam Qua Tiếng Anh — Nâng Cao |
| 95 | Banking & Money | `20TQ86uZFoCH5CYb` | beginner | balanced_skills | [] | Daily life | Bước Đầu Tiên |
| 96 | Conflict Resolution | `vIBGcoPkzkZk0kBD` | intermediate | vocab_acquisition | [] | Relationships | Giao Tiếp Sâu |
| 97 | Broken Strings — James Morrison | `ERf7E4BNpJN2hgRC` | intermediate | balanced_skills | ["music"] | Relationships | Âm Nhạc — Nâng Cao |
| 98 | Lose Yourself — Eminem | `nkjlFytVbqqmJmRv` | upperintermediate | balanced_skills | ["music"] | Sports | Âm Nhạc — Nâng Cao |
| 99 | The Shawshank Redemption | `UdVrVb7XeJ2g2mjL` | advanced | balanced_skills | ["movie"] | Law | Phim Ảnh — Nâng Cao |
| 100 | The Garden of Small Things | `uWHBTCJEaZ23nzAu` | upperintermediate | reader | ["story"] | Food | Truyện Ngắn — Nâng Cao |

## Series IDs (8 total — 4 new, 4 existing)

| Series ID | Title | Collection | Curriculums | Levels | Status |
|-----------|-------|------------|-------------|--------|--------|
| `zdtzggcy` | Thế Giới Số | Công Nghệ & Đời Sống Số | #89 Social Media Impact, #90 Cybersecurity Basics | preint-int | NEW |
| `h4012dzf` | Công Nghệ Nâng Cao | Công Nghệ & Đời Sống Số | #91 Digital Privacy, #92 AI Ethics | upperint-adv | NEW |
| `faoghgja` | Việt Nam Qua Tiếng Anh — Nâng Cao | Văn Hóa Việt Nam Bằng Tiếng Anh | #93 Vietnamese Festivals, #94 Vietnamese History | preint-int | NEW |
| `skmippbo` | Giao Tiếp Sâu | Quan Hệ & Kỹ Năng Xã Hội | #96 Conflict Resolution | int | NEW |
| `qxobskn8` | Bước Đầu Tiên | Cuộc Sống Hàng Ngày | + #95 Banking & Money | beginner | EXISTING (batch-01) |
| `5is05njr` | Âm Nhạc — Nâng Cao | Âm Nhạc | + #97 Broken Strings, #98 Lose Yourself | int-upperint | EXISTING (batch-03) |
| `hmsbjryc` | Phim Ảnh — Nâng Cao | Phim Ảnh | + #99 The Shawshank Redemption | int-adv | EXISTING (batch-03) |
| `fq9zvs5p` | Truyện Ngắn — Nâng Cao | Truyện Ngắn | + #100 The Garden of Small Things | int-adv | EXISTING (batch-04) |

## Collection IDs (7 total — 1 new, 6 existing)

| Collection ID | Title | Status |
|---------------|-------|--------|
| `cayh4ldy` | Công Nghệ & Đời Sống Số | NEW |
| `5z2gl6ca` | Cuộc Sống Hàng Ngày | EXISTING (batch-01) |
| `kg0ug56u` | Quan Hệ & Kỹ Năng Xã Hội | EXISTING (batch-01) |
| `n0p37me0` | Văn Hóa Việt Nam Bằng Tiếng Anh | EXISTING (batch-01) |
| `lfi1xjbb` | Âm Nhạc | EXISTING (batch-03) |
| `0utj9i9f` | Phim Ảnh | EXISTING (batch-03) |
| `fn9q77oq` | Truyện Ngắn | EXISTING (batch-04) |

## Distribution Summary

- **Level**: 1 beginner, 2 preintermediate, 3 intermediate, 2 upperintermediate, 2 advanced (+ 2 reader/music at int/upperint)
- **Skill focus**: 10 balanced_skills, 1 vocab_acquisition, 1 reader
- **Content type**: 8 general ([]), 2 music (["music"]), 1 movie (["movie"]), 1 story (["story"])
- **Topics**: 4 Tech/digital life, 2 Vietnamese culture, 1 Daily life, 1 Relationships, 1 Sports, 1 Law, 1 Food, 1 Relationships (music)

## How Content Was Created

- Each curriculum created via standalone Python script calling `POST https://helloapi.step.is/curriculum/create`
- Scripts validated content before upload using `validate_curriculum.py` shared helper
- Series and collections created via `create_batch_08_series.py` orchestrator script
- All scripts deleted after verification (only this README remains)
- Language: `en` (target), `vi` (user) — bilingual (beginner through upperintermediate), English-only (advanced)

### Curriculum Types in This Batch

| Type | Word Count | Sessions | Key Constraints |
|------|-----------|----------|-----------------|
| balanced_skills (beginner) | 12 words (2×6) | 4 (2 learning + 1 review + 1 final reading) | No writingParagraph, no vocabLevel3, simple sentences <15 words avg |
| balanced_skills (preint/int) | 18 words (3×6) | 5 (3 learning + 1 review + 1 final reading) | Standard activity sequence, bilingual |
| balanced_skills (upperint) | 18 words (3×6) | 5 | Bilingual, analytical writingParagraph prompts |
| balanced_skills (advanced) | 18 words (3×6) | 5 | English-only, complex sentences, domain-specific terminology |
| vocab_acquisition (int) | 24 words (4×6) | 6 (4 learning + 1 review + 1 final reading) | vocabLevel1-3 every learning session, no writingParagraph, bilingual |
| reader (upperint) | 12-18 words | 4 | readAlong every session, cohesive narrative, final reading ≥500 words |

## SQL Queries

```sql
-- Find all batch-08 curriculums by ID
SELECT c.id, c.content->>'title' AS title, c.display_order, c.language, c.user_language,
       c.content->>'contentTypeTags' AS content_type,
       c.created_at
FROM curriculum c
WHERE c.id IN (
    '3qkSs0QPyiUGSa3O', 'pkBkGLMB5fYAYpaD', '7Ee1r8QAYTtpgQCb',
    'MfoMo2NXP0hk4UUp', 'tGZnQkSDmnDS6KWY', 'kvuLob49xUreF5oi',
    '20TQ86uZFoCH5CYb', 'vIBGcoPkzkZk0kBD', 'ERf7E4BNpJN2hgRC',
    'nkjlFytVbqqmJmRv', 'UdVrVb7XeJ2g2mjL', 'uWHBTCJEaZ23nzAu'
)
ORDER BY c.display_order;

-- Find all batch-08 series (new)
SELECT cs.id, cs.title, cs.description, cs.is_public
FROM curriculum_series cs
WHERE cs.id IN ('zdtzggcy', 'h4012dzf', 'faoghgja', 'skmippbo')
ORDER BY cs.title;

-- Find batch-08 collection (new)
SELECT cc.id, cc.title, cc.is_public
FROM curriculum_collections cc
WHERE cc.id = 'cayh4ldy';

-- Find curriculums within each series (with series membership)
SELECT cs.title AS series_title, c.id, c.content->>'title' AS title, c.display_order
FROM curriculum c
JOIN curriculum_series_items csi ON csi.curriculum_id = c.id
JOIN curriculum_series cs ON cs.id = csi.curriculum_series_id
WHERE csi.curriculum_series_id IN ('zdtzggcy', 'h4012dzf', 'faoghgja', 'skmippbo', 'qxobskn8', '5is05njr', 'hmsbjryc', 'fq9zvs5p')
ORDER BY cs.title, c.display_order;

-- Find series within each collection
SELECT cc.title AS collection_title, cs.id AS series_id, cs.title AS series_title
FROM curriculum_series cs
JOIN curriculum_collection_series ccs ON ccs.curriculum_series_id = cs.id
JOIN curriculum_collections cc ON cc.id = ccs.curriculum_collection_id
WHERE ccs.curriculum_collection_id IN ('cayh4ldy', '5z2gl6ca', 'kg0ug56u', 'n0p37me0', 'lfi1xjbb', '0utj9i9f', 'fn9q77oq')
ORDER BY cc.title, cs.title;

-- Verify language homogeneity across new series
SELECT * FROM curriculum_series_language_list
WHERE id IN ('zdtzggcy', 'h4012dzf', 'faoghgja', 'skmippbo');

-- Duplicate check for all batch-08 titles
SELECT id, content->>'title' AS title, created_at
FROM curriculum
WHERE uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'
  AND content->>'title' IN (
    'Social Media Impact',
    'Cybersecurity Basics',
    'Digital Privacy',
    'AI Ethics',
    'Vietnamese Festivals',
    'Vietnamese History in English',
    'Banking & Money',
    'Conflict Resolution',
    'Broken Strings — James Morrison',
    'Lose Yourself — Eminem',
    'The Shawshank Redemption',
    'The Garden of Small Things'
  )
ORDER BY content->>'title', created_at;
```

## Recreation

To recreate this batch: write 12 standalone Python scripts (one per curriculum) following the vi-en-curriculum-expansion spec in `.kiro/specs/vi-en-curriculum-expansion/`. Each script needs hand-written learner-facing content (no templates), structural validation via `validate_curriculum.py`, and API call to `curriculum/create` with `language: "en"`, `userLanguage: "vi"`. Then run an orchestrator to create 4 new series (Thế Giới Số, Công Nghệ Nâng Cao, Việt Nam Qua Tiếng Anh — Nâng Cao, Giao Tiếp Sâu), create 1 new collection (Công Nghệ & Đời Sống Số), add curriculums to 4 existing series (Bước Đầu Tiên, Âm Nhạc — Nâng Cao, Phim Ảnh — Nâng Cao, Truyện Ngắn — Nâng Cao), wire new series to new and existing collections, and set display orders. Mix of balanced_skills (12-18 words), vocab_acquisition (24 words), and reader (12-18 words). Bilingual for beginner through upperintermediate, English-only for advanced.
