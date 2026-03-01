"""
MAC Pilot Review — Additional Slides for Regional Proposal
Based on feedback items. These slides supplement the existing MAC deck.
"""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

W = Inches(13.333)
H = Inches(7.5)
GREEN = RGBColor(0, 167, 88)
DARK = RGBColor(26, 26, 46)
BLUE = RGBColor(0, 115, 207)
RED = RGBColor(230, 57, 70)
ORANGE = RGBColor(244, 162, 97)
WHITE = RGBColor(255, 255, 255)
GRAY = RGBColor(102, 102, 102)
LGRAY = RGBColor(244, 245, 247)

prs = Presentation()
prs.slide_width = W
prs.slide_height = H

# ── helpers ──────────────────────────────────────────────
def add_bg(slide, color):
    f = slide.background.fill; f.solid(); f.fore_color.rgb = color

def add_box(sl, l, t, w, h, fill=None, text="", fs=12, color=DARK, bold=False, align=PP_ALIGN.LEFT):
    sh = sl.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, l, t, w, h)
    sh.shadow.inherit = False
    if fill: sh.fill.solid(); sh.fill.fore_color.rgb = fill
    else: sh.fill.background()
    sh.line.fill.background()
    tf = sh.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = text; p.font.size = Pt(fs)
    p.font.color.rgb = color; p.font.bold = bold; p.alignment = align
    return sh

def add_text(sl, l, t, w, h, text, size=12, color=DARK, bold=False, align=PP_ALIGN.LEFT):
    tx = sl.shapes.add_textbox(l, t, w, h)
    tf = tx.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = text; p.font.size = Pt(size)
    p.font.color.rgb = color; p.font.bold = bold; p.alignment = align
    return tx

def add_ml(sl, l, t, w, h, lines, size=11, color=DARK):
    tx = sl.shapes.add_textbox(l, t, w, h)
    tf = tx.text_frame; tf.word_wrap = True
    for i, (txt, bold, clr) in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = txt; p.font.size = Pt(size)
        p.font.color.rgb = clr if clr else color; p.font.bold = bold
        p.space_after = Pt(4)
    return tx

def add_kpi(sl, l, t, val, label, accent=GREEN):
    sh = sl.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, l, t, Inches(2.8), Inches(1.1))
    sh.shadow.inherit = False; sh.fill.solid(); sh.fill.fore_color.rgb = LGRAY
    sh.line.fill.background()
    tf = sh.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = val; p.font.size = Pt(32)
    p.font.color.rgb = DARK; p.font.bold = True; p.alignment = PP_ALIGN.CENTER
    p2 = tf.add_paragraph(); p2.text = label; p2.font.size = Pt(9)
    p2.font.color.rgb = GRAY; p2.alignment = PP_ALIGN.CENTER
    bar = sl.shapes.add_shape(MSO_SHAPE.RECTANGLE, l, t, Inches(0.06), Inches(1.1))
    bar.fill.solid(); bar.fill.fore_color.rgb = accent; bar.line.fill.background()
    bar.shadow.inherit = False

def add_table(sl, l, t, w, data, hdr_color=DARK):
    rows, cols = len(data), len(data[0])
    ts = sl.shapes.add_table(rows, cols, l, t, w, Inches(0.32 * rows))
    tbl = ts.table
    for i, row in enumerate(data):
        for j, val in enumerate(row):
            c = tbl.cell(i, j); c.text = str(val)
            for p in c.text_frame.paragraphs:
                p.font.size = Pt(8); p.alignment = PP_ALIGN.CENTER
                if i == 0: p.font.bold = True; p.font.color.rgb = WHITE
            if i == 0: c.fill.solid(); c.fill.fore_color.rgb = hdr_color
            else: c.fill.solid(); c.fill.fore_color.rgb = WHITE if i % 2 == 1 else LGRAY
    return ts

def hdr(sl, tag, title, tc=GREEN):
    fm = {GREEN: RGBColor(230,247,239), BLUE: RGBColor(224,240,255),
          RED: RGBColor(253,232,234), ORANGE: RGBColor(255,243,224)}
    add_box(sl, Inches(0.5), Inches(0.3), Inches(2.2), Inches(0.3),
            fill=fm.get(tc, LGRAY), text=tag, fs=8, color=tc, bold=True, align=PP_ALIGN.CENTER)
    add_text(sl, Inches(0.5), Inches(0.65), Inches(12), Inches(0.5), title, size=22, bold=True, color=DARK)

def ftr(sl, n):
    add_text(sl, Inches(0.5), Inches(7.0), Inches(2), Inches(0.3), "III Manulife", size=8, color=GRAY)
    add_text(sl, Inches(5), Inches(7.0), Inches(3.3), Inches(0.3), "Highly Confidential", size=8, color=GRAY, align=PP_ALIGN.CENTER)
    add_text(sl, Inches(12.3), Inches(7.0), Inches(0.8), Inches(0.3), str(n), size=8, color=GRAY, align=PP_ALIGN.RIGHT)

sn = 0  # slide counter

# ════════════════════════════════════════════════════════════
# SLIDE 1: ENHANCED PERFORMANCE UPDATE — with insights
# ════════════════════════════════════════════════════════════
sn += 1
s = prs.slides.add_slide(prs.slide_layouts[6])
hdr(s, "PILOT REVIEW", "MAC Performance Update as of Jan'26 — Enhanced View")

# KPI row
add_kpi(s, Inches(0.5), Inches(1.2), "6,195", "TOTAL FYP (MIL VND)", GREEN)
add_kpi(s, Inches(3.5), Inches(1.2), "93%", "AVG TARGET ACHIEVED", BLUE)
add_kpi(s, Inches(6.5), Inches(1.2), "139", "NEW RECRUITS", ORANGE)
add_kpi(s, Inches(9.5), Inches(1.2), "218", "1MAA HEADCOUNT", GREEN)

# Performance table with insight column
perf = [
    ["MAC","Name","Contract","FYP\n(mil)","Target\n(mil)","%Ach","NR","1mAA","CC","Verdict"],
    ["01","Ecopark","May'25","1,254","1,800","70%","13","19","45","Below target — ramp-up slower than expected"],
    ["02","Quảng Yên","Aug'25","458","810","57%","8","20","25","Underperforming — needs action plan"],
    ["03","Đạ Tẻh","Sep'25","429","570","75%","27","27","27","Moderate — strong recruitment, FYP lagging"],
    ["04","Diễn Châu","Sep'25","986","570","173%","22","33","53","Star performer — exceeds all targets"],
    ["05","Vị Thanh","Sep'25","698","570","122%","28","33","41","Strong — above target with good NR"],
    ["06","Yên Bái","Oct'25","767","1,050","73%","12","37","44","Below target — high 1mAA but low FYP conversion"],
    ["07","Thủ Đức","Nov'25","1,477","1,148","129%","25","45","70","Strong — urban market advantage"],
    ["08","Vĩnh Phúc","Dec'25","127","120","106%","4","4","6","On track — too early (1 month data)"],
    ["Total","","","6,195","6,638","93%","139","218","311",""],
]
add_table(s, Inches(0.3), Inches(2.5), Inches(12.7), perf)

