# Uncomfortable Growth Curriculum

Mini `balanced_skills` curriculums built around the theme: **"Get comfortable being uncomfortable is the essence of language learning."**

## Overview

This folder contains 4 mini gateway curriculums designed to introduce learners to the mindset of embracing discomfort as the engine of language learning:

1. **en-en** — English speaker learning advanced English vocabulary (5 words, 2 sessions)
2. **en-zh** — English speaker learning Chinese (6 words, 2 sessions)
3. **vi-zh** — Vietnamese speaker learning Chinese (6 words, 2 sessions)
4. **vi-en** — Vietnamese speaker learning English (6 words, 2 sessions)

## Status

✅ **Complete** — All 4 curriculums created, verified, and organized into series.

## Creation Details

### Curriculums Created

| Language Pair | Curriculum ID | Title | Language | User Language |
|---------------|---------------|-------|----------|---------------|
| en-en | `VdgEbnzAassbpRPa` | Get Comfortable Being Uncomfortable | en | en |
| en-zh | `5WldmqQBSq2297qE` | Get Comfortable Being Uncomfortable | zh | en |
| vi-zh | `VXgegS0buEmL1qAr` | Thoải Mái Với Sự Khó Chịu | zh | vi |
| vi-en | `2hcxuPuBD1g1F3Zk` | Bước Ra Khỏi Vùng An Toàn | en | vi |

### Series Created

| Series Name | Series ID | Curriculums |
|-------------|-----------|-------------|
| Uncomfortable Growth | `zpe1tut0` | en-en (`VdgEbnzAassbpRPa`), en-zh (`5WldmqQBSq2297qE`) |
| Tăng Trưởng Qua Khó Khăn | `jdi8d27v` | vi-zh (`VXgegS0buEmL1qAr`), vi-en (`2hcxuPuBD1g1F3Zk`) |

### Curriculum Type: Mini Balanced Skills

- **Single-language (en-en):** 5 vocab words, 2 sessions (8, 6 activities)
- **Bilingual (en-zh, vi-zh, vi-en):** 6 vocab words, 2 sessions (9, 5 activities)

### Theme

Each curriculum explores the psychology of discomfort as a growth mechanism — how embracing awkwardness, making mistakes, tolerating ambiguity, and pushing past the "comfort zone" are not obstacles to language learning but the actual engine of it.

## SQL Queries

### Find All 4 Curriculums

```sql
-- Find all uncomfortable growth curriculums by ID
SELECT id, title, language, user_language, is_public, created_at
FROM curriculum
WHERE id IN (
    'VdgEbnzAassbpRPa',  -- en-en
    '5WldmqQBSq2297qE',  -- en-zh
    'VXgegS0buEmL1qAr',  -- vi-zh
    '2hcxuPuBD1g1F3Zk'   -- vi-en
)
ORDER BY created_at;
```

```sql
-- Alternative: Find by owner and title pattern
SELECT id, title, language, user_language, is_public, created_at
FROM curriculum
WHERE uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'
  AND (
    title ILIKE '%uncomfortable%' 
    OR title ILIKE '%Thoải Mái%'
    OR title ILIKE '%Vùng An Toàn%'
  )
ORDER BY created_at;
```

### Find the Series

```sql
-- Find uncomfortable growth series
SELECT id, title, description, is_public, created_at
FROM curriculum_series
WHERE id IN ('zpe1tut0', 'jdi8d27v')
ORDER BY created_at;
```

### Find Series Membership

```sql
-- Find which curriculums belong to which series
SELECT 
    cs.id AS series_id,
    cs.title AS series_title,
    csc.curriculum_id,
    c.title AS curriculum_title,
    c.language,
    c.user_language
FROM curriculum_series cs
JOIN curriculum_series_curriculums csc ON cs.id = csc.curriculum_series_id
JOIN curriculum c ON csc.curriculum_id = c.id
WHERE cs.id IN ('zpe1tut0', 'jdi8d27v')
ORDER BY cs.id, c.created_at;
```

### Verify Language Homogeneity

```sql
-- Check that each series has homogeneous language settings
SELECT 
    cs.id,
    cs.title,
    array_agg(DISTINCT c.language) AS languages,
    array_agg(DISTINCT c.user_language) AS user_languages
FROM curriculum_series cs
JOIN curriculum_series_curriculums csc ON cs.id = csc.curriculum_series_id
JOIN curriculum c ON csc.curriculum_id = c.id
WHERE cs.id IN ('zpe1tut0', 'jdi8d27v')
GROUP BY cs.id, cs.title;
```

## Recreation Context

Each curriculum was created via a standalone Python script with all text content hand-written. After successful creation and verification, scripts were deleted. To recreate:

1. Refer to the spec at `.kiro/specs/uncomfortable-growth-curriculum/`
2. Follow the design document for activity structure and content guidelines
3. Create new scripts following the patterns documented in the spec

### Key Implementation Details

- **API Endpoint:** `curriculum/create` with `language` and `userLanguage` as top-level body params
- **Auth:** Firebase ID token via `firebase_token.get_firebase_id_token(UID)`
- **UID:** `zs5AMpVfqkcfDf8CJ9qrXdH58d73`
- **Strip Keys:** All auto-generated keys removed before creation (`mp3Url`, `illustrationSet`, `segments`, etc.)
- **Privacy:** All curriculums created as private (`is_public: false`)

### Vocabulary Themes by Curriculum

- **en-en:** Cognitive psychology, neuroplasticity, growth mindset (5 words)
- **en-zh:** Perseverance, self-cultivation, Chinese philosophical tradition (6 words)
- **vi-zh:** Resilience, emotional regulation, learning journey (6 words)
- **vi-en:** Stepping outside comfort zone, embracing failure, science of learning (6 words)
