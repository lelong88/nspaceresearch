# Hướng Dẫn Viên Du Lịch (Tour Guides)

Series ID: `1e6e8a71`
Collection: Tiếng Anh Chuyên Nghiệp (Professional English) — `89acc79b`
Language: vi-en | Level: Upper-intermediate

## Curriculums

| # | Title | ID | Words |
|---|---|---|---|
| 0 | Introducing Huế to the World | `EA1OBMOANK7hskWq` | 18 (imperial citadel, heritage, reign, royal tomb, pagoda, mausoleum, elaborate, ornate, reenactment, royal cuisine, steamed rice cake, tapioca dumpling, culinary refinement, dragon boat cruise, cultural pageantry, ...) |
| 1 | Discovering Hội An | `R0KOL7u1sB7GpU7f` | 18 (ancient town, lantern, merchant house, Japanese covered bridge, silk, tailor, UNESCO-listed, well-preserved, pedestrian street, sampan, handicraft, lacquerware, full moon festival, floating lantern, cao lau, white rose dumpling, assembly hall, communal house) |
| 2 | Exploring Hạ Long Bay | `XBbd4PkOIyWEvH0i` | 18 (limestone karst, emerald water, archipelago, geological formation, cave, grotto, cruise ship, kayaking, floating village, pearl farm, viewpoint, sunrise, biodiversity, marine ecosystem, conservation, sustainable tourism, national park, endangered species) |
| 3 | Trekking Sa Pa | `rGzQQB9go0wLplNo` | 18 (terraced rice field, valley, ethnic minority, Hmong, homestay, trekking, Fansipan, cable car, misty, bamboo forest, waterfall, scenic route, brocade weaving, local market, indigo dyeing, traditional costume, cultural immersion, hospitality) |

## SQL Queries

```sql
-- All curriculums in this series
SELECT c.id, c.content->>'title' as title, c.display_order
FROM curriculum c
JOIN curriculum_series_items csi ON csi.curriculum_id = c.id
WHERE csi.curriculum_series_id = '1e6e8a71'
ORDER BY c.display_order;

-- Get full content of any curriculum
SELECT c.content FROM curriculum c WHERE c.id = '<curriculum_id>';
```

## Recreation

Each curriculum follows the same 5-session structure:
- Sessions 1-3: introAudio (welcome + vocab + grammar) → viewFlashcards → speakFlashcards → vocabLevel1 → vocabLevel2 → vocabLevel3 → reading → speakReading → readAlong → writingSentence
- Session 4: Review (introAudio → flashcards/vocab for all 18 words → full reading → writingSentence)
- Session 5: Full reading + farewell (introAudio → reading → speakReading → readAlong → introAudio farewell)

Scripts were created following the pattern in `science-technology-series/create_science_1_ai.py`. Content was hand-written per curriculum topic (no templates). Source scripts deleted after successful import.
