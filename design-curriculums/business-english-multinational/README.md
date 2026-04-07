# Tự Tin Giao Tiếp Ở Tập Đoàn Đa Quốc Gia

Business English curriculum for pre-intermediate Vietnamese learners working in multinational corporations.

## Curriculum

- **ID**: `DGhw6hHkxGjy8Fkb`
- **Language**: en (target) / vi (user)
- **Level**: preintermediate
- **Content type**: [] (general)
- **18 vocab words** across 5 sessions

### Vocabulary

| Session | Theme | Words |
|---|---|---|
| 1 | Nền tảng giao tiếp công sở | agenda, deadline, stakeholder, alignment, delegate, escalate |
| 2 | Kỹ năng email và phản hồi | follow-up, feedback, proposal, collaborate, prioritize, initiative |
| 3 | Tư duy lãnh đạo và hiệu suất | benchmark, leverage, streamline, accountability, consensus, milestone |
| 4 | Ôn tập — Bức tranh hoàn chỉnh | (all 18 words in comprehensive reading) |
| 5 | Bài đọc cuối và lời chia tay | (all 18 words + farewell) |

### Story arc

Follows Linh, a Vietnamese professional transferred to a Singapore office of a multinational corporation. Tracks her journey from nervous newcomer afraid to speak in meetings to confident team lead managing four regional teams.

## Curriculum 2: Sống Sót Qua Mùa Họp

Meeting survival vocabulary for intermediate Vietnamese learners.

- **ID**: `k7CtmQWVYSZOQNt5`
- **Language**: en (target) / vi (user)
- **Level**: intermediate
- **Content type**: [] (general)
- **18 vocab words** across 5 sessions
- **Description tone**: vivid_scenario
- **Farewell tone**: warm accountability

### Vocabulary

| Session | Theme | Words |
|---|---|---|
| 1 | Tham gia cuộc họp | contribute, interrupt, clarify, rephrase, elaborate, concur |
| 2 | Phản đối và đề xuất | object, propose, table, second, motion, yield |
| 3 | Kết thúc meeting hiệu quả | recap, wrap up, follow through, action item, takeaway, adjourn |
| 4 | Ôn tập — Toàn cảnh meeting | (all 18 words in comprehensive reading) |
| 5 | Bài đọc cuối và lời chia tay | (all 18 words + farewell) |

### Story arc

Continues Linh's journey as team lead. Tracks her growth from freezing in a quarterly review to confidently running meetings with four regional teams — learning to participate, manage disagreements, and close meetings with clear action items.

## Curriculum 3: Email Không Phải Bãi Mìn

Email tone control vocabulary for intermediate Vietnamese learners.

- **ID**: `uNwBzjBN17SYkbMr`
- **Language**: en (target) / vi (user)
- **Level**: intermediate
- **Content type**: [] (general)
- **18 vocab words** across 5 sessions
- **Description tone**: empathetic_observation
- **Farewell tone**: introspective guide

### Vocabulary

| Session | Theme | Words |
|---|---|---|
| 1 | Ấn tượng đầu tiên | acknowledge, regarding, cordially, tentative, comply, expedite |
| 2 | Nhắc nhở, xin lỗi, từ chối | accommodate, oversight, rectify, reiterate, disregard, confidential |
| 3 | Khi email là bằng chứng | mandatory, provisional, forthcoming, hereby, amendment, correspondence |
| 4 | Ôn tập — Toàn cảnh email | (all 18 words in comprehensive reading) |
| 5 | Bài đọc cuối và lời chia tay | (all 18 words + farewell) |

### Story arc

Continues Linh's journey. Tracks her email evolution from spending 25 minutes on 3 sentences to writing precise, tone-aware emails in 4 minutes — learning to handle Australian brevity, vendor disputes, and formal legal correspondence.

## Curriculum 4: Giải Mã Ngôn Ngữ Phòng Họp

Corporate jargon decoder for intermediate Vietnamese learners.

- **ID**: `ZU9Hdq8yeDhw3n1A`
- **Language**: en (target) / vi (user)
- **Level**: intermediate
- **Content type**: [] (general)
- **18 vocab words** across 5 sessions
- **Description tone**: surprising_fact
- **Farewell tone**: team-building energy

### Vocabulary

| Session | Theme | Words |
|---|---|---|
| 1 | Jargon cơ bản | circle back, low-hanging fruit, move the needle, deep dive, bandwidth, synergy |
| 2 | Jargon hành động | pivot, double down, touch base, loop in, pushback, buy-in |
| 3 | Jargon chuyên sâu | pain point, deliverable, boil the ocean, take offline, drill down, stakeholder alignment |
| 4 | Ôn tập — Toàn cảnh jargon | (all 18 words in comprehensive reading) |
| 5 | Bài đọc cuối và lời chia tay | (all 18 words + farewell) |

### Story arc

Continues Linh's journey. Tracks her jargon education from confusing "low-hanging fruit" with actual fruit to becoming the "jargon queen of APAC" — learning that jargon is a compression algorithm, not decoration.

## Curriculum 5: Nói Không Mà Không Mất Bạn

Diplomatic negotiation vocabulary for upper-intermediate Vietnamese learners.

- **ID**: `8EFwc0wmneljc37M`
- **Language**: en (target) / vi (user)
- **Level**: upperintermediate
- **Content type**: [] (general)
- **18 vocab words** across 5 sessions
- **Description tone**: bold_declaration
- **Farewell tone**: quiet awe

### Vocabulary

| Session | Theme | Words |
|---|---|---|
| 1 | Nền tảng ngoại giao | diplomatic, tactful, assertive, concession, compromise, impasse |
| 2 | Công cụ đàm phán | counterproposal, leverage, stipulate, caveat, non-negotiable, goodwill |
| 3 | Kỹ thuật ngôn ngữ | mutual, tentative, binding, pushback, hedge, soften |
| 4 | Ôn tập — Toàn cảnh đàm phán | (all 18 words in comprehensive reading) |
| 5 | Bài đọc cuối và lời chia tay | (all 18 words + farewell) |

### Story arc

Final chapter of Linh's journey. Tracks her growth from saying yes to everything to mastering the "invisible no" — negotiating with VPs, resolving inter-office conflicts, and ultimately earning a promotion to Director of QA for Asia-Pacific.

## SQL Queries

```sql
-- Find all curriculums in this series
SELECT id, content->>'title' as title, created_at FROM curriculum
WHERE id IN ('DGhw6hHkxGjy8Fkb', 'k7CtmQWVYSZOQNt5', 'uNwBzjBN17SYkbMr', 'ZU9Hdq8yeDhw3n1A', '8EFwc0wmneljc37M');

-- Verify structure
SELECT id, content->>'title' as title, jsonb_array_length(content->'learningSessions') as sessions
FROM curriculum WHERE id IN ('DGhw6hHkxGjy8Fkb', 'k7CtmQWVYSZOQNt5', 'uNwBzjBN17SYkbMr', 'ZU9Hdq8yeDhw3n1A', '8EFwc0wmneljc37M');
```

## Creation

- Curriculum 1 created: 2026-04-06
- Curriculum 2 created: 2026-04-07
- Curriculum 3 created: 2026-04-07
- Curriculum 4 created: 2026-04-07
- Curriculum 5 created: 2026-04-07
- Method: Python scripts via curriculum/create API
- Scripts deleted after successful creation
