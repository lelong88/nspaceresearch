# Môi Trường & Phát Triển Bền Vững (Environment & Sustainability)

Series ID: `mg9ud60h`
Collection: Học Từ Vựng Theo Chủ Đề (`279d6843`)
Display Order: 500

## Curriculums

| Order | ID | Title |
|---|---|---|
| 0 | `JyFELIUEgZrGbI4O` | Climate Change – Biến Đổi Khí Hậu |
| 1 | `jnjv95TfXeFmaV8w` | Ocean Conservation – Bảo Tồn Đại Dương |
| 2 | `YiYKjSWtdH5ZGp0q` | Renewable Energy – Năng Lượng Tái Tạo |
| 3 | `v4W6bDHrQuPVsYVv` | Sustainable Agriculture – Nông Nghiệp Bền Vững |

## Creation Method

Each curriculum was created via a standalone Python script (`create_env_1_climate.py`, etc.) with hand-written Vietnamese/English content (18 words, 5 sessions, persuasive copy). An orchestrator script (`create_env_series.py`) created the series, added curriculums, set display orders, and added the series to the collection. All scripts deleted after successful execution.

## SQL Queries

```sql
-- Find series
SELECT * FROM curriculum_series WHERE id = 'mg9ud60h';

-- List curriculums in series
SELECT c.id, c.content->>'title' as title, c.display_order
FROM curriculum c
JOIN curriculum_series_items csi ON csi.curriculum_id = c.id
WHERE csi.curriculum_series_id = 'mg9ud60h'
ORDER BY c.display_order;
```

## Recreation

Each curriculum has 18 vocabulary words across 3 word groups (W1/W2/W3, 6 each), 3 reading passages, 5 sessions with introAudio, flashcards, vocab exercises, reading, writing activities. Content recoverable via `curriculum/getOne` with the curriculum IDs above.
