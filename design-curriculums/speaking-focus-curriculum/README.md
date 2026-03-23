# Speaking Focus Curriculum

Speaking-focus curriculums that maximize time spent producing speech. No writing activities — all productive time goes to open-ended `speak` activities with escalating prompts. `speakFlashcards` and `speakReading` retained as pronunciation scaffolding. 10 vocab words (2×5) across 4 sessions.

## Collection

- **Collection ID**: `rmvq0pbo`
- **Title**: Speaking Focus

## Series 1: Speaking Focus (en-en, advanced)

- **Series ID**: `8ncovquk`
- **Display Order**: 100

| # | Curriculum ID | Title | Topic |
|---|---|---|---|
| 1 | `aNq8f3hieTh43yQv` | Speaking Focus: The Hidden Machinery of Decision-Making | Cognitive biases & decision-making |
| 2 | `TVNteE4TpOvcjB1I` | Speaking Focus: The Ethics of Artificial Intelligence | AI ethics & societal impact |

Session structure (single-language): 8, 8, 6, 7 activities. 2 speak activities per session. Prompts escalate: explain → role-play → summarize → debate → monologue → counter-argument → presentation → impromptu response.

## Series 2: Luyện Nói Tiếng Anh (vi-en, intermediate)

- **Series ID**: `ui33faux`
- **Display Order**: 200

| # | Curriculum ID | Title | Topic |
|---|---|---|---|
| 3 | `VuOIM696VFuSFlLl` | Luyện Nói: Du Lịch và Trải Nghiệm Văn Hóa | Travel & cultural experiences |
| 4 | `9Xwvbnt3jtuawJrt` | Luyện Nói: Sức Khỏe và Lối Sống Lành Mạnh | Health & lifestyle |

Session structure (bilingual): 11, 11, 8, 6 activities. Speak count: 1, 1, 2, 1 per session. Vietnamese prompts, English responses. `vocabLevel2` retained.

## How Content Was Created

Each curriculum was a standalone Python script (~850-900 lines) with all hand-written content (no templates). Scripts included inline `validate(content, variant)` checking 18 structural properties before API upload. One orchestrator script created the collection, both series, and wired everything together. All scripts deleted after successful creation and verification.

Curriculum type: `speaking_focus` — two variants:
- **Single-language** (en-en): No `vocabLevel2`, no writing, 2 speaks/session
- **Bilingual** (vi-en): Keeps `vocabLevel2`, Vietnamese introAudio teaching, 1-2 speaks/session

## SQL Queries

```sql
-- Find the collection
SELECT * FROM curriculum_collections WHERE id = 'rmvq0pbo';

-- Find both series
SELECT * FROM curriculum_series WHERE id IN ('8ncovquk', 'ui33faux');

-- Find all 4 curriculums with series info
SELECT c.id, c.content->>'title' as title, c.language, c.user_language, c.display_order, cs.title as series
FROM curriculum c
JOIN curriculum_series_items csi ON csi.curriculum_id = c.id
JOIN curriculum_series cs ON cs.id = csi.curriculum_series_id
WHERE cs.id IN ('8ncovquk', 'ui33faux')
ORDER BY cs.display_order, c.display_order;

-- Verify language homogeneity
SELECT * FROM curriculum_series_language_list WHERE id IN ('8ncovquk', 'ui33faux');
```

## Recreation

To recreate, write 4 Python scripts following the `speaking_focus` pattern:
- Scripts 1-2: single-language en-en advanced, 4 sessions (8,8,6,7), 2 speaks/session
- Scripts 3-4: bilingual vi-en intermediate, 4 sessions (11,11,8,6), speaks 1,1,2,1
- Each script: 10 vocab words (2×5), 3 reading passages, inline validate + strip_keys, API call to `curriculum/create`
- Orchestrator: 1 collection, 2 series, wire with display orders
