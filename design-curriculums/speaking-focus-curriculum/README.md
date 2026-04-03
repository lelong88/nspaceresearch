# Luyện Nói Tiếng Anh (Speaking Focus Series)

Series ID: `ui33faux`
Language: vi-en (Vietnamese speakers learning English)
Level: preintermediate
Skill focus: speaking

## Structure

Each curriculum follows the same 4-session pattern. 15 vocab words total (5 per session). All words are familiar refreshers, not new learning targets. First-person narrative ("I...") throughout.

**Per session (1–3):** introAudio → viewFlashcards → reading → readAlong → speakReading
**Session 4 (review):** introAudio (recap all 15 words) → viewFlashcards (all 15) → reading (full story) → readAlong → speakReading

## Curriculums

### Luyện Nói: Nấu Cá Hồi Áp Chảo
- **ID:** `yMq70CXQiBV27WEu`
- **Display order:** 4
- **Topic:** Person describing their pan-seared salmon cooking process
- **Vocab:** salmon, pan, oil, heat, season, skin, flip, crispy, garlic, butter, tender, juicy, slice, squeeze, plate
- **Sessions:** (1) Chuẩn bị nguyên liệu, (2) Áp chảo cá hồi, (3) Hoàn thành và thưởng thức, (4) Ôn tập toàn bộ quy trình
- **Created by:** direct API calls (no script preserved)

### Luyện Nói: Chạy Bộ Đường Núi
- **ID:** `9t0tDH7mE6kIbafF`
- **Display order:** 5
- **Topic:** Person describing their mountain trail running experience
- **Vocab:** trail, gear, lace, stretch, pace, climb, steep, breathe, ridge, summit, descend, stumble, steady, reward, accomplish
- **Sessions:** (1) Chuẩn bị trước khi chạy, (2) Trên đường chạy, (3) Xuống núi và hoàn thành, (4) Ôn tập toàn bộ hành trình
- **Script:** `create_trail_running.py`

## SQL Queries

```sql
-- All curriculums in this series
SELECT csi.curriculum_id, c.content->>'title' as title, c.display_order, c.is_public
FROM curriculum_series_items csi
JOIN curriculum c ON c.id = csi.curriculum_id
WHERE csi.curriculum_series_id = 'ui33faux'
ORDER BY c.display_order;

-- Get full content for a specific curriculum
SELECT content FROM curriculum WHERE id = '<curriculum_id>';
```

## Recreation

To recreate the trail running curriculum, run:
```bash
python3 speaking-focus-curriculum/create_trail_running.py
```
Then delete any duplicates and verify series membership.
