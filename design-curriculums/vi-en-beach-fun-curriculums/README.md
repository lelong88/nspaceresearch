# vi-en Beach Fun Curriculums — Vui Bên Bờ Biển

Three vi-en preintermediate curriculums on the "having fun on the beach"
theme, organised into a single Vietnamese-titled series.

Language pair: `userLanguage="vi"`, `language="en"` (Vietnamese speakers
learning English).

UID: `zs5AMpVfqkcfDf8CJ9qrXdH58d73`

## a. Series

| Field | Value |
|---|---|
| Series id | `u36dcktg` |
| Vietnamese title | Vui Bên Bờ Biển |
| Description tone | `bold_declaration` |
| Visibility | `is_public = false` |

## b. Curriculums

| Display order | Curriculum id | Vietnamese title |
|:---:|---|---|
| 1 | `HPHIYGB0rds7YUoS` | Vui Chơi & Thể Thao Bãi Biển |
| 2 | `u1fpdD30ittA825B` | Ăn Uống & Thư Giãn Bên Biển |
| 3 | `1sRBwHUE8VIbMpWv` | Hoàng Hôn & Lửa Trại Bên Biển |

All three: `language="en"`, `userLanguage="vi"`, `is_public=false`,
preintermediate level, 4-session speaking-focus pattern.

## c. Display orders

Locked in design.md, written by the orchestrator via `curriculum/setDisplayOrder`
after `curriculum-series/addCurriculum`:

| Curriculum | Display order |
|---|:---:|
| Vui Chơi & Thể Thao Bãi Biển (Beach Activities) | 1 |
| Ăn Uống & Thư Giãn Bên Biển (Beach Food) | 2 |
| Hoàng Hôn & Lửa Trại Bên Biển (Beach Evening) | 3 |

The order follows a natural beach-day progression: morning/midday active
play → afternoon food and rest → sunset and evening gathering.

## d. Vocabulary lists (15 per curriculum, partitioned 5/5/5 into W1/W2/W3)

### 1 — Vui Chơi & Thể Thao Bãi Biển (Beach Activities & Sports)

| Group | Session | Words |
|---|:---:|---|
| W1 | 1 | splash, wave, swim, paddle, float |
| W2 | 2 | surf, board, snorkel, goggles, fin |
| W3 | 3 | dive, sandcastle, frisbee, volleyball, kite |

### 2 — Ăn Uống & Thư Giãn Bên Biển (Beach Food & Relaxation)

| Group | Session | Words |
|---|:---:|---|
| W1 | 1 | picnic, basket, towel, sandals, sunscreen |
| W2 | 2 | grill, snack, coconut, smoothie, umbrella |
| W3 | 3 | lounge, tan, doze, breeze, hammock |

### 3 — Hoàng Hôn & Lửa Trại Bên Biển (Sunset & Evening Beach Fun)

| Group | Session | Words |
|---|:---:|---|
| W1 | 1 | sunset, twilight, shore, tide, glow |
| W2 | 2 | bonfire, firelight, marshmallow, blanket, gather |
| W3 | 3 | stargaze, lantern, guitar, laughter, drift |

Total: 45 unique lowercase ASCII English words. Zero pairwise overlap
between curriculums (verified post-upload via `curriculum/getOne`).

## e. Description tone assignments

Locked in design.md. Each curriculum opens with an ALL-CAPS Vietnamese
headline (3–12 words) on its own line, using a tone from the platform's
Tone_Palette. No two adjacent curriculums share a tone, and no tone is
used by more than one of the three.

| Display order | Curriculum | Headline tone |
|:---:|---|---|
| 1 | Beach Activities | `vivid_scenario` |
| 2 | Beach Food | `empathetic_observation` |
| 3 | Beach Evening | `metaphor_led` |

The series description uses `bold_declaration`, distinct from the
curriculum 1 headline tone.

## f. Farewell tone assignments

Locked in design.md. Each Session 4 (review) introAudio uses one of the
five Farewell_Palette registers; exactly three are selected, each used
once.

| Curriculum | Farewell register |
|---|---|
| Beach Activities | `team_building_energy` |
| Beach Food | `practical_momentum` |
| Beach Evening | `quiet_awe` |

Unused: `introspective_guide`, `warm_accountability`.

## g. Creation method summary

Created via the helloapi REST API (`https://helloapi.step.is`) using a
6-script Python pipeline run from this folder. All learner-facing text
was hand-written as literal Python strings — no f-strings, no
`.format()`, no shared text templates. Locked design decisions (vocab
lists, titles, tones, display orders) lived as module-level constants in
the orchestrator and were mirrored as literal values in each
per-curriculum builder.

Pipeline order (per `orchestrate_beach_fun.py`):

