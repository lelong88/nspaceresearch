# Implementation Plan: Xanh Tương Lai Explainer Website

## Overview

Build a single-file static explainer website (`output/xanh-tuong-lai-explainer/index.html`) for Manulife Vietnam's "Xanh Tương Lai" ILP product. All CSS and JS are embedded inline. Content is hardcoded as JS data objects. The site uses IntersectionObserver for scroll animations, an inline jargon tooltip system, FAQ accordion, fixed navigation, and animated charts — all with zero external dependencies.

## Tasks

- [x] 1. Create HTML skeleton with semantic structure and embedded CSS
  - [x] 1.1 Create `output/xanh-tuong-lai-explainer/index.html` with the full semantic HTML structure
    - Add `<!DOCTYPE html>`, `<html lang="vi">`, `<head>` with meta viewport, charset, title
    - Create all `<section>` elements with correct IDs: `hero`, `tong-quan`, `quyen-loi`, `riders`, `quy-dau-tu`, `ai-nen-chon`, `faq`, `lien-he`
    - Add `<nav id="main-nav">`, `<main>`, `<footer id="footer">`
    - Use semantic elements: `<nav>`, `<main>`, `<section>`, `<article>`, `<button>` throughout
    - _Requirements: 12.6, 13.1_

  - [x] 1.2 Embed CSS custom properties and base styles in `<style>` block
    - Define `:root` variables: `--color-primary: #00A758`, `--color-dark-green: #006B3F`, `--color-white: #FFFFFF`, spacing, typography tokens
    - Set body font-size minimum 16px, clean sans-serif font-family
    - Add CSS fallback values: `color: #00A758; color: var(--color-primary, #00A758)`
    - Ensure color contrast ratios meet 4.5:1 for normal text, 3:1 for large text
    - _Requirements: 14.1, 14.2, 12.2, 12.3_

  - [x] 1.3 Embed responsive CSS and animation keyframes
    - Add responsive breakpoints for 375px to 1920px
    - Add hamburger menu styles for screen widths below 768px
    - Define `@keyframes` for fade-in, slide-up, slide-in-left, slide-in-right, scale-up
    - Add `[data-animate]` base styles (opacity: 0, transform offsets) and animated-state classes
    - Add `@media (prefers-reduced-motion: reduce)` override setting all animation durations to 0s and showing elements immediately
    - Add hover micro-interactions on CTA buttons (scale, shadow) and cards (lift effect)
    - _Requirements: 12.1, 9.2, 9.4, 9.5, 10.5_

- [x] 2. Implement Hero Section and Navigation Bar
  - [x] 2.1 Build the Hero Section HTML content
    - Add headline "Xanh Tương Lai – Phí ổn định, tương lai vững vàng" and subheading about dual protection-investment
    - Add primary CTA button "Tính phí & nhận minh họa" and secondary CTA "Nhận tư vấn miễn phí"
    - Add 4 inline SVG icon badges: bảo vệ tử vong/TTTBVV, tự động tăng STBH 10%/năm, riders linh hoạt, danh mục quỹ đa dạng
    - Add compliance disclaimer "Lợi nhuận không đảm bảo, phụ thuộc thị trường"
    - Add `data-animate="fade-in"` with staggered `data-delay` attributes for headline, badges, CTAs
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5_

  - [x] 2.2 Build the Navigation Bar with links and hamburger menu
    - Add fixed nav with links to: Tổng quan, Quyền lợi, Riders, Quỹ đầu tư, FAQ, Liên hệ
    - Add "Xanh Tương Lai" and "Manulife Việt Nam" branding in nav
    - Add hamburger button with `aria-expanded` for mobile
    - Add ARIA labels on all nav links
    - _Requirements: 10.1, 10.5, 14.3, 12.5_

