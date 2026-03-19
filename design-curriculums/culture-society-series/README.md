# Văn Hóa & Xã Hội (Culture & Society)

Series ID: `n7qs5dwv`
Collection: Học Từ Vựng Theo Chủ Đề (`279d6843`)
Display Order: 700

## Curriculums

| Order | ID | Title |
|---|---|---|
| 0 | `4oshk5D43rdJhCY9` | Social Media Psychology – Tâm Lý Mạng Xã Hội |
| 1 | `ne1Pgz3H6o78puqh` | Cultural Intelligence – Trí Tuệ Văn Hóa |
| 2 | `hHxoTzV6HIXXZaWA` | Urbanization – Đô Thị Hóa |
| 3 | `Dt5Je1DcJsOlfaW2` | Future of Work – Tương Lai Nghề Nghiệp |

## Creation Method

Each curriculum was created via a standalone Python script (`create_culture_1_social_media.py`, etc.) with hand-written Vietnamese/English content (18 words, 5 sessions, persuasive copy). An orchestrator script (`create_culture_series.py`) created the series, added curriculums, set display orders, and added the series to the collection. All scripts deleted after successful execution.

## SQL Queries

```sql
-- Find series
SELECT * FROM curriculum_series WHERE id = 'n7qs5dwv';

-- List curriculums in series
SELECT c.id, c.content->>'title' as title, c.display_order
FROM curriculum c
JOIN curriculum_series_items csi ON csi.curriculum_id = c.id
WHERE csi.curriculum_series_id = 'n7qs5dwv'
ORDER BY c.display_order;
```

## Recreation

Each curriculum has 18 vocabulary words across 3 word groups (W1/W2/W3, 6 each), 3 reading passages, 5 sessions with introAudio, flashcards, vocab exercises, reading, writing activities. Content recoverable via `curriculum/getOne` with the curriculum IDs above.
