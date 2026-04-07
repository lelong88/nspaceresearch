# Nói Không Mà Không Mất Lòng

Business English curriculum about pushback & negotiation for intermediate Vietnamese learners working at multinational companies in Vietnam.

## Curriculum

- **ID**: `2kva6Um5mENQMFag`
- **Language**: en (target) / vi (user)
- **Level**: intermediate
- **Content type**: [] (general)
- **18 vocab words** across 5 sessions
- **Description tone**: empathetic_observation
- **Farewell tone**: warm accountability

### Vocabulary

| Session | Theme | Words |
|---|---|---|
| 1 | Từ chối lịch sự & đặt ranh giới | decline, boundary, capacity, overwhelm, prioritize, trade-off |
| 2 | Đàm phán & đề xuất thay thế | negotiate, compromise, feasible, alternative, constraint, flexibility |
| 3 | Giữ mối quan hệ khi bất đồng | respectfully, concern, transparent, align, reassure, mutual |
| 4 | Ôn tập — Toàn bộ hành trình | (all 18 words in comprehensive reading) |
| 5 | Bài đọc cuối và lời chia tay | (all 18 words + farewell) |

### Story arc

Follows Ha, a 26-year-old Vietnamese marketing coordinator at a European FMCG multinational in Ho Chi Minh City. Cultural tension: Vietnamese workplace norms (respect through harmony, avoiding direct refusal) vs Western corporate expectations (respect through transparency, clear communication). Set entirely in Vietnam — Ha lives in Vietnamese culture 24/7 but operates in Western corporate culture 8 hours a day. Neutral tone throughout — no villains, just different operating systems colliding.

Key characters:
- **Daniel** — Australian regional marketing manager (Ha's direct boss)
- **Priya** — Indian brand manager (senior to Ha)
- **Yuki** — Japanese client lead based in Singapore
- **Lan** — Vietnamese marketing director, 12 years at MNCs, Ha's mentor

Core message: "Mình vẫn là mình — chỉ thêm cách nói mới."

## SQL Queries

```sql
-- Find this curriculum
SELECT id, content->>'title' as title, created_at FROM curriculum WHERE id = '2kva6Um5mENQMFag';

-- Verify structure
SELECT jsonb_array_length(content->'learningSessions') as sessions FROM curriculum WHERE id = '2kva6Um5mENQMFag';
```

## Creation

- Created: 2026-04-06
- Method: Python script via curriculum/create API
- Script deleted after successful creation
