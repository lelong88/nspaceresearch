# Implementation Plan: Economics University Curriculum

## Overview

Create 25 vi-en curriculums (5 series × 5 curriculums) for Vietnamese economics university students, organized in a new "Tiếng Anh Kinh Tế Đại Học" collection. Each curriculum: 18 vocabulary words, 5 sessions, bilingual content (Vietnamese UI, English reading passages), preintermediate-to-intermediate level. One standalone Python script per curriculum, one orchestrator for series/collection assembly, README documentation, then script cleanup.

## Tasks

- [x] 1. Create project directory and shared validation helper
  - [x] 1.1 Create `economics-university-curriculum/` working directory and `economics-university-curriculum/validate_curriculum.py` shared helper
    - Implement `validate_session_structure(content)` — checks exactly 5 sessions; sessions 1-3 have activity sequence [introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, vocabLevel3, reading, speakReading, readAlong, writingSentence] with vocabList of 6 words; session 4 has [introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, vocabLevel3, writingSentence] with vocabList of 18 words; session 5 has [introAudio, reading, speakReading, readAlong, writingParagraph, introAudio] referencing all 18 words
    - Implement `validate_activity_schema(activity)` — checks activityType (not type), title, description, data fields; activityType is one of 11 valid values; all content inside data object; no strip keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId)
    - Implement `validate_vocablist_integrity(content)` — checks viewFlashcards/speakFlashcards vocabList match within each session; all vocabList entries are lowercase strings; field name is vocabList not words
    - Implement `validate_top_level(content)` — checks contentTypeTags = [], title present, description present, preview.text present, learningSessions is array of length 5
    - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 12.1, 12.2, 12.3, 12.4, 12.5, 12.6, 12.7, 15.4_

  - [x] 1.2 Write property test for curriculum structure validity (Property 1)
    - **Property 1: Curriculum structure validity**
    - Verify any curriculum content JSON has exactly 5 sessions with correct activity sequences, vocabList sizes (6 per learning session, 18 for review/full-reading), and correct activity order per session type
    - **Validates: Requirements 3.1, 3.2, 3.3, 3.4, 3.5**

  - [x] 1.3 Write property test for activity schema compliance (Property 2)
    - **Property 2: Activity schema compliance**
    - Verify every activity has activityType/title/description/data, valid activityType value, no strip keys, contentTypeTags = [], all content inside data object
    - **Validates: Requirements 12.1, 12.2, 12.5, 12.6, 12.7, 3.6**

  - [x] 1.4 Write property test for vocabList integrity (Property 3)
    - **Property 3: VocabList integrity**
    - Verify viewFlashcards/speakFlashcards vocabList match within each session; all vocabList entries are lowercase strings
    - **Validates: Requirements 12.3, 12.4**

  - [x] 1.5 Write property test for no vocabulary duplication within a series (Property 4)
    - **Property 4: No vocabulary duplication within a series**
    - Verify the union of all vocabulary words across 5 curriculums in a series contains no duplicates (90 unique words per series)
    - **Validates: Requirements 4.8**

