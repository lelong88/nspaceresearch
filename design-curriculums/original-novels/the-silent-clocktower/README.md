# Tháp Đồng Hồ Im Lặng (The Silent Clocktower)

Original 10-chapter mystery/detective fiction novel written for Vietnamese-English bilingual curriculum creation at preintermediate level.

## How It Was Created
- Original English mystery novel written as 10 chapters, each with 5 reading passage segments (~150-200 words each)
- Each chapter uses 15 familiar A2-B1 vocabulary words (3 per passage) as quick refreshers
- Each chapter was converted into a Python content module (`chapterN_content.py`) exporting a curriculum dict
- Curriculum structure: 6 learning sessions per chapter (sessions 1-5: viewFlashcards + reading + readAlong; session 6: review with all vocab + full chapter readAlong)
- All content validated against 14 correctness properties before upload (`validate_content.py`)
- Uploaded via `create_all_chapters.py` — created all 10 curriculums, series, attached to Fiction collection, set public

## Series Info
- Series ID: `[TO BE FILLED AFTER UPLOAD]`
- Collection: Truyện (Fiction) — ID: `97cee550`
- Language: en, User Language: vi
- Level: preintermediate

## Curriculums in Database

```sql
SELECT c.id, c.content->>'title' as title, c.display_order
FROM curriculum c
JOIN curriculum_series_items csi ON c.id = csi.curriculum_id
WHERE csi.curriculum_series_id = '[SERIES_ID]'
ORDER BY c.display_order;
```

## To Recreate
The full chapter text is stored in each curriculum's reading activities in the DB. To extract:
```sql
SELECT c.id, c.content->>'title' as title, c.display_order,
       c.content::jsonb as full_content
FROM curriculum c
JOIN curriculum_series_items csi ON c.id = csi.curriculum_id
WHERE csi.curriculum_series_id = '[SERIES_ID]'
ORDER BY c.display_order;
```

The original chapter text can be recovered from the `reading` and `readAlong` activity content within each curriculum. Each chapter has 15 vocab words in the `viewFlashcards` activities. Vietnamese previews and descriptions are in the `preview` and `description` fields.

## Novel Summary
Mai Nguyen, a young Vietnamese-Australian journalist from Melbourne, travels to Eldermere, a small mountain town in northern England, to write a travel article. She discovers the town's clocktower has stopped at 3:20 and the elderly clockmaker, Mr. Arthur Whitfield, has vanished. Over 10 chapters, Mai meets the townspeople (Tom the pub owner, Mrs. Chen the tea shop owner, Lily at the post office), explores the clocktower, finds Whitfield's workshop and a leather journal with drawings of a hidden compartment. The journal disappears overnight. A stranger arrives — David Whitfield, the clockmaker's nephew, who has a warning letter from his uncle. Together they open the compartment and find an 1890 deed proving the tower is private Hargrove family property (never legally transferred to the town) and a map of underground tunnels. Mai researches the Hargrove family at the library and confronts Mr. Graves, the corrupt council head who threatens her. In the tunnels beneath the tower, Mai and David find Whitfield alive — he's been hiding underground for three months after Graves threatened him. They organize a town meeting where Mai presents the evidence and Whitfield walks in alive. Graves admits to a deal with a developer to sell the tower land. He is taken away by police. In the resolution, Mrs. Chen is elected new council head, Whitfield repairs the clock with David's help, Mai publishes an investigative article, and the clock strikes again as Mai says goodbye and boards the train home.

## Chapter List
1. Thị Trấn Trên Đồi (The Town on the Hill) — Setup: Mai arrives, sees stopped clock
2. Những Người Hàng Xóm (The Neighbours) — Setup: Mai meets townspeople
3. Bên Trong Tháp (Inside the Tower) — Investigation: workshop, journal, compartment
4. Người Lạ Trong Thị Trấn (The Stranger in Town) — Investigation: journal stolen, stranger appears
5. Cuộc Gặp Gỡ Bất Ngờ (The Unexpected Meeting) — Twist: stranger is David, uncle's warning letter
6. Ngăn Bí Mật (The Secret Compartment) — Investigation: deed and tunnel map found
7. Hồ Sơ Cũ (The Old Records) — Investigation: library research, confronting Graves
8. Đường Hầm (The Tunnel) — Climax: tunnels explored, Whitfield found alive
9. Đối Mặt (The Confrontation) — Climax: town meeting, Graves exposed
10. Tiếng Chuông Trở Lại (The Clock Strikes Again) — Resolution: clock repaired, Mai goes home
