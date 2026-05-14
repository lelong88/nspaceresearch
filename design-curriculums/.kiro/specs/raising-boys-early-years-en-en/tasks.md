# Implementation Plan: raising-boys-early-years-en-en

## Overview

Convert the feature design into a series of prompts for a code-generation LLM that
will implement each step with incremental progress. Make sure that each prompt
builds on the previous prompts, and ends with wiring things together. There
should be no hanging or orphaned code that isn't integrated into a previous
step. Focus ONLY on tasks that involve writing, modifying, or testing code.

This plan implements the locked design: a new repo-root folder
`raising-boys-early-years-en-en/` containing five Python scripts (helpers,
validator, two curriculum builders, orchestrator) that hand-craft and upload
two en-en advanced parenting curriculums based on Steve Biddulph's *Raising
Boys*. Every locked decision (titles, the 30-item vocabulary partitions in
design §D5, the per-session reading themes in §D6, description tone
assignments in §D8, farewell registers in §D9, series placement in §D10,
`contentTypeTags = []`, `difficultyTags = ["advanced", "vocab_advanced",
"reading_advanced", "writing_advanced"]`) is consumed verbatim from the design
and is never re-derived in the scripts. All learner-facing prose is written
as literal Python string constants — no `f`-strings, no `.format()`, no
`string.Template`, no shared text builders.

The curriculums must be created via `curriculum/create` with `language="en"`,
`userLanguage="en"`, and `content` as top-level body params. The orchestrator
applies the truly-generated subset of `strip-keys.json`
(`{mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems,
userReadingId, lessonUniqueId, curriculumTags, taskId, imageId,
practiceMinutes, practiceTime}`) before upload while emitting `difficultyTags`,
`skillFocusTags`, `lengthTags`, and `contentTypeTags` explicitly. No
`setPublic` is ever called. Scripts are deleted only after both curriculum
rows are confirmed present and non-deleted in PostgreSQL via the design's
verification SQL.

## Tasks

- [x] 1. Set up folder structure and shared infrastructure
  - [x] 1.1 Create `raising-boys-early-years-en-en/` working folder at the repo root
    - Folder will hold the five run scripts during the run and the persistent
      `README.md` after success-and-cleanup
    - Folder is sibling to `vi-en-beach-fun-curriculums/`,
      `en-en-education-tutoring-curriculums/`, and the existing learner
      folders; do NOT place code inside `.kiro/specs/...`
    - _Requirements: 11.4, 11.5_
  - [x] 1.2 Implement `raising-boys-early-years-en-en/raising_boys_helpers.py` with structure-only helpers (no prose templating)
    - Define module-level constant `STRIP_KEYS = {"mp3Url", "illustrationSet",
      "chapterBookmarks", "segments", "whiteboardItems", "userReadingId",
      "lessonUniqueId", "curriculumTags", "taskId", "imageId",
      "practiceMinutes", "practiceTime"}` (truly-generated subset of
      `strip-keys.json`); add a code comment that `difficultyTags`,
      `skillFocusTags`, `contentTypeTags`, and `lengthTags` are emitted
      explicitly and MUST NOT be added here
    - Implement `make_intro_audio(title, description, text)`,
      `make_view_flashcards(title, description, vocab_list)`,
      `make_speak_flashcards(title, description, vocab_list)`,
      `make_vocab_level_1(title, description, vocab_list)`,
      `make_vocab_level_2(title, description, vocab_list)`,
      `make_reading(title, description, text)`,
      `make_speak_reading(title, description, text)`,
      `make_read_along(title, description, text)`,
      `make_writing_sentence(title, description, vocab_list, items)`,
      `make_writing_paragraph(title, description, vocab_list, instructions, prompts)`,
      `make_session(title, activities)` — each returns a schema-compliant dict
      and only assembles its already-written literal-string arguments (no
      f-strings, no `.format()`, no `string.Template`, no substitution on
      prose); the structural concat
      `description = "Words: " + ", ".join(vocab_list)` is allowed because it
      is structural reuse of an already-written list, not prose generation
    - Implement `recursive_strip_keys(content, strip_keys)` (post-order,
      idempotent, returns a new structure) and
      `recursive_find_keys(content, keys)` (returns dotted paths to any
      remaining occurrence)
    - Implement `post_to_api(endpoint, body)` which prepends
      `https://helloapi.step.is`, injects `firebaseIdToken` from
      `firebase_token.get_firebase_id_token("zs5AMpVfqkcfDf8CJ9qrXdH58d73")`,
      raises on non-2xx with endpoint + status + body, and returns the parsed
      JSON; uses `sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")`
      to import the repo-root helper
    - _Requirements: 4.1, 4.2, 11.2_

  - [x] 1.3 Property test 2 — `recursive_find_keys(content, STRIP_KEYS) == []` on a fixture content dict that has been passed through `recursive_strip_keys`
    - **Property 2: Strip-keys absence in pre-upload content**
    - **Validates: Requirements 4.1, 4.2**
    - Build a fixture mirroring the reference curriculum's shape, including
      one `mp3Url`, one `illustrationSet`, one nested `segments` array, one
      `userReadingId`, and one `lessonUniqueId`; assert that after
      `recursive_strip_keys` the `recursive_find_keys` call returns an empty
      list

  - [x] 1.4 Implement `raising-boys-early-years-en-en/validate_raising_boys.py` skeleton
    - Define `class ValidationError(AssertionError)`
    - Define `pre_upload_validate(content: dict, label: str) -> None` and
      `post_upload_validate(returned_content: dict, label: str) -> None` as
      sequencers that call individual property checks (filled in by Task 2);
      both raise `ValidationError` on the first failure and surface the
      property number plus the failing field path in the message
    - Define module-level constants `REFERENCE_BEGINNER_VOCAB_SET = {"bond",
      "safe", "warmth", "to respond", "to hold", "to cry", "baby", "love",
      "family", "mother", "father", "son", "boy", "gentle", "calm", "smile",
      "eye contact", "hug"}` (per design Property 5) and
      `A1_STAPLES_BLACKLIST = {"baby", "love", "safe", "to hold", "to cry",
      "mom", "mum", "dad", "hug", "kiss", "play", "run", "jump", "eat",
      "sleep", "big", "small", "happy", "sad", "boy", "girl", "friend"}`
      (per design Property 6)
    - Define module-level constant `ENGLISH_ALLOW_UNICODE = {"\u201c",
      "\u201d", "\u2018", "\u2019", "\u2026", "\u2014", "\u2013"}` (smart
      quotes, ellipsis, em-dash, en-dash) plus the ASCII letters/digits/
      whitespace/standard-punctuation set (per design Property 1)
    - `post_upload_validate` skips Property 2 (strip-keys absence) — the
      platform may legitimately add `mp3Url`, `lessonUniqueId`, etc. after
      creation — and runs every other property
    - _Requirements: 14.1, 14.2_

  - [x] 1.5 Scaffold `raising-boys-early-years-en-en/orchestrate_raising_boys.py` with the locked design constants
    - Module-level constants:
      `UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"`, `LANGUAGE = "en"`,
      `USER_LANGUAGE = "en"`,
      `CURRICULUM_A_TITLE = "Raising Boys 4\u20135: The Last of the Tender Years"`,
      `CURRICULUM_B_TITLE = "Raising Boys 6\u20137: When the Father Years Switch On"`,
      `SERIES_TITLE = "Raising Boys: The Early Years"`,
      `HOST_SERIES_DECISION = "create"`, `DISPLAY_ORDER_A = 1`,
      `DISPLAY_ORDER_B = 2`, `TONE_A = "empathetic_observation"`,
      `TONE_B = "provocative_question"`, `TONE_SERIES = "metaphor_led"`,
      `FAREWELL_REGISTER_A = "introspective_guide"`,
      `FAREWELL_REGISTER_B = "practical_momentum"`
    - Stub functions `duplicate_check_curriculum(title)`,
      `duplicate_check_series(title)`, `create_or_reuse_series()`,
      `create_curriculum(label, module)`, `verify_db_state()`,
      `write_readme()`, `cleanup_scripts()`, `run_pipeline()`; bodies wired in
      Tasks 4–6
    - Module MUST NOT contain the substring `"setPublic"` anywhere (Property
      24, Requirement 11.1) — add a code comment forbidding it
    - Module MUST NOT contain the substring
      `"curriculum-collection/setDisplayOrder"` anywhere (Property 27,
      Requirement 12.5) — add a code comment forbidding it
    - _Requirements: 11.1, 11.2, 12.5, 13.1, 13.2_

