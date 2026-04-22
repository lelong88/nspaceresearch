"""
vi-zh orchestrator — Creates 4 collections, 14 series, wires them together,
and sets display orders for the Vietnamese-Chinese language pair.

Language pair: userLanguage=vi (Vietnamese speakers), language=zh (learning Chinese)
User-facing text: Vietnamese
Reading passages: Chinese

Total: 79 curriculums (31 beginner, 22 preintermediate, 26 intermediate)

Distribution across 4 collections, 14 series:
  Collection A: Đời sống và Du lịch (生活与旅行) — 4 series, 24 curriculums
  Collection B: Công việc và Kinh doanh (工作与商务) — 3 series, 17 curriculums
  Collection C: Học thuật và Tri thức (学术与知识) — 4 series, 22 curriculums
  Collection D: Văn hóa và Xã hội (文化与社会) — 3 series, 16 curriculums

Tone assignments are pre-computed via tone_assigner.
All series descriptions are short persuasive Vietnamese hooks (≤255 chars) using the assigned tone.
Collection descriptions are short informative Vietnamese summaries (not persuasive copy).
"""

import sys
import logging

sys.path.insert(0, "/home/ubuntu/nspaceresearch2/design-curriculums")
sys.path.insert(0, "/home/ubuntu/nspaceresearch2/design-curriculums/vi-zh")
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
# We have 4 collections with varying series counts: 4, 3, 4, 3 = 14 series
# Curriculum counts per series (approximate):
#   A: 6, 6, 6, 6 = 24
#   B: 6, 6, 5 = 17
#   C: 6, 6, 5, 5 = 22
#   D: 6, 5, 5 = 16
# Total = 79
#
# We use tone_assigner with uniform params then manually document the mapping.
# Since tone_assigner expects uniform series_per_collection and curriculums_per_series,
# we call it with max values (4 series, 6 curriculums) and trim unused slots.
tones = tone_assigner.assign_tones_for_language_pair(4, 4, 6)

