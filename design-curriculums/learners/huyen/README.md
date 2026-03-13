# Huyen — Learner Curriculums

Personalized Vietnamese-English curriculum for Huyen.

## Learner Profile
Small business owner, selling healthy meals service.

## How It Was Created
- Curriculum JSON was hand-crafted based on the learner profile, topic: opportunity cost
- Uploaded via `curriculum/create`

## To Recreate
1. Use the learner profile above and the topic "opportunity cost"
2. Generate a vi-en curriculum tailored to a small business owner context
3. Upload via `curriculum/create`, add to series "Preintermediate - Business Owner" in collection "Coaching"

## Curriculums in Database
Curriculum ID: `EX4E093ppEMsAlW8` — "Opportunity Cost: Mỗi lựa chọn đều có giá"
Collection: Coaching → Series: Preintermediate - Business Owner

```sql
SELECT id, content->>'title' as title
FROM curriculum
WHERE id = 'EX4E093ppEMsAlW8';
```