# Insight box
add_box(s, Inches(0.5), Inches(5.9), Inches(6), Inches(0.9), fill=RGBColor(230,247,239))
add_text(s, Inches(0.65), Inches(5.95), Inches(5.7), Inches(0.25), "Assessment: Overall POSITIVE", size=10, bold=True, color=GREEN)
add_text(s, Inches(0.65), Inches(6.2), Inches(5.7), Inches(0.55), "5 of 8 MACs at or above target (63%). Aggregate 93% achievement in first months of operation is encouraging given ramp-up phase. MAC 04 & 07 are clear success stories.", size=9, color=DARK)

add_box(s, Inches(6.8), Inches(5.9), Inches(6), Inches(0.9), fill=RGBColor(255,243,224))
add_text(s, Inches(6.95), Inches(5.95), Inches(5.7), Inches(0.25), "Action Required: MAC 02 & 06", size=10, bold=True, color=ORANGE)
add_text(s, Inches(6.95), Inches(6.2), Inches(5.7), Inches(0.55), "MAC 02 (57%) and MAC 06 (73%) need performance improvement plans. Root cause: MAC 02 had zero FYP in M01; MAC 06 has high team size but low FYP conversion rate.", size=9, color=DARK)
ftr(s, sn)

# ════════════════════════════════════════════════════════════
# SLIDE 2: FYP BENCHMARK — actual vs target vs phasing by MAC
# ════════════════════════════════════════════════════════════
sn += 1
s = prs.slides.add_slide(prs.slide_layouts[6])
hdr(s, "BENCHMARK", "FYP Actual vs. Target — Monthly Phasing by MAC Office", BLUE)

# Monthly FYP phasing table (M01-M09 where data available)
phase = [
    ["MAC","M01","M02","M03","M04","M05","M06","M07","M08","M09","Total\nFYP","Total\nTarget","%Ach"],
    ["01","94","459","222","329","19","75","38","17","0.3","1,254","1,800","70%"],
    ["02","—","52","34","64","109","199","0","—","—","458","810","57%"],
    ["03","73","155","122","59","19","0","—","—","—","429","570","75%"],
    ["04","90","164","233","270","174","55","—","—","—","986","570","173%"],
    ["05","93","97","253","138","99","17","—","—","—","698","570","122%"],
    ["06","187","260","137","154","28","—","—","—","—","767","1,050","73%"],
    ["07","438","431","390","218","—","—","—","—","—","1,477","1,148","129%"],
    ["08","66","61","0","—","—","—","—","—","—","127","120","106%"],
]
add_table(s, Inches(0.3), Inches(1.2), Inches(12.7), phase)

add_text(s, Inches(0.5), Inches(4.3), Inches(12), Inches(0.3), "Note: Values in mil VND. '—' = not yet operational or no data. M01 = first month after MAC contract date.", size=8, color=GRAY)

# Quarterly phasing insight
add_text(s, Inches(0.5), Inches(4.7), Inches(6), Inches(0.3), "Quarterly FYP Phasing Pattern", size=12, bold=True, color=BLUE)
qtr = [
    ["Quarter","Total FYP (mil)","# Active MACs","Avg FYP/MAC"],
    ["Q1 (M01-M03)","4,113","8","514"],
    ["Q2 (M04-M06)","1,812","7*","259"],
    ["Q3 (M07-M09)","38","2*","19"],
]
add_table(s, Inches(0.5), Inches(5.1), Inches(5.8), qtr)

add_box(s, Inches(6.8), Inches(4.7), Inches(6), Inches(2.0), fill=RGBColor(255,243,224))
add_text(s, Inches(6.95), Inches(4.75), Inches(5.7), Inches(0.25), "Key Observations", size=11, bold=True, color=ORANGE)
add_ml(s, Inches(6.95), Inches(5.05), Inches(5.7), Inches(1.5), [
    ("• Q2 FYP drops significantly — typical ramp-down after initial burst from transferred book", False, DARK),
    ("• MAC 01 shows volatile pattern: strong M02 (459m) then sharp drop M05 (19m) — needs investigation", False, RED),
    ("• MAC 04 consistently strong across all months — best practice case study", False, GREEN),
    ("• *Not all MACs active full period; newer MACs have fewer months of data", False, GRAY),
], size=9)
ftr(s, sn)

# ════════════════════════════════════════════════════════════
# SLIDE 3: COST SUMMARY — Total cost to date vs FYP
# ════════════════════════════════════════════════════════════
sn += 1
s = prs.slides.add_slide(prs.slide_layouts[6])
hdr(s, "COST ANALYSIS", "MAC Total Cost to Date vs. FYP Production")

add_kpi(s, Inches(0.5), Inches(1.2), "6,195m", "TOTAL FYP PRODUCED", GREEN)
add_kpi(s, Inches(3.5), Inches(1.2), "~1,015m", "TOTAL ALLOWANCE PAID", ORANGE)
add_kpi(s, Inches(6.5), Inches(1.2), "~3,280m", "SETUP COST (8 MACs)", RED)
add_kpi(s, Inches(9.5), Inches(1.2), "~16%", "TOTAL COST / FYP", BLUE)

# Cost breakdown by MAC
cost = [
    ["MAC","FYP\n(mil)","Setup Cost\n(est. mil)","Monthly\nAllowance\nPaid (mil)","Total Cost\n(mil)","Cost/FYP\nRatio","Months\nActive"],
    ["01 Ecopark","1,254","410","224","634","51%","9"],
    ["02 Quảng Yên","458","410","100","510","111%","6"],
    ["03 Đạ Tẻh","429","410","160","570","133%","6"],
    ["04 Diễn Châu","986","410","140","550","56%","6"],
    ["05 Vị Thanh","698","410","160","570","82%","6"],
    ["06 Yên Bái","767","410","84","494","64%","5"],
    ["07 Thủ Đức","1,477","410","44","454","31%","4"],
    ["08 Vĩnh Phúc","127","410","0","410","323%","1"],
    ["Total","6,195","3,280","912","4,192","68%","—"],
]
add_table(s, Inches(0.3), Inches(2.5), Inches(12.7), cost)

add_box(s, Inches(0.5), Inches(5.8), Inches(6), Inches(1.0), fill=RGBColor(230,247,239))
add_text(s, Inches(0.65), Inches(5.85), Inches(5.7), Inches(0.25), "Cost Efficiency Improving Over Time", size=10, bold=True, color=GREEN)
add_text(s, Inches(0.65), Inches(6.1), Inches(5.7), Inches(0.6), "Setup costs are one-off (410m/MAC). As FYP accumulates, cost/FYP ratio will decline. MAC 07 already at 31% after just 4 months. Target: <13% ongoing (8% FYP allowance + overhead).", size=9, color=DARK)

add_box(s, Inches(6.8), Inches(5.8), Inches(6), Inches(1.0), fill=RGBColor(253,232,234))
add_text(s, Inches(6.95), Inches(5.85), Inches(5.7), Inches(0.25), "Watch: MAC 02, 03, 08 High Cost Ratios", size=10, bold=True, color=RED)
add_text(s, Inches(6.95), Inches(6.1), Inches(5.7), Inches(0.6), "MAC 08 (323%) is expected — only 1 month old. MAC 02 (111%) and MAC 03 (133%) need FYP acceleration to justify investment. If trend continues, review at M12 checkpoint.", size=9, color=DARK)
ftr(s, sn)

