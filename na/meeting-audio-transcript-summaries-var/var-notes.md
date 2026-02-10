# Tóm tắt cuộc họp

## 1. Tổng quan cuộc họp

Cuộc họp tập trung phân tích VAR exposure (Value At Risk) trong năm 2025, đặc biệt là các trường hợp bất thường khi có payout nhưng không có FYP/FQP tương ứng. Team đang review chi tiết bonus contribution của các UM trong 12 tháng qua và xác định các nguyên nhân gây ra lệch lạc giữa production và payout, đặc biệt chú ý đến rủi ro tiềm ẩn từ GTF subsidy scheme.

## 2. Các điểm thảo luận chính

• **VAR exposure hiện tại**: 0.3M (con số nhỏ nhưng cần xem xét risk tiềm ẩn từ gaming behavior)

• **Phân tích trường hợp FYP = 0 nhưng vẫn có payout**: Tập trung vào 2 slide chính để identify các pattern bất thường

• **Ba nguyên nhân chính gây lệch FYP vs Payout**:
  - Defer payment (NAB, MLY agent MLY) - production cuối 2024 nhưng payout vào đầu 2025
  - Contest payout - cũng trả sau freelook period
  - Công thức tính FYP vs payout không match (FYP loại trừ UM direct reports, nhưng payout bao gồm override và leader activation)

• **GTF subsidy risk**: Đây là mối quan ngại lớn nhất do:
  - Tính trên net production (không cần pass freelook)
  - Không có claw back mechanism
  - Có thể bị abuse thông qua việc submit-cancel-resubmit liên tục cùng một đơn

## 3. Quyết định đã đưa ra

• Cần review kỹ hơn các case có phần trăm lớn tại mục 3.2 (UM + GTF subsidy)

• Phải xác định mức độ exposure từ GTF subsidy trong tổng VAR 0.33M

• Cần cân nhắc có đưa risk này vào proposal hay không

## 4. Action Items

• **Phân tích chi tiết GTF exposure**:
  - Xác định số lượng và phần trăm các UM GTF trong dataset
  - Tính mức độ VAR của các UM GTF
  - Đánh giá GTF subsidy đóng góp bao nhiêu % trong tổng 0.33M VAR

• **Review các case cụ thể**: Kiểm tra kỹ các trường hợp có UM + GTF subsidy payment với FYP = 0

• **Follow-up với BR team**: Có vẻ đã có discussion sáng nay, cần sync lại thông tin

## 5. Câu hỏi chưa giải quyết

• GTF subsidy risk có nên được include trong proposal không?

• Mức độ gaming thực tế từ GTF scheme có đáng lo ngại không?

• Làm thế nào để mitigate GTF abuse risk (submit-cancel loop) nếu không có claw back mechanism?

• Data từ buổi sáng (BR discussion) có insights gì bổ sung?

## 6. Số liệu/Dữ liệu quan trọng

• **VAR exposure**: 0.3M

• **Thời gian phân tích**: 12 tháng trong năm 2025

• **Freelook period**: 21 ngày

• **Ví dụ GTF abuse**: 100 VND submit/cancel liên tục, mỗi lần nhận 10% bonus (10 VND)

• **Thành phần defer payment**: NAB, MLY agent MLY payments

• **Ví dụ team structure**: 10 người (8 agents + 2 UMs), nếu 8 agents không bán nhưng 2 UMs bán → có override/leader activation payout nhưng không có FYP tương ứng
