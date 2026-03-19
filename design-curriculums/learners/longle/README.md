# Long Le — vi-zh Curriculums

## Collection
- Collection ID: `64fb68f8` — Sơ Cấp 2 (初级二)
- Language: `zh` (Chinese), User language: `vi` (Vietnamese)

---

## Series 1: Hán Ngữ Phổ Thông - Sơ cấp 2
- Series ID: `dqce6wbh`
- Display order: 0
- 25 curriculums (Bài 1–25), display order 1–25

### How content was created
- Source material: PPTX slides from the Hán Ngữ Phổ Thông textbook (Bài 1–25)
- Vocab and reading text extracted from PPTX files using `python-pptx`, saved to `lesson_data.json`
- Each curriculum created via per-lesson Python scripts using a shared `curriculum_builder.py` module
- 5 sessions per curriculum: 3 vocab-learning sessions, 1 review session, 1 full-reading session

### SQL queries
```sql
SELECT c.id, c.display_order, c.content::json->>'title' as title
FROM curriculum c
JOIN curriculum_series_items csi ON c.id = csi.curriculum_id
WHERE csi.curriculum_series_id = 'dqce6wbh'
ORDER BY c.display_order;
```

### Recreation notes
- Full content recoverable from DB via `curriculum/getOne`
- Original PPTX source files no longer needed — all content is in the DB

---

## Series 2: Triết Lý Trong Chữ Hán (汉字中的智慧)
- Series ID: `vxvh04b5`
- Display order: 1
- Level: preintermediate
- 4 curriculums, 18 words each, 5 sessions each

| # | Title | Curriculum ID | Display Order |
|---|---|---|---|
| 1 | Tâm Tự — Chữ của Trái Tim (心字篇) | QOvwYvTVMi6OkkWp | 0 |
| 2 | Nhân Tự — Chữ của Con Người (人字篇) | cPjQO2MkPgWdMvlv | 1 |
| 3 | Gia Tự — Chữ của Gia Đình và Ngôi Nhà (家字篇) | tepW8yNMEOWiKnkC | 2 |
| 4 | Lực Tự — Chữ của Hành Động và Sức Mạnh (力字篇) | DSsoTpLVsaE4ktmJ | 3 |

### How content was created
- Theme: Life philosophy embedded in Chinese character structure (radicals, etymology)
- Each curriculum explores characters sharing a common radical (心, 人, 宀/女, 力)
- Created via per-curriculum Python scripts in `chinese-wisdom-series/`
- Pattern follows `economics-finance-series/` structure: 5 sessions, introAudio + flashcards + vocab + reading + writing
- Series orchestrated via `create_wisdom_series.py`

### SQL queries
```sql
SELECT c.id, c.display_order, c.content::json->>'title' as title
FROM curriculum c
JOIN curriculum_series_items csi ON c.id = csi.curriculum_id
WHERE csi.curriculum_series_id = 'vxvh04b5'
ORDER BY c.display_order;
```

### Recreation notes
- Full content recoverable from DB via `curriculum/getOne` or SQL above
- Source scripts: `create_wisdom_1_heart.py`, `create_wisdom_2_human.py`, `create_wisdom_3_home.py`, `create_wisdom_4_action.py`, `create_wisdom_series.py`
