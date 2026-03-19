# Health & Wellness Series Expansion

Series: **Sức Khỏe & Lối Sống (Health & Wellness)** (`e24f29c4`)
Collection: **Học Từ Vựng Theo Chủ Đề (Topic-Based Vocabulary)** (`279d6843`)
Language pair: vi-en | 18 words each | 5 sessions

## Curriculums in series

| # | ID | Title |
|---|---|---|
| 0 | `nG3KtewNxA7iEkut` | Outlive: Healthspan vs. Lifespan (original) |
| 1 | `WoFcRVXJLIfsTXnr` | The Science of Sleep – Giấc Ngủ: Siêu Năng Lực Bị Lãng Quên |
| 2 | `qBXFufi1wo9U0xIj` | Gut Health & The Microbiome – Bộ Não Thứ Hai Bên Trong Bạn |
| 3 | `izvYsuQ0vaeNfs8E` | Stress, Cortisol & Resilience – Nghệ Thuật Bền Bỉ Trong Thế Giới Quá Tải |
| 4 | `EzGDu7x1blVRXhVB` | Nutrition & Metabolism – Dinh Dưỡng: Nhiên Liệu Cho Cỗ Máy Cơ Thể |
| 5 | `ByfeP1fgRiVkc6pQ` | Exercise & Movement Science – Vận Động: Liều Thuốc Mạnh Nhất Mà Không Ai Kê Đơn |
| 6 | `dBbVnKCnLq3VgauU` | Mental Health & Neuroplasticity – Não Bộ: Cỗ Máy Tự Chữa Lành Bên Trong Bạn |
| 7 | `GgGcJKMFU9tSvVn4` | Hydration & Detox Systems – Nước: Dòng Sông Thanh Lọc Bên Trong Cơ Thể |

## How content was created

All 7 new curriculums were modeled on `nG3KtewNxA7iEkut` (the Outlive curriculum):
- Same 5-session structure: 3 learning sessions (6 words each) + review + full reading
- Same activity pattern per learning session: introAudio × 3, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, vocabLevel3, reading, speakReading, readAlong, writingSentence
- Vietnamese user-facing text, English reading passages
- Persuasive copy style for descriptions and previews
- `strip_keys()` applied before upload

## SQL to find these curriculums

```sql
SELECT c.id, c.content->>'title' as title, c.display_order
FROM curriculum c
JOIN curriculum_series_items csi ON csi.curriculum_id = c.id
WHERE csi.curriculum_series_id = 'e24f29c4'
ORDER BY c.display_order;
```
