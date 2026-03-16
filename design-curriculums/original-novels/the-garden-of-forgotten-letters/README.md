# Khu Vườn Những Lá Thư Bị Lãng Quên (The Garden of Forgotten Letters)

Original 10-chapter coming-of-age/family drama fiction novel written for Vietnamese-English bilingual curriculum creation at preintermediate level.

## How It Was Created
- Original English novel written as 10 chapters, each with 5 reading passage segments (~150-200 words each)
- Each chapter uses 15 familiar A2-B1 vocabulary words (3 per passage) as quick refreshers
- Each chapter was converted into a Python content module (`chapterN_content.py`) exporting a curriculum dict
- Curriculum structure: 6 learning sessions per chapter (sessions 1-5: viewFlashcards + reading + readAlong; session 6: review with all vocab + full chapter readAlong)
- All content validated against 14 correctness properties before upload (`validate_content.py`)
- Uploaded via `create_all_chapters.py` — created all 10 curriculums, series, attached to Fiction collection, set public

## Series Info
- Series ID: `f5ort29f`
- Collection: Truyện (Fiction) — ID: `bjgtj1xj`
- Language: en, User Language: vi
- Level: preintermediate

## Curriculums in Database

```sql
SELECT c.id, c.content->>'title' as title, c.display_order
FROM curriculum c
JOIN curriculum_series_items csi ON c.id = csi.curriculum_id
WHERE csi.curriculum_series_id = 'f5ort29f'
ORDER BY c.display_order;
```

## To Recreate
The full chapter text is stored in each curriculum's reading activities in the DB. To extract:
```sql
SELECT c.id, c.content->>'title' as title, c.display_order,
       c.content::jsonb as full_content
FROM curriculum c
JOIN curriculum_series_items csi ON c.id = csi.curriculum_id
WHERE csi.curriculum_series_id = 'f5ort29f'
ORDER BY c.display_order;
```

## Novel Summary
Linh Tran, a 17-year-old Vietnamese-Australian girl, travels alone to the English village of Willowbrook to inherit Maple Cottage from her grandmother Rose — whom she never met. Her mother left England 30 years ago after a bitter argument and never returned. Linh discovers 47 unsent letters from Rose to her mother, an overgrown garden hiding buried treasures, and a leather notebook revealing the family's century-old history: her great-great-grandparents were Eleanor Marsh (an English nurse) and Minh Tran (a Vietnamese WWI soldier) who married in 1918. Over 10 chapters, Linh follows a hand-drawn map to find 7 gifts buried by different generations, rallies the village to restore the garden, survives a devastating storm, reconnects her mother with England via a tearful phone call, and welcomes her mother back to Willowbrook for the first time in 30 years. Together they find the final gift — the original house deed — and decide to turn the garden into a community space. Linh leaves with the family locket around her neck, understanding that her identity spans Vietnam, England, and Australia.

## Chapter List
1. Ngôi Nhà Trên Đồi (The House on the Hill) — Setup: Linh arrives, discovers dusty house and unsent letters
2. Những Lá Thư (The Letters) — Setup: Linh reads the letters, learns of the argument and a garden secret
3. Người Hàng Xóm (The Neighbour) — Setup: Mrs. Patterson shares Rose's story, delivers the dying message
4. Đào Bới (The Dig) — Investigation: First dig, metal box with photos, family notebook, treasure map
5. Cuốn Sổ Gia Đình (The Family Notebook) — Revelation: Eleanor & Minh's love story, WWI, family heritage
6. Những Món Quà Trong Vườn (The Garden Gifts) — Adventure: Compass, pottery bowl, locket found; village rallies
7. Cơn Bão (The Storm) — Crisis: Storm destroys garden, Linh nearly gives up, community rebuilds
8. Cuộc Gọi (The Phone Call) — Turning point: Linh calls her mother, 30 years of silence breaks
9. Mẹ Về Nhà (Mother Comes Home) — Reunion: Mother arrives, they dig together, find forgiveness letter
10. Món Quà Cuối Cùng (The Last Gift) — Resolution: Final gift found, community garden decision, Linh goes home
