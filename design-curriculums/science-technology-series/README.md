# Khoa Học & Công Nghệ (Science & Technology)

Series ID: `sv3uijyq`
Collection: Học Từ Vựng Theo Chủ Đề (`279d6843`)
Display Order: 300

## Curriculums

| Order | ID | Title |
|---|---|---|
| 0 | `i50J0TWyjxWDZRNN` | AI & Machine Learning – Trí Tuệ Nhân Tạo |
| 1 | `fEEOL3jxjq0R2Zo2` | Space Exploration – Khám Phá Vũ Trụ |
| 2 | `dF8myKUtZilKthhk` | Genetic Engineering & CRISPR – Công Nghệ Gen |
| 3 | `KPvsi7CMwgzUqqKA` | Quantum Computing – Máy Tính Lượng Tử |

## Creation Method

Each curriculum was created via a standalone Python script (`create_science_1_ai.py`, etc.) with hand-written Vietnamese/English content (18 words, 5 sessions, persuasive copy). An orchestrator script (`create_science_series.py`) created the series, added curriculums, set display orders, and added the series to the collection. All scripts deleted after successful execution.

## SQL Queries

```sql
-- Find series
SELECT * FROM curriculum_series WHERE id = 'sv3uijyq';

-- List curriculums in series
SELECT c.id, c.content->>'title' as title, c.display_order
FROM curriculum c
JOIN curriculum_series_items csi ON csi.curriculum_id = c.id
WHERE csi.curriculum_series_id = 'sv3uijyq'
ORDER BY c.display_order;
```

## Recreation

Each curriculum has 18 vocabulary words across 3 word groups (W1/W2/W3, 6 each), 3 reading passages, 5 sessions with introAudio, flashcards, vocab exercises, reading, writing activities. Content recoverable via `curriculum/getOne` with the curriculum IDs above.
