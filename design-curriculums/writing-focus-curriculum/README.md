# Writing Focus Curriculum

## Collection
- **ID**: `zf3wbzvi`
- **Title**: Writing Focus

## Series 1: Writing Focus (en-en, advanced)
- **ID**: `n1jopztf`
- **Display Order**: 100

| Order | Curriculum ID | Title |
|---|---|---|
| 0 | `y4uKm7ecm3zhilMH` | Writing Focus: The Architecture of Persuasion |
| 1 | `xlOJ1A9yuIpUpDGS` | Writing Focus: The Paradox of Progress |

## Series 2: Luyện Viết Tiếng Anh (vi-en, intermediate)
- **ID**: `strxp8gn`
- **Display Order**: 200

| Order | Curriculum ID | Title |
|---|---|---|
| 0 | `Llpp3cYA41FCTazM` | Luyện Viết: Sức Mạnh Của Thói Quen |
| 1 | `7CMzgUvCSbrDJZ7g` | Luyện Viết: Nghệ Thuật Giao Tiếp |

## How Content Was Created
- Curriculum type: `writing_focus` — writing as the centerpiece, no speaking activities
- Single-language variant (en-en): 4 sessions (8, 8, 5, 5 activities), `writingParagraph` in every session, prompt escalation from paragraph response → compare/contrast → analytical essay → argumentative capstone
- Bilingual variant (vi-en): 4 sessions (9, 9, 7, 5 activities), `writingSentence` dominates S1-S3, `writingParagraph` in S3-S4, Vietnamese prompts with English responses
- 10 vocab words per curriculum (2 groups of 5), no `speakFlashcards`/`speakReading`/`vocabLevel3`
- Each curriculum created via standalone Python script with hand-written content, validated inline, uploaded via `curriculum/create` API
- Orchestrator script created collection + 2 series, wired everything, set display orders
- All scripts deleted after verification

## SQL Queries

```sql
-- Find the collection
SELECT id, title, is_public FROM curriculum_collections WHERE id = 'zf3wbzvi';

-- Find both series
SELECT cs.id, cs.title, cs.display_order
FROM curriculum_series cs
JOIN curriculum_collection_series ccs ON ccs.curriculum_series_id = cs.id
WHERE ccs.curriculum_collection_id = 'zf3wbzvi'
ORDER BY cs.display_order;

-- Find all curriculums
SELECT c.id, c.content->>'title' as title, c.display_order, c.language, c.user_language
FROM curriculum c
JOIN curriculum_series_items csi ON csi.curriculum_id = c.id
WHERE csi.curriculum_series_id IN ('n1jopztf', 'strxp8gn')
ORDER BY csi.curriculum_series_id, c.display_order;

-- Verify language homogeneity
SELECT * FROM curriculum_series_language_list WHERE id IN ('n1jopztf', 'strxp8gn');
```

## Recreation
To recreate, write 4 Python scripts following the `writing_focus` curriculum type spec in `.kiro/specs/writing-focus-curriculum/`. Each script needs: 10 vocab words (2×5), 3 reading passages (MODEL_TEXT_1, MODEL_TEXT_2, FULL_ARTICLE), 4 sessions with hand-written introAudio/description/preview/writing prompts, inline validate() function, and API call to `curriculum/create`. Then run an orchestrator to create collection + 2 series + wire everything.
