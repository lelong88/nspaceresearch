# Requirements Document

## Introduction

Website giới thiệu sản phẩm bảo hiểm "Xanh Tương Lai" (Phiên bản phí ổn định) của Manulife Việt Nam, hướng đến khách hàng tiềm năng. Website đơn giản hóa thông điệp sản phẩm bảo hiểm liên kết đơn vị (ILP) phức tạp bằng ngôn ngữ dễ hiểu, trực quan hóa hiệu quả, animation và các phương pháp hỗ trợ tương tác. Website là file HTML/CSS/JS tĩnh, single-page scrolling, không cần backend. Nội dung hoàn toàn bằng tiếng Việt.

## Glossary

- **Explainer_Site**: Website giới thiệu sản phẩm Xanh Tương Lai cho khách hàng tiềm năng
- **Hero_Section**: Khu vực đầu trang chứa headline, mô tả ngắn và nút hành động
- **Product_Overview**: Phần giải thích sản phẩm ILP là gì bằng ngôn ngữ đơn giản
- **Benefit_Section**: Phần trình bày quyền lợi chính của sản phẩm (tử vong/TTTBVV, tăng STBH, đáo hạn)
- **Rider_Section**: Phần trình bày các sản phẩm bổ trợ (Lá Chắn Xanh, Dự Phòng Xanh, Hộ Vệ Xanh)
- **Fund_Section**: Phần giới thiệu các quỹ đầu tư liên kết đơn vị
- **FAQ_Section**: Phần câu hỏi thường gặp dạng accordion
- **Glossary_Tooltip**: Tooltip hiển thị định nghĩa thuật ngữ bảo hiểm khi hover/tap
- **Scroll_Animation**: Hiệu ứng animation kích hoạt khi phần tử xuất hiện trong viewport
- **ILP**: Bảo hiểm liên kết đơn vị (Investment-Linked Policy)
- **STBH**: Số tiền bảo hiểm
- **TTTBVV**: Thương tật toàn bộ vĩnh viễn
- **Sum_Assured_Visualizer**: Biểu đồ trực quan hóa sự tăng trưởng STBH qua các năm
- **Fund_Comparison**: Bảng hoặc biểu đồ so sánh các quỹ đầu tư theo mức độ rủi ro
- **Compliance_Disclaimer**: Thông điệp tuân thủ pháp lý về rủi ro đầu tư
- **CTA_Section**: Khu vực kêu gọi hành động cuối trang
- **Navigation_Bar**: Thanh điều hướng cố định cho phép nhảy đến các phần trên trang
- **Jargon_Highlighter**: Hệ thống đánh dấu và giải thích thuật ngữ bảo hiểm chuyên ngành

## Requirements

### Requirement 1: Hero Section và Thông Điệp Chính

**User Story:** As a prospective customer, I want to immediately understand what Xanh Tương Lai offers, so that I can decide whether to continue reading.

#### Acceptance Criteria

1. THE Explainer_Site SHALL display a Hero_Section with the headline "Xanh Tương Lai – Phí ổn định, tương lai vững vàng" and a subheading explaining the dual protection-investment nature of the product.
2. THE Hero_Section SHALL display a primary CTA button labeled "Tính phí & nhận minh họa" and a secondary CTA button labeled "Nhận tư vấn miễn phí".
3. THE Hero_Section SHALL display 4 icon badges summarizing key benefits: bảo vệ tử vong/TTTBVV, tự động tăng STBH 10%/năm, riders linh hoạt, and danh mục quỹ đa dạng.
4. WHEN the page loads, THE Hero_Section SHALL animate the headline, badges, and CTA buttons into view using a staggered fade-in Scroll_Animation within 1.5 seconds.
5. THE Hero_Section SHALL include the Compliance_Disclaimer text "Lợi nhuận không đảm bảo, phụ thuộc thị trường" in a visible but non-intrusive position.

### Requirement 2: Giải Thích Sản Phẩm Bằng Ngôn Ngữ Đơn Giản

**User Story:** As a prospective customer unfamiliar with insurance, I want to understand what a unit-linked insurance product is in plain language, so that I can grasp the concept without prior knowledge.

#### Acceptance Criteria

