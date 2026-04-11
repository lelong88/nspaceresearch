# Batch 03 — Movie & Music Content (12 curriculums)

Vi-en curriculum expansion, batch 3: 12 balanced_skills curriculums across 4 difficulty levels (beginner through upperintermediate) using movie and music content. Topics: Psychology, Vietnamese culture, Relationships, Food, Tech, Law, History, Arts.

## Curriculum IDs (12 total)

| # | Title | ID | Level | Skill Focus | Content Type | Topic |
|---|-------|----|-------|-------------|--------------|-------|
| 1 | Inside Out 2 — Cảm Xúc Bên Trong | `nhozU6UE3Ok8ecuY` | beginner | balanced_skills | ["movie"] | Psychology |
| 2 | Coco — Gia Đình Và Âm Nhạc | `uQmO5rKAWe2gFJZX` | beginner | balanced_skills | ["movie"] | Vietnamese culture |
| 3 | The Pursuit of Happyness — Hành Trình Theo Đuổi Hạnh Phúc | `JveWZZJHP0MGoAqp` | preintermediate | balanced_skills | ["movie"] | Relationships |
| 4 | Ratatouille — Chú Chuột Đầu Bếp | `8mWOHy2AMtlmLcb0` | preintermediate | balanced_skills | ["movie"] | Food |
| 5 | The Social Network — Mạng Xã Hội Và Cái Giá Của Tham Vọng | `L9FqtIA4X7pHDfZm` | intermediate | balanced_skills | ["movie"] | Tech |
| 6 | 12 Angry Men — Mười Hai Người Đàn Ông Giận Dữ Và Sức Mạnh Của Một Tiếng Nói | `cNnm61yWEPFlWjIZ` | intermediate | balanced_skills | ["movie"] | Law |
| 7 | Inception — Giấc Mơ Trong Giấc Mơ Và Tâm Lý Của Sự Buông Bỏ | `ESDCO9VLePpLs1Yp` | upperintermediate | balanced_skills | ["movie"] | Psychology |
| 8 | Count on Me — Bruno Mars — Tình Bạn Đích Thực | `prq8RbajcClXXVFl` | beginner | balanced_skills | ["music"] | Relationships |
| 9 | Happy — Pharrell Williams — Sức Mạnh Của Niềm Vui | `oUjA2tp67D7S4bW2` | beginner | balanced_skills | ["music"] | Psychology |
| 10 | Viva La Vida — Coldplay — Khi Vinh Quang Tàn Phai | `rClx0i45niliAGgO` | preintermediate | balanced_skills | ["music"] | History |
| 11 | Imagine — John Lennon — Thế Giới Không Biên Giới | `zl0mmNlY1MxQ5De7` | preintermediate | balanced_skills | ["music"] | Law |
| 12 | Bohemian Rhapsody — Queen — Nghệ Thuật Phá Vỡ Mọi Quy Tắc | `qmm4KNgs3MO0Iy01` | intermediate | balanced_skills | ["music"] | Arts |

## Series IDs (4 total)

| Series ID | Title | Curriculums | Levels |
|-----------|-------|-------------|--------|
| `e9xt62lc` | Phim Ảnh — Cơ Bản | #1 Inside Out 2, #2 Coco, #3 Pursuit of Happyness, #4 Ratatouille | beg-preint |
| `hmsbjryc` | Phim Ảnh — Nâng Cao | #5 Social Network, #6 12 Angry Men, #7 Inception | int-upperint |
| `uhz1ytip` | Âm Nhạc — Cơ Bản | #8 Count on Me, #9 Happy, #10 Viva La Vida, #11 Imagine | beg-preint |
| `5is05njr` | Âm Nhạc — Nâng Cao | #12 Bohemian Rhapsody | int (more in batch 8: Broken Strings int, Lose Yourself upperint) |

## Collection IDs (2 new)

| Collection ID | Title | Series |
|---------------|-------|--------|
| `0utj9i9f` | Phim Ảnh | Phim Ảnh — Cơ Bản (`e9xt62lc`), Phim Ảnh — Nâng Cao (`hmsbjryc`) |
| `lfi1xjbb` | Âm Nhạc | Âm Nhạc — Cơ Bản (`uhz1ytip`), Âm Nhạc — Nâng Cao (`5is05njr`) |

## Series Descriptions & Tones

| Series | Description | Tone |
|--------|-------------|------|
| Phim Ảnh — Cơ Bản | Bạn đang ngồi trong rạp, đèn vừa tắt — và từ vựng tiếng Anh bắt đầu sáng lên qua Inside Out 2, Coco, The Pursuit of Happyness, Ratatouille. | vivid_scenario |
| Phim Ảnh — Nâng Cao | Ba bộ phim, ba thế giới — từ startup công nghệ đến phòng xử án đến giấc mơ nhiều tầng. Tiếng Anh trung-cao cấp qua điện ảnh kinh điển. | bold_declaration |
| Âm Nhạc — Cơ Bản | Có những bài hát bạn đã nghe trăm lần mà chưa hiểu hết lời — bốn bài học này giúp bạn vừa hát vừa học từ vựng tiếng Anh tự nhiên nhất. | empathetic_observation |
| Âm Nhạc — Nâng Cao | Bohemian Rhapsody chứa hơn 40 từ vựng trung cấp trong 6 phút nhạc — một bài học tiếng Anh ẩn trong rock kinh điển. | surprising_fact |

## Distribution Summary

