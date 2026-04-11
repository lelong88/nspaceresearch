# Batch 02 — Writing Focus & Vocab Acquisition (13 curriculums)

Vi-en curriculum expansion, batch 2: 12 writing_focus curriculums across 4 difficulty levels (beginner through advanced) plus 1 vocab_acquisition curriculum. Topics: Psychology, Vietnamese culture, Relationships, Food, Daily life, Tech, Arts, History.

## Curriculum IDs (13 total)

| # | Title | ID | Level | Skill Focus | Content Type | Topic |
|---|-------|----|-------|-------------|--------------|-------|
| 1 | Viết Về Cảm Xúc — Luyện Viết | `9ywytqNGbsBhoHf9` | beginner | writing_focus | [] | Psychology |
| 2 | Nơi Yêu Thích Của Tôi — Luyện Viết | `r166F1WdntU8UXSM` | beginner | writing_focus | [] | Vietnamese culture |
| 3 | Mô Tả Người — Luyện Viết | `gDQAPRFypMB5JIzB` | beginner | writing_focus | [] | Relationships |
| 4 | Email Cho Bạn — Luyện Viết | `F8aVDCYBqj6iHoEb` | preintermediate | writing_focus | [] | Relationships |
| 5 | Viết Đánh Giá Nhà Hàng — Luyện Viết | `HpUhpXrxB9pbpseG` | preintermediate | writing_focus | [] | Food |
| 6 | Blog Du Lịch — Luyện Viết | `aTdjE2zcUYKTr5yU` | preintermediate | writing_focus | [] | Daily life |
| 7 | Bài Luận Ý Kiến: Mạng Xã Hội — Luyện Viết | `rGNqKsdwbNANT0Yi` | intermediate | writing_focus | [] | Tech |
| 8 | Thư Thuyết Phục: Môi Trường — Luyện Viết | `nd9VmVJbSKIbIIby` | intermediate | writing_focus | [] | Arts |
| 9 | Viết Bài Phê Bình Phim — Luyện Viết | `29wgFdV9cAoXGes4` | intermediate | writing_focus | ["movie"] | Arts |
| 10 | Bài Luận Tranh Luận: Giáo Dục — Luyện Viết | `G4iAEjxFmwtRJjcb` | upperintermediate | writing_focus | [] | Psychology |
| 11 | Phân Tích Phản Biện: Tin Tức — Luyện Viết | `IMx10MlGC22Zm8DB` | upperintermediate | writing_focus | [] | Tech |
| 12 | Academic Writing: Research | `Jo02Yckq7P2RbxQY` | advanced | writing_focus | [] | History |
| 13 | Từ Vựng Cảm Xúc — Tâm Lý Học | `V6k3M9zSV0n5rq3W` | beginner | vocab_acquisition | [] | Psychology |

## Series IDs (4 total — 1 existing updated, 3 new)

| Series ID | Title | Curriculums | Status |
|-----------|-------|-------------|--------|
| `quq5otpf` | Luyện Viết — Cơ Bản | #12 Diary (batch-01), #1 Feelings, #2 Favorite Place, #3 Describing People | EXISTING — added 3 curriculums |
| `gwlak7rn` | Luyện Viết — Trung Cấp | #4 Email, #5 Restaurant, #6 Travel, #7 Social Media, #8 Persuasive, #9 Film Review | NEW |
| `j6rxpu7o` | Luyện Viết — Nâng Cao | #10 Argument Essay, #11 Critical Analysis, #12 Academic Writing | NEW |
| `s5iid1fg` | Cảm Xúc | #1 Feelings, #13 Emotion Vocab | NEW |

## Collection IDs (1 new, 1 existing updated)

| Collection ID | Title | Status |
|---------------|-------|--------|
| `nqmqcwny` | Luyện Viết | EXISTING — now has 3 series (Cơ Bản, Trung Cấp, Nâng Cao) |
| `d9lm2uwf` | Tâm Lý & Cảm Xúc | NEW |

## Series Descriptions & Tones

| Series | Description | Tone |
|--------|-------------|------|
| Luyện Viết — Trung Cấp | Từ email cho bạn đến bài luận ý kiến — 6 bài học nâng cấp kỹ năng viết tiếng Anh từ giao tiếp đến phân tích. | empathetic_observation |
| Luyện Viết — Nâng Cao | Tranh luận, phân tích phản biện, viết học thuật — ba bài học đưa kỹ năng viết tiếng Anh lên tầm chuyên nghiệp. | bold_declaration |
| Cảm Xúc | Gọi tên cảm xúc bằng tiếng Anh — từ 10 từ viết về cảm xúc đến 24 từ tâm lý học chuyên sâu. | surprising_fact |

## Cross-Series Note

Curriculum `9ywytqNGbsBhoHf9` (Viết Về Cảm Xúc) appears in two series:
- `quq5otpf` Luyện Viết — Cơ Bản (writing skill focus grouping)
- `s5iid1fg` Cảm Xúc (psychology topic grouping)

## Distribution Summary

- **Level**: 4 beginner, 3 preintermediate, 3 intermediate, 2 upperintermediate, 1 advanced
- **Skill focus**: 12 writing_focus, 1 vocab_acquisition
- **Content type**: 12 general ([]), 1 movie (["movie"])
- **Topics**: 2 Psychology, 2 Relationships, 2 Arts, 2 Tech, 1 Vietnamese culture, 1 Food, 1 Daily life, 1 History

## How Content Was Created

