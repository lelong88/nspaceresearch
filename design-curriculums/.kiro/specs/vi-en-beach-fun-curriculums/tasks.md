# Implementation Plan: vi-en Beach Fun Curriculums

## Overview

Implement 3 vi-en preintermediate curriculums on the "having fun on the beach" theme, organized into a single Vietnamese-titled series ("Vui Bên Bờ Biển"). The implementation follows the locked design: 6 Python scripts (3 per-curriculum creation scripts, an orchestrator, a non-text helpers module, and a validator), each with hand-written learner-facing text. All locked decisions (vocab lists, titles, description tones, farewell tones, display orders) come from `design.md` and must not be re-derived in the scripts.

Convert the feature design into a series of prompts for a code-generation LLM that will implement each step with incremental progress. Make sure that each prompt builds on the previous prompts, and ends with wiring things together. There should be no hanging or orphaned code that isn't integrated into a previous step. Focus ONLY on tasks that involve writing, modifying, or testing code.

## Tasks

- [x] 1. Set up folder structure and shared infrastructure
  - [x] 1.1 Create `vi-en-beach-fun-curriculums/` working folder at the repo root
    - Folder will hold the 6 scripts during the run and the persistent `README.md` after success
    - _Requirements: 12.5, 12.6_
  - [x] 1.2 Implement `vi-en-beach-fun-curriculums/beach_helpers.py` with non-text structure helpers only
    - Implement `make_intro_audio(title, description, text)`, `make_view_flashcards(title, description, vocab_list)`, `make_reading(title, description, text)`, `make_speak_reading(title, description, text)`, `make_read_along(title, description, text)`, `make_session(title, activities)` — each returns a schema-compliant dict using only its literal-string args (no f-strings, no `.format()`, no substitution on prose)
    - Implement `recursive_strip_keys(content, strip_keys)` (post-order, idempotent, in-place safe) and `recursive_find_keys(content, keys)` (returns dotted paths)
    - Implement `post_to_api(endpoint, body)` which injects `firebaseIdToken` from `firebase_token.get_firebase_id_token("zs5AMpVfqkcfDf8CJ9qrXdH58d73")` and raises on non-2xx with endpoint+status+body
    - Add the explicit-emit allow-list note in code comments: `skillFocusTags`, `difficultyTags`, `lengthTags`, `contentTypeTags` are NOT stripped
    - _Requirements: 9.1–9.5, 11.2, 11.3, 12.4, 13.1_
  - [x] 1.3 Implement `vi-en-beach-fun-curriculums/validate_content.py` with `pre_upload_validate(content, curriculum_label)` and `post_upload_validate(content, curriculum_id)`
    - Pre-upload checks (all of Req 15 AC1–7): non-empty `title`/`description`/`preview.text`; `learningSessions` length exactly 4 with non-empty session titles and ≥1 activity each; every activity has `activityType`, `title`, `description`, `data` non-null and no `type` key; `activityType` ∈ {introAudio, viewFlashcards, reading, speakReading, readAlong}; every `vocabList` is an array of `s == s.lower()` strings and no `words` field substitutes for `vocabList`; no Strip_Keys appear at any depth (load list from `/home/ubuntu/nspaceresearch/design-curriculums/strip-keys.json`); `contentTypeTags` ∈ {["movie"], ["music"], ["podcast"], ["story"], []}
    - Add structural checks tied to the design: 4-session structure (Req 1), session activity ordering and counts (Req 1.5–1.8), 5/5/5 vocab partitioning into W1/W2/W3, 15-word total, lowercase ASCII (Req 3.4–3.5), `data.text` length bounds for reading (1–10000) and introAudio (1–5000), exact `readAlong.description` string, viewFlashcards title/description format, reading/speakReading title format and 80-char (±5) description prefix
    - On failure: write a single stderr line `"[<label>] Req 15.<N> failed at <field-path>"` and raise `ValidationError`; the caller must `sys.exit(1)` within 5 seconds
    - `post_upload_validate` runs the same checks except Strip_Keys absence (post-upload payloads legitimately gain generated keys); returns True/False per curriculum
    - _Requirements: 1.1–1.9, 2.1–2.9, 3.4–3.6, 7.1–7.12, 8.1–8.9, 9.1–9.5, 15.1–15.11_
  - [x] 1.4 Scaffold `vi-en-beach-fun-curriculums/orchestrate_beach_fun.py` with the locked design constants at the top of the file
    - Module-level dicts for: `SERIES_TITLE = "Vui Bên Bờ Biển"`, the 3 curriculum titles, the 3 vocabulary lists (W1/W2/W3 per curriculum), the 3 description headline tones (`vivid_scenario`, `empathetic_observation`, `metaphor_led`), the series description tone (`bold_declaration`), the 3 farewell tones (`team_building_energy`, `practical_momentum`, `quiet_awe`), and the display order map (Beach_Activities=1, Beach_Food=2, Beach_Evening=3)
    - Stub functions `duplicate_check_series(title)`, `duplicate_check_curriculum(title, uid)`, `run_pipeline()` — bodies wired in Task 5
    - _Requirements: 3.1–3.3, 5.3, 6.5, 10.3, 12.2, 14.1, 14.5–14.7_