- **Level**: 4 beginner, 4 preintermediate, 3 intermediate, 1 upperintermediate
- **Skill focus**: 12 balanced_skills (100%)
- **Content type**: 7 movie (["movie"]), 5 music (["music"])
- **Topics**: 2 Psychology, 2 Relationships, 2 Law, 1 Vietnamese culture, 1 Food, 1 Tech, 1 History, 1 Arts

## How Content Was Created

- Each curriculum created via standalone Python script calling `POST https://helloapi.step.is/curriculum/create`
- Scripts validated content before upload using `validate_curriculum.py` shared helper
- Series and collections created via `create_batch_03_series.py` orchestrator script
- All scripts deleted after verification (only this README remains)
- Language: `en` (target), `vi` (user) — all bilingual (beginner through upperintermediate)
- Created: April 10, 2026

### Curriculum Types in This Batch

| Type | Word Count | Sessions | Key Constraints |
|------|-----------|----------|-----------------|
| balanced_skills (beginner) | 12 words (2×6) | 4 (2 learning + 1 review + 1 final reading) | No writingParagraph, no vocabLevel3, simple sentences <15 words avg |
| balanced_skills (preint/int) | 18 words (3×6) | 5 (3 learning + 1 review + 1 final reading) | writingParagraph in S5, bilingual |
| balanced_skills (upperint) | 18 words (3×6) | 5 | Bilingual, writingParagraph requires analytical responses |

## SQL Queries

```sql
-- Find all batch-03 curriculums by ID
SELECT c.id, c.content->>'title' AS title, c.display_order, c.language, c.user_language,
       c.content->>'contentTypeTags' AS content_type,
       c.created_at
FROM curriculum c
WHERE c.id IN (
    'nhozU6UE3Ok8ecuY', 'uQmO5rKAWe2gFJZX', 'JveWZZJHP0MGoAqp',
    '8mWOHy2AMtlmLcb0', 'L9FqtIA4X7pHDfZm', 'cNnm61yWEPFlWjIZ',
    'ESDCO9VLePpLs1Yp', 'prq8RbajcClXXVFl', 'oUjA2tp67D7S4bW2',
    'rClx0i45niliAGgO', 'zl0mmNlY1MxQ5De7', 'qmm4KNgs3MO0Iy01'
)
ORDER BY c.display_order;

-- Find all batch-03 series
SELECT cs.id, cs.title, cs.description, cs.is_public
FROM curriculum_series cs
WHERE cs.id IN ('e9xt62lc', 'hmsbjryc', 'uhz1ytip', '5is05njr')
ORDER BY cs.title;

-- Find batch-03 collections
SELECT cc.id, cc.title, cc.is_public
FROM curriculum_collections cc
WHERE cc.id IN ('0utj9i9f', 'lfi1xjbb');

-- Find curriculums within each series (with series membership)
SELECT cs.title AS series_title, c.id, c.content->>'title' AS title, c.display_order
FROM curriculum c
JOIN curriculum_series_items csi ON csi.curriculum_id = c.id
JOIN curriculum_series cs ON cs.id = csi.curriculum_series_id
WHERE csi.curriculum_series_id IN ('e9xt62lc', 'hmsbjryc', 'uhz1ytip', '5is05njr')
ORDER BY cs.title, c.display_order;

-- Find series within each collection
SELECT cc.title AS collection_title, cs.id AS series_id, cs.title AS series_title
FROM curriculum_series cs
JOIN curriculum_collection_series ccs ON ccs.curriculum_series_id = cs.id
JOIN curriculum_collections cc ON cc.id = ccs.curriculum_collection_id
WHERE ccs.curriculum_collection_id IN ('0utj9i9f', 'lfi1xjbb')
ORDER BY cc.title, cs.title;

-- Verify language homogeneity across series
SELECT * FROM curriculum_series_language_list
WHERE id IN ('e9xt62lc', 'hmsbjryc', 'uhz1ytip', '5is05njr');

-- Duplicate check for all batch-03 titles
SELECT id, content->>'title' AS title, created_at
FROM curriculum
WHERE uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'
  AND content->>'title' IN (
    'Inside Out 2 — Cảm Xúc Bên Trong',
    'Coco — Gia Đình Và Âm Nhạc',
    'The Pursuit of Happyness — Hành Trình Theo Đuổi Hạnh Phúc',
    'Ratatouille — Chú Chuột Đầu Bếp',
    'The Social Network — Mạng Xã Hội Và Cái Giá Của Tham Vọng',
    '12 Angry Men — Mười Hai Người Đàn Ông Giận Dữ Và Sức Mạnh Của Một Tiếng Nói',
    'Inception — Giấc Mơ Trong Giấc Mơ Và Tâm Lý Của Sự Buông Bỏ',
    'Count on Me — Bruno Mars — Tình Bạn Đích Thực',
    'Happy — Pharrell Williams — Sức Mạnh Của Niềm Vui',
    'Viva La Vida — Coldplay — Khi Vinh Quang Tàn Phai',
    'Imagine — John Lennon — Thế Giới Không Biên Giới',
    'Bohemian Rhapsody — Queen — Nghệ Thuật Phá Vỡ Mọi Quy Tắc'
  )
ORDER BY content->>'title', created_at;
```

## Recreation

To recreate this batch: write 12 standalone Python scripts (one per curriculum) following the vi-en-curriculum-expansion spec in `.kiro/specs/vi-en-curriculum-expansion/`. Each script needs hand-written learner-facing content (no templates), structural validation via `validate_curriculum.py`, and API call to `curriculum/create` with `language: "en"`, `userLanguage: "vi"`. Then run an orchestrator to create 4 series, wire curriculums to series, set display orders, create 2 collections, and add series to collections. All balanced_skills, beginner through upperintermediate, all bilingual.
