# Requirements Document

## Introduction

Ứng dụng web mô phỏng kịch bản chi trả bảo hiểm cho sản phẩm "Xanh Tương Lai" (Phiên bản phí ổn định) của Manulife Việt Nam. Ứng dụng giúp khách hàng thay đổi các thông số đầu vào và xem kết quả mô phỏng giá trị tài khoản, quyền lợi bảo hiểm, và phí theo thời gian. Ứng dụng là file HTML/CSS/JS tĩnh, không cần backend, toàn bộ dữ liệu và logic được hardcode.

## Glossary

- **Simulator**: Ứng dụng web mô phỏng kịch bản chi trả bảo hiểm Xanh Tương Lai
- **Account_Value**: Giá trị tài khoản hợp đồng bảo hiểm tại một thời điểm
- **Sum_Assured**: Số tiền bảo hiểm (STBH) ban đầu
- **Basic_Premium**: Phí bảo hiểm cơ bản hàng năm
- **Initial_Fee**: Phí ban đầu tính theo % phí bảo hiểm cơ bản
- **Risk_Fee**: Phí rủi ro bảo hiểm, thay đổi theo tuổi, giới tính, nghề nghiệp
- **Management_Fee**: Phí quản lý hợp đồng hàng tháng
- **Early_Termination_Fee**: Phí hủy hợp đồng sớm
- **Loyalty_Bonus**: Thưởng duy trì hợp đồng tại các mốc năm thứ 10/15/20
- **Investment_Fund**: Quỹ đầu tư liên kết đơn vị mà khách hàng chọn
- **Return_Rate**: Tỷ suất lợi nhuận đầu tư (kịch bản cao hoặc thấp)
- **Lapse**: Tình trạng hợp đồng mất hiệu lực do giá trị tài khoản không đủ trả phí
- **Death_Benefit**: Quyền lợi tử vong (giá trị lớn hơn giữa Account_Value và Sum_Assured + giá trị tài khoản bổ sung)
- **TPD_Benefit**: Quyền lợi thương tật toàn bộ vĩnh viễn
- **Rider**: Sản phẩm bổ trợ đính kèm hợp đồng chính
- **Input_Panel**: Khu vực nhập liệu cho khách hàng thay đổi thông số
- **Results_Panel**: Khu vực hiển thị kết quả mô phỏng
- **Projection_Table**: Bảng dự phóng giá trị tài khoản theo năm
- **Fee_Chart**: Biểu đồ trực quan hóa cấu trúc phí

## Requirements

### Requirement 1: Customer Input Controls

**User Story:** As a customer, I want to change my personal details and plan parameters, so that I can see how different choices affect my insurance outcomes.

#### Acceptance Criteria

1. THE Simulator SHALL display an Input_Panel with fields for age (18-60), gender (male/female), Basic_Premium amount, payment duration (3 or 5 years), and Investment_Fund selection.
2. WHEN the customer changes the age field, THE Simulator SHALL accept integer values between 18 and 60 inclusive.
3. WHEN the customer changes the gender field, THE Simulator SHALL provide a selection between "Nam" (male) and "Nữ" (female).
4. WHEN the customer changes the Basic_Premium field, THE Simulator SHALL accept values in VND with a minimum of 20,000,000 VND.
5. WHEN the customer changes the payment duration, THE Simulator SHALL provide a selection between 3 years and 5 years.
6. WHEN the customer selects an Investment_Fund, THE Simulator SHALL display all 9 available funds: Bảo Toàn, Tích Lũy, Ổn Định, Cân Bằng, Phát Triển, Tăng Trưởng, Hưng Thịnh 2035, Hưng Thịnh 2040, Hưng Thịnh 2045.
7. THE Simulator SHALL set default values matching the example profile: female, age 30, Basic_Premium 28,570,000 VND, 5-year payment, Cân Bằng fund.

### Requirement 2: Sum Assured Calculation

**User Story:** As a customer, I want to see my Sum Assured amount and how it increases over time, so that I can understand my coverage level.

#### Acceptance Criteria

1. WHEN the customer submits input parameters, THE Simulator SHALL calculate the initial Sum_Assured based on the Basic_Premium and age/gender factors.
2. THE Simulator SHALL apply a 10% annual increase to Sum_Assured from contract year 2 through year 6, up to a maximum cumulative increase of 50%.
3. THE Simulator SHALL display the Sum_Assured value for each contract year in the Projection_Table.

### Requirement 3: Fee Structure Calculation and Display

**User Story:** As a customer, I want to understand all fees deducted from my premiums, so that I can see how much of my money is actually invested.

#### Acceptance Criteria

1. THE Simulator SHALL calculate Initial_Fee as follows: Year 1 at 50%, Year 2 at 30%, Year 3 at 20%, Year 4-5 at 20%, Year 6-10 at 2%, Year 11 onward at 0% of Basic_Premium.
2. THE Simulator SHALL calculate Management_Fee starting at 45,000 VND per month in 2025, increasing by 2,000 VND per year, with a maximum of 70,000 VND per month.
3. THE Simulator SHALL calculate Early_Termination_Fee as: Year 1-2 at 90%, Year 3 at 50%, Year 4 at 30%, Year 5 at 20%, Year 6 at 10%, Year 7 onward at 0% of Account_Value.
4. THE Simulator SHALL calculate Risk_Fee based on the customer's age, gender, and Sum_Assured using hardcoded rate tables.
5. THE Simulator SHALL display the Fee_Chart showing the breakdown of Initial_Fee, Management_Fee, and Risk_Fee for each contract year.
6. WHEN the customer views the fee section, THE Simulator SHALL show a visual bar or chart illustrating how each year's premium is split between fees and invested amount.

