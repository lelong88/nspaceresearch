# Implementation Plan: Vietnamese-English Digital Economy Curriculums

## Overview

Create 10 English-learning curriculums for Vietnamese speakers (`userLanguage="vi"`, `language="en"`) on the Digital Economy theme, organized as 1 collection × 3 series × 10 curriculums. Skill-focus distribution: 3 story-reading, 3 speaking, 4 balanced. Difficulty: 5 preintermediate + 5 intermediate. All curriculums have 4 sessions, 20 unique vocab words (5 per session), are priced at 49 credits, and stay private.

Scripts go in `vi-en-digital-economy-curriculums/`. Reuses root-level `api_helpers.py` and `firebase_token.py`. The directory contains a format-aware validator (`validate_content.py`), property-based tests (`test_validate_content.py`), an orchestrator, and 10 standalone curriculum-creation scripts.

Phased execution per Requirement 16: (Phase 0) shared validator + PBT tests, (Phase 1) orchestrator wiring collection + 3 series, (Phase 2) 3 story-reading scripts, (Phase 3) 3 speaking scripts, (Phase 4) 4 balanced scripts, (Phase 5) integration verification + content audits, (Phase 6) README + script cleanup.

Implementation language: **Python 3** (per design — `validate_content.py`, `orchestrator.py`, and `create_*.py` scripts).

## Tasks

