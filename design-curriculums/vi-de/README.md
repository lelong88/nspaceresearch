# vi-de — Vietnamese-German Curriculum Collection (bilingual-parity-expansion)

Created: 2025-07-25
Language pair: userLanguage=vi (Vietnamese speakers), language=de (learning German)
User-facing text: Vietnamese. Reading passages: German.
Levels: beginner, preintermediate, intermediate (bilingual).
155 curriculums total: 60 beginner, 56 preintermediate, 39 intermediate.
5 collections, 27 series.

## Collection IDs

| Collection | ID | Title | displayOrder |
|---|---|---|---|
| A | wo5ruhf4 | Đời Sống Hàng Ngày (Alltag und Reisen) | 1 |
| B | rzqj2tfd | Kinh Doanh và Nghề Nghiệp (Geschäft und Beruf) | 2 |
| C | e9dqsr5l | Học Thuật và Khoa Học (Akademisch und Wissenschaft) | 3 |
| D | 9dxkbcgg | Văn Hóa và Xã Hội (Kultur und Gesellschaft) | 4 |
| E | 6uew8zaj | Thiên Nhiên và Đổi Mới (Natur und Innovation) | 5 |

## Series IDs

| Series | ID | Title | Curriculums |
|---|---|---|---|
| A1 | nk9din6m | Ẩm Thực và Nhà Hàng (Essen und Gastronomie) | 6 |
| A2 | 3mhngi2t | Di Chuyển và Giao Thông (Stadtnavigation und Verkehr) | 6 |
| A3 | 97adx881 | Mua Sắm và Dịch Vụ (Einkaufen und Dienstleistungen) | 6 |
| A4 | lchdu4h9 | Đời Sống Xã Hội (Soziales Leben und Beziehungen) | 6 |
| A5 | ctltteoi | Sức Khỏe và Thể Chất (Gesundheit und Wohlbefinden) | 6 |
| A6 | b65nfsu6 | Nhà Ở và Sinh Hoạt (Zuhause und Wohnen) | 6 |
| A7 | 2rwtt7qv | Du Lịch và Khám Phá (Reisen und Tourismus) | 6 |
| B1 | b728w7en | Giao Tiếp Công Sở (Kommunikation am Arbeitsplatz) | 6 |
| B2 | kvo9n6fi | Tìm Việc và Sự Nghiệp (Jobsuche und Karriere) | 6 |
| B3 | ov90ej6e | Từ Vựng Chuyên Ngành (Branchenspezifischer Wortschatz) | 6 |
| B4 | 1vj4cxev | Vận Hành Doanh Nghiệp (Geschäftsbetrieb) | 6 |
| B5 | jpcerwpf | Kinh Doanh Quốc Tế (Internationaler Handel) | 5 |
| B6 | lchul6ks | Khởi Nghiệp và Đổi Mới (Unternehmertum und Innovation) | 5 |
| C1 | 7ynvp10s | Khoa Học và Công Nghệ (Wissenschaft und Technologie) | 6 |
| C2 | d40hkx87 | Kinh Tế và Tài Chính (Wirtschaft und Finanzen) | 6 |
| C3 | zy1nysrw | Lịch Sử và Chính Trị (Geschichte und Politik) | 6 |
| C4 | e86rvx3z | Tâm Lý và Giáo Dục (Psychologie und Bildung) | 6 |
| C5 | 0fcoig25 | Triết Học và Tư Duy (Philosophie und kritisches Denken) | 5 |
| C6 | 1lpvrvgp | Nghiên Cứu và Viết Học Thuật (Forschung und wissenschaftliches Schreiben) | 5 |
| D1 | cyukhwqr | Nghệ Thuật và Văn Học (Kunst und Literatur) | 6 |
| D2 | klqwba15 | Kiến Trúc và Thiết Kế (Architektur und Design) | 6 |
| D3 | 2ab33g02 | Truyền Thông và Báo Chí (Medien und Journalismus) | 5 |
| D4 | dwqdoqpl | Truyền Thống và Lễ Hội (Traditionen und Feste) | 5 |
| E1 | ifuxuxts | Môi Trường và Bền Vững (Umwelt und Nachhaltigkeit) | 6 |
| E2 | a0xkx2y5 | Công Nghệ Số và Trí Tuệ Nhân Tạo (Digitalisierung und KI) | 6 |
| E3 | 3xg9bmqd | Thể Thao và Giải Trí (Sport und Freizeit) | 6 |
| E4 | 3ywqyzum | Thiên Nhiên và Động Vật (Natur und Tierwelt) | 5 |

