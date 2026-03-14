# The Little Bookshop by the Sea (Tiệm Sách Nhỏ Bên Biển)

Original 10-chapter fiction novel written for Vietnamese-English bilingual curriculum creation at preintermediate level.

## How They Were Created
- Original English novel written as 10 chapters, each with 5 reading passage segments
- Each chapter uses 15 familiar A2-B1 vocabulary words (3 per passage) as quick refreshers
- Each chapter was converted into a Python content module (`chapterN_content.py`) exporting a curriculum dict
- Curriculum structure: 6 learning sessions per chapter (sessions 1-5: viewFlashcards + reading + readAlong; session 6: review with all vocab + full chapter readAlong)
- Uploaded via `create_chapterN_vi.py` scripts calling `curriculum/create` API
- Series organized via `organize_series.py` — created series, added all 10 curriculums, attached to Fiction collection, set display orders 1-10
- All content validated against 11 correctness properties before upload (validate_content.py)

## Series Info
- Series ID: `n4y9zm3v`
- Collection: Truyện (Fiction) — ID: `97cee550`
- Language: en, User Language: vi
- Level: preintermediate

## Curriculums in Database

```sql
SELECT c.id, c.content->>'title' as title, c.display_order
FROM curriculum c
JOIN curriculum_series_items csi ON c.id = csi.curriculum_id
WHERE csi.curriculum_series_id = 'n4y9zm3v'
ORDER BY c.display_order;
```

## To Recreate
The full chapter text is stored in each curriculum's reading activities in the DB. To extract:
```sql
SELECT c.id, c.content->>'title' as title, c.display_order,
       c.content::jsonb as full_content
FROM curriculum c
JOIN curriculum_series_items csi ON c.id = csi.curriculum_id
WHERE csi.curriculum_series_id = 'n4y9zm3v'
ORDER BY c.display_order;
```

The original chapter text can be recovered from the `reading` and `readAlong` activity content within each curriculum. Each chapter has 15 vocab words in the `viewFlashcards` activities. Vietnamese previews and descriptions are in the `preview` and `description` fields.

## Novel Summary
Emma Clarke, 25, inherits a small bookshop in the coastal town of Saltwick, Cornwall from her late grandmother. Over 10 chapters she discovers the town, meets its people (Tom the carpenter, Mrs. Penny, Jack the fisherman), uncovers Gran's secret rare book collection, faces a decision to sell or stay, weathers a storm with the community, finds Gran's unsent letters to her estranged mother, reopens the bookshop, and finally finds home.
