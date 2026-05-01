# Tasks

## Task 1: Create validation script and folder setup

- [x] 1.1 Create `vi-en-customer-psychology-curriculums/` folder
- [x] 1.2 Create `validate_customer_psychology.py` implementing all 11 correctness properties as assertions against a curriculum content dict (session structure, vocab distribution, reading passage constraints, vocab format, activity schema, title formats, top-level structure, strip-keys, introAudio coverage, valid activity types)
  - _Requirements: 1.1–1.10, 2.1–2.2, 2.8–2.10, 3.7, 7.1–7.11, 8.1–8.8, 9.1, 15.1–15.7_
- [x] 1.3 Create `orchestrate_series.py` that creates the series "Tâm Lý Khách Hàng" via `curriculum-series/create` with Vietnamese title and description (≤255 chars, metaphor_led tone), and has functions to add curriculums and set display orders (Anchoring=1, Social_Proof=2, Loss_Aversion=3, Emotional_Triggers=4, Trust=5)
  - _Requirements: 10.1, 10.2, 10.5, 14.1_

## Task 2: Create Curriculum 1 — Ấn Tượng Đầu & Hiệu Ứng Neo (First Impressions & Anchoring)

- [x] 2.1 Create `create_anchoring.py` with hand-written content: W1 (anchor, perception, reference, premium, contrast), W2 (bias, initial, frame, benchmark, expectation), W3 (impression, positioning, threshold, baseline, cognitive)
  - _Requirements: 3.1, 3.7, 3.8, 12.1, 13.1_
- [x] 2.2 Write all introAudio scripts in Vietnamese teaching each word with anchoring/first-impression context examples (setting reference prices, making strong first impressions, using contrast in pricing); farewell script (400–600 words) using introspective_guide tone
  - _Requirements: 6.1–6.6, 13.3, 14.6_
- [x] 2.3 Write 3 first-person business narrative reading passages (2–4 sentences each, about applying anchoring in sales) and 1 review passage (6–12 sentences) using all 15 vocab words
  - _Requirements: 2.1–2.10_
- [x] 2.4 Write persuasive description (provocative_question tone), preview (~150 words in Vietnamese), and all activity metadata (titles, descriptions following format conventions)
  - _Requirements: 4.1, 5.2–5.6, 7.2–7.5, 8.1–8.8, 14.5_
- [x] 2.5 Run validation, execute script, verify curriculum created successfully
  - _Requirements: 11.1–11.4, 15.1–15.7, 16.1–16.3_

## Task 3: Create Curriculum 2 — Bằng Chứng Xã Hội & Tâm Lý Bầy Đàn (Social Proof & Herd Mentality)

- [x] 3.1 Create `create_social_proof.py` with hand-written content: W1 (testimonial, endorsement, consensus, conform, influence), W2 (popularity, bandwagon, credibility, peer, validation), W3 (trend, follower, mainstream, viral, recommendation)
  - _Requirements: 3.2, 3.7, 3.8, 12.1, 13.1_
- [x] 3.2 Write all introAudio scripts in Vietnamese teaching each word with social proof context examples (showing customer reviews, displaying best-seller labels, referencing popular choices); farewell script (400–600 words) using warm_accountability tone
  - _Requirements: 6.1–6.6, 13.4, 14.6_
- [x] 3.3 Write 3 first-person business narrative reading passages (2–4 sentences each, about using social proof in sales) and 1 review passage (6–12 sentences) using all 15 vocab words
  - _Requirements: 2.1–2.10_
- [x] 3.4 Write persuasive description (bold_declaration tone), preview (~150 words in Vietnamese), and all activity metadata (titles, descriptions following format conventions)
  - _Requirements: 4.2, 5.2–5.6, 7.2–7.5, 8.1–8.8, 14.5_
- [x] 3.5 Run validation, execute script, verify curriculum created successfully
  - _Requirements: 11.1–11.4, 15.1–15.7, 16.1–16.3_

## Task 4: Create Curriculum 3 — Sợ Mất & Tâm Lý Khẩn Cấp (Loss Aversion & Urgency)

- [x] 4.1 Create `create_loss_aversion.py` with hand-written content: W1 (scarcity, deadline, urgency, exclusive, limited), W2 (hesitation, regret, countdown, shortage, expire), W3 (forfeit, opportunity, irreversible, procrastinate, incentive)
  - _Requirements: 3.3, 3.7, 3.8, 12.1, 13.1_
- [x] 4.2 Write all introAudio scripts in Vietnamese teaching each word with loss aversion context examples (limited-time offers, "only 3 left" messaging, deadline-driven promotions); farewell script (400–600 words) using team_building_energy tone
  - _Requirements: 6.1–6.6, 13.5, 14.6_