- [x] 2. Series A — Kinh Tế Vi Mô / Microeconomics (5 curriculums)
  - [x] 2.1 Create `create_micro_1_supply_demand.py` — Supply & Demand – Cung và Cầu
    - 18 words: supply, demand, equilibrium, surplus, shortage, quantity | elasticity, substitute, complement, shift, curve, price | allocate, ration, ceiling, floor, incentive, scarcity
    - 5 sessions, persuasive Vietnamese description (provocative_question tone), English reading passages about supply/demand fundamentals
    - Farewell tone: introspective guide
    - Include pre-upload validation using shared helper
    - Include duplicate-check SQL after creation
    - _Requirements: 1.1, 1.4, 2.1, 3.1-3.7, 4.1, 4.3, 4.8, 5.1-5.7, 6.1-6.6, 7.1, 7.2, 9.1-9.5, 10.1-10.5, 11.1-11.4, 12.1-12.7, 14.1-14.6, 15.1-15.4_

  - [x] 2.2 Create `create_micro_2_market_structures.py` — Market Structures – Cấu Trúc Thị Trường
    - 18 words: monopoly, oligopoly, competition, barrier, market, industry | differentiation, homogeneous, concentration, merger, antitrust, regulation | cartel, collusion, duopoly, contestable, dominance, deregulation
    - Persuasive Vietnamese description (vivid_scenario tone), English reading about market structures and competition
    - Farewell tone: warm accountability
    - _Requirements: 1.1, 1.4, 2.1, 3.1-3.7, 4.1, 4.3, 4.8, 5.1-5.7, 6.1-6.6, 7.1, 7.2, 9.1-9.5, 10.1-10.5, 11.1-11.4, 12.1-12.7, 14.1-14.6, 15.1-15.4_

  - [x] 2.3 Create `create_micro_3_consumer_choice.py` — Consumer Choice – Lựa Chọn Người Tiêu Dùng
    - 18 words: utility, preference, budget, constraint, marginal, rational | indifference, diminishing, maximize, consumption, satisfaction, income | opportunity, trade-off, optimal, welfare, expenditure, threshold
    - Persuasive Vietnamese description (bold_declaration tone), English reading about consumer choice and utility theory
    - Farewell tone: team-building energy
    - _Requirements: 1.1, 1.4, 2.1, 3.1-3.7, 4.1, 4.3, 4.8, 5.1-5.7, 6.1-6.6, 7.1, 7.2, 9.1-9.5, 10.1-10.5, 11.1-11.4, 12.1-12.7, 14.1-14.6, 15.1-15.4_

  - [x] 2.4 Create `create_micro_4_production_costs.py` — Production Costs – Chi Phí Sản Xuất
    - 18 words: variable, fixed, marginal, output, revenue, profit | economies, diseconomies, average, total, diminish, scale | productivity, efficiency, overhead, depreciation, capacity, breakeven
    - Persuasive Vietnamese description (empathetic_observation tone), English reading about production costs and firm decisions
    - Farewell tone: quiet awe
    - _Requirements: 1.1, 1.4, 2.1, 3.1-3.7, 4.1, 4.3, 4.8, 5.1-5.7, 6.1-6.6, 7.1, 7.2, 9.1-9.5, 10.1-10.5, 11.1-11.4, 12.1-12.7, 14.1-14.6, 15.1-15.4_

  - [x] 2.5 Create `create_micro_5_market_failure.py` — Market Failure – Thất Bại Thị Trường
    - 18 words: externality, subsidy, public, free-rider, commons, pollution | intervention, tax, quota, welfare, deadweight, loss | asymmetry, moral, adverse, regulation, corrective, spillover
    - Persuasive Vietnamese description (surprising_fact tone), English reading about market failure and externalities
    - Farewell tone: practical momentum
    - _Requirements: 1.1, 1.4, 2.1, 3.1-3.7, 4.1, 4.3, 4.8, 5.1-5.7, 6.1-6.6, 7.1, 7.2, 9.1-9.5, 10.1-10.5, 11.1-11.4, 12.1-12.7, 14.1-14.6, 15.1-15.4_