- [x] 1. Phase 0 — Setup directory and shared modules
  - [x] 1.1 Create `vi-en-digital-economy-curriculums/validate_content.py` with the format-aware `validate(content, fmt, level=None)` function
    - Expose constants: `STRIP_KEYS`, `VALID_ACTIVITY_TYPES`, `ACTIVITY_TEMPLATES`, `CONTENT_TYPE_TAGS` (per design Section "2. validate_content.py")
    - `fmt` argument accepts `"story_reading"`, `"speaking"`, `"balanced"`; `level` accepts `"preintermediate"`, `"intermediate"`, or `None` (skip Property 12 check)
    - Check 1: `content` is a dict (corruption rules §1)
    - Check 2-4: `title`, `description`, `preview.text` are non-empty strings (1-255 char bounds where defined)
    - Check 5: `contentTypeTags == CONTENT_TYPE_TAGS[fmt]` exactly (`["story"]` for story_reading, `[]` for speaking/balanced)
    - Check 6: `learningSessions` is a list of exactly 4 elements
    - Check 7: each session has non-empty `title` (5-150 chars), unique across the curriculum, and non-empty `activities` list
    - Check 8: activity-type sequence in each session matches `ACTIVITY_TEMPLATES[fmt][i]` exactly (raise with session index, expected, actual)
    - Check 9: each activity has `activityType`, `title` (1-255 chars), `description` (1-255 chars), `data` (dict); reject `type` field; activityType in `VALID_ACTIVITY_TYPES`
    - Check 10: activity `title`/`description` follow per-type conventions in Req 9.8 (Flashcards/Đọc/Nghe/Viết prefixes; reading description = first 80 chars of `data.text`; introAudio title 5-60 chars)
    - Check 11: `vocabList` is array of lowercase strings (1-64 chars each, 1-20 items); never named `words`
    - Check 12: in any session, viewFlashcards / speakFlashcards / vocabLevel1 share an identical `data.vocabList` (same order)
    - Check 13: each Session_Vocab_Group has exactly 5 unique words
    - Check 14: union of 4 Session_Vocab_Groups has exactly 20 unique words
    - Check 15: `reading`/`speakReading`/`readAlong` activities have non-empty `data.text`
    - Check 16: `writingSentence` has `data.vocabList`, `data.items` (1-10), each item has non-empty `prompt` (1-500) and `targetVocab` (1-64) where `targetVocab ∈ data.vocabList`
    - Check 17: `writingParagraph` has `data.vocabList`, `data.instructions` (1-1000), `data.prompts` (2-10 non-empty strings, each 1-500)
    - Check 18: recursive scan rejects any `STRIP_KEYS` element anywhere in dicts/lists (raise naming the offending key)
    - Check 19: introAudio whitespace-token counts: welcome (first introAudio of session 1) in 500-800; mid-session wrap-ups/recaps (last introAudio of sessions 1-3, first introAudio of sessions 2-3) in 200-400; farewell (last introAudio of session 4) in 400-600
    - Check 20: when `level` is provided, average sentence length across union of all `reading` + `speakReading` `data.text` is within 10-14 (preintermediate) or 12-18 (intermediate)
    - Raise `ValueError` with rule name, JSON path (e.g., `learningSessions[1].activities[3].data.vocabList`), and expected vs actual values
    - _Requirements: 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 10.9, 10.10, 10.11, 10.12, 10.13_

  - [x] 1.2 Create `vi-en-digital-economy-curriculums/test_validate_content.py` with property-based tests using Hypothesis
    - Use `@settings(max_examples=100)` minimum
    - Generator strategies (per design "Testing Strategy"): `valid_curriculum(fmt, level)`, `random_activity(activity_type)`, `random_vocab_list(n)`, `random_strip_key()`, `random_json_path()`, `random_format()`, `random_level()`, `controlled_passage(target_avg_sentence_length, n_sentences)`, `controlled_intro_audio(word_count)`
    - Tag each test with `# Feature: vi-en-digital-economy-curriculums, Property N: <text>`
    - **Property 1: Valid content passes validation** — Validates: Requirements 1.4, 1.5, 1.6, 3.1, 3.2, 3.3, 3.4, 5.1, 9.1-9.9, 10.1-10.13
    - **Property 2: contentTypeTags must match the declared format** — Validates: Requirements 1.5, 1.6, 10.12
    - **Property 3: Strip keys are rejected anywhere in the JSON tree** — Validates: Requirements 1.7, 10.11
    - **Property 4: Activity sequence must match the format template** — Validates: Requirements 3.1, 3.2, 3.3, 3.7, 3.8, 10.2
    - **Property 5: Curriculum must have exactly 4 sessions, each well-shaped** — Validates: Requirements 3.4, 9.9, 10.2
    - **Property 6: Session_Vocab_Group structure (5 per session, 20 unique total)** — Validates: Requirements 3.5, 5.1, 10.7, 10.8
    - **Property 7: Activity structural shape** — Validates: Requirements 9.1, 9.2, 9.5, 10.3, 10.4
    - **Property 8: vocabList format** — Validates: Requirements 5.5, 9.3, 10.5
    - **Property 9: Flashcard / vocabLevel vocabList consistency within a session** — Validates: Requirements 9.4, 10.6
    - **Property 10: writingSentence shape** — Validates: Requirements 9.6, 10.9
    - **Property 11: writingParagraph shape** — Validates: Requirements 9.7, 10.10
    - **Property 12: Reading passage average sentence length matches level** — Validates: Requirement 2.4
    - **Property 13: introAudio word counts match script role** — Validates: Requirements 8.1, 8.3, 8.4
    - **Property 14: Activity title/description conventions** — Validates: Requirement 9.8
    - **Property 15: Top-level structural fields** — Validates: Requirements 10.1, 10.13
    - _Requirements: 9.1-9.9, 10.1-10.13_

  - [x] 1.3 Add design-time table validation tests in `test_validate_content.py` (or companion `test_design_tables.py`)
    - Vocabulary distinctness audit: pairwise overlap ≤ 2 across all 10 designed vocabLists; max single-word frequency ≤ 2 across all 200 words
    - Description tone distribution: per series, no adjacent equality; max tone count ≤ 3 across the 10 curriculums
    - Farewell register distribution: per series, no adjacent equality; each register count in [1, 3]
    - Series description tones: all 3 distinct
    - Curriculum titles: 2-8 words, ≤50 chars, no forbidden level substrings, no duplicates across the 10
    - Subtopic-noun coverage: each title contains at least one subtopic noun or vocab word
    - _Requirements: 2.3, 6.5, 6.6, 7.1, 7.3, 7.4, 7.5, 8.8, 8.9, 13.7_

