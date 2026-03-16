# 山中日出 (Bình Minh Trên Núi) — Sunrise in the Mountains

Original 10-chapter Chinese mystery novel written for Vietnamese-Chinese bilingual curriculum creation at preintermediate level.

## How It Was Created
- Original Chinese mystery novel written as 10 chapters, each with 5 reading passage segments (~100-150 Chinese characters each)
- Each chapter uses 15 familiar HSK2-3 vocabulary words (3 per passage) as quick refreshers
- Each chapter was converted into a Python content module (`chapterN_content.py`) exporting a curriculum dict
- Curriculum structure: 6 learning sessions per chapter (sessions 1-5: viewFlashcards + reading + readAlong; session 6: review with all vocab + full chapter readAlong)
- All content validated against 12 correctness properties before upload (`validate_content.py`)
- Uploaded via `create_all_chapters.py` calling `curriculum/create` API
- Script also created series, added all 10 curriculums to series, attached to existing vi-zh Fiction collection, set display orders 1-10

## Series Info
- Series ID: `wlzqfag8`
- Collection: Truyện (小说) — ID: `7nf5wi1d`
- Language: zh, User Language: vi
- Level: preintermediate

## Curriculums in Database

Chapter IDs for reference:
1. `9ZntJ8l8x6nF7bWs`
2. `yVDIyV8oyHVaEPCD`
3. `kYqvKjgr6cRq8kh1`
4. `obgKPpVUOHXqpdTc`
5. `va00n1ogMFtEZ5pU`
6. `8MKUIlyHcUfE30Cf`
7. `Y945YN5j375kyJ85`
8. `2GhyQTgHDfn5OiEA`
9. `zelh0lNebfgDLYTy`
10. `ctJ66iwDaE6Nrm3H`

```sql
SELECT c.id, c.content->>'title' as title, c.display_order
FROM curriculum c
JOIN curriculum_series_items csi ON c.id = csi.curriculum_id
WHERE csi.curriculum_series_id = 'wlzqfag8'
ORDER BY c.display_order;
```

## To Recreate
The full chapter text is stored in each curriculum's reading activities in the DB. To extract:
```sql
SELECT c.id, c.content->>'title' as title, c.display_order,
       c.content::jsonb as full_content
FROM curriculum c
JOIN curriculum_series_items csi ON c.id = csi.curriculum_id
WHERE csi.curriculum_series_id = 'wlzqfag8'
ORDER BY c.display_order;
```

The original chapter text can be recovered from the `reading` and `readAlong` activity content within each curriculum. Each chapter has 15 vocab words in the `viewFlashcards` activities. Vietnamese previews and descriptions are in the `preview` and `description` fields.

## Novel Summary
Linh (阿玲), a Vietnamese art student, arrives at a small Chinese town for a summer art program. She visits the town gallery and sees the famous painting "山中日出" (Sunrise in the Mountains). The painting mysteriously disappears. Over 10 chapters, Linh and her friend Xiaoming investigate — finding clues (red cloth, secret meetings), discovering the painting's history (artist Zhao Mingyuan left 20 years ago after a dispute with gallery owner Wang), traveling south to find Zhao, learning his son took the painting back, and ultimately resolving everything with the painting returned and the artist's name finally credited beside it.