1. THE Product_Overview SHALL explain ILP using a visual diagram showing two components: "Bảo vệ rủi ro" (protection) and "Đầu tư qua Quỹ" (investment) flowing from a single premium payment.
2. THE Product_Overview SHALL use an animated flow diagram that reveals each component sequentially as the user scrolls into the section.
3. THE Product_Overview SHALL explain the "phí ổn định" concept with a plain-language paragraph stating that total periodic premiums are designed to remain stable during the expected payment term.
4. THE Product_Overview SHALL include a Compliance_Disclaimer stating that account values and benefits are not guaranteed because they depend on investment performance.
5. WHEN the user hovers or taps on the term "bảo hiểm liên kết đơn vị", THE Jargon_Highlighter SHALL display a Glossary_Tooltip with a plain-language definition.

### Requirement 3: Thuật Ngữ Bảo Hiểm và Hệ Thống Glossary

**User Story:** As a prospective customer, I want insurance jargon explained inline, so that I can understand the content without searching for definitions elsewhere.

#### Acceptance Criteria

1. THE Explainer_Site SHALL identify and highlight all insurance jargon terms (including but not limited to: ILP, STBH, TTTBVV, phí rủi ro, giá trị tài khoản, quỹ liên kết đơn vị, NAV, đáo hạn, phí ban đầu) with a distinct visual style (dotted underline and accent color).
2. WHEN the user hovers (desktop) or taps (mobile) on a highlighted jargon term, THE Jargon_Highlighter SHALL display a Glossary_Tooltip containing a plain-language Vietnamese definition within 200 milliseconds.
3. THE Explainer_Site SHALL include a dedicated glossary section accessible via the Navigation_Bar listing all jargon terms with definitions in alphabetical order.
4. THE Glossary_Tooltip SHALL dismiss when the user moves the cursor away (desktop) or taps outside (mobile).
5. THE Jargon_Highlighter SHALL contain definitions for a minimum of 15 insurance-specific terms used throughout the Explainer_Site.

### Requirement 4: Quyền Lợi Chính – Trực Quan Hóa

**User Story:** As a prospective customer, I want to see the main benefits visualized clearly, so that I can understand what protection I receive.

#### Acceptance Criteria

1. THE Benefit_Section SHALL present three benefit cards: "Tử vong / TTTBVV", "Tăng STBH tự động", and "Đáo hạn" with icon, title, and plain-language description for each.
2. THE Benefit_Section SHALL display the death/TPD benefit explanation: chi trả giá trị cao hơn giữa STBH và giá trị tài khoản cơ bản, cộng giá trị tài khoản đóng thêm.
3. THE Benefit_Section SHALL include a Sum_Assured_Visualizer showing an animated bar chart or step chart illustrating the 10% annual STBH increase from year 2 through year 6.
4. WHEN the Sum_Assured_Visualizer scrolls into view, THE Explainer_Site SHALL animate the bars growing sequentially to show the cumulative increase.
5. THE Benefit_Section SHALL explain the maturity benefit with a plain-language note that the customer receives the full account value at maturity, with a Compliance_Disclaimer that the value may be lower than total premiums paid.
6. THE Benefit_Section SHALL mention the funeral advance of 30 million VND and the additional 10% thyroid cancer benefit (maximum 100 million VND) as supplementary details.
7. THE Benefit_Section SHALL explain the new family member STBH increase (+5% per member, maximum +25%) with a simple icon-based illustration.

### Requirement 5: Quyền Lợi Bổ Sung (Riders) – So Sánh Trực Quan

**User Story:** As a prospective customer, I want to compare the optional rider benefits side by side, so that I can decide which additional coverage suits my needs.

#### Acceptance Criteria

1. THE Rider_Section SHALL display three rider cards in a comparison layout: "Lá Chắn Xanh" (Bệnh lý nghiêm trọng), "Dự Phòng Xanh" (Trợ cấp nằm viện), and "Hộ Vệ Xanh" (Tai nạn).
2. THE Rider_Section SHALL display for Lá Chắn Xanh: giai đoạn cuối 100% STBH (trẻ em tối đa 1 tỷ, giới tính đặc biệt 125%), giai đoạn sớm and đặc biệt coverage, and the count of covered conditions (78+ bệnh giai đoạn cuối, 61 bệnh giai đoạn sớm, 4 bệnh đặc biệt).
3. THE Rider_Section SHALL display for Dự Phòng Xanh: ICU/Hồi sức tích cực at 300% STBH per day and khoa thường at 100% STBH per day.
4. THE Rider_Section SHALL display for Hộ Vệ Xanh: tử vong tai nạn at 100% STBH and a summary of thương tật nghiêm trọng, bộ phận, tổn thương nội tạng, gãy xương, and bỏng coverage.
5. WHEN each rider card scrolls into view, THE Explainer_Site SHALL animate the card with a slide-up Scroll_Animation.
6. THE Rider_Section SHALL use color-coded icons or badges to visually distinguish each rider category.