- [x] 2. Phase 1 — Create orchestrator and wire infrastructure
  - [x] 2.1 Create `vi-en-digital-economy-curriculums/orchestrator.py`
    - Create 1 collection: title `"Học Tiếng Anh Qua Kinh Tế Số"`; neutral informative Vietnamese description summarizing the digital-economy theme and the 10 curriculums spanning preintermediate to intermediate; do NOT set collection `displayOrder`
    - Create 3 series:
      - Series 1: `"Câu Chuyện Kinh Tế Số"` (story-reading) — description tone `vivid_scenario`, ≤255 chars
      - Series 2: `"Nói Chuyện Kinh Tế Số"` (speaking) — description tone `empathetic_observation`, ≤255 chars
      - Series 3: `"Khám Phá Kinh Tế Số"` (balanced) — description tone `bold_declaration`, ≤255 chars
    - Wire all 3 series to the collection via `addSeriesToCollection`
    - Set series display orders: Series 1 → 1, Series 2 → 2, Series 3 → 3
    - Print `collection_id` and the 3 `series_ids` to stdout for use in per-curriculum scripts
    - Use `api_helpers.create_collection`, `api_helpers.create_series`, `api_helpers.add_series_to_collection`, `api_helpers.set_series_display_order` (root-level imports via `sys.path.insert`)
    - _Requirements: 13.1, 13.2, 13.3, 13.4, 13.7, 13.10, 14.1, 14.2, 14.3, 14.4, 14.5_

  - [x] 2.2 Run orchestrator and capture identifiers
    - Execute `python orchestrator.py` from `vi-en-digital-economy-curriculums/`
    - Record returned `collection_id` and 3 `series_ids` for paste-in to per-curriculum scripts
    - Verify in DB: 1 collection exists with the expected title; 3 series exist with display orders 1, 2, 3 within the collection
    - _Requirements: 13.1, 13.2, 13.3, 13.4_

- [x] 3. Checkpoint — Phase 0 + Phase 1 complete
  - Verify `validate_content.py` exists, exports `validate`, `STRIP_KEYS`, `VALID_ACTIVITY_TYPES`, `ACTIVITY_TEMPLATES`, `CONTENT_TYPE_TAGS`
  - Run `python -m pytest vi-en-digital-economy-curriculums/test_validate_content.py -v` and confirm all property tests pass
  - Verify collection and 3 series exist in DB with correct titles, descriptions, and display orders
  - Ensure all tests pass, ask the user if questions arise.

