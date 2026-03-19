# Implementation Plan: Topic-Based Vocab Series Expansion

## Overview

Create 4 new series (16 curriculums total) for the "Học Từ Vựng Theo Chủ Đề" collection (279d6843). Each curriculum is a standalone Python script with all hand-written content (18 words, 5 sessions, persuasive copy). Each series has an orchestrator script for series-level setup. After verification, scripts are deleted and READMEs are written.

## Tasks

- [x] 1. Science & Technology Series — Curriculum Scripts
  - [x] 1.1 Create `science-technology-series/create_science_1_ai.py` — AI & Machine Learning curriculum
    - Define 18 domain-specific vocabulary words (W1, W2, W3 — 6 each) about artificial intelligence and machine learning
    - Write 3 reading passages (R1, R2, R3) and FULL combined text in English
    - Write persuasive Vietnamese description (5-beat structure), preview (~150 words), and curriculum title
    - Write 5 sessions of hand-crafted introAudio scripts (welcome, vocab teaching, grammar notes per learning session; review intro for session 4; farewell with word review for session 5)
    - Write writingSentence items with targetVocab, specific context prompts, and "Ví dụ:" examples for each session
    - Include all activity metadata (title, description) following the naming conventions
    - Include inline `strip_keys()`, `validate(content)` function checking Properties 1-7, 11
    - API call: `curriculum/create` with `language="en"`, `userLanguage="vi"`, `content=json.dumps(content)`
    - Print created curriculum ID
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 4.1, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 8.1, 8.3, 9.1, 9.2, 10.1, 11.1, 11.3_

  - [x] 1.2 Create `science-technology-series/create_science_2_space.py` — Space Exploration curriculum
    - Same structure as 1.1 but with 18 vocabulary words about space exploration and the new space race
    - All text content (description, preview, introAudio scripts, reading passages, writing prompts) hand-written for this specific topic
    - Include inline `strip_keys()`, `validate(content)`, and API call
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 4.1, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 8.1, 8.3, 9.1, 9.2, 10.1, 11.1, 11.3_

  - [x] 1.3 Create `science-technology-series/create_science_3_genetics.py` — Genetic Engineering & CRISPR curriculum
    - Same structure as 1.1 but with 18 vocabulary words about genetic engineering and CRISPR
    - All text content hand-written for this specific topic
    - Include inline `strip_keys()`, `validate(content)`, and API call
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 4.1, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 8.1, 8.3, 9.1, 9.2, 10.1, 11.1, 11.3_

  - [x] 1.4 Create `science-technology-series/create_science_4_quantum.py` — Quantum Computing curriculum
    - Same structure as 1.1 but with 18 vocabulary words about quantum computing and the future of processing
    - All text content hand-written for this specific topic
    - Include inline `strip_keys()`, `validate(content)`, and API call
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 4.1, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 8.1, 8.3, 9.1, 9.2, 10.1, 11.1, 11.3_

- [x] 2. Science & Technology Series — Orchestrator & Execution
  - [x] 2.1 Create `science-technology-series/create_science_series.py` — Series orchestrator
    - Create series via `curriculum-series/create` with title "Khoa Học & Công Nghệ (Science & Technology)", Vietnamese description (≤255 chars), `isPublic: true`
    - Add all 4 curriculum IDs to series via `curriculum-series/addCurriculum`
    - Set curriculum display orders (0, 1, 2, 3) via `curriculum/setDisplayOrder`
    - Add series to collection 279d6843 via `curriculum-collection/addSeriesToCollection`
    - Set series display order 300 via `curriculum-series/setDisplayOrder`
    - _Requirements: 1.1, 1.2, 1.3, 7.1, 7.2, 8.2, 10.3, 11.2_

  - [x] 2.2 Run all 4 curriculum scripts and the orchestrator, verify output
    - Run `python create_science_1_ai.py`, `create_science_2_space.py`, `create_science_3_genetics.py`, `create_science_4_quantum.py`
    - Paste curriculum IDs into orchestrator, run `python create_science_series.py`
    - _Requirements: 7.3, 11.1_

- [x] 3. Checkpoint — Science & Technology series
  - Ensure all 4 curriculum scripts ran successfully and the orchestrator completed. Verify via SQL that the series has 4 curriculums with correct display orders. Ask the user if questions arise.

