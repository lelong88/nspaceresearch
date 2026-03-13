# Hugo — Learner Curriculums

English-English curriculums for Hugo, covering diverse topics at intermediate level.
Series ID: `db5930f6`.

## How They Were Created
- Template curriculum: "Rewriting Extinction" (`gA1W24Ga6lXwdHHx`) — used `curriculum/getOne` with `strip_keys()` to get the structure
- Generated 20 curriculums matching the template's structure and difficulty across diverse topics
- Quality-rewritten preview, introAudio, writingSentence, and writingParagraph texts to match the project quality bar (see Quality Standards in product.md steering)
- Additional curriculums added to the series over time

## To Recreate
1. Fetch the template: `curriculum/getOne` for `gA1W24Ga6lXwdHHx`, run through `strip_keys()`
2. Generate new curriculums following the same 4-session structure, activity types, and quality bar
3. Upload via `curriculum/create`, add to series `db5930f6`

## Curriculums in Database

```sql
SELECT c.id, c.content->>'title' as title, c.display_order
FROM curriculum c
JOIN curriculum_series_items csi ON c.id = csi.curriculum_id
WHERE csi.curriculum_series_id = 'db5930f6'
ORDER BY c.display_order;
```