- [x] 3. Series B — Kinh Tế Vĩ Mô / Macroeconomics (5 curriculums)
  - [x] 3.1 Create `create_macro_1_gdp_indicators.py` — GDP & Indicators – GDP và Chỉ Số Kinh Tế
    - 18 words: gross, domestic, nominal, real, per capita, output | indicator, index, inflation, deflation, growth, contraction | aggregate, productivity, benchmark, quarterly, annual, forecast
    - Persuasive Vietnamese description (bold_declaration tone), English reading about GDP and economic indicators
    - Farewell tone: warm accountability
    - _Requirements: 1.1, 1.4, 2.1, 3.1-3.7, 4.1, 4.4, 4.8, 5.1-5.7, 6.1-6.6, 7.1, 7.3, 9.1-9.5, 10.1-10.5, 11.1-11.4, 12.1-12.7, 14.1-14.6, 15.1-15.4_

  - [x] 3.2 Create `create_macro_2_labor_markets.py` — Labor Markets – Thị Trường Lao Động
    - 18 words: unemployment, labor, workforce, participation, wage, hiring | structural, cyclical, frictional, seasonal, underemployment, layoff | vacancy, turnover, mobility, outsource, automation, retraining
    - Persuasive Vietnamese description (empathetic_observation tone), English reading about unemployment and labor markets
    - Farewell tone: quiet awe
    - _Requirements: 1.1, 1.4, 2.1, 3.1-3.7, 4.1, 4.4, 4.8, 5.1-5.7, 6.1-6.6, 7.1, 7.3, 9.1-9.5, 10.1-10.5, 11.1-11.4, 12.1-12.7, 14.1-14.6, 15.1-15.4_

  - [x] 3.3 Create `create_macro_3_fiscal_policy.py` — Fiscal Policy – Chính Sách Tài Khóa
    - 18 words: fiscal, budget, deficit, surplus, expenditure, revenue | taxation, progressive, regressive, stimulus, austerity, debt | bond, treasury, allocation, discretionary, mandatory, appropriation
    - Persuasive Vietnamese description (surprising_fact tone), English reading about fiscal policy and government spending
    - Farewell tone: practical momentum
    - _Requirements: 1.1, 1.4, 2.1, 3.1-3.7, 4.1, 4.4, 4.8, 5.1-5.7, 6.1-6.6, 7.1, 7.3, 9.1-9.5, 10.1-10.5, 11.1-11.4, 12.1-12.7, 14.1-14.6, 15.1-15.4_

  - [x] 3.4 Create `create_macro_4_monetary_policy.py` — Monetary Policy – Chính Sách Tiền Tệ
    - 18 words: monetary, interest, central, reserve, liquidity, credit | inflation, target, tighten, ease, transmission, benchmark | quantitative, yield, maturity, deposit, lending, overnight
    - Persuasive Vietnamese description (vivid_scenario tone), English reading about monetary policy and central banking
    - Farewell tone: introspective guide
    - _Requirements: 1.1, 1.4, 2.1, 3.1-3.7, 4.1, 4.4, 4.8, 4.9, 5.1-5.7, 6.1-6.6, 7.1, 7.3, 9.1-9.5, 10.1-10.5, 11.1-11.4, 12.1-12.7, 14.1-14.6, 15.1-15.4_

  - [x] 3.5 Create `create_macro_5_economic_growth.py` — Economic Growth – Tăng Trưởng Kinh Tế
    - 18 words: growth, development, investment, capital, infrastructure, innovation | convergence, divergence, sustainable, emerging, industrialization, urbanization | productivity, human, institutional, reform, liberalization, stagnation
    - Persuasive Vietnamese description (provocative_question tone), English reading about economic growth and development
    - Farewell tone: team-building energy
    - _Requirements: 1.1, 1.4, 2.1, 3.1-3.7, 4.1, 4.4, 4.8, 5.1-5.7, 6.1-6.6, 7.1, 7.3, 9.1-9.5, 10.1-10.5, 11.1-11.4, 12.1-12.7, 14.1-14.6, 15.1-15.4_

- [x] 4. Checkpoint — Series A & B complete
  - Ensure all 10 curriculums (Microeconomics + Macroeconomics) are created and validated. Ask the user if questions arise.