1. `curriculum-series/listAll` → reuse seriesId if title match exists,
   else `curriculum-series/create` with the locked title and
   `bold_declaration` Vietnamese description.
2. For each curriculum in display order (`activities`, `food`,
   `evening`):
   - `build_content()` from the per-curriculum module assembles the
     4-session content via `beach_helpers` (structure-only helpers, no
     text templating) and runs strip-keys cleanup + re-verify.
   - `pre_upload_validate(content, label)` runs the full Requirement-15
     check set; failures abort the run.
   - `curriculum/create` with `language="en"`, `userLanguage="vi"`,
     `content=json.dumps(content)`, no `isPublic`.
   - Duplicate check via `curriculum/list` filtered on
     `content.title == <locked title>` and uid not ending `_deleted`;
     keep earliest, remove + delete the rest.
   - `curriculum-series/addCurriculum` then
     `curriculum/setDisplayOrder` with the locked integer (1, 2, or 3).
3. `curriculum/getOne` per id → `post_upload_validate` (lenient on the
   four platform-managed tag fields, since the platform recomputes them
   after upload).

Authentication: every API call carries a Firebase ID token obtained via
`firebase_token.get_firebase_id_token("zs5AMpVfqkcfDf8CJ9qrXdH58d73")`.

Pipeline returned `0` (all post-upload validations passed).

## h. SQL queries to find the series and curriculums in the DB

Series + member curriculums in display order:

```sql
SELECT
    csi.curriculum_series_id,
    csi.curriculum_id,
    c.uid,
    c.language,
    c.user_language,
    c.is_public,
    c.display_order,
    c.content->>'title' AS title
FROM curriculum_series_items csi
JOIN curriculum c ON c.id = csi.curriculum_id
WHERE csi.curriculum_series_id = 'u36dcktg'
  AND NOT (c.uid LIKE '%\_deleted')
ORDER BY c.display_order ASC;
```

Series-level homogeneity (single row expected, `language_list=['en']`,
`user_language_list=['vi']`):

```sql
SELECT id, title, language_list, user_language_list
FROM curriculum_series_language_list
WHERE id = 'u36dcktg';
```

Series difficulty gap (zero rows expected — all preintermediate):

```sql
SELECT series_id, series_title, curriculum_id, curriculum_title,
       curriculum_level, series_max_level, level_gap
FROM curriculum_series_level_gap
WHERE series_id = 'u36dcktg';
```

Find a single curriculum's full content:

```sql
SELECT id, content
FROM curriculum
WHERE id IN ('HPHIYGB0rds7YUoS', 'u1fpdD30ittA825B', '1sRBwHUE8VIbMpWv');
```

Find the series by title (case-sensitive, non-deleted):

```sql
SELECT id, uid, title, description
FROM curriculum_series
WHERE title = 'Vui Bên Bờ Biển'
  AND NOT (uid LIKE '%\_deleted');
```

## i. Recreation context

If the series or any curriculum is lost, recreate from this README plus
the spec at `/home/ubuntu/nspaceresearch/design-curriculums/.kiro/specs/vi-en-beach-fun-curriculums/`.
The spec contains:

- `requirements.md` — 16 numbered requirement clusters that govern every
  decision below.
- `design.md` — the locked decisions (vocabulary partitions, titles,
  tones, display orders, schema shapes, validation strategy).
- `tasks.md` — the 36-task implementation plan that produced this
  folder.

Locked inputs needed to recreate:

- UID: `zs5AMpVfqkcfDf8CJ9qrXdH58d73`
- Language pair: `userLanguage="vi"`, `language="en"`
- Series title: `Vui Bên Bờ Biển` (Vietnamese, locked)
- Series description tone: `bold_declaration`
- Curriculum titles, vocab lists, description tones, farewell tones,
  display orders: see sections (a)–(f) above.
- Difficulty: preintermediate; `lengthTags=["medium"]`,
  `skillFocusTags=["speaking_focus"]`,
  `difficultyTags=["preintermediate", "vocab_preintermediate", "reading_preintermediate"]`
  at upload time. The platform recomputes these fields after
  `curriculum/create` (`lengthTags` from content size, etc.) — that is
  expected and the post-upload validator is lenient on them.

Helper modules used (deleted after a successful run per the spec's
script-lifecycle rule):

- `beach_helpers.py` — non-text structure helpers + `post_to_api`.
- `validate_content.py` — pre-upload (strict) and post-upload
  (platform-aware lenient) validators.
- `create_beach_activities.py` / `create_beach_food.py` /
  `create_beach_evening.py` — per-curriculum content builders.
- `orchestrate_beach_fun.py` — top-level orchestrator.

Recovery path: if scripts are gone but the DB still holds the
curriculums, all learner-facing text is recoverable via
`curriculum/getOne` for each id (or the SQL query in section h).
