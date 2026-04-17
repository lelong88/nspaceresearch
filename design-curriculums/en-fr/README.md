# en-fr — English-French Curriculum Collection

English-speaking learners studying French. 4 collections, 20 series, 100 curriculums. All complete.

- **userLanguage**: `en`
- **language**: `fr`
- **UID**: `zs5AMpVfqkcfDf8CJ9qrXdH58d73`
- **API base**: `https://helloapi.step.is`

## Status

All creation scripts have been executed and deleted. Remaining files: `orchestrator.py`, `api_helpers.py`, `validate_content.py`, `README.md`.

| Series | Curriculums | Status |
|--------|-------------|--------|
| A1–A5 | 25/25 | ✅ |
| B1–B5 | 25/25 | ✅ |
| C1–C5 | 25/25 | ✅ |
| D1–D5 | 25/25 | ✅ |
| **Total** | **100/100** | ✅ |

## Collection & Series IDs

### Collection A — Daily Life and Travel (Vie Quotidienne et Voyages)

| Key | ID | Title |
|-----|-----|-------|
| Collection A | `ryizoean` | Daily Life and Travel (Vie Quotidienne et Voyages) |
| Series A1 | `ija0u3nb` | Food and Dining — 5 curriculums |
| Series A2 | `sv234nd5` | City Navigation and Transport — 5 curriculums |
| Series A3 | `r3p6iee8` | Shopping and Services — 5 curriculums |
| Series A4 | `07echqco` | Social Life and Relationships — 5 curriculums |
| Series A5 | `9tkc6zjo` | Health and Wellness — 5 curriculums |

### Collection B — Business and Professional (Affaires et Professionnel)

| Key | ID | Title |
|-----|-----|-------|
| Collection B | `snvuj7i4` | Business and Professional (Affaires et Professionnel) |
| Series B1 | `bfzeof6g` | Workplace Communication — 5 curriculums |
| Series B2 | `ozgsetun` | Job Search and Career — 5 curriculums |
| Series B3 | `l6clmnca` | Industry-Specific Vocabulary — 5 curriculums |
| Series B4 | `kgnackph` | Business Operations — 5 curriculums |
| Series B5 | `rra9jo07` | International Business — 5 curriculums |

### Collection C — Academic and Intellectual (Académique et Intellectuel)

| Key | ID | Title |
|-----|-----|-------|
| Collection C | `uw4gc0vw` | Academic and Intellectual (Académique et Intellectuel) |
| Series C1 | `i0vsbjqx` | Science and Technology — 5 curriculums |
| Series C2 | `gjzcwtn4` | Economics and Finance — 5 curriculums |
| Series C3 | `kacowgkb` | History and Politics — 5 curriculums |
| Series C4 | `zhvruw0q` | Psychology and Education — 5 curriculums |
| Series C5 | `q5689ug1` | Philosophy and Critical Thinking — 5 curriculums |

### Collection D — Culture and Society (Culture et Société)

| Key | ID | Title |
|-----|-----|-------|
| Collection D | `vzjkxa3m` | Culture and Society (Culture et Société) |
| Series D1 | `kjcuu34a` | Arts and Literature — 5 curriculums |
| Series D2 | `suu0rkw6` | Architecture and Design — 5 curriculums |
| Series D3 | `anvj5sug` | Environment and Sustainability — 5 curriculums |
| Series D4 | `1qihbrzz` | Sports and Recreation — 5 curriculums |
| Series D5 | `em41cb2u` | Traditions and Festivals — 5 curriculums |

## SQL Verification Queries

```sql
-- Duplicate check
SELECT content->>'title' AS title, COUNT(*) AS cnt
FROM curriculum
WHERE uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'
  AND uid NOT LIKE '%_deleted'
  AND language = 'fr' AND user_language = 'en'
GROUP BY content->>'title'
HAVING COUNT(*) > 1;

-- Series curriculum counts
SELECT cs.id, cs.title, COUNT(csi.curriculum_id) AS cnt
FROM curriculum_series cs
LEFT JOIN curriculum_series_items csi ON csi.curriculum_series_id = cs.id
WHERE cs.id IN (
  'ija0u3nb','sv234nd5','r3p6iee8','07echqco','9tkc6zjo',
  'bfzeof6g','ozgsetun','l6clmnca','kgnackph','rra9jo07',
  'i0vsbjqx','gjzcwtn4','kacowgkb','zhvruw0q','q5689ug1',
  'kjcuu34a','suu0rkw6','anvj5sug','1qihbrzz','em41cb2u'
)
GROUP BY cs.id, cs.title ORDER BY cs.title;

-- Language homogeneity
SELECT * FROM curriculum_series_language_list
WHERE id IN (
  'ija0u3nb','sv234nd5','r3p6iee8','07echqco','9tkc6zjo',
  'bfzeof6g','ozgsetun','l6clmnca','kgnackph','rra9jo07',
  'i0vsbjqx','gjzcwtn4','kacowgkb','zhvruw0q','q5689ug1',
  'kjcuu34a','suu0rkw6','anvj5sug','1qihbrzz','em41cb2u'
);
```

## Recreation Instructions

1. **Infrastructure**: Run `orchestrator.py` to create 4 collections and 20 series.
2. **Curriculums**: Query DB for content via `curriculum/getOne` or MCP postgres.
3. **Validation**: Use `validate_content.py` before upload.
4. **API helpers**: Use `api_helpers.py` for all API calls.

> The orchestrator is NOT idempotent — do not re-run without deleting existing infrastructure first.
