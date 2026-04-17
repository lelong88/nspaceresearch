# de-de — German-German Curriculum Collection

Created: 2026-04-16
Language: de (German), User Language: de (German)
Single-language pair. All content entirely in German.
Vocabulary from formal/academic German registers (Bildungssprache, Fachsprache).
Upper-intermediate to advanced level.
Each curriculum: 18 German vocab words, 6 per session.

## Collection IDs

| Collection | ID |
|---|---|
| E: Literatur und Fortgeschrittene Kultur | wd23cti7 |
| F: Professionelle Meisterschaft | whtf608r |

## Collection E: Literatur und Fortgeschrittene Kultur

### E1: Literarische Analyse (30kl0nzj)

| # | Title | ID | Display Order |
|---|---|---|---|
| 1 | Erzähltechniken | hVNXkPpKSMDxmeJl | 1 |
| 2 | Poetische Formen | A6vlUBptcAirU6rG | 2 |
| 3 | Rhetorische Mittel | EI7YR8HfBbOo8J39 | 3 |
| 4 | Literaturkritik | wFyRn73dIzQHRwDe | 4 |
| 5 | Vergleichende Literaturwissenschaft | JmDlYIQVi2TJ8nbw | 5 |

### E2: Philosophie und Geistesgeschichte (g6xl6u6j)

| # | Title | ID | Display Order |
|---|---|---|---|
| 1 | Die Aufklärung | gn4KKca50Hhjr7rR | 1 |
| 2 | Existenzialismus | 0jblkn8feIrk44LX | 2 |
| 3 | Phänomenologie | qNrkvqAt8c9cUuSH | 3 |
| 4 | Politische Philosophie | LuPm1n2U85oWEdY5 | 4 |
| 5 | Zeitgenössische Debatten | Qe7s8tN8miJgGkhK | 5 |

### E3: Kunst, Film und Kulturkritik (0c4l8ofp)

| # | Title | ID | Display Order |
|---|---|---|---|
| 1 | Kunstbewegungen | 8SxZLDOxmo1mmK4c | 1 |
| 2 | Filmtheorie | 6NBdVAvjVbc9nPIF | 2 |
| 3 | Musikkritik | 3N2EIEuE9GmLRaSK | 3 |
| 4 | Kulturelle Identität | iNVubA55jT54Otia | 4 |
| 5 | Medienanalyse | id4HIEejnikvBK8O | 5 |

## Collection F: Professionelle Meisterschaft

### F1: Fortgeschrittenes Wirtschaftsrecht (khe92j6c)

| # | Title | ID | Display Order |
|---|---|---|---|
| 1 | Gesellschaftsrecht | IOaQQCU8Ef6xzTX0 | 1 |
| 2 | Finanzanalyse | JWVvYH2Cdy4Y5T2t | 2 |
| 3 | Strategisches Management | jX2NrYTUngzLNXsU | 3 |
| 4 | Arbeitsrecht | RtLm5KtgwFp3bZFw | 4 |
| 5 | Unternehmertum | rdWYN0k5MYN6Caxw | 5 |

### F2: Wissenschaft und Innovation (xpeg92h6)

| # | Title | ID | Display Order |
|---|---|---|---|
| 1 | Forschungsmethodik | grKGwoZe0ByHWOZu | 1 |
| 2 | Biotechnologie | dq6FZpJyPuq1daJV | 2 |
| 3 | Künstliche Intelligenz | L4xWN5wM7BTndcPy | 3 |
| 4 | Klimawissenschaft | YbNdYCLvEHUCqFwM | 4 |
| 5 | Medizinische Fortschritte | tvZw0NTclZjQfie1 | 5 |

### F3: Medien, Journalismus und öffentlicher Diskurs (07e38ade)

| # | Title | ID | Display Order |
|---|---|---|---|
| 1 | Investigativer Journalismus | 4KRb7wqDKtkoAnMl | 1 |
| 2 | Meinungsjournalismus | ttKcKjjry6nZAM2l | 2 |
| 3 | Redekunst | vscUlzSE3g5qJ5ZA | 3 |
| 4 | Debattentechniken | qUmmb5YH60eC35xt | 4 |
| 5 | Digitale Medien | 6WrlM3oBnY9sqclJ | 5 |

## SQL Queries

```sql
-- All de-de curriculums
SELECT c.id, c.content->>'title' as title, c.display_order
FROM curriculum c
WHERE c.uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'
AND c.uid NOT LIKE '%_deleted'
AND c.language = 'de' AND c.user_language = 'de'
ORDER BY c.created_at;

-- Duplicate check
SELECT c.content->>'title' as title, count(*) as cnt
FROM curriculum c
WHERE c.uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'
AND c.uid NOT LIKE '%_deleted'
AND c.language = 'de' AND c.user_language = 'de'
GROUP BY c.content->>'title'
HAVING count(*) > 1;

-- Series curriculum counts
SELECT cs.id AS series_id, cs.title, COUNT(csi.curriculum_id) AS curriculum_count
FROM curriculum_series cs
LEFT JOIN curriculum_series_items csi ON cs.id = csi.curriculum_series_id
WHERE cs.id IN ('30kl0nzj','g6xl6u6j','0c4l8ofp','khe92j6c','xpeg92h6','07e38ade')
GROUP BY cs.id, cs.title
ORDER BY cs.title;

-- Language homogeneity
SELECT * FROM curriculum_series_language_list
WHERE id IN ('30kl0nzj','g6xl6u6j','0c4l8ofp','khe92j6c','xpeg92h6','07e38ade');

-- Display orders
SELECT c.id, c.content->>'title' as title, c.display_order, csi.curriculum_series_id
FROM curriculum c
JOIN curriculum_series_items csi ON c.id = csi.curriculum_id
WHERE csi.curriculum_series_id IN ('30kl0nzj','g6xl6u6j','0c4l8ofp','khe92j6c','xpeg92h6','07e38ade')
AND c.uid NOT LIKE '%_deleted'
ORDER BY csi.curriculum_series_id, c.display_order;
```

## Recreation Instructions

1. **Infrastructure** (collections + series): Run `orchestrator.py`. Creates 2 collections and 6 series, wires them together, sets display orders. IDs logged to stdout.
2. **Curriculums**: All creation scripts have been deleted after successful execution. To recreate:
   - Query the DB for curriculum content via `curriculum/getOne` using the curriculum ID
   - Or query MCP postgres: `SELECT id, content->>'title', content FROM curriculum WHERE uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73' AND language = 'de' AND user_language = 'de' AND uid NOT LIKE '%_deleted'`
3. **Validation**: Use `validate_content.py` to check content JSON before upload.
4. **API helpers**: Use `api_helpers.py` for all API calls.

## Creation Method

- Orchestrator: `de-de/orchestrator.py` — created 2 collections, 6 series
- Batch creator: `de-de/run_all.py` (imported from create_all_de_de.py, create_e3_f_all.py, create_f_remaining.py, run_all_remaining.py)
- E2-5 retry: manual retry after timeout (orphan duplicate deleted)
- All validated against content corruption rules before upload
- 30/30 curriculums created successfully
