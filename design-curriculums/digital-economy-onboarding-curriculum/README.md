# Digital Economy Onboarding Curriculum — Kinh Tế Số

## Curriculum
- **ID**: `SUdvlKlkNSwa4Hew`
- **Title**: Kinh Tế Số
- **Language pair**: userLanguage="vi", language="en" (Vietnamese speakers learning English)
- **Level**: preintermediate
- **Type**: onboarding/demo, balanced_skills, 1 session, 9 activities
- **Pricing**: free (0 credits)
- **Status**: private (not published)

## Vocabulary
5 words: `platform`, `transaction`, `startup`, `innovation`, `digital`

## Activity Sequence (1 session)
1. introAudio — welcome + teach all 5 vocabulary words
2. viewFlashcards — all 5 words
3. speakFlashcards — all 5 words
4. vocabLevel1 — all 5 words
5. reading — expository passage about digital economy in Vietnam (60-70 words)
6. speakReading — same text
7. readAlong — same text
8. writingSentence — 3 items using vocabulary words
9. introAudio — farewell with vocab review (practical_momentum register)

## How Content Was Created
- Single standalone Python script (`create_digital_economy_onboarding.py`) with all hand-crafted content
- Inline `validate()` function checks 20 structural properties before upload
- Uploaded via `curriculum/create` API (language="en", userLanguage="vi")
- No setPrice call (free by default), no setPublic call (stays private)
- No series or collection — standalone onboarding curriculum
- Script deleted after successful creation and verification

## SQL Queries

```sql
-- Find the curriculum by ID
SELECT id, title, language, "userLanguage", "isPublic", created_at
FROM curriculum
WHERE id = 'SUdvlKlkNSwa4Hew';

-- Verify content structure
SELECT id,
       content::jsonb->>'title' as title,
       content::jsonb->'contentTypeTags' as tags,
       jsonb_array_length(content::jsonb->'learningSessions') as sessions
FROM curriculum
WHERE id = 'SUdvlKlkNSwa4Hew';

-- Verify activity count and sequence
SELECT jsonb_array_length(
    content::jsonb->'learningSessions'->0->'activities'
) as activity_count
FROM curriculum
WHERE id = 'SUdvlKlkNSwa4Hew';

-- Find by title and UID (duplicate check)
SELECT id, title, created_at
FROM curriculum
WHERE title = 'Kinh Tế Số'
  AND uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'
ORDER BY created_at;
```

## Recreation
To recreate this curriculum:
1. Write a Python script following the design in `.kiro/specs/digital-economy-onboarding-curriculum/design.md`
2. Build content with: title "Kinh Tế Số", 5 vocab words (platform, transaction, startup, innovation, digital), 1 session with 9 activities in the sequence above
3. All marketing text (title, description, preview) in Vietnamese; reading passage in English; introAudio scripts bilingual
4. Description uses `surprising_fact` tone; farewell uses `practical_momentum` register
5. Validate with inline validator (20 checks), then upload via `create_curriculum(content, "en", "vi")` using root-level `api_helpers.py`
6. Verify in database, then delete the script