- Each curriculum created via standalone Python script calling `POST https://helloapi.step.is/curriculum/create`
- Scripts validated content before upload using `validate_curriculum.py` shared helper
- Series and collections created via `create_batch_02_series.py` orchestrator script
- All scripts deleted after verification (only this README remains)
- Language: `en` (target), `vi` (user) — all bilingual except advanced (English-only)
- Created: April 10, 2026

### Curriculum Types in This Batch

| Type | Word Count | Sessions | Key Constraints |
|------|-----------|----------|-----------------|
| writing_focus (beginner) | 10 words (2×5) | 4 | No speakFlashcards/speakReading/vocabLevel3, no writingParagraph, heavy scaffolding |
| writing_focus (preint/int) | 10 words (2×5) | 4 | No speakFlashcards/speakReading/vocabLevel3, writingParagraph in S3-S4 |
| writing_focus (upperint) | 10 words (2×5) | 4 | Bilingual, writingParagraph requires analytical responses |
| writing_focus (advanced) | 10 words (2×5) | 4 | English-only, writingParagraph requires academic responses |
| vocab_acquisition (beginner) | 24 words (4×6) | 6 (4 learning + 1 review + 1 final reading) | vocabLevel1-3 every learning session, intensive drill |

## SQL Queries

```sql
-- Find all batch-02 curriculums by ID
SELECT c.id, c.content->>'title' AS title, c.display_order, c.language, c.user_language,
       c.content->>'contentTypeTags' AS content_type,
       c.created_at
FROM curriculum c
WHERE c.id IN (
    '9ywytqNGbsBhoHf9', 'r166F1WdntU8UXSM', 'gDQAPRFypMB5JIzB',
    'F8aVDCYBqj6iHoEb', 'HpUhpXrxB9pbpseG', 'aTdjE2zcUYKTr5yU',
    'rGNqKsdwbNANT0Yi', 'nd9VmVJbSKIbIIby', '29wgFdV9cAoXGes4',
    'G4iAEjxFmwtRJjcb', 'IMx10MlGC22Zm8DB', 'Jo02Yckq7P2RbxQY',
    'V6k3M9zSV0n5rq3W'
)
ORDER BY c.display_order;

-- Find all batch-02 series
SELECT cs.id, cs.title, cs.description, cs.display_order, cs.is_public
FROM curriculum_series cs
WHERE cs.id IN ('quq5otpf', 'gwlak7rn', 'j6rxpu7o', 's5iid1fg')
ORDER BY cs.display_order;

-- Find batch-02 collections
SELECT cc.id, cc.title, cc.is_public
FROM curriculum_collections cc
WHERE cc.id IN ('nqmqcwny', 'd9lm2uwf');

-- Find curriculums within each series (with series membership)
SELECT cs.title AS series_title, c.id, c.content->>'title' AS title, c.display_order
FROM curriculum c
JOIN curriculum_series_items csi ON csi.curriculum_id = c.id
JOIN curriculum_series cs ON cs.id = csi.curriculum_series_id
WHERE csi.curriculum_series_id IN ('quq5otpf', 'gwlak7rn', 'j6rxpu7o', 's5iid1fg')
ORDER BY cs.display_order, c.display_order;

-- Find series within each collection
SELECT cc.title AS collection_title, cs.id AS series_id, cs.title AS series_title, cs.display_order
FROM curriculum_series cs
JOIN curriculum_collection_series ccs ON ccs.curriculum_series_id = cs.id
JOIN curriculum_collections cc ON cc.id = ccs.curriculum_collection_id
WHERE ccs.curriculum_collection_id IN ('nqmqcwny', 'd9lm2uwf')
ORDER BY cc.title, cs.display_order;

-- Verify language homogeneity across series
SELECT * FROM curriculum_series_language_list
WHERE id IN ('quq5otpf', 'gwlak7rn', 'j6rxpu7o', 's5iid1fg');

-- Duplicate check for all batch-02 titles
SELECT id, content->>'title' AS title, created_at
FROM curriculum
WHERE uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'
  AND content->>'title' IN (
    'Viết Về Cảm Xúc — Luyện Viết',
    'Nơi Yêu Thích Của Tôi — Luyện Viết',
    'Mô Tả Người — Luyện Viết',
    'Email Cho Bạn — Luyện Viết',
    'Viết Đánh Giá Nhà Hàng — Luyện Viết',
    'Blog Du Lịch — Luyện Viết',
    'Bài Luận Ý Kiến: Mạng Xã Hội — Luyện Viết',
    'Thư Thuyết Phục: Môi Trường — Luyện Viết',
    'Viết Bài Phê Bình Phim — Luyện Viết',
    'Bài Luận Tranh Luận: Giáo Dục — Luyện Viết',
    'Phân Tích Phản Biện: Tin Tức — Luyện Viết',
    'Academic Writing: Research',
    'Từ Vựng Cảm Xúc — Tâm Lý Học'
  )
ORDER BY content->>'title', created_at;
```

## Recreation

To recreate this batch: write 13 standalone Python scripts (one per curriculum) following the vi-en-curriculum-expansion spec in `.kiro/specs/vi-en-curriculum-expansion/`. Each script needs hand-written learner-facing content (no templates), structural validation via `validate_curriculum.py`, and API call to `curriculum/create` with `language: "en"`, `userLanguage: "vi"`. Then run an orchestrator to create 3 new series, update 1 existing series, wire curriculums to series, set display orders, create 1 new collection, and add series to 2 collections. Writing_focus curriculums span beginner through advanced; vocab_acquisition is beginner.
