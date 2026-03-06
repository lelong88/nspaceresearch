"""
Send 2 emails about Activity Requirements for PSM+ and UM+:
  Email 1 → Working Group: detailed, with tables
  Email 2 → EMT: high-level summary with infographic, requesting approval

Usage:
    python -m output.activity-requirement-psm-um.send_emails
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from send_email import send_email


# ─── Shared styles ───────────────────────────────────────────────────────────

STYLE = """
<style>
  body { font-family: 'Segoe UI', Arial, sans-serif; color: #222; line-height: 1.6; }
  .container { max-width: 780px; margin: 0 auto; padding: 24px; }
  h1 { color: #00703c; font-size: 22px; border-bottom: 3px solid #00703c; padding-bottom: 8px; }
  h2 { color: #00703c; font-size: 17px; margin-top: 28px; }
  h3 { color: #333; font-size: 15px; margin-top: 20px; }
  .badge { display: inline-block; padding: 4px 12px; border-radius: 12px; font-size: 12px; font-weight: 600; }
  .badge-green { background: #d4edda; color: #155724; }
  .badge-red { background: #f8d7da; color: #721c24; }
  .badge-yellow { background: #fff3cd; color: #856404; }
  .badge-blue { background: #d1ecf1; color: #0c5460; }
  .badge-gray { background: #e2e3e5; color: #383d41; }
  table { border-collapse: collapse; width: 100%; margin: 12px 0; font-size: 14px; }
  th { background: #00703c; color: #fff; padding: 10px 12px; text-align: left; font-weight: 600; }
  td { padding: 9px 12px; border-bottom: 1px solid #dee2e6; }
  tr:nth-child(even) { background: #f8f9fa; }
  .info-box { background: #e8f5e9; border-left: 4px solid #00703c; padding: 14px 18px; margin: 16px 0; border-radius: 4px; }
  .warn-box { background: #fff8e1; border-left: 4px solid #f9a825; padding: 14px 18px; margin: 16px 0; border-radius: 4px; }
  .section-card { border: 1px solid #dee2e6; border-radius: 8px; padding: 18px; margin: 16px 0; }
  .timeline { border-left: 3px solid #00703c; padding-left: 20px; margin: 16px 0; }
  .timeline-item { margin-bottom: 14px; position: relative; }
  .timeline-item::before { content: '●'; color: #00703c; position: absolute; left: -27px; font-size: 14px; }
  .footer { margin-top: 32px; padding-top: 16px; border-top: 1px solid #dee2e6; font-size: 13px; color: #666; }
  .highlight { background: #fff3cd; padding: 2px 6px; border-radius: 3px; }
  ul { padding-left: 20px; }
  li { margin-bottom: 4px; }
</style>
"""

# ─── EMAIL 1: Working Group (detailed) ──────────────────────────────────────

EMAIL_1_SUBJECT = "[Working Group] Activity Requirements cho PSM+ và UM+ — Chi tiết triển khai"

EMAIL_1_BODY = STYLE + """
<div class="container">

<h1>📋 Activity Requirements cho PSM+ và UM+ — Chi tiết triển khai</h1>

<div class="info-box">
  <strong>Mục đích:</strong> Triển khai điều kiện hoạt động (activity requirements) đối với PSM+ và UM+ nhằm đảm bảo tuân thủ
  <strong>Luật Kinh doanh Bảo hiểm (IBL)</strong>. UM và PSM là các servicing contract — cần chứng minh hoạt động để hợp lệ nhận phí dịch vụ.
</div>

<!-- ═══════════════════════════════════════════════════════════════════ -->
<h2>I. Background</h2>

<p>Theo Luật bảo hiểm mới, phạm vi dịch vụ trong hợp đồng dịch vụ yêu cầu SM phải có bằng chứng hỗ trợ đội ngũ hoạt động. Working team đề xuất sử dụng các hoạt động được tạo bởi SM trên <strong>ứng dụng M-PA</strong>, bao gồm:</p>
<ul>
  <li><strong>COP</strong> — Hội thảo tuyển dụng</li>
  <li><strong>DA (Diligent Agent)</strong> — Đội ngũ chuyên cần</li>
  <li><strong>Training</strong> — Đào tạo</li>
</ul>

<!-- ═══════════════════════════════════════════════════════════════════ -->
<h2>II. Phần A — Áp dụng cho PSM+</h2>

<h3>1. Điều kiện hoạt động tối thiểu trên M-PA (hàng tháng)</h3>

<table>
  <tr>
    <th>Rank</th>
    <th>Số lượng tối thiểu<br>(COP / Training / DA)</th>
    <th>Bắt buộc bao gồm</th>
  </tr>
  <tr>
    <td><strong>SM — SSM</strong></td>
    <td style="text-align:center; font-size:20px; font-weight:700; color:#00703c;">2</td>
    <td>1 COP + 1 DA</td>
  </tr>
  <tr>
    <td><strong>DRD — RD — SRD</strong></td>
    <td style="text-align:center; font-size:20px; font-weight:700; color:#00703c;">4</td>
    <td>1 COP + 1 DA</td>
  </tr>
  <tr>
    <td><strong>AVP+</strong></td>
    <td style="text-align:center; font-size:20px; font-weight:700; color:#00703c;">6</td>
    <td>1 COP + 2 Training</td>
  </tr>
</table>

<div class="info-box">
  <strong>Ghi nhận trên M-PA:</strong><br>
  <table style="margin:8px 0;">
    <tr><th>Event type</th><th>Activity type code</th></tr>
    <tr><td>COP</td><td><code>COP</code></td></tr>
    <tr><td>DA workshop</td><td><code>WEEK_MEETING</code></td></tr>
    <tr><td>Training</td><td><code>Sale_training</code>, <code>Agency_meeting</code>, <code>Week_meeting</code></td></tr>
  </table>
  <strong>Cut-off:</strong> Event có start date trong tháng, data cut-off 24h00 ngày ME-1 (1 ngày trước cuối tháng).<br>
  <strong>Status hợp lệ:</strong> Published / Pending Acceptance / Completed
</div>

<h3>2. Các khoản phí dịch vụ — Áp dụng hay không?</h3>

<table>
  <tr>
    <th>Loại khoản chi trả</th>
    <th>Áp dụng Activity?</th>
    <th>Cách lấy kết quả</th>
  </tr>
  <tr>
    <td>Compensation / Monthly allowance<br><span style="color:#666; font-size:12px;">(tel, taxi, thưởng tháng/quý/năm)</span></td>
    <td><span class="badge badge-green">✅ Áp dụng</span></td>
    <td>
      • Thưởng tháng → KQ hoạt động tháng đó<br>
      • Thưởng quý → KQ tháng cuối quý<br>
      • Thưởng năm → KQ tháng 4 (chi trả T4 hàng năm)
    </td>
  </tr>
  <tr>
    <td>Benefit manual<br><span style="color:#666; font-size:12px;">(laptop, healthcare, top SM…)</span></td>
    <td><span class="badge badge-green">✅ Áp dụng</span></td>
    <td>KQ hoạt động <strong>tháng trước</strong> tháng chi trả</td>
  </tr>
  <tr>
    <td>Contest cash / Gift qua contest</td>
    <td><span class="badge badge-green">✅ Áp dụng</span></td>
    <td>KQ hoạt động của tháng thi đua</td>
  </tr>
  <tr>
    <td>Cash advance trên NR, UM</td>
    <td><span class="badge badge-yellow">⏳ TBC</span></td>
    <td>Memo yêu cầu SM đăng ký — cần trao đổi thêm với FA/team thuế</td>
  </tr>
  <tr>
    <td>Trip (hội nghị đào tạo)</td>
    <td><span class="badge badge-red">❌ Không áp dụng</span></td>
    <td>Do công ty tổ chức, SM không chịu PIT</td>
  </tr>
  <tr>
    <td>Meeting / Training event</td>
    <td><span class="badge badge-red">❌ Không áp dụng</span></td>
    <td>Đã được xem là hoạt động kinh doanh</td>
  </tr>
  <tr>
    <td>Gift qua sales activity</td>
    <td><span class="badge badge-red">❌ Không áp dụng</span></td>
    <td>—</td>
  </tr>
  <tr>
    <td>M-shop</td>
    <td><span class="badge badge-red">❌ Không áp dụng</span></td>
    <td>Chưa chốt quy trình, chỉ key thuế/thu hồi</td>
  </tr>
  <tr>
    <td>COP/CS budget</td>
    <td><span class="badge badge-red">❌ Không áp dụng</span></td>
    <td>Memo đã yêu cầu tối thiểu 2 COP/CS + claim hóa đơn</td>
  </tr>
  <tr>
    <td>Khoản key tính thuế only / thu hồi</td>
    <td><span class="badge badge-gray">N/A</span></td>
    <td>Nghĩa vụ thuế / khoản nợ — không phải thu nhập</td>
  </tr>
</table>

<div class="warn-box">
  <strong>⚠️ Lưu ý:</strong> Nếu SM không đạt điều kiện Activity → hệ thống vẫn tính kết quả nhưng <strong>không chi trả</strong> thu nhập (giữ lại phòng trường hợp appeal).
</div>

<h3>3. Thời gian áp dụng PSM+</h3>
<div class="timeline">
  <div class="timeline-item"><strong>Tháng 3/2026:</strong> Bắt đầu áp dụng. Working team đã clear rule, đang UAT và sẵn sàng checking.</div>
</div>

<!-- ═══════════════════════════════════════════════════════════════════ -->
<h2>III. Phần B — Áp dụng cho UM+</h2>

<h3>Cơ chế hoạt động trên M-PA</h3>
<p>Mở rộng quyền truy cập M-PA web-portal cho UM+ — sử dụng tính năng <strong>Quản lý sự kiện</strong> (flow hiện hữu, không thay đổi).</p>

<div class="section-card">
  <strong>🔔 Flow hàng tháng:</strong>
  <ol>
    <li>Ngày 01 hàng tháng: hệ thống gửi <strong>notification tự động</strong> nhắc UM+ lên lịch họp/huấn luyện đội ngũ.</li>
    <li>UM+ mở M-PA → <strong>pop-up full screen</strong> bắt buộc xác nhận trước khi dùng app:
      <ul>
        <li>Ngày sự kiện: mặc định Monday gần nhất (hoặc first working day), cho phép chỉnh trong tháng (trước ngày 20)</li>
        <li>Loại sự kiện: <em>"Mời họp huấn luyện đội ngũ định kỳ tháng"</em></li>
        <li>Tên sự kiện: <code>(LOC) + UM Agent code + Tên UM - Mời họp huấn luyện đội ngũ định kỳ tháng</code></li>
        <li>Tối đa <strong>4 ngày sự kiện / 4 tuần</strong></li>
      </ul>
    </li>
    <li>UM+ xác nhận → hệ thống tạo sự kiện → thành viên direct team / whole team (bao gồm SA) nhận thư mời qua email + noti M-PA.</li>
    <li>UM+ không xác nhận / drop ngang → khi vào lại M-PA sẽ bị redirect lại pop-up.</li>
  </ol>
</div>

<h3>2 Option triển khai cho UM+</h3>

<table>
  <tr>
    <th></th>
    <th>Option 1</th>
    <th>Option 2</th>
  </tr>
  <tr>
    <td><strong>18/01/2026</strong></td>
    <td>Launch tính năng xác nhận hỗ trợ hợp đồng + thông báo điều kiện chi trả dựa trên #DL đã xác nhận.<br>Điều kiện bắt đầu apply <span class="highlight">T4/2026</span></td>
    <td>Chỉ thông báo về điều kiện chi trả dựa trên #DL đã có hoạt động hỗ trợ. Chi tiết yêu cầu & thời gian apply thông báo Q2/2026</td>
  </tr>
  <tr>
    <td><strong>T4/2026</strong></td>
    <td>Launch tính năng tạo hoạt động họp UM+ + thông báo điều kiện chi trả dựa trên #DL đã đặt lịch họp.<br>Bắt đầu apply <span class="highlight">T7/2026</span></td>
    <td>Tương tự Option 1: launch tính năng tạo hoạt động họp UM+.<br>Bắt đầu apply <span class="highlight">T7/2026</span></td>
  </tr>
</table>

<!-- ═══════════════════════════════════════════════════════════════════ -->
<h2>IV. Cách áp dụng tổng hợp (System)</h2>

<div class="section-card">
  <strong>Phương án đề xuất:</strong> Gom chung 1 cách áp dụng cho compensation, contest và benefit:
  <ul>
    <li>System chạy cuối kỳ trước chi trả cho SM (các team vẫn key payment bình thường)</li>
    <li>Lấy kết quả activity của tháng chi trả</li>
    <li>Màn hình upload payment có <strong>checkbox</strong> cho user tick khoản có áp dụng activity hay không</li>
  </ul>
</div>

<div class="warn-box">
  <strong>⚠️ Trong thời gian chờ system setup — phương án manual:</strong>
  <ul>
    <li>Dùng KQ activity tháng trước (cần truyền thông lại rule khi system go-live)</li>
    <li>Dùng KQ activity theo từng thi đua (cần truyền thông lại rule)</li>
    <li>Chi trả trước, tháng sau tính lại & thu hồi (rủi ro: SM nghỉ việc → không thu hồi được)</li>
  </ul>
</div>

<div class="footer">
  Vui lòng review và phản hồi nếu có góp ý. Xin cảm ơn.
</div>

</div>
"""

# ─── EMAIL 2: EMT (high-level, approval request) ────────────────────────────

EMAIL_2_SUBJECT = "[EMT Approval Required] Áp dụng Activity Requirements cho PSM+ và UM+"

EMAIL_2_BODY = STYLE + """
<div class="container">

<h1>🔔 Xin Approval: Áp dụng Activity Requirements cho PSM+ và UM+</h1>

<div class="info-box">
  <strong>Kính gửi EMT,</strong><br><br>
  Working team xin trình bày phương án áp dụng <strong>điều kiện hoạt động (Activity Requirements)</strong> đối với PSM+ và UM+,
  nhằm đảm bảo tuân thủ <strong>Luật Kinh doanh Bảo hiểm (IBL)</strong> và xin approval để triển khai.
</div>

<!-- ═══ WHY ═══ -->
<div class="section-card" style="background: #f8f9fa;">
  <h2 style="margin-top:0;">📌 Tại sao cần áp dụng?</h2>
  <table style="border:none;">
    <tr>
      <td style="width:50px; text-align:center; font-size:28px; border:none;">📜</td>
      <td style="border:none;"><strong>Yêu cầu pháp lý:</strong> Luật IBL mới yêu cầu SM phải có bằng chứng hoạt động hỗ trợ đội ngũ để hợp lệ nhận phí dịch vụ.</td>
    </tr>
    <tr>
      <td style="text-align:center; font-size:28px; border:none;">📝</td>
      <td style="border:none;"><strong>Servicing contract:</strong> UM và PSM là các hợp đồng dịch vụ — cần chứng minh hoạt động để được nhận income/thưởng.</td>
    </tr>
    <tr>
      <td style="text-align:center; font-size:28px; border:none;">📱</td>
      <td style="border:none;"><strong>Giải pháp:</strong> Ghi nhận hoạt động qua ứng dụng <strong>M-PA</strong> (COP, DA workshop, Training).</td>
    </tr>
  </table>
</div>

<!-- ═══ PSM+ SUMMARY ═══ -->
<h2>🅰️ PSM+ — Điều kiện hoạt động hàng tháng</h2>

<table>
  <tr>
    <th style="width:30%;">Rank</th>
    <th style="width:25%; text-align:center;">Số hoạt động tối thiểu</th>
    <th>Bắt buộc bao gồm</th>
  </tr>
  <tr>
    <td>SM — SSM</td>
    <td style="text-align:center;"><span style="font-size:22px; font-weight:700; color:#00703c;">2</span></td>
    <td>1 COP + 1 DA</td>
  </tr>
  <tr>
    <td>DRD — RD — SRD</td>
    <td style="text-align:center;"><span style="font-size:22px; font-weight:700; color:#00703c;">4</span></td>
    <td>1 COP + 1 DA</td>
  </tr>
  <tr>
    <td>AVP+</td>
    <td style="text-align:center;"><span style="font-size:22px; font-weight:700; color:#00703c;">6</span></td>
    <td>1 COP + 2 Training</td>
  </tr>
</table>

<div style="display:flex; gap:12px; margin:16px 0; flex-wrap:wrap;">
  <div style="flex:1; min-width:200px; background:#d4edda; border-radius:8px; padding:14px; text-align:center;">
    <div style="font-size:13px; color:#155724;">Compensation & Benefits</div>
    <div style="font-size:18px; font-weight:700; color:#155724; margin-top:4px;">✅ Áp dụng</div>
  </div>
  <div style="flex:1; min-width:200px; background:#d4edda; border-radius:8px; padding:14px; text-align:center;">
    <div style="font-size:13px; color:#155724;">Contest cash</div>
    <div style="font-size:18px; font-weight:700; color:#155724; margin-top:4px;">✅ Áp dụng</div>
  </div>
  <div style="flex:1; min-width:200px; background:#f8d7da; border-radius:8px; padding:14px; text-align:center;">
    <div style="font-size:13px; color:#721c24;">Trip / Meeting / M-shop</div>
    <div style="font-size:18px; font-weight:700; color:#721c24; margin-top:4px;">❌ Không áp dụng</div>
  </div>
</div>

<p><strong>Không đạt điều kiện →</strong> hệ thống vẫn tính kết quả nhưng <strong>tạm giữ, không chi trả</strong> (phòng appeal).</p>

<!-- ═══ UM+ SUMMARY ═══ -->
<h2>🅱️ UM+ — Ghi nhận hoạt động qua M-PA</h2>

<div style="display:flex; gap:16px; margin:16px 0; flex-wrap:wrap;">
  <div style="flex:1; min-width:220px; border:2px solid #00703c; border-radius:8px; padding:16px;">
    <div style="font-size:13px; color:#666;">Bước 1</div>
    <div style="font-size:15px; font-weight:600; margin:6px 0;">🔔 Notification tự động</div>
    <div style="font-size:13px;">Ngày 01 hàng tháng, hệ thống nhắc UM+ lên lịch họp/huấn luyện đội ngũ</div>
  </div>
  <div style="flex:1; min-width:220px; border:2px solid #00703c; border-radius:8px; padding:16px;">
    <div style="font-size:13px; color:#666;">Bước 2</div>
    <div style="font-size:15px; font-weight:600; margin:6px 0;">📱 Xác nhận trên M-PA</div>
    <div style="font-size:13px;">UM+ mở app → pop-up bắt buộc xác nhận sự kiện huấn luyện (tối đa 4/tháng)</div>
  </div>
  <div style="flex:1; min-width:220px; border:2px solid #00703c; border-radius:8px; padding:16px;">
    <div style="font-size:13px; color:#666;">Bước 3</div>
    <div style="font-size:15px; font-weight:600; margin:6px 0;">📧 Thư mời tự động</div>
    <div style="font-size:13px;">Hệ thống gửi thư mời cho direct team / whole team (bao gồm SA)</div>
  </div>
</div>

<!-- ═══ TIMELINE ═══ -->
<h2>📅 Timeline triển khai</h2>

<table>
  <tr>
    <th style="width:25%;">Thời gian</th>
    <th>PSM+</th>
    <th>UM+</th>
  </tr>
  <tr>
    <td><strong>T3/2026</strong></td>
    <td><span class="badge badge-green">Go-live</span> Bắt đầu áp dụng (UAT hoàn tất)</td>
    <td>—</td>
  </tr>
  <tr>
    <td><strong>T4/2026</strong></td>
    <td>—</td>
    <td>Launch tính năng tạo hoạt động họp UM+ trên M-PA</td>
  </tr>
  <tr>
    <td><strong>T7/2026</strong></td>
    <td>—</td>
    <td><span class="badge badge-green">Go-live</span> Bắt đầu áp dụng điều kiện chi trả</td>
  </tr>
</table>

<!-- ═══ APPROVAL ═══ -->
<div style="background:#e8f5e9; border:2px solid #00703c; border-radius:8px; padding:20px; margin:24px 0; text-align:center;">
  <div style="font-size:18px; font-weight:700; color:#00703c; margin-bottom:8px;">🙏 Xin EMT approval để triển khai</div>
  <div style="font-size:14px; color:#333;">
    Phương án trên đã được working team review và chuẩn bị sẵn sàng.<br>
    Kính mong EMT xem xét và phê duyệt để tiến hành triển khai theo timeline.
  </div>
</div>

<div class="footer">
  Chi tiết đầy đủ đã được gửi cho Working Group. Nếu cần thêm thông tin, vui lòng liên hệ working team.<br>
  Trân trọng.
</div>

</div>
"""


# ─── SEND ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("Sending Email 1 → Working Group (detailed)...")
    print("=" * 60)
    r1 = send_email(EMAIL_1_SUBJECT, EMAIL_1_BODY, html=True)
    print(f"  Result: {r1}\n")

    print("=" * 60)
    print("Sending Email 2 → EMT (high-level, approval)...")
    print("=" * 60)
    r2 = send_email(EMAIL_2_SUBJECT, EMAIL_2_BODY, html=True)
    print(f"  Result: {r2}\n")

    if r1["success"] and r2["success"]:
        print("✅ Both emails sent successfully.")
    else:
        print("⚠️  One or more emails failed. Check output above.")
        sys.exit(1)