- [x] 5. Series C — Thương Mại Quốc Tế & Toàn Cầu Hóa / International Trade (5 curriculums)
  - [x] 5.1 Create `create_trade_1_theory.py` — Trade Theory – Lý Thuyết Thương Mại
    - 18 words: comparative, absolute, advantage, specialization, export, import | trade, surplus, deficit, balance, terms, gains | autarky, protectionism, liberalization, reciprocal, bilateral, multilateral
    - Persuasive Vietnamese description (empathetic_observation tone), English reading about comparative advantage and trade theory
    - Farewell tone: team-building energy
    - _Requirements: 1.1, 1.4, 2.1, 3.1-3.7, 4.1, 4.5, 4.8, 5.1-5.7, 6.1-6.6, 7.1, 7.4, 9.1-9.5, 10.1-10.5, 11.1-11.4, 12.1-12.7, 14.1-14.6, 15.1-15.4_

  - [x] 5.2 Create `create_trade_2_barriers.py` — Trade Barriers – Rào Cản Thương Mại
    - 18 words: tariff, quota, embargo, sanction, dumping, countervailing | barrier, non-tariff, standard, certification, licensing, restriction | retaliation, safeguard, anti-dumping, preferential, exemption, compliance
    - Persuasive Vietnamese description (provocative_question tone), English reading about tariffs, quotas, and trade barriers
    - Farewell tone: introspective guide
    - _Requirements: 1.1, 1.4, 2.1, 3.1-3.7, 4.1, 4.5, 4.8, 5.1-5.7, 6.1-6.6, 7.1, 7.4, 9.1-9.5, 10.1-10.5, 11.1-11.4, 12.1-12.7, 14.1-14.6, 15.1-15.4_

  - [x] 5.3 Create `create_trade_3_exchange_markets.py` — Exchange Markets – Thị Trường Ngoại Hối
    - 18 words: exchange, currency, appreciation, depreciation, floating, pegged | forex, spot, forward, hedge, speculation, volatility | arbitrage, devaluation, revaluation, convertible, reserve, intervention
    - Persuasive Vietnamese description (vivid_scenario tone), English reading about foreign exchange markets
    - Farewell tone: quiet awe
    - _Requirements: 1.1, 1.4, 2.1, 3.1-3.7, 4.1, 4.5, 4.8, 5.1-5.7, 6.1-6.6, 7.1, 7.4, 9.1-9.5, 10.1-10.5, 11.1-11.4, 12.1-12.7, 14.1-14.6, 15.1-15.4_

  - [x] 5.4 Create `create_trade_4_organizations.py` — Trade Organizations – Tổ Chức Thương Mại
    - 18 words: organization, treaty, agreement, negotiation, ratification, membership | dispute, resolution, panel, appellate, ruling, enforcement | accession, protocol, framework, consensus, sovereignty, harmonization
    - Persuasive Vietnamese description (surprising_fact tone), English reading about international trade organizations
    - Farewell tone: practical momentum
    - _Requirements: 1.1, 1.4, 2.1, 3.1-3.7, 4.1, 4.5, 4.8, 5.1-5.7, 6.1-6.6, 7.1, 7.4, 9.1-9.5, 10.1-10.5, 11.1-11.4, 12.1-12.7, 14.1-14.6, 15.1-15.4_

  - [x] 5.5 Create `create_trade_5_supply_chains.py` — Supply Chains – Chuỗi Cung Ứng Toàn Cầu
    - 18 words: logistics, supply, chain, procurement, inventory, warehouse | freight, customs, clearance, shipment, container, transit | disruption, resilience, diversification, nearshoring, traceability, optimization
    - Persuasive Vietnamese description (metaphor_led tone), English reading about global supply chains and logistics
    - Farewell tone: warm accountability
    - _Requirements: 1.1, 1.4, 2.1, 3.1-3.7, 4.1, 4.5, 4.8, 5.1-5.7, 6.1-6.6, 7.1, 7.4, 9.1-9.5, 10.1-10.5, 11.1-11.4, 12.1-12.7, 14.1-14.6, 15.1-15.4_

