# Khám Phá Châu Âu (Discover Europe)

Series ID: `6aqul3cz`
Collection: Học Từ Vựng Theo Chủ Đề — `279d6843`
Language: vi-en | Level: Preintermediate

## Curriculums

| # | Title | ID | Words |
|---|---|---|---|
| 0 | Paris – Thành Phố Ánh Sáng Đang Gọi Tên Bạn | `Fck67sZc37NK85Bu` | 18 (landmark, cathedral, boulevard, terrace, pastry, stroll, masterpiece, exhibition, riverside, charming, cobblestone, balcony, breathtaking, sunset, fountain, souvenir, cuisine, unforgettable) |
| 1 | Santorini – Hòn Đảo Nơi Bầu Trời Chạm Biển | `DW14oXIjEgJBASpF` | 18 (cliff, whitewashed, volcanic, horizon, turquoise, winding, ancient, ruins, harbor, fisherman, donkey, steep, spectacular, romantic, vineyard, rooftop, paradise, wander) |
| 2 | Barcelona – Thành Phố Nơi Nghệ Thuật Nhảy Múa Trên Phố | `pjyPmUwUHiYvsVZ9` | 18 (mosaic, promenade, tapas, architecture, vibrant, seaside, marketplace, alleyway, spire, ornate, lively, mural, terracotta, courtyard, flamenco, aroma, dazzling, wanderlust) |
| 3 | Rome – Thành Phố Vĩnh Cửu Đang Chờ Bạn | `BQfZxwpVrCI1P312` | 18 (colosseum, gladiator, empire, piazza, trattoria, eternal, fresco, basilica, pilgrimage, Renaissance, marble, dome, ruin, aqueduct, legendary, espresso, cobbled, timeless) |

## SQL Queries

```sql
-- All curriculums in this series
SELECT c.id, c.content->>'title' as title, c.display_order
FROM curriculum c
JOIN curriculum_series_items csi ON csi.curriculum_id = c.id
WHERE csi.curriculum_series_id = '6aqul3cz'
ORDER BY c.display_order;

-- Get full content of any curriculum
SELECT c.content FROM curriculum c WHERE c.id = '<curriculum_id>';
```

## Recreation

Each curriculum follows a 5-session structure with 18 vocabulary words (9 per learning session):
- Sessions 1-2: introAudio → viewFlashcards → speakFlashcards → vocabLevel1 → vocabLevel2 → reading → speakReading → readAlong → writingSentence
- Session 3: introAudio → viewFlashcards → speakFlashcards → vocabLevel1 → vocabLevel2 → reading → speakReading → readAlong → writingSentence → writingParagraph
- Session 4 (Review): introAudio → viewFlashcards → speakFlashcards → vocabLevel1 → vocabLevel2 → reading → speakReading → readAlong → writingSentence
- Session 5 (Full reading + farewell): introAudio → reading → speakReading → readAlong → introAudio (farewell)

Content was hand-written per curriculum topic. All 72 words are unique across the 4 curriculums. Source scripts deleted after successful import.
