# Implementation Plan: Effective Learning Curriculum

## Overview

Create 10 standalone Python scripts (5 learning science topics × 2 language pairs: en-en, vi-en), each producing a curriculum via the helloapi REST API. Then create 2 orchestrator scripts to organize the 10 new curriculums + 2 existing "Get Comfortable Being Uncomfortable" curriculums into 2 collections. Each curriculum script contains ~800+ lines of hand-written content with `build_content()`, `validate()`, `strip_keys()`, and `create()` functions. All scripts live in `effective-learning-curriculum/`, are run once, verified, then deleted — leaving only a README.

## Tasks

- [x] 1. Create en-en Grit podcast curriculum
  - [x] 1.1 Write `effective-learning-curriculum/create_en_en_grit.py`
    - Hand-write complete curriculum content for Angela Duckworth's "Grit" TED Talk (en-en, podcast)
    - 18 English vocabulary words in 3 groups of 6, drawn from the TED Talk
    - 5 sessions with activity counts [12, 12, 12, 4, 5] following exact activity type sequences
    - Include `youtubeUrl: "https://www.youtube.com/watch?v=H14bBuluwB8"` and `contentTypeTags: ["podcast"]`
    - Set `language: "en"`, `userLanguage: "en"` as top-level API body params
    - All user-facing text in English: persuasive description (bold_declaration tone), preview (~150 words), introAudio scripts (500-800 words for vocab teaching), reading passages inspired by the TED Talk, writing prompts, farewell (warm accountability tone)
    - Implement `build_content()`, `validate()`, `strip_keys()`, `create()` functions
    - `validate()` must check all 12 correctness properties applicable to a single curriculum (Properties 1-8)
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 14.1, 14.2, 14.3, 14.4, 15.1-15.7, 16.1-16.6, 17.1, 18.1, 19.1, 19.2, 20.1, 20.2, 20.3_

  - [x] 1.2 Run `create_en_en_grit.py` and verify curriculum exists in DB
    - Execute the script, collect the curriculum ID
    - Check for duplicates by title + uid
    - _Requirements: 1.6, 1.7, 21.1, 21.2_

- [x] 2. Create vi-en Grit podcast curriculum
  - [x] 2.1 Write `effective-learning-curriculum/create_vi_en_grit.py`
    - Hand-write complete curriculum content for Angela Duckworth's "Grit" TED Talk (vi-en, podcast)
    - Same 18 English vocabulary words as en-en Grit (Property 10: vocab parity)
    - 5 sessions with activity counts [12, 12, 12, 4, 5] following exact activity type sequences
    - Include `youtubeUrl: "https://www.youtube.com/watch?v=H14bBuluwB8"` and `contentTypeTags: ["podcast"]`
    - Set `language: "en"`, `userLanguage: "vi"` as top-level API body params
    - Vietnamese for user-facing text (titles, descriptions, preview, introAudio, writing prompts), English for reading passages and vocab words
    - Persuasive description (vivid_scenario tone), farewell (team-building energy tone)
    - NOT a translation of en-en — written from scratch for Vietnamese audience
    - Implement `build_content()`, `validate()`, `strip_keys()`, `create()` functions
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 14.1-14.4, 15.1-15.7, 16.1-16.6, 17.1, 18.1, 19.1, 19.2, 20.1-20.4, 22.4_

  - [x] 2.2 Run `create_vi_en_grit.py` and verify curriculum exists in DB
    - Execute the script, collect the curriculum ID
    - Check for duplicates by title + uid
    - _Requirements: 2.6, 2.7, 21.1, 21.2_

- [x] 3. Create en-en Growth Mindset concept curriculum
  - [x] 3.1 Write `effective-learning-curriculum/create_en_en_growth_mindset.py`
    - Hand-write complete curriculum content for Carol Dweck's Growth Mindset (en-en, concept)
    - 18 English vocabulary words in 3 groups of 6, related to Growth Mindset
    - 5 sessions with activity counts [12, 12, 12, 4, 5] following exact activity type sequences
    - Include `contentTypeTags: []` (empty array), NO `youtubeUrl` field
    - Set `language: "en"`, `userLanguage: "en"` as top-level API body params
    - All user-facing text in English: persuasive description (provocative_question tone), original educational reading passages, farewell (introspective guide tone)
    - Implement `build_content()`, `validate()`, `strip_keys()`, `create()` functions
    - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 14.1-14.4, 15.1-15.7, 16.1-16.6, 17.1, 18.1, 19.1, 19.2, 20.1-20.3_

  - [x] 3.2 Run `create_en_en_growth_mindset.py` and verify curriculum exists in DB
    - Execute the script, collect the curriculum ID
    - Check for duplicates by title + uid
    - _Requirements: 3.4, 3.5, 21.1, 21.2_

