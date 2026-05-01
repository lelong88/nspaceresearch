# Miêu Tả Người Quen (Describing People You Know Series)

## Series Info

- **Series ID**: `jv54tnvp`
- **Series Title**: Miêu Tả Người Quen
- **Series Description Tone**: surprising_fact
- **Description**: Vietnamese, ≤255 chars, surprising_fact tone — about how often you meet people but can't describe them in English

## Language Pair

- **userLanguage**: vi (Vietnamese speakers)
- **language**: en (learning English)
- **Level**: preintermediate (difficultyTags: beginner, vocab_preintermediate, reading_preintermediate)

## Curriculums

| # | Display Order | ID | Title | Desc Tone | Farewell Tone |
|---|---|---|---|---|---|
| 1 | 1 | 1ZcAjlbDYtot0tHn | Miêu Tả Tính Cách | empathetic_observation | introspective_guide |
| 2 | 2 | xW0Bqe1Eyz0bmB3m | Miêu Tả Ngoại Hình | vivid_scenario | warm_accountability |

## Vocabulary Lists (30 unique words)

### Curriculum 1 — Miêu Tả Tính Cách (Describing Personalities)
- **W1**: outgoing, shy, generous, patient, stubborn
- **W2**: honest, cheerful, calm, confident, creative
- **W3**: reliable, thoughtful, ambitious, easygoing, sensitive

### Curriculum 2 — Miêu Tả Ngoại Hình (Describing Appearances)
- **W1**: tall, slim, curly, straight, freckles
- **W2**: muscular, pale, tan, beard, bald
- **W3**: chubby, elegant, wrinkles, dimples, broad

## Creation Method

- Each curriculum created via standalone Python script with hand-written content
- Validation script checked all 11 correctness properties before upload
- Orchestrator script created series and assembled curriculums
- All scripts deleted after successful creation (per project convention)

## Pattern

- **Pattern**: 4-session speaking-focus (introAudio → viewFlashcards → reading → readAlong → speakReading)
- **15 vocab words per curriculum** (5 per session 1–3, all 15 in session 4 review)
- **Reading passages**: first-person mini-speeches describing people the learner knows
- **All marketing text in Vietnamese**

## SQL Queries

```sql
-- Find both curriculums
SELECT id, content->>'title' as title, display_order, is_public, language, user_language
FROM curriculum
WHERE id IN ('1ZcAjlbDYtot0tHn', 'xW0Bqe1Eyz0bmB3m');

-- Find the series and its members
SELECT csi.curriculum_id, c.content->>'title' as title, c.display_order
FROM curriculum_series_items csi
JOIN curriculum c ON c.id = csi.curriculum_id
WHERE csi.curriculum_series_id = 'jv54tnvp'
ORDER BY c.display_order;

-- Get full content for recreation
SELECT id, content FROM curriculum WHERE id = '1ZcAjlbDYtot0tHn';
SELECT id, content FROM curriculum WHERE id = 'xW0Bqe1Eyz0bmB3m';

-- Check for duplicates
SELECT id, content->>'title' as title, created_at
FROM curriculum
WHERE content->>'title' IN ('Miêu Tả Tính Cách', 'Miêu Tả Ngoại Hình')
  AND uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'
  AND uid NOT LIKE '%_deleted'
ORDER BY content->>'title', created_at;
```

## Recreation Context

- **UID**: zs5AMpVfqkcfDf8CJ9qrXdH58d73
- **API**: helloapi.step.is
- **Pattern**: 4-session speaking-focus (introAudio → viewFlashcards → reading → readAlong → speakReading)
- **Each session**: introAudio → viewFlashcards → reading → readAlong → speakReading
- **Content recoverable** via `curriculum/getOne` API with each curriculum ID
- **Created**: 2026-04-30