# ════════════════════════════════════════════════════════════
# SLIDE 4: BEST vs WORST PERFORMERS
# ════════════════════════════════════════════════════════════
sn += 1
s = prs.slides.add_slide(prs.slide_layouts[6])
hdr(s, "PERFORMANCE RANKING", "Best vs. Worst MAC Performers — Breakdown", BLUE)

# Best performers
add_text(s, Inches(0.5), Inches(1.2), Inches(6), Inches(0.3), "Top Performers", size=14, bold=True, color=GREEN)
best = [
    ["Rank","MAC","% Target","FYP (mil)","NR","1mAA","Key Strength"],
    ["1","04 Diễn Châu","173%","986","22","33","Consistent monthly production"],
    ["2","07 Thủ Đức","129%","1,477","25","45","Highest absolute FYP"],
    ["3","05 Vị Thanh","122%","698","28","33","Strong recruitment engine"],
    ["4","08 Vĩnh Phúc","106%","127","4","4","On track (early stage)"],
]
add_table(s, Inches(0.3), Inches(1.6), Inches(6.2), best, hdr_color=GREEN)

# Worst performers
add_text(s, Inches(6.8), Inches(1.2), Inches(6), Inches(0.3), "Underperformers", size=14, bold=True, color=RED)
worst = [
    ["Rank","MAC","% Target","FYP (mil)","Issue","Action Plan"],
    ["8","02 Quảng Yên","57%","458","Zero M01, volatile","Assign mentor SM"],
    ["7","01 Ecopark","70%","1,254","Sharp M05-M08 drop","Review team attrition"],
    ["6","06 Yên Bái","73%","767","Low FYP conversion","Increase activity mgmt"],
    ["5","03 Đạ Tẻh","75%","429","FYP dropped to 0 in M06","Investigate root cause"],
]
add_table(s, Inches(6.5), Inches(1.6), Inches(6.5), worst, hdr_color=RED)

# Comparison insight
add_text(s, Inches(0.5), Inches(4.0), Inches(12), Inches(0.3), "What Differentiates Top from Bottom?", size=13, bold=True, color=BLUE)
for i, (title, body) in enumerate([
    ("Market Type", "Urban MACs (Thủ Đức, Ecopark) generate higher absolute FYP but rural MACs (Diễn Châu, Vị Thanh) show better target achievement — suggesting targets may need recalibration by market type."),
    ("Recruitment Quality", "Top MACs maintain steady monthly recruitment (4-9 NR/month). Underperformers show spiky patterns — bursts followed by zero months. Consistency matters more than volume."),
    ("Leader Experience", "MAC 04 & 05 under RH K8536/Y8847 with strong industry background. MAC 02 struggles despite same RH — location-specific challenges (Quảng Ninh market saturation)."),
]):
    x = Inches(0.5 + i * 4.2)
    add_box(s, x, Inches(4.4), Inches(3.9), Inches(2.3), fill=LGRAY)
    add_text(s, x + Inches(0.15), Inches(4.5), Inches(3.6), Inches(0.3), title, size=10, bold=True, color=DARK)
    add_text(s, x + Inches(0.15), Inches(4.8), Inches(3.6), Inches(1.8), body, size=9, color=GRAY)
ftr(s, sn)

# ════════════════════════════════════════════════════════════
# SLIDE 5: TEAM SIZE GROWTH TRAJECTORY
# ════════════════════════════════════════════════════════════
sn += 1
s = prs.slides.add_slide(prs.slide_layouts[6])
hdr(s, "TEAM GROWTH", "Team Size Growth Trajectory — 1mAA & New Recruits by Month")

# Monthly team growth data
team = [
    ["Metric","M01","M02","M03","M04","M05","M06","M07","Total"],
    ["New Recruits","32","34","37","24","20","13","5","165*"],
    ["1mAA","40","45","59","38","3","2","2","—"],
    ["CC (Case Count)","52","85","76","52","25","18","2","311"],
    ["Active MACs","7","7","7","7","6","5","2","8"],
]
add_table(s, Inches(0.3), Inches(1.2), Inches(12.7), team)
add_text(s, Inches(0.5), Inches(3.0), Inches(12), Inches(0.3), "*Cumulative NR from monthly data; total NR to date = 139 (some agents counted in contracted month, not monthly breakdown). Suggest: line chart overlay in PPT.", size=8, color=GRAY)

# NR per MAC
add_text(s, Inches(0.5), Inches(3.5), Inches(6), Inches(0.3), "Recruitment by MAC (Cumulative)", size=12, bold=True, color=BLUE)
nr_mac = [
    ["MAC","NR","1mAA","CC","NR/Month\n(avg)","Team\nBuild Rate"],
    ["01 Ecopark","13","19","45","1.4","Slow"],
    ["02 Quảng Yên","8","20","25","1.3","Slow"],
    ["03 Đạ Tẻh","27","27","27","4.5","Fast"],
    ["04 Diễn Châu","22","33","53","3.7","Fast"],
    ["05 Vị Thanh","28","33","41","4.7","Fast"],
    ["06 Yên Bái","12","37","44","2.4","Moderate"],
    ["07 Thủ Đức","25","45","70","6.3","Very Fast"],
    ["08 Vĩnh Phúc","4","4","6","4.0","Early"],
]
add_table(s, Inches(0.3), Inches(3.9), Inches(6.2), nr_mac)

add_box(s, Inches(6.8), Inches(3.5), Inches(6), Inches(3.2), fill=RGBColor(230,247,239))
add_text(s, Inches(6.95), Inches(3.55), Inches(5.7), Inches(0.25), "Team Size vs. Normal GTF Benchmark", size=11, bold=True, color=GREEN)
add_ml(s, Inches(6.95), Inches(3.85), Inches(5.7), Inches(2.8), [
    ("Typical GTF SM team after 6 months: 8-12 agents", True, BLUE),
    ("", False, None),
    ("• MAC 07 (45 1mAA in 4 months) — significantly above benchmark", False, GREEN),
    ("• MAC 04 (33 1mAA in 6 months) — above benchmark", False, GREEN),
    ("• MAC 05 (33 1mAA in 6 months) — above benchmark", False, GREEN),
    ("• MAC 06 (37 1mAA in 5 months) — above benchmark", False, GREEN),
    ("• MAC 01 (19 1mAA in 9 months) — below benchmark pace", False, RED),
    ("• MAC 02 (20 1mAA in 6 months) — at benchmark", False, ORANGE),
    ("", False, None),
    ("Insight: MAC model attracts faster team building than normal GTF due to dedicated office presence and local market focus.", False, DARK),
], size=9)
ftr(s, sn)

# ════════════════════════════════════════════════════════════
# SLIDE 6: QUALITY METRICS & MOC TRACKING
# ════════════════════════════════════════════════════════════
sn += 1
s = prs.slides.add_slide(prs.slide_layouts[6])
hdr(s, "QUALITY TRACKING", "Sales Quality Indicators & MOC Status — All 8 MACs", RED)