- [x] 4.3 Write 3 first-person business narrative reading passages (2–4 sentences each, about using urgency/scarcity in sales) and 1 review passage (6–12 sentences) using all 15 vocab words
  - _Requirements: 2.1–2.10_
- [x] 4.4 Write persuasive description (vivid_scenario tone), preview (~150 words in Vietnamese), and all activity metadata (titles, descriptions following format conventions)
  - _Requirements: 4.3, 5.2–5.6, 7.2–7.5, 8.1–8.8, 14.5_
- [x] 4.5 Run validation, execute script, verify curriculum created successfully
  - _Requirements: 11.1–11.4, 15.1–15.7, 16.1–16.3_

## Task 5: Create Curriculum 4 — Cảm Xúc & Nghệ Thuật Kể Chuyện (Emotional Triggers & Storytelling)

- [x] 5.1 Create `create_emotional_triggers.py` with hand-written content: W1 (narrative, empathy, compelling, resonate, aspiration), W2 (nostalgia, curiosity, vulnerable, authentic, relatable), W3 (inspire, evoke, tension, climax, transformation)
  - _Requirements: 3.4, 3.7, 3.8, 12.1, 13.1_
- [x] 5.2 Write all introAudio scripts in Vietnamese teaching each word with emotional storytelling context examples (sharing customer transformation stories, creating curiosity about product origins); farewell script (400–600 words) using quiet_awe tone
  - _Requirements: 6.1–6.6, 13.6, 14.6_
- [x] 5.3 Write 3 first-person business narrative reading passages (2–4 sentences each, about using emotional triggers in sales) and 1 review passage (6–12 sentences) using all 15 vocab words
  - _Requirements: 2.1–2.10_
- [x] 5.4 Write persuasive description (empathetic_observation tone), preview (~150 words in Vietnamese), and all activity metadata (titles, descriptions following format conventions)
  - _Requirements: 4.4, 5.2–5.6, 7.2–7.5, 8.1–8.8, 14.5_
- [x] 5.5 Run validation, execute script, verify curriculum created successfully
  - _Requirements: 11.1–11.4, 15.1–15.7, 16.1–16.3_

## Task 6: Create Curriculum 5 — Xây Dựng Niềm Tin & Có Qua Có Lại (Trust & Reciprocity)

- [x] 6.1 Create `create_trust.py` with hand-written content: W1 (transparency, reciprocity, loyalty, guarantee, integrity), W2 (rapport, generosity, commitment, consistency, reputation), W3 (goodwill, reliable, trustworthy, accountability, credibility)
  - _Requirements: 3.5, 3.7, 3.8, 12.1, 13.1_
- [x] 6.2 Write all introAudio scripts in Vietnamese teaching each word with trust-building context examples (offering free samples, providing money-back guarantees, being transparent about pricing); farewell script (400–600 words) using practical_momentum tone
  - _Requirements: 6.1–6.6, 13.7, 14.6_
- [x] 6.3 Write 3 first-person business narrative reading passages (2–4 sentences each, about building trust with customers) and 1 review passage (6–12 sentences) using all 15 vocab words
  - _Requirements: 2.1–2.10_
- [x] 6.4 Write persuasive description (surprising_fact tone), preview (~150 words in Vietnamese), and all activity metadata (titles, descriptions following format conventions)
  - _Requirements: 4.5, 5.2–5.6, 7.2–7.5, 8.1–8.8, 14.5_
- [x] 6.5 Run validation, execute script, verify curriculum created successfully
  - _Requirements: 11.1–11.4, 15.1–15.7, 16.1–16.3_

## Task 7: Series assembly and verification

- [x] 7.1 Run orchestrator to create series and add all 5 curriculums with sequential display orders (Anchoring=1, Social_Proof=2, Loss_Aversion=3, Emotional_Triggers=4, Trust=5)
  - _Requirements: 10.1–10.5, 14.1_
- [x] 7.2 Run cross-curriculum vocab uniqueness check (Property 5) across all 5 curriculums
  - _Requirements: 3.8, 14.3_
- [x] 7.3 Query DB to verify all 5 curriculums are in the series with correct display orders and `is_public: false`
  - _Requirements: 10.2, 10.3, 11.3_
- [x] 7.4 Check for and clean up any duplicate curriculums
  - _Requirements: 16.1–16.3_

## Task 8: Documentation and cleanup

- [x] 8.1 Create `vi-en-customer-psychology-curriculums/README.md` with: series ID and title, all 5 curriculum IDs and titles, display orders, vocab lists, tone assignments, farewell tone assignments, creation method, SQL queries, recreation context
  - _Requirements: 12.5_
- [x] 8.2 Delete all `.py` scripts from the folder (5 creation scripts, orchestrator, validation script)
  - _Requirements: 12.6_