## SQL Verification Queries

```sql
-- All vi-de curriculums (should return 155 rows)
SELECT c.id, c.content->>'title' AS title, c.level, c.display_order, c.price
FROM curriculum c
WHERE c.uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'
  AND c.uid NOT LIKE '%_deleted'
  AND c.language = 'de' AND c.user_language = 'vi'
ORDER BY c.created_at;

-- Duplicate check (should return 0 rows)
SELECT c.content->>'title' AS title, COUNT(*) AS cnt
FROM curriculum c
WHERE c.uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'
  AND c.uid NOT LIKE '%_deleted'
  AND c.language = 'de' AND c.user_language = 'vi'
GROUP BY c.content->>'title'
HAVING COUNT(*) > 1;

-- Series curriculum counts (verify each series has expected count)
SELECT cs.id AS series_id, cs.title, COUNT(csi.curriculum_id) AS curriculum_count
FROM curriculum_series cs
LEFT JOIN curriculum_series_items csi ON cs.id = csi.curriculum_series_id
WHERE cs.id IN (
  'nk9din6m','3mhngi2t','97adx881','lchdu4h9','ctltteoi','b65nfsu6','2rwtt7qv',
  'b728w7en','kvo9n6fi','ov90ej6e','1vj4cxev','jpcerwpf','lchul6ks',
  '7ynvp10s','d40hkx87','zy1nysrw','e86rvx3z','0fcoig25','1lpvrvgp',
  'cyukhwqr','klqwba15','2ab33g02','dwqdoqpl',
  'ifuxuxts','a0xkx2y5','3xg9bmqd','3ywqyzum'
)
GROUP BY cs.id, cs.title
ORDER BY cs.title;

-- Language homogeneity (all series should show language=de, user_language=vi)
SELECT * FROM curriculum_series_language_list
WHERE id IN (
  'nk9din6m','3mhngi2t','97adx881','lchdu4h9','ctltteoi','b65nfsu6','2rwtt7qv',
  'b728w7en','kvo9n6fi','ov90ej6e','1vj4cxev','jpcerwpf','lchul6ks',
  '7ynvp10s','d40hkx87','zy1nysrw','e86rvx3z','0fcoig25','1lpvrvgp',
  'cyukhwqr','klqwba15','2ab33g02','dwqdoqpl',
  'ifuxuxts','a0xkx2y5','3xg9bmqd','3ywqyzum'
);

-- Level gap check (all should show max_level_gap ≤ 1)
SELECT * FROM curriculum_series_level_gap
WHERE id IN (
  'nk9din6m','3mhngi2t','97adx881','lchdu4h9','ctltteoi','b65nfsu6','2rwtt7qv',
  'b728w7en','kvo9n6fi','ov90ej6e','1vj4cxev','jpcerwpf','lchul6ks',
  '7ynvp10s','d40hkx87','zy1nysrw','e86rvx3z','0fcoig25','1lpvrvgp',
  'cyukhwqr','klqwba15','2ab33g02','dwqdoqpl',
  'ifuxuxts','a0xkx2y5','3xg9bmqd','3ywqyzum'
);

-- Display order check (verify no gaps or duplicates within each series)
SELECT csi.curriculum_series_id, c.id, c.content->>'title' AS title, c.display_order
FROM curriculum c
JOIN curriculum_series_items csi ON c.id = csi.curriculum_id
WHERE csi.curriculum_series_id IN (
  'nk9din6m','3mhngi2t','97adx881','lchdu4h9','ctltteoi','b65nfsu6','2rwtt7qv',
  'b728w7en','kvo9n6fi','ov90ej6e','1vj4cxev','jpcerwpf','lchul6ks',
  '7ynvp10s','d40hkx87','zy1nysrw','e86rvx3z','0fcoig25','1lpvrvgp',
  'cyukhwqr','klqwba15','2ab33g02','dwqdoqpl',
  'ifuxuxts','a0xkx2y5','3xg9bmqd','3ywqyzum'
)
AND c.uid NOT LIKE '%_deleted'
ORDER BY csi.curriculum_series_id, c.display_order;

-- Pricing check (beginner=19, preintermediate/intermediate=49)
SELECT c.level, c.price, COUNT(*) AS cnt
FROM curriculum c
WHERE c.uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'
  AND c.uid NOT LIKE '%_deleted'
  AND c.language = 'de' AND c.user_language = 'vi'
GROUP BY c.level, c.price
ORDER BY c.level, c.price;
```