# Quality metrics table
qual = [
    ["MAC","Office\nQuality","DC\nCheck","FYP %\nM1-M3","FYP %\nM4-M6","SM MOC\nStatus","P13\nStatus","Overall\nRating"],
    ["01 Ecopark","Green","Pass","369%","70%","Fail","n/a","⚠ Watch"],
    ["02 Quảng Yên","Green","Pass","41%","62%","n/a","n/a","⚠ Watch"],
    ["03 Đạ Tẻh","Green","Pass","167%","13%","n/a","n/a","⚠ Watch"],
    ["04 Diễn Châu","Green","Pass","232%","83%","n/a","n/a","✓ Good"],
    ["05 Vị Thanh","Green","Pass","211%","42%","n/a","n/a","✓ Good"],
    ["06 Yên Bái","Green","Pass","76%","19%","n/a","Pass","✓ Good"],
    ["07 Thủ Đức","Green","Pass","110%","n/a","n/a","Pass","✓ Good"],
    ["08 Vĩnh Phúc","Green","Pass","60%","n/a","n/a","n/a","Early"],
]
add_table(s, Inches(0.3), Inches(1.2), Inches(12.7), qual)

# MOC tracking detail
add_text(s, Inches(0.5), Inches(4.0), Inches(6), Inches(0.3), "MOC Tracking Summary", size=12, bold=True, color=BLUE)
moc = [
    ["MAC","FYP\nOntrack","SM MOC","Office\nQuality","DC/P13","Overall\nMAC Status"],
    ["01 Ecopark","Ontrack","Fail (M9-M12)","Green","Pass","At Risk"],
    ["02 Quảng Yên","Ontrack","n/a","Green","Pass","On Track"],
    ["03 Đạ Tẻh","Ontrack","n/a","Green","Pass","On Track"],
    ["04 Diễn Châu","Ontrack","n/a","Green","Pass","On Track"],
    ["05 Vị Thanh","Ontrack","n/a","Green","Pass","On Track"],
    ["06 Yên Bái","Ontrack","n/a","Green","Pass","On Track"],
    ["07 Thủ Đức","Ontrack","n/a","Green","Pass","On Track"],
    ["08 Vĩnh Phúc","Ontrack","n/a","Green","Pass","On Track"],
]
add_table(s, Inches(0.3), Inches(4.4), Inches(6.2), moc)

add_box(s, Inches(6.8), Inches(4.0), Inches(6), Inches(1.4), fill=RGBColor(253,232,234))
add_text(s, Inches(6.95), Inches(4.05), Inches(5.7), Inches(0.25), "Alert: MAC 01 SM MOC Failure", size=10, bold=True, color=RED)
add_ml(s, Inches(6.95), Inches(4.35), Inches(5.7), Inches(0.9), [
    ("• MAC 01 (Ecopark) failed SM MOC at M9-M12 checkpoint", False, RED),
    ("• Per MAC validation rules: MAC contract maintained, but guaranteed office subsidy stopped", False, DARK),
    ("• Action: Performance improvement plan in place; next review at M12", False, DARK),
    ("• If demoted below SM rank → MAC contract terminated", False, DARK),
], size=9)

add_box(s, Inches(6.8), Inches(5.6), Inches(6), Inches(1.2), fill=RGBColor(230,247,239))
add_text(s, Inches(6.95), Inches(5.65), Inches(5.7), Inches(0.25), "Positive: All MACs Pass Quality & DC", size=10, bold=True, color=GREEN)
add_ml(s, Inches(6.95), Inches(5.95), Inches(5.7), Inches(0.7), [
    ("• 100% Green office quality across all 8 MACs", False, GREEN),
    ("• 100% DC (Due Conduct) pass rate", False, GREEN),
    ("• P13 data available for MAC 06 & 07 — both pass", False, DARK),
    ("• Remaining MACs too early for P13 measurement", False, GRAY),
], size=9)
ftr(s, sn)

# ════════════════════════════════════════════════════════════
# SLIDE 7: 1mAA BENCHMARK ANALYSIS
# ════════════════════════════════════════════════════════════
sn += 1
s = prs.slides.add_slide(prs.slide_layouts[6])
hdr(s, "BENCHMARK", "1mAA Requirement Benchmark — Is the Target Stretch Enough?", BLUE)

# Current MAC 1mAA requirement table
add_text(s, Inches(0.5), Inches(1.2), Inches(6), Inches(0.3), "Current MAC 1mAA Monthly Requirement", size=12, bold=True, color=BLUE)
req = [
    ["Month","M1","M2","M3","M4","M5","M6","M7","M8","M9","M10","M11","M12-24","M25-36"],
    ["1mAA Req","2","2","3","4","5","6","7","8","9","10","10","10/mth","12/mth"],
]
add_table(s, Inches(0.3), Inches(1.6), Inches(12.7), req)

# Benchmark comparison
add_text(s, Inches(0.5), Inches(2.6), Inches(12), Inches(0.3), "Benchmark Comparison", size=13, bold=True, color=BLUE)
bench = [
    ["Benchmark Source","Avg 1mAA\nat M6","Avg 1mAA\nat M12","Notes"],
    ["MAC Requirement","6","10","Current scheme target"],
    ["MAC Actual (avg of 8)","27","—","Significantly exceeds requirement"],
    ["Normal Branch SM (median)","8-10","12-15","Based on internal BAU SM data"],
    ["Industry Benchmark (est.)","6-8","10-12","Competitor franchise model typical range"],
    ["MAC 04 Diễn Châu (best)","33","—","5.5x the M6 requirement"],
    ["MAC 02 Quảng Yên (worst)","20","—","3.3x the M6 requirement"],
]
add_table(s, Inches(0.3), Inches(3.0), Inches(12.7), bench)

# Analysis boxes
add_box(s, Inches(0.5), Inches(5.3), Inches(3.9), Inches(1.5), fill=RGBColor(230,247,239))
add_text(s, Inches(0.65), Inches(5.35), Inches(3.6), Inches(0.25), "Finding: Target Is Achievable", size=10, bold=True, color=GREEN)
add_text(s, Inches(0.65), Inches(5.65), Inches(3.6), Inches(1.0), "All 8 MACs exceed the 1mAA requirement by 3-5x. Even the weakest MAC (02) has 20 1mAA vs. requirement of 6 at M6. The current target appears conservative.", size=9, color=DARK)

add_box(s, Inches(4.7), Inches(5.3), Inches(3.9), Inches(1.5), fill=RGBColor(255,243,224))
add_text(s, Inches(4.85), Inches(5.35), Inches(3.6), Inches(0.25), "Consideration: Raise for Big MAC?", size=10, bold=True, color=ORANGE)
add_text(s, Inches(4.85), Inches(5.65), Inches(3.6), Inches(1.0), "For Big MAC (DRD+ level, 150m2 office), a higher threshold of 12-15/month from M12 may be appropriate given larger investment and higher FYP targets (7-11 bil/year).", size=9, color=DARK)

