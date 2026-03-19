# Khám Phá Trung Quốc (探索中国) — Chinese Travel Destinations Series

vi-zh | preintermediate | 4 curriculums × 18 words = 72 words total

## Series

- Series ID: `yjwuyhtk`
- Series title: Khám Phá Trung Quốc (探索中国)
- Status: private (not public, not assigned to any collection)

## Curriculums

| # | Title | ID | Display Order |
|---|---|---|---|
| 1 | 桂林 — Nơi Núi Non Đẹp Nhất Thiên Hạ (桂林山水甲天下) | `yHoyB8QAHuoPQTHD` | 0 |
| 2 | 成都 — Thành Phố Không Ai Muốn Rời Đi (一座来了就不想走的城市) | `Cmb9OPN9alWErMVv` | 1 |
| 3 | 丽江 — Cổ Trấn Ngàn Năm Dưới Chân Tuyết Sơn (雪山下的千年古城) | `x5u34HwpUIvrxOmK` | 2 |
| 4 | 西安 — Cố Đô Ngàn Năm Nơi Lịch Sử Sống Lại (千年古都，历史重生) | `slq4m8qrLtfCsfvM` | 3 |

## SQL Queries

```sql
-- Find the series
SELECT * FROM curriculum_series WHERE id = 'yjwuyhtk';

-- Find all curriculums in the series
SELECT c.id, c.title, c.language, c.user_language, c.display_order
FROM curriculums c
JOIN curriculum_series_curriculums csc ON c.id = csc.curriculum_id
WHERE csc.curriculum_series_id = 'yjwuyhtk'
ORDER BY c.display_order;

-- Get full content of any curriculum
SELECT content FROM curriculums WHERE id = 'yHoyB8QAHuoPQTHD';
```

## Collection

- Collection ID: `q9j66zxj`
- Collection title: Học Từ Vựng Theo Chủ Đề (主题词汇)
- Status: private

## Recreation

Each curriculum has 5 sessions:
- Sessions 1-3: Learning (introAudio welcome + vocab + grammar → viewFlashcards → speakFlashcards → vocabLevel1 → vocabLevel2 → vocabLevel3 → reading → speakReading → readAlong → writingSentence)
- Session 4: Review (introAudio → viewFlashcards → speakFlashcards → vocabLevel1 → vocabLevel2 → vocabLevel3 → reading → speakReading → readAlong → writingSentence)
- Session 5: Full reading & farewell (introAudio intro → reading → speakReading → readAlong → introAudio farewell → writingParagraph)

Vocabulary per curriculum: 18 words (6 per learning session).

Source scripts were in this directory (deleted after successful import).
