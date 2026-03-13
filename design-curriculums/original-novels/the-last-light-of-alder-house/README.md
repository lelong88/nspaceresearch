# The Last Light of Alder House

Original novel written for Vietnamese-English bilingual curriculum creation. 20 chapters, each converted into a curriculum.

## How They Were Created
- Original English novel written as 20 chapter text files
- Each chapter was converted into a vi-en curriculum via `create_chapter{N}_vi.py` scripts
- Chapter text is embedded in the curriculum content (reading passages)

## To Recreate
The full chapter text is stored in each curriculum's reading activities in the DB. To extract:
```sql
SELECT c.id, c.content->>'title' as title, c.display_order,
       c.content::jsonb as full_content
FROM curriculum c
JOIN curriculum_series_items csi ON c.id = csi.curriculum_id
WHERE csi.curriculum_series_id = '70b5bb22'
ORDER BY c.display_order;
```
The original chapter text can be recovered from the `reading` and `readAlong` activity content within each curriculum.

## Curriculums in Database
Series: "The Last Light of Alder House" (ID: `70b5bb22`), under collection "Fiction".
20 chapters, display_order 1–20.

```sql
SELECT c.id, c.content->>'title' as title, c.display_order
FROM curriculum c
JOIN curriculum_series_items csi ON c.id = csi.curriculum_id
WHERE csi.curriculum_series_id = '70b5bb22'
ORDER BY c.display_order;
```