add_box(s, Inches(8.9), Inches(5.3), Inches(3.9), Inches(1.5), fill=RGBColor(224,240,255))
add_text(s, Inches(9.05), Inches(5.35), Inches(3.6), Inches(0.25), "Recommendation", size=10, bold=True, color=BLUE)
add_text(s, Inches(9.05), Inches(5.65), Inches(3.6), Inches(1.0), "Keep current Normal MAC targets (proven achievable). Set Big MAC threshold at 12/mth from M6 and 15/mth from M12. Review after first Big MAC cohort completes 12 months.", size=9, color=DARK)
ftr(s, sn)

# ════════════════════════════════════════════════════════════
# SLIDE 8: RECRUITMENT PIPELINE & TIMELINE
# ════════════════════════════════════════════════════════════
sn += 1
s = prs.slides.add_slide(prs.slide_layouts[6])
hdr(s, "PIPELINE", "MAC Recruitment Pipeline & Onboarding Timeline")

# Pipeline funnel
add_kpi(s, Inches(0.5), Inches(1.2), "74", "POOL / NOMINEES", BLUE)
add_kpi(s, Inches(3.5), Inches(1.2), "20", "OFFER LETTERS", ORANGE)
add_kpi(s, Inches(6.5), Inches(1.2), "8", "ONBOARDING", GREEN)
add_kpi(s, Inches(9.5), Inches(1.2), "7+1", "OPERATIONAL", GREEN)

# Pipeline detail
pipe = [
    ["Stage","Count","Status","Expected Timeline"],
    ["Completed interview, awaiting confirmation","2","Pending","Q1 2026"],
    ["Location approved, pre-construction","2","Ready","Q1-Q2 2026"],
    ["Under onboarding process","6","In Progress","Q1-Q2 2026"],
    ["Under construction","1","Building","Mar 2026"],
    ["Operational (opened)","7","Live","Since May-Dec 2025"],
]
add_table(s, Inches(0.3), Inches(2.5), Inches(6.2), pipe)

# Specific MAC pipeline
add_text(s, Inches(6.8), Inches(2.5), Inches(6), Inches(0.3), "Detailed Pipeline Status", size=11, bold=True, color=BLUE)
detail = [
    ["MAC Name","Stage","Est. Opening"],
    ["MAC Thanh Sơn","Interview done","Q2 2026"],
    ["MAC Nam Định","Interview done","Q2 2026"],
    ["MAC Bảy Hiền","Location approved","Q2 2026"],
    ["MAC Sơn La","Location approved","Q2 2026"],
    ["MAC Trà Vinh","Onboarding","Q2 2026"],
    ["MAC Phố Nối","Onboarding","Q2 2026"],
    ["MAC Quy Nhơn","Onboarding","H1 2026"],
    ["MAC Cẩm Phả","Onboarding","H1 2026"],
    ["MAC Pleiku","Onboarding","H1 2026"],
    ["MAC Đan Phượng","Onboarding","H1 2026"],
    ["MAC Vĩnh Phúc","Construction","Mar 2026"],
]
add_table(s, Inches(6.5), Inches(2.9), Inches(6.3), detail)

# Forecast box
add_box(s, Inches(0.5), Inches(5.5), Inches(6), Inches(1.3), fill=RGBColor(230,247,239))
add_text(s, Inches(0.65), Inches(5.55), Inches(5.7), Inches(0.25), "Forecast: ~4 new MACs in H1 2026", size=10, bold=True, color=GREEN)
add_ml(s, Inches(0.65), Inches(5.85), Inches(5.7), Inches(0.8), [
    ("• MAC Vĩnh Phúc opening ceremony: 05/03/2026", False, DARK),
    ("• 2 location-approved MACs expected Q1-Q2 2026", False, DARK),
    ("• 6 onboarding MACs expected throughout H1 2026", False, DARK),
    ("• Total operational by end H1 2026: ~12-15 MACs", False, DARK),
], size=9)

add_box(s, Inches(6.8), Inches(5.9), Inches(6), Inches(0.9), fill=RGBColor(255,243,224))
add_text(s, Inches(6.95), Inches(5.95), Inches(5.7), Inches(0.25), "Bottlenecks Identified", size=10, bold=True, color=ORANGE)
add_ml(s, Inches(6.95), Inches(6.2), Inches(5.7), Inches(0.5), [
    ("• Location approval process: avg 2-3 months (CRE & AMkt review)", False, DARK),
    ("• Construction timeline: 1-2 months after location approval", False, DARK),
    ("• Conversion rate: 65 applications → 7 operational (11%)", False, RED),
], size=9)
ftr(s, sn)

# ════════════════════════════════════════════════════════════
# SLIDE 9: RECRUITMENT & SELECTION PROCESS (ENHANCED)
# ════════════════════════════════════════════════════════════
sn += 1
s = prs.slides.add_slide(prs.slide_layouts[6])
hdr(s, "SELECTION PROCESS", "MAC Recruitment & Selection Criteria — Detailed", BLUE)

# Selection criteria detail
add_text(s, Inches(0.5), Inches(1.2), Inches(6), Inches(0.3), "Selection Criteria", size=13, bold=True, color=BLUE)
crit = [
    ["Criteria","Requirement","Rationale"],
    ["FYP L12M","Min 2x Standard FYP Target","Proven production capability"],
    ["# CA L6M","Active case count threshold","Recent activity indicator"],
    ["Income L12M","> VND 1 billion","Financial stability & capability"],
    ["P13 Persistency","> 75% (13M) or > 80% (19M)","Sales quality assurance"],
    ["Work Experience","Min 12 months at current insurer","Stability & commitment"],
    ["Age Range","25-50 years (recommended)","Productive career runway"],
    ["Education","College degree or equivalent","Management capability baseline"],
    ["CIC Credit Check","Clean credit history","Financial responsibility"],
    ["Reference Check","From prior insurer leadership","Character & reputation"],
]
add_table(s, Inches(0.3), Inches(1.6), Inches(6.2), crit)

# Process flow
add_text(s, Inches(6.8), Inches(1.2), Inches(6), Inches(0.3), "Interview & Onboarding Process", size=13, bold=True, color=BLUE)
proc = [
    ["Phase","Step","Owner","Gate"],
    ["1. Screen","Application review","Recruiter/RH","Pass/Fail"],
    ["2. Due Diligence","Background check","Agency Ops","Pass/Fail"],
    ["3. Interview","Official MVL interview","AO + MBA","Stop if Fail"],
    ["4. Committee","MAC committee review","CAO/ASBD/MBA/L1B","Stop if Fail"],
    ["5. Offer","Issue offer letter","Agency Ops","—"],
    ["6. Location","Office location review","CRE & AMkt","Approve/Reject"],
    ["7. Construction","Build-out per standards","MAC SM","Compliance"],
    ["8. Acceptance","Final inspection","CRE & AMkt","Sign-off"],
]
add_table(s, Inches(6.5), Inches(1.6), Inches(6.3), proc)