- [x] 4. Phase 2 — Create story-reading curriculum scripts (Series 1, contentTypeTags `["story"]`)
  - [x] 4.1 Create `vi-en-digital-economy-curriculums/create_hanh_trinh_shopee.py` — Curriculum 1 "Hành Trình Của Shopee"
    - Format: `story_reading`, level: `preintermediate`, price 49, contentTypeTags `["story"]`
    - Series 1, display order 1
    - Description tone: `provocative_question`; farewell register: `introspective_guide`
    - Session_Vocab_Groups (20 unique words across 4 sessions of 5):
      - S1: platform, shopper, browse, listing, cart
      - S2: checkout, seller, customer, inventory, growth
      - S3: marketplace, store, supplier, online, shipping
      - S4: profit, expansion, packaging, transform, journey
    - Narrative arc: Mai, a Hanoi fabric-shop owner, opens her first Shopee store across 4 sessions; reading passages 150-200 / 150-200 / 150-200 / 200-250 words; one continuous story
    - Vietnamese platform mentions (≥3): Shopee, Lazada, Tiki; daily-life situations (≥2): Hanoi shop owner, students browsing on phones
    - Hand-written description (5-beat persuasive copy, ALL-CAPS Vietnamese opener), preview ~150 words Vietnamese, bilingual welcome introAudio 500-800 words, mid-session wrap-ups 200-400 words, farewell 400-600 words
    - Activity sequence per `ACTIVITY_TEMPLATES["story_reading"]`; final session includes writingSentence with 3-4 items
    - Validate with `validate(content, "story_reading", "preintermediate")` before upload
    - Calls: `create_curriculum(content, "en", "vi")`, `add_to_series(SERIES_1_ID, id)`, `set_display_order(id, 1)`, `set_price(id, 49)`. NO `setPublic`.
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.4, 2.5, 3.1, 3.4, 3.5, 3.6, 3.7, 4.1, 4.4, 4.5, 4.7, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 6.1, 6.2, 6.3, 6.4, 6.7, 7.1, 7.2, 7.3, 7.4, 7.5, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 9.1-9.9, 10.1-10.13, 11.1, 11.2, 12.1, 12.2, 13.5, 13.6, 13.8, 13.9, 14.1, 14.4, 14.5, 14.6_

  - [x] 4.2 Create `vi-en-digital-economy-curriculums/create_khoi_nghiep_viet.py` — Curriculum 2 "Câu Chuyện Khởi Nghiệp Việt"
    - Format: `story_reading`, level: `intermediate`, price 49
    - Series 1, display order 2
    - Description tone: `vivid_scenario`; farewell register: `warm_accountability`
    - Session_Vocab_Groups: S1 [founder, venture, capital, funding, pivot], S2 [scale, valuation, milestone, ambition, perseverance], S3 [mentor, ecosystem, innovation, breakthrough, prototype], S4 [investor, equity, traction, unicorn, vision]
    - Narrative arc: Composite founder Tuấn inspired by VNG, Tiki, MoMo, VinFast — co-founder ideation → pivot → scale → unicorn moment
    - Vietnamese platform mentions: VNG, Tiki, MoMo, VinFast; daily-life situations: HCMC coworking spaces, late-night coding sessions
    - Validate with `validate(content, "story_reading", "intermediate")` before upload
    - _Requirements: same as 4.1 (with intermediate level for sentence-length bounds 12-18)_

  - [x] 4.3 Create `vi-en-digital-economy-curriculums/create_tu_tien_mat_den_vi_so.py` — Curriculum 3 "Từ Tiền Mặt Đến Ví Số"
    - Format: `story_reading`, level: `intermediate`, price 49
    - Series 1, display order 3
    - Description tone: `metaphor_led`; farewell register: `practical_momentum`
    - Session_Vocab_Groups: S1 [cashless, wallet, transfer, scan, balance], S2 [transaction, fintech, adoption, convenience, trust], S3 [regulation, banking, deposit, withdrawal, generation], S4 [instant, secure, ledger, settlement, peer]
    - Narrative arc: Bà Hoa, a phở vendor on Hàng Buồm Street, adopts MoMo and VNPay; tracks one neighborhood's shift from cash to digital wallets
    - Vietnamese platform mentions: MoMo, VNPay, ZaloPay; daily-life situations: street vendor in Hà Nội, families sending tiền lì xì
    - Validate with `validate(content, "story_reading", "intermediate")` before upload
    - _Requirements: same as 4.2_

- [x] 5. Checkpoint — Phase 2 verification
  - Run all 3 story-reading scripts in display order (1, 2, 3)
  - Verify 3 curriculums exist in Series 1 in DB with correct display orders, prices=49, language="en", userLanguage="vi", contentTypeTags=`["story"]`
  - Run duplicate-check query for each of the 3 titles
  - Resolve any discovered issues (recreate, re-add, or reset display order/price)
  - Ensure all tests pass, ask the user if questions arise.

