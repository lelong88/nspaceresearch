# Implementation Plan: Insurance Payout Simulator

## Overview

Build a self-contained HTML/CSS/JS insurance payout simulator for Manulife's "Xanh Tương Lai" product. Implementation proceeds bottom-up: data layer first, then calculation engine, then UI rendering, then wiring and integration. All output files go in `output/insurance-payout-simulator/`. Tests use fast-check and Node.js test runner.

## Tasks

- [x] 1. Create data layer (`data.js`)
  - [x] 1.1 Create `output/insurance-payout-simulator/data.js` with all hardcoded constants
    - Define `FUNDS` array with all 9 fund objects (id, name, highRate, lowRate)
    - Define `INITIAL_FEE_RATES` object mapping contract year to fee percentage
    - Define `EARLY_TERMINATION_RATES` object mapping contract year to termination fee percentage
    - Define `MGMT_FEE` config object (baseMonthly, annualIncrease, maxMonthly)
    - Define `RISK_RATES` nested object keyed by gender then age (18–99)
    - Define `LOYALTY_MILESTONES` array [10, 15, 20]
    - Define `SA_INCREASE` config object (startYear, endYear, annualRate, maxCumulative)
    - Define `RIDERS` array with 3 rider objects (Lá Chắn Xanh, Dự Phòng Xanh, Hộ Vệ Xanh)
    - Define `DEFAULTS` object with default input values (age 30, female, 28570000 VND, 5 years, can-bang)
    - Export all constants via `module.exports` for testability, and attach to `window` for browser use
    - _Requirements: 1.6, 1.7, 3.1, 3.2, 3.3, 3.4, 7.1, 7.2, 7.3, 8.1, 11.3_

- [ ] 2. Implement core calculation functions (`app.js` — calculation engine)
  - [-] 2.1 Create `output/insurance-payout-simulator/app.js` with input handling functions
    - Implement `collectInputs()` — reads form values, looks up fund rates, returns InputParams object
    - Implement `validateInputs(params)` — validates age 18–60, premium ≥ 20M, returns {valid, errors[]}
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6_

  - [~] 2.2 Implement Sum Assured and fee calculation functions
    - Implement `calcSumAssuredSchedule(baseSA, maxYear)` — 10% annual increase years 2–6, max +50%, constant after
    - Implement `calcInitialFee(year, basicPremium)` — lookup from INITIAL_FEE_RATES, 0% for year 11+
    - Implement `calcManagementFee(year)` — min(45000 + (year-1)*2000, 70000) * 12
    - Implement `calcRiskFee(age, gender, sumAssured)` — RISK_RATES[gender][age] * sumAssured / 1000
    - Implement `calcLoyaltyBonus(year, ageAtYear, firstYearPremium)` — (ageAtMilestone/100) * firstYearPremium at milestones
    - _Requirements: 2.1, 2.2, 3.1, 3.2, 3.4, 8.1_

  - [~] 2.3 Implement projection engine and benefit functions
    - Implement `projectAccountValue(params)` — year-by-year projection for both high/low scenarios, up to 40 years or lapse
    - Implement `detectLapse(rows)` — returns first year where AV ≤ 0 or insufficient for fees, or null
    - Implement `calcDeathBenefit(accountValue, sumAssured)` — max(AV, SA)
    - Implement `calcTPDBenefit(accountValue, sumAssured, age)` — same as death benefit if age ≤ 75, null otherwise
    - Implement `formatVND(amount)` — format with dot separators and " VND" suffix
    - Export all functions via `module.exports` for testability, and attach to `window` for browser use
    - _Requirements: 4.1, 4.2, 4.3, 5.1, 6.1, 6.2, 6.3, 8.2, 8.3, 9.2_

- [ ] 3. Checkpoint — Verify calculation engine
  - Ensure all calculation functions are implemented and exported correctly. Ask the user if questions arise.

