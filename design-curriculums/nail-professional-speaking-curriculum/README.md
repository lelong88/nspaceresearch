# Tiếng Anh Nghề Nail — Luyện Nói Với Khách (Nail Professional Speaking Series)

Series ID: `mdntfeac`
Language: vi-en (Vietnamese speakers learning English)
Level: preintermediate to intermediate
Skill focus: speaking

## Structure

Each curriculum follows the same 4-session speaking-focus pattern. 15 vocab words total (5 per session 1–3, all 15 in session 4). All reading passages are first-person mini-speeches (2–4 sentences) — the learner speaks as a nail technician addressing a customer. No dialogue, no third-person narration.

**Per session (1–3):** introAudio → viewFlashcards(5) → reading → readAlong → speakReading
**Session 4 (review):** introAudio (recap all 15 words) → viewFlashcards(15) → reading (6–12 sentences) → readAlong → speakReading

## Curriculums

### 1. Chào Khách và Hỏi Ý
- **ID:** `iAFXP9ZvcgpdejCe`
- **Display order:** 1
- **Topic:** Greeting walk-ins, asking what they want
- **Description tone:** vivid_scenario / **Farewell tone:** warm_accountability
- **Vocab:**
  - W1: welcome, appointment, walk-in, prefer, seat
  - W2: schedule, available, wait, ready, check
  - W3: service, today, choose, help, enjoy

### 2. Tư Vấn Kiểu Móng
- **ID:** `u7sUY2goW7oACXLa`
- **Display order:** 2
- **Topic:** Asking about nail preferences and styles
- **Description tone:** empathetic_observation / **Farewell tone:** introspective_guide
- **Vocab:**
  - W1: shape, oval, square, round, length
  - W2: color, shade, match, natural, bold
  - W3: design, simple, pattern, glitter, tip

### 3. Giới Thiệu Dịch Vụ
- **ID:** `mylbpolcxKR0kLse`
- **Display order:** 3
- **Topic:** Describing services, explaining options
- **Description tone:** bold_declaration / **Farewell tone:** team_building_energy
- **Vocab:**
  - W1: gel, polish, manicure, pedicure, acrylic
  - W2: soak, trim, file, buff, cuticle
  - W3: coat, dry, cure, last, protect

### 4. Xử Lý Phàn Nàn
- **ID:** `kcKerGTN5B3Gx6Xq`
- **Display order:** 4
- **Topic:** Handling customer concerns and complaints
- **Description tone:** provocative_question / **Farewell tone:** quiet_awe
- **Vocab:**
  - W1: sorry, fix, redo, adjust, concern
  - W2: chip, crack, uneven, thick, thin
  - W3: careful, gentle, comfortable, satisfy, promise

### 5. Trò Chuyện Nhẹ
- **ID:** `8AzU150dLSH5p78y`
- **Display order:** 5
- **Topic:** Making small talk during appointments
- **Description tone:** surprising_fact / **Farewell tone:** practical_momentum
- **Vocab:**
  - W1: weather, weekend, plan, family, vacation
  - W2: busy, relax, favorite, movie, music
  - W3: nice, beautiful, love, try, recommend

### 6. Thanh Toán và Tiễn Khách
- **ID:** `eIPMF7pevjTOybL7`
- **Display order:** 6
- **Topic:** Processing payment and saying goodbye
- **Description tone:** metaphor_led / **Farewell tone:** warm_accountability
- **Vocab:**
  - W1: total, cash, card, change, receipt
  - W2: tip, discount, price, charge, pay
  - W3: thank, visit, return, next, care

## Known Issues

- "tip" appears in both Curriculum 2 (W3: nail tip) and Curriculum 6 (W2: gratuity tip). Different meanings in context.

## SQL Queries

```sql
-- All curriculums in this series
SELECT csi.curriculum_id, c.content->>'title' as title, c.display_order, c.is_public
FROM curriculum_series_items csi
JOIN curriculum c ON c.id = csi.curriculum_id
WHERE csi.curriculum_series_id = 'mdntfeac'
ORDER BY c.display_order;

-- Get full content for a specific curriculum
SELECT content FROM curriculum WHERE id = '<curriculum_id>';

-- Check for duplicates
SELECT content->>'title' as title, count(*)
FROM curriculum
WHERE uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'
  AND content->>'title' IN ('Chào Khách và Hỏi Ý', 'Tư Vấn Kiểu Móng', 'Giới Thiệu Dịch Vụ', 'Xử Lý Phàn Nàn', 'Trò Chuyện Nhẹ', 'Thanh Toán và Tiễn Khách')
GROUP BY content->>'title'
HAVING count(*) > 1;
```

## Creation Method

Each curriculum was created via a standalone Python script calling `curriculum/create` API. All text content (introAudio scripts, reading passages, descriptions, previews) was hand-written per curriculum — no templates, no string interpolation. A validation script checked all 11 correctness properties before upload. An orchestrator script created the series and set display orders.

Scripts were deleted after successful creation and verification. Content is recoverable from DB via `curriculum/getOne` API or MCP postgres.