# Hierarchy mapping
add_text(s, Inches(0.5), Inches(5.0), Inches(12), Inches(0.3), "Competitor Rank Mapping to Manulife Equivalent", size=12, bold=True, color=BLUE)
hier = [
    ["Competitor Rank","Typical Title","MVL Equivalent","MAC Eligibility","Notes"],
    ["Agency Director","AD / GAD","SM / SSM","Normal MAC (SM+)","Most common MAC candidate"],
    ["Senior AD / Branch Mgr","Branch Manager","DRD / RD","Big MAC (DRD+)","Higher investment tier"],
    ["Regional Director","Regional Head","SRD / AVP","Big MAC (DRD+)","Premium candidate"],
    ["Unit Manager","UM / Senior UM","UM+ / AM","Not eligible","Below SM threshold"],
]
add_table(s, Inches(0.3), Inches(5.4), Inches(12.7), hier)
ftr(s, sn)

# ════════════════════════════════════════════════════════════
# SLIDE 10: COMPETITIVE ANALYSIS — Normal MAC vs Big MAC
# ════════════════════════════════════════════════════════════
sn += 1
s = prs.slides.add_slide(prs.slide_layouts[6])
hdr(s, "COMPETITIVE ANALYSIS", "Normal MAC vs. Big MAC — Compensation Comparison", ORANGE)

# Normal MAC comparison
add_text(s, Inches(0.5), Inches(1.2), Inches(6), Inches(0.3), "Normal MAC (SM+ Level) vs. Competitor AD", size=12, bold=True, color=BLUE)
norm = [
    ["Component","MVL Normal MAC\n(SM+)","Competitor\nFranchise AD","MVL\nAdvantage"],
    ["Office Size","~70-100 m2","50-80 m2","Larger"],
    ["FYP Target/Year","3-4.6 bil","2-3 bil","Higher"],
    ["Gross Income/mth","~90 mil","~80-120 mil","Comparable"],
    ["Net Income/mth","~60 mil","~40-60 mil","Higher"],
    ["Office Cost Subsidy","8% FYP + guarantee","Self-funded","Major advantage"],
    ["Setup Cost","100% sponsored","Self-funded","Major advantage"],
    ["Cash Advance","Up to 300-420 mil","Varies","Structured"],
    ["Brand & Support","Full MVL brand","Own brand","Trust factor"],
    ["Risk to Leader","Low (subsidy)","High (self-fund)","Lower risk"],
]
add_table(s, Inches(0.3), Inches(1.6), Inches(6.2), norm)

# Big MAC comparison
add_text(s, Inches(6.8), Inches(1.2), Inches(6), Inches(0.3), "Big MAC (DRD+ Level) vs. Competitor BM/GD", size=12, bold=True, color=BLUE)
big = [
    ["Component","MVL Big MAC\n(DRD+)","Competitor\nBranch Mgr/GD","MVL\nAdvantage"],
    ["Office Size","~150 m2","100-200 m2","Comparable"],
    ["FYP Target/Year","7-11 bil","5-8 bil","Higher"],
    ["Gross Income/mth","~160 mil","~120-200 mil","Comparable"],
    ["Net Income/mth","~110 mil","~60-100 mil","Higher"],
    ["Office Cost Subsidy","8% FYP + guarantee","Self-funded","Major advantage"],
    ["Setup Cost","100% sponsored","Self-funded","Major advantage"],
    ["Cash Advance","Up to 720 mil","Varies","Higher cap"],
    ["Sign-on Bonus","Up to 2.5 bil","Varies","Structured"],
    ["Risk to Leader","Low (subsidy)","High (self-fund)","Lower risk"],
]
add_table(s, Inches(6.5), Inches(1.6), Inches(6.3), big)

# Key differentiator
add_box(s, Inches(0.5), Inches(5.6), Inches(12.3), Inches(1.2), fill=RGBColor(230,247,239))
add_text(s, Inches(0.65), Inches(5.65), Inches(12), Inches(0.25), "Key Competitive Advantage: Hybrid Model = Lower Risk + Higher Support", size=11, bold=True, color=GREEN)
add_ml(s, Inches(0.65), Inches(5.95), Inches(11.8), Inches(0.7), [
    ("• Unlike pure franchise models, MAC provides financial safety net (guaranteed subsidy) while maintaining entrepreneurial incentive (variable 8% FYP)", False, DARK),
    ("• Setup cost fully sponsored eliminates the #1 barrier for competitor leaders considering a move", False, DARK),
    ("• Manulife brand presence (signage, standards) provides immediate credibility in new markets — competitors must build from scratch", False, DARK),
], size=9)
ftr(s, sn)

# ════════════════════════════════════════════════════════════
# SLIDE 11: VISION & AMBITION — 2-Year MAC Program
# ════════════════════════════════════════════════════════════
sn += 1
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, DARK)
add_box(s, Inches(0.5), Inches(0.3), Inches(2.2), Inches(0.3), fill=RGBColor(50,50,70), text="VISION & AMBITION", fs=8, color=GREEN, bold=True, align=PP_ALIGN.CENTER)
add_text(s, Inches(0.5), Inches(0.7), Inches(12), Inches(0.5), "MAC Program 2-Year Ambition (2026-2027)", size=22, bold=True, color=WHITE)

# 4 pillars
pillars = [
    ("Scale", "30+", "Target MACs by end 2027\n(8 today → 15 by H2'26 → 30+ by 2027)", GREEN),
    ("Contribution", "3-5%", "Target % of total Agency FYP\n(0.6% today → 2% by end 2026 → 3-5% by 2027)", BLUE),
    ("Geography", "15+", "New provinces covered\n(Currently in 8 locations across 7 provinces;\ntarget 20+ provinces by 2027)", ORANGE),
    ("Talent", "50+", "Inorganic leaders attracted\n(Pipeline of 74 nominees;\ntarget 50+ contracted by 2027)", RGBColor(180,130,255)),
]
for i, (title, val, desc, accent) in enumerate(pillars):
    x = Inches(0.4 + i * 3.2)
    add_box(s, x, Inches(1.4), Inches(3.0), Inches(2.8), fill=RGBColor(40,40,60))
    bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, Inches(1.4), Inches(0.06), Inches(2.8))
    bar.fill.solid(); bar.fill.fore_color.rgb = accent; bar.line.fill.background(); bar.shadow.inherit = False
    add_text(s, x + Inches(0.2), Inches(1.5), Inches(2.6), Inches(0.3), title, size=12, color=accent, bold=True)
    add_text(s, x + Inches(0.2), Inches(1.85), Inches(2.6), Inches(0.5), val, size=30, color=WHITE, bold=True)
    add_text(s, x + Inches(0.2), Inches(2.45), Inches(2.6), Inches(1.5), desc, size=9, color=RGBColor(170,170,187))

