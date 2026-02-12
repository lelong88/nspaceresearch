# Tóm tắt cuộc họp

## 1. Tổng quan cuộc họp

Cuộc thảo luận nhanh về việc tính toán lại cost simulation cho MAC scheme. Hiện tại đang chuẩn bị proposal và cần update phần cost analysis để phản ánh tình huống mới: một sales leader có thể mở nhiều MAC (thay vì chỉ 1 MAC như trước). Cần đánh giá cost percentage trong scenario này và quyết định xem có cho phép hay không, mức độ cost nào có thể chấp nhận được.

## 2. Các điểm thảo luận chính

- **Tình huống mới**: Trước đây mỗi leader chỉ mở 1 MAC, nhưng giờ có thể có trường hợp 1 leader (DRD/AVP level) có nhiều MAC trong hệ thống của họ (5-6-7-8 MAC)
- **Hai phương pháp tính cost**:
  - **Cách 1 (phương pháp cũ)**: Tính cost dựa trên FYP target theo rank (SSM = 3 tỷ, SSM = 5 tỷ, DRD = 7 tỷ, v.v.)
  - **Cách 2 (phương pháp mới - đề xuất)**: Tính ngược từ minimum requirement - chỉ đạt đủ 1mAA (76 1mAA) × FYP per active average (4-trừ C52-trừ PI) → khoảng 2 tỷ+ FYP thực tế
- **Vấn đề dự đoán**: Với cách 2, cost percentage sẽ cao hơn vì FYP base thấp hơn nhiều so với target thông thường
- **Tác động business**: Về mặt kinh doanh, việc để leader giỏi mở nhiều MAC là hợp lý và không nên cấm, nhưng cần kiểm soát cost và biết mức độ chấp nhận được

## 3. Quyết định đã đưa ra

- Sẽ làm cost simulation theo **cả hai cách** để so sánh
- Ưu tiên làm file cost simulation cho MAC scheme trước hai công việc khác (SOP và activity management)
- Sẽ clean up và update file MAC cost hiện tại với các assumption mới (SMC mới, scheme adjustments)

## 4. Action Items

- **Người gọi (có thể là team member)**: 
  - Clean up file MAC cost hiện tại
  - Update assumptions mới (SMC, scheme changes)
  - Gửi file + viết hướng dẫn chi tiết cho chị Phương
  - Làm cost simulation theo cách 1 (phương pháp cũ của mình)

- **Chị Phương**: 
  - Nhận file và hướng dẫn chi tiết
  - Làm cost simulation theo cách 2 (phương pháp mới - tính từ minimum 1mAA requirement)
  - Hoặc có thể làm mới lại toàn bộ file nếu thấy cần thiết
  - Tạm hoãn: SOP và activity management (không gấp bằng)

## 5. Câu hỏi chưa giải quyết

- Cost percentage cụ thể sẽ cao đến mức nào trong scenario nhiều MAC?
- Mức cost nào là acceptable để company chấp nhận cho phép 1 leader mở nhiều MAC?
- Có cần set limit số lượng MAC mỗi leader được phép mở không?
- Nên áp dụng control mechanism gì để quản lý cost trong trường hợp này?

## 6. Số liệu/Dữ liệu quan trọng

- **1mAA requirement**: 76 1mAA (minimum để qualify cho MAC scheme)
- **FYP estimates theo rank**:
  - SSM: 3 tỷ VND
  - SSM (rank cao hơn): 5 tỷ VND  
  - DRD: 7 tỷ VND
- **FYP từ minimum requirement**: ~2 tỷ+ VND (76 1mAA × FYP per active, loại trừ 4-trừ C52-trừ PI)
- **Số lượng MAC trong scenario mới**: 5-8 MAC per leader (DRD/AVP level)
