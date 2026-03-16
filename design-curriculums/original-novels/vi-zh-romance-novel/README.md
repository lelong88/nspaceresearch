# 湖边的琴声 (Tiếng Đàn Bên Hồ) — The Sound of Music by the Lake

Original 10-chapter Chinese romance/coming-of-age novel written for Vietnamese-Chinese bilingual curriculum creation at preintermediate level.

## How It Was Created
- Original Chinese romance novel written as 10 chapters, each with 5 reading passage segments (~100-150 Chinese characters each)
- Each chapter uses 15 familiar HSK2-3 vocabulary words (3 per passage) as quick refreshers
- Each chapter was converted into a Python content module (`chapterN_content.py`) exporting a curriculum dict
- Curriculum structure: 6 learning sessions per chapter (sessions 1-5: viewFlashcards + reading + readAlong; session 6: review with all vocab + full chapter readAlong)
- All content validated against 12 correctness properties before upload (`validate_content.py`)
- Uploaded via `create_all_chapters.py` calling `curriculum/create` API
- Script also created series, added all 10 curriculums to series, attached to existing vi-zh Fiction collection, set display orders 1-10

## Series Info
- Series ID: `z6xddztr`
- Collection: Truyện (小说) — ID: `7nf5wi1d`
- Language: zh, User Language: vi
- Level: preintermediate

## Curriculums in Database

Chapter IDs for reference:
1. `oBbLBgdhhB92sw1W`
2. `0gDfBmaaILFsybhn`
3. `BnexmG0Eew9ly0Q5`
4. `PIkkeQwiHyZTLdW8`
5. `uDnmKGnd1rBxtC0R`
6. `NuTdMMGAJMUEWaTu`
7. `WH6TuntirAt9amdj`
8. `6Mlkss6aQIoPWw2S`
9. `SkKxWR6p5klRiWFR`
10. `32kDXxWAmeH6qwSZ`

```sql
SELECT c.id, c.content->>'title' as title, c.display_order
FROM curriculum c
JOIN curriculum_series_items csi ON c.id = csi.curriculum_id
WHERE csi.curriculum_series_id = 'z6xddztr'
ORDER BY c.display_order;
```

## To Recreate
The full chapter text is stored in each curriculum's reading activities in the DB. To extract:
```sql
SELECT c.id, c.content->>'title' as title, c.display_order,
       c.content::jsonb as full_content
FROM curriculum c
JOIN curriculum_series_items csi ON c.id = csi.curriculum_id
WHERE csi.curriculum_series_id = 'z6xddztr'
ORDER BY c.display_order;
```

## Novel Summary
Hà (阿荷), a 20-year-old Vietnamese girl, travels to a small lakeside town in China to work at a tea house for the summer. She meets the kind owner Trần A Di (陈阿姨), learns to brew tea, and hears mysterious guzheng music from the lake at night. She discovers the musician is Tiểu Kiệt (小杰), a local boy her age. He teaches her guzheng, they attend the summer festival together, and grow close through music and conversation. Hà learns Tiểu Kiệt has been accepted to a music conservatory in the city and must leave. She meets his grandfather, who shares the guzheng's wartime history and gives her a precious red cord. During a rainy afternoon trapped in the tea house, they confess how much they mean to each other. Tiểu Kiệt holds a farewell concert by the lake where Hà joins him for a duet. They promise to return every summer. One year later, both keep their promise — reuniting by the lake to play music together again.