- [ ] 4. Set up test infrastructure and write property-based tests
  - [~] 4.1 Create `output/insurance-payout-simulator/tests/` directory with package.json for fast-check dependency
    - Create `package.json` with fast-check as a dependency
    - Provide instructions to run `npm install` in the tests directory
    - _Requirements: 11.1_

  - [~] 4.2 Write property test: Age input validation (Property 1)
    - **Property 1: Age input validation**
    - For any integer, validation accepts iff 18 ≤ age ≤ 60
    - **Validates: Requirements 1.2**

  - [~] 4.3 Write property test: Premium input validation (Property 2)
    - **Property 2: Premium input validation**
    - For any numeric value, validation accepts iff value ≥ 20,000,000
    - **Validates: Requirements 1.4**

  - [~] 4.4 Write property test: Sum Assured schedule correctness (Property 3)
    - **Property 3: Sum Assured schedule correctness**
    - Year 1 = base SA; years 2–6 increase by 10% of base each; max +50%; constant from year 7
    - **Validates: Requirements 2.1, 2.2**

  - [~] 4.5 Write property test: Initial fee schedule correctness (Property 4)
    - **Property 4: Initial fee schedule correctness**
    - Correct rate applied per year bracket (50%, 30%, 20%, 2%, 0%)
    - **Validates: Requirements 3.1**

  - [~] 4.6 Write property test: Management fee formula with cap (Property 5)
    - **Property 5: Management fee formula with cap**
    - Annual fee = min(45000 + (year-1)*2000, 70000) * 12
    - **Validates: Requirements 3.2**

  - [~] 4.7 Write property test: Early termination fee schedule (Property 6)
    - **Property 6: Early termination fee schedule correctness**
    - Correct rate per year bracket (90%, 50%, 30%, 20%, 10%, 0%)
    - **Validates: Requirements 3.3**

  - [~] 4.8 Write property test: Risk fee calculation (Property 7)
    - **Property 7: Risk fee calculation**
    - riskFee = RISK_RATES[gender][age] * sumAssured / 1000
    - **Validates: Requirements 3.4**

  - [~] 4.9 Write property test: Account value single-step formula (Property 8)
    - **Property 8: Account value single-step formula**
    - nextAV = prevAV * (1 + rate) + invested - riskFee - mgmtFee + loyaltyBonus
    - **Validates: Requirements 4.2, 8.3**

  - [~] 4.10 Write property test: Projection year count (Property 9)
    - **Property 9: Projection runs correct number of years**
    - Rows from year 1 to min(40, lapseYear), no rows beyond
    - **Validates: Requirements 4.1**

  - [~] 4.11 Write property test: Lapse detection correctness (Property 10)
    - **Property 10: Lapse detection correctness**
    - Lapse = first year where AV ≤ 0 or AV < riskFee + mgmtFee; null if none in 40 years
    - **Validates: Requirements 5.1**

  - [~] 4.12 Write property test: Death benefit (Property 11)
    - **Property 11: Death benefit is max of account value and sum assured**
    - deathBenefit = max(AV, SA)
    - **Validates: Requirements 6.1**

  - [~] 4.13 Write property test: TPD benefit age rule (Property 12)
    - **Property 12: TPD benefit follows age rule**
    - If age ≤ 75: TPD = max(AV, SA); if age > 75: TPD = null
    - **Validates: Requirements 6.2, 6.3**

  - [~] 4.14 Write property test: Rider premium (Property 13)
    - **Property 13: Rider premium equals total minus basic**
    - riderPremium = totalPremium - basicPremium
    - **Validates: Requirements 7.4**

  - [~] 4.15 Write property test: Loyalty bonus formula (Property 14)
    - **Property 14: Loyalty bonus formula**
    - bonus = (ageAtMilestone / 100) * firstYearPremium at years 10, 15, 20
    - **Validates: Requirements 8.1**

  - [~] 4.16 Write property test: Loyalty bonus forfeited on lapse (Property 15)
    - **Property 15: Loyalty bonus forfeited on lapse**
    - All milestones after lapse year yield zero bonus
    - **Validates: Requirements 8.2**

  - [~] 4.17 Write property test: VND formatting (Property 16)
    - **Property 16: VND currency formatting**
    - formatVND round-trips: removing dots and " VND" suffix recovers original number
    - **Validates: Requirements 9.2**

  - [~] 4.18 Write unit tests for calculation functions
    - Create `output/insurance-payout-simulator/tests/calculations.test.js`
    - Test default profile produces expected year-1 values
    - Test boundary ages (18, 60), boundary premium (20M exactly)
    - Test fee schedule year boundaries (year 5→6, year 10→11)
    - Test loyalty bonus at milestones with known values
    - Test lapse detection with known lapse and no-lapse scenarios
    - Test formatVND with specific values (0, 1000, 28570000)
    - _Requirements: 1.2, 1.4, 2.1, 3.1, 3.2, 4.2, 5.1, 6.1, 8.1, 9.2_

