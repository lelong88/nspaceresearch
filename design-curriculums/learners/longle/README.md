# Long Le — Hán Ngữ Phổ Thông - Sơ cấp 2

## Series
- Series ID: `dqce6wbh`
- Series name: Hán Ngữ Phổ Thông - Sơ cấp 2
- Language: `zh` (Chinese), User language: `vi` (Vietnamese)
- 25 curriculums (Bài 1–25), display order 1–25

## How content was created
- Source material: PPTX slides from the Hán Ngữ Phổ Thông textbook (Bài 1–25), containing vocab lists and reading passages
- Vocab and reading text extracted from PPTX files using `python-pptx`, saved to `lesson_data.json`
- Each curriculum created via a per-lesson Python script (`bai01_create.py` through `bai25_create.py`) using a shared `curriculum_builder.py` module
- 3 curriculums (Bài 14, 17, 18) were pre-existing; the other 22 were created in this batch
- Bilingual content (Vietnamese + Chinese) for all introAudio, previews, titles, descriptions
- 5 sessions per curriculum: 3 vocab-learning sessions, 1 review session, 1 full-reading session
- Each vocab session: introAudio (lesson intro) → introAudio (vocab teaching) → viewFlashcards → speakFlashcards → vocabLevel1 → vocabLevel2 → introAudio (grammar) → reading → speakReading → readAlong

## SQL queries to find curriculums
```sql
-- All curriculums in the series
SELECT c.id, c.display_order, c.content::json->>'title' as title
FROM curriculum c
JOIN curriculum_series_items csi ON c.id = csi.curriculum_id
WHERE csi.curriculum_series_id = 'dqce6wbh'
ORDER BY c.display_order;

-- Get full content for any curriculum
SELECT content FROM curriculum WHERE id = '<curriculum_id>';
```

## Recreation notes
- Full content is recoverable from the DB via `curriculum/getOne` or the SQL above
- Original PPTX source files are no longer needed — all vocab and reading text is embedded in the curriculum content in the DB
- To recreate: extract vocab/reading from DB content, use the same `curriculum_builder.py` pattern (build_session_1_2_3, build_session_4, build_session_5), write new introAudio/grammar content
