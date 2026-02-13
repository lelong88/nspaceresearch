# Tổng quan cuộc họp

Cuộc họp review tình hình VAR (Value at Risk) 2025 của agency, tập trung phân tích 260 UM units có VAR dương với tổng exposure 0.29% mil USD. Phân tích chi tiết performance profile, xác định các trường hợp đặc biệt và đánh giá mức độ rủi ro thực tế. Kết luận chung là tình hình VAR ổn định, phần lớn cases có risk thấp do các đặc điểm về cách tính toán compensation hơn là gaming behavior.

# Các điểm thảo luận chính

## 1. Overview VAR 2025
- **260 UM units** có VAR > 0, chiếm tổng exposure **0.29% mil USD**
- Phần lớn không phải high risk profile:
  - **63%** không phải GTF
  - **95%** không phải top agent (không phải MBA)
  - **87%** có VAR rất thấp (dưới **2,000 USD** trong last 12 months)

## 2. Deep-dive Analysis - Units với VAR < 2,000 USD
- Nhóm này chiếm **40%** total VAR
- Được đánh giá là **đủ thấp** để không encouraging gaming behavior
- Con số 2,000 USD/năm không đủ động lực để lợi dụng hệ thống

## 3. Analysis Units với VAR > 2,000 USD
### Trường hợp FYP > 0 và Payout > 0 (168 người)
**Phân loại theo P13:**
- **76 người:** P13 > 60% (performance tốt)
- **16 người:** P13 thấp, nhưng VAR < 2,000 USD
- **76 người:** Chưa có P13 (UM mới promote hoặc GTF dưới 12 tháng)

**Deep-dive 76 người có P13 tốt:**
- **71 người:** VAR thấp, team size nhỏ
- **5 người:** Chưa có P13 nhưng VAR > 4,000 USD
  - **Tất cả 5 người đều là GTF**
  - **Tất cả là top UM** (high risk profile)
  - **90% payout** đến từ UMC (31%) và GTF Subsidy (57%)
  - **Root cause:** Mismatch calculation giữa Direct Report (base cho UMC/GTF subsidy) vs Direct Team (base cho FYP calculation trong VAR)
  - **Kết luận:** Không phải risk thực tế, do technical calculation mismatch

## 4. Special Cases - Zero/Negative FYP Units (Slide 9)
**Profile:**
- **Tất cả** không phải top UM
- **Tất cả** không phải MBA
- **Hơn 50%** là GTF

**Root causes:**
- Defer payment từ năm trước làm payout dương
- Payout bao gồm override từ indirect team
- FYP chỉ tính direct team → mismatch
- **Phần lớn có VAR < 2,000 USD** → không đủ encouraging

# Quyết định đã đưa ra

1. **VAR 2025 review được đánh giá ổn định** - không có red flags nghiêm trọng
2. **Hai nhóm high VAR đều không phải gaming risk:**
   - Nhóm GTF top UM: do cách tính UMC/GTF subsidy (Direct Report) vs FYP (Direct Team)
   - Nhóm zero/negative FYP: do defer payment và override indirect team
3. Cần **combine và summarize lại** các findings từ slide 7 & 8

# Action Items

1. **Combine slides 7 & 8:**
   - Slide 7: Units với VAR > 0, FYP > 0, payout > 0, là GTF
   - Slide 8: Units với FYP Direct Team > 0, payout > 0, là GTF
   - **Action:** Tạo một slide summary cô đọng các thông số chính từ hai slides này
   - **Owner:** Chưa được assign cụ thể

# Câu hỏi chưa giải quyết

- Không có câu hỏi open được đề cập trong transcript này

# Số liệu/Dữ liệu quan trọng

## Key Metrics
| Metric | Value |
|--------|-------|
| **Total UM units với VAR > 0** | 260 units |
| **Total VAR exposure** | 0.29% mil USD |
| **Non-GTF units** | 63% |
| **Non-top agents (non-MBA)** | 95% |
| **Units với VAR < 2,000 USD** | 87% |
| **% total VAR từ units < 2,000 USD** | 40% |

## Detailed Breakdown (168 units: FYP > 0, Payout > 0)
| Category | Count | Notes |
|----------|-------|-------|
| **P13 > 60%** | 76 người | Performance tốt |
| **P13 thấp + VAR < 2,000 USD** | 16 người | Low risk |
| **Chưa có P13** | 76 người | UM mới hoặc GTF < 12 tháng |

## High VAR Sub-group (5 GTF top UM, VAR > 4,000 USD)
| Payout Component | % of Total Payout |
|------------------|-------------------|
| **UMC** | 31% |
| **GTF Subsidy** | 57% |
| **Combined (UMC + GTF Subsidy)** | 90% |

## Special Cases (Zero/Negative FYP)
- **50%+** là GTF
- **Phần lớn** có VAR < 2,000 USD
- **100%** không phải top UM
- **100%** không phải MBA
