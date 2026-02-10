# TÓM TẮT CUỘC HỌP

## 1. Tổng quan cuộc họp
Cuộc họp tập trung phân tích và đối chiếu dữ liệu back-test 2025 với forecast 2026 cho scheme compensation mới, đặc biệt là tác động lên VAR (Value at Risk) và số lượng GTF units có VAR > 0. Nhóm thảo luận phát hiện một số bất thường trong dữ liệu cần giải thích, đặc biệt là số lượng GTF units có VAR dương tăng đột biến trong khi agent compensation scheme không thay đổi.

## 2. Các điểm thảo luận chính

• **Làm rõ cấu trúc bảng phân tích:**
  - Bảng bên trái: Back-test 2025 (performance năm 2025 áp dụng scheme mới)
  - Bảng bên phải: Forecast 2026 (performance dự kiến 2026 với scheme mới)
  - Cả hai đều dùng scheme mới, chỉ khác performance/production

• **Phát hiện bất thường về số lượng GTF units:**
  - GTF units với VAR > 0 tăng từ 105 (2025) lên 124 (2026) — tăng ~20 units (~20%)
  - Non-MBA GTF tăng từ 102 lên 119 units
  - Điều này ngược với kỳ vọng: khi FYP tăng mà GTF compensation scheme không đổi, lẽ ra VAR/FYP ratio phải giảm → số units có VAR > 0 phải giảm, không phải tăng

• **Phân tích tổng thể VAR:**
  - Tổng số units có VAR > 0 giảm từ 391 xuống 306 — điều này hợp lý
  - Nhưng riêng GTF segment lại tăng — cần giải thích
  - Back-test cho thấy VAR tăng gấp 3 lần (từ 0.3 lên ~1.0 triệu USD) khi áp dụng scheme mới cho performance 2025

• **Giả thuyết giải thích:**
  - Production tăng → có thể nhiều GTF units nhảy rate/tier cao hơn
  - GTF có thể recruit nhiều new agents → tăng team size → thay đổi cơ cấu payout
  - Absolute payout tăng nhưng không tăng ngang FYP → VAR behavior khác nhau giữa các segments

## 3. Quyết định đã đưa ra

• Chưa có quyết định cuối cùng — cần phân tích sâu hơn trước khi kết luận

• Cần đi sâu vào chi tiết 119 GTF units (tăng từ 102) để hiểu tại sao chúng có VAR > 0 trong forecast 2026

## 4. Action Items

• **Phân tích chi tiết 119 GTF units non-MBA** (tăng từ 102 năm 2025):
  - Xem các units này thuộc compensation component nào
  - Kiểm tra agent compensation, UM compensation changes
  - Xác định yếu tố nào làm VAR của chúng tăng lên (new recruit activity, tier jump, etc.)

• **Giải thích nguyên nhân tổng units giảm từ 391 → 306:**
  - So sánh với giả thuyết: FYP tăng nhưng income không tăng tương ứng → VAR/FYP giảm

• **Review lại logic và số liệu:**
  - Đảm bảo phương pháp tính VAR nhất quán
  - Kiểm tra xem có thay đổi nào khác trong assumption không

## 5. Câu hỏi chưa giải quyết

• **Tại sao số lượng GTF units có VAR > 0 lại tăng 20% (từ 105 → 124) khi:**
  - GTF compensation scheme không thay đổi
  - FYP forecast tăng 35% (từ ~1,330 lên 1,787)
  - Logic thông thường: production tăng mạnh + compensation không đổi → VAR/FYP phải giảm → số units at-risk phải giảm?

• **Có units nào chuyển từ VAR âm (2025) sang VAR dương (2026) không?**
  - Nếu có thì nguyên nhân gì?
  - Có phải do production pattern thay đổi hay do đặc thù GTF financing/subsidy?

• **Agent compensation có thay đổi gì không?**
  - Xác nhận lại agent scheme có hoàn toàn giữ nguyên không
  - Có component nào tăng rate theo production threshold không?

## 6. Số liệu/Dữ liệu quan trọng

| Chỉ số | 2025 (Back-test) | 2026 (Forecast) | Thay đổi |
|--------|------------------|-----------------|----------|
| **Total units with VAR > 0** | 391 | 306 | -85 (-22%) |
| **GTF units with VAR > 0** | 105 | 124 | +19 (+18%) |
| **GTF non-MBA with VAR > 0** | 102 | 119 | +17 (+17%) |
| **FYP (tỷ VND)** | ~1,330 | 1,787 | +457 (+35%) |
| **VAR estimate (khi dùng scheme mới cho 2025)** | ~1.0 triệu USD | - | Gấp 3 lần baseline 0.3 triệu USD |

**Lưu ý quan trọng:**
- 124 GTF units chỉ có **4-5 units thuộc MBA**, phần lớn là non-MBA
- Trong 119 non-MBA GTF, hầu hết absolute cost đều tăng nhưng không tăng ngang tỷ lệ với FYP
- Hiện tượng này cần được giải thích rõ trước khi trình bày với leadership
