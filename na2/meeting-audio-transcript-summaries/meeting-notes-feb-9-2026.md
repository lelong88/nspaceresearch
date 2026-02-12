# Tóm tắt cuộc họp: MAC Scheme Big MAC & Cost Simulation

## 1. Tổng quan cuộc họp

Cuộc họp tập trung vào việc thiết kế và tính toán cost simulation cho **Big MAC scheme** (bổ sung vào Normal/Small MAC đã pilot 2025). Team thảo luận cách approach để tính cost, xác định FYP base targets, xử lý các sensitivity scenarios, và đặc biệt là vấn đề **potential abuse** khi một leader mở nhiều MAC trong cùng một nhánh. Ngoài ra còn bàn về competitor analysis và phân công công việc.

## 2. Các điểm thảo luận chính

### A. Methodology cho Cost Simulation

**Hai cách tiếp cận được đề xuất:**

- **Cách 1 (Conservative/Optimize-first approach)**: Dựa trên office size → derive ngược lại FYP target tối thiểu để survive → đó là base scenario, sau đó mới làm sensitivity scenarios (higher/lower FYP). Ví dụ: văn phòng 150m² cần 60M VND guarantee/tháng → cần ~9-10 tỷ FYP để self-sustain về dài hạn (8% FYP phải cover được 60M).

- **Cách 2 (Traditional approach - được chọn)**: Giữ phương pháp như Normal MAC hiện tại - base trên rank targets (SM = 3 tỷ, DRD = 7-10 tỷ), sau đó làm sensitivity scenarios bao gồm cả trường hợp "optimize" (leader chỉ làm đủ để maximize guarantee mà không grow thêm).

### B. FYP Base Targets

| MAC Type | Target Rank | FYP Base Estimate |
|----------|-------------|-------------------|
| Small MAC | SM/SSM | 3-5 tỷ |
| Big MAC | DRD+ | 7-10 tỷ |

- Office size 150m² (Big MAC) với 8% FYP + 60M guarantee → cần ~9-10 tỷ để break-even về dài hạn
- Nhưng sẽ approach từ rank-based targets trước (7-10 tỷ cho DRD), sau đó test scenarios thấp hơn

### C. Vấn đề Potential Abuse - Multiple MACs

**Tình huống được quan ngại:**
- Một DRD mở Big MAC (target 7-10 tỷ), dưới có 2-3 SM, những SM này lại mở Small MAC riêng
- → DRD nhận Big MAC scheme (office setup 600M + guarantee 60M), các SM dưới cũng nhận Small MAC scheme (300M + 40M mỗi người)
- → Công ty phải invest nhiều lần cho cùng một nhánh, trong khi không có ý định ban đầu

**Ví dụ cụ thể được tính:**
- Big MAC (DRD): 10 tỷ target
- Small MAC #1 (SM dưới DRD): 3 tỷ
- Small MAC #2 (SM khác dưới DRD): 2 tỷ
- → Tổng production chỉ 15 tỷ nhưng công ty phải invest 600M + 300M + 300M setup + guarantees cho 3 văn phòng

**Vấn đề với optimization scenario:**
- Nếu DRD chỉ làm đủ 19 active/tháng (tương đương ~3.5 tỷ FYP theo one-month-AA logic) → vẫn nhận full 60M guarantee
- Các SM dưới cũng optimize tương tự → toàn bộ nhánh under-perform nhưng vẫn nhận full guarantees

**Giải pháp đề xuất - Limit Rules:**

1. **SSM/SM**: Chỉ được mở **tối đa 1 MAC** trên toàn hệ thống
2. **DRD+**: Được mở **1 Big MAC HOẶC 2 Small MACs** (không mix)
3. **Điều kiện cấm**: Nếu toàn bộ team structure của leader đó đã nằm trong một Big MAC, không cho mở thêm MAC con bên trong

### D. One-Month-AA (1mAA) Calculation Logic

- Hiện tại: guarantee dựa trên việc đạt 1mAA (monthly active agents)
- Ví dụ Normal MAC: 19 active/tháng x 12 tháng x 12M FYC/active ≈ 2.7 tỷ FYP
- Vấn đề: 2.7 tỷ chỉ = 40% target SM (nếu target SM là ~7 tỷ) → có thể optimize để nhận guarantee mà không cần grow
- Đối với Big MAC: Cần recalculate 1mAA threshold phù hợp với 60M guarantee và 7-10 tỷ target

## 3. Quyết định đã đưa ra

1. **Chọn Cách 2** (traditional approach): Base cost simulation trên rank-based FYP targets (3-5 tỷ cho Small, 7-10 tỷ cho Big), sau đó làm sensitivity scenarios
2. **Cần làm sensitivity scenarios bao gồm**:
   - Below base FYP
   - Above base FYP  
   - "Optimize scenario" (chỉ làm đủ 1mAA để maximize guarantee)
3. **Phải test trường hợp multiple MACs** trong cùng một nhánh để quantify cost impact và quyết định có chấp nhận được không
4. **Nếu không chấp nhận multiple MACs abuse** → phải design limit rules rõ ràng trong scheme document
5. **Competitor analysis format**: Làm high-level 2 levels thôi (không chi tiết từng năm), tương tự file cũ:
   - Assumptions/Inputs
   - Total comparison (office setup + monthly support + max potential)