# Strategic positioning
add_box(s, Inches(0.5), Inches(4.5), Inches(6), Inches(2.2), fill=RGBColor(0,40,25))
bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.5), Inches(4.5), Inches(0.06), Inches(2.2))
bar.fill.solid(); bar.fill.fore_color.rgb = GREEN; bar.line.fill.background(); bar.shadow.inherit = False
add_text(s, Inches(0.7), Inches(4.55), Inches(5.6), Inches(0.25), "Strategic Positioning vs. Competitors", size=11, bold=True, color=GREEN)
add_ml(s, Inches(0.7), Inches(4.85), Inches(5.6), Inches(1.7), [
    ("• Prudential: ~200 GAs nationwide (fully franchise)", False, RGBColor(170,170,187)),
    ("• Dai-ichi: ~100 franchise offices", False, RGBColor(170,170,187)),
    ("• AIA: ~80 franchise offices", False, RGBColor(170,170,187)),
    ("• Manulife today: 43 branches + 8 MACs", False, WHITE),
    ("• Manulife 2027 target: 43 branches + 30 MACs = 73 locations", False, GREEN),
    ("", False, None),
    ("MAC bridges the gap without cannibalizing branch model", True, GREEN),
], size=9)

# Geographic expansion
add_box(s, Inches(6.8), Inches(4.5), Inches(6), Inches(2.2), fill=RGBColor(0,25,50))
bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.8), Inches(4.5), Inches(0.06), Inches(2.2))
bar.fill.solid(); bar.fill.fore_color.rgb = BLUE; bar.line.fill.background(); bar.shadow.inherit = False
add_text(s, Inches(7.0), Inches(4.55), Inches(5.6), Inches(0.25), "Geographic Expansion Plan", size=11, bold=True, color=BLUE)
add_ml(s, Inches(7.0), Inches(4.85), Inches(5.6), Inches(1.7), [
    ("Phase 1 (2025-H1'26): Pilot in 8 diverse locations ✓", False, GREEN),
    ("Phase 2 (H2'26): Scale to 15 MACs in proven markets", False, WHITE),
    ("Phase 3 (2027): Expand to 30+ MACs covering 20+ provinces", False, WHITE),
    ("", False, None),
    ("Priority regions: Mekong Delta, Central Highlands,", False, RGBColor(170,170,187)),
    ("Northern Mountains — areas with no MVL branch presence", False, RGBColor(170,170,187)),
    ("but significant insurance market potential", False, RGBColor(170,170,187)),
], size=9)
ftr(s, sn)

# ════════════════════════════════════════════════════════════
# SLIDE 12: INTERNAL MAC — Branch Closure Transition
# ════════════════════════════════════════════════════════════
sn += 1
s = prs.slides.add_slide(prs.slide_layouts[6])
hdr(s, "INTERNAL MAC", "Branch Closure → MAC Transition Proposal", RED)

add_kpi(s, Inches(0.5), Inches(1.2), "16-17", "BRANCHES CLOSING 2026", RED)
add_kpi(s, Inches(3.5), Inches(1.2), "~30-50", "EST. SM+ LEADERS AFFECTED", ORANGE)
add_kpi(s, Inches(6.5), Inches(1.2), "~10-15", "POTENTIAL INTERNAL MACs", GREEN)
add_kpi(s, Inches(9.5), Inches(1.2), "Same", "COMPENSATION STRUCTURE", BLUE)

# Eligibility criteria
add_text(s, Inches(0.5), Inches(2.5), Inches(6), Inches(0.3), "Internal MAC Eligibility Criteria", size=12, bold=True, color=BLUE)
elig = [
    ["Criteria","Requirement","Notes"],
    ["Current Rank","SM or above","Must hold SM+ rank at time of transition"],
    ["Tenure at MVL","Min 24 months","Proven track record within Manulife"],
    ["FYP Achievement","Min 80% of target L12M","Demonstrates production capability"],
    ["Team Size","Min 5 active agents","Has existing team to transfer"],
    ["Location","Outside existing branch coverage","No overlap with remaining branches"],
    ["Quality","No DC/P13 flags","Clean conduct record"],
    ["Willingness","Voluntary opt-in","Not forced transition"],
]
add_table(s, Inches(0.3), Inches(2.9), Inches(6.2), elig)

# Transition support
add_text(s, Inches(6.8), Inches(2.5), Inches(6), Inches(0.3), "Transition Support Plan", size=12, bold=True, color=BLUE)
trans = [
    ["Support Item","Detail"],
    ["Office Setup","Same MAC setup subsidy (410 mil)"],
    ["Transition Period","3-month overlap with branch closure"],
    ["Team Transfer","Existing agents transfer to MAC office"],
    ["Compensation","Same MAC scheme (8% FYP + guarantee)"],
    ["Target Adjustment","Reduced target for first 6 months (80%)"],
    ["Mentoring","Paired with successful MAC operator"],
    ["Fallback","Can return to nearest branch if MAC fails"],
]
add_table(s, Inches(6.5), Inches(2.9), Inches(6.3), trans)

# Key differences
add_text(s, Inches(0.5), Inches(5.7), Inches(12), Inches(0.3), "Internal MAC vs. Inorganic/GTF MAC — Key Differences", size=12, bold=True, color=BLUE)
diff = [
    ["Aspect","Internal MAC","Inorganic/GTF MAC"],
    ["Source","Existing MVL SM+ from closing branches","External recruitment from competitors"],
    ["Compensation","Same MAC scheme, count new agents only after MAC","Same MAC scheme + GTF bonus + sign-on"],
    ["Cash Advance","Not applicable","Up to 80% of debts (300-720 mil)"],
    ["Setup Subsidy","Same (410 mil)","Same (410 mil)"],
    ["Guarantee Subsidy","Same (40m Y1-2, 30m Y3)","Same (40m Y1-2, 30m Y3)"],
    ["Risk Level","Lower (known leader)","Higher (new to MVL)"],
]
add_table(s, Inches(0.3), Inches(6.1), Inches(12.7), diff)
ftr(s, sn)

# ════════════════════════════════════════════════════════════
# SLIDE 13: COMPENSATION SUMMARY — Total Income from MAC Scheme
# ════════════════════════════════════════════════════════════
sn += 1
s = prs.slides.add_slide(prs.slide_layouts[6])
hdr(s, "COMPENSATION", "MAC Scheme Total Income & SM+ Compensation Summary")

# Income summary from actual data
add_text(s, Inches(0.5), Inches(1.2), Inches(12), Inches(0.3), "Actual Compensation Paid to Date (mil VND)", size=12, bold=True, color=BLUE)
comp = [
    ["MAC","Total Income\nfrom MAC\nScheme","Total SM+\nCompensation","Total\nAllowance\nPaid","Months\nActive","Avg Monthly\nMAC Income","Avg Monthly\nSM+ Comp"],
    ["01 Ecopark","9.74","1.28","224","9","1.08","0.14"],
    ["02 Quảng Yên","9.60","0.42","100","6","1.60","0.07"],
    ["03 Đạ Tẻh","6.40","0.60","160","6","1.07","0.10"],
    ["04 Diễn Châu","7.20","1.14","140","6","1.20","0.19"],
    ["05 Vị Thanh","8.00","0.87","160","6","1.33","0.15"],
    ["06 Yên Bái","5.12","0.71","84","5","1.02","0.14"],
    ["07 Thủ Đức","5.28","1.28","44","4","1.32","0.32"],
    ["08 Vĩnh Phúc","3.20","0.10","0","1","3.20","0.10"],
    ["Total","54.54","6.38","912","—","—","—"],
]
add_table(s, Inches(0.3), Inches(1.6), Inches(12.7), comp)

