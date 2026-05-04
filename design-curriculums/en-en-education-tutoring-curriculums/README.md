# EN-EN Education & Tutoring Curriculums

Two standalone en-en advanced curriculums exploring education philosophy and language tutoring methodology.

## Curriculums

| # | ID | Title | Desc Tone | Farewell Tone |
|---|---|---|---|---|
| 1 | `QulwtD4YN1zTSnGt` | Education Is Not About Filling a Pail but Lighting a Fire | provocative_question | introspective_guide |
| 2 | `GBLkXkXHJ7HHPrJk` | How to Be a Good Language Tutor | empathetic_observation | practical_momentum |

## Language Pair & Level

- **userLanguage**: en (English speakers)
- **language**: en (learning advanced English vocabulary)
- **Level**: advanced (single-language — all text in English)
- **contentTypeTags**: `[]` (concept-based, no media source)

## Vocabulary Lists (60 unique words, no overlap)

### Curriculum 1 — Education Is Not About Filling a Pail but Lighting a Fire

- **Session 1**: pedagogy, didactic, constructivism, scaffolding, metacognition, heuristic
- **Session 2**: intrinsic, extrinsic, autonomy, self-efficacy, mastery, engagement
- **Session 3**: socratic, dialectical, inquiry, facilitation, elicitation, synthesis
- **Session 4**: progressive, holistic, experiential, differentiation, inclusivity, empowerment
- **Session 5**: transformative, paradigm, praxis, emancipatory, conscientization, liberation

### Curriculum 2 — How to Be a Good Language Tutor

- **Session 1**: scaffolding, comprehensible, acquisition, proficiency, fluency, interlanguage
- **Session 2**: recast, elicitation, corrective, uptake, negotiation, reformulation
- **Session 3**: rapport, affective, motivation, inhibition, fossilization, plateau
- **Session 4**: formative, summative, rubric, diagnostic, backwash, alignment
- **Session 5**: autonomy, metacognitive, self-regulated, differentiated, adaptive, responsive

## Creation Method

Each curriculum was created by a standalone Python script (`create_education_philosophy.py`, `create_language_tutoring.py`) with all text content hand-written inline. Scripts implemented `build_content()`, `validate_content()`, and `main()` functions, calling the helloapi REST API via the shared `api_helpers.create_curriculum()` helper. After successful creation and verification, scripts were deleted.

## Activity Sequence (per session, both curriculums)

Each session has exactly 11 activities in this order:

1. introAudio — Session introduction + vocabulary teaching (500–800 words)
2. viewFlashcards — Visual vocab review (6 words)
3. speakFlashcards — Speaking vocab practice (same vocabList)
4. vocabLevel1 — Vocab exercise level 1
5. vocabLevel2 — Vocab exercise level 2
6. reading — Long passage (800–1200+ words)
7. speakReading — Speak the passage (same text)
8. readAlong — Listen to the passage (same text)
9. writingSentence — Sentence-level writing (4–6 items with prompts)
10. writingParagraph — Paragraph-level writing (instructions + 2–3 prompts)
11. introAudio — Session wrap-up / farewell (session 5: full farewell with vocab review)

## Session Reading Themes

### Curriculum 1

| Session | Theme |
|---------|-------|
| 1 | The Socratic method and the art of questioning |
| 2 | Intrinsic motivation vs. extrinsic rewards in education |
| 3 | Dialectical inquiry and facilitation in the classroom |
| 4 | Progressive education — Montessori, Dewey, and experiential learning |
| 5 | Transformative education and critical pedagogy (Freire) |

### Curriculum 2

| Session | Theme |
|---------|-------|
| 1 | Scaffolding and comprehensible input — Krashen's i+1 in tutoring |
| 2 | Error correction strategies — recasts, elicitation, and explicit correction |
| 3 | Rapport, affective factors, and overcoming fossilization |
| 4 | Assessment in one-on-one tutoring — formative vs. summative approaches |
| 5 | Building learner autonomy and adaptive instruction |

## SQL Queries

```sql
-- Find both curriculums
SELECT id, content->>'title' as title, language, user_language, is_public, created_at
FROM curriculum
WHERE id IN ('QulwtD4YN1zTSnGt', 'GBLkXkXHJ7HHPrJk');

-- Get full content for recreation
SELECT id, content FROM curriculum WHERE id = 'QulwtD4YN1zTSnGt';
SELECT id, content FROM curriculum WHERE id = 'GBLkXkXHJ7HHPrJk';

-- Check for duplicates
SELECT id, content->>'title' as title, created_at
FROM curriculum
WHERE content->>'title' IN (
    'Education Is Not About Filling a Pail but Lighting a Fire',
    'How to Be a Good Language Tutor'
)
  AND uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'
  AND uid NOT LIKE '%_deleted'
ORDER BY content->>'title', created_at;
```

## Recreation Context

- **Spec**: `.kiro/specs/en-en-education-tutoring-curriculums/`
- **UID**: zs5AMpVfqkcfDf8CJ9qrXdH58d73
- **API**: `https://helloapi.step.is/curriculum/create` with `language="en"`, `userLanguage="en"` as top-level body params
- **Auth**: `firebase_token.get_firebase_id_token(UID)` via shared `api_helpers.py`
- **Both curriculums created private** (`is_public: false`) — no `setPublic` calls
- **Standalone** — no collection, no series, no display order
- **Content fully recoverable** via `curriculum/getOne` with each curriculum ID
