# Tasks

## Task 1: Create validation script and series setup

- [x] 1.1 Create `nail-professional-speaking-curriculum/` folder
- [x] 1.2 Create `validate_nail_curriculum.py` implementing all 11 correctness properties as assertions against a curriculum content dict
- [x] 1.3 Create `orchestrate_nail_series.py` that creates the series via `curriculum-series/create` with Vietnamese title and description (≤255 chars), and has functions to add curriculums and set display orders

## Task 2: Create Curriculum 1 — Chào Khách và Hỏi Ý (Greeting & Asking)

- [x] 2.1 Create `create_nail_1_greeting.py` with hand-written content: W1 (welcome, appointment, walk-in, prefer, seat), W2 (schedule, available, wait, ready, check), W3 (service, today, choose, help, enjoy)
- [x] 2.2 Write all introAudio scripts in Vietnamese teaching each word with nail salon context examples
- [x] 2.3 Write 3 first-person mini-speech reading passages (2–4 sentences each) and 1 review passage (6–12 sentences) using all vocab words
- [x] 2.4 Write persuasive description (vivid_scenario tone), preview (~150 words), and all activity metadata
- [x] 2.5 Run validation, execute script, verify curriculum created successfully

## Task 3: Create Curriculum 2 — Tư Vấn Kiểu Móng (Nail Style Preferences)

- [x] 3.1 Create `create_nail_2_preferences.py` with hand-written content: W1 (shape, oval, square, round, length), W2 (color, shade, match, natural, bold), W3 (design, simple, pattern, glitter, tip)
- [x] 3.2 Write all introAudio scripts in Vietnamese teaching each word with nail style consultation context
- [x] 3.3 Write 3 first-person mini-speech reading passages and 1 review passage using all vocab words
- [x] 3.4 Write persuasive description (empathetic_observation tone), preview, and all activity metadata
- [x] 3.5 Run validation, execute script, verify curriculum created successfully

## Task 4: Create Curriculum 3 — Giới Thiệu Dịch Vụ (Describing Services)

- [x] 4.1 Create `create_nail_3_services.py` with hand-written content: W1 (gel, polish, manicure, pedicure, acrylic), W2 (soak, trim, file, buff, cuticle), W3 (coat, dry, cure, last, protect)
- [x] 4.2 Write all introAudio scripts in Vietnamese teaching each word with service description context
- [x] 4.3 Write 3 first-person mini-speech reading passages and 1 review passage using all vocab words
- [x] 4.4 Write persuasive description (bold_declaration tone), preview, and all activity metadata
- [x] 4.5 Run validation, execute script, verify curriculum created successfully

## Task 5: Create Curriculum 4 — Xử Lý Phàn Nàn (Handling Concerns)

- [x] 5.1 Create `create_nail_4_concerns.py` with hand-written content: W1 (sorry, fix, redo, adjust, concern), W2 (chip, crack, uneven, thick, thin), W3 (careful, gentle, comfortable, satisfy, promise)
- [x] 5.2 Write all introAudio scripts in Vietnamese teaching each word with complaint handling context
- [x] 5.3 Write 3 first-person mini-speech reading passages and 1 review passage using all vocab words
- [x] 5.4 Write persuasive description (provocative_question tone), preview, and all activity metadata
- [x] 5.5 Run validation, execute script, verify curriculum created successfully

## Task 6: Create Curriculum 5 — Trò Chuyện Nhẹ (Small Talk)

- [x] 6.1 Create `create_nail_5_small_talk.py` with hand-written content: W1 (weather, weekend, plan, family, vacation), W2 (busy, relax, favorite, movie, music), W3 (nice, beautiful, love, try, recommend)
- [x] 6.2 Write all introAudio scripts in Vietnamese teaching each word with small talk context
- [x] 6.3 Write 3 first-person mini-speech reading passages and 1 review passage using all vocab words
- [x] 6.4 Write persuasive description (surprising_fact tone), preview, and all activity metadata
- [x] 6.5 Run validation, execute script, verify curriculum created successfully

## Task 7: Create Curriculum 6 — Thanh Toán và Tiễn Khách (Payment & Farewell)

- [x] 7.1 Create `create_nail_6_payment.py` with hand-written content: W1 (total, cash, card, change, receipt), W2 (tip, discount, price, charge, pay), W3 (thank, visit, return, next, care)
- [x] 7.2 Write all introAudio scripts in Vietnamese teaching each word with payment/checkout context
- [x] 7.3 Write 3 first-person mini-speech reading passages and 1 review passage using all vocab words
- [x] 7.4 Write persuasive description (metaphor_led tone), preview, and all activity metadata
- [x] 7.5 Run validation, execute script, verify curriculum created successfully

## Task 8: Series assembly and verification

- [x] 8.1 Run orchestrator to create series and add all 6 curriculums with sequential display orders (1–6)
- [x] 8.2 Run cross-curriculum vocab uniqueness check (Property 5) across all 6 curriculums
- [x] 8.3 Query DB to verify all curriculums are in the series with correct display orders and `is_public: false`
- [x] 8.4 Check for and clean up any duplicate curriculums

## Task 9: Documentation and cleanup

- [x] 9.1 Create `nail-professional-speaking-curriculum/README.md` with: series ID and title, all 6 curriculum IDs and titles, display orders, vocab lists, creation method, SQL queries, recreation context
- [x] 9.2 Delete all `.py` scripts from the folder (creation scripts, orchestrator, validation script)
