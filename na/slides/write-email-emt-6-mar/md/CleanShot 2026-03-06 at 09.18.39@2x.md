# MAC Activity Requirements for Service Fee Payment

![Source](../images/CleanShot 2026-03-06 at 09.18.39@2x.png)

## I. Background:

Theo Luật bảo hiểm mới và phạm vi dịch vụ trong hợp đồng dịch vụ có đề cập đến việc SM hỗ trợ đội ngũ hoạt động thì việc hỗ trợ hoạt động này phải có bằng chứng thể hiện, do đó sau khi xem xét, working team đề xuất sử dụng các hoạt động được tạo bởi SM tương ứng với phạm vi dịch vụ để áp dụng vào chi trả phí dịch vụ dành cho SM, bao gồm:

Quản lý hoạt động tuyển dụng, đào tạo, hỗ trợ kinh doanh: lấy kết quả Hội thảo tuyển dụng (COP), Đội ngũ chuyên cần (DA) và Đào tạo (Training)

Theo đó kết quả ghi nhận các hoạt động này sẽ được lấy dữ liệu từ ứng dụng M-PA

## II. Áp dụng:

### A. Đối với PSM+:

**1. Danh sách các khoản chi trả phí dịch vụ có áp dụng điều kiện hoạt động:**

a) Đối với compensation/monthly allowance (tel, taxi...): system tính và áp dụng các điều kiện hoạt động của **tháng** chi trả **khoản phí dịch vụ**.

**Lưu ý:**

- Thưởng tháng lấy kết quả hoạt động của đúng tháng đó,
- Thưởng quý lấy kết quả hoạt động của tháng cuối quý
- Thưởng năm tính toán và chi trả ở kỳ thu nhập tháng 4 hằng năm, sử dụng kết quả hoạt động của tháng 4

b) Đối với các khoản benefit tính toán manual (laptop, healthcare, top SM..): áp dụng điều kiện hoạt động của **tháng trước tháng** chi trả **khoản phí dịch vụ.**

c) Đối với các chương trình thi đua: áp dụng điều kiện hoạt động riêng theo từng thi đua

   i. Contest cash, gift tặng thông qua contest: **áp dụng** KQ hoạt động của tháng thi đua

   ii. Cash advance trên NR, UM: trên memo có yêu cầu SM phải đăng ký chương trình, có thể dùng để giải thích là có hoạt động nhưng lý do này chưa strong, cần trao đổi với lại FA xem có phù hợp hay không hay phải áp điều kiện cụ thể. **TBC**

---

iii. Trip: được định nghĩa là các hội nghị đào tạo do công ty tổ chức và SM cũng không chịu PIT nên **không áp dụng** điều kiện hoạt động

iv. Meeting/training event: đã được xem là hoạt động kinh doanh rồi nên **không áp dụng**

v. Gift tặng thông qua sales activity: **không áp dụng**

vi. M-shop: chưa chốt quy trình với FA và không key phí dịch vụ của SM, chỉ key thuế hoặc thu hồi nên **không áp dụng**

vii. COP/CS budget: trong memo đã có yêu cầu tạo tối thiểu 2 COP/CS và sau đó đem hóa đơn và claim: **không áp dụng**

**2. Thời gian áp dụng:** áp dụng từ tháng 3/2026. Hiện tại working team đã clear rule xong, đang UAT và sẵn sàng checking.

**3. Chi tiết cách ghi nhận hoạt động trên M-PA:** áp dụng activity cho các chi trả cho SM/HKD theo HĐ dịch vụ

| Event type | Activity type code recorded in system |
|---|---|
| COP | COP |
| DA workshop | WEEK_MEETING |
| Training | Sale_training, Agency_meeting, Week_meeting |

| Directly created by | SM-SSM | DRD-RD-SRD | AVP+ |
|---|---|---|---|
| # COP or # Training or Diligent Agent WS (DA) | 2 | 4 | 6 |
| Must include | 1 COP, 1 DA | 1 COP, 1 DA | 1 COP, 2 training |

**Rule:**

- Lấy các event có start date được tạo trong tháng và cut-off data 24h00 1 day before month end (ME-1) và lấy Status = Published or pending acceptance or completed

*Page 1 of 7 | 1856 words*