# Tone mapping (from tone_assigner output):
#
# Collection A (Đời sống và Du lịch): description_tone = provocative_question
#   Series A1: bold_declaration
#     Cur 1: vivid_scenario / introspective_guide
#     Cur 2: empathetic_observation / warm_accountability
#     Cur 3: surprising_fact / team_building_energy
#     Cur 4: metaphor_led / quiet_awe
#     Cur 5: provocative_question / practical_momentum
#     Cur 6: bold_declaration / introspective_guide
#   Series A2: vivid_scenario
#     Cur 1: empathetic_observation / warm_accountability
#     Cur 2: surprising_fact / team_building_energy
#     Cur 3: metaphor_led / quiet_awe
#     Cur 4: provocative_question / practical_momentum
#     Cur 5: bold_declaration / introspective_guide
#     Cur 6: vivid_scenario / warm_accountability
#   Series A3: empathetic_observation
#     Cur 1: surprising_fact / team_building_energy
#     Cur 2: metaphor_led / quiet_awe
#     Cur 3: provocative_question / practical_momentum
#     Cur 4: bold_declaration / introspective_guide
#     Cur 5: vivid_scenario / warm_accountability
#     Cur 6: empathetic_observation / team_building_energy
#   Series A4: surprising_fact
#     Cur 1: metaphor_led / quiet_awe
#     Cur 2: provocative_question / practical_momentum
#     Cur 3: bold_declaration / introspective_guide
#     Cur 4: vivid_scenario / warm_accountability
#     Cur 5: empathetic_observation / team_building_energy
#     Cur 6: surprising_fact / quiet_awe
#
# Collection B (Công việc và Kinh doanh): description_tone = bold_declaration
#   Series B1: vivid_scenario
#     Cur 1: empathetic_observation / practical_momentum
#     Cur 2: surprising_fact / introspective_guide
#     Cur 3: metaphor_led / warm_accountability
#     Cur 4: provocative_question / team_building_energy
#     Cur 5: bold_declaration / quiet_awe
#     Cur 6: vivid_scenario / practical_momentum
#   Series B2: empathetic_observation
#     Cur 1: surprising_fact / introspective_guide
#     Cur 2: metaphor_led / warm_accountability
#     Cur 3: provocative_question / team_building_energy
#     Cur 4: bold_declaration / quiet_awe
#     Cur 5: vivid_scenario / practical_momentum
#     Cur 6: empathetic_observation / introspective_guide
#   Series B3: surprising_fact
#     Cur 1: metaphor_led / warm_accountability
#     Cur 2: provocative_question / team_building_energy
#     Cur 3: bold_declaration / quiet_awe
#     Cur 4: vivid_scenario / practical_momentum
#     Cur 5: empathetic_observation / introspective_guide
#
# Collection C (Học thuật và Tri thức): description_tone = vivid_scenario
#   Series C1: empathetic_observation
#     Cur 1: surprising_fact / team_building_energy
#     Cur 2: metaphor_led / quiet_awe
#     Cur 3: provocative_question / practical_momentum
#     Cur 4: bold_declaration / introspective_guide
#     Cur 5: vivid_scenario / warm_accountability
#     Cur 6: empathetic_observation / team_building_energy
#   Series C2: surprising_fact
#     Cur 1: metaphor_led / quiet_awe
#     Cur 2: provocative_question / practical_momentum
#     Cur 3: bold_declaration / introspective_guide
#     Cur 4: vivid_scenario / warm_accountability
#     Cur 5: empathetic_observation / team_building_energy
#     Cur 6: surprising_fact / quiet_awe
#   Series C3: metaphor_led
#     Cur 1: provocative_question / practical_momentum
#     Cur 2: bold_declaration / introspective_guide
#     Cur 3: vivid_scenario / warm_accountability
#     Cur 4: empathetic_observation / team_building_energy
#     Cur 5: surprising_fact / quiet_awe
#   Series C4: provocative_question
#     Cur 1: bold_declaration / introspective_guide
#     Cur 2: vivid_scenario / warm_accountability
#     Cur 3: empathetic_observation / team_building_energy
#     Cur 4: surprising_fact / quiet_awe
#     Cur 5: metaphor_led / practical_momentum
#
# Collection D (Văn hóa và Xã hội): description_tone = empathetic_observation
#   Series D1: surprising_fact
#     Cur 1: metaphor_led / warm_accountability
#     Cur 2: provocative_question / team_building_energy
#     Cur 3: bold_declaration / quiet_awe
#     Cur 4: vivid_scenario / practical_momentum
#     Cur 5: empathetic_observation / introspective_guide
#     Cur 6: surprising_fact / warm_accountability
#   Series D2: metaphor_led
#     Cur 1: provocative_question / team_building_energy
#     Cur 2: bold_declaration / quiet_awe
#     Cur 3: vivid_scenario / practical_momentum
#     Cur 4: empathetic_observation / introspective_guide
#     Cur 5: surprising_fact / warm_accountability
#   Series D3: provocative_question
#     Cur 1: bold_declaration / quiet_awe
#     Cur 2: vivid_scenario / practical_momentum
#     Cur 3: empathetic_observation / introspective_guide
#     Cur 4: surprising_fact / warm_accountability
#     Cur 5: metaphor_led / team_building_energy

# ---------------------------------------------------------------------------
# Collection definitions — Vietnamese titles, informative summaries
# ---------------------------------------------------------------------------
COLLECTIONS = [
    {
        "title": "Đời sống và Du lịch (生活与旅行)",
        "description": (
            "Tiếng Trung cho các tình huống hàng ngày: du lịch, ẩm thực, mua sắm, "
            "giao tiếp xã hội và sức khỏe. Mỗi chủ đề trang bị từ vựng và sự tự tin "
            "để bạn xử lý các cuộc hội thoại thực tế khi sống hoặc du lịch tại các nước nói tiếng Trung."
        ),
    },
    {
        "title": "Công việc và Kinh doanh (工作与商务)",
        "description": (
            "Tiếng Trung chuyên nghiệp cho môi trường công sở, tìm việc, vận hành doanh nghiệp "
            "và thương mại quốc tế. Từ email và cuộc họp đến đàm phán hợp đồng, xây dựng kỹ năng "
            "ngôn ngữ cần thiết để phát triển sự nghiệp tại thị trường Trung Quốc."
        ),
    },
    {
        "title": "Học thuật và Tri thức (学术与知识)",
        "description": (
            "Tiếng Trung học thuật về khoa học, kinh tế, lịch sử, tâm lý và triết học. "
            "Phù hợp cho ai muốn đọc tài liệu chuyên ngành, tham gia thảo luận trí tuệ, "
            "hoặc chuẩn bị du học tại các trường đại học Trung Quốc."
        ),
    },
    {
        "title": "Văn hóa và Xã hội (文化与社会)",
        "description": (
            "Tiếng Trung về nghệ thuật, kiến trúc, môi trường, thể thao và truyền thống văn hóa. "
            "Mỗi chuỗi bài mở ra một góc nhìn khác về đời sống văn hóa Trung Quốc, giúp bạn "
            "tham gia những cuộc trò chuyện sâu sắc hơn."
        ),
    },
]

