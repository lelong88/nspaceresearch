# Hugo — Learner Curriculums

English-English curriculums created for Hugo, covering 20 diverse topics at intermediate level.

## Source Material
- `PROMPT.md` — Original prompt used to generate the 20 curriculums
- `curriculums/*.py` — High-quality rewritten content (preview, introAudio, writing prompts). Each file exports a `CONTENT` dict with `curriculum_id` linking it to the DB record.
- `curriculums/README.md` — Quality bar documentation

## Reusable Tools
- `update_curriculums.py` — Patches existing curriculums with content from `curriculums/*.py` (reads `curriculum_id` from each module at runtime)

## Curriculums in Database
Language pair: en-en. UID: `zs5AMpVfqkcfDf8CJ9qrXdH58d73`.

To get the current list:
```sql
SELECT id, content->>'title' as title
FROM curriculum
WHERE uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'
  AND language = 'en' AND user_language = 'en'
ORDER BY content->>'title';
```

The `curriculum_id` field in each `curriculums/*.py` file is the authoritative link between source content and DB record.