- [x] 4. Create vi-en Growth Mindset concept curriculum
  - [x] 4.1 Write `effective-learning-curriculum/create_vi_en_growth_mindset.py`
    - Hand-write complete curriculum content for Carol Dweck's Growth Mindset (vi-en, concept)
    - Same 18 English vocabulary words as en-en Growth Mindset (Property 10: vocab parity)
    - 5 sessions with activity counts [12, 12, 12, 4, 5] following exact activity type sequences
    - Include `contentTypeTags: []` (empty array), NO `youtubeUrl` field
    - Set `language: "en"`, `userLanguage: "vi"` as top-level API body params
    - Vietnamese for user-facing text, English for reading passages and vocab words
    - Persuasive description (empathetic_observation tone), farewell (warm accountability tone)
    - NOT a translation of en-en — written from scratch for Vietnamese audience
    - _Requirements: 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 14.1-14.4, 15.1-15.7, 16.1-16.6, 17.1, 18.1, 19.1, 19.2, 20.1-20.4, 22.4_

  - [x] 4.2 Run `create_vi_en_growth_mindset.py` and verify curriculum exists in DB
    - Execute the script, collect the curriculum ID
    - Check for duplicates by title + uid
    - _Requirements: 4.4, 4.5, 21.1, 21.2_

- [x] 5. Checkpoint — Grit and Growth Mindset curriculums verified
  - Ensure all 4 curriculums (en-en Grit, vi-en Grit, en-en Growth Mindset, vi-en Growth Mindset) exist in DB with correct structure, ask the user if questions arise.

- [x] 6. Create en-en Desirable Difficulties concept curriculum
  - [x] 6.1 Write `effective-learning-curriculum/create_en_en_desirable_difficulties.py`
    - Hand-write complete curriculum content for Robert Bjork's Desirable Difficulties (en-en, concept)
    - 18 English vocabulary words in 3 groups of 6, related to Desirable Difficulties
    - 5 sessions with activity counts [12, 12, 12, 4, 5] following exact activity type sequences
    - Include `contentTypeTags: []` (empty array), NO `youtubeUrl` field
    - Set `language: "en"`, `userLanguage: "en"` as top-level API body params
    - Persuasive description (surprising_fact tone), farewell (practical momentum tone)
    - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 14.1-14.4, 15.1-15.7, 16.1-16.6, 17.1, 18.1, 19.1, 19.2, 20.1-20.3_

  - [x] 6.2 Run `create_en_en_desirable_difficulties.py` and verify curriculum exists in DB
    - Execute the script, collect the curriculum ID
    - Check for duplicates by title + uid
    - _Requirements: 5.4, 5.5, 21.1, 21.2_

- [x] 7. Create vi-en Desirable Difficulties concept curriculum
  - [x] 7.1 Write `effective-learning-curriculum/create_vi_en_desirable_difficulties.py`
    - Hand-write complete curriculum content for Robert Bjork's Desirable Difficulties (vi-en, concept)
    - Same 18 English vocabulary words as en-en Desirable Difficulties (Property 10: vocab parity)
    - 5 sessions with activity counts [12, 12, 12, 4, 5] following exact activity type sequences
    - Include `contentTypeTags: []` (empty array), NO `youtubeUrl` field
    - Set `language: "en"`, `userLanguage: "vi"` as top-level API body params
    - Persuasive description (bold_declaration tone), farewell (quiet awe tone)
    - NOT a translation of en-en — written from scratch for Vietnamese audience
    - _Requirements: 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 14.1-14.4, 15.1-15.7, 16.1-16.6, 17.1, 18.1, 19.1, 19.2, 20.1-20.4, 22.4_

  - [x] 7.2 Run `create_vi_en_desirable_difficulties.py` and verify curriculum exists in DB
    - Execute the script, collect the curriculum ID
    - Check for duplicates by title + uid
    - _Requirements: 6.4, 6.5, 21.1, 21.2_

- [x] 8. Create en-en Productive Struggle concept curriculum
  - [x] 8.1 Write `effective-learning-curriculum/create_en_en_productive_struggle.py`
    - Hand-write complete curriculum content for Manu Kapur's Productive Struggle (en-en, concept)
    - 18 English vocabulary words in 3 groups of 6, related to Productive Struggle
    - 5 sessions with activity counts [12, 12, 12, 4, 5] following exact activity type sequences
    - Include `contentTypeTags: []` (empty array), NO `youtubeUrl` field
    - Set `language: "en"`, `userLanguage: "en"` as top-level API body params
    - Persuasive description (vivid_scenario tone), farewell (team-building energy tone)
    - _Requirements: 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 14.1-14.4, 15.1-15.7, 16.1-16.6, 17.1, 18.1, 19.1, 19.2, 20.1-20.3_

  - [x] 8.2 Run `create_en_en_productive_struggle.py` and verify curriculum exists in DB
    - Execute the script, collect the curriculum ID
    - Check for duplicates by title + uid
    - _Requirements: 7.4, 7.5, 21.1, 21.2_