## Recreation Instructions

1. **Infrastructure** (collections + series): Run `orchestrator.py`. Creates 5 collections and 27 series, wires them together, sets display orders. IDs logged to stdout.
2. **Curriculums**: All creation scripts have been deleted after successful execution. To recreate:
   - Query the DB for curriculum content via `curriculum/getOne` using the curriculum IDs
   - Or query MCP postgres: `SELECT id, content->>'title' AS title, content FROM curriculum WHERE uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73' AND language = 'de' AND user_language = 'vi' AND uid NOT LIKE '%_deleted'`
3. **Validation**: Use `validate_content.py` to check content JSON before upload.
4. **API helpers**: Use `api_helpers.py` for all API calls.

> **Note**: The orchestrator is NOT idempotent — do not re-run it without deleting existing collections/series first. Curriculum scripts are idempotent in intent but create duplicates if re-run.

## Creation Method

- Orchestrator: `vi-de/orchestrator.py` — created 5 collections, 27 series, wired and ordered
- Curriculum scripts: 155 individual `create_*.py` scripts (60 beginner, 56 preintermediate, 39 intermediate)
- All validated against content corruption rules and curriculum quality standards before upload
- 155/155 curriculums created successfully
- All creation scripts and temporary files deleted after successful execution

## Note on Old multilingual-curriculum-expansion Infrastructure

The old `multilingual-curriculum-expansion` spec created separate vi-de infrastructure with 4 collections, 20 series, and 100 curriculums. Those old collections/series still exist in the database:

| Old Collection | ID | Title |
|---|---|---|
| A | 8w1ejkj2 | Đời Sống và Du Lịch (Alltag und Reisen) |
| B | skd7409r | Kinh Doanh và Chuyên Nghiệp (Geschäft und Beruf) |
| C | 8rrpbalf | Học Thuật và Tri Thức (Akademisch und Intellektuell) |
| D | o56dyd33 | Văn Hóa và Xã Hội (Kultur und Gesellschaft) |

Old series IDs: `odrawqgd`, `ohbrf7jv`, `9g1u93r8`, `n53wtdqm`, `et16j3o5`, `7uy42xaq`, `rx0em3i9`, `302y4k0k`, `hbm06q7j`, `80bo01ro`, `wdrnqzs8`, `xp72ampr`, `dlx44j71`, `bb60uyn6`, `87prtfmn`, `p4wm6tbm`, `4u0b3u3y`, `pp6xz8uq`, `sw3jeikv`, `zjk63btb`.

These are **not deleted** but are superseded by the bilingual-parity-expansion infrastructure listed above (5 collections, 27 series, 155 curriculums). The new infrastructure is entirely separate — different collection IDs, different series IDs, different curriculums.

## Remaining Files

- `vi-de/orchestrator.py` — infrastructure creation script (collections, series, wiring)
- `vi-de/validate_content.py` — content validation utility
- `vi-de/api_helpers.py` — shared API helper functions
- `vi-de/README.md` — this file