- [ ] 5. Checkpoint — Verify tests pass
  - Ensure all tests pass with `node --test output/insurance-payout-simulator/tests/`. Ask the user if questions arise.

- [ ] 6. Build HTML structure (`index.html`)
  - [~] 6.1 Create `output/insurance-payout-simulator/index.html`
    - Semantic HTML5 structure: header, main (two-column grid), footer
    - Input Panel section with form controls: age (number input), gender (select), basic premium (number input), payment duration (select), fund (select)
    - All labels, headings, placeholders, and descriptions in Vietnamese
    - Proper `<label>` with `for`/`id` associations for accessibility
    - Results Panel section with: projection table container, account value chart canvas, fee chart container, benefits & rider summary section
    - Link to `style.css` and load `data.js` before `app.js`
    - Set default values from `DEFAULTS` on form controls
    - Disclaimer footer in Vietnamese
    - _Requirements: 1.1, 1.3, 1.5, 1.6, 1.7, 7.1, 7.2, 7.3, 9.1, 10.2, 11.1, 11.2_

- [ ] 7. Build styles (`style.css`)
  - [~] 7.1 Create `output/insurance-payout-simulator/style.css`
    - CSS custom properties for brand colors (green #00a758, white, dark gray)
    - CSS Grid layout: two-column on desktop, single-column stacked on mobile
    - Media query at 768px breakpoint for responsive stacking
    - Input panel styling: form fields, labels, validation error styles (red border, red text)
    - Results panel styling: table with sticky header, horizontal scroll on mobile
    - Fee chart: CSS flex-based stacked bars
    - Canvas chart container sizing
    - Benefits and rider summary card styling
    - Color contrast ratios ≥ 4.5:1 for all text
    - Support for screen widths 375px to 1920px
    - _Requirements: 10.1, 10.2, 10.4_

- [ ] 8. Implement UI rendering and wiring in `app.js`
  - [~] 8.1 Add rendering functions to `app.js`
    - Implement `renderTable(projection)` — builds HTML table rows with year-by-year data, highlights lapse years with red background, shows Vietnamese column headers
    - Implement `renderAccountChart(projection)` — draws Canvas line chart with high/low scenario lines, axis labels in Vietnamese
    - Implement `renderFeeChart(projection)` — renders CSS stacked bar chart showing initial fee, management fee, risk fee per year
    - Implement `renderBenefits(projection)` — updates benefits section with death benefit, TPD benefit, rider summary, lapse warnings
    - _Requirements: 3.5, 3.6, 4.4, 4.5, 5.2, 5.3, 5.4, 6.4, 7.1, 7.2, 7.3, 7.4, 9.1, 9.2, 9.3_

  - [~] 8.2 Implement `recalculate()` and wire event listeners
    - Implement `recalculate()` — master function: collectInputs → validateInputs → projectAccountValue → render all
    - Show validation errors inline below fields when invalid; show placeholder message in results panel
    - Attach `input`/`change` event listeners to all form controls to trigger `recalculate()`
    - Call `recalculate()` on page load with default values
    - Ensure recalculation completes within 500ms without page reload
    - _Requirements: 10.3, 11.2_

- [ ] 9. Final checkpoint — Full integration verification
  - Ensure all tests pass. Verify the app loads correctly from file:// protocol with default values populated and results displayed. Ask the user if questions arise.

## Notes

- Tasks marked with `*` are optional and can be skipped for faster MVP
- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation
- Property tests validate universal correctness properties (Properties 1–16 from design)
- Unit tests validate specific examples and edge cases
- All output files go in `output/insurance-payout-simulator/`
- Tests go in `output/insurance-payout-simulator/tests/`
