# Batch 01 — Beginner Foundation (15 curriculums)

Vi-en curriculum expansion, batch 1: 15 beginner-level curriculums covering daily life, relationships, Vietnamese culture, plus one each of writing_focus, speaking_focus, vocab_acquisition, and reader.

## Curriculum IDs (15 total)

| # | Title | ID | Level | Skill Focus | Content Type | Topic |
|---|-------|----|-------|-------------|--------------|-------|
| 1 | Mua Sắm & Trả Giá — Bước Đầu Tiên | `KSGpyKJWs38YNKyP` | beginner | balanced_skills | [] | Daily life |
| 2 | Nấu Ăn Tại Nhà — Bước Đầu Tiên | `J9CfOkZrcbgV7Xyt` | beginner | balanced_skills | [] | Daily life |
| 3 | Tìm Nhà Trọ — Bước Đầu Tiên | `urEIKtDqoNkgtU1D` | beginner | balanced_skills | [] | Daily life |
| 4 | Đi Xe Buýt — Bước Đầu Tiên | `p4a3KRLmz7conztx` | beginner | balanced_skills | [] | Daily life |
| 5 | Kết Bạn — Bước Đầu Tiên | `eRw34qLH5iykxeMf` | beginner | balanced_skills | [] | Relationships |
| 6 | Bữa Cơm Gia Đình — Sợi Dây Kết Nối | `m41sfYQRQ3L7ekjr` | beginner | balanced_skills | [] | Relationships |
| 7 | Xin Lỗi — Nói Lời Xin Lỗi | `uU6VIfi4GqbCLVU8` | beginner | balanced_skills | [] | Relationships |
| 8 | Tết Nguyên Đán — Việt Nam Qua Tiếng Anh | `7HDdJ2T7tUaSE5fQ` | beginner | balanced_skills | [] | Vietnamese culture |
| 9 | Ẩm Thực Đường Phố Việt Nam — Việt Nam Qua Tiếng Anh | `2sufg0maDdiX7JMZ` | beginner | balanced_skills | [] | Vietnamese culture |
| 10 | Áo Dài — Trang Phục Quốc Gia | `h79ewc3LfchP15sS` | beginner | balanced_skills | [] | Vietnamese culture |
| 11 | Phở — Lịch Sử Trong Một Tô | `96VjDz34g8zeAsWz` | beginner | balanced_skills | [] | Vietnamese culture |
| 12 | Nhật Ký Tiếng Anh Đầu Tiên | `Yyl9VshfDCwrBJII` | beginner | writing_focus | [] | Daily life |
| 13 | Kể Về Ngày Của Tôi — Luyện Nói | `QPTIYopUV0psvosc` | beginner | speaking_focus | [] | Daily life |
| 14 | Từ Vựng Thức Ăn Quanh Ta | `46XgQMnDDUsZ4jIT` | beginner | vocab_acquisition | [] | Food |
| 15 | Chiếc Xe Đạp Đỏ Nhỏ | `hdWxqiwbvLsJapnL` | beginner | reader | ["story"] | Daily life |

## Series IDs (7 total)

| Series ID | Title | Curriculums | Display Order Range |
|-----------|-------|-------------|---------------------|
| `qxobskn8` | Bước Đầu Tiên | #1 Shopping, #2 Cooking, #3 Apartment, #4 Bus | 4 curriculums |
| `vksuyken` | Kết Nối | #5 Friends, #6 Family, #7 Sorry | 3 curriculums |
| `kh9hctru` | Việt Nam Qua Tiếng Anh — Cơ Bản | #8 Tết, #9 Street Food, #10 Áo Dài, #11 Phở | 4 curriculums |
| `quq5otpf` | Luyện Viết — Cơ Bản | #12 Diary | 1 curriculum |
| `k51natol` | Luyện Nói — Cơ Bản | #13 My Day | 1 curriculum |
| `3ouiua4h` | Ẩm Thực Cơ Bản | #14 Food Words | 1 curriculum |
| `ztfkvruv` | Truyện Ngắn — Cơ Bản | #15 Bicycle | 1 curriculum |

## Collection IDs (7 total)

| Collection ID | Title |
|---------------|-------|
| `5z2gl6ca` | Cuộc Sống Hàng Ngày |
| `kg0ug56u` | Quan Hệ & Kỹ Năng Xã Hội |
| `n0p37me0` | Văn Hóa Việt Nam Bằng Tiếng Anh |
| `erbl74ej` | Ẩm Thực & Văn Hóa Ăn Uống |
| `nqmqcwny` | Luyện Viết |
| `7i71l2wu` | Luyện Nói |
| `fn9q77oq` | Truyện Ngắn |

## Distribution Summary

- **Level**: 15 beginner (100%)
- **Skill focus**: 11 balanced_skills, 1 writing_focus, 1 speaking_focus, 1 vocab_acquisition, 1 reader
- **Content type**: 14 general ([]), 1 story (["story"])
- **Topics**: 5 daily life, 3 relationships, 4 Vietnamese culture, 1 food, 1 daily life (writing), 1 daily life (reader)

## How Content Was Created

- Each curriculum created via standalone Python script calling `POST https://helloapi.step.is/curriculum/create`
- Scripts validated content before upload using `validate_curriculum.py` shared helper
- Series and collections created via `create_batch_01_series.py` orchestrator script
- All scripts deleted after verification (only this README remains)
- Language: `en` (target), `vi` (user) — all bilingual at beginner level
- Created: April 10, 2026

### Curriculum Types in This Batch