- [x] 6. Phase 3 — Create speaking curriculum scripts (Series 2, contentTypeTags `[]`)
  - [x] 6.1 Create `vi-en-digital-economy-curriculums/create_mua_sam_truc_tuyen.py` — Curriculum 4 "Mua Sắm Trực Tuyến"
    - Format: `speaking`, level: `preintermediate`, price 49, contentTypeTags `[]`
    - Series 2, display order 1
    - Description tone: `bold_declaration`; farewell register: `team_building_energy`
    - Session_Vocab_Groups: S1 [order, item, deliver, package, address], S2 [review, rating, discount, voucher, coupon], S3 [shipping, payment, confirm, cancel, track], S4 [arrive, damaged, satisfied, refund, return]
    - Reading passages conversational/instructional: 80-110 / 80-110 / 100-130 / 120-150 words; sub-aspect of e-commerce conversation across the 4 sessions
    - Vietnamese platform mentions: Shopee, Lazada, Tiki; daily-life situations: university student ordering, parents in Đà Nẵng buying gifts
    - Activity sequence per `ACTIVITY_TEMPLATES["speaking"]`; final session includes vocabLevel2 (all 20 words), second speakFlashcards round (all 20 words), readAlong, writingSentence (2-3 items)
    - Validate with `validate(content, "speaking", "preintermediate")` before upload
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.4, 2.5, 3.2, 3.4, 3.5, 3.6, 3.7, 4.2, 4.4, 4.5, 4.7, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 6.1, 6.2, 6.3, 6.4, 6.7, 7.1, 7.2, 7.3, 7.4, 7.5, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 9.1-9.9, 10.1-10.13, 11.1, 11.2, 12.1, 12.2, 13.5, 13.6, 13.8, 13.9, 14.1, 14.4, 14.5, 14.6_

  - [x] 6.2 Create `vi-en-digital-economy-curriculums/create_thanh_toan_khong_tien_mat.py` — Curriculum 5 "Thanh Toán Không Tiền Mặt"
    - Format: `speaking`, level: `preintermediate`, price 49
    - Series 2, display order 2
    - Description tone: `empathetic_observation`; farewell register: `practical_momentum`
    - Session_Vocab_Groups: S1 [account, fee, charge, code, link], S2 [send, receive, receipt, history, statement], S3 [amount, recharge, confirm, success, error], S4 [qr, password, pin, mobile, verify]
    - Vietnamese platform mentions: MoMo, VNPay, ZaloPay; daily-life situations: morning coffee at quán cà phê, paying for grocery delivery
    - Validate with `validate(content, "speaking", "preintermediate")` before upload
    - _Requirements: same as 6.1_

  - [x] 6.3 Create `vi-en-digital-economy-curriculums/create_lam_viec_tu_xa.py` — Curriculum 6 "Làm Việc Từ Xa"
    - Format: `speaking`, level: `preintermediate`, price 49
    - Series 2, display order 3
    - Description tone: `surprising_fact`; farewell register: `warm_accountability`
    - Session_Vocab_Groups: S1 [remote, meeting, video, microphone, mute], S2 [share, screen, schedule, deadline, project], S3 [task, team, manager, colleague, message], S4 [reply, available, focus, break, hybrid]
    - Vietnamese platform mentions: Grab, FPT, VNG; daily-life situations: freelancers in cafes, hybrid offices in District 1
    - Validate with `validate(content, "speaking", "preintermediate")` before upload
    - _Requirements: same as 6.1_

- [x] 7. Checkpoint — Phase 3 verification
  - Run all 3 speaking scripts in display order (1, 2, 3)
  - Verify 3 curriculums exist in Series 2 with correct display orders, prices=49, language="en", userLanguage="vi", contentTypeTags=`[]`
  - Run duplicate-check query for each of the 3 titles
  - Resolve any issues discovered
  - Ensure all tests pass, ask the user if questions arise.