- [x] 2. Build Curriculum 1 — Vui Chơi & Thể Thao Bãi Biển (Beach Activities & Sports)
  - [x] 2.1 Create `vi-en-beach-fun-curriculums/create_beach_activities.py` with the locked vocab groups as literal lists
    - W1: `["splash", "wave", "swim", "paddle", "float"]`
    - W2: `["surf", "board", "snorkel", "goggles", "fin"]`
    - W3: `["dive", "sandcastle", "frisbee", "volleyball", "kite"]`
    - Define 4 Vietnamese session topic phrases as literal strings (one per session; no templating)
    - _Requirements: 3.1, 3.4–3.6, 12.1, 13.1, 13.2_
  - [x] 2.2 Hand-write the 4 introAudio scripts (Vietnamese)
    - Sessions 1–3: teach each of the 5 W-group words with part of speech, Vietnamese definition (8–40 words), one English example sentence (6–20 words) drawn ONLY from active beach scenarios (catching a wave, building a sandcastle, playing volleyball, paddling, snorkeling), and IPA or Vietnamese phonetic respelling
    - Session 4 farewell (400–600 words target) using the `team_building_energy` register: recap of 5–6 of the 15 words with FRESH English examples (not character-for-character identical to Sessions 1–3), Vietnamese summary of the 4-session progression, warm Vietnamese farewell, ≥1 named Vietnamese beach context (Đà Nẵng / Nha Trang / Phú Quốc / Vũng Tàu / family or friend gathering), and ≤3 such references in the script
    - All examples must avoid food/picnic/evening/sunset scenarios and any distressing content (drowning, jellyfish, sunburn, rip currents, lost children, severe weather, medical emergencies)
    - _Requirements: 6.1–6.7, 13.4, 14.6_
  - [x] 2.3 Hand-write the 4 reading passages (English, first-person)
    - Sessions 1–3: 2–4 sentences each (6–20 words per sentence), open with `I ` or `My `, first-person pronoun set only, no quoted dialogue, every word in the session's W-group appears at least once (case-insensitive whole-word match; `-s/-es/-ed/-ing` inflections accepted), ≥3 sub-topic-specific concrete nouns/actions per passage, exclusively active-beach content
    - Session 4 review: 6–12 sentences (6–20 words each), opens `I ` or `My `, combines the 3 prior narrative threads, every one of the 15 vocabulary words appears at least once
    - _Requirements: 2.1–2.9, 13.2, 13.3_
  - [x] 2.4 Hand-write the curriculum description, preview, and activity metadata
    - Description: ≥200 chars Vietnamese, ≥3 paragraphs separated by blank lines, opens with an ALL-CAPS Vietnamese headline of 3–12 words on its own line using the `vivid_scenario` tone
    - Preview: 120–250 Vietnamese words, opens with a vivid hook naming a beach setting element (sand/wave/sunset/etc.), names all 15 vocabulary words verbatim, references all 4 sessions in display order
    - Activity titles/descriptions per Req 7: `Flashcards: <topic>` / `Học N từ: word1, word2, ...`; `Đọc: <topic>` / first 80 chars of `data.text` (±5); `Nghe: <topic>` / exact string `"Nghe đoạn văn vừa đọc và theo dõi."`; introAudio titles drawn from the allowed set (`Giới thiệu bài học`, `Giới thiệu từ vựng`, `Lời tạm biệt`)
    - Session titles: `"Phần 1"`, `"Phần 2"`, `"Phần 3"`, `"Ôn tập"`
    - _Requirements: 4.1, 4.4–4.7, 5.2, 5.4, 5.5, 7.1–7.6, 8.1–8.3, 14.5_
  - [x] 2.5 Implement `build_content()` in `create_beach_activities.py` assembling the full content JSON via `beach_helpers`
    - Wire all sessions and activities; set top-level `contentTypeTags=[]`, `lengthTags=["medium"]`, `skillFocusTags=["speaking_focus"]`, `difficultyTags=["preintermediate", "vocab_preintermediate", "reading_preintermediate"]`
    - Run `recursive_strip_keys` then `recursive_find_keys` to confirm zero Strip_Keys remain; raise on residual matches
    - Run `pre_upload_validate(content, "beach_activities")`; on failure, exit 1
    - On pass, POST `curriculum/create` with body `{firebaseIdToken, language: "en", userLanguage: "vi", content: json.dumps(content)}` and return the curriculum id (omit `isPublic`)
    - _Requirements: 8.1–8.9, 9.1–9.5, 11.1–11.7, 14.4, 15.1–15.9_

