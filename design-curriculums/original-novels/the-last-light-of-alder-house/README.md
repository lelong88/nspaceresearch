# The Last Light of Alder House

Original novel written for Vietnamese-English bilingual curriculum creation.

## Source Material
- `chapters/1.txt` through `chapters/20.txt` — Plain text chapter files (original English novel)

## Curriculums in Database
Each chapter has a corresponding curriculum in the database (language pair: vi-en).
Series: "The Last Light of Alder House" (series ID: `70b5bb22`), under collection "Fiction".

To get the current chapter-to-curriculum mapping, query:
```sql
SELECT c.id, c.content->>'title' as title, c.display_order
FROM curriculum c
JOIN curriculum_series_items csi ON c.id = csi.curriculum_id
WHERE csi.curriculum_series_id = '70b5bb22'
ORDER BY c.display_order;
```

## History
The 20 chapter curriculums were created via `create_chapter{N}_vi.py` scripts (now deleted).
The original chapter text files are preserved as the source material.