- [x] 3. Implement Product Overview and Benefits Sections
  - [x] 3.1 Build the Product Overview section
    - Create visual flow diagram showing "Phí bảo hiểm" splitting into "Bảo vệ rủi ro" and "Đầu tư qua Quỹ" using inline SVG or CSS
    - Add `data-animate` attributes for sequential reveal on scroll
    - Add "phí ổn định" explanation paragraph
    - Add compliance disclaimer about account values not being guaranteed
    - Wrap "bảo hiểm liên kết đơn vị" in `<span class="jargon" data-term="bảo hiểm liên kết đơn vị" tabindex="0" role="button" aria-describedby="tooltip">`
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5_

  - [x] 3.2 Build the Benefits section with 3 benefit cards and supplementary details
    - Render 3 benefit cards from BENEFITS data: Tử vong/TTTBVV, Tăng STBH tự động, Đáo hạn — each with inline SVG icon, title, description
    - Add death/TPD benefit explanation text
    - Add maturity benefit note with compliance disclaimer about value possibly being lower than premiums paid
    - Add funeral advance (30 million VND) and thyroid cancer benefit (10%, max 100 million VND) details
    - Add family member STBH increase illustration (+5% per member, max +25%) with icon-based visual
    - Add `data-animate="fade-in"` on cards
    - _Requirements: 4.1, 4.2, 4.5, 4.6, 4.7_

  - [x] 3.3 Build the STBH growth chart (Sum_Assured_Visualizer)
    - Create bar/step chart container with bars for years 1–6 using STBH_GROWTH data
    - Bars start at height 0 with CSS transitions
    - Add `data-animate` trigger for ChartAnimator to animate bars on scroll
    - Labels show year and percentage increase
    - _Requirements: 4.3, 4.4_

- [x] 4. Implement Riders, Funds, and Audience Sections
  - [x] 4.1 Build the Riders comparison section
    - Render 3 rider cards from RIDERS data in comparison layout
    - Display Lá Chắn Xanh details: giai đoạn cuối 100% STBH, trẻ em tối đa 1 tỷ, giới tính đặc biệt 125%, condition counts
    - Display Dự Phòng Xanh details: ICU 300% STBH/ngày, khoa thường 100% STBH/ngày
    - Display Hộ Vệ Xanh details: tử vong tai nạn 100% STBH, thương tật/bộ phận/nội tạng/gãy xương/bỏng
    - Use color-coded icons/badges per rider (distinct colors from RIDERS data)
    - Add `data-animate="slide-up"` on each card
    - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5, 5.6_

  - [x] 4.2 Build the Fund section with risk spectrum visualization
    - Create horizontal gradient bar from "Thận trọng" to "Mạo hiểm"
    - Position 9 fund markers along spectrum based on riskLevel
    - Group funds into "Theo khẩu vị rủi ro" (6 funds) and "Theo mốc hưu trí" (3 funds)
    - Add hover/tap interaction to highlight fund and show description
    - Add compliance disclaimer about fund values not being guaranteed
    - Add `data-animate` for spectrum animation on scroll
    - _Requirements: 6.1, 6.2, 6.3, 6.4, 6.5, 6.6_

  - [x] 4.3 Build the Target Audience section
    - Render 4 profile cards from AUDIENCE_PROFILES data with inline SVG icons and titles
    - Add `data-animate="fade-in"` on each card
    - _Requirements: 7.1, 7.2, 7.3_

- [x] 5. Checkpoint - Verify static content and layout
  - Ensure all sections render correctly with proper content, review in browser at 375px and 1920px widths. Ask the user if questions arise.

