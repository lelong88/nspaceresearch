# Effective Learning Curriculum

10 curriculums (5 learning science topics × 2 language pairs: en-en, vi-en) organized into 2 collections with 2 existing "Get Comfortable Being Uncomfortable" curriculums.

## Status

✅ Complete — All 10 curriculums created, verified, and organized into 2 collections.

## Curriculums Created

| # | Topic | en-en ID | vi-en ID |
|---|---|---|---|
| 1 | Grit (podcast) | `NwGqhGPTLqf86mPv` | `mF7QKxEONRjvYlgF` |
| 2 | Growth Mindset | `LvXWRDjOGkJA2Ics` | `Pv14gqxcurn3ORDS` |
| 3 | Desirable Difficulties | `Ctx4MJM18a1iuw6W` | `6rO5xp3ZiYLuU41k` |
| 4 | Productive Struggle | `DQ9IXIpzfKxprt3f` | `7qmrcN3jezI1xxIp` |
| 5 | Zone of Proximal Development | `4LkcmlHc9PNZ14DT` | `6ch7UhPQqU1oP2Kr` |

## Collections Created

| Collection | ID | Language | display_order |
|---|---|---|---|
| How to Learn Effectively | `qq3as66z` | en-en | -999 |
| Học Cách Học Hiệu Quả | `ucyiavdp` | vi-en | -999 |

## Collection Layout

**en-en "How to Learn Effectively" (`qq3as66z`):**

| display_order | Curriculum | ID |
|---|---|---|
| 0 | Growth Mindset | `LvXWRDjOGkJA2Ics` |
| 1 | Get Comfortable Being Uncomfortable | `VdgEbnzAassbpRPa` |
| 2 | Desirable Difficulties | `Ctx4MJM18a1iuw6W` |
| 3 | Productive Struggle | `DQ9IXIpzfKxprt3f` |
| 4 | Zone of Proximal Development | `4LkcmlHc9PNZ14DT` |
| 5 | Grit | `NwGqhGPTLqf86mPv` |

**vi-en "Học Cách Học Hiệu Quả" (`ucyiavdp`):**

| display_order | Curriculum | ID |
|---|---|---|
| 0 | Tư Duy Phát Triển | `Pv14gqxcurn3ORDS` |
| 1 | Bước Ra Khỏi Vùng An Toàn | `2hcxuPuBD1g1F3Zk` |
| 2 | Khó Khăn Đáng Mong Muốn | `6rO5xp3ZiYLuU41k` |
| 3 | Vật Lộn Hiệu Quả | `7qmrcN3jezI1xxIp` |
| 4 | Vùng Phát Triển Gần | `6ch7UhPQqU1oP2Kr` |
| 5 | Grit | `mF7QKxEONRjvYlgF` |

## Podcast Cross-Listings

- en-en Grit (`NwGqhGPTLqf86mPv`) → podcast collection `mqdqxuyp`
- vi-en Grit (`mF7QKxEONRjvYlgF`) → podcast collection `1pspi6gt`

## SQL Queries

```sql
-- Find all 10 curriculums
SELECT id, content->>'title' as title, language, user_language, is_public, created_at
FROM curriculum
WHERE id IN (
    'NwGqhGPTLqf86mPv', 'mF7QKxEONRjvYlgF',
    'LvXWRDjOGkJA2Ics', 'Pv14gqxcurn3ORDS',
    'Ctx4MJM18a1iuw6W', '6rO5xp3ZiYLuU41k',
    'DQ9IXIpzfKxprt3f', '7qmrcN3jezI1xxIp',
    '4LkcmlHc9PNZ14DT', '6ch7UhPQqU1oP2Kr'
)
ORDER BY created_at;

-- Find both collections
SELECT id, title, display_order
FROM curriculum_collections
WHERE id IN ('qq3as66z', 'ucyiavdp');

-- Find en-en collection members
SELECT c.id, c.content->>'title' as title, c.display_order
FROM curriculum c
JOIN curriculum_collection_items cci ON cci.curriculum_id = c.id
WHERE cci.curriculum_collection_id = 'qq3as66z'
ORDER BY c.display_order;

-- Find vi-en collection members
SELECT c.id, c.content->>'title' as title, c.display_order
FROM curriculum c
JOIN curriculum_collection_items cci ON cci.curriculum_id = c.id
WHERE cci.curriculum_collection_id = 'ucyiavdp'
ORDER BY c.display_order;

-- Get full content for any curriculum
SELECT content FROM curriculum WHERE id = '<curriculum_id>';
```

## How Content Was Created

Each curriculum was created by a standalone Python script with all text content hand-written inline. Scripts implemented `build_content()`, `validate()`, `strip_keys()`, and `create()` functions. After successful creation and verification, all scripts were deleted.

## Recreation Context

- Spec: `.kiro/specs/effective-learning-curriculum/`
- Auth: `firebase_token.get_firebase_id_token(UID)` with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`
- API: `https://helloapi.step.is/curriculum/create` with `language="en"` and `userLanguage` as top-level body params
- All curriculums created private (`is_public: false`)
- Content fully recoverable via `curriculum/getOne` with each curriculum ID

## Vocabulary by Topic

Each topic has 18 unique English vocabulary words shared between en-en and vi-en versions:

- **Grit**: perseverance, stamina, tenacity, resilience, diligence, fortitude, passion, aptitude, deliberate, consistency, endurance, determination, grit, predictor, achievement, talent, potential, mindset
- **Growth Mindset**: neuroplasticity, cognition, adaptability, persevere, incremental, cultivate, feedback, setback, embrace, evolve, mastery, trajectory, fixed, innate, malleable, flourish, threshold, paradigm
- **Desirable Difficulties**: retrieval, spacing, interleaving, encoding, consolidation, retention, desirable, counterintuitive, effortful, durable, fluency, illusion, interference, generation, variability, transfer, metacognition, calibration
- **Productive Struggle**: scaffold, hypothesis, exploration, intuition, schema, construct, productive, failure, consolidate, activate, prior, explicit, struggle, conventional, innovation, cognitive, engagement, autonomy
- **ZPD**: proximal, mediation, internalization, scaffolding, competence, zone, collaborative, guidance, apprenticeship, modeling, reciprocal, dynamic, developmental, sociocultural, appropriation, regulation, agency, potential

## Full Catastrophe Living (added separately)

Two additional curriculums based on Jon Kabat-Zinn's "Full Catastrophe Living" — mindfulness-based stress reduction and changing your relationship with pain.

| Language Pair | Level | ID | Series |
|---|---|---|---|
| en-en | upperintermediate | `9or41nCXqmbU9cNS` | Mind & Society (`kxxkeo1f`, display_order 1200) |
| vi-en | intermediate | `a1pDbYdr6xSiCUD6` | Tâm Lý & Phát Triển Bản Thân (`6k2ij0ut`, display_order 100) |

Both also added to Featured collection (`73e9d0aa`).

Description tone: empathetic_observation (both). Farewell tone: introspective guide (en-en), quiet awe (vi-en).

Vocabulary (shared across both): mindfulness, awareness, reactivity, autopilot, avoidance, stillness, equanimity, impermanence, compassion, surrender, acceptance, vulnerability, catastrophe, resilience, embodiment, wholeness, liberation, transformation

```sql
-- Find Full Catastrophe Living curriculums
SELECT id, content->>'title' as title, language, user_language, display_order
FROM curriculum WHERE id IN ('9or41nCXqmbU9cNS', 'a1pDbYdr6xSiCUD6');
```