| Type | Word Count | Sessions | Key Constraints |
|------|-----------|----------|-----------------|
| balanced_skills (beginner) | 12 words (2×6) | 4 (2 learning + 1 review + 1 final reading) | No writingParagraph, no vocabLevel3, simple sentences <15 words avg |
| writing_focus (beginner) | 10 words (2×5) | 4 | No speakFlashcards/speakReading/vocabLevel3, heavy scaffolding |
| speaking_focus (beginner) | 18 words (3×6) | 5 | speakFlashcards+speakReading every learning session, pronunciation-focused introAudio |
| vocab_acquisition (beginner) | 24 words (4×6) | 6 (4 learning + 1 review + 1 final reading) | vocabLevel1-3 every learning session, intensive drill |
| reader (beginner) | 12 words | 4 | readAlong every session, cohesive narrative, final reading ≥500 words |

## SQL Queries

```sql
-- Find all batch-01 curriculums by ID
SELECT c.id, c.content->>'title' AS title, c.display_order, c.language, c.user_language,
       c.content->>'contentTypeTags' AS content_type,
       c.created_at
FROM curriculum c
WHERE c.id IN (
    'KSGpyKJWs38YNKyP', 'J9CfOkZrcbgV7Xyt', 'urEIKtDqoNkgtU1D', 'p4a3KRLmz7conztx',
    'eRw34qLH5iykxeMf', 'm41sfYQRQ3L7ekjr', 'uU6VIfi4GqbCLVU8',
    '7HDdJ2T7tUaSE5fQ', '2sufg0maDdiX7JMZ', 'h79ewc3LfchP15sS', '96VjDz34g8zeAsWz',
    'Yyl9VshfDCwrBJII', 'QPTIYopUV0psvosc', '46XgQMnDDUsZ4jIT', 'hdWxqiwbvLsJapnL'
)
ORDER BY c.display_order;

-- Find all batch-01 series
SELECT cs.id, cs.title, cs.display_order, cs.is_public
FROM curriculum_series cs
WHERE cs.id IN ('qxobskn8', 'vksuyken', 'kh9hctru', 'quq5otpf', 'k51natol', '3ouiua4h', 'ztfkvruv')
ORDER BY cs.display_order;

-- Find all batch-01 collections
SELECT cc.id, cc.title, cc.is_public
FROM curriculum_collections cc
WHERE cc.id IN ('5z2gl6ca', 'kg0ug56u', 'n0p37me0', 'erbl74ej', 'nqmqcwny', '7i71l2wu', 'fn9q77oq');

-- Find curriculums within each series (with series membership)
SELECT cs.title AS series_title, c.id, c.content->>'title' AS title, c.display_order
FROM curriculum c
JOIN curriculum_series_items csi ON csi.curriculum_id = c.id
JOIN curriculum_series cs ON cs.id = csi.curriculum_series_id
WHERE csi.curriculum_series_id IN ('qxobskn8', 'vksuyken', 'kh9hctru', 'quq5otpf', 'k51natol', '3ouiua4h', 'ztfkvruv')
ORDER BY cs.display_order, c.display_order;

-- Find series within each collection
SELECT cc.title AS collection_title, cs.id AS series_id, cs.title AS series_title, cs.display_order
FROM curriculum_series cs
JOIN curriculum_collection_series ccs ON ccs.curriculum_series_id = cs.id
JOIN curriculum_collections cc ON cc.id = ccs.curriculum_collection_id
WHERE ccs.curriculum_collection_id IN ('5z2gl6ca', 'kg0ug56u', 'n0p37me0', 'erbl74ej', 'nqmqcwny', '7i71l2wu', 'fn9q77oq')
ORDER BY cc.title, cs.display_order;

-- Verify language homogeneity across series
SELECT * FROM curriculum_series_language_list
WHERE id IN ('qxobskn8', 'vksuyken', 'kh9hctru', 'quq5otpf', 'k51natol', '3ouiua4h', 'ztfkvruv');

-- Verify no level gap violations
SELECT * FROM curriculum_series_level_gap
WHERE id IN ('qxobskn8', 'vksuyken', 'kh9hctru', 'quq5otpf', 'k51natol', '3ouiua4h', 'ztfkvruv');

-- Duplicate check for all batch-01 titles
SELECT id, content->>'title' AS title, created_at
FROM curriculum
WHERE uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'
  AND content->>'title' IN (
    'Mua Sắm & Trả Giá — Bước Đầu Tiên',
    'Nấu Ăn Tại Nhà — Bước Đầu Tiên',
    'Tìm Nhà Trọ — Bước Đầu Tiên',
    'Đi Xe Buýt — Bước Đầu Tiên',
    'Kết Bạn — Bước Đầu Tiên',
    'Bữa Cơm Gia Đình — Sợi Dây Kết Nối',
    'Xin Lỗi — Nói Lời Xin Lỗi',
    'Tết Nguyên Đán — Việt Nam Qua Tiếng Anh',
    'Ẩm Thực Đường Phố Việt Nam — Việt Nam Qua Tiếng Anh',
    'Áo Dài — Trang Phục Quốc Gia',
    'Phở — Lịch Sử Trong Một Tô',
    'Nhật Ký Tiếng Anh Đầu Tiên',
    'Kể Về Ngày Của Tôi — Luyện Nói',
    'Từ Vựng Thức Ăn Quanh Ta',
    'Chiếc Xe Đạp Đỏ Nhỏ'
  )
ORDER BY content->>'title', created_at;
```

## Recreation

To recreate this batch: write 15 standalone Python scripts (one per curriculum) following the vi-en-curriculum-expansion spec in `.kiro/specs/vi-en-curriculum-expansion/`. Each script needs hand-written learner-facing content (no templates), structural validation via `validate_curriculum.py`, and API call to `curriculum/create` with `language: "en"`, `userLanguage: "vi"`. Then run an orchestrator to create 7 series, wire curriculums to series, set display orders, and add series to 7 collections. All beginner-level, all bilingual.