- [x] 4. Economics & Personal Finance Series — Curriculum Scripts
  - [x] 4.1 Create `economics-finance-series/create_econ_1_behavioral.py` — Behavioral Economics curriculum
    - Define 18 vocabulary words (W1, W2, W3) about behavioral economics and decision-making
    - Write 3 English reading passages, persuasive Vietnamese description/preview/title, 5 sessions of introAudio scripts, writingSentence items
    - Include inline `strip_keys()`, `validate(content)`, and API call
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 4.1, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 8.1, 8.3, 9.1, 9.2, 10.1, 12.1, 12.3_

  - [x] 4.2 Create `economics-finance-series/create_econ_2_investing.py` — Investing Fundamentals curriculum
    - Same structure with 18 vocabulary words about investing fundamentals and compound growth
    - All text content hand-written for this specific topic
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 4.1, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 8.1, 8.3, 9.1, 9.2, 10.1, 12.1, 12.3_

  - [x] 4.3 Create `economics-finance-series/create_econ_3_inflation.py` — Inflation & Monetary Policy curriculum
    - Same structure with 18 vocabulary words about inflation, central banks, and monetary policy
    - All text content hand-written for this specific topic
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 4.1, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 8.1, 8.3, 9.1, 9.2, 10.1, 12.1, 12.3_

  - [x] 4.4 Create `economics-finance-series/create_econ_4_gig.py` — Gig Economy curriculum
    - Same structure with 18 vocabulary words about the gig economy and future of employment
    - All text content hand-written for this specific topic
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 4.1, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 8.1, 8.3, 9.1, 9.2, 10.1, 12.1, 12.3_

- [x] 5. Economics & Personal Finance Series — Orchestrator & Execution
  - [x] 5.1 Create `economics-finance-series/create_econ_series.py` — Series orchestrator
    - Create series "Kinh Tế & Tài Chính Cá Nhân (Economics & Personal Finance)", description ≤255 chars, `isPublic: true`
    - Add 4 curriculums, set display orders 0-3, add to collection 279d6843, set series display order 400
    - _Requirements: 1.1, 1.2, 1.3, 7.1, 7.2, 8.2, 10.3, 12.2_

  - [x] 5.2 Run all 4 curriculum scripts and the orchestrator, verify output
    - Run each curriculum script, paste IDs into orchestrator, run orchestrator
    - _Requirements: 7.3, 12.1_

- [x] 6. Checkpoint — Economics & Personal Finance series
  - Ensure all 4 curriculum scripts ran successfully and the orchestrator completed. Verify via SQL that the series has 4 curriculums with correct display orders. Ask the user if questions arise.

- [x] 7. Environment & Sustainability Series — Curriculum Scripts
  - [x] 7.1 Create `environment-sustainability-series/create_env_1_climate.py` — Climate Change curriculum
    - Define 18 vocabulary words about climate change and the carbon cycle
    - Write 3 English reading passages, persuasive Vietnamese description/preview/title, 5 sessions of introAudio scripts, writingSentence items
    - Include inline `strip_keys()`, `validate(content)`, and API call
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 4.1, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 8.1, 8.3, 9.1, 9.2, 10.1, 13.1, 13.3_

  - [x] 7.2 Create `environment-sustainability-series/create_env_2_ocean.py` — Ocean Conservation curriculum
    - Same structure with 18 vocabulary words about ocean conservation and marine ecosystems
    - All text content hand-written for this specific topic
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 4.1, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 8.1, 8.3, 9.1, 9.2, 10.1, 13.1, 13.3_

  - [x] 7.3 Create `environment-sustainability-series/create_env_3_energy.py` — Renewable Energy curriculum
    - Same structure with 18 vocabulary words about renewable energy and the grid transition
    - All text content hand-written for this specific topic
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 4.1, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 8.1, 8.3, 9.1, 9.2, 10.1, 13.1, 13.3_

  - [x] 7.4 Create `environment-sustainability-series/create_env_4_agriculture.py` — Sustainable Agriculture curriculum
    - Same structure with 18 vocabulary words about sustainable agriculture and food systems
    - All text content hand-written for this specific topic
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 4.1, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 8.1, 8.3, 9.1, 9.2, 10.1, 13.1, 13.3_

- [x] 8. Environment & Sustainability Series — Orchestrator & Execution
  - [x] 8.1 Create `environment-sustainability-series/create_env_series.py` — Series orchestrator
    - Create series "Môi Trường & Phát Triển Bền Vững (Environment & Sustainability)", description ≤255 chars, `isPublic: true`
    - Add 4 curriculums, set display orders 0-3, add to collection 279d6843, set series display order 500
    - _Requirements: 1.1, 1.2, 1.3, 7.1, 7.2, 8.2, 10.3, 13.2_

  - [x] 8.2 Run all 4 curriculum scripts and the orchestrator, verify output
    - Run each curriculum script, paste IDs into orchestrator, run orchestrator
    - _Requirements: 7.3, 13.1_

- [x] 9. Checkpoint — Environment & Sustainability series
  - Ensure all 4 curriculum scripts ran successfully and the orchestrator completed. Verify via SQL that the series has 4 curriculums with correct display orders. Ask the user if questions arise.

