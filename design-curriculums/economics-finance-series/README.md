# Kinh Tế & Tài Chính Cá Nhân (Economics & Personal Finance)

Series ID: `u6mywecv`
Collection: Học Từ Vựng Theo Chủ Đề (`279d6843`)
Display Order: 400

## Curriculums

| Order | ID | Title |
|---|---|---|
| 0 | `rkgaIEVr1QByTjzE` | Behavioral Economics – Kinh Tế Học Hành Vi |
| 1 | `DA5zHtAn37q3Celm` | Investing Fundamentals – Đầu Tư Cơ Bản |
| 2 | `O89eTyXbzgewvqAo` | Inflation & Monetary Policy – Lạm Phát & Chính Sách Tiền Tệ |
| 3 | `lyv2BDh2ROGQ0ZUs` | Gig Economy – Nền Kinh Tế Tự Do |

## Creation Method

Each curriculum was created via a standalone Python script (`create_econ_1_behavioral.py`, etc.) with hand-written Vietnamese/English content (18 words, 5 sessions, persuasive copy). An orchestrator script (`create_econ_series.py`) created the series, added curriculums, set display orders, and added the series to the collection. All scripts deleted after successful execution.

## SQL Queries

```sql
-- Find series
SELECT * FROM curriculum_series WHERE id = 'u6mywecv';

-- List curriculums in series
SELECT c.id, c.content->>'title' as title, c.display_order
FROM curriculum c
JOIN curriculum_series_items csi ON csi.curriculum_id = c.id
WHERE csi.curriculum_series_id = 'u6mywecv'
ORDER BY c.display_order;
```

## Recreation

Each curriculum has 18 vocabulary words across 3 word groups (W1/W2/W3, 6 each), 3 reading passages, 5 sessions with introAudio, flashcards, vocab exercises, reading, writing activities. Content recoverable via `curriculum/getOne` with the curriculum IDs above.