- [x] 6. Implement JavaScript data models and interactive components
  - [x] 6.1 Embed all JS data objects in `<script>` block
    - Add GLOSSARY (15+ terms), FAQ_ITEMS (5+ items), FUNDS (9 funds), RIDERS (3 riders), BENEFITS (3 benefits), STBH_GROWTH (6 years), AUDIENCE_PROFILES (4 profiles)
    - All data hardcoded, no external fetches
    - _Requirements: 13.3, 3.5, 8.1_

  - [x] 6.2 Implement ScrollAnimator component
    - Create `ScrollAnimator` with `init()`, `handleIntersection()`, `respectsReducedMotion()`
    - Use single IntersectionObserver with threshold 0.15
    - Query all `[data-animate]` elements, observe each
    - On intersection: add CSS class matching `data-animate` value, unobserve element (animate once)
    - Support `data-delay` attribute for staggered animations
    - If `prefers-reduced-motion: reduce`, add all animation classes immediately without observer
    - If IntersectionObserver unavailable, show all elements immediately (graceful degradation)
    - _Requirements: 9.1, 9.2, 9.3, 9.4_

  - [x] 6.3 Implement TooltipManager component
    - Create `TooltipManager` with `init()`, `show()`, `hide()`, `positionTooltip()`
    - Query all `[data-term]` elements, attach mouseenter/mouseleave (desktop) and click (mobile) listeners
    - Create single reusable tooltip DOM element
    - On trigger: look up definition in GLOSSARY, position tooltip near trigger, show with opacity transition
    - Handle viewport overflow by repositioning tooltip
    - If term not found in GLOSSARY, fail silently
    - Dismiss on mouseleave (desktop) or tap outside (mobile)
    - _Requirements: 3.2, 3.4_

  - [x] 6.4 Implement AccordionController component
    - Create `AccordionController` with `init()`, `toggle()`, `collapse()`, `expand()`
    - Query all `.accordion-trigger` buttons, attach click and keydown (Enter, Space) listeners
    - Single-open behavior: expanding one collapses any other open item
    - Animate panel height via max-height transition (300ms)
    - Update `aria-expanded` attribute on toggle
    - Handle rapid clicks by checking current state before toggling
    - _Requirements: 8.2, 8.3, 8.4_

  - [x] 6.5 Implement NavController component
    - Create `NavController` with `init()`, `scrollToSection()`, `updateActiveLink()`, `updateNavBackground()`, `toggleHamburger()`
    - Smooth scroll to section on nav link click (~600ms)
    - Track visible section with IntersectionObserver, update active nav link
    - Transition nav background from transparent to solid after scrolling past hero
    - Toggle hamburger menu with `aria-expanded` update, close on link click
    - _Requirements: 10.2, 10.3, 10.4, 10.5_

  - [x] 6.6 Implement ChartAnimator component
    - Create `ChartAnimator` with `initSTBHChart()`, `animateSTBHBars()`, `initFundSpectrum()`, `animateFundSpectrum()`
    - STBH chart: animate bars sequentially with 200ms staggered delays using CSS transitions
    - Fund spectrum: animate gradient bar width 0→100%, then fade in fund markers sequentially
    - Triggered by ScrollAnimator when chart containers enter viewport
    - _Requirements: 4.4, 6.6_

- [x] 7. Implement FAQ section and Glossary page section
  - [x] 7.1 Build the FAQ accordion HTML from FAQ_ITEMS data
    - Render FAQ items with `<button aria-expanded="false" aria-controls="faq-panel-N">` and `<div id="faq-panel-N" role="region">`
    - Highlight jargon terms within FAQ answers using `<span class="jargon" data-term="...">` markup
    - Wire up AccordionController on DOMContentLoaded
    - _Requirements: 8.1, 8.5, 12.5_

  - [x] 7.2 Build the dedicated Glossary section in footer area
    - Render all GLOSSARY terms with definitions in alphabetical order (Vietnamese locale sort)
    - Make section accessible via Navigation_Bar link
    - _Requirements: 3.3_