- [x] 9. Create vi-en Productive Struggle concept curriculum
  - [x] 9.1 Write `effective-learning-curriculum/create_vi_en_productive_struggle.py`
    - Hand-write complete curriculum content for Manu Kapur's Productive Struggle (vi-en, concept)
    - Same 18 English vocabulary words as en-en Productive Struggle (Property 10: vocab parity)
    - 5 sessions with activity counts [12, 12, 12, 4, 5] following exact activity type sequences
    - Include `contentTypeTags: []` (empty array), NO `youtubeUrl` field
    - Set `language: "en"`, `userLanguage: "vi"` as top-level API body params
    - Persuasive description (metaphor_led tone), farewell (introspective guide tone)
    - NOT a translation of en-en — written from scratch for Vietnamese audience
    - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 14.1-14.4, 15.1-15.7, 16.1-16.6, 17.1, 18.1, 19.1, 19.2, 20.1-20.4, 22.4_

  - [x] 9.2 Run `create_vi_en_productive_struggle.py` and verify curriculum exists in DB
    - Execute the script, collect the curriculum ID
    - Check for duplicates by title + uid
    - _Requirements: 8.4, 8.5, 21.1, 21.2_

- [x] 10. Checkpoint — Desirable Difficulties and Productive Struggle verified
  - Ensure all 4 curriculums exist in DB with correct structure, ask the user if questions arise.

- [x] 11. Create en-en ZPD concept curriculum
  - [x] 11.1 Write `effective-learning-curriculum/create_en_en_zpd.py`
    - Hand-write complete curriculum content for Vygotsky's Zone of Proximal Development (en-en, concept)
    - 18 English vocabulary words in 3 groups of 6, related to ZPD
    - 5 sessions with activity counts [12, 12, 12, 4, 5] following exact activity type sequences
    - Include `contentTypeTags: []` (empty array), NO `youtubeUrl` field
    - Set `language: "en"`, `userLanguage: "en"` as top-level API body params
    - Persuasive description (metaphor_led tone), farewell (quiet awe tone)
    - _Requirements: 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 14.1-14.4, 15.1-15.7, 16.1-16.6, 17.1, 18.1, 19.1, 19.2, 20.1-20.3_

  - [x] 11.2 Run `create_en_en_zpd.py` and verify curriculum exists in DB
    - Execute the script, collect the curriculum ID
    - Check for duplicates by title + uid
    - _Requirements: 9.4, 9.5, 21.1, 21.2_

- [x] 12. Create vi-en ZPD concept curriculum
  - [x] 12.1 Write `effective-learning-curriculum/create_vi_en_zpd.py`
    - Hand-write complete curriculum content for Vygotsky's Zone of Proximal Development (vi-en, concept)
    - Same 18 English vocabulary words as en-en ZPD (Property 10: vocab parity)
    - 5 sessions with activity counts [12, 12, 12, 4, 5] following exact activity type sequences
    - Include `contentTypeTags: []` (empty array), NO `youtubeUrl` field
    - Set `language: "en"`, `userLanguage: "vi"` as top-level API body params
    - Persuasive description (surprising_fact tone), farewell (practical momentum tone)
    - NOT a translation of en-en — written from scratch for Vietnamese audience
    - _Requirements: 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 14.1-14.4, 15.1-15.7, 16.1-16.6, 17.1, 18.1, 19.1, 19.2, 20.1-20.4, 22.4_

  - [x] 12.2 Run `create_vi_en_zpd.py` and verify curriculum exists in DB
    - Execute the script, collect the curriculum ID
    - Check for duplicates by title + uid
    - _Requirements: 10.4, 10.5, 21.1, 21.2_

- [x] 13. Checkpoint — All 10 curriculums verified
  - Ensure all 10 curriculums exist in DB with correct structure
  - Verify vocabulary parity: each en-en/vi-en pair shares the same 18 English words (Property 10)
  - Verify no vocabulary reuse within the en-en set or within the vi-en set (Property 9)
  - Ask the user if questions arise.