- [x] 10. Culture & Society Series — Curriculum Scripts
  - [x] 10.1 Create `culture-society-series/create_culture_1_social_media.py` — Social Media Psychology curriculum
    - Define 18 vocabulary words about social media psychology and digital wellbeing
    - Write 3 English reading passages, persuasive Vietnamese description/preview/title, 5 sessions of introAudio scripts, writingSentence items
    - Include inline `strip_keys()`, `validate(content)`, and API call
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 4.1, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 8.1, 8.3, 9.1, 9.2, 10.1, 14.1, 14.3_

  - [x] 10.2 Create `culture-society-series/create_culture_2_cultural_intel.py` — Cultural Intelligence curriculum
    - Same structure with 18 vocabulary words about cultural intelligence and cross-cultural communication
    - All text content hand-written for this specific topic
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 4.1, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 8.1, 8.3, 9.1, 9.2, 10.1, 14.1, 14.3_

  - [x] 10.3 Create `culture-society-series/create_culture_3_urbanization.py` — Urbanization curriculum
    - Same structure with 18 vocabulary words about urbanization and the future of cities
    - All text content hand-written for this specific topic
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 4.1, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 8.1, 8.3, 9.1, 9.2, 10.1, 14.1, 14.3_

  - [x] 10.4 Create `culture-society-series/create_culture_4_future_work.py` — Future of Work curriculum
    - Same structure with 18 vocabulary words about the future of work and automation
    - All text content hand-written for this specific topic
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 4.1, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 8.1, 8.3, 9.1, 9.2, 10.1, 14.1, 14.3_

- [x] 11. Culture & Society Series — Orchestrator & Execution
  - [x] 11.1 Create `culture-society-series/create_culture_series.py` — Series orchestrator
    - Create series "Văn Hóa & Xã Hội (Culture & Society)", description ≤255 chars, `isPublic: true`
    - Add 4 curriculums, set display orders 0-3, add to collection 279d6843, set series display order 600
    - _Requirements: 1.1, 1.2, 1.3, 7.1, 7.2, 8.2, 10.3, 14.2_

  - [x] 11.2 Run all 4 curriculum scripts and the orchestrator, verify output
    - Run each curriculum script, paste IDs into orchestrator, run orchestrator
    - _Requirements: 7.3, 14.1_

- [x] 12. Checkpoint — Culture & Society series
  - Ensure all 4 curriculum scripts ran successfully and the orchestrator completed. Verify via SQL that the series has 4 curriculums with correct display orders. Ask the user if questions arise.

- [x] 13. Post-creation verification across all 4 series
  - [x] 13.1 Run SQL verification queries against the database
    - Verify collection 279d6843 has exactly 6 series (2 existing + 4 new)
    - Verify each new series has exactly 4 curriculums
    - Verify series display orders: 300, 400, 500, 600
    - Verify curriculum display orders within each series: 0, 1, 2, 3
    - Verify language homogeneity via `curriculum_series_language_list` (all vi-en)
    - _Requirements: 1.4, 7.1, 7.2, 7.3, 10.1, 10.2_

- [x] 14. Cleanup — Delete scripts and write READMEs
  - [x] 14.1 Delete all curriculum and orchestrator scripts from `science-technology-series/`, write `README.md`
    - README includes: series ID, 4 curriculum IDs and titles, creation method, SQL queries, recreation context
    - _Requirements: 8.4, 15.1, 15.2, 15.3_

  - [x] 14.2 Delete all scripts from `economics-finance-series/`, write `README.md`
    - README includes: series ID, 4 curriculum IDs and titles, creation method, SQL queries, recreation context
    - _Requirements: 8.4, 15.1, 15.2, 15.3_

  - [x] 14.3 Delete all scripts from `environment-sustainability-series/`, write `README.md`
    - README includes: series ID, 4 curriculum IDs and titles, creation method, SQL queries, recreation context
    - _Requirements: 8.4, 15.1, 15.2, 15.3_

  - [x] 14.4 Delete all scripts from `culture-society-series/`, write `README.md`
    - README includes: series ID, 4 curriculum IDs and titles, creation method, SQL queries, recreation context
    - _Requirements: 8.4, 15.1, 15.2, 15.3_

- [x] 15. Final checkpoint
  - Ensure all 16 curriculums exist in DB, all 4 series are in collection 279d6843 with correct ordering, all source scripts are deleted, and all 4 folders contain only README.md. Ask the user if questions arise.

## Notes

- Each curriculum script is ~500-800 lines with all hand-written Vietnamese/English content — no templates or string interpolation for learner-facing text
- The `validate(content)` function in each script checks structural properties (18 words, 5 sessions, activity order, title/description presence, no strip keys, vocab list correctness) before making the API call
- Orchestrator scripts take curriculum IDs as constants (pasted from curriculum script output)
- Follow the exact pattern from `health-wellness-series/create_nutrition.py` for script structure and `test-prep/toeic_create_series.py` for orchestrator structure
- All series descriptions must be under 255 characters (PostgreSQL varchar limit)
- Token is refreshed via `get_firebase_id_token(UID)` before each API call