### Requirement 6: Quỹ Đầu Tư – Trực Quan Hóa Theo Rủi Ro

**User Story:** As a prospective customer, I want to understand the investment fund options and their risk levels, so that I can choose a fund matching my risk appetite.

#### Acceptance Criteria

1. THE Fund_Section SHALL display a Fund_Comparison visualization showing all 9 funds arranged on a risk spectrum from conservative (Bảo Toàn) to aggressive (Tăng Trưởng).
2. THE Fund_Section SHALL group funds into two categories: "Theo khẩu vị rủi ro" (Bảo Toàn, Tích Lũy, Ổn Định, Cân Bằng, Phát Triển, Tăng Trưởng) and "Theo mốc hưu trí" (Hưng Thịnh 2035, 2040, 2045).
3. THE Fund_Comparison SHALL use a visual scale (gradient bar, slider, or spectrum chart) with labels indicating risk level from "Thận trọng" to "Mạo hiểm".
4. WHEN the user hovers or taps on a fund name in the Fund_Comparison, THE Explainer_Site SHALL highlight that fund and display a brief description of the fund strategy.
5. THE Fund_Section SHALL include a Compliance_Disclaimer stating that fund values can increase or decrease and are not guaranteed.
6. WHEN the Fund_Section scrolls into view, THE Explainer_Site SHALL animate the risk spectrum visualization into view.

### Requirement 7: Ai Nên Chọn Sản Phẩm Này

**User Story:** As a prospective customer, I want to know if this product is suitable for me, so that I can self-assess before requesting a consultation.

#### Acceptance Criteria

1. THE Explainer_Site SHALL display a "Ai nên chọn?" section with 4 customer profile cards: families wanting protection and savings in one contract, long-term oriented individuals accepting market volatility, parents needing automatic STBH increase while children are young, and individuals wanting optional medical/critical illness/accident riders.
2. WHEN each profile card scrolls into view, THE Explainer_Site SHALL animate the card with a fade-in Scroll_Animation.
3. THE Explainer_Site SHALL use distinct icons for each customer profile to aid visual recognition.

### Requirement 8: Câu Hỏi Thường Gặp (FAQ) Tương Tác

**User Story:** As a prospective customer, I want to find answers to common questions quickly, so that I can resolve doubts without contacting an agent.

#### Acceptance Criteria

1. THE FAQ_Section SHALL display a minimum of 5 questions in an accordion format: "ILP là gì? Có đảm bảo lãi không?", "Vì sao cần xem nhiều kịch bản minh họa?", "Khi nào hợp đồng có thể mất hiệu lực?", "Có thể đổi Quỹ đầu tư không?", and "Tôi theo dõi NAV ở đâu?".
2. WHEN the user clicks or taps on a question, THE FAQ_Section SHALL expand the answer panel with a smooth slide-down animation within 300 milliseconds.
3. WHEN the user clicks or taps on an already-expanded question, THE FAQ_Section SHALL collapse the answer panel with a smooth slide-up animation.
4. THE FAQ_Section SHALL display only one expanded answer at a time, collapsing any previously open answer when a new question is selected.
5. THE FAQ_Section SHALL highlight jargon terms within answers using the Jargon_Highlighter system.

### Requirement 9: Scroll Animation và Micro-Interactions

**User Story:** As a prospective customer, I want engaging animations as I scroll through the page, so that the content feels dynamic and holds my attention.

#### Acceptance Criteria

1. THE Explainer_Site SHALL implement Scroll_Animation using Intersection Observer API to trigger animations when sections enter the viewport.
2. THE Explainer_Site SHALL support the following animation types: fade-in, slide-up, slide-in-left, slide-in-right, and scale-up for different content sections.
3. THE Explainer_Site SHALL animate each section only once (on first scroll into view) and retain the visible state afterward.
4. WHEN the user prefers reduced motion (prefers-reduced-motion media query), THE Explainer_Site SHALL disable all Scroll_Animations and display content immediately.
5. THE Explainer_Site SHALL apply hover micro-interactions on CTA buttons (scale and shadow change) and rider/benefit cards (subtle lift effect).

