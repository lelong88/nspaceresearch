# fr-fr — French-French Curriculum Collection

Created: 2026-04-16
Language: fr (French), User Language: fr (French)
Single-language pair. All content entirely in French.
Vocabulary from formal/literary French registers (soutenu, littéraire).
Upper-intermediate to advanced level.
Each curriculum: 18 French vocab words, 6 per session.

## Collection IDs

| Collection | ID |
|---|---|
| E: Littérature et Culture Avancée | bsofq17k |
| F: Maîtrise Professionnelle | 6ad3953v |

## Collection E: Littérature et Culture Avancée

### E1: Analyse Littéraire (n2xt5ou7)

| # | Title | ID | Display Order |
|---|---|---|---|
| 1 | Techniques narratives | yEjlksrY1FNVQVPI | 1 |
| 2 | Formes poétiques | iMnvYHQL1QhKqhqQ | 2 |
| 3 | Procédés rhétoriques | lvr8hP6CG1REHXer | 3 |
| 4 | Critique littéraire | VH2W0Y7bWYZJDMab | 4 |
| 5 | Littérature comparée | pJc6askCjDzW2DqN | 5 |

### E2: Philosophie et Histoire Intellectuelle (yl6czv2i)

| # | Title | ID | Display Order |
|---|---|---|---|
| 1 | Les Lumières | wR0TOu7BAYlRMT5R | 1 |
| 2 | Existentialisme | wgSAiCIMAPf91f9h | 2 |
| 3 | Phénoménologie | NZZQ4RvyE5XHKgry | 3 |
| 4 | Philosophie politique | gVbWfa1VPWSIH61j | 4 |
| 5 | Débats contemporains | X0713WQ2b6GCCBPv | 5 |

### E3: Art, Cinéma et Critique Culturelle (xzp8grcq)

| # | Title | ID | Display Order |
|---|---|---|---|
| 1 | Mouvements artistiques | PkE7dqwPmkMz1rsy | 1 |
| 2 | Théorie du cinéma | Pa5jmrJy2vQixH8m | 2 |
| 3 | Critique musicale | 5PdiQX26y8PJyTM4 | 3 |
| 4 | Identité culturelle | dC669mAoLUSKfHXm | 4 |
| 5 | Analyse des médias | mhwfpauUysXGGdjZ | 5 |

## Collection F: Maîtrise Professionnelle

### F1: Droit et Affaires Avancés (ew1mmrus)

| # | Title | ID | Display Order |
|---|---|---|---|
| 1 | Droit des sociétés | Lcw3ezE7GQNTb96j | 1 |
| 2 | Analyse financière | aj8mXe5nniElpboD | 2 |
| 3 | Management stratégique | Oh7uKUoXcMcHsCG1 | 3 |
| 4 | Droit du travail | UWQKbC0DNsMz0rCW | 4 |
| 5 | Entrepreneuriat | uIgrPDU0CxHRGw9Q | 5 |

### F2: Science et Innovation (yn1wrbmh)

| # | Title | ID | Display Order |
|---|---|---|---|
| 1 | Méthodologie de la recherche | Q6FpZD8YIyfoESpK | 1 |
| 2 | Biotechnologie | rl52jW3STk0VJiZb | 2 |
| 3 | Intelligence artificielle | A77vCeiPPkvH3YgX | 3 |
| 4 | Science du climat | 7BMY0TRnMeDS8qx5 | 4 |
| 5 | Avancées médicales | KY6e7h3QKn5skME5 | 5 |

### F3: Médias, Journalisme et Discours Public (uu3jixu3)

| # | Title | ID | Display Order |
|---|---|---|---|
| 1 | Journalisme d'investigation | t1GWdk0TCHygji9Z | 1 |
| 2 | Ecriture editoriale | JmYh19nzTRZ4FyGT | 2 |
| 3 | Prise de parole | ZFqWyNOvoKlMwmiL | 3 |
| 4 | Techniques de debat | 41tbvSXggJFSO5Sh | 4 |
| 5 | Medias numeriques | ZsKUEKB0qef9ZVTO | 5 |

## SQL Queries

```sql
-- All fr-fr curriculums
SELECT c.id, c.content->>'title' as title, c.display_order
FROM curriculum c
WHERE c.uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'
AND c.uid NOT LIKE '%_deleted'
AND c.language = 'fr' AND c.user_language = 'fr'
ORDER BY c.created_at;

-- Duplicate check
SELECT c.content->>'title' as title, count(*) as cnt
FROM curriculum c
WHERE c.uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'
AND c.uid NOT LIKE '%_deleted'
AND c.language = 'fr' AND c.user_language = 'fr'
GROUP BY c.content->>'title'
HAVING count(*) > 1;

-- Series curriculum counts
SELECT cs.id AS series_id, cs.title, COUNT(csc."curriculumId") AS curriculum_count
FROM curriculum_series cs
LEFT JOIN curriculum_series_curriculums csc ON cs.id = csc."curriculumSeriesId"
WHERE cs.id IN ('n2xt5ou7','yl6czv2i','xzp8grcq','ew1mmrus','yn1wrbmh','uu3jixu3')
GROUP BY cs.id, cs.title
ORDER BY cs.title;

-- Language homogeneity
SELECT * FROM curriculum_series_language_list
WHERE id IN ('n2xt5ou7','yl6czv2i','xzp8grcq','ew1mmrus','yn1wrbmh','uu3jixu3');

-- Display orders
SELECT c.id, c.content->>'title' as title, c.display_order
FROM curriculum c
JOIN curriculum_series_curriculums csc ON c.id = csc."curriculumId"
WHERE csc."curriculumSeriesId" IN ('n2xt5ou7','yl6czv2i','xzp8grcq','ew1mmrus','yn1wrbmh','uu3jixu3')
AND c.uid NOT LIKE '%_deleted'
ORDER BY csc."curriculumSeriesId", c.display_order;
```

## Recreation Instructions

1. **Infrastructure** (collections + series): Run `orchestrator.py`. Creates 2 collections and 6 series, wires them together, sets display orders. IDs logged to stdout.
2. **Curriculums**: All creation scripts have been deleted after successful execution. To recreate:
   - Query the DB for curriculum content via `curriculum/getOne` using the curriculum ID
   - Or query MCP postgres: `SELECT id, content->>'title', content FROM curriculum WHERE uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73' AND language = 'fr' AND user_language = 'fr' AND uid NOT LIKE '%_deleted'`
3. **Validation**: Use `validate_content.py` to check content JSON before upload.
4. **API helpers**: Use `api_helpers.py` for all API calls.

## Creation Method

- Orchestrator: `fr-fr/orchestrator.py` — created 2 collections, 6 series
- Batch creator: `fr-fr/create_f3_and_run.py` (imports from create_all_fr_fr.py, create_remaining.py, create_f_series.py, create_f2f3_remaining.py)
- F3-5 retry: manual retry after timeout
- All validated against content corruption rules before upload
- 30/30 curriculums created successfully
