# Mùa Review Đến — Bạn Lại Nói Đúng Câu Cũ?

Business English curriculum for intermediate Vietnamese learners struggling to articulate their value during performance reviews at multinational companies.

## Curriculum

- **ID**: `AlUayqpZfmSFTUVS`
- **Language**: en (target) / vi (user)
- **Level**: intermediate
- **Content type**: [] (general)
- **18 vocab words** across 5 sessions

### Vocabulary

| Session | Theme | Words |
|---|---|---|
| 1 | Nói về thành tích | achievement, contribution, impact, initiative, exceed, demonstrate |
| 2 | Đàm phán lương & đãi ngộ | compensation, promotion, benchmark, leverage, negotiate, justify |
| 3 | Career path & mục tiêu dài hạn | aspiration, ownership, growth, trajectory, mentor, articulate |
| 4 | Ôn tập — Review năm nay | (all 18 words in comprehensive reading) |
| 5 | Bài đọc cuối & lời chia tay | (all 18 words + farewell) |

### Story arc

Follows Trang, a 29-year-old HR Business Partner at a Danish FMCG company in Binh Duong. The irony: Trang coaches 12 managers on writing performance feedback, but when her own review comes, she says "I did my best" — the exact phrases she tells others to avoid.

- **Session 1**: Flashback to last year's review. Trang says "I completed all my reports on time" while her actual achievements (redesigned onboarding cutting time-to-productivity by 35%, built retention dashboard) go unmentioned. Rating: meets expectations.
- **Session 2**: Colleague Mei (Malaysian procurement specialist) gets promoted. Trang realizes the gap isn't performance — it's articulation. Mei benchmarks, justifies with data, leverages results.
- **Session 3**: Trang books her first proactive 1-on-1 with Erik. Instead of "I want to improve," she articulates specific aspirations, asks about trajectory, requests a mentor.
- **Session 4**: Review cycle returns. Same room, same Erik, same questions — completely different answers. Trang presents achievements with numbers, negotiates promotion timeline, discusses career trajectory.
- **Session 5**: Epilogue — Trang isn't promoted immediately, but Erik's review notes reflect her true value for the first time. Farewell reviews all 18 words.

### Description tone
- `empathetic_observation` (headline: "MỖI NĂM REVIEW ĐẾN, BẠN LẠI NÓI VỚI SẾP ĐÚNG NHỮNG CÂU CỦA NĂM NGOÁI?")

### Farewell tone
- `warm accountability`

## SQL Queries

```sql
-- Find this curriculum
SELECT id, content->>'title' as title, created_at FROM curriculum WHERE id = 'AlUayqpZfmSFTUVS';

-- Verify structure
SELECT jsonb_array_length(content->'learningSessions') as sessions FROM curriculum WHERE id = 'AlUayqpZfmSFTUVS';

-- Check all activity types
SELECT s.idx as session, a.val->>'activityType' as type, a.val->>'title' as title
FROM curriculum c,
     jsonb_array_elements(c.content->'learningSessions') WITH ORDINALITY AS s(val, idx),
     jsonb_array_elements(s.val->'activities') WITH ORDINALITY AS a(val, idx)
WHERE c.id = 'AlUayqpZfmSFTUVS'
ORDER BY s.idx, a.idx;
```

## Series / Collection

Not yet assigned to any series or collection.

## Creation

- Created: 2026-04-06
- Method: Python script via curriculum/create API
- Script deleted after successful creation
