# Tâm Lý Khách Hàng (Customer Psychology Series)

## Series Info

- **Series ID**: `zf2y1xqc`
- **Series Title**: Tâm Lý Khách Hàng
- **Series Description**: "Tâm lý khách hàng là chiếc chìa khóa vàng — hiểu được nó, bạn mở được mọi cánh cửa bán hàng. 5 khóa học giúp bạn nói tiếng Anh về neo giá, bằng chứng xã hội, sự khan hiếm, cảm xúc và niềm tin."
- **Series Description Tone**: metaphor_led

## Language Pair

- **userLanguage**: vi (Vietnamese speakers)
- **language**: en (learning English)
- **Level**: preintermediate/intermediate

## Curriculums

| # | Display Order | ID | Title | Desc Tone | Farewell Tone |
|---|---|---|---|---|---|
| 1 | 1 | FIWSqPaOkqSkNQHu | Ấn Tượng Đầu & Hiệu Ứng Neo | provocative_question | introspective_guide |
| 2 | 2 | NTpGvJWaAmzrdBA6 | Bằng Chứng Xã Hội & Tâm Lý Bầy Đàn | bold_declaration | warm_accountability |
| 3 | 3 | bsS9Gsl5AY3KHcgQ | Sợ Mất & Tâm Lý Khẩn Cấp | vivid_scenario | team_building_energy |
| 4 | 4 | 39Dokk6YVThHvF2M | Cảm Xúc & Nghệ Thuật Kể Chuyện | empathetic_observation | quiet_awe |
| 5 | 5 | zYfRDWSaUVxT8LIl | Xây Dựng Niềm Tin & Có Qua Có Lại | surprising_fact | practical_momentum |

## Vocabulary Lists (75 unique words)

### Curriculum 1 — Ấn Tượng Đầu & Hiệu Ứng Neo
- **W1**: anchor, perception, reference, premium, contrast
- **W2**: bias, initial, frame, benchmark, expectation
- **W3**: impression, positioning, threshold, baseline, cognitive

### Curriculum 2 — Bằng Chứng Xã Hội & Tâm Lý Bầy Đàn
- **W1**: testimonial, endorsement, consensus, conform, influence
- **W2**: popularity, bandwagon, credibility, peer, validation
- **W3**: trend, follower, mainstream, viral, recommendation

### Curriculum 3 — Sợ Mất & Tâm Lý Khẩn Cấp
- **W1**: scarcity, deadline, urgency, exclusive, limited
- **W2**: hesitation, regret, countdown, shortage, expire
- **W3**: forfeit, opportunity, irreversible, procrastinate, incentive

### Curriculum 4 — Cảm Xúc & Nghệ Thuật Kể Chuyện
- **W1**: narrative, empathy, compelling, resonate, aspiration
- **W2**: nostalgia, curiosity, vulnerable, authentic, relatable
- **W3**: inspire, evoke, tension, climax, transformation

### Curriculum 5 — Xây Dựng Niềm Tin & Có Qua Có Lại
- **W1**: transparency, reciprocity, loyalty, guarantee, integrity
- **W2**: rapport, generosity, commitment, consistency, reputation
- **W3**: goodwill, reliable, trustworthy, accountability, dependable

## Creation Method

- One Python script per curriculum with all text content hand-written
- Validation script checked all 11 correctness properties before upload
- Orchestrator script created series and assembled curriculums
- All scripts deleted after successful creation

## Pattern

- **Pattern**: 4-session speaking-focus (same as salmon-cooking curriculum `yMq70CXQiBV27WEu`)
- **Each session**: introAudio → viewFlashcards → reading → readAlong → speakReading

## SQL Queries

```sql
-- Find all curriculums in the series
SELECT csi.curriculum_id, c.content->>'title' as title, c.display_order, c.is_public
FROM curriculum_series_items csi
JOIN curriculum c ON c.id = csi.curriculum_id
WHERE csi.curriculum_series_id = 'zf2y1xqc'
ORDER BY c.display_order;

-- Find series
SELECT * FROM curriculum_series WHERE id = 'zf2y1xqc';

-- Find individual curriculums
SELECT id, content->>'title' as title, language, user_language, display_order, is_public
FROM curriculum
WHERE id IN ('FIWSqPaOkqSkNQHu', 'NTpGvJWaAmzrdBA6', 'bsS9Gsl5AY3KHcgQ', '39Dokk6YVThHvF2M', 'zYfRDWSaUVxT8LIl');

-- Check for duplicates
SELECT content->>'title' as title, count(*)
FROM curriculum
WHERE uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'
  AND content->>'title' IN (
    'Ấn Tượng Đầu & Hiệu Ứng Neo',
    'Bằng Chứng Xã Hội & Tâm Lý Bầy Đàn',
    'Sợ Mất & Tâm Lý Khẩn Cấp',
    'Cảm Xúc & Nghệ Thuật Kể Chuyện',
    'Xây Dựng Niềm Tin & Có Qua Có Lại'
  )
  AND uid NOT LIKE '%_deleted'
GROUP BY content->>'title'
HAVING count(*) > 1;
```

## Recreation Context

- **UID**: zs5AMpVfqkcfDf8CJ9qrXdH58d73
- **API**: helloapi.step.is
- **Pattern**: 4-session speaking-focus (same as salmon-cooking curriculum `yMq70CXQiBV27WEu`)
- **Each session**: introAudio → viewFlashcards → reading → readAlong → speakReading
- **Content recoverable** via `curriculum/getOne` API with each curriculum ID
