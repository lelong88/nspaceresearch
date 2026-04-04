# Description Tone Variety

Rewrote all descriptions across collections, series, and curriculums, plus farewell introAudio scripts, to replace monotonous "Did you know" / "BẠN CÓ BIẾT" openers with varied, individually crafted copy.

## What Was Changed

- **32 collection descriptions** — concise category summaries with varied angles
- **46 series descriptions** — all ≤255 chars, varied tones, no adjacent duplicates within collections
- **326+ curriculum descriptions** — full Persuasive_Copy_Style (bold headline, concrete examples, vivid metaphor, transformation promise), varied tones across 6 opener types
- **~200 farewell introAudio scripts** — individually crafted vocab reviews with warm sign-offs, mp3Url stripped for audio regeneration
- **4 orphaned curriculums** (not in any series) — descriptions rewritten

## Tone Palette (6 types)

1. Provocative question — "TẠI SAO BẠN NỖ LỰC NHƯNG VẪN THẤY MÔNG LUNG?"
2. Bold declaration — "ĐIỆN ẢNH KHÔNG CHỈ LÀ GIẢI TRÍ..."
3. Vivid scenario — "Hãy tưởng tượng bạn đang ngồi trong quán cà phê..."
4. Empathetic observation — "Bạn đã học tiếng Anh bao lâu rồi mà vẫn ngại mở miệng?"
5. Surprising fact — "95% người học ngôn ngữ bỏ cuộc trước khi đạt đến điểm bùng phát."
6. Metaphor-led hook — "Học ngôn ngữ giống như tập gym cho não..."

## Distribution Rules

- No two adjacent items in the same series/collection share the same opener type
- No single opener type > 30% of descriptions at any content level
- Language matches context: Vietnamese for vi-*, English for en-*, Chinese for zh-*

## Verification Queries

```sql
-- Check for template remnants
SELECT id, title FROM curriculum_collections
WHERE description LIKE '%Did you know%' OR description LIKE '%BẠN CÓ BIẾT%';

SELECT id, title FROM curriculum_series
WHERE description LIKE '%Did you know%' OR description LIKE '%BẠN CÓ BIẾT%';

SELECT c.id, c.content->>'title' as title
FROM curriculum c
WHERE c.uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'
AND (c.content->>'description' LIKE '%Did you know%' OR c.content->>'description' LIKE '%BẠN CÓ BIẾT%');

-- Verify series description lengths
SELECT id, title, length(description) FROM curriculum_series WHERE length(description) > 255;

-- Count descriptions
SELECT COUNT(*) as total,
  COUNT(CASE WHEN c.content->>'description' IS NOT NULL AND c.content->>'description' != '' THEN 1 END) as has_desc
FROM curriculum c WHERE c.uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73';
```

## Recreation Instructions

Scripts were deleted after verification. To re-run:

1. Create per-level Python scripts that query IDs from DB at runtime
2. Collection/series updates: POST `curriculum-collection/update` or `curriculum-series/update` with `{id, description, firebaseIdToken}`
3. Curriculum updates: fetch full content via `curriculum/getOne`, replace `content["description"]` and farewell `introAudio.data.text`, strip farewell `data.mp3Url`, push back via `curriculum/update`
4. Auth: `firebase_token.get_firebase_id_token("zs5AMpVfqkcfDf8CJ9qrXdH58d73")`
5. CRITICAL: Preserve all generated keys on non-farewell activities
