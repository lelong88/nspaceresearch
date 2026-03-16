# The Signal Beyond

Original 20-chapter science fiction novel written for English-only (en-en) curriculum creation at upper-intermediate (B2) level.

## How It Was Created
- Original English science fiction novel written as 20 chapters, each with 5 reading passage segments (~150–290 words each)
- Each chapter uses 20 familiar B2 vocabulary words (4 per passage) as contextual refreshers
- Each chapter was converted into a Python content module (`chapterN_content.py`) exporting a curriculum dict
- Curriculum structure: 6 learning sessions per chapter (sessions 1–5: viewFlashcards + reading + readAlong; session 6: review with all vocab + full chapter readAlong)
- All content validated against 14 correctness properties before upload (`validate_content.py`)
- Uploaded via `create_all_chapters.py` — created all 20 curriculums, series, attached to en-en Fiction collection, set public

## Series Info
- Series ID: `2wlmlwpz`
- Collection: Fiction (en-en) — ID: `bjgtj1xj`
- Language: en, User Language: en
- Level: upperintermediate

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

The original chapter text can be recovered from the `reading` and `readAlong` activity content within each curriculum. Each chapter has 20 vocab words in the `viewFlashcards` activities. English previews and descriptions are in the `preview` and `description` fields. VocabList entries are plain strings (no translation objects).

## Novel Summary
Dr. Lena Vasquez, a radio astronomer at the Cerro Alto Observatory in Chile's Atacama Desert, detects an anomalous signal containing a prime number sequence. She recruits colleague Dr. Raj Patel to confirm the signal, then discovers her late father's redacted files about a prior detection — along with a warning about Director Hale's efforts to suppress it. Lena brings in computational linguist Mara Chen, who finds Earth coordinates embedded in the signal. A network breach is detected, and Dr. Okafor joins as an ally just as unknown agents search the control room. A government audit is announced, and the team discovers monitoring software on their systems. Mara decodes device instructions within the signal, and the team builds a transmitter — only for the signal to change at dawn. They discover the signal is interactive, responding to their actions. Under mounting pressure the team fractures and Raj leaves. Lena decides to go public through journalist Elena Vargas, but a partial leak destroys her credibility and she is suspended. Vargas's full article goes live, Raj returns with proof, and the signal amplifies. Global observatories confirm the signal and Lena testifies before Congress. Hale orders the observatory seized, but the team votes to respond. They transmit a reply and the signal responds immediately — federal agents arrive too late to stop it. In the resolution, Hale resigns, the observatory reopens as an international research centre, and the team stands together under a sky full of stars, knowing they are part of a larger universe.

## Chapter List
1. The Signal — Setup: Lena detects an anomalous signal with a prime number sequence
2. The Colleague — Setup: Lena recruits Dr. Raj Patel, they confirm the signal
3. The Archive — Setup: Lena discovers her father's redacted files about a prior detection
4. The Warning — Setup: Lena reads her father's warning about Director Hale's suppression
5. The Linguist — Rising: Recruits Mara Chen (computational linguist), signal contains Earth coordinates
6. The Coordinates — Rising: Signal points to locations on Earth, network breach detected
7. The Ally — Rising: Dr. Okafor joins as ally, control room searched by unknown agents
8. The Audit — Rising: Government audit announced, team discovers monitoring software
9. The Instructions — Rising: Mara decodes device instructions embedded in the signal
10. The Transmitter — Rising: Team builds transmitter, signal changes at dawn
11. The Response — Midpoint: Signal is interactive and responsive, changes when they interact
12. The Fracture — Midpoint: Team fractures under pressure, Raj leaves
13. The Decision — Midpoint: Lena decides to go public via journalist Elena Vargas
14. The Article — Escalation: Meets Vargas, audit team inspects, Hale moves to discredit Lena
15. The Leak — Escalation: Partial leak destroys credibility, Lena suspended
16. The Truth — Escalation: Vargas's full article goes live, Raj returns with proof, signal amplifies
17. The Point of No Return — Escalation: Global observatories confirm signal, Lena testifies before Congress
18. The Threshold — Climax: Hale orders observatory seized, team votes to respond to signal
19. The Reply — Climax: Team transmits reply, signal responds immediately, federal agents arrive too late
20. A Larger Universe — Resolution: Hale resigns, observatory reopens as international centre, team stands together