- [x] 8. Phase 4 — Create balanced curriculum scripts (Series 3, contentTypeTags `[]`)
  - [x] 8.1 Create `vi-en-digital-economy-curriculums/create_mang_xa_hoi.py` — Curriculum 7 "Mạng Xã Hội Và Tiếp Thị Số"
    - Format: `balanced`, level: `preintermediate`, price 49, contentTypeTags `[]`
    - Series 3, display order 1
    - Description tone: `provocative_question`; farewell register: `quiet_awe`
    - Session_Vocab_Groups: S1 [post, like, follow, comment, content], S2 [viral, audience, brand, campaign, influencer], S3 [engagement, reach, target, click, banner], S4 [promote, channel, trend, hashtag, analytics]
    - Reading passages expository: 100-130 / 100-130 / 100-130 / 150-200 words
    - Vietnamese platform mentions: TikTok (Vietnamese creators), Shopee, MoMo, VinFast; daily-life situations: Vietnamese influencers, weekend markets
    - Activity sequence per `ACTIVITY_TEMPLATES["balanced"]`; session 3 includes writingSentence; final session includes vocabLevel2 + writingSentence + writingParagraph
    - Validate with `validate(content, "balanced", "preintermediate")` before upload
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.4, 2.5, 3.3, 3.4, 3.5, 3.6, 3.7, 4.3, 4.4, 4.5, 4.7, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 6.1, 6.2, 6.3, 6.4, 6.7, 7.1, 7.2, 7.3, 7.4, 7.5, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 9.1-9.9, 10.1-10.13, 11.1, 11.2, 12.1, 12.2, 13.5, 13.6, 13.8, 13.9, 14.1, 14.4, 14.5, 14.6_

  - [x] 8.2 Create `vi-en-digital-economy-curriculums/create_tien_ma_hoa_blockchain.py` — Curriculum 8 "Tiền Mã Hoá Và Blockchain"
    - Format: `balanced`, level: `intermediate`, price 49
    - Series 3, display order 2
    - Description tone: `bold_declaration`; farewell register: `practical_momentum`
    - Session_Vocab_Groups: S1 [cryptocurrency, blockchain, decentralized, token, mining], S2 [exchange, address, contract, smart, protocol], S3 [volatile, speculative, custody, validate, consensus], S4 [network, hash, encryption, immutable, distributed]
    - Reading passages educational/factual only — no investment advice, trading recommendations, or speculative return claims (Req 4.6)
    - Vietnamese platform mentions: VNG, FPT, Tiki; daily-life situations: Vietnamese fintech learners, university students
    - Validate with `validate(content, "balanced", "intermediate")` before upload
    - _Requirements: same as 8.1, plus 4.6_

  - [x] 8.3 Create `vi-en-digital-economy-curriculums/create_ai_trong_kinh_doanh.py` — Curriculum 9 "Trí Tuệ Nhân Tạo Trong Kinh Doanh"
    - Format: `balanced`, level: `intermediate`, price 49
    - Series 3, display order 3
    - Description tone: `metaphor_led`; farewell register: `introspective_guide`
    - Session_Vocab_Groups: S1 [artificial, intelligence, automate, algorithm, model], S2 [predict, dataset, training, chatbot, recommendation], S3 [efficiency, productivity, machine, learning, generate], S4 [analyze, insight, decision, augment, deploy]
    - Reading passages educational/factual only (Req 4.6)
    - Vietnamese platform mentions: Grab, Shopee, FPT, VNG; daily-life situations: customer service chat in HCMC, productivity apps
    - Validate with `validate(content, "balanced", "intermediate")` before upload
    - _Requirements: same as 8.2_

  - [x] 8.4 Create `vi-en-digital-economy-curriculums/create_an_ninh_mang.py` — Curriculum 10 "An Ninh Mạng Và Quyền Riêng Tư"
    - Format: `balanced`, level: `intermediate`, price 49
    - Series 3, display order 4
    - Description tone: `vivid_scenario`; farewell register: `team_building_energy`
    - Session_Vocab_Groups: S1 [cyber, security, password, encryption, privacy], S2 [breach, hacker, phishing, malware, firewall], S3 [authentication, vulnerable, protect, identity, leak], S4 [scam, fraud, sensitive, consent, threat]
    - Vietnamese platform mentions: MoMo, VNPay, FPT; daily-life situations: parents protecting accounts, students avoiding scams
    - Validate with `validate(content, "balanced", "intermediate")` before upload
    - _Requirements: same as 8.2_

- [x] 9. Checkpoint — Phase 4 verification
  - Run all 4 balanced scripts in display order (1, 2, 3, 4)
  - Verify 4 curriculums exist in Series 3 with correct display orders, prices=49, language="en", userLanguage="vi", contentTypeTags=`[]`
  - Run duplicate-check query for each of the 4 titles
  - Resolve any issues discovered
  - Ensure all tests pass, ask the user if questions arise.

