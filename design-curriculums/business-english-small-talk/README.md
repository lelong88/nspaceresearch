# Business English Small Talk

Two-curriculum series about small talk in multinational workplaces, targeting Vietnamese learners (vi-en).

## Curriculums

### 1. 30 Giây Im Lặng Khó Xử (Preintermediate)
- **ID**: `6uyVQdmcTsYkKpgG`
- **Language**: en (target) / vi (user)
- **Level**: preintermediate
- **Content type**: [] (general)
- **12 vocab words** across 5 sessions

| Session | Theme | Words |
|---|---|---|
| 1 | Mở đầu cuộc trò chuyện | casual, weather, commute, recommend |
| 2 | Giữ cuộc trò chuyện sống | colleague, mention, grab, catch up |
| 3 | Kết thúc tự nhiên và mở rộng | settle in, hang out, figure out, run into |
| 4 | Ôn tập — Small talk trong mọi tình huống | (all 12 words in comprehensive reading) |
| 5 | Bài đọc cuối và lời chia tay | (all 12 words + farewell) |

**Story arc**: Follows Minh, a Vietnamese developer transferred to a Singapore MNC. Tracks his journey from silent elevator rides to building a Friday lunch club with colleagues from six countries.

### 2. Đọc Không Khí, Nói Đúng Lúc (Intermediate)
- **ID**: `KEMdADPDc0hTduPi`
- **Language**: en (target) / vi (user)
- **Level**: intermediate
- **Content type**: [] (general)
- **12 vocab words** across 5 sessions

| Session | Theme | Words |
|---|---|---|
| 1 | Đọc tín hiệu xã hội | awkward, vibe, genuine, approachable |
| 2 | Điều hướng cuộc trò chuyện | transition, tangent, wrap up, bring up |
| 3 | Xây dựng kết nối sâu sắc | bond, perspective, relatable, open up |
| 4 | Ôn tập — Nghệ thuật đọc không khí | (all 12 words in comprehensive reading) |
| 5 | Bài đọc cuối và lời chia tay | (all 12 words + farewell) |

**Story arc**: Follows Hà, a Vietnamese marketing manager who has been at a Singapore MNC for 1 year. She can do basic small talk but struggles with nuances — reading social cues, navigating conversations, building genuine connections. Her journey goes from "functional" to "natural."

## SQL Queries

```sql
-- Find both curriculums
SELECT id, content->>'title' as title, created_at FROM curriculum
WHERE id IN ('6uyVQdmcTsYkKpgG', 'KEMdADPDc0hTduPi');

-- Verify structure
SELECT id, content->>'title' as title, jsonb_array_length(content->'learningSessions') as sessions
FROM curriculum WHERE id IN ('6uyVQdmcTsYkKpgG', 'KEMdADPDc0hTduPi');
```

## Creation

- Created: 2026-04-06
- Method: Python scripts via curriculum/create API
- Scripts deleted after successful creation
- Description tones: vivid_scenario (preintermediate), empathetic_observation (intermediate)
- Farewell tones: introspective guide (preintermediate), warm accountability (intermediate)