- [x] 6. Series D — Kế Toán & Tài Chính Doanh Nghiệp / Accounting & Corporate Finance (5 curriculums)
  - [x] 6.1 Create `create_accounting_1_financial_statements.py` — Financial Statements – Báo Cáo Tài Chính
    - 18 words: asset, liability, equity, revenue, expense, balance | income, statement, cash, flow, receivable, payable | accrual, depreciation, amortization, retained, comprehensive, disclosure
    - Persuasive Vietnamese description (surprising_fact tone), English reading about financial statements and reporting
    - Farewell tone: quiet awe
    - _Requirements: 1.1, 1.4, 2.1, 3.1-3.7, 4.1, 4.6, 4.8, 5.1-5.7, 6.1-6.6, 7.1, 7.5, 9.1-9.5, 10.1-10.5, 11.1-11.4, 12.1-12.7, 14.1-14.6, 15.1-15.4_

  - [x] 6.2 Create `create_accounting_2_cost_accounting.py` — Cost Accounting – Kế Toán Chi Phí
    - 18 words: cost, budget, variance, overhead, allocation, direct | indirect, standard, actual, absorption, marginal, contribution | breakeven, forecast, performance, benchmark, controllable, uncontrollable
    - Persuasive Vietnamese description (metaphor_led tone), English reading about cost accounting and budgeting
    - Farewell tone: practical momentum
    - _Requirements: 1.1, 1.4, 2.1, 3.1-3.7, 4.1, 4.6, 4.8, 5.1-5.7, 6.1-6.6, 7.1, 7.5, 9.1-9.5, 10.1-10.5, 11.1-11.4, 12.1-12.7, 14.1-14.6, 15.1-15.4_

  - [x] 6.3 Create `create_accounting_3_auditing.py` — Auditing – Kiểm Toán
    - 18 words: audit, compliance, assurance, material, misstatement, opinion | internal, external, sampling, evidence, procedure, engagement | fraud, detection, disclosure, independence, objectivity, skepticism
    - Persuasive Vietnamese description (provocative_question tone), English reading about auditing and compliance
    - Farewell tone: warm accountability
    - _Requirements: 1.1, 1.4, 2.1, 3.1-3.7, 4.1, 4.6, 4.8, 5.1-5.7, 6.1-6.6, 7.1, 7.5, 9.1-9.5, 10.1-10.5, 11.1-11.4, 12.1-12.7, 14.1-14.6, 15.1-15.4_

  - [x] 6.4 Create `create_accounting_4_capital_structure.py` — Capital Structure – Cấu Trúc Vốn
    - 18 words: capital, debt, equity, leverage, ratio, valuation | dividend, shareholder, bond, yield, maturity, coupon | weighted, optimal, restructuring, refinancing, dilution, buyback
    - Persuasive Vietnamese description (bold_declaration tone), English reading about capital structure and investment
    - Farewell tone: team-building energy
    - _Requirements: 1.1, 1.4, 2.1, 3.1-3.7, 4.1, 4.6, 4.8, 5.1-5.7, 6.1-6.6, 7.1, 7.5, 9.1-9.5, 10.1-10.5, 11.1-11.4, 12.1-12.7, 14.1-14.6, 15.1-15.4_

  - [x] 6.5 Create `create_accounting_5_corporate_governance.py` — Corporate Governance – Quản Trị Doanh Nghiệp
    - 18 words: governance, board, director, fiduciary, accountability, transparency | stakeholder, shareholder, proxy, charter, bylaw, oversight | whistleblower, ethics, conflict, disclosure, remuneration, succession
    - Persuasive Vietnamese description (empathetic_observation tone), English reading about corporate governance and ethics
    - Farewell tone: introspective guide
    - _Requirements: 1.1, 1.4, 2.1, 3.1-3.7, 4.1, 4.6, 4.8, 5.1-5.7, 6.1-6.6, 7.1, 7.5, 9.1-9.5, 10.1-10.5, 11.1-11.4, 12.1-12.7, 14.1-14.6, 15.1-15.4_

- [x] 7. Checkpoint — Series C & D complete
  - Ensure all 20 curriculums (Series A-D) are created and validated. Verify no vocabulary duplication within each series. Ask the user if questions arise.