- [x] 8. Implement CTA section, footer, and jargon highlighting pass
  - [x] 8.1 Build the CTA section
    - Render 3 action cards: "Tính phí & nhận minh họa", "Đặt lịch tư vấn 1:1", "Tra cứu NAV & chọn Quỹ phù hợp" — each with inline SVG icon, title, description
    - Add full compliance disclaimer text
    - Add `data-animate="slide-up"` with staggered delays on cards
    - _Requirements: 11.1, 11.2, 11.3, 11.4_

  - [x] 8.2 Build the footer with branding
    - Add "Xanh Tương Lai" and "Manulife Việt Nam" branding
    - Link to glossary section
    - _Requirements: 14.3_

  - [x] 8.3 Apply jargon highlighting across all sections
    - Ensure all insurance jargon terms throughout the page (including FAQ answers) are wrapped in `<span class="jargon" data-term="..." tabindex="0" role="button" aria-describedby="tooltip">`
    - Apply dotted underline and accent color styling
    - Verify minimum 15 distinct terms are highlighted
    - _Requirements: 3.1, 3.5_

- [x] 9. Wire all components together and initialize on DOMContentLoaded
  - [x] 9.1 Add initialization script
    - On `DOMContentLoaded`: initialize ScrollAnimator, TooltipManager, AccordionController, NavController, ChartAnimator in correct order
    - Ensure all components are wired: ScrollAnimator triggers ChartAnimator, TooltipManager handles all jargon spans, NavController manages nav state
    - Verify keyboard accessibility: Tab through all interactive elements, Enter/Space activates buttons and accordion triggers, Escape closes tooltips
    - _Requirements: 9.1, 12.4, 12.5_

- [x] 10. Checkpoint - Full integration verification
  - Ensure all interactive features work: scroll animations trigger once, tooltips show/hide correctly, FAQ accordion single-open behavior, nav smooth scroll and active highlighting, charts animate on scroll. Ensure all tests pass, ask the user if questions arise.

- [ ] 11. Set up test infrastructure and write unit tests
  - [x] 11.1 Create test configuration and setup files
    - Create `output/xanh-tuong-lai-explainer/tests/` directory
    - Set up package.json with jest/vitest and fast-check dependencies
    - Create test setup file that loads index.html into jsdom
    - _Requirements: 13.1_

  - [ ]* 11.2 Write unit tests for static content and structure
    - Test Hero section: headline text, 2 CTA buttons, 4 badges, disclaimer text (Req 1.1–1.5)
    - Test Product Overview: ILP diagram elements, "phí ổn định" paragraph, disclaimer (Req 2.1, 2.3, 2.4)
    - Test Glossary minimum count: `Object.keys(GLOSSARY).length >= 15` (Req 3.5)
    - Test Benefit cards: 3 cards, death/TPD text, maturity text, funeral advance, thyroid cancer details (Req 4.1, 4.2, 4.5, 4.6)
    - Test Rider cards: 3 cards with correct details per rider (Req 5.1–5.4)
    - Test Fund spectrum labels and disclaimer (Req 6.3, 6.5)
    - Test Target audience: 4 profile cards (Req 7.1)
    - Test FAQ: >= 5 items with correct questions (Req 8.1)
    - Test Navigation structure: nav links, hamburger (Req 10.1, 10.5)
    - Test CTA: 3 action cards, full compliance disclaimer (Req 11.1, 11.4)
    - Test Semantic HTML: presence of `<nav>`, `<main>`, `<section>`, `<button>` (Req 12.6)
    - Test Font size >= 16px (Req 12.2)
    - Test No external dependencies: no fetch/XMLHttpRequest in source (Req 13.3)
    - Test Brand colors: CSS custom properties, font-family, branding text (Req 14.1–14.3)
    - _Requirements: 1.1–1.5, 2.1, 2.3, 2.4, 3.5, 4.1, 4.2, 4.5, 4.6, 5.1–5.4, 6.3, 6.5, 7.1, 8.1, 10.1, 10.5, 11.1, 11.4, 12.2, 12.6, 13.3, 14.1–14.3_