- [x] 2. Implement the 30+1 correctness properties as validator functions
  - [x] 2.1 Property 1 — English-only check
    - **Property 1: All user-facing strings are English-only**
    - **Validates: Requirements 2.3, 2.5, 2.6, 2.7, 5.6, 7.3, 9.1, 9.2**
    - Walk every user-facing string field in `content` (`title`,
      `description`, `preview.text`, every session `title`, every activity
      `title`/`description`/`data.text`/`data.instructions`/`data.prompts[*]`/
      `data.items[*].prompt`); reject any character outside the allow-set
      defined in `validate_raising_boys.py` constants

  - [x] 2.2 Property 3 — Reference-curriculum structural arc preserved
    - **Property 3: Reference-curriculum structural arc is preserved**
    - **Validates: Requirements 4.3, 4.4, 8.5**
    - Assert `len(content["learningSessions"]) == 5`; for `i \u2208 {0, 1, 2}`
      assert the activity-type sequence is exactly
      `["introAudio", "introAudio", "viewFlashcards", "speakFlashcards",
      "vocabLevel1", "vocabLevel2", "introAudio", "reading", "speakReading",
      "readAlong"]`; assert session index 3 has no `reading` and contains a
      `viewFlashcards`, a `vocabLevel1`, and a `vocabLevel2`; assert session
      index 4 has exactly one each of `reading`, `speakReading`, `readAlong`,
      with at least one `introAudio` at the end

  - [x] 2.3 Property 4 — Vocabulary count bands
    - **Property 4: Vocabulary count bands**
    - **Validates: Requirements 5.1, 4.5**
    - Compute the deduplicated union of `data.vocabList` across the
      `viewFlashcards` activities of `content["learningSessions"][0..2]` and
      assert its size is in `[30, 48]`; for each `i \u2208 {0, 1, 2}` assert
      the `viewFlashcards` `vocabList` has size in `[6, 10]`

  - [x] 2.4 Property 5 — Taught vocabulary disjoint from reference beginner set
    - **Property 5: Taught vocabulary disjoint from beginner reference set**
    - **Validates: Requirement 5.5**
    - Assert the taught-vocab union from Property 4 is disjoint from
      `REFERENCE_BEGINNER_VOCAB_SET`

  - [x] 2.5 Property 6 — Taught vocabulary disjoint from A1-staples blacklist
    - **Property 6: Taught vocabulary disjoint from A1-staples blacklist**
    - **Validates: Requirement 5.2**
    - Assert the taught-vocab union from Property 4 is disjoint from
      `A1_STAPLES_BLACKLIST`

  - [x] 2.6 Property 7 — Per-session reading word-count band
    - **Property 7: Per-session reading word-count band**
    - **Validates: Requirement 6.1**
    - For each `i \u2208 {0, 1, 2}`, take the unique `reading` activity in
      `content["learningSessions"][i]` and assert
      `len(data.text.split()) \u2208 [220, 360]`

  - [x] 2.7 Property 8 — Whole-text reading is paragraph-joined concatenation
    - **Property 8: Whole-text reading is paragraph-joined concatenation**
    - **Validates: Requirement 6.2**
    - Assert
      `whole_text == "\\n\\n".join([per_session_reading_text(C, 0), per_session_reading_text(C, 1), per_session_reading_text(C, 2)])`
      where `whole_text` is the `data.text` of the unique `reading` in
      `content["learningSessions"][4]`

  - [x] 2.8 Property 9 — Average sentence length band in reading passages
    - **Property 9: Average sentence length band in reading passages**
    - **Validates: Requirement 6.3**
    - For every `reading` activity (per-session and whole-text), split
      sentences on `.`, `?`, `!`; for each non-empty sentence compute
      `len(sentence.split())`; assert the average across sentences is in
      `[14, 22]`

  - [x] 2.9 Property 10 — Vocabulary embedded in same-session reading
    - **Property 10: Vocabulary embedded in same-session reading**
    - **Validates: Requirement 6.4**
    - For each `i \u2208 {0, 1, 2}` and each `v` in the session's
      `viewFlashcards.vocabList`, assert `v` appears as a case-insensitive
      substring of the session's `reading.data.text`

  - [x] 2.10 Property 11 — reading / speakReading / readAlong text identity
    - **Property 11: reading / speakReading / readAlong text identity per session**
    - **Validates: Requirements 6.5, 6.6**
    - For each session containing a `reading` activity, assert every
      `speakReading` and `readAlong` activity in the same session has a
      `data.text` byte-identical to the `reading.data.text`

  - [x] 2.11 Property 12 — Writing prompts reference \u2265 2 curriculum-taught vocab items
    - **Property 12: Writing prompts reference \u2265 2 curriculum-taught vocab items**
    - **Validates: Requirement 7.4**
    - For each writing activity, build the haystack as the case-folded join
      of the activity's prompt fields (`writingSentence`:
      `data.items[*].prompt`; `writingParagraph`: `data.instructions` plus
      every `data.prompts[*]`); assert at least 2 distinct items from the
      curriculum-taught vocab set appear as case-insensitive substrings

  - [x] 2.12 Property 13 — writingParagraph instructions state an 80\u2013150-word range
    - **Property 13: writingParagraph instructions state an 80\u2013150-word range**
    - **Validates: Requirement 7.5**
    - For every `writingParagraph` activity, regex-match
      `data.instructions` against
      `(8[0-9]|9[0-9]|1[0-4][0-9]|150)\\s*(?:to|\u2013|-|\u2014)\\s*(8[0-9]|9[0-9]|1[0-4][0-9]|150)\\s*words`
      case-insensitively; assert the first integer is \u2265 80, the second is
      \u2264 150, and second \u2265 first

  - [x] 2.13 Property 14 — Session count band
    - **Property 14: Session count band**
    - **Validates: Requirement 8.1**
    - Assert `len(content["learningSessions"]) \u2208 [4, 6]`

  - [x] 2.14 Property 15 — First-session opener and last-session closer are introAudio
    - **Property 15: First-session opener and last-session closer are introAudio**
    - **Validates: Requirements 8.2, 8.3**
    - Assert `learningSessions[0].activities[0].activityType == "introAudio"`
      and `learningSessions[-1].activities[-1].activityType == "introAudio"`

  - [x] 2.15 Property 16 — Penultimate session is a cumulative review
    - **Property 16: Penultimate session is a cumulative review**
    - **Validates: Requirement 8.4**
    - Take `P = learningSessions[-2]`; assert `P` contains exactly one
      activity of each of `viewFlashcards`, `vocabLevel1`, `vocabLevel2`; for
      each of those three activities, assert `set(data.vocabList) \u2287`
      Property 4's deduplicated taught-vocab union

  - [x] 2.16 Property 17 — Writing activities appear after the reading block of their session
    - **Property 17: Writing activities appear after the reading block of their session**
    - **Validates: Requirement 8.6**
    - For every session that contains both a writing activity and a `reading`
      activity, assert each writing activity index is strictly greater than
      every `reading` activity index in that session's `activities` list

  - [x] 2.17 Property 18 — Description headline is ALL-CAPS
    - **Property 18: Description headline is ALL-CAPS**
    - **Validates: Requirement 9.3**
    - Take the first non-empty line of `content["description"]`; assert it
      equals its `.upper()` form and has length \u2265 6

  - [x] 2.18 Property 19 — Description is multi-paragraph and names Biddulph and the book
    - **Property 19: Description is multi-paragraph and names Biddulph and the book**
    - **Validates: Requirement 9.5**
    - Assert `len(description.split("\\n\\n")) >= 2`,
      `"Biddulph" in description`, and `"Raising Boys" in description`

  - [x] 2.19 Property 20 — Vague-intensifier cap in description
    - **Property 20: Vague-intensifier cap in description**
    - **Validates: Requirement 9.6**
    - Sum the case-insensitive whole-word counts (regex
      `\\b(very|really|super|incredibly)\\b`) across `description`; assert
      the sum is \u2264 2

  - [x] 2.20 Property 21 — Title shape: no level word, age-band substring present
    - **Property 21: Title shape \u2014 no level word, age-band substring present**
    - **Validates: Requirement 9.1**
    - Assert the lowercased title contains none of `{"beginner",
      "intermediate", "advanced", "upper-intermediate",
      "upper intermediate", "preintermediate", "pre-intermediate"}`;
      additionally, when `label == "A"` assert the title contains both `"4"`
      and `"5"`, and when `label == "B"` assert the title contains both `"6"`
      and `"7"`

  - [x] 2.21 Property 22 — Preview word-count band
    - **Property 22: Preview word-count band**
    - **Validates: Requirement 9.2**
    - Assert `len(content["preview"]["text"].split()) \u2208 [60, 200]`

  - [x] 2.22 Property 23 — contentTypeTags is present and a valid array value
    - **Property 23: contentTypeTags is present and a valid array value**
    - **Validates: Requirements 10.1, 10.2**
    - Assert `"contentTypeTags" in content`,
      `isinstance(content["contentTypeTags"], list)`, and the value is one of
      `[]`, `["movie"]`, `["music"]`, `["podcast"]`, `["story"]`

  - [x] 2.23 Property 24 — No setPublic call in any script
    - **Property 24: No setPublic call and both rows stay private**
    - **Validates: Requirement 11.1**
    - Static-analysis test: read every `*.py` file in
      `raising-boys-early-years-en-en/` and assert the literal substring
      `"setPublic"` does NOT appear in any of them

  - [x] 2.24 Property 27 — No collection setDisplayOrder call in any script
    - **Property 27: No collection displayOrder is set**
    - **Validates: Requirement 12.5**
    - Static-analysis test: read every `*.py` file in
      `raising-boys-early-years-en-en/` and assert the literal substring
      `"curriculum-collection/setDisplayOrder"` does NOT appear in any of
      them

  - [x] 2.25 Property 28 — Description-tone distinctness across the spec batch
    - **Property 28: Description-tone distinctness across the spec batch**
    - **Validates: Requirements 9.4, 13.1, 13.2, 13.3**
    - Build the tone batch
      `T = [TONE_A, TONE_B] + ([TONE_SERIES] if HOST_SERIES_DECISION == "create" else [])`
      from the orchestrator's locked constants; assert
      `max(Counter(T).values()) == 1`

  - [x] 2.26 Property 30b — difficultyTags strict superset
    - **Property 30b: difficultyTags strict superset**
    - **Validates: Requirement 2.4**
    - Assert `set(content["difficultyTags"]) >=
      {"advanced", "vocab_advanced", "reading_advanced", "writing_advanced"}`

  - [x] 2.27 Property 25 — Any parent attached to either curriculum is en-en pure
    - **Property 25: Any parent attached to either curriculum is en-en pure**
    - **Validates: Requirements 12.1, 12.2, 12.4**
    - Post-creation DB test: query
      `curriculum_series_language_list` joined with
      `curriculum_series_items` to assert every series containing either new
      curriculum id has `language_list = ['en']` and
      `user_language_list = ['en']`; query
      `curriculum_collections_language_list` joined with the corresponding
      collection-items table to assert the same for collections; when the
      orchestrator runs with `HOST_SERIES_DECISION = "skip"`, assert no
      series and no collection contains either id

  - [x] 2.28 Property 26 — New series description size and tone distinctness when created
    - **Property 26: New series description size and tone distinctness when created**
    - **Validates: Requirement 12.3**
    - Conditional on `HOST_SERIES_DECISION == "create"`: query the new series
      row by `title = 'Raising Boys: The Early Years'` and assert
      `length(description) <= 255`; assert the language pair via
      `curriculum_series_language_list` is `(['en'], ['en'])`; assert
      `TONE_SERIES != TONE_A` and `TONE_SERIES != TONE_B` from the
      orchestrator's constants

  - [x] 2.29 Property 29 — DB locate-by-language-title query returns the two rows
    - **Property 29: DB locate-by-language-title query returns the two rows**
    - **Validates: Requirement 14.1**
    - Run the design's §"Verification SQL" §14.1 query against PostgreSQL via
      MCP postgres; assert exactly 2 rows are returned with
      `(language, user_language) = ('en', 'en')`, titles equal to
      `CURRICULUM_A_TITLE` and `CURRICULUM_B_TITLE`, and `uid NOT LIKE
      '%_deleted'`

  - [x] 2.30 Property 30 — DB difficultyTags / contentTypeTags shape query passes
    - **Property 30: DB difficultyTags / contentTypeTags shape query passes**
    - **Validates: Requirements 14.2, 2.4**
    - Run the design's §"Verification SQL" §14.2 query; assert exactly 2 rows
      with `(content->'difficultyTags') @> '["advanced"]'::jsonb = true` and
      `jsonb_typeof(content->'contentTypeTags') = 'array'`

  - [x] 2.31 Wire all property functions into `pre_upload_validate` and `post_upload_validate`
    - In `pre_upload_validate`, call Properties 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
      11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 30b in order; on
      first failure raise `ValidationError` with the property number and
      field path
    - In `post_upload_validate`, call the same set EXCEPT Property 2
      (strip-keys absence) — the platform legitimately adds generated keys
      after creation
    - Properties 24, 25, 26, 27, 28, 29, 30 are run by the orchestrator (via
      static-analysis or DB queries), not by the per-content validators
    - _Requirements: 14.1, 14.2_