- [x] 8. Series E — Marketing & Quản Trị / Marketing & Management (5 curriculums)
  - [x] 8.1 Create `create_marketing_1_market_research.py` — Market Research – Nghiên Cứu Thị Trường
    - 18 words: research, survey, sample, demographic, segment, target | qualitative, quantitative, focus, panel, respondent, bias | insight, trend, forecast, correlation, hypothesis, methodology
    - Persuasive Vietnamese description (vivid_scenario tone), English reading about market research and consumer behavior
    - Farewell tone: practical momentum
    - _Requirements: 1.1, 1.4, 2.1, 3.1-3.7, 4.1, 4.7, 4.8, 5.1-5.7, 6.1-6.6, 7.1, 7.6, 9.1-9.5, 10.1-10.5, 11.1-11.4, 12.1-12.7, 14.1-14.6, 15.1-15.4_

  - [x] 8.2 Create `create_marketing_2_branding.py` — Branding Strategy – Chiến Lược Thương Hiệu
    - 18 words: brand, positioning, differentiation, perception, loyalty, awareness | identity, equity, portfolio, extension, endorsement, licensing | rebranding, premium, niche, archetype, touchpoint, narrative
    - Persuasive Vietnamese description (bold_declaration tone), English reading about branding and product strategy
    - Farewell tone: team-building energy
    - _Requirements: 1.1, 1.4, 2.1, 3.1-3.7, 4.1, 4.7, 4.8, 4.9, 5.1-5.7, 6.1-6.6, 7.1, 7.6, 9.1-9.5, 10.1-10.5, 11.1-11.4, 12.1-12.7, 14.1-14.6, 15.1-15.4_

  - [x] 8.3 Create `create_marketing_3_leadership.py` — Leadership – Lãnh Đạo & Hành Vi Tổ Chức
    - 18 words: leadership, delegation, motivation, empowerment, accountability, vision | organizational, culture, hierarchy, collaboration, conflict, negotiation | transformational, situational, mentorship, succession, resilience, agility
    - Persuasive Vietnamese description (metaphor_led tone), English reading about organizational behavior and leadership
    - Farewell tone: introspective guide
    - _Requirements: 1.1, 1.4, 2.1, 3.1-3.7, 4.1, 4.7, 4.8, 5.1-5.7, 6.1-6.6, 7.1, 7.6, 9.1-9.5, 10.1-10.5, 11.1-11.4, 12.1-12.7, 14.1-14.6, 15.1-15.4_

  - [x] 8.4 Create `create_marketing_4_hr_management.py` — HR Management – Quản Trị Nhân Sự
    - 18 words: recruitment, retention, compensation, benefit, appraisal, onboarding | training, development, turnover, engagement, diversity, inclusion | compliance, grievance, termination, workforce, talent, pipeline
    - Persuasive Vietnamese description (provocative_question tone), English reading about human resource management
    - Farewell tone: warm accountability
    - _Requirements: 1.1, 1.4, 2.1, 3.1-3.7, 4.1, 4.7, 4.8, 5.1-5.7, 6.1-6.6, 7.1, 7.6, 9.1-9.5, 10.1-10.5, 11.1-11.4, 12.1-12.7, 14.1-14.6, 15.1-15.4_

  - [x] 8.5 Create `create_marketing_5_strategic_planning.py` — Strategic Planning – Hoạch Định Chiến Lược
    - 18 words: strategy, objective, mission, competitive, analysis, benchmark | swot, stakeholder, portfolio, diversification, acquisition, merger | disruption, innovation, scalability, sustainability, alignment, execution
    - Persuasive Vietnamese description (empathetic_observation tone), English reading about strategic planning and competitive analysis
    - Farewell tone: quiet awe
    - _Requirements: 1.1, 1.4, 2.1, 3.1-3.7, 4.1, 4.7, 4.8, 5.1-5.7, 6.1-6.6, 7.1, 7.6, 9.1-9.5, 10.1-10.5, 11.1-11.4, 12.1-12.7, 14.1-14.6, 15.1-15.4_

- [x] 9. Checkpoint — All 25 curriculums created
  - Ensure all 25 curriculums are created and validated. Verify no vocabulary duplication within each of the 5 series. Verify tone variety across all descriptions and farewells. Ask the user if questions arise.