### Requirement 4: Account Value Projection

**User Story:** As a customer, I want to see my projected account value over time under different return scenarios, so that I can set realistic expectations.

#### Acceptance Criteria

1. WHEN the customer submits input parameters, THE Simulator SHALL calculate Account_Value for each year from year 1 through year 40 (or until Lapse).
2. THE Simulator SHALL compute Account_Value using the formula: previous Account_Value × (1 + Return_Rate) + invested premium − Risk_Fee − Management_Fee for each year.
3. THE Simulator SHALL display two projection scenarios: high Return_Rate and low Return_Rate based on the selected Investment_Fund.
4. THE Simulator SHALL display the Projection_Table with columns for: year, age, annual premium paid, Initial_Fee deducted, amount invested, Risk_Fee, Management_Fee, and Account_Value for both high and low scenarios.
5. THE Simulator SHALL display a line chart showing Account_Value over time for both high and low return scenarios.

### Requirement 5: Policy Lapse Detection

**User Story:** As a customer, I want to know when my policy might lapse under different scenarios, so that I can plan my finances accordingly.

#### Acceptance Criteria

1. WHEN the Account_Value drops below zero or is insufficient to cover Risk_Fee and Management_Fee, THE Simulator SHALL mark that year as the Lapse year.
2. THE Simulator SHALL highlight the Lapse year in the Projection_Table with a distinct visual indicator (red background or warning icon).
3. THE Simulator SHALL display a warning message stating the year and age at which the policy lapses for each scenario.
4. WHEN the policy does not lapse within 40 years, THE Simulator SHALL display a message confirming the policy remains active.

### Requirement 6: Death and TPD Benefit Display

**User Story:** As a customer, I want to see my death and TPD benefit amounts at any given year, so that I can understand my protection coverage.

#### Acceptance Criteria

1. THE Simulator SHALL calculate Death_Benefit for each year as the greater of Account_Value or Sum_Assured (with auto-increase applied).
2. THE Simulator SHALL calculate TPD_Benefit identical to Death_Benefit for ages up to 75.
3. WHEN the customer's age exceeds 75, THE Simulator SHALL display TPD_Benefit as not applicable.
4. THE Simulator SHALL display Death_Benefit and TPD_Benefit values in the Projection_Table or a dedicated benefits section.

### Requirement 7: Rider Benefits Summary

**User Story:** As a customer, I want to see a summary of my rider benefits, so that I can understand the full scope of my coverage.

#### Acceptance Criteria

1. THE Simulator SHALL display a Rider benefits summary section listing: Lá Chắn Xanh (Critical Illness) with 200M VND late-stage, 50M VND early-stage, and 50M VND special coverage.
2. THE Simulator SHALL display Dự Phòng Xanh (Hospital Cash) rider with 200M VND per day coverage.
3. THE Simulator SHALL display Hộ Vệ Xanh (Accident) rider with 250M VND coverage.
4. THE Simulator SHALL display the total annual rider premium as the difference between total premium (30,000,000 VND) and Basic_Premium.

### Requirement 8: Loyalty Bonus Calculation

**User Story:** As a customer, I want to understand the loyalty bonus structure, so that I can see potential bonuses at milestone years.

#### Acceptance Criteria

1. THE Simulator SHALL calculate Loyalty_Bonus at contract year 10, 15, and 20 as x% of the first year Basic_Premium, where x equals the customer's age at that anniversary.
2. WHEN the policy lapses before a Loyalty_Bonus milestone, THE Simulator SHALL indicate that the bonus is forfeited.
3. THE Simulator SHALL add the Loyalty_Bonus to the Account_Value in the year it is awarded.
4. THE Simulator SHALL display Loyalty_Bonus amounts in the Projection_Table at the applicable milestone years.

### Requirement 9: Vietnamese Language UI

**User Story:** As a Vietnamese customer, I want the entire interface in Vietnamese, so that I can understand all information without language barriers.

#### Acceptance Criteria

1. THE Simulator SHALL render all labels, headings, descriptions, tooltips, and messages in Vietnamese.
2. THE Simulator SHALL format currency values in VND format with thousand separators (e.g., 1.965.078.000 VND).
3. THE Simulator SHALL use Vietnamese terminology consistent with Manulife product documentation (e.g., "Số tiền bảo hiểm", "Phí bảo hiểm cơ bản", "Giá trị tài khoản").

### Requirement 10: Responsive and Accessible UI

**User Story:** As a customer using various devices, I want the simulator to work well on both desktop and mobile, so that I can access it anywhere.

#### Acceptance Criteria

1. THE Simulator SHALL render correctly on screen widths from 375px (mobile) to 1920px (desktop).
2. THE Simulator SHALL use a clean, modern visual design with clear section separation between Input_Panel, Results_Panel, Fee_Chart, and Rider summary.
3. WHEN the customer changes any input parameter, THE Simulator SHALL recalculate and update all results within 500 milliseconds without page reload.
4. THE Simulator SHALL use sufficient color contrast ratios for all text and interactive elements.

### Requirement 11: Self-Contained Deployment

**User Story:** As a distributor, I want the simulator to be a self-contained set of files with no external dependencies, so that I can share it easily with customers.

#### Acceptance Criteria

1. THE Simulator SHALL consist of HTML, CSS, and JavaScript files only, with no external CDN links, API calls, or backend dependencies.
2. THE Simulator SHALL function correctly when opened directly from the local file system (file:// protocol).
3. THE Simulator SHALL store all calculation data, rate tables, and fund information as hardcoded values within the JavaScript files.
