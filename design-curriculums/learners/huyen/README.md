# Huyen — Learner Curriculums

Personalized Vietnamese-English curriculum for Huyen.

## Learner Profile
Small business owner, selling healthy meals service.

## How It Was Created
- Curriculum JSON was hand-crafted based on the learner profile
- Each curriculum: 4 sessions, 6 vocab words (2 per session), session 4 is review
- Activity pattern: introAudio × 4 → viewFlashcards → vocabLevel1 → vocabLevel2 → reading → speakReading → readAlong
- All reading passages use the healthy food business context
- Uploaded via `curriculum/create`, added to series via `curriculum-series/addCurriculum`

## To Recreate
1. Use the learner profile above and the business topics below
2. Generate vi-en curriculums tailored to a small business owner context
3. Upload via `curriculum/create`, add to series `85d6512e`, collection `95ea42ed`

## Curriculums in Database
Series: "Chủ Doanh Nghiệp (Business Owner)" (`85d6512e`)
Collection: "Huấn Luyện Viên (Coaching)" (`95ea42ed`)

| displayOrder | ID | Title | Topic |
|---|---|---|---|
| 0 | `EX4E093ppEMsAlW8` | Opportunity Cost: Mỗi lựa chọn đều có giá | cost, choice, to give up, worth, to invest, to focus on |
| 1 | `yBynNSeRi2J5yWAr` | Customer & Demand: Hiểu khách hàng, nắm thị trường | customer, demand, to attract, loyal, to satisfy, feedback |
| 2 | `xiizGXiLB3SYlKo6` | Profit & Expense: Tiền vào, tiền ra | revenue, expense, profit, to budget, to save, to afford |
| 3 | `H5ORSpyXC6aSMdxi` | Brand & Compete: Xây thương hiệu, vượt đối thủ | brand, to compete, quality, unique, reputation, to improve |

```sql
SELECT c.id, c.content->>'title' as title, c.display_order
FROM curriculum c
JOIN curriculum_series_items csi ON csi.curriculum_id = c.id
WHERE csi.curriculum_series_id = '85d6512e'
ORDER BY c.display_order;
```