- [x] 3. Build Curriculum A — *Raising Boys 4\u20135: The Last of the Tender Years*
  - [x] 3.1 Author Curriculum_A vocabulary partition and session themes (literal Python lists / strings)
    - In `raising-boys-early-years-en-en/create_raising_boys_a_tender_years.py`,
      define module-level constants:
      `VOCAB_S1 = ["attunement", "co-regulation", "to soothe", "meltdown",
      "overwhelm", "to validate", "disappointment", "frustration",
      "composure", "to acknowledge"]`,
      `VOCAB_S2 = ["narrative", "to scaffold", "vocabulary", "pretend play",
      "make-believe", "to elaborate", "articulate", "dialogue", "imagination",
      "to recount"]`,
      `VOCAB_S3 = ["boisterous", "tantrum", "to wind down", "nervous system",
      "to settle", "vigorous", "physical affection", "restless",
      "to discharge", "proprioception"]`
    - All entries are lowercase ASCII (multi-token entries like
      `"pretend play"`, `"co-regulation"`, `"physical affection"`, and the
      `"to <verb>"` form are allowed per design §"Vocab list lowercase rule")
    - Define the three per-session theme strings used by Property D6:
      Session 1 = `"Naming the inner weather"`,
      Session 2 = `"The language explosion and imaginative play"`,
      Session 3 = `"Bodies, big feelings, and somatic regulation"`
    - _Requirements: 5.1, 5.2, 5.3, 5.5, 5.6_

  - [x] 3.2 Hand-write Curriculum_A intro audio scripts (English literal strings)
    - For Sessions 1, 2, 3: write a theme `introAudio` script (500\u2013900 words)
      framing the developmental thesis; a vocabulary `introAudio` script
      (700\u20131200 words) teaching all 10 of the session's `Vocab_Item`s with
      a one-or-two-sentence English definition and at least one English
      example sentence per item (Requirement 5.6); a grammar/usage
      `introAudio` script (400\u2013700 words) tied to a register or syntax point
      visible in the session's reading
    - Session 5 farewell `introAudio` script (400\u2013600 words) using register
      `FAREWELL_REGISTER_A = "introspective_guide"` (design §D9), reviewing
      5\u20136 of the 30 `Vocab_Item`s with definitions and FRESH English example
      sentences (not character-for-character identical to Sessions 1\u20133)
    - Every paraphrased Biddulph claim attributes the idea to Biddulph by
      name (Requirement 3.3); no more than 30 consecutive verbatim words
      from *Raising Boys* anywhere (Requirement 3.4); contested or
      culturally-specific claims phrased as Biddulph's view, not universal
      fact (Requirement 3.5)
    - All strings are literal Python — no f-strings, no `.format()`, no
      shared text builders; only `make_intro_audio` consumes them
    - _Requirements: 3.1, 3.3, 3.4, 3.5, 5.6, 8.2, 8.3_

  - [x] 3.3 Hand-write Curriculum_A per-session reading passages and the whole-text reading
    - Session 1 reading `data.text` (220\u2013360 English words, design §D6
      "Naming the inner weather"): a parent attuning to a 4-year-old's
      meltdown without rushing to fix it; embed every Session-1
      `Vocab_Item` at least once (Property 10); mix simple, compound, and
      complex sentences; average sentence length in `[14, 22]` words
      (Property 9)
    - Session 2 reading `data.text` (220\u2013360 words, "The language
      explosion at four and five"): pretend play, narrating, the parent as
      co-author rather than corrector; embed every Session-2 `Vocab_Item`
    - Session 3 reading `data.text` (220\u2013360 words, "Big bodies, big
      feelings"): somatic regulation, why running and rolling are
      nervous-system tools, why physical affection still matters at this
      age; embed every Session-3 `Vocab_Item`
    - Session 5 whole-text reading `data.text` is the byte-exact
      `"\\n\\n".join` of the three per-session readings (Property 8) \u2014
      construct it in `build_content()` as `READING_S1 + "\\n\\n" + READING_S2
      + "\\n\\n" + READING_S3` rather than rewriting it
    - _Requirements: 3.1, 6.1, 6.2, 6.3, 6.4_

  - [x] 3.4 Hand-write Curriculum_A description, preview, and writing prompts
    - `title = "Raising Boys 4\u20135: The Last of the Tender Years"`
    - `description`: multi-paragraph English; first non-empty line is an
      ALL-CAPS headline of \u2265 6 chars using `TONE_A =
      "empathetic_observation"`; body names Steve Biddulph and *Raising
      Boys* at least once (Requirement 9.5, Property 19); names the
      Tender_Years_Stage framing in plain prose at least once
      (Requirement 1.4); contains \u2264 2 occurrences of any of
      `\\b(very|really|super|incredibly)\\b` total (Property 20); no
      ASCII-or-allowed-Unicode violations (Property 1)
    - `preview.text`: 60\u2013200 English words (Property 22); names the stage
      framing and the four-session journey
    - Two `writingSentence` activities in Session 4: each `data.items` array
      has 2 entries, each with `prompt` and `targetVocab`; each prompt
      references at least 2 distinct `Vocab_Item`s by name from the
      30-item curriculum vocab and asks the learner to apply a Biddulph
      idea to their own parenting situation (Requirement 7.4, Property 12)
    - One `writingParagraph` activity in Session 4: `data.instructions`
      contains a literal `"80 to 150 words"` (or `"80\u2013150 words"`) phrase
      (Property 13); `data.prompts` has \u2265 2 prompts, each English-only;
      `data.vocabList` lists the targeted items (\u2265 2)
    - _Requirements: 1.4, 7.1, 7.2, 7.3, 7.4, 7.5, 9.1, 9.2, 9.3, 9.5, 9.6_

  - [x] 3.5 Implement `build_content()` in `create_raising_boys_a_tender_years.py`
    - Assemble the full content dict via `raising_boys_helpers.make_*`
      helpers in the locked order (design §D4):
      Session 1 = `[introAudio_theme, introAudio_vocab, viewFlashcards,
      speakFlashcards, vocabLevel1, vocabLevel2, introAudio_grammar, reading,
      speakReading, readAlong]`; same shape for Sessions 2, 3
    - Session 4 = `[introAudio_review, viewFlashcards(all 30), vocabLevel1(all
      30), vocabLevel2(all 30), writingSentence_1, writingSentence_2,
      writingParagraph]`
    - Session 5 = `[introAudio_pre_reading, reading_whole, speakReading_whole,
      readAlong_whole, introAudio_farewell]` where the three reading-trio
      `data.text` values are byte-identical (Property 11)
    - Top-level fields: `title`, `description`, `preview`, `learningSessions`,
      `contentTypeTags = []`, `lengthTags = ["medium"]`,
      `skillFocusTags = ["balanced_skills"]`,
      `difficultyTags = ["advanced", "vocab_advanced", "reading_advanced",
      "writing_advanced"]`
    - Run `recursive_strip_keys(content, STRIP_KEYS)` and assert
      `recursive_find_keys(content, STRIP_KEYS) == []`
    - Call `validate_raising_boys.pre_upload_validate(content, "A")`; on
      failure, propagate the `ValidationError`
    - Module exposes `build_content()` so the orchestrator can import and
      call it; the script's `if __name__ == "__main__":` block additionally
      builds and POSTs to `/curriculum/create` for standalone debugging
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 4.1, 4.2, 4.3, 4.4, 4.5, 8.1,
      8.2, 8.3, 8.4, 8.5, 8.6, 10.1, 10.2, 11.2_

  - [x] 3.6 Run `pre_upload_validate` against Curriculum_A's content as a smoke check
    - Import `create_raising_boys_a_tender_years.build_content` in a tiny
      driver, build the content, run `pre_upload_validate(content, "A")`,
      and confirm no `ValidationError` is raised
    - _Requirements: 14.1, 14.2_

- [x] 4. Build Curriculum B — *Raising Boys 6\u20137: When the Father Years Switch On*
  - [x] 4.1 Author Curriculum_B vocabulary partition and session themes (literal Python lists / strings)
    - In `raising-boys-early-years-en-en/create_raising_boys_b_father_years.py`,
      define module-level constants:
      `VOCAB_S1 = ["identification", "role model", "mentor", "apprenticeship",
      "masculinity", "to emulate", "belonging", "aspirational", "presence",
      "to initiate"]`,
      `VOCAB_S2 = ["rough-and-tumble", "horseplay", "roughhousing",
      "boundary-setting", "playful resistance", "physicality", "restraint",
      "consensual", "to negotiate", "to wrestle"]`,
      `VOCAB_S3 = ["self-discipline", "delay of gratification", "competence",
      "autonomy", "accountability", "to internalise", "consequence",
      "disposition", "to step back", "to follow through"]`
    - All entries lowercase ASCII; multi-token and `to <verb>` entries
      allowed per design §"Vocab list lowercase rule"
    - Define the three per-session theme strings:
      Session 1 = `"Switching on: a boy looks toward his father"`,
      Session 2 = `"Rough-and-tumble: structured play and trust"`,
      Session 3 = `"Stepping back, stepping up: early self-discipline"`
    - Cross-curriculum check: zero overlap with Curriculum_A's 30-item set
      and zero overlap with the reference's 18-item beginner set (handled
      by Property 5 / Property 6 inside the validator; this task simply
      keeps the literal lists in the file)
    - _Requirements: 5.1, 5.2, 5.4, 5.5, 5.6_

  - [x] 4.2 Hand-write Curriculum_B intro audio scripts (English literal strings)
    - Theme, vocabulary, and grammar/usage `introAudio`s for Sessions 1, 2,
      3 (same word-count bands as Curriculum_A); vocabulary intros teach all
      10 session items with English definitions and English example
      sentences per item (Requirement 5.6)
    - Session 5 farewell `introAudio` (400\u2013600 words) using register
      `FAREWELL_REGISTER_B = "practical_momentum"` (design §D9), reviewing
      5\u20136 `Vocab_Item`s with FRESH English example sentences
    - Biddulph attributed by name in any script that paraphrases a book
      claim; \u2264 30 consecutive verbatim words; contested claims phrased as
      Biddulph's view (Requirements 3.2, 3.3, 3.4, 3.5)
    - _Requirements: 3.2, 3.3, 3.4, 3.5, 5.6, 8.2, 8.3_

  - [x] 4.3 Hand-write Curriculum_B per-session reading passages and the whole-text reading
    - Session 1 reading `data.text` (220\u2013360 words, "When the switch
      flips"): the six-year-old's new outward gaze toward his father or a
      male mentor; embed every Session-1 `Vocab_Item`
    - Session 2 reading `data.text` (220\u2013360 words, "Rough-and-tumble as
      language"): structured play as a way boys negotiate trust, restraint,
      and physicality; embed every Session-2 `Vocab_Item`
    - Session 3 reading `data.text` (220\u2013360 words, "When mum steps back
      without disappearing"): the start of self-discipline, delayed
      gratification, and follow-through; embed every Session-3 `Vocab_Item`
    - Session 5 whole-text reading is the byte-exact `"\\n\\n".join` of the
      three Curriculum_B per-session readings; constructed in
      `build_content()`
    - _Requirements: 3.2, 6.1, 6.2, 6.3, 6.4_

  - [x] 4.4 Hand-write Curriculum_B description, preview, and writing prompts
    - `title = "Raising Boys 6\u20137: When the Father Years Switch On"`
    - `description`: multi-paragraph English; first non-empty line is an
      ALL-CAPS headline of \u2265 6 chars using `TONE_B =
      "provocative_question"` (distinct from `TONE_A`); body names Steve
      Biddulph and *Raising Boys* at least once; names the Father_Years_Stage
      framing in plain prose at least once (Requirement 1.5); \u2264 2 vague
      intensifiers total
    - `preview.text`: 60\u2013200 English words; names the stage framing and
      the four-session journey
    - Two `writingSentence` and one `writingParagraph` in Session 4, each
      English-only, each referencing \u2265 2 `Vocab_Item`s by name and asking
      the learner to apply a Biddulph idea to their own parenting situation
      (Requirement 7.4); the `writingParagraph` `data.instructions` contains
      the literal `"80 to 150 words"` (or `"80\u2013150 words"`) phrase
      (Requirement 7.5, Property 13)
    - _Requirements: 1.5, 7.1, 7.2, 7.3, 7.4, 7.5, 9.1, 9.2, 9.3, 9.4, 9.5,
      9.6, 13.1_

  - [x] 4.5 Implement `build_content()` in `create_raising_boys_b_father_years.py`
    - Same wiring pattern as Task 3.5: assemble all 5 sessions in the locked
      activity order; set top-level
      `contentTypeTags = []`, `lengthTags = ["medium"]`,
      `skillFocusTags = ["balanced_skills"]`, and
      `difficultyTags = ["advanced", "vocab_advanced", "reading_advanced",
      "writing_advanced"]`
    - Run `recursive_strip_keys` then `recursive_find_keys` to confirm zero
      strip-keys remain
    - Call `validate_raising_boys.pre_upload_validate(content, "B")`
    - Module exposes `build_content()` for the orchestrator
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 4.1, 4.2, 4.3, 4.4, 4.5, 8.1,
      8.2, 8.3, 8.4, 8.5, 8.6, 10.1, 10.2, 11.2_

  - [x] 4.6 Run `pre_upload_validate` against Curriculum_B's content as a smoke check
    - Same pattern as Task 3.6 but for Curriculum_B
    - _Requirements: 14.1, 14.2_

- [x] 5. Checkpoint — review both curriculum content modules
  - Manually review every reading passage, intro audio script, description,
    preview, and writing prompt against the locked design constraints (design
    §D1\u2013D9). Ensure all property tests pass for both curriculums offline
    before invoking the API. Ensure all tests pass, ask the user if questions
    arise.

- [x] 6. Wire the orchestrator end-to-end
  - [x] 6.1 Implement duplicate checks against MCP postgres
    - In `orchestrate_raising_boys.py`, implement
      `duplicate_check_curriculum(title)` to query
      `SELECT id, uid, content->>'title' FROM curriculum
       WHERE language = 'en' AND user_language = 'en'
         AND content->>'title' = $title
         AND uid NOT LIKE '%\\_deleted' ESCAPE '\\'`
      and halt the run with a clear message if any row is returned
    - Implement `duplicate_check_series(title)` to query
      `SELECT id, title FROM curriculum_series WHERE title = $title`
      (with the same `_deleted`-suffix filter on whatever uid column the
      view exposes); on a non-deleted match, return the existing
      `seriesId` for reuse
    - These checks run BEFORE any `curriculum/create` or
      `curriculum-series/create` call (design §"API call sequence" step 1)
    - _Requirements: 11.3, 14.4_

  - [x] 6.2 Implement the optional series creation flow
    - Implement `create_or_reuse_series()`: if `HOST_SERIES_DECISION ==
      "create"`, call `duplicate_check_series(SERIES_TITLE)`; if a row
      exists, reuse `seriesId`, else POST `curriculum-series/create` with
      body `{firebaseIdToken, title=SERIES_TITLE, description=<\u2264 255 chars,
      metaphor_led tone>, isPublic=False}`
    - On 403 (UID not in SuperAuthGuard allowlist) or any non-2xx, set
      `seriesId = None` and proceed with `HOST_SERIES_DECISION = "skip"`
      semantics for the rest of the run; log the failure for the README
      (design §"API-call failure modes" + Requirement 12.4)
    - When `HOST_SERIES_DECISION == "skip"`, return `seriesId = None`
      without any API call
    - _Requirements: 12.1, 12.3, 12.4, 13.2_

  - [x] 6.3 Implement per-curriculum dispatch and `curriculum/create` POST
    - Implement `create_curriculum(label, module)`:
      `content = module.build_content()` then
      `content = recursive_strip_keys(content, STRIP_KEYS)` then
      `assert recursive_find_keys(content, STRIP_KEYS) == []` then
      `pre_upload_validate(content, label)` then
      `response = post_to_api("/curriculum/create",
        {firebaseIdToken, language=LANGUAGE, userLanguage=USER_LANGUAGE,
         content=json.dumps(content)})`; return `response["id"]`
    - In `run_pipeline()`, iterate `[("A",
      create_raising_boys_a_tender_years), ("B",
      create_raising_boys_b_father_years)]` and capture the two ids
    - On a 2xx response missing `"id"`, treat as failure and halt; do NOT
      delete any script (design §"API-call failure modes")
    - _Requirements: 11.2, 11.3_

  - [x] 6.4 Implement series-membership wiring (only when `seriesId is not None`)
    - For each `(label, curriculumId)` in `[("A", cur_a_id), ("B",
      cur_b_id)]` in display-order order, call
      `POST curriculum-series/addCurriculum
       {firebaseIdToken, curriculumSeriesId=seriesId, curriculumId}`
      then `POST curriculum/setDisplayOrder
       {firebaseIdToken, id=curriculumId, displayOrder=DISPLAY_ORDER_A or _B}`
    - On non-2xx, halt and surface endpoint + status + body; the
      curriculum row exists but is unattached / un-ordered \u2014 do NOT delete
      any script (design §"API-call failure modes")
    - _Requirements: 12.1, 12.3_

  - [x] 6.5 Implement post-upload validation aggregation
    - For each `(label, curriculumId)`, call
      `POST curriculum/getOne {id=curriculumId, uid=UID}` and pass the
      returned `content` (parse if string) into
      `post_upload_validate(returned_content, label)`
    - Print one line per curriculum: `"[<label>] post-upload PASS"` or
      `"[<label>] post-upload FAIL: Property <N> at <field-path>"`
    - If any post-upload check fails, set a flag preventing
      script-deletion and exit non-zero after printing all results (design
      §"Validator failure modes")
    - _Requirements: 14.3, 14.4_

  - [x] 6.6 Implement DB-state verification using the design's §"Verification SQL"
    - Implement `verify_db_state()` that runs the §14.1 locate-by-language-
      title query (must return exactly 2 non-deleted rows whose titles
      match `CURRICULUM_A_TITLE` and `CURRICULUM_B_TITLE`) and the §14.2
      shape query (must return 2 rows with `has_advanced = true` and
      `content_type_tags_kind = 'array'`) via MCP postgres
    - When `seriesId is not None`, additionally run the §"series wiring"
      query and assert both new ids appear under the new series with
      display orders 1 and 2
    - When `HOST_SERIES_DECISION == "skip"`, assert the §"series wiring"
      query returns zero rows for the locked series title (Property 25
      degenerate case)
    - On `< 2` rows for the title query, treat as failure (Requirement
      14.4) \u2014 do NOT delete any script and exit non-zero; on `> 2` rows,
      halt and surface the orphan ids for manual `curriculum/delete`
    - _Requirements: 14.1, 14.2, 14.3, 14.4_

- [x] 7. Execute the pipeline against the API and the database
  - [x] 7.1 Run `python orchestrate_raising_boys.py` from the
        `raising-boys-early-years-en-en/` working folder
    - Confirms Firebase auth succeeds for `UID =
      "zs5AMpVfqkcfDf8CJ9qrXdH58d73"`, both pre-flight duplicate checks pass,
      both `curriculum/create` calls return 2xx with an `id`, the optional
      series creation completes (or gracefully degrades to
      `seriesId = None`), and both `curriculum/setDisplayOrder` calls return
      2xx (when applicable)
    - _Requirements: 11.2, 11.3_

  - [x] 7.2 Run the design's §"Verification SQL" via MCP postgres and confirm pass
    - Execute the §14.1 locate query, the §14.2 shape query, the §14
      duplicate-check query (must return zero rows), and the §"series
      wiring" query (when `seriesId is not None`) directly via MCP postgres
    - Compare results to the design's pass criteria; abort cleanup on any
      mismatch
    - _Requirements: 14.1, 14.2, 14.3, 14.4_

  - [x] 7.3 Run cross-curriculum vocabulary uniqueness check
    - Combine the published `vocabList`s of all `viewFlashcards` activities
      for both curriculums (via `curriculum/getOne` or the persisted
      content); assert the union has exactly 60 distinct case-folded
      entries with zero pairwise overlap between Curriculum_A's 30-item set
      and Curriculum_B's 30-item set (design §D5 closing paragraph)
    - _Requirements: 5.1, 5.5_

- [x] 8. Checkpoint — confirm DB state matches the locked design
  - Ensure all property checks (offline + DB) pass and that both new rows
    have `language = 'en'`, `user_language = 'en'`, `is_public = false`,
    `uid NOT LIKE '%_deleted'`, `difficultyTags @> '["advanced"]'::jsonb`,
    `jsonb_typeof(content->'contentTypeTags') = 'array'`. Ensure all tests
    pass, ask the user if questions arise.

- [x] 9. Documentation and gated cleanup
  - [x] 9.1 Create `raising-boys-early-years-en-en/README.md`
    - Sections (all non-empty): (a) both curriculum IDs and titles; (b)
      optional `seriesId` and `seriesTitle` (or "no series created" when
      `HOST_SERIES_DECISION == "skip"`); (c) display orders for A and B;
      (d) the two 30-item vocabulary partitions copied verbatim from
      design §D5 (organised by session); (e) description tone
      assignments (`empathetic_observation` for A, `provocative_question`
      for B, `metaphor_led` for the optional series); (f) farewell
      register assignments (`introspective_guide` for A,
      `practical_momentum` for B); (g) creation method summary (the run
      pipeline); (h) the four §"Verification SQL" queries from the
      design; (i) recreation context (`UID`, language pair, locked
      design pointers, command to re-author scripts via
      `curriculum/getOne`)
    - _Requirements: 11.4, 14.3_

  - [x] 9.2 Delete the five run scripts ONLY AFTER Task 7.2 has confirmed both rows in the DB
    - Delete `create_raising_boys_a_tender_years.py`,
      `create_raising_boys_b_father_years.py`, `raising_boys_helpers.py`,
      `validate_raising_boys.py`, `orchestrate_raising_boys.py` (last)
    - If DB verification did NOT return exactly 2 rows, leave EVERY script
      on disk and skip this task entirely; the spec forbids deleting any
      `create_*.py` script before the corresponding curriculum row is
      confirmed present and non-deleted in PostgreSQL (Requirements 11.4,
      11.5; product steering "Script Lifecycle — NEVER Delete Before
      Execution")
    - _Requirements: 11.4, 11.5_

- [x] 10. Final checkpoint — both curriculums verified, scripts cleaned up
  - Ensure both DB rows are present, the README is complete, and all five
    scripts have been deleted (only on success). Ensure all tests pass, ask
    the user if questions arise.

## Notes

- Tasks marked with `*` are optional and can be skipped for a faster MVP run;
  property tests live behind `*` per the workflow's optional-task-marking
  rule. Validator scaffolding (Task 1.4) and validator wiring (Task 2.31)
  are NOT optional — they are the integration glue that the property tests
  plug into.
- Each task references specific requirement clauses (granular sub-clauses
  where relevant) for traceability.
- All learner-facing prose is hand-written as literal Python string
  constants; no `f`-strings, no `.format()`, no `string.Template`, no shared
  text builders anywhere across the five scripts (design §"Inputs and
  source", §"Architecture", and `CURRICULUM_QUALITY_STANDARDS.md` "No
  Templated Content Generation").
- Locked design decisions (titles, vocabulary partitions, tones, farewell
  registers, display orders, host-series decision) live as module-level
  constants in the orchestrator and are mirrored as literal values in the
  per-curriculum scripts; any divergence is caught by the property tests.
- Scripts MUST run successfully against the API and the DB MUST confirm
  both curriculums via the design's §"Verification SQL" BEFORE any cleanup
  deletion (Requirement 11.4, Requirement 11.5; product steering "Script
  Lifecycle — NEVER Delete Before Execution"). The orchestrator's
  cleanup gate enforces this.
- `setPublic` is never called and is statically forbidden in any script
  (Property 24, Requirement 11.1); collection `setDisplayOrder` is never
  called and is statically forbidden in any script (Property 27,
  Requirement 12.5).
- The pre-upload validator runs Properties 1\u201323 and 30b; the post-upload
  validator runs the same set EXCEPT Property 2 (strip-keys absence) since
  the platform legitimately adds generated keys after creation. Properties
  24, 25, 26, 27, 28 are static-analysis or cross-batch checks run by the
  orchestrator; Properties 29 and 30 are DB queries embedded in
  `verify_db_state()`.

## Task Dependency Graph

```json
{
  "waves": [
    { "id": 0, "tasks": ["1.1"] },
    { "id": 1, "tasks": ["1.2"] },
    { "id": 2, "tasks": ["1.3", "1.4", "1.5"] },
    { "id": 3, "tasks": ["2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7", "2.8", "2.9", "2.10", "2.11", "2.12", "2.13", "2.14", "2.15", "2.16", "2.17", "2.18", "2.19", "2.20", "2.21", "2.22", "2.23", "2.24", "2.25", "2.26", "2.27", "2.28", "2.29", "2.30"] },
    { "id": 4, "tasks": ["2.31", "3.1", "4.1"] },
    { "id": 5, "tasks": ["3.2", "3.3", "3.4", "4.2", "4.3", "4.4"] },
    { "id": 6, "tasks": ["3.5", "4.5"] },
    { "id": 7, "tasks": ["3.6", "4.6"] },
    { "id": 8, "tasks": ["6.1"] },
    { "id": 9, "tasks": ["6.2", "6.3"] },
    { "id": 10, "tasks": ["6.4", "6.5"] },
    { "id": 11, "tasks": ["6.6"] },
    { "id": 12, "tasks": ["7.1"] },
    { "id": 13, "tasks": ["7.2"] },
    { "id": 14, "tasks": ["7.3"] },
    { "id": 15, "tasks": ["9.1"] },
    { "id": 16, "tasks": ["9.2"] }
  ]
}
```