- [x] 10. Phase 5 — Final integration verification
  - [x] 10.1 Run integration verification SQL queries (design Section "Integration verification")
    - Query 1: Count and core attributes — expect 10 rows with `language='en'`, `user_language='vi'`, `price=49`, correct contentTypeTags
    - Query 2: Language pair check — expect 0 rows where `language != 'en'` or `user_language != 'vi'`
    - Query 3: Price check — expect 0 rows where `price != 49`
    - Query 4a: Story-reading contentTypeTags — expect 0 rows where C1, C2, C3 do NOT have `["story"]`
    - Query 4b: Speaking + Balanced contentTypeTags — expect 0 rows where C4-C10 do NOT have `[]`
    - Query 5: Session count — expect 0 rows where `jsonb_array_length(content->'learningSessions') != 4`
    - Query 6: Series membership and display orders — expect Series 1 (3 curriculums, orders 1-3), Series 2 (3 curriculums, orders 1-3), Series 3 (4 curriculums, orders 1-4)
    - Query 7: Collection-series wiring — expect 1 collection containing the 3 series with display orders 1, 2, 3
    - Query 8: Privacy check — expect 0 rows where `is_public = TRUE`
    - Query 9: Duplicate title check — expect 0 rows with `COUNT(*) > 1`
    - Query 10: Strip-keys probe — expect `has_strip_key = FALSE` for every row
    - _Requirements: 1.1, 1.2, 1.4, 1.5, 1.6, 1.8, 1.9, 3.4, 11.1, 11.4, 12.1, 12.2, 13.1-13.6, 13.8, 13.9, 16.3_

  - [x] 10.2 Resolve any issues found during verification
    - Missing curriculums: recreate affected scripts (since they may have been deleted) and re-run; re-add to series, set display order, set price
    - Wrong display orders or prices: fix via `set_display_order` / `set_price` API calls
    - Public curriculums (should not happen): call `setPublic` with `isPublic: false`
    - Duplicate titles: keep earliest, remove extras from series via `removeCurriculum`, then `delete`
    - Strip keys present: rewrite content, call `curriculum/update` with corrected JSON
    - _Requirements: 11.4, 12.3, 15.3, 16.4_

  - [x] 10.3 Run smoke filesystem and code checks (design Section "Smoke checks")
    - Confirm all 10 `create_*.py`, `orchestrator.py`, `validate_content.py`, `test_validate_content.py` exist in `vi-en-digital-economy-curriculums/`
    - `grep -R "setPublic" vi-en-digital-economy-curriculums/` produces zero matches
    - `grep -R "displayOrder.*collection" vi-en-digital-economy-curriculums/orchestrator.py` shows no collection-displayOrder call
    - _Requirements: 1.9, 12.1, 13.10, 14.4_

  - [x] 10.4 Manual content review checklist (design Section "Manual content review checklist")
    - Each story-reading curriculum tells one continuous narrative across 4 sessions (Req 4.7)
    - Each speaking-curriculum reading is conversational/instructional (Req 4.2)
    - Each balanced-curriculum reading is expository (Req 4.3)
    - Crypto/AI passages (C8, C9) are educational, never investment advice (Req 4.6)
    - introAudio scripts are bilingual: Vietnamese explanations + English vocabulary (Req 8.5)
    - Each description follows persuasive copy 5-beat structure with assigned tone (Reqs 6.1, 6.4)
    - Each farewell uses the assigned register and reviews 5-6 vocab words (Req 8.4)
    - Vocabulary is level-appropriate (preintermediate concrete, intermediate abstract/specialized) (Req 5.3)
    - No template-generated text — every passage hand-written (Reqs 8.6, 14.6)
    - Each title is in Vietnamese with brand exceptions only (Req 7.2)
    - _Requirements: 4.2, 4.3, 4.6, 4.7, 5.3, 6.1, 6.4, 7.2, 8.4, 8.5, 8.6, 14.6_

- [x] 11. Phase 6 — Documentation and cleanup
  - [x] 11.1 Create `vi-en-digital-economy-curriculums/README.md`
    - Collection ID, all 3 series IDs (with titles, display orders, description tones)
    - All 10 curriculum IDs with: title, level, format (story_reading/speaking/balanced), series number, display order, contentTypeTags, price (49), description tone, farewell register
    - Vocabulary lists per curriculum organized by Session_Vocab_Group (S1-S4)
    - Skill focus assignments and tone-distribution audit (description tones, farewell registers, series tones)
    - Vocabulary distinctness audit (pairwise overlap table from design)
    - Cultural-context plan summary (platform mentions, daily-life situations per curriculum)
    - SQL verification queries (the 10 from Phase 5) parameterized with the actual IDs and titles
    - Recreation context: how the 10 scripts were authored, where source materials lived, and the phased execution order
    - _Requirements: 15.1_

  - [x] 11.2 Delete creation scripts after database verification confirms all 10 curriculums exist
    - Delete all 10 `create_*.py` scripts from `vi-en-digital-economy-curriculums/` (only after Phase 5 verification confirms presence in DB)
    - Delete `orchestrator.py` (only after Phase 1 confirmation)
    - Retain `README.md`, `validate_content.py`, and `test_validate_content.py` in the directory
    - _Requirements: 15.2_

  - [x] 11.3 Run final duplicate check and resolve
    - For each of the 10 curriculum titles, run the duplicate-check SQL query against `uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'`, excluding `_deleted` UIDs
    - If any title has `COUNT(*) > 1`: keep earliest by `created_at`; remove extras from their series via `curriculum-series/removeCurriculum`; then delete via `curriculum/delete`
    - _Requirements: 15.3_