# Insight
add_box(s, Inches(0.5), Inches(5.0), Inches(6), Inches(1.8), fill=RGBColor(230,247,239))
add_text(s, Inches(0.65), Inches(5.05), Inches(5.7), Inches(0.25), "MAC Scheme Income Analysis", size=10, bold=True, color=GREEN)
add_ml(s, Inches(0.65), Inches(5.35), Inches(5.7), Inches(1.3), [
    ("• Total MAC scheme income: 54.54 mil across 8 MACs", False, DARK),
    ("• Total SM+ compensation: 6.38 mil", False, DARK),
    ("• Total allowance paid: ~912 mil (office subsidy)", False, DARK),
    ("• MAC as % of Agency FYP: 0.6% (early stage)", False, DARK),
    ("• GTF FYP contribution: ~20% of inorganic group", False, DARK),
], size=9)

add_box(s, Inches(6.8), Inches(5.0), Inches(6), Inches(1.8), fill=RGBColor(224,240,255))
add_text(s, Inches(6.95), Inches(5.05), Inches(5.7), Inches(0.25), "Cost Efficiency Outlook", size=10, bold=True, color=BLUE)
add_ml(s, Inches(6.95), Inches(5.35), Inches(5.7), Inches(1.3), [
    ("• Current total cost/FYP: ~68% (high due to setup costs)", False, DARK),
    ("• Excluding one-off setup: ~15% (allowance only)", False, GREEN),
    ("• Target steady-state: 8% FYP (allowance) + ~5% overhead = ~13%", False, DARK),
    ("• vs. Branch model: ~16-20% FYP for office operations", False, DARK),
    ("• MAC model is more cost-efficient at steady state", True, GREEN),
], size=9)
ftr(s, sn)

# ════════════════════════════════════════════════════════════
# SLIDE 14: LESSONS LEARNT & NEXT STEPS
# ════════════════════════════════════════════════════════════
sn += 1
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, DARK)
add_box(s, Inches(0.5), Inches(0.3), Inches(2.2), Inches(0.3), fill=RGBColor(50,50,70), text="LESSONS & NEXT STEPS", fs=8, color=GREEN, bold=True, align=PP_ALIGN.CENTER)
add_text(s, Inches(0.5), Inches(0.7), Inches(12), Inches(0.5), "Pilot Review Summary & Recommendations", size=22, bold=True, color=WHITE)

# What worked
add_box(s, Inches(0.4), Inches(1.4), Inches(4.0), Inches(2.8), fill=RGBColor(0,40,25))
bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.4), Inches(1.4), Inches(0.06), Inches(2.8))
bar.fill.solid(); bar.fill.fore_color.rgb = GREEN; bar.line.fill.background(); bar.shadow.inherit = False
add_text(s, Inches(0.6), Inches(1.5), Inches(3.6), Inches(0.3), "What Worked Well", size=12, color=GREEN, bold=True)
add_ml(s, Inches(0.6), Inches(1.85), Inches(3.6), Inches(2.2), [
    ("• 5/8 MACs at or above target (63%)", False, WHITE),
    ("• 100% Green office quality", False, WHITE),
    ("• 100% DC pass rate", False, WHITE),
    ("• Strong recruitment in rural markets", False, WHITE),
    ("• MAC 04 & 07 as clear success stories", False, WHITE),
    ("• Team building faster than normal GTF", False, WHITE),
], size=9)

# What needs improvement
add_box(s, Inches(4.6), Inches(1.4), Inches(4.0), Inches(2.8), fill=RGBColor(50,30,10))
bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(4.6), Inches(1.4), Inches(0.06), Inches(2.8))
bar.fill.solid(); bar.fill.fore_color.rgb = ORANGE; bar.line.fill.background(); bar.shadow.inherit = False
add_text(s, Inches(4.8), Inches(1.5), Inches(3.6), Inches(0.3), "What Needs Improvement", size=12, color=ORANGE, bold=True)
add_ml(s, Inches(4.8), Inches(1.85), Inches(3.6), Inches(2.2), [
    ("• MAC 02 underperforming (57%)", False, WHITE),
    ("• MAC 01 SM MOC failure", False, WHITE),
    ("• FYP volatility month-to-month", False, WHITE),
    ("• Pipeline conversion rate low (11%)", False, WHITE),
    ("• Location approval bottleneck", False, WHITE),
    ("• P13 data still limited for most MACs", False, WHITE),
], size=9)

# Recommendations
add_box(s, Inches(8.8), Inches(1.4), Inches(4.2), Inches(2.8), fill=RGBColor(15,25,50))
bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(8.8), Inches(1.4), Inches(0.06), Inches(2.8))
bar.fill.solid(); bar.fill.fore_color.rgb = BLUE; bar.line.fill.background(); bar.shadow.inherit = False
add_text(s, Inches(9.0), Inches(1.5), Inches(3.8), Inches(0.3), "Recommendations", size=12, color=BLUE, bold=True)
add_ml(s, Inches(9.0), Inches(1.85), Inches(3.8), Inches(2.2), [
    ("• Approve MAC for ongoing implementation", False, GREEN),
    ("• Launch Big MAC tier for DRD+ candidates", False, WHITE),
    ("• Introduce Internal MAC for branch closures", False, WHITE),
    ("• Streamline location approval process", False, WHITE),
    ("• Set higher 1mAA threshold for Big MAC", False, WHITE),
    ("• Quarterly performance review cadence", False, WHITE),
], size=9)

# Bottom summary
add_box(s, Inches(0.5), Inches(4.5), Inches(12.3), Inches(2.2), fill=RGBColor(40,40,60))
bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.5), Inches(4.5), Inches(0.06), Inches(2.2))
bar.fill.solid(); bar.fill.fore_color.rgb = GREEN; bar.line.fill.background(); bar.shadow.inherit = False
add_text(s, Inches(0.7), Inches(4.6), Inches(11.8), Inches(0.3), "Conclusion", size=13, bold=True, color=GREEN)
add_ml(s, Inches(0.7), Inches(4.95), Inches(11.8), Inches(1.5), [
    ("The MAC pilot has demonstrated the viability of the hybrid model. With 93% aggregate target achievement across 8 offices, strong recruitment momentum (139 NR, 218 1mAA), and 100% quality compliance, the program is ready for scale-up.", False, WHITE),
    ("", False, None),
    ("Key ask: Approve (1) ongoing MAC implementation with refined scheme, (2) Big MAC tier for DRD+ level, and (3) Internal MAC pathway for leaders affected by 16-17 branch closures in 2026.", False, RGBColor(170,170,187)),
    ("", False, None),
    ("Total investment to date: ~4.2 bil VND across 8 MACs generating 6.2 bil FYP. Projected steady-state cost efficiency: ~13% of FYP vs. ~16-20% for branch model.", False, RGBColor(170,170,187)),
], size=10)
ftr(s, sn)

# ════════════════════════════════════════════════════════════
# SAVE
# ════════════════════════════════════════════════════════════
out = "/home/ubuntu/nspaceresearch/na/output/mac-proposal/mac-pilot-review-additional-slides.pptx"
prs.save(out)
print(f"Saved {sn} slides to {out}")