- [ ] 12. Write property-based tests with fast-check
  - [ ]* 12.1 Write property test for jargon highlighting
    - **Property 1: Jargon terms are highlighted throughout the page**
    - **Validates: Requirements 3.1, 8.5**

  - [ ]* 12.2 Write property test for tooltip definitions
    - **Property 2: Tooltip displays correct definition for any term**
    - **Validates: Requirements 3.2**

  - [ ]* 12.3 Write property test for glossary alphabetical order
    - **Property 3: Glossary section is alphabetically ordered**
    - **Validates: Requirements 3.3**

  - [ ]* 12.4 Write property test for tooltip dismissal
    - **Property 4: Tooltip dismisses on leave/tap-outside**
    - **Validates: Requirements 3.4**

  - [ ]* 12.5 Write property test for STBH growth calculation
    - **Property 5: STBH growth calculation is correct**
    - Generate random base amounts and years 2–6, verify `base × 1.1^(N-1)`
    - **Validates: Requirements 4.3**

  - [ ]* 12.6 Write property test for family STBH increase cap
    - **Property 6: Family member STBH increase is capped correctly**
    - Generate random non-negative integers, verify `min(N×5, 25)`
    - **Validates: Requirements 4.7**

  - [ ]* 12.7 Write property test for distinct rider colors
    - **Property 7: Each rider has a distinct color**
    - **Validates: Requirements 5.6**

  - [ ]* 12.8 Write property test for fund risk ordering
    - **Property 8: Funds are ordered by risk level on the spectrum**
    - **Validates: Requirements 6.1**

  - [ ]* 12.9 Write property test for fund category grouping
    - **Property 9: Funds are grouped into correct categories**
    - **Validates: Requirements 6.2**

  - [ ]* 12.10 Write property test for fund hover description
    - **Property 10: Fund hover/tap shows correct description**
    - **Validates: Requirements 6.4**

  - [ ]* 12.11 Write property test for FAQ toggle round-trip
    - **Property 11: FAQ accordion toggle round-trip**
    - **Validates: Requirements 8.2, 8.3**

  - [ ]* 12.12 Write property test for FAQ single-open invariant
    - **Property 12: FAQ single-open invariant**
    - **Validates: Requirements 8.4**

  - [ ]* 12.13 Write property test for animation type application
    - **Property 13: All animation types are applied correctly**
    - **Validates: Requirements 9.2**

  - [ ]* 12.14 Write property test for animate-once idempotence
    - **Property 14: Animate-once idempotence**
    - **Validates: Requirements 9.3**

  - [ ]* 12.15 Write property test for nav link scroll target
    - **Property 15: Nav link scrolls to correct section**
    - **Validates: Requirements 10.2**

  - [ ]* 12.16 Write property test for active nav link
    - **Property 16: Active nav link matches visible section**
    - **Validates: Requirements 10.3**

  - [ ]* 12.17 Write property test for CTA card fields
    - **Property 17: CTA cards contain all required fields**
    - **Validates: Requirements 11.2**

  - [ ]* 12.18 Write property test for color contrast
    - **Property 18: Color contrast meets WCAG thresholds**
    - **Validates: Requirements 12.3**

  - [ ]* 12.19 Write property test for keyboard accessibility
    - **Property 19: All interactive elements are keyboard accessible**
    - **Validates: Requirements 12.4**

  - [ ]* 12.20 Write property test for ARIA attributes
    - **Property 20: All interactive elements have ARIA attributes**
    - **Validates: Requirements 12.5**

  - [ ]* 12.21 Write property test for no external URLs
    - **Property 21: No external resource URLs**
    - **Validates: Requirements 13.1, 13.4**

- [x] 13. Final checkpoint - Complete verification
  - Ensure all tests pass, verify the site works on file:// protocol, check responsive layout at 375px and 1920px, confirm all 14 requirements are covered. Ask the user if questions arise.

## Notes

- Tasks marked with `*` are optional and can be skipped for faster MVP
- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation
- Property tests validate universal correctness properties from the design document
- Unit tests validate specific examples and edge cases
- All output goes to `output/xanh-tuong-lai-explainer/`
- Single `index.html` file with all CSS/JS embedded inline