- [x] 10. Create orchestrator script and assemble collection/series
  - [x] 10.1 Create `create_economics_university_series.py` orchestrator script
    - Create the "Tiếng Anh Kinh Tế Đại Học" collection via `curriculum-collection/create` with Vietnamese description
    - Create 5 series via `curriculum-series/create` with tone-assigned descriptions (≤255 chars each):
      - Series A: Kinh Tế Vi Mô (provocative_question), displayOrder 0
      - Series B: Kinh Tế Vĩ Mô (bold_declaration), displayOrder 1
      - Series C: Thương Mại Quốc Tế & Toàn Cầu Hóa (surprising_fact), displayOrder 2
      - Series D: Kế Toán & Tài Chính Doanh Nghiệp (empathetic_observation), displayOrder 3
      - Series E: Marketing & Quản Trị (vivid_scenario), displayOrder 4
    - Add curriculums to series via `curriculum-series/addCurriculum`
    - Set curriculum display orders (0-4 within each series) via `curriculum/setDisplayOrder`
    - Set series display orders via `curriculum-series/setDisplayOrder`
    - Add series to collection via `curriculum-collection/addSeriesToCollection`
    - Print all IDs (collection, series, curriculums) for README documentation
    - _Requirements: 1.1, 1.2, 1.3, 2.1-2.5, 8.1-8.7, 13.1-13.5, 14.7_

  - [x] 10.2 Run orchestrator script and record all IDs
    - _Requirements: 13.1-13.5, 14.7_

- [x] 11. Post-creation verification
  - [x] 11.1 Run duplicate-check SQL queries for all 25 curriculums
    - `SELECT id, title, created_at FROM curriculum WHERE title = '<title>' AND uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73' ORDER BY created_at` for each curriculum
    - Keep earliest, delete extras if duplicates found
    - _Requirements: 15.1, 15.2, 15.3_

  - [x] 11.2 Verify content integrity for all 25 curriculums
    - Check each curriculum via `curriculum/getOne`
    - Validate against CONTENT_CORRUPTION_RULES.md: correct activityType field names, vocabList not words, data inside data object, matching vocabLists for viewFlashcards/speakFlashcards in same session
    - Verify contentTypeTags = [] on all curriculums
    - Verify language = 'en' and userLanguage = 'vi'
    - _Requirements: 15.4, 3.6, 3.7, 12.1-12.7_

  - [x] 11.3 Verify series/collection assembly
    - Confirm all 5 series exist in the collection
    - Confirm each series has 5 curriculums
    - Confirm display orders are correct (series 0-4, curriculums 0-4 within each)
    - _Requirements: 13.1-13.5_

  - [x] 11.4 Cross-check vocabulary uniqueness within each series
    - For each of the 5 series, verify no duplicate words across its 5 curriculums (90 unique words per series)
    - _Requirements: 4.8_

- [x] 12. Final checkpoint — All verification complete
  - Ensure all 25 curriculums pass verification, all series/collection assembly is correct, no duplicates found. Ask the user if questions arise.

- [x] 13. Documentation and cleanup
  - [x] 13.1 Create `economics-university-curriculum/README.md`
    - Document: collection ID, all 5 series IDs, all 25 curriculum IDs and titles
    - Include creation method and recreation context
    - Include SQL queries for retrieval
    - Include full topic plan: which curriculums belong to which series, with display orders
    - Include vocabulary lists per curriculum
    - Include tone assignments (description tones and farewell tones)
    - _Requirements: 16.1, 16.3_

  - [x] 13.2 Delete all Python scripts from `economics-university-curriculum/`
    - Delete all `create_*.py` scripts and `validate_curriculum.py`
    - Only README.md remains in the directory
    - _Requirements: 16.2_

## Notes

- Tasks marked with `*` are optional and can be skipped for faster MVP
- Each curriculum task references specific requirements for traceability
- Checkpoints ensure incremental validation after logical groupings
- Property tests validate the 4 correctness properties from the design document
- All learner-facing text must be individually crafted — no templated content generation
- The design specifies Python as the implementation language
- All scripts use `firebase_token.get_firebase_id_token()` for auth and `https://helloapi.step.is` as API base
- Newly created curriculums remain private (no setPublic call)
