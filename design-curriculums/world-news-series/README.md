# World News

Series ID: `3d836654`
Collection: News-Based Learning — `38fb6061`
Language: vi-en | Level: Advanced

## Curriculums

| # | Title | ID | Words |
|---|---|---|---|
| 0 | Gulf Crisis 2026 | `G1pwg72KEECMqy5s` | 18 |
| 1 | Climate Crisis 2026: Extreme Weather, Carbon Wars, and the Fight for Survival | `wpDA2qMthvXHPjAX` | 18 (carbon emissions, greenhouse effect, fossil fuels, renewable energy, global warming, climate change, drought, flooding, heatwave, wildfire, sea level rise, ecosystem, sustainability, carbon footprint, net zero, climate refugee, adaptation, resilience) |
| 2 | Global Migration Crisis: Borders, Survival, and the Human Cost | `epFdZ7Nqj8Z5ugR8` | 18 (migration, asylum, refugee, displacement, border, humanitarian, smuggling, detention, deportation, undocumented, trafficking, quota, integration, xenophobia, remittance, diaspora, resettlement, sovereignty) |
| 3 | AI Regulation & the Global Tech Power Struggle | `VwUCKDA4tI8XoTk1` | 18 (regulation, artificial intelligence, surveillance, privacy, algorithm, accountability, monopoly, antitrust, data breach, misinformation, deepfake, censorship, intellectual property, open source, semiconductor, tech sovereignty, digital divide, compliance) |

## SQL Queries

```sql
-- All curriculums in this series
SELECT c.id, c.content->>'title' as title, c.display_order
FROM curriculum c
JOIN curriculum_series_items csi ON csi.curriculum_id = c.id
WHERE csi.curriculum_series_id = '3d836654'
ORDER BY c.display_order;

-- Get full content of any curriculum
SELECT c.content FROM curriculum c WHERE c.id = '<curriculum_id>';
```

## Recreation

Curriculums 1-3 follow the same 5-session structure (matching `science-technology-series/create_science_1_ai.py` pattern):
- Sessions 1-3: introAudio (welcome + vocab + grammar) → viewFlashcards → speakFlashcards → vocabLevel1 → vocabLevel2 → reading → speakReading → readAlong → writingSentence
- Session 4: Review (introAudio → flashcards/vocab for all 18 words → writingSentence for all 18)
- Session 5: Full reading + farewell (introAudio → reading → speakReading → readAlong → introAudio farewell)

Curriculum 0 (Gulf Crisis) uses a slightly different structure (has vocabLevel3, writingParagraph). Content was hand-written per curriculum topic (no templates). Source scripts deleted after successful import.
