# zh-vi — Chinese-Vietnamese Curriculum Collection

Chinese-speaking learners studying Vietnamese. 4 collections, 16 series, 78 curriculums (31 beginner, 21 preintermediate, 26 intermediate).

- **userLanguage**: `zh`
- **language**: `vi`
- **UID**: `zs5AMpVfqkcfDf8CJ9qrXdH58d73`
- **API base**: `https://helloapi.step.is`

## Status

Scripts created but not yet executed against the API. Orchestrator uses `PLACEHOLDER` for series IDs. Remaining files after cleanup: `orchestrator.py`, `api_helpers.py`, `validate_content.py`, `README.md`.

| Collection | Series | Curriculums | Beginner | Preintermediate | Intermediate |
|------------|--------|-------------|----------|-----------------|--------------|
| A (日常生活与旅行) | A1–A4 | 20 | 8 | 5 | 7 |
| B (商务与职场) | B1–B4 | 20 | 8 | 6 | 6 |
| C (学术与思想) | C1–C4 | 20 | 8 | 6 | 6 |
| D (文化与社会) | D1–D4 | 18 | 7 | 4 | 7 |
| **Total** | **16** | **78** | **31** | **21** | **26** |

### Pricing

| Level | Price (credits) |
|-------|----------------|
| Beginner (4 sessions, 12 words) | 19 |
| Preintermediate (5 sessions, 18 words) | 49 |
| Intermediate (5 sessions, 18 words) | 49 |

## Collection & Series IDs

> IDs are placeholders — to be filled after `orchestrator.py` runs.

### Collection A — 日常生活与旅行 (Cuộc sống & Du lịch)

| Key | ID | Title | Curriculums |
|-----|-----|-------|-------------|
| Collection A | `PLACEHOLDER` | 日常生活与旅行 (Cuộc sống & Du lịch) | — |
| Series A1 | `PLACEHOLDER` | 美食与餐饮 (Ẩm thực) | 5 (2 beg, 1 preint, 2 inter) |
| Series A2 | `PLACEHOLDER` | 城市出行与交通 (Giao thông) | 5 (2 beg, 1 preint, 2 inter) |
| Series A3 | `PLACEHOLDER` | 购物与服务 (Mua sắm & Dịch vụ) | 5 (2 beg, 2 preint, 1 inter) |
| Series A4 | `PLACEHOLDER` | 社交与人际关系 (Quan hệ xã hội) | 5 (2 beg, 1 preint, 2 inter) |

### Collection B — 商务与职场 (Kinh doanh & Nghề nghiệp)

| Key | ID | Title | Curriculums |
|-----|-----|-------|-------------|
| Collection B | `PLACEHOLDER` | 商务与职场 (Kinh doanh & Nghề nghiệp) | — |
| Series B1 | `PLACEHOLDER` | 职场沟通 (Giao tiếp công sở) | 5 (2 beg, 2 preint, 1 inter) |
| Series B2 | `PLACEHOLDER` | 求职与职业发展 (Tìm việc & Sự nghiệp) | 5 (2 beg, 1 preint, 2 inter) |
| Series B3 | `PLACEHOLDER` | 行业专业词汇 (Từ vựng chuyên ngành) | 5 (2 beg, 2 preint, 1 inter) |
| Series B4 | `PLACEHOLDER` | 商务运营与贸易 (Vận hành & Thương mại) | 5 (2 beg, 1 preint, 2 inter) |

### Collection C — 学术与思想 (Học thuật & Tri thức)

| Key | ID | Title | Curriculums |
|-----|-----|-------|-------------|
| Collection C | `PLACEHOLDER` | 学术与思想 (Học thuật & Tri thức) | — |
| Series C1 | `PLACEHOLDER` | 科学与技术 (Khoa học & Công nghệ) | 5 (2 beg, 2 preint, 1 inter) |
| Series C2 | `PLACEHOLDER` | 经济与金融 (Kinh tế & Tài chính) | 5 (2 beg, 1 preint, 2 inter) |
| Series C3 | `PLACEHOLDER` | 历史与政治 (Lịch sử & Chính trị) | 5 (2 beg, 2 preint, 1 inter) |
| Series C4 | `PLACEHOLDER` | 心理学与教育 (Tâm lý học & Giáo dục) | 5 (2 beg, 1 preint, 2 inter) |

### Collection D — 文化与社会 (Văn hóa & Xã hội)

