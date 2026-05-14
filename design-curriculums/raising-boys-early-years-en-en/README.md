# Raising Boys: The Early Years (en-en advanced)

Two hand-crafted English-only advanced curriculums drawn from Steve Biddulph's
*Raising Boys*, scoped to the developmental window the user framed as ages 4 to 7
and split deliberately around Biddulph's age-six pivot between Stage 1
(*Tender Years*) and Stage 2 (*Father Years*). Both curriculums are private and
were created via `curriculum/create` with `language="en"` and
`userLanguage="en"` for UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`.

## Curriculum identifiers

| Slot | Curriculum id | Title | Age band | Display order |
|---|---|---|---|---|
| A | `LnjhbFEHekIbWRnp` | Raising Boys 4–5: The Last of the Tender Years | 4–5 | 1 |
| B | `JiVfxUyaWilVT9bm` | Raising Boys 6–7: When the Father Years Switch On | 6–7 | 2 |

## Host series

| Field | Value |
|---|---|
| Series id | `fry4z95a` |
| Series title | Raising Boys: The Early Years |
| Series description tone | `metaphor_led` |
| Members | Curriculum_A (display_order 1), Curriculum_B (display_order 2) |
| Public | No |

## Description tone assignments (design §D8)

| Item | Tone |
|---|---|
| Curriculum_A description headline | `empathetic_observation` |
| Curriculum_B description headline | `provocative_question` |
| Series description headline | `metaphor_led` |

All three tones are distinct (Property 28 / Requirements 9.4, 13.1, 13.2, 13.3).

## Farewell introAudio register assignments (design §D9)

| Curriculum | Farewell register |
|---|---|
| A | `introspective_guide` |
| B | `practical_momentum` |

## Vocabulary partitions (design §D5)

### Curriculum_A — Tender Years 4–5 (30 items, 10 per session)

**Session 1 — Naming the inner weather (emotional attunement):**
attunement, co-regulation, to soothe, meltdown, overwhelm, to validate,
disappointment, frustration, composure, to acknowledge.

**Session 2 — The language explosion and imaginative play:**
narrative, to scaffold, vocabulary, pretend play, make-believe, to elaborate,
articulate, dialogue, imagination, to recount.

**Session 3 — Bodies, big feelings, and somatic regulation:**
boisterous, tantrum, to wind down, nervous system, to settle, vigorous,
physical affection, restless, to discharge, proprioception.

### Curriculum_B — Father Years 6–7 (30 items, 10 per session)

**Session 1 — Switching on: a boy looks toward his father:**
identification, role model, mentor, apprenticeship, masculinity, to emulate,
belonging, aspirational, presence, to initiate.

**Session 2 — Rough-and-tumble: structured play and trust:**
rough-and-tumble, horseplay, roughhousing, boundary-setting, playful resistance,
physicality, restraint, consensual, to negotiate, to wrestle.

**Session 3 — Stepping back, stepping up: early self-discipline:**
self-discipline, delay of gratification, competence, autonomy, accountability,
to internalise, consequence, disposition, to step back, to follow through.

Cross-curriculum check: zero overlap between the two 30-item lists; total of
60 distinct case-folded entries (verified post-creation via `curriculum/getOne`).

## Top-level content tags (every curriculum)

```
contentTypeTags    = []
lengthTags         = ["medium"]
skillFocusTags     = ["balanced_skills"]
difficultyTags     = ["advanced", "vocab_advanced", "reading_advanced", "writing_advanced"]
```

## Creation method

The run pipeline lived in five run-only Python files under
`raising-boys-early-years-en-en/`:

```
raising_boys_helpers.py              # structure-only helpers (make_*, recursive_strip_keys, post_to_api)
validate_raising_boys.py             # pre/post-upload validators (Properties 1-23 + 30b)
create_raising_boys_a_tender_years.py  # Curriculum_A literal-string content + build_content()
create_raising_boys_b_father_years.py  # Curriculum_B literal-string content + build_content()
orchestrate_raising_boys.py          # pipeline driver: duplicate checks, series, dispatch, validation, DB verification
```

The pipeline ran in this order:

1. Duplicate checks against `curriculum` and `curriculum_series` via MCP postgres
   (zero rows on both → proceed).
2. `curriculum-series/create` with the `metaphor_led` 235-char description
   (≤ 255 chars per Requirement 12.3) → series id `fry4z95a`.
3. `build_content()` for each curriculum, which assembled the 5-session arc
   from literal-string constants via the `make_*` helpers, ran
   `recursive_strip_keys` plus `pre_upload_validate` (Properties 1, 2, 3, 4,
   5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 30b),
   and returned the content dict.
4. `curriculum/create` for A then B (both returned 2xx with an `id`).
5. `curriculum-series/addCurriculum` for both curriculums under the new series.
6. `curriculum/setDisplayOrder` setting A=1 and B=2.
7. `curriculum/getOne` for each id followed by `post_upload_validate` —
   both `[A]` and `[B]` reported `post-upload PASS`.
8. The four §"Verification SQL" queries (locate-by-language-title,
   difficultyTags / contentTypeTags shape, parent purity, series
   description / language pair) were run via MCP postgres and all
   returned the design's pass criteria.
9. Cross-curriculum vocabulary uniqueness check on the published
   `viewFlashcards` activities returned 60 distinct entries with zero overlap.

Per script-lifecycle rules, the five run scripts are deleted only after the
DB rows are confirmed. The deletion step is Task 9.2 of `tasks.md`.

`setPublic` is never called and is statically forbidden in any script
(Property 24 / Requirement 11.1). The collection-level displayOrder endpoint
is never called and is statically forbidden in any script (Property 27 /
Requirement 12.5). Both new curriculums and the host series remain private.

## Verification SQL

Run any of the queries below via MCP postgres (or `psql`) to confirm the
state of the two rows.

### §14.1 Locate by language and title

```sql
SELECT id,
       uid,
       content->>'title' AS title,
       language,
       user_language,
       is_public
