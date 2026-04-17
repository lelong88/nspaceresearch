# vi-de — Vietnamese-German Curriculum Collection

Vietnamese learners studying German. 4 collections, 20 series, 100 curriculums (all complete).

- **userLanguage**: `vi`
- **language**: `de`
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
| **Total** | **100/100** | ✅ All complete |

## Collection & Series IDs

### Collection A — Đời Sống và Du Lịch (Alltag und Reisen)

| Key | ID | Title |
|-----|-----|-------|
| Collection A | `8w1ejkj2` | Đời Sống và Du Lịch (Alltag und Reisen) |
| Series A1 | `odrawqgd` | Ẩm Thực và Nhà Hàng (Essen und Gastronomie) — 5 curriculums |
| Series A2 | `ohbrf7jv` | Di Chuyển Thành Phố (Stadtnavigation und Verkehr) — 5 curriculums |
| Series A3 | `9g1u93r8` | Mua Sắm và Dịch Vụ (Einkaufen und Dienstleistungen) — 5 curriculums |
| Series A4 | `n53wtdqm` | Đời Sống Xã Hội (Soziales Leben und Beziehungen) — 5 curriculums |
| Series A5 | `et16j3o5` | Sức Khỏe và Thể Chất (Gesundheit und Wohlbefinden) — 5 curriculums |

### Collection B — Kinh Doanh và Chuyên Nghiệp (Geschäft und Beruf)

| Key | ID | Title |
|-----|-----|-------|
| Collection B | `skd7409r` | Kinh Doanh và Chuyên Nghiệp (Geschäft und Beruf) |
| Series B1 | `7uy42xaq` | Giao Tiếp Công Sở (Kommunikation am Arbeitsplatz) — 5 curriculums |
| Series B2 | `rx0em3i9` | Tìm Việc và Sự Nghiệp (Jobsuche und Karriere) — 5 curriculums |
| Series B3 | `302y4k0k` | Từ Vựng Ngành Nghề (Branchenvokabular) — 5 curriculums |
| Series B4 | `hbm06q7j` | Vận Hành Doanh Nghiệp (Geschäftsbetrieb) — 5 curriculums |
| Series B5 | `80bo01ro` | Kinh Doanh Quốc Tế (Internationaler Handel) — 5 curriculums |

### Collection C — Học Thuật và Tri Thức (Akademisch und Intellektuell)

| Key | ID | Title |
|-----|-----|-------|
| Collection C | `8rrpbalf` | Học Thuật và Tri Thức (Akademisch und Intellektuell) |
| Series C1 | `wdrnqzs8` | Khoa Học và Công Nghệ (Wissenschaft und Technologie) — 5 curriculums |
| Series C2 | `xp72ampr` | Kinh Tế và Tài Chính (Wirtschaft und Finanzen) — 5 curriculums |
| Series C3 | `dlx44j71` | Lịch Sử và Chính Trị (Geschichte und Politik) — 5 curriculums |
| Series C4 | `bb60uyn6` | Tâm Lý và Giáo Dục (Psychologie und Bildung) — 5 curriculums |
| Series C5 | `87prtfmn` | Triết Học và Tư Duy Phản Biện (Philosophie und kritisches Denken) — 5 curriculums |

### Collection D — Văn Hóa và Xã Hội (Kultur und Gesellschaft)

| Key | ID | Title |
|-----|-----|-------|
| Collection D | `o56dyd33` | Văn Hóa và Xã Hội (Kultur und Gesellschaft) |
| Series D1 | `p4wm6tbm` | Nghệ Thuật và Văn Học (Kunst und Literatur) — 5 curriculums |
| Series D2 | `4u0b3u3y` | Kiến Trúc và Thiết Kế (Architektur und Design) — 5 curriculums |
| Series D3 | `pp6xz8uq` | Môi Trường và Bền Vững (Umwelt und Nachhaltigkeit) — 5 curriculums |
| Series D4 | `sw3jeikv` | Thể Thao và Giải Trí (Sport und Freizeit) — 5 curriculums |
| Series D5 | `zjk63btb` | Truyền Thống và Lễ Hội (Traditionen und Feste) — 5 curriculums |

## SQL Verification Queries

### Duplicate check
```sql
SELECT title, COUNT(*) as cnt
FROM curriculums
WHERE uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'
  AND language = 'de' AND "userLanguage" = 'vi'
  AND uid NOT LIKE '%_deleted'
GROUP BY title
HAVING COUNT(*) > 1;
```

### Series curriculum counts
```sql
SELECT cs.id AS series_id, cs.title, COUNT(csc."curriculumId") AS curriculum_count
FROM curriculum_series cs
LEFT JOIN curriculum_series_curriculums csc ON cs.id = csc."curriculumSeriesId"
WHERE cs.id IN (
  'odrawqgd','ohbrf7jv','9g1u93r8','n53wtdqm','et16j3o5',
  '7uy42xaq','rx0em3i9','302y4k0k','hbm06q7j','80bo01ro',
  'wdrnqzs8','xp72ampr','dlx44j71','bb60uyn6','87prtfmn',
  'p4wm6tbm','4u0b3u3y','pp6xz8uq','sw3jeikv','zjk63btb'
)
GROUP BY cs.id, cs.title
ORDER BY cs.title;
```

### Language homogeneity
```sql
SELECT * FROM curriculum_series_language_list
WHERE id IN (
  'odrawqgd','ohbrf7jv','9g1u93r8','n53wtdqm','et16j3o5',
  '7uy42xaq','rx0em3i9','302y4k0k','hbm06q7j','80bo01ro',
  'wdrnqzs8','xp72ampr','dlx44j71','bb60uyn6','87prtfmn',
  'p4wm6tbm','4u0b3u3y','pp6xz8uq','sw3jeikv','zjk63btb'
);
```

### Display orders
```sql
SELECT c.id, c.title, c."displayOrder"
FROM curriculums c
JOIN curriculum_series_curriculums csc ON c.id = csc."curriculumId"
WHERE csc."curriculumSeriesId" IN (
  'odrawqgd','ohbrf7jv','9g1u93r8','n53wtdqm','et16j3o5',
  '7uy42xaq','rx0em3i9','302y4k0k','hbm06q7j','80bo01ro',
  'wdrnqzs8','xp72ampr','dlx44j71','bb60uyn6','87prtfmn',
  'p4wm6tbm','4u0b3u3y','pp6xz8uq','sw3jeikv','zjk63btb'
)
AND c.uid NOT LIKE '%_deleted'
ORDER BY csc."curriculumSeriesId", c."displayOrder";
```

## Recreation Instructions

1. **Infrastructure** (collections + series): Run `orchestrator.py`. This creates 4 collections and 20 series, wires them together, and sets display orders. IDs are logged to stdout.
2. **Curriculums**: All `create_*.py` scripts have been deleted after successful execution. To recreate a curriculum:
   - Query the DB for the curriculum content via `curriculum/getOne` using the curriculum ID
   - Or query MCP postgres: `SELECT id, title, content FROM curriculums WHERE uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73' AND language = 'de' AND "userLanguage" = 'vi' AND uid NOT LIKE '%_deleted'`
   - Write a new creation script following the patterns in `CURRICULUM_CREATION_RULES.md`
3. **Validation**: Use `validate_content.py` to check content JSON before upload.
4. **API helpers**: Use `api_helpers.py` for all API calls (create, add to series, set display order).

> **Note**: The orchestrator is NOT idempotent — do not re-run it without deleting existing collections/series first. Curriculum scripts are idempotent in intent but create duplicates if re-run.
