# Medical English Curriculum — Tiếng Anh Y Khoa

25 curriculums across 5 series for Vietnamese-speaking medical students (vi→en, preintermediate-to-intermediate).

## Collection

| Field | Value |
|-------|-------|
| Collection ID | `dimq220a` |
| Title | Tiếng Anh Y Khoa (Medical English) |

## Series

| Order | Series | ID |
|-------|--------|----|
| 0 | Giải Phẫu & Hệ Cơ Quan (Anatomy & Body Systems) | `6y8ht584` |
| 1 | Kỹ Năng Lâm Sàng & Giao Tiếp Bệnh Nhân (Clinical Skills) | `4bo08u2x` |
| 2 | Bệnh Lý & Cơ Chế Bệnh (Diseases & Pathology) | `stv4pwjc` |
| 3 | Dược Lý & Điều Trị (Pharmacology & Treatment) | `k8pgzvey` |
| 4 | Nghiên Cứu Y Học & Y Học Chứng Cứ (Medical Research) | `pbu435xd` |

## Curriculum IDs

### Series A — Anatomy & Body Systems (`6y8ht584`)

| # | Title | ID |
|---|-------|----|
| 0 | Cardiovascular System – Hệ Tim Mạch | `mrGBWySLRx9CFI8D` |
| 1 | Respiratory System – Hệ Hô Hấp | `XPBe5YFqCe4WcNqS` |
| 2 | Digestive System – Hệ Tiêu Hóa | `bl5EYzgURCPq65Yf` |
| 3 | Nervous System – Hệ Thần Kinh | `AmXYmLlmASOl6d4C` |
| 4 | Musculoskeletal System – Hệ Cơ Xương | `yZTG6H0fWIELmCgv` |

### Series B — Clinical Skills & Patient Communication (`4bo08u2x`)

| # | Title | ID |
|---|-------|----|
| 0 | Taking a Patient History – Hỏi Bệnh Sử | `QVL4rDFaNnFw0NSj` |
| 1 | Physical Examination – Khám Lâm Sàng | `G3j98CdKFW10JKIn` |
| 2 | Explaining a Diagnosis – Giải Thích Chẩn Đoán | `O9ojEpdZESedjb96` |
| 3 | Discussing Treatment Options – Thảo Luận Phương Án Điều Trị | `lQXUMiUQ1Tmzs2uT` |
| 4 | Obtaining Informed Consent – Lấy Đồng Ý Điều Trị | `2V7baqsMje80wp8y` |

### Series C — Diseases & Pathology (`stv4pwjc`)

| # | Title | ID |
|---|-------|----|
| 0 | Infectious Diseases – Bệnh Truyền Nhiễm | `ftEqGRyRAMRBpWOr` |
| 1 | Cardiovascular Diseases – Bệnh Tim Mạch | `RF0A09n8F2vGtUb5` |
| 2 | Respiratory Diseases – Bệnh Hô Hấp | `oc2oz2ZOzZEkiy1J` |
| 3 | Cancer & Oncology – Ung Thư & Ung Bướu | `OkELKswI457EnNYy` |
| 4 | Diabetes & Metabolic Disorders – Đái Tháo Đường & Rối Loạn Chuyển Hóa | `pCTPwDZgCcnPoPN3` |

### Series D — Pharmacology & Treatment (`k8pgzvey`)

| # | Title | ID |
|---|-------|----|
| 0 | Antibiotics & Anti-Infectives – Kháng Sinh & Thuốc Chống Nhiễm Trùng | `g8QSoeuQanXlaLFE` |
| 1 | Pain Management & Analgesics – Giảm Đau & Thuốc Giảm Đau | `Fvb6qVlfbw3zU0lM` |
| 2 | Cardiovascular Drugs – Thuốc Tim Mạch | `TJqd0x7RB2cokDpF` |
| 3 | Psychiatric Medications – Thuốc Tâm Thần | `fsgtexdqICynNrBr` |
| 4 | Surgical Procedures & Recovery – Phẫu Thuật & Hồi Phục | `WH7oSAjZHvgDcj9d` |

### Series E — Medical Research & Evidence-Based Medicine (`pbu435xd`)

| # | Title | ID |
|---|-------|----|
| 0 | Study Design & Methodology – Thiết Kế Nghiên Cứu | `Qyn2zOApNSP1NZOT` |
| 1 | Clinical Trials – Thử Nghiệm Lâm Sàng | `h4ZiH0R9j45R6r0B` |
| 2 | Biostatistics Basics – Thống Kê Y Sinh Cơ Bản | `1M7U6u0GAVEbva6t` |
| 3 | Reading a Journal Article – Đọc Hiểu Bài Báo Khoa Học | `KA5GsCIuhzXvljjU` |
| 4 | Systematic Reviews & Meta-Analyses – Tổng Quan Hệ Thống | `oIIqgSO7VZEc2R2G` |

## SQL Queries

Find all curriculums in this collection:
```sql
SELECT c.id, c.content->>'title' as title, c.created_at
FROM curriculum c
JOIN curriculum_series_curriculums csc ON csc."curriculumId" = c.id
JOIN curriculum_series cs ON cs.id = csc."curriculumSeriesId"
JOIN curriculum_collections_series ccs ON ccs."curriculumSeriesId" = cs.id
WHERE ccs."curriculumCollectionId" = 'dimq220a'
ORDER BY cs."displayOrder", c."displayOrder";
```

Find a specific curriculum by ID:
```sql
SELECT id, content->>'title' as title, content FROM curriculum WHERE id = '<ID>';
```

Find all series in the collection:
```sql
SELECT cs.id, cs.title, cs."displayOrder"
FROM curriculum_series cs
JOIN curriculum_collections_series ccs ON ccs."curriculumSeriesId" = cs.id
WHERE ccs."curriculumCollectionId" = 'dimq220a'
ORDER BY cs."displayOrder";
```

## Creation Method

Each curriculum was created via a standalone Python script (`create_<series>_<n>_<topic>.py`) that:
1. Defined the full curriculum content JSON inline (title, description, preview, 5 learning sessions with activities)
2. Validated content against CONTENT_CORRUPTION_RULES.md before upload
3. POSTed to `curriculum/create` with `language='en'`, `userLanguage='vi'`

An orchestrator script (`create_medical_english_series.py`) then:
1. Created the collection via `curriculum-collection/create`
2. Created 5 series via `curriculum-series/create`
3. Added curriculums to series via `curriculum-series/addCurriculum`
4. Set display orders via `curriculum/setDisplayOrder` and `curriculum-series/setDisplayOrder`
5. Added series to collection via `curriculum-collection/addSeriesToCollection`

All scripts were deleted after successful execution. Content is fully recoverable from the database via `curriculum/getOne` or MCP postgres.

## Recreation Context

- Target audience: Vietnamese medical students, preintermediate-to-intermediate English
- 18 words per curriculum (3 groups of 6), 5 sessions each
- Session structure: introAudio → viewFlashcards → speakFlashcards → vocabLevel1-3 → reading → speakReading → readAlong → writingSentence (sessions 1-2, 4); review session (3) with all 18 words; full-reading session (5) with writingParagraph and farewell
- Vietnamese UI text, English reading passages
- Persuasive Vietnamese marketing copy with tone variety per CURRICULUM_QUALITY_STANDARDS.md
- All curriculums are private (not yet public)
