"""
vi-de orchestrator (bilingual-parity-expansion) — Creates 5 collections, 27 series,
wires them together, and sets display orders for the Vietnamese-German language pair.

NOTE: This orchestrator REPLACES the old multilingual-curriculum-expansion orchestrator
that created 4 collections with 20 series (100 curriculums). Those old collections/series
already exist in the database. This script creates ENTIRELY NEW infrastructure for the
bilingual-parity-expansion spec.

Language pair: userLanguage=vi (Vietnamese speakers), language=de (learning German)
User-facing text (titles, descriptions): Vietnamese
Reading passages: German

Target: 155 curriculums (60 beginner, 56 preintermediate, 39 intermediate)

Distribution across 5 collections, 27 series:
  Collection A: Đời Sống Hàng Ngày (Alltag und Reisen) — 7 series, 42 curriculums
  Collection B: Kinh Doanh và Nghề Nghiệp (Geschäft und Beruf) — 6 series, 34 curriculums
  Collection C: Học Thuật và Khoa Học (Akademisch und Wissenschaft) — 6 series, 34 curriculums
  Collection D: Văn Hóa và Xã Hội (Kultur und Gesellschaft) — 4 series, 22 curriculums
  Collection E: Thiên Nhiên và Đổi Mới (Natur und Innovation) — 4 series, 23 curriculums

Tone assignments are pre-computed via tone_assigner.assign_tones_for_language_pair(5, 7, 7),
which generates 245 tone slots across a uniform 5x7x7 grid. The orchestrator uses only the
slots needed for each collection's actual series count (A=7, B=6, C=6, D=4, E=4) and each
series' actual curriculum count (5, 6, or 7). Unused slots are simply not consumed.

All series descriptions are short persuasive Vietnamese hooks (<=255 chars) using the assigned tone.
Collection descriptions are short informative Vietnamese summaries (not persuasive copy).

Requirements: 6.1-6.8, 8.1-8.4, 8.7
"""

import sys
import logging