- [x] 12. Final checkpoint — All tasks complete
  - Verify 10 new curriculums total: 3 story-reading (Series 1) + 3 speaking (Series 2) + 4 balanced (Series 3)
  - Verify the 1 collection contains 3 series in display orders 1, 2, 3
  - Verify all 10 prices are 49, all `language='en'` and `user_language='vi'`, all are private (`is_public = FALSE`)
  - Verify contentTypeTags: 3 story-reading have `["story"]`; 7 speaking + balanced have `[]`
  - Verify no `setPublic` calls were made anywhere in the spec (zero `grep` matches)
  - Verify no collection `displayOrder` was set on the collection itself (workspace rule, Req 13.10)
  - Verify `validate_content.py` and `test_validate_content.py` remain in the directory along with `README.md`; all 10 `create_*.py` and `orchestrator.py` are deleted
  - Verify pairwise vocabulary overlap ≤ 2 across all 10 curriculums (Req 2.3a) and no word appears in more than 2 curriculums (Req 2.3b)
  - Ensure all tests pass, ask the user if questions arise.

## Notes

- Tasks marked with `*` are optional and can be skipped for faster MVP
- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation between phases
- Property tests validate universal correctness properties from the design document
- Design-time table tests validate hand-authored design constraints (vocab overlap, tone distribution, title shape)
- Root-level `api_helpers.py` and `firebase_token.py` are reused as-is — no changes needed
- All curriculum content must be hand-crafted — no template-based generation for learner-facing text
- Marketing text (title, description, preview) is in Vietnamese
- introAudio scripts are bilingual (Vietnamese explanations of English vocabulary)
- Reading passages are entirely in English
- vocabList: English words in lowercase, never named `words`
- All curriculums private by default — no `setPublic` calls anywhere in the spec
- Collection has no `displayOrder` set (workspace rule, Req 13.10)
- Phased execution order (Req 16): orchestrator → 3 story-reading → 3 speaking → 4 balanced → verification → docs/cleanup
- Each curriculum: immediately add to series + set display order + set price after creation (Req 16.2)
- Description tone distribution (Req 6.6): max 2 per tone (well under 30% cap of 3); per-series adjacency clean (design Section 5.1)
- Farewell register distribution (Req 8.9): each register used 1-3 times; per-series adjacency clean (design Section 5.2)
- Series description tones (Req 13.7): 3 distinct (vivid_scenario, empathetic_observation, bold_declaration)
- Vocabulary distinctness (Req 2.3): max pairwise overlap = 1; repeated words {shipping, confirm, address, password, encryption} each appear in exactly 2 curriculums

## Task Dependency Graph

```json
{
  "waves": [
    { "id": 0, "tasks": ["1.1"] },
    { "id": 1, "tasks": ["1.2", "1.3", "2.1"] },
    { "id": 2, "tasks": ["2.2"] },
    { "id": 3, "tasks": ["4.1", "4.2", "4.3"] },
    { "id": 4, "tasks": ["6.1", "6.2", "6.3"] },
    { "id": 5, "tasks": ["8.1", "8.2", "8.3", "8.4"] },
    { "id": 6, "tasks": ["10.1", "10.3", "10.4"] },
    { "id": 7, "tasks": ["10.2"] },
    { "id": 8, "tasks": ["11.1"] },
    { "id": 9, "tasks": ["11.2", "11.3"] }
  ]
}
```