FROM   curriculum
WHERE  language = 'en'
  AND  user_language = 'en'
  AND  content->>'title' IN (
         'Raising Boys 4–5: The Last of the Tender Years',
         'Raising Boys 6–7: When the Father Years Switch On'
       )
  AND  uid NOT LIKE '%\_deleted' ESCAPE '\'
ORDER  BY content->>'title';
```

Expected: exactly 2 rows, both with `language='en'`, `user_language='en'`,
`is_public=false`, `uid='zs5AMpVfqkcfDf8CJ9qrXdH58d73'`.

### §14.2 difficultyTags / contentTypeTags shape

```sql
SELECT id,
       content->>'title'                              AS title,
       (content->'difficultyTags') @> '["advanced"]'::jsonb AS has_advanced,
       jsonb_typeof(content->'contentTypeTags')      AS ctype_tags_kind,
       content->'contentTypeTags'                    AS ctype_tags
FROM   curriculum
WHERE  id IN ('LnjhbFEHekIbWRnp', 'JiVfxUyaWilVT9bm');
```

Expected: 2 rows, both with `has_advanced=true`, `ctype_tags_kind='array'`,
`ctype_tags=[]`.

### Series wiring

```sql
SELECT cs.id   AS series_id,
       cs.title AS series_title,
       c.id    AS curriculum_id,
       c.content->>'title' AS curriculum_title,
       c.display_order
FROM   curriculum_series cs
JOIN   curriculum_series_items csi ON csi.curriculum_series_id = cs.id
JOIN   curriculum c                ON c.id = csi.curriculum_id
WHERE  cs.title = 'Raising Boys: The Early Years'
ORDER  BY c.display_order;
```

Expected: 2 rows, series_id `fry4z95a`, curriculum_ids
`LnjhbFEHekIbWRnp` (display_order 1) and `JiVfxUyaWilVT9bm`
(display_order 2).

### Series language purity (Property 25, 26)

```sql
SELECT id, language_list, user_language_list
FROM   curriculum_series_language_list
WHERE  id = 'fry4z95a';
```

Expected: 1 row with `language_list = ['en']`, `user_language_list = ['en']`.

## Recreation context

If the rows above are accidentally lost, the curriculums can be recreated
from `curriculum/getOne` against `LnjhbFEHekIbWRnp` and
`JiVfxUyaWilVT9bm` (both still owned by UID
`zs5AMpVfqkcfDf8CJ9qrXdH58d73`). The persisted `content` field is the
full curriculum JSON minus the platform-added generated keys
(`mp3Url`, `illustrationSet`, `chapterBookmarks`, `segments`,
`whiteboardItems`, `userReadingId`, `lessonUniqueId`, `curriculumTags`,
`taskId`, `imageId`, `practiceMinutes`, `practiceTime`).

The locked design pointers are:

- `.kiro/specs/raising-boys-early-years-en-en/requirements.md`
- `.kiro/specs/raising-boys-early-years-en-en/design.md`
- `.kiro/specs/raising-boys-early-years-en-en/tasks.md`

Authentication pattern (recreation):

```python
import sys
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
token = get_firebase_id_token(UID)
# POST to https://helloapi.step.is/curriculum/getOne with
# {"id": "<id>", "uid": UID, "firebaseIdToken": token}
```
