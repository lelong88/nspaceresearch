# Ordinary Life Philosophy Curriculum

vi-en series exploring the philosophy of ordinary life for Vietnamese office workers. Inspired by the viral trend "Nếu cả cuộc đời này không rực rỡ thì sao?" Core framing: accurate self-awareness → identify core values → grow from there.

## Series

- **Series ID:** `lg81tyxt`
- **Title:** Nếu Đời Không Rực Rỡ Thì Sao?
- **Language:** en / vi
- **Status:** Private (needs content generation)

## Curriculums

| # | ID | Title | Description Tone | Farewell Tone | Display Order |
|---|---|---|---|---|---|
| 1 | `XrBa2v2cwWiNjfYP` | Tự Nhận Thức: Nhìn Rõ Bản Thân | provocative_question | introspective guide | 0 |
| 2 | `3cbUy3Sx7ZF7RrXe` | Giá Trị Cốt Lõi: Sống Theo Điều Bạn Thật Sự Tin | empathetic_observation | warm accountability | 1 |
| 3 | `zjv789nVZPIWnt8p` | Hài Lòng vs. Tự Mãn: Ranh Giới Mỏng Manh | bold_declaration | quiet awe | 2 |
| 4 | `iaoh0g011AxDzOCw` | Tư Duy Phát Triển Trung Thực: Phát Triển Từ Sự Thật | vivid_scenario | practical momentum | 3 |
| 5 | `enyZYYY9DjHD6421` | Ý Nghĩa Trong Công Việc: Tìm Ý Nghĩa Ngay Trong Công Việc Bình Thường | metaphor_led | team-building energy | 4 |
| 6 | `r7cdd1zXmzRZs63I` | Góc Nhìn Văn Hóa: Thành Công Trông Khác Nhau Ở Mỗi Nơi | surprising_fact | introspective guide | 5 |

## Vocabulary Lists

### 1. Self-Awareness (Tự Nhận Thức)
introspection, bias, denial, perception, rationalize, authentic, projection, deflection, accountability, self-awareness, cognitive, objectivity, vulnerability, defensiveness, transparency, distortion, clarity, candor

### 2. Core Values (Giá Trị Cốt Lõi)
authenticity, conformity, expectation, autonomy, compromise, fulfillment, obligation, rebellion, alignment, conviction, integrity, sacrifice, aspiration, validation, resilience, liberation, boundary, discernment

### 3. Contentment vs. Complacency (Hài Lòng vs. Tự Mãn)
complacency, contentment, stagnation, gratitude, ambition, adaptation, moderation, restlessness, acceptance, aspiration, threshold, equilibrium, momentum, apathy, sufficiency, perspective, renewal, deliberate

### 4. Growth Mindset (Tư Duy Phát Triển Trung Thực)
resilience, vulnerability, compassion, accountability, feedback, plateau, perseverance, setback, humility, reflection, iteration, candor, stagnation, self-compassion, authenticity, calibration, grit, incremental

### 5. Meaning in Work (Ý Nghĩa Trong Công Việc)
craftsmanship, contribution, purpose, mundane, significance, vocation, fulfillment, connection, dedication, alignment, engagement, autonomy, legacy, impact, intentional, stewardship, dignity, ritual

### 6. Cultural Perspectives (Góc Nhìn Văn Hóa)
collectivism, individualism, prestige, hierarchy, aspiration, fulfillment, conformity, identity, expectation, perception, stereotype, assimilation, perspective, autonomy, authenticity, resilience, introspection, liberation

## SQL Queries

```sql
-- Find all 6 curriculums
SELECT id, content->>'title' as title, language, user_language, is_public, display_order, created_at
FROM curriculum
WHERE id IN ('XrBa2v2cwWiNjfYP', '3cbUy3Sx7ZF7RrXe', 'zjv789nVZPIWnt8p', 'iaoh0g011AxDzOCw', 'enyZYYY9DjHD6421', 'r7cdd1zXmzRZs63I')
ORDER BY display_order;

-- Find series and members
SELECT cs.id AS series_id, cs.title, csc.curriculum_id, c.content->>'title' AS curriculum_title, c.display_order
FROM curriculum_series cs
JOIN curriculum_series_items csc ON cs.id = csc.curriculum_series_id
JOIN curriculum c ON csc.curriculum_id = c.id
WHERE cs.id = 'lg81tyxt'
ORDER BY c.display_order;

-- Verify series description
SELECT id, title, length(description) as desc_length, description
FROM curriculum_series WHERE id = 'lg81tyxt';
```

## Recreation Context

Each curriculum was created via a standalone Python script (`create_<topic>.py`) calling the helloapi REST API. Scripts authenticated via `firebase_token.get_firebase_id_token()` with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`. Each script contained `build_content()` (all text hand-written inline), `validate()` (10 correctness properties as assertions), `strip_keys()`, and `create()`. Scripts were deleted after successful creation and verification.

Structure: 18 vocab words per curriculum, 4 sessions (12, 12, 12, 9 activities), `language: "en"`, `userLanguage: "vi"`, `contentTypeTags: []`. Sources: Kahneman, Tasha Eurich, Brené Brown, ACT, Stoicism, Carol Dweck, Kristin Neff, Viktor Frankl, Amy Wrzesniewski, Hofstede, ikigai, hansei, mianzi, nunchi. Reading passages use Vietnamese office worker scenarios. Content recoverable from DB via `curriculum/getOne`.