## 4. Action Items

| Task | Owner | Details |
|------|-------|---------|
| **Clean up & finalize Cost Simulation file V1** | Chị (speaker) | - Sử dụng file V1 (không có chữ xanh)<br>- Update để reflect Big MAC parameters (600M setup, 60M guarantee)<br>- Có thể làm file mới nếu thấy quá rối<br>- Test "optimize scenario" với 1mAA minimums |
| **Derive FYP base targets & 1mAA thresholds** | Chị | - Small MAC: 3-5 tỷ base<br>- Big MAC: 7-10 tỷ base<br>- Calculate matching 1mAA requirements |
| **Test multiple MACs scenario** | Chị | - Simulate cost nếu DRD mở Big MAC + 2 SMs dưới mở Small MACs<br>- Quantify total investment vs production<br>- Determine acceptability |
| **Competitor analysis** | Chị Phương (lead) | - High-level comparison (2 levels only: inputs + totals)<br>- Break out: Office setup + Monthly support<br>- Compare both Small MAC & Big MAC vs competitor equivalents<br>- May need support from Quỳnh if workload heavy |
| **SOP review for MAC** | Chị Phương | - Review điều kiện nếu leader không có direct log<br>- Identify which compensation components cannot auto-apply (manual workaround needed)<br>- List exceptions/exemptions needed (e.g., healthcare)<br>- Coordinate with CPA on system requirements |
| **Support work if needed** | Quỳnh | - Hỗ trợ chị Phương nếu competitor analysis quá tải<br>- Có thể chia nhỏ sections để làm song song |
| **MOC (Minimum Operating Criteria) rules** | Em (meeting lead) | - Nghĩ thêm về MOC requirements cho Big MAC<br>- Design limit rules cho multiple MACs (rank-based, quantity limits)<br>- Draft conditions: 1 Big hoặc 2 Small, không cho con MAC trong Big MAC, etc. |

## 5. Câu hỏi chưa giải quyết

1. **Sensitivity ranges cụ thể**: Cần define rõ các mức FYP scenarios (ví dụ: 70%, 85%, 100%, 115%, 130% của base?) cho cả Small và Big MAC

2. **1mAA thresholds cho Big MAC**: Con số cụ thể bao nhiêu active/tháng để nhận 60M guarantee? Hiện chưa finalize.

3. **Office setup breakdown**: Cần chi tiết hơn về setup 600M VND cho Big MAC được allocate như thế nào (furniture, equipment, signage, etc.) - có thể hỏi anh Long về benchmark theo m² như competitors (Pro đã có data này)

4. **Multiple MACs limit rules - final decision**: 
   - Có cho phép hay hoàn toàn cấm?
   - Nếu cho phép có điều kiện → điều kiện cụ thể là gì? (production threshold? separation rules?)
   - Approval process ra sao?

5. **Catchup mechanism cho Big MAC**: Normal MAC có catchup nếu miss monthly nhưng achieve trong 3-6 tháng. Big MAC có apply tương tự không?

6. **Internal MAC for Big MAC**: Scheme có apply cho internal leader lên DRD+ mở Big MAC không? Nếu có thì 8% FYP chỉ tính trên new recruits hay toàn bộ team?

7. **Competitor analysis scope**: Cần compare với bao nhiêu competitors? Format cuối cùng là table hay narrative? Cần data points gì từ field/anh Long?

## 6. Số liệu/Dữ liệu quan trọng

### Big MAC Scheme Parameters (2026 proposal)

| Item | Value |
|------|-------|
| Office size | ~150 m² |
| Office setup | 600M VND |
| Monthly office allowance | 8% FYP |
| Guarantee with 1mAA | 60M VND/month |
| Guarantee without 1mAA | 30M VND/month |
| Guarantee period | 3 years |
| Target rank | DRD+ |
| Estimated FYP range | 7-10 tỷ |

### Normal/Small MAC (reference - 2025 pilot)

| Item | Value |
|------|-------|
| Office size | ~70 m² |
| Office setup | 300M VND |
| Monthly allowance | 8% FYP |
| Guarantee with 1mAA | 40M VND/month |
| Guarantee without 1mAA | 20M VND/month |
| Target rank | SM/SSM |
| Estimated FYP | 3-5 tỷ |
| 2025 results | 8 MACs opened (7 GTF + 1 internal) |

### Recruiter Benefits (applies to both)

- One-off bonus: **50M VND** per MAC recruited
- Monthly bonus: **3% FYP** for first 12 months (max 100M VND total)

### Cost Ratios Referenced

- **8% FYP** phải đủ cover office costs để sustainable long-term
- Để 60M/month sustainable → cần ~**9-10 tỷ FYP** (60M x 12 / 8% ≈ 9 tỷ)
- Current CE (Controllable Expenses) = **20-30% FYP** trong Branch Model
- "Optimize scenario" example: 19 active x 12M FYC x 12 months ≈ **2.7 tỷ FYP** (chỉ ~40% of typical SM target)

### Timeline

- 2025: Pilot Normal MAC approved locally (đã chạy 7 tháng từ tháng 5)
- 2026: Đề xuất Big MAC + xin approve regional level (không chỉ pilot 1 năm mà là ongoing scheme)
- Deadline không rõ ràng nhưng cần hoàn thành cost file & competitor analysis sớm để submit lên vùng