# ---------------------------------------------------------------------------
# Series definitions — Vietnamese titles with Chinese labels
# Descriptions: short persuasive hooks ≤255 chars using assigned tone
# ---------------------------------------------------------------------------
SERIES = {
    # ===== Collection A: Đời sống và Du lịch — 4 series =====
    "A": [
        {
            # A1 — tone: bold_declaration — 6 curriculums
            "title": "Ẩm thực và Nhà hàng (美食与餐厅)",
            "description": (
                "Từ vựng ẩm thực Trung Quốc không chỉ là từ ngữ — mà là chìa khóa mở ra cả một nền văn hóa. "
                "Từ gọi món đến trò chuyện tại chợ, bạn sẽ tự tin bước vào bất kỳ nhà hàng nào."
            ),
            "count": 6,
        },
        {
            # A2 — tone: vivid_scenario — 6 curriculums
            "title": "Di chuyển và Giao thông (交通与出行)",
            "description": (
                "Hãy tưởng tượng bạn đứng giữa ga Bắc Kinh, dòng người hối hả — và bạn biết chính xác phải nói gì "
                "để tìm đúng sân ga. Đó là sức mạnh của chuỗi bài này."
            ),
            "count": 6,
        },
        {
            # A3 — tone: empathetic_observation — 6 curriculums
            "title": "Mua sắm và Dịch vụ (购物与服务)",
            "description": (
                "Đã bao giờ bạn muốn hỏi đổi size, so sánh giá, hay mở tài khoản ngân hàng bằng tiếng Trung "
                "nhưng không biết bắt đầu từ đâu? Chuỗi bài này dành cho khoảnh khắc đó."
            ),
            "count": 6,
        },
        {
            # A4 — tone: surprising_fact — 6 curriculums
            "title": "Sức khỏe và Đời sống (健康与生活)",
            "description": (
                "Y học cổ truyền Trung Quốc có lịch sử hơn 2.000 năm và vẫn ảnh hưởng sâu sắc đến đời sống hiện đại. "
                "Nắm vững từ vựng sức khỏe để tự tin chăm sóc bản thân."
            ),
            "count": 6,
        },
    ],
    # ===== Collection B: Công việc và Kinh doanh — 3 series =====
    "B": [
        {
            # B1 — tone: vivid_scenario — 6 curriculums
            "title": "Giao tiếp Công sở (职场沟通)",
            "description": (
                "Hãy tưởng tượng bạn đang thuyết trình trước phòng họp toàn đồng nghiệp Trung Quốc — tự tin, rõ ràng, "
                "chuyên nghiệp. Chuỗi bài này đưa bạn từ email đến bài trình bày."
            ),
            "count": 6,
        },
        {
            # B2 — tone: empathetic_observation — 6 curriculums
            "title": "Tìm việc và Sự nghiệp (求职与职业)",
            "description": (
                "Viết hồ sơ xin việc bằng tiếng Trung đã khó; phỏng vấn còn khó hơn. Nếu bạn đang theo đuổi "
                "cơ hội nghề nghiệp tại Trung Quốc, đây là bước đệm bạn cần."
            ),
            "count": 6,
        },
        {
            # B3 — tone: surprising_fact — 5 curriculums
            "title": "Thương mại Quốc tế (国际贸易)",
            "description": (
                "Trung Quốc là đối tác thương mại lớn nhất của hơn 120 quốc gia. Từ thuật ngữ xuất nhập khẩu "
                "đến luật kinh doanh, chuỗi bài này biến bạn thành đối tác đáng gờm."
            ),
            "count": 5,
        },
    ],
    # ===== Collection C: Học thuật và Tri thức — 4 series =====
    "C": [
        {
            # C1 — tone: empathetic_observation — 6 curriculums
            "title": "Khoa học và Công nghệ (科学与技术)",
            "description": (
                "Đọc một bài báo khoa học bằng tiếng Trung mà cảm thấy lạc lõng? Bạn không đơn độc. "
                "Chuỗi bài này xây dựng vốn từ từ sinh học đến công nghệ thông tin."
            ),
            "count": 6,
        },
        {
            # C2 — tone: surprising_fact — 6 curriculums
            "title": "Kinh tế và Tài chính (经济与金融)",
            "description": (
                "Trung Quốc là nền kinh tế lớn thứ 2 thế giới, nhưng hầu hết người học bỏ qua từ vựng tài chính. "
                "Từ vi mô đến vĩ mô, chuỗi bài này lấp đầy khoảng trống đó."
            ),
            "count": 6,
        },
        {
            # C3 — tone: metaphor_led — 5 curriculums
            "title": "Lịch sử và Chính trị (历史与政治)",
            "description": (
                "Lịch sử là tấm gương; chính trị là ánh sáng chiếu lên đó. "
                "Chuỗi bài này giúp bạn đọc, thảo luận và tranh luận về quá khứ và hiện tại bằng tiếng Trung."
            ),
            "count": 5,
        },
        {
            # C4 — tone: provocative_question — 5 curriculums
            "title": "Tâm lý và Giáo dục (心理与教育)",
            "description": (
                "Tại sao trẻ em học ngôn ngữ nhanh hơn người lớn? Tâm lý học có câu trả lời — "
                "và chuỗi bài này dạy bạn cách nói về điều đó bằng tiếng Trung."
            ),
            "count": 5,
        },
    ],
    # ===== Collection D: Văn hóa và Xã hội — 3 series =====
    "D": [
        {
            # D1 — tone: surprising_fact — 6 curriculums
            "title": "Nghệ thuật và Văn học (艺术与文学)",
            "description": (
                "Trung Quốc có bốn phát minh vĩ đại và hàng ngàn năm văn học rực rỡ. "
                "Chuỗi bài này mở cánh cửa để bạn thảo luận nghệ thuật và văn học như người bản xứ."
            ),
            "count": 6,
        },
        {
            # D2 — tone: metaphor_led — 5 curriculums
            "title": "Môi trường và Bền vững (环境与可持续)",
            "description": (
                "Thiên nhiên là cuốn sách; con người là người đọc đang viết lại từng trang. "
                "Chuỗi bài này trang bị từ vựng cho cuộc trò chuyện quan trọng nhất thời đại."
            ),
            "count": 5,
        },
        {
            # D3 — tone: provocative_question — 5 curriculums
            "title": "Truyền thống và Lễ hội (传统与节日)",
            "description": (
                "Bạn có biết Tết Nguyên Đán ở Trung Quốc khác gì Tết Việt Nam không? Từ phong tục đến ẩm thực lễ hội, "
                "chuỗi bài này giúp bạn hiểu sâu văn hóa Trung Hoa."
            ),
            "count": 5,
        },
    ],
}