- [x] 3. Build Curriculum 2 — Ăn Uống & Thư Giãn Bên Biển (Beach Food & Relaxation)
  - [x] 3.1 Create `vi-en-beach-fun-curriculums/create_beach_food.py` with the locked vocab groups as literal lists
    - W1: `["picnic", "basket", "towel", "sandals", "sunscreen"]`
    - W2: `["grill", "snack", "coconut", "smoothie", "umbrella"]`
    - W3: `["lounge", "tan", "doze", "breeze", "hammock"]`
    - Define 4 Vietnamese session topic phrases as literal strings
    - _Requirements: 3.2, 3.4–3.6, 12.1, 13.1, 13.2_
  - [x] 3.2 Hand-write the 4 introAudio scripts (Vietnamese)
    - Sessions 1–3: teach each W-group word with part of speech, Vietnamese definition (8–40 words), one English example (6–20 words) drawn ONLY from slow beach food and rest scenarios (unpacking a picnic basket, sipping a coconut smoothie, dozing under an umbrella, lounging in a hammock), IPA or phonetic respelling
    - Session 4 farewell (400–600 words target) using the `practical_momentum` register: recap of 5–6 words with FRESH English examples, 4-session progression summary, warm farewell, ≥1 Vietnamese beach context, ≤3 references
    - No active sport, evening, or bonfire scenario examples; no distressing content
    - _Requirements: 6.1–6.7, 13.5, 14.6_
  - [x] 3.3 Hand-write the 4 reading passages (English, first-person)
    - Sessions 1–3: 2–4 sentences each (6–20 words per sentence), open with `I ` or `My `, first-person only, no quoted dialogue, every W-group word appears (with allowed inflections), exclusively beach picnic / sunbathing / lounging / dozing / under-umbrella content
    - Session 4 review: 6–12 sentences combining the 3 narrative threads with all 15 vocab words
    - No 8+ consecutive-word substring shared with Curriculum 1's corresponding fields
    - _Requirements: 2.1–2.9, 13.2, 13.3_
  - [x] 3.4 Hand-write the curriculum description, preview, and activity metadata
    - Description headline tone: `empathetic_observation` (different from Curriculum 1's `vivid_scenario`)
    - Preview: 120–250 Vietnamese words, vivid hook naming a beach setting element, names all 15 vocab words verbatim, references all 4 sessions in display order
    - Activity titles/descriptions and session titles per the schema in Task 2.4
    - _Requirements: 4.2, 4.4–4.7, 5.2–5.5, 7.1–7.6, 8.1–8.3, 14.5_
  - [x] 3.5 Implement `build_content()` in `create_beach_food.py` assembling the full content JSON via `beach_helpers`
    - Same wiring as Task 2.5: explicit top-level tags, strip-keys removal + re-verify, `pre_upload_validate(content, "beach_food")`, POST `curriculum/create` with `language="en"`, `userLanguage="vi"`
    - _Requirements: 8.1–8.9, 9.1–9.5, 11.1–11.7, 14.4, 15.1–15.9_

- [x] 4. Build Curriculum 3 — Hoàng Hôn & Lửa Trại Bên Biển (Sunset & Evening Beach Fun)
  - [x] 4.1 Create `vi-en-beach-fun-curriculums/create_beach_evening.py` with the locked vocab groups as literal lists
    - W1: `["sunset", "twilight", "shore", "tide", "glow"]`
    - W2: `["bonfire", "firelight", "marshmallow", "blanket", "gather"]`
    - W3: `["stargaze", "lantern", "guitar", "laughter", "drift"]`
    - Define 4 Vietnamese session topic phrases as literal strings
    - _Requirements: 3.3, 3.4–3.6, 12.1, 13.1, 13.2_
  - [x] 4.2 Hand-write the 4 introAudio scripts (Vietnamese)
    - Sessions 1–3: teach each W-group word with part of speech, Vietnamese definition (8–40 words), one English example (6–20 words) drawn ONLY from evening beach scenarios (gathering around a bonfire, watching the sunset paint the sky, stargazing on a blanket, listening to laughter and a guitar by firelight), IPA or phonetic respelling
    - Session 4 farewell (400–600 words target) using the `quiet_awe` register: recap of 5–6 words with FRESH English examples, 4-session progression summary, warm farewell, ≥1 Vietnamese beach context, ≤3 references
    - No active daytime sport or food picnic scenarios; no distressing content
    - _Requirements: 6.1–6.7, 13.6, 14.6_
  - [x] 4.3 Hand-write the 4 reading passages (English, first-person)
    - Sessions 1–3: 2–4 sentences each (6–20 words per sentence), open with `I ` or `My `, first-person only, no quoted dialogue, every W-group word appears (with allowed inflections), exclusively sunset/bonfire/stargazing/lantern/evening-music content
    - Session 4 review: 6–12 sentences combining the 3 narrative threads with all 15 vocab words
    - No 8+ consecutive-word substring shared with Curriculum 1 or Curriculum 2's corresponding fields
    - _Requirements: 2.1–2.9, 13.2, 13.3_
  - [x] 4.4 Hand-write the curriculum description, preview, and activity metadata
    - Description headline tone: `metaphor_led` (different from adjacent Curriculum 2's `empathetic_observation`)
    - Preview: 120–250 Vietnamese words, vivid hook naming a beach setting element, names all 15 vocab words verbatim, references all 4 sessions in display order
    - Activity titles/descriptions and session titles per the schema in Task 2.4
    - _Requirements: 4.3, 4.4–4.7, 5.2–5.5, 7.1–7.6, 8.1–8.3, 14.5_
  - [x] 4.5 Implement `build_content()` in `create_beach_evening.py` assembling the full content JSON via `beach_helpers`
    - Same wiring as Tasks 2.5 / 3.5: explicit top-level tags, strip-keys removal + re-verify, `pre_upload_validate(content, "beach_evening")`, POST `curriculum/create` with `language="en"`, `userLanguage="vi"`
    - _Requirements: 8.1–8.9, 9.1–9.5, 11.1–11.7, 14.4, 15.1–15.9_

- [x] 5. Checkpoint — review all 3 curriculum content files
  - Manually review every reading passage, introAudio script, description, and preview against the locked design constraints. Ensure all tests pass, ask the user if questions arise.
  - _Requirements: 13.2, 13.3, 14.2, 14.3_

- [x] 6. Wire orchestrator end-to-end
  - [x] 6.1 Implement series creation and duplicate-check in `orchestrate_beach_fun.py`
    - `duplicate_check_series("Vui Bên Bờ Biển")` queries `curriculum_series` for a matching trimmed, case-sensitive, non-`_deleted` row; reuse seriesId if present
    - Otherwise POST `curriculum-series/create` with title `"Vui Bên Bờ Biển"` and a Vietnamese description (40–255 chars) using the `bold_declaration` tone (different from Curriculum 1's `vivid_scenario` headline)
    - On non-2xx, halt the run with endpoint + response in stderr
    - _Requirements: 5.1, 5.7, 10.1, 10.2, 11.7, 16.7_
  - [x] 6.2 Implement the per-curriculum loop in `run_pipeline()`
    - Iterate `["activities", "food", "evening"]` in order. For each: import the corresponding `create_*` module, call its `build_content()`, run strip-keys + re-verify, `pre_upload_validate`, POST `curriculum/create` (with `language="en"`, `userLanguage="vi"`, no `isPublic`), capture the new curriculum id
    - Immediately after `curriculum/create`, call `duplicate_check_curriculum(title, uid="zs5AMpVfqkcfDf8CJ9qrXdH58d73")` against `content->>'title'`; on >1 row keep earliest by `created_at` (tie-break smallest id), `curriculum-series/removeCurriculum` then `curriculum/delete` for each duplicate; log non-2xx but continue cleanup
    - Then POST `curriculum-series/addCurriculum` followed immediately by `curriculum/setDisplayOrder` with the integer 1, 2, or 3 from the locked map; halt the dependent chain on non-2xx
    - _Requirements: 10.3, 10.4, 10.5, 10.7, 10.8, 11.1, 11.4, 11.5, 11.6, 11.7, 16.1–16.6_
  - [x] 6.3 Implement post-upload validation aggregation
    - For each created curriculum id, POST `curriculum/getOne` and run `post_upload_validate` against the returned content (Strip_Keys check skipped per the design clarification)
    - Print one stdout line per curriculum: `"[<label>] post-upload PASS"` or `"[<label>] post-upload FAIL: Req 15.<N> at <path>"`
    - If any fail, set a flag preventing source-script deletion and exit 1 after printing all results
    - _Requirements: 15.10, 15.11_

- [x] 7. Run the pipeline end-to-end against the API
  - [x] 7.1 Execute `python orchestrate_beach_fun.py` from `vi-en-beach-fun-curriculums/`
    - Confirms Firebase auth succeeds for UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`, all 3 curriculums upload with the 3 locked titles, the series is created (or reused), and all addCurriculum + setDisplayOrder calls return 2xx
    - _Requirements: 10.1–10.8, 11.1–11.7, 12.2_
  - [x] 7.2 Run database verification SQL via the postgres MCP
    - Query `curriculum_series_items` joined to `curriculum` to confirm exactly the 3 curriculum ids appear under the series with non-null `content->>'title'`, `is_public = false`, `language = 'en'`, `user_language = 'vi'`, and uid not ending in `_deleted`; confirm display orders 1/2/3 match the locked map
    - Query `curriculum_series_language_list` to verify a single homogeneous row (en/vi) for the series, and `curriculum_series_level_gap` to confirm a 0-level gap (all preintermediate)
    - _Requirements: 10.6, 10.7, 12.5, 14.1, 14.4_
  - [x] 7.3 Run cross-curriculum vocabulary uniqueness check
    - Collect the 3 vocabLists from the persisted content; assert union has exactly 45 entries with zero pairwise overlap (case-insensitive, trimmed)
    - _Requirements: 3.6, 14.3_

- [x] 8. Checkpoint — confirm DB state matches design
  - Ensure all tests pass, ask the user if questions arise. Verify the README target structure and that scripts can be safely deleted only after the DB confirms all 3 curriculums.
  - _Requirements: 12.5, 12.7, 12.8_

- [x] 9. Documentation and cleanup
  - [x] 9.1 Create `vi-en-beach-fun-curriculums/README.md` with the 9 required non-empty sections
    - (a) Series ID + Vietnamese title; (b) Curriculum IDs + Vietnamese titles; (c) Display orders; (d) Vocabulary lists per curriculum (15 each, partitioned by W1/W2/W3); (e) Description tone assignments (vivid_scenario / empathetic_observation / metaphor_led); (f) Farewell tone assignments (team_building_energy / practical_momentum / quiet_awe); (g) Creation method summary; (h) SQL queries to find series and curriculums in the DB; (i) Recreation context (locked design pointers, UID, language pair)
    - _Requirements: 12.5, 12.6_
  - [x] 9.2 Delete `create_beach_activities.py`, `create_beach_food.py`, `create_beach_evening.py`, `orchestrate_beach_fun.py`, `beach_helpers.py`, `validate_content.py` — only AFTER Task 7.2 returns all 3 curriculums in the DB
    - If DB verification did not return all 3 curriculums, leave every script on disk and skip this task
    - _Requirements: 12.7, 12.8_

## Notes

- This spec has no "Correctness Properties" section in `design.md`, so no property-based test sub-tasks are added. Validation is performed by `validate_content.py` against the corruption rules in Requirement 15.
- Unit/integration tests are not appropriate for this content-creation work; the design's pre-upload and post-upload validators are the quality gate.
- All learner-facing text is hand-written as literal Python strings — no f-strings, no `.format()`, no shared text templates anywhere across the 6 files (Requirements 12.3, 13.1).
- Locked design decisions (vocab, titles, tones, display orders) live as module-level constants in `orchestrate_beach_fun.py` and are mirrored as literal values in the per-curriculum scripts; any divergence triggers a validation failure.
- Each task references the specific requirement clauses it satisfies, including granular sub-clauses where relevant.
- Scripts MUST run successfully against the API and the DB MUST confirm all 3 curriculums BEFORE any cleanup deletion (per `product.md` "Script Lifecycle — NEVER Delete Before Execution").

## Task Dependency Graph

```json
{
  "waves": [
    { "id": 0, "tasks": ["1.1"] },
    { "id": 1, "tasks": ["1.2", "1.3", "1.4"] },
    { "id": 2, "tasks": ["2.1", "3.1", "4.1"] },
    { "id": 3, "tasks": ["2.2", "2.3", "2.4", "3.2", "3.3", "3.4", "4.2", "4.3", "4.4"] },
    { "id": 4, "tasks": ["2.5", "3.5", "4.5"] },
    { "id": 5, "tasks": ["6.1"] },
    { "id": 6, "tasks": ["6.2"] },
    { "id": 7, "tasks": ["6.3"] },
    { "id": 8, "tasks": ["7.1"] },
    { "id": 9, "tasks": ["7.2", "7.3"] },
    { "id": 10, "tasks": ["9.1"] },
    { "id": 11, "tasks": ["9.2"] }
  ]
}
```