sys.path.insert(0, "/home/ubuntu/nspaceresearch2/design-curriculums")
sys.path.insert(0, "/home/ubuntu/nspaceresearch2/design-curriculums/vi-de")
import tone_assigner
from api_helpers import (
    create_collection,
    create_series,
    add_series_to_collection,
    set_series_display_order,
    set_collection_display_order,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Tone assignments
# ---------------------------------------------------------------------------
# The tone_assigner requires uniform series-per-collection and curriculums-per-series
# counts. We request a 5 x 7 x 7 grid (245 tone slots) — enough to cover the maximum
# of 7 series per collection and 7 curriculums per series. Collections with fewer
# series (B,C=6; D,E=4) simply ignore extra series slots; series with fewer curriculums
# (5 or 6 instead of 7) ignore extra curriculum slots.
#
# The assigner already enforces:
#   - No adjacent duplicate description tones (curriculums within a series,
#     series within a collection)
#   - No adjacent duplicate farewell tones (curriculums within a series)
#   - No single description tone exceeds 30% across the whole pair
tones = tone_assigner.assign_tones_for_language_pair(5, 7, 7)

# ---------------------------------------------------------------------------
# Tone reference (from tone_assigner output, collections A-E):
# ---------------------------------------------------------------------------
#
# Collection A (Doi Song Hang Ngay): description_tone = provocative_question
#   Series A1: bold_declaration     — 6 curriculums  (desc_tone + farewell_tone per curriculum below)
#   Series A2: vivid_scenario       — 6 curriculums
#   Series A3: empathetic_observation — 6 curriculums
#   Series A4: surprising_fact      — 6 curriculums
#   Series A5: metaphor_led         — 6 curriculums
#   Series A6: provocative_question — 6 curriculums
#   Series A7: bold_declaration     — 6 curriculums
#
# Collection B (Kinh Doanh va Nghe Nghiep): description_tone = bold_declaration
#   Series B1: vivid_scenario       — 6 curriculums
#   Series B2: empathetic_observation — 6 curriculums
#   Series B3: surprising_fact      — 6 curriculums
#   Series B4: metaphor_led         — 6 curriculums
#   Series B5: provocative_question — 5 curriculums
#   Series B6: bold_declaration     — 5 curriculums
#
# Collection C (Hoc Thuat va Khoa Hoc): description_tone = vivid_scenario
#   Series C1: empathetic_observation — 6 curriculums
#   Series C2: surprising_fact      — 6 curriculums
#   Series C3: metaphor_led         — 6 curriculums
#   Series C4: provocative_question — 6 curriculums
#   Series C5: bold_declaration     — 5 curriculums
#   Series C6: vivid_scenario       — 5 curriculums
#
# Collection D (Van Hoa va Xa Hoi): description_tone = empathetic_observation
#   Series D1: surprising_fact      — 6 curriculums
#   Series D2: metaphor_led         — 6 curriculums
#   Series D3: provocative_question — 5 curriculums
#   Series D4: bold_declaration     — 5 curriculums
#
# Collection E (Thien Nhien va Doi Moi): description_tone = surprising_fact
#   Series E1: metaphor_led         — 6 curriculums
#   Series E2: provocative_question — 6 curriculums
#   Series E3: bold_declaration     — 6 curriculums
#   Series E4: vivid_scenario       — 5 curriculums
#
# Per-curriculum description + farewell tones are printed to stdout at the end of
# this script (see the "Tone Assignments" section), and the curriculum create_*.py
# scripts (tasks 11.3-11.5) will reference that output.

# ---------------------------------------------------------------------------
# Collection definitions — Vietnamese titles with German labels,
# informative summaries (not persuasive copy)
# ---------------------------------------------------------------------------
COLLECTIONS = [
    {
        "title": "Đời Sống Hàng Ngày (Alltag und Reisen)",
        "description": (
            "Tiếng Đức cho các tình huống thường nhật: du lịch, ẩm thực, mua sắm, "
            "giao tiếp xã hội, sức khỏe và nhà ở. Mỗi chủ đề trang bị từ vựng và sự tự tin "
            "để bạn xử lý hội thoại thực tế khi sống hoặc du lịch tại các nước nói tiếng Đức."
        ),
    },
    {
        "title": "Kinh Doanh và Nghề Nghiệp (Geschäft und Beruf)",
        "description": (
            "Tiếng Đức chuyên ngành cho môi trường công sở, tìm việc, vận hành doanh nghiệp "
            "và thương mại quốc tế. Từ email và cuộc họp đến đàm phán hợp đồng — xây dựng "
            "kỹ năng ngôn ngữ cần thiết để phát triển sự nghiệp trong thị trường Đức ngữ."
        ),
    },
    {
        "title": "Học Thuật và Khoa Học (Akademisch und Wissenschaft)",
        "description": (
            "Tiếng Đức học thuật qua các lĩnh vực khoa học, kinh tế, lịch sử, tâm lý học "
            "và triết học. Phù hợp cho người muốn đọc tài liệu chuyên sâu, tham gia thảo luận "
            "trí tuệ hoặc chuẩn bị du học tại các trường đại học Đức ngữ."
        ),
    },
    {
        "title": "Văn Hóa và Xã Hội (Kultur und Gesellschaft)",
        "description": (
            "Tiếng Đức về nghệ thuật, kiến trúc, truyền thông và truyền thống văn hóa. "
            "Mỗi series mở ra một góc nhìn khác về đời sống văn hóa Đức ngữ, giúp bạn "
            "trò chuyện sâu sắc hơn vượt xa phạm vi giao tiếp thông thường."
        ),
    },
    {
        "title": "Thiên Nhiên và Đổi Mới (Natur und Innovation)",
        "description": (
            "Tiếng Đức về môi trường, bền vững, công nghệ và thể thao. Khám phá từ vựng "
            "cho những chủ đề đang định hình tương lai — từ năng lượng tái tạo đến đổi mới "
            "kỹ thuật số trong bối cảnh Đức ngữ."
        ),
    },
]

# ---------------------------------------------------------------------------
# Series definitions — Vietnamese titles with German topic labels
# Descriptions: short persuasive hooks <=255 chars using the series' assigned tone
# The "count" field records the number of curriculums planned per series, for
# total-count verification (should sum to 155).
# ---------------------------------------------------------------------------
SERIES = {
    # ===== Collection A: Doi Song Hang Ngay — 7 series, 42 curriculums =====
    "A": [
        {
            # A1 — tone: bold_declaration
            "title": "Ẩm Thực và Nhà Hàng (Essen und Gastronomie)",
            "description": (
                "Từ vựng ẩm thực Đức không chỉ là từ ngữ — đó là chìa khóa mở ra cả một nền "
                "văn hóa. Từ gọi món tại Gasthaus đến trò chuyện ở chợ, bạn sẽ tự tin bước vào "
                "bất kỳ nhà hàng Đức nào."
            ),
            "count": 6,
        },
        {
            # A2 — tone: vivid_scenario
            "title": "Di Chuyển và Giao Thông (Stadtnavigation und Verkehr)",
            "description": (
                "Hãy tưởng tượng bạn đứng giữa ga Berlin Hauptbahnhof, dòng người cuồn cuộn — "
                "và bạn biết chính xác phải nói gì để tìm đúng sân ga. Đó là sức mạnh series này "
                "trao cho bạn."
            ),
            "count": 6,
        },
        {
            # A3 — tone: empathetic_observation
            "title": "Mua Sắm và Dịch Vụ (Einkaufen und Dienstleistungen)",
            "description": (
                "Bạn đã bao giờ muốn hỏi giá, đổi size hay mở tài khoản ngân hàng bằng tiếng "
                "Đức mà không biết bắt đầu từ đâu? Series này sinh ra cho khoảnh khắc ấy."
            ),
            "count": 6,
        },
        {
            # A4 — tone: surprising_fact
            "title": "Đời Sống Xã Hội (Soziales Leben und Beziehungen)",
            "description": (
                "Người Đức phân biệt rõ ràng giữa \"du\" và \"Sie\" — sai một từ có thể thay đổi "
                "cả mối quan hệ. Nắm vững giao tiếp xã hội giúp bạn hòa nhập thay vì chỉ tồn tại."
            ),
            "count": 6,
        },
        {
            # A5 — tone: metaphor_led
            "title": "Sức Khỏe và Thể Chất (Gesundheit und Wohlbefinden)",
            "description": (
                "Sức khỏe là tấm hộ chiếu thứ hai khi sống ở nước ngoài. Series này trang bị "
                "từ vựng y tế, thể dục và chăm sóc bản thân — chìa khóa mở mọi cánh cửa "
                "phòng khám và Apotheke."
            ),
            "count": 6,
        },
        {
            # A6 — tone: provocative_question
            "title": "Nhà Ở và Sinh Hoạt (Zuhause und Wohnen)",
            "description": (
                "Bạn có thể thuê nhà, tranh luận hóa đơn Nebenkosten hay đăng ký tại Bürgeramt "
                "hoàn toàn bằng tiếng Đức không? Nếu chưa, series này là con đường ngắn nhất."
            ),
            "count": 6,
        },
        {
            # A7 — tone: bold_declaration
            "title": "Du Lịch và Khám Phá (Reisen und Tourismus)",
            "description": (
                "Du lịch thật sự bắt đầu khi tiếng Đức sách hướng dẫn kết thúc. Đặt phòng, "
                "tìm hành lý thất lạc hay tham gia Wanderung — series này biến bạn thành lữ "
                "khách, không phải du khách."
            ),
            "count": 6,
        },
    ],
    # ===== Collection B: Kinh Doanh va Nghe Nghiep — 6 series, 34 curriculums =====
    "B": [
        {
            # B1 — tone: vivid_scenario
            "title": "Giao Tiếp Công Sở (Kommunikation am Arbeitsplatz)",
            "description": (
                "Hình dung bạn đang trình bày trước phòng họp toàn đồng nghiệp Đức — tự tin, "
                "mạch lạc, chuyên nghiệp. Series này đưa bạn từ email ngày đầu đến thuyết trình "
                "không vấp váp."
            ),
            "count": 6,
        },
        {
            # B2 — tone: empathetic_observation
            "title": "Tìm Việc và Sự Nghiệp (Jobsuche und Karriere)",
            "description": (
                "Viết Lebenslauf bằng tiếng Đức đã khó, phỏng vấn còn khó hơn. Nếu bạn đang "
                "theo đuổi cơ hội nghề nghiệp trong vùng DACH, đây là bước đệm bạn cần."
            ),
            "count": 6,
        },
        {
            # B3 — tone: surprising_fact
            "title": "Từ Vựng Chuyên Ngành (Branchenspezifischer Wortschatz)",
            "description": (
                "Mỗi ngành có một \"ngôn ngữ Đức\" riêng — từ IT đến khách sạn, từ sản xuất "
                "Mittelstand đến logistics toàn cầu. Nắm đúng thuật ngữ, bạn được tôn trọng "
                "ngay lập tức."
            ),
            "count": 6,
        },
        {
            # B4 — tone: metaphor_led
            "title": "Vận Hành Doanh Nghiệp (Geschäftsbetrieb)",
            "description": (
                "Doanh nghiệp như một cỗ máy — quản lý dự án là bánh răng, ngân sách là nhiên "
                "liệu, tuân thủ là phanh. Series này giúp bạn vận hành cỗ máy ấy bằng tiếng Đức."
            ),
            "count": 6,
        },
        {
            # B5 — tone: provocative_question
            "title": "Kinh Doanh Quốc Tế (Internationaler Handel)",
            "description": (
                "Bạn có thể đàm phán hợp đồng triệu euro bằng tiếng Đức không? Từ Incoterms "
                "đến văn hóa kinh doanh, series này biến bạn thành đối tác đáng gờm trên bàn "
                "đàm phán."
            ),
            "count": 5,
        },
        {
            # B6 — tone: bold_declaration
            "title": "Khởi Nghiệp và Đổi Mới (Unternehmertum und Innovation)",
            "description": (
                "Berlin, München và Wien là trung tâm startup châu Âu. Nếu bạn đang sáng lập, "
                "gọi vốn hay gia nhập Gründerteam, tiếng Đức là lợi thế không thể bỏ qua."
            ),
            "count": 5,
        },
    ],
    # ===== Collection C: Hoc Thuat va Khoa Hoc — 6 series, 34 curriculums =====
    "C": [
        {
            # C1 — tone: empathetic_observation
            "title": "Khoa Học và Công Nghệ (Wissenschaft und Technologie)",
            "description": (
                "Đọc bài báo khoa học bằng tiếng Đức mà cảm thấy lạc lõng? Bạn không đơn độc. "
                "Series này xây nền tảng từ vựng từ sinh học đến tin học để bạn tiếp cận tự tin."
            ),
            "count": 6,
        },
        {
            # C2 — tone: surprising_fact
            "title": "Kinh Tế và Tài Chính (Wirtschaft und Finanzen)",
            "description": (
                "Đức là nền kinh tế lớn nhất châu Âu, nhưng hầu hết người học bỏ qua từ vựng "
                "tài chính. Từ vi mô đến vĩ mô, từ Sparkasse đến DAX — series này lấp đầy "
                "khoảng trống."
            ),
            "count": 6,
        },
        {
            # C3 — tone: metaphor_led
            "title": "Lịch Sử và Chính Trị (Geschichte und Politik)",
            "description": (
                "Lịch sử là tấm gương, chính trị là ánh sáng chiếu vào đó. Series này giúp bạn "
                "đọc hiểu và thảo luận về quá khứ lẫn hiện tại của châu Âu Đức ngữ."
            ),
            "count": 6,
        },
        {
            # C4 — tone: provocative_question
            "title": "Tâm Lý và Giáo Dục (Psychologie und Bildung)",
            "description": (
                "Tại sao trẻ em học ngôn ngữ nhanh hơn người lớn? Tâm lý học và giáo dục có "
                "câu trả lời — series này dạy bạn cách nói về điều đó bằng tiếng Đức."
            ),
            "count": 6,
        },
        {
            # C5 — tone: bold_declaration
            "title": "Triết Học và Tư Duy (Philosophie und kritisches Denken)",
            "description": (
                "Triết học Đức định hình tư tưởng phương Tây suốt nhiều thế kỷ — từ Kant đến "
                "Habermas. Nắm vững từ vựng triết học là bước đầu tham gia những cuộc tranh luận "
                "sâu sắc nhất."
            ),
            "count": 5,
        },
        {
            # C6 — tone: vivid_scenario
            "title": "Nghiên Cứu và Viết Học Thuật (Forschung und wissenschaftliches Schreiben)",
            "description": (
                "Hãy tưởng tượng bạn ngồi trong Seminar ở Heidelberg, phân tích một bài luận "
                "bằng tiếng Đức. Series này trang bị từ vựng học thuật để bạn viết và trình bày "
                "tự tin."
            ),
            "count": 5,
        },
    ],
    # ===== Collection D: Van Hoa va Xa Hoi — 4 series, 22 curriculums =====
    "D": [
        {
            # D1 — tone: surprising_fact
            "title": "Nghệ Thuật và Văn Học (Kunst und Literatur)",
            "description": (
                "Các nhà văn Đức ngữ đã giành nhiều giải Nobel Văn học hơn hầu hết mọi nhóm "
                "ngôn ngữ khác. Series này mở cánh cửa để bạn nói về nghệ thuật như người bản xứ."
            ),
            "count": 6,
        },
        {
            # D2 — tone: metaphor_led
            "title": "Kiến Trúc và Thiết Kế (Architektur und Design)",
            "description": (
                "Kiến trúc là ngôn ngữ thầm lặng của một thành phố. Từ Bauhaus đến Passivhaus, "
                "series này dạy bạn đọc và kể câu chuyện của thế giới xây dựng bằng tiếng Đức."
            ),
            "count": 6,
        },
        {
            # D3 — tone: provocative_question
            "title": "Truyền Thông và Báo Chí (Medien und Journalismus)",
            "description": (
                "Bạn có thể hiểu bản tin Tagesschau sau mười giây đầu tiên không? Series này "
                "dẫn bạn qua ngôn ngữ tin tức, tranh luận và truyền thông số bằng tiếng Đức."
            ),
            "count": 5,
        },
        {
            # D4 — tone: bold_declaration
            "title": "Truyền Thống và Lễ Hội (Traditionen und Feste)",
            "description": (
                "Lễ hội Đức không chỉ là Oktoberfest — đó là cả một hệ thống văn hóa sống động. "
                "Series này giúp bạn mô tả mọi truyền thống, món ăn và Tracht bằng tiếng Đức "
                "lưu loát."
            ),
            "count": 5,
        },
    ],
    # ===== Collection E: Thien Nhien va Doi Moi — 4 series, 23 curriculums =====
    "E": [
        {
            # E1 — tone: metaphor_led
            "title": "Môi Trường và Bền Vững (Umwelt und Nachhaltigkeit)",
            "description": (
                "Trái đất là ngôi nhà chung, và tiếng Đức là ngôn ngữ của cuộc cách mạng xanh "
                "châu Âu. Từ Energiewende đến lối sống zero-waste — series này trang bị từ vựng "
                "cho tương lai."
            ),
            "count": 6,
        },
        {
            # E2 — tone: provocative_question
            "title": "Công Nghệ Số và Trí Tuệ Nhân Tạo (Digitalisierung und KI)",
            "description": (
                "Bạn có thể giải thích trí tuệ nhân tạo bằng tiếng Đức không? Từ blockchain "
                "đến machine learning, series này đưa bạn vào cuộc trò chuyện công nghệ nóng "
                "nhất châu Âu."
            ),
            "count": 6,
        },
        {
            # E3 — tone: bold_declaration
            "title": "Thể Thao và Giải Trí (Sport und Freizeit)",
            "description": (
                "Thể thao là ngôn ngữ chung của nhân loại — nhưng bình luận trận Bundesliga "
                "bằng tiếng Đức là một đẳng cấp khác. Series này đưa bạn từ sân bóng đến phòng "
                "gym với vốn từ chuyên dụng."
            ),
            "count": 6,
        },
        {
            # E4 — tone: vivid_scenario
            "title": "Thiên Nhiên và Động Vật (Natur und Tierwelt)",
            "description": (
                "Hãy tưởng tượng bạn đang đi bộ qua Schwarzwald, nghe tiếng chim hót — và có "
                "thể gọi tên mọi loài cây, mọi con vật bằng tiếng Đức. Series này biến giấc mơ "
                "ấy thành hiện thực."
            ),
            "count": 5,
        },
    ],
}

# Verify planned total:
# A: 6+6+6+6+6+6+6 = 42
# B: 6+6+6+6+5+5   = 34
# C: 6+6+6+6+5+5   = 34
# D: 6+6+5+5        = 22
# E: 6+6+6+5        = 23
# Grand total = 42 + 34 + 34 + 22 + 23 = 155 ✓
#
# Planned level distribution across all 27 series (60 beg / 56 preint / 39 inter):
# The per-series level split is finalized in tasks 11.3-11.5 when the individual
# create_*.py scripts are written. Each series respects the max-1-level-gap
# rule (curriculum_series_level_gap view).

# Series counts per collection for iteration
SERIES_COUNTS = {"A": 7, "B": 6, "C": 6, "D": 4, "E": 4}


# ---------------------------------------------------------------------------
# Main execution
# ---------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("vi-de Orchestrator (bilingual-parity-expansion)")
    print("Creating collections and series")
    print("userLanguage=vi (Vietnamese), language=de (German)")
    print("Target: 155 curriculums across 5 collections, 27 series")
    print("=" * 60)

    collection_keys = ["A", "B", "C", "D", "E"]
    collection_ids = {}
    series_ids = {}

    # --- Step 1: Create collections ---
    print("\n--- Creating 5 collections ---")
    for i, col_def in enumerate(COLLECTIONS):
        col_id = create_collection(col_def["title"], col_def["description"])
        col_key = collection_keys[i]
        collection_ids[col_key] = col_id
        col_tone = tones["collections"][i]["description_tone"]
        print(f"  Collection {col_key}: {col_id}  (tone: {col_tone})")
        print(f"    Title: {col_def['title']}")

    # --- Step 2: Create series ---
    total_series = sum(SERIES_COUNTS.values())
    print(f"\n--- Creating {total_series} series ---")
    for i, col_key in enumerate(collection_keys):
        series_list = SERIES[col_key]
        for j, ser_def in enumerate(series_list):
            ser_id = create_series(ser_def["title"], ser_def["description"])
            ser_label = f"{col_key}{j + 1}"
            series_ids[ser_label] = ser_id
            ser_tone = tones["collections"][i]["series"][j]["description_tone"]
            print(f"  Series {ser_label}: {ser_id}  (tone: {ser_tone})")
            print(f"    Title: {ser_def['title']}")
            print(f"    Curriculum count: {ser_def['count']}")

    # --- Step 3: Wire series to collections ---
    print("\n--- Wiring series to collections ---")
    for i, col_key in enumerate(collection_keys):
        col_id = collection_ids[col_key]
        series_list = SERIES[col_key]
        for j in range(len(series_list)):
            ser_label = f"{col_key}{j + 1}"
            ser_id = series_ids[ser_label]
            add_series_to_collection(col_id, ser_id)
            print(f"  Wired {ser_label} ({ser_id}) -> Collection {col_key} ({col_id})")

    # --- Step 4: Set collection display orders (1-5) ---
    print("\n--- Setting collection display orders ---")
    for i, col_key in enumerate(collection_keys):
        col_id = collection_ids[col_key]
        order = i + 1
        set_collection_display_order(col_id, order)
        print(f"  Collection {col_key} ({col_id}) -> displayOrder {order}")

    # --- Step 5: Set series display orders ---
    print("\n--- Setting series display orders ---")
    for col_key in collection_keys:
        series_list = SERIES[col_key]
        for j in range(len(series_list)):
            ser_label = f"{col_key}{j + 1}"
            ser_id = series_ids[ser_label]
            order = j + 1
            set_series_display_order(ser_id, order)
            print(f"  Series {ser_label} ({ser_id}) -> displayOrder {order}")

    # --- Summary ---
    print("\n" + "=" * 60)
    print("SUMMARY — vi-de Infrastructure (bilingual-parity-expansion)")
    print("=" * 60)
    print("\nCollection IDs:")
    for col_key, col_id in collection_ids.items():
        print(f"  {col_key}: {col_id}")
    print("\nSeries IDs:")
    for ser_label, ser_id in series_ids.items():
        print(f"  {ser_label}: {ser_id}")

    # --- Tone assignment reference for curriculum scripts ---
    print("\n--- Tone Assignments (for curriculum scripts) ---")
    for i, col_key in enumerate(collection_keys):
        col_data = tones["collections"][i]
        print(f"\nCollection {col_key} (tone: {col_data['description_tone']}):")
        series_list = SERIES[col_key]
        for j in range(len(series_list)):
            ser_data = col_data["series"][j]
            ser_label = f"{col_key}{j + 1}"
            num_cur = series_list[j]["count"]
            print(f"  Series {ser_label} (tone: {ser_data['description_tone']}, {num_cur} curriculums):")
            for k in range(num_cur):
                cur_data = ser_data["curriculums"][k]
                print(
                    f"    Curriculum {k + 1}: "
                    f"desc_tone={cur_data['description_tone']}, "
                    f"farewell_tone={cur_data['farewell_tone']}"
                )

    print("\n✅ vi-de orchestrator (bilingual-parity-expansion) complete.")
    return collection_ids, series_ids


if __name__ == "__main__":
    main()