# Verify total: 6+6+6+6 + 6+6+5 + 6+6+5+5 + 6+5+5 = 24+17+22+16 = 79 ✓

# Series counts per collection for iteration
SERIES_COUNTS = {"A": 4, "B": 3, "C": 4, "D": 3}


# ---------------------------------------------------------------------------
# Main execution
# ---------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("vi-zh Orchestrator — Creating collections and series")
    print("userLanguage=vi (Vietnamese), language=zh (Chinese)")
    print("=" * 60)

    collection_keys = ["A", "B", "C", "D"]
    collection_ids = {}
    series_ids = {}

    # --- Step 1: Create collections ---
    print("\n--- Creating 4 collections ---")
    for i, col_def in enumerate(COLLECTIONS):
        col_id = create_collection(col_def["title"], col_def["description"])
        col_key = collection_keys[i]
        collection_ids[col_key] = col_id
        col_tone = tones["collections"][i]["description_tone"]
        print(f"  Collection {col_key}: {col_id}  (tone: {col_tone})")
        print(f"    Title: {col_def['title']}")

    # --- Step 2: Create series ---
    print("\n--- Creating 14 series ---")
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

    # --- Step 4: Set collection display orders (1-4) ---
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
    print("SUMMARY — vi-zh Infrastructure")
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

    print("\n✅ vi-zh orchestrator complete.")
    return collection_ids, series_ids


if __name__ == "__main__":
    main()