### Requirement 10: Navigation Cố Định và Smooth Scroll

**User Story:** As a prospective customer, I want to navigate quickly between sections, so that I can find the information I need without excessive scrolling.

#### Acceptance Criteria

1. THE Explainer_Site SHALL display a fixed Navigation_Bar at the top of the page with links to: Tổng quan, Quyền lợi, Riders, Quỹ đầu tư, FAQ, and Liên hệ.
2. WHEN the user clicks a Navigation_Bar link, THE Explainer_Site SHALL smooth-scroll to the corresponding section within 600 milliseconds.
3. WHILE the user scrolls, THE Navigation_Bar SHALL highlight the currently visible section link using an active indicator style.
4. WHEN the user scrolls past the Hero_Section, THE Navigation_Bar SHALL transition from transparent to a solid background color.
5. THE Navigation_Bar SHALL collapse into a hamburger menu on screen widths below 768px.

### Requirement 11: Kêu Gọi Hành Động (CTA) Cuối Trang

**User Story:** As a prospective customer who has read the full page, I want clear next steps, so that I can take action toward purchasing or learning more.

#### Acceptance Criteria

1. THE CTA_Section SHALL display three action options: "Tính phí & nhận minh họa", "Đặt lịch tư vấn 1:1", and "Tra cứu NAV & chọn Quỹ phù hợp".
2. THE CTA_Section SHALL present each action as a distinct card with icon, title, and brief description.
3. WHEN the CTA_Section scrolls into view, THE Explainer_Site SHALL animate the action cards with a staggered slide-up Scroll_Animation.
4. THE CTA_Section SHALL include the full Compliance_Disclaimer: "Kết quả Quỹ liên kết đơn vị có thể lỗ hoặc lãi, không được bảo đảm. Khách hàng hưởng toàn bộ kết quả đầu tư và chịu mọi rủi ro. Giá trị tài khoản có thể thấp hơn tổng phí đã đóng. Minh họa không phải là hợp đồng."

### Requirement 12: Responsive Design và Accessibility

**User Story:** As a prospective customer using a mobile phone, I want the website to display correctly and be accessible, so that I can read and interact with all content on any device.

#### Acceptance Criteria

1. THE Explainer_Site SHALL render correctly on screen widths from 375px (mobile) to 1920px (desktop) using responsive CSS.
2. THE Explainer_Site SHALL use a minimum font size of 16px for body text to ensure readability on mobile devices.
3. THE Explainer_Site SHALL use sufficient color contrast ratios (minimum 4.5:1 for normal text, 3:1 for large text) for all text elements.
4. THE Explainer_Site SHALL ensure all interactive elements (buttons, accordion triggers, tooltips) are accessible via keyboard navigation (Tab, Enter, Escape keys).
5. THE Explainer_Site SHALL include appropriate ARIA labels on interactive elements (accordion buttons, tooltip triggers, navigation links).
6. THE Explainer_Site SHALL use semantic HTML elements (nav, main, section, article, button) throughout the page structure.

### Requirement 13: Self-Contained Deployment

**User Story:** As a distributor, I want the website to be a self-contained set of files with no external dependencies, so that I can share it easily with customers.

#### Acceptance Criteria

1. THE Explainer_Site SHALL consist of HTML, CSS, and JavaScript files only, with no external CDN links, API calls, or backend dependencies.
2. THE Explainer_Site SHALL function correctly when opened directly from the local file system (file:// protocol).
3. THE Explainer_Site SHALL store all content, glossary definitions, and FAQ data as hardcoded values within the source files.
4. THE Explainer_Site SHALL use inline SVG icons or CSS-based icons instead of external icon font libraries.

### Requirement 14: Thiết Kế Thương Hiệu Manulife

**User Story:** As a Manulife representative, I want the website to reflect the Manulife Vietnam brand identity, so that customers recognize and trust the source.

#### Acceptance Criteria

1. THE Explainer_Site SHALL use a color palette based on Manulife brand colors: primary green (#00A758), dark green (#006B3F), white (#FFFFFF), and accent colors for highlights.
2. THE Explainer_Site SHALL use a clean, modern sans-serif font family consistent with professional financial services branding.
3. THE Explainer_Site SHALL include the product name "Xanh Tương Lai" and "Manulife Việt Nam" branding in the Navigation_Bar and footer.
4. THE Explainer_Site SHALL maintain a professional, trustworthy visual tone appropriate for financial products.