| Key | ID | Title | Curriculums |
|-----|-----|-------|-------------|
| Collection D | `PLACEHOLDER` | 文化与社会 (Văn hóa & Xã hội) | — |
| Series D1 | `PLACEHOLDER` | 艺术与文学 (Nghệ thuật & Văn học) | 5 (2 beg, 1 preint, 2 inter) |
| Series D2 | `PLACEHOLDER` | 建筑与设计 (Kiến trúc & Thiết kế) | 5 (2 beg, 1 preint, 2 inter) |
| Series D3 | `PLACEHOLDER` | 环境与可持续发展 (Môi trường & Phát triển bền vững) | 5 (2 beg, 1 preint, 2 inter) |
| Series D4 | `PLACEHOLDER` | 体育与休闲 (Thể thao & Giải trí) | 3 (1 beg, 1 preint, 1 inter) |

## SQL Verification Queries

> Replace `PLACEHOLDER` with actual series IDs after orchestrator runs.

```sql
-- Duplicate title check
SELECT content->>'title' AS title, COUNT(*) AS cnt
FROM curriculum
WHERE uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'
  AND uid NOT LIKE '%_deleted'
  AND language = 'vi' AND user_language = 'zh'
GROUP BY content->>'title'
HAVING COUNT(*) > 1;

-- Series curriculum counts
SELECT cs.id, cs.title, COUNT(csi.curriculum_id) AS cnt
FROM curriculum_series cs
LEFT JOIN curriculum_series_items csi ON csi.curriculum_series_id = cs.id
WHERE cs.id IN (
  'PLACEHOLDER','PLACEHOLDER','PLACEHOLDER','PLACEHOLDER',
  'PLACEHOLDER','PLACEHOLDER','PLACEHOLDER','PLACEHOLDER',
  'PLACEHOLDER','PLACEHOLDER','PLACEHOLDER','PLACEHOLDER',
  'PLACEHOLDER','PLACEHOLDER','PLACEHOLDER','PLACEHOLDER'
)
GROUP BY cs.id, cs.title ORDER BY cs.title;

-- Language homogeneity (all series should show userLanguage=zh, language=vi)
SELECT * FROM curriculum_series_language_list
WHERE id IN (
  'PLACEHOLDER','PLACEHOLDER','PLACEHOLDER','PLACEHOLDER',
  'PLACEHOLDER','PLACEHOLDER','PLACEHOLDER','PLACEHOLDER',
  'PLACEHOLDER','PLACEHOLDER','PLACEHOLDER','PLACEHOLDER',
  'PLACEHOLDER','PLACEHOLDER','PLACEHOLDER','PLACEHOLDER'
);

-- Level gap check (max 1 level gap within each series)
SELECT * FROM curriculum_series_level_gap
WHERE id IN (
  'PLACEHOLDER','PLACEHOLDER','PLACEHOLDER','PLACEHOLDER',
  'PLACEHOLDER','PLACEHOLDER','PLACEHOLDER','PLACEHOLDER',
  'PLACEHOLDER','PLACEHOLDER','PLACEHOLDER','PLACEHOLDER',
  'PLACEHOLDER','PLACEHOLDER','PLACEHOLDER','PLACEHOLDER'
);

-- Pricing verification: beginner = 19, standard = 49
SELECT
  c.id,
  content->>'title' AS title,
  content->'difficultyTags'->>0 AS level,
  c.price
FROM curriculum c
WHERE uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'
  AND uid NOT LIKE '%_deleted'
  AND language = 'vi' AND user_language = 'zh'
ORDER BY content->'difficultyTags'->>0, content->>'title';
```

## Recreation Instructions

1. **Infrastructure**: Run `orchestrator.py` to create 4 collections and 16 series. Record the IDs from stdout.
2. **Update scripts**: Replace `SERIES_ID = "PLACEHOLDER"` in each `create_*.py` script with the actual series ID from the orchestrator output.
3. **Run curriculum scripts**: Execute each `create_*.py` script. Each script validates content, uploads via API, adds to series, sets display order, and sets price.
4. **Verify**: Run the SQL queries above (with real IDs) to confirm counts, language homogeneity, level gaps, and pricing.
5. **Cleanup**: Delete all `create_*.py` scripts after successful execution.

> The orchestrator is NOT idempotent — do not re-run without deleting existing infrastructure first.

## Tone Assignments

All tone assignments are documented in `orchestrator.py` comments. Summary:

| Collection | Description Tone |
|------------|-----------------|
| A (日常生活与旅行) | provocative_question |
| B (商务与职场) | bold_declaration |
| C (学术与思想) | vivid_scenario |
| D (文化与社会) | empathetic_observation |

Series and curriculum tones follow the adjacency and distribution constraints documented in the orchestrator.