- [x] 14. Create en-en collection orchestrator and run it
  - [x] 14.1 Write `effective-learning-curriculum/create_en_en_collection.py`
    - Create collection "How to Learn Effectively" with short informative description (not persuasive copy)
    - Add 6 curriculums to collection via `curriculum-collection/addCurriculum`:
      - display_order 0: Growth Mindset (en-en)
      - display_order 1: Get Comfortable Being Uncomfortable (existing: `VdgEbnzAassbpRPa`)
      - display_order 2: Desirable Difficulties (en-en)
      - display_order 3: Productive Struggle (en-en)
      - display_order 4: Zone of Proximal Development (en-en)
      - display_order 5: Grit (en-en)
    - Set collection `display_order: -999` via `curriculum-collection/setDisplayOrder`
    - Cross-list en-en Grit to existing podcast collection `mqdqxuyp` via `curriculum-collection/addCurriculum`, set display_order 4 on the curriculum
    - _Requirements: 11.1, 11.2, 11.3, 11.4, 11.5, 11.6, 13.1, 13.2_

  - [x] 14.2 Run `create_en_en_collection.py` and verify collection in DB
    - Execute the script, collect the collection ID
    - Verify 6 curriculums in collection with correct display orders
    - Verify Grit appears in podcast collection `mqdqxuyp` at display_order 4
    - Verify collection display_order is -999
    - _Requirements: 11.2, 11.3, 11.4, 13.1, 13.2_

- [x] 15. Create vi-en collection orchestrator and run it
  - [x] 15.1 Write `effective-learning-curriculum/create_vi_en_collection.py`
    - Create collection "Học Cách Học Hiệu Quả" with short informative description in Vietnamese (not persuasive copy)
    - Add 6 curriculums to collection via `curriculum-collection/addCurriculum`:
      - display_order 0: Growth Mindset (vi-en)
      - display_order 1: Bước Ra Khỏi Vùng An Toàn (existing: `2hcxuPuBD1g1F3Zk`)
      - display_order 2: Desirable Difficulties (vi-en)
      - display_order 3: Productive Struggle (vi-en)
      - display_order 4: Zone of Proximal Development (vi-en)
      - display_order 5: Grit (vi-en)
    - Set collection `display_order: -999` via `curriculum-collection/setDisplayOrder`
    - Cross-list vi-en Grit to existing podcast collection `1pspi6gt` via `curriculum-collection/addCurriculum`, set display_order to next available position
    - _Requirements: 12.1, 12.2, 12.3, 12.4, 12.5, 12.6, 13.3, 13.4_

  - [x] 15.2 Run `create_vi_en_collection.py` and verify collection in DB
    - Execute the script, collect the collection ID
    - Verify 6 curriculums in collection with correct display orders
    - Verify Grit appears in podcast collection `1pspi6gt`
    - Verify collection display_order is -999
    - _Requirements: 12.2, 12.3, 12.4, 13.3, 13.4_

- [x] 16. Checkpoint — Both collections verified
  - Ensure both collections exist with 6 curriculums each (Property 11)
  - Verify collection display orders are -999
  - Verify Grit cross-listings to podcast collections
  - Verify tone variety: no adjacent curriculums in same collection share description tone or farewell tone (Property 12)
  - Ask the user if questions arise.

- [x] 17. Final verification and cleanup
  - [x] 17.1 Run comprehensive verification queries
    - Verify all 10 curriculums exist with correct structure, language settings, and content type tags
    - Verify both collections have exactly 6 members each with correct display orders
    - Verify Grit cross-listings in podcast collections
    - Check for duplicates across all 10 curriculums by title + uid
    - Verify no vocabulary reuse within each collection (Property 9)
    - Verify vocab parity across en-en/vi-en pairs (Property 10)
    - _Requirements: 11.2, 11.6, 12.2, 12.6, 13.1-13.4, 21.1, 21.2, 22.1, 22.2, 22.4_

  - [x] 17.2 Delete all creation scripts and write README
    - Delete all 12 `.py` files from `effective-learning-curriculum/`
    - Create `effective-learning-curriculum/README.md` with: creation method, all 10 curriculum IDs, both collection IDs, display order layout, SQL queries to find content in DB, recreation context
    - _Requirements: 19.3, 19.4_

- [x] 18. Final checkpoint — Effective Learning Curriculum complete
  - Ensure all 10 curriculums and 2 collections exist, all scripts deleted, README created, ask the user if questions arise.

## Notes

- Each curriculum script is ~800+ lines of hand-written content — no templated generation
- The en-en and vi-en versions of each topic share the same 18 English vocabulary words but all user-facing text is written independently
- Vocabulary must be distinct across all 5 topics within each collection (90 unique words per collection)
- Tone assignments are specified in the design document's Tone Assignments table
- All curriculums are created private (`is_public: false`) — no `setPublic` calls
- Scripts are deleted after verification, leaving only the README
- The 2 existing "Get Comfortable Being Uncomfortable" curriculums are added to collections but NOT modified
