# 味道的记忆 (Ký Ức Hương Vị) — Memories of Flavor

Original 10-chapter Chinese fiction novel written for Vietnamese-Chinese bilingual curriculum creation at preintermediate level.

## How It Was Created
- Original Chinese novel written as 10 chapters, each with 5 reading passage segments (~100-150 Chinese characters each)
- Each chapter uses 15 familiar HSK2-3 vocabulary words (3 per passage) as quick refreshers
- Each chapter was converted into a Python content module (`chapterN_content.py`) exporting a curriculum dict
- Curriculum structure: 6 learning sessions per chapter (sessions 1-5: viewFlashcards + reading + readAlong; session 6: review with all vocab + full chapter readAlong)
- Uploaded via `create_all_chapters.py` calling `curriculum/create` API
- Series organized via `organize_series.py` — created series, added all 10 curriculums, created new vi-zh Fiction collection "Truyện (小说)", set display orders 1-10
- All content validated against 12 correctness properties before upload (`validate_content.py`)

## Series Info
- Series ID: `uq7ezeuh`
- Collection: Truyện (小说) — ID: `7nf5wi1d`
- Language: zh, User Language: vi
- Level: preintermediate

## Curriculums in Database

```sql
SELECT c.id, c.content->>'title' as title, c.display_order
FROM curriculum c
JOIN curriculum_series_items csi ON c.id = csi.curriculum_id
WHERE csi.curriculum_series_id = 'uq7ezeuh'
ORDER BY c.display_order;
```

## To Recreate
The full chapter text is stored in each curriculum's reading activities in the DB. To extract:
```sql
SELECT c.id, c.content->>'title' as title, c.display_order,
       c.content::jsonb as full_content
FROM curriculum c
JOIN curriculum_series_items csi ON c.id = csi.curriculum_id
WHERE csi.curriculum_series_id = 'uq7ezeuh'
ORDER BY c.display_order;
```

The original chapter text can be recovered from the `reading` and `readAlong` activity content within each curriculum. Each chapter has 15 vocab words in the `viewFlashcards` activities. Vietnamese previews and descriptions are in the `preview` and `description` fields.

## Novel Summary
Lan (阮秋兰), a 22-year-old Vietnamese woman from Hanoi, moves to Kunming, China to study cooking at a culinary school. Over 10 chapters she arrives in the city, meets roommate Xiaoyu and noodle shop owner Daming, explores the market, gets homesick and cooks phở for friends, has an idea to combine Vietnamese and Chinese flavors for her semester project, fails at first attempts, discovers her grandmother's secret recipe from a Chinese friend, tries again successfully, presents at the competition and wins a special creativity award, and decides to stay in Kunming for the summer to open a weekend food stall with Xiaoyu.
