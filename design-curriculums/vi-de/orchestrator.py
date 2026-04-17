"""
vi-de orchestrator — Creates 4 collections, 20 series, wires them together,
and sets display orders for the Vietnamese-German language pair.

Tone assignments are pre-computed via tone_assigner.assign_tones_for_language_pair(4, 5, 5).
All series descriptions are short persuasive Vietnamese hooks (≤255 chars) using the assigned tone.
Collection descriptions are short informative Vietnamese summaries (not persuasive copy).
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
# Tone assignments from tone_assigner.assign_tones_for_language_pair(4, 5, 5)
# ---------------------------------------------------------------------------
tones = tone_assigner.assign_tones_for_language_pair(4, 5, 5)

# Collection 0 (A): description_tone = provocative_question
#   Series A1: bold_declaration
#   Series A2: vivid_scenario
#   Series A3: empathetic_observation
#   Series A4: surprising_fact
#   Series A5: metaphor_led
#
# Collection 1 (B): description_tone = bold_declaration
#   Series B1: vivid_scenario
#   Series B2: empathetic_observation
#   Series B3: surprising_fact
#   Series B4: metaphor_led
#   Series B5: provocative_question
#
# Collection 2 (C): description_tone = vivid_scenario
#   Series C1: empathetic_observation
#   Series C2: surprising_fact
#   Series C3: metaphor_led
#   Series C4: provocative_question
#   Series C5: bold_declaration
#
# Collection 3 (D): description_tone = empathetic_observation
#   Series D1: surprising_fact
#   Series D2: metaphor_led
#   Series D3: provocative_question
#   Series D4: bold_declaration
#   Series D5: vivid_scenario

# ---------------------------------------------------------------------------
# Collection definitions
# ---------------------------------------------------------------------------
COLLECTIONS = [
    {
        "title": "Đời Sống và Du Lịch (Alltag und Reisen)",
        "description": (
            "Tổng hợp tiếng Đức cho các tình huống hàng ngày: đi du lịch, ăn uống, "
            "mua sắm, giao tiếp xã hội và chăm sóc sức khỏe. Mỗi chủ đề giúp bạn tự tin "
            "xử lý những cuộc hội thoại thực tế khi sống hoặc đi chơi tại các nước nói tiếng Đức."
        ),
    },
    {
        "title": "Kinh Doanh và Chuyên Nghiệp (Geschäft und Beruf)",
        "description": (
            "Tiếng Đức chuyên ngành dành cho môi trường công sở, tìm việc, vận hành doanh nghiệp "
            "và thương mại quốc tế. Từ email, họp hành đến đàm phán hợp đồng — bạn sẽ nắm vững "
            "ngôn ngữ cần thiết để phát triển sự nghiệp trong bối cảnh Đức ngữ."
        ),
    },
    {
        "title": "Học Thuật và Tri Thức (Akademisch und Intellektuell)",
        "description": (
            "Khám phá tiếng Đức học thuật qua các lĩnh vực khoa học, kinh tế, lịch sử, "
            "tâm lý học và triết học. Phù hợp cho người muốn đọc hiểu tài liệu chuyên sâu, "
            "tham gia thảo luận trí tuệ hoặc chuẩn bị cho môi trường đại học Đức ngữ."
        ),
    },
    {
        "title": "Văn Hóa và Xã Hội (Kultur und Gesellschaft)",
        "description": (
            "Tiếng Đức về nghệ thuật, kiến trúc, môi trường, thể thao và truyền thống văn hóa. "
            "Mỗi series mở ra một góc nhìn khác nhau về đời sống văn hóa Đức ngữ, giúp bạn "
            "trò chuyện sâu sắc hơn về những chủ đề vượt xa phạm vi giao tiếp thông thường."
        ),
    },
]

# ---------------------------------------------------------------------------
# Series definitions — 5 per collection, Vietnamese titles with German labels
# Descriptions: short persuasive hooks ≤255 chars using assigned tone
# ---------------------------------------------------------------------------
SERIES = {
    # ===== Collection A: Đời Sống và Du Lịch =====
    "A": [
        {
            # A1 — tone: bold_declaration
            "title": "Ẩm Thực và Nhà Hàng (Essen und Gastronomie)",
            "description": (
                "Tiếng Đức ẩm thực không chỉ là từ vựng — đó là chìa khóa mở ra cả một nền văn hóa. "
                "Từ gọi món đến nói chuyện với đầu bếp, bạn sẽ tự tin bước vào bất kỳ nhà hàng Đức nào."
            ),
        },
        {
            # A2 — tone: vivid_scenario
            "title": "Di Chuyển Thành Phố (Stadtnavigation und Verkehr)",
            "description": (
                "Hãy tưởng tượng bạn đứng giữa ga Berlin Hauptbahnhof, dòng người cuồn cuộn — và bạn biết chính xác "
                "phải nói gì để tìm đường. Đó là sức mạnh của series này."
            ),
        },
        {
            # A3 — tone: empathetic_observation
            "title": "Mua Sắm và Dịch Vụ (Einkaufen und Dienstleistungen)",
            "description": (
                "Bạn đã bao giờ muốn hỏi giá, đổi size hay mở tài khoản ngân hàng bằng tiếng Đức mà không biết "
                "bắt đầu từ đâu? Series này sinh ra cho khoảnh khắc ấy."
            ),
        },
        {
            # A4 — tone: surprising_fact
            "title": "Đời Sống Xã Hội (Soziales Leben und Beziehungen)",
            "description": (
                "Người Đức phân biệt rõ ràng giữa \"du\" và \"Sie\" — sai một từ có thể thay đổi cả mối quan hệ. "
                "Nắm vững ngôn ngữ giao tiếp xã hội giúp bạn hòa nhập thay vì chỉ tồn tại."
            ),
        },
        {
            # A5 — tone: metaphor_led
            "title": "Sức Khỏe và Thể Chất (Gesundheit und Wohlbefinden)",
            "description": (
                "Sức khỏe là tấm hộ chiếu thứ hai khi bạn sống ở nước ngoài. "
                "Series này trang bị cho bạn từ vựng y tế, thể dục và chăm sóc bản thân bằng tiếng Đức."
            ),
        },
    ],
    # ===== Collection B: Kinh Doanh và Chuyên Nghiệp =====
    "B": [
        {
            # B1 — tone: vivid_scenario
            "title": "Giao Tiếp Công Sở (Kommunikation am Arbeitsplatz)",
            "description": (
                "Hình dung bạn đang trình bày trước phòng họp toàn người Đức — tự tin, mạch lạc, chuyên nghiệp. "
                "Series này đưa bạn từ email đến thuyết trình không vấp váp."
            ),
        },
        {
            # B2 — tone: empathetic_observation
            "title": "Tìm Việc và Sự Nghiệp (Jobsuche und Karriere)",
            "description": (
                "Viết CV bằng tiếng Đức đã khó, phỏng vấn còn khó hơn. Nếu bạn đang tìm cơ hội nghề nghiệp "
                "trong môi trường Đức ngữ, đây là bước đệm bạn cần."
            ),
        },
        {
            # B3 — tone: surprising_fact
            "title": "Từ Vựng Ngành Nghề (Branchenvokabular)",
            "description": (
                "Mỗi ngành có một \"ngôn ngữ riêng\" — từ công nghệ đến khách sạn, sản xuất đến logistics. "
                "Nắm đúng thuật ngữ chuyên ngành giúp bạn được đồng nghiệp Đức tôn trọng ngay lập tức."
            ),
        },
        {
            # B4 — tone: metaphor_led
            "title": "Vận Hành Doanh Nghiệp (Geschäftsbetrieb)",
            "description": (
                "Doanh nghiệp như một cỗ máy — quản lý dự án là bánh răng, ngân sách là nhiên liệu. "
                "Series này giúp bạn vận hành cỗ máy ấy bằng tiếng Đức."
            ),
        },
        {
            # B5 — tone: provocative_question
            "title": "Kinh Doanh Quốc Tế (Internationaler Handel)",
            "description": (
                "Bạn có thể đàm phán hợp đồng triệu đô bằng tiếng Đức không? Từ thuật ngữ thương mại đến "
                "luật kinh doanh, series này biến bạn thành đối tác đáng gờm trên bàn đàm phán quốc tế."
            ),
        },
    ],
    # ===== Collection C: Học Thuật và Tri Thức =====
    "C": [
        {
            # C1 — tone: empathetic_observation
            "title": "Khoa Học và Công Nghệ (Wissenschaft und Technologie)",
            "description": (
                "Đọc bài báo khoa học bằng tiếng Đức mà cảm thấy lạc lõng? Bạn không đơn độc. "
                "Series này xây nền tảng từ vựng từ sinh học đến tin học, giúp bạn tiếp cận tri thức tự tin hơn."
            ),
        },
        {
            # C2 — tone: surprising_fact
            "title": "Kinh Tế và Tài Chính (Wirtschaft und Finanzen)",
            "description": (
                "Đức là nền kinh tế lớn nhất châu Âu, nhưng hầu hết người học bỏ qua từ vựng tài chính. "
                "Từ vi mô đến vĩ mô, series này lấp đầy khoảng trống đó."
            ),
        },
        {
            # C3 — tone: metaphor_led
            "title": "Lịch Sử và Chính Trị (Geschichte und Politik)",
            "description": (
                "Lịch sử là tấm gương, chính trị là ánh sáng chiếu vào đó. "
                "Series này giúp bạn đọc hiểu và thảo luận về quá khứ lẫn hiện tại bằng tiếng Đức."
            ),
        },
        {
            # C4 — tone: provocative_question
            "title": "Tâm Lý và Giáo Dục (Psychologie und Bildung)",
            "description": (
                "Tại sao trẻ em học ngôn ngữ nhanh hơn người lớn? Tâm lý học có câu trả lời — "
                "và series này dạy bạn cách nói về nó bằng tiếng Đức."
            ),
        },
        {
            # C5 — tone: bold_declaration
            "title": "Triết Học và Tư Duy Phản Biện (Philosophie und kritisches Denken)",
            "description": (
                "Triết học Đức định hình tư tưởng phương Tây suốt nhiều thế kỷ. "
                "Nắm vững từ vựng triết học là bước đầu để tham gia những cuộc tranh luận sâu sắc nhất."
            ),
        },
    ],
    # ===== Collection D: Văn Hóa và Xã Hội =====
    "D": [
        {
            # D1 — tone: surprising_fact
            "title": "Nghệ Thuật và Văn Học (Kunst und Literatur)",
            "description": (
                "Đức sở hữu hơn 6.800 bảo tàng — nhiều nhất trên thế giới tính theo đầu người. "
                "Series này mở cánh cửa để bạn nói về nghệ thuật và văn học như người bản xứ."
            ),
        },
        {
            # D2 — tone: metaphor_led
            "title": "Kiến Trúc và Thiết Kế (Architektur und Design)",
            "description": (
                "Kiến trúc là ngôn ngữ thầm lặng của một thành phố. "
                "Từ Bauhaus đến thiết kế bền vững, series này giúp bạn đọc và kể câu chuyện đó bằng tiếng Đức."
            ),
        },
        {
            # D3 — tone: provocative_question
            "title": "Môi Trường và Bền Vững (Umwelt und Nachhaltigkeit)",
            "description": (
                "Bạn có thể giải thích biến đổi khí hậu bằng tiếng Đức không? "
                "Từ năng lượng tái tạo đến lối sống xanh, series này trang bị ngôn ngữ cho cuộc chiến quan trọng nhất."
            ),
        },
        {
            # D4 — tone: bold_declaration
            "title": "Thể Thao và Giải Trí (Sport und Freizeit)",
            "description": (
                "Thể thao là ngôn ngữ chung của nhân loại — nhưng bình luận bằng tiếng Đức là một đẳng cấp khác. "
                "Series này đưa bạn từ sân bóng đến phòng gym với vốn từ chuyên dụng."
            ),
        },
        {
            # D5 — tone: vivid_scenario
            "title": "Truyền Thống và Lễ Hội (Traditionen und Feste)",
            "description": (
                "Hãy tưởng tượng bạn đang đứng giữa lễ hội Oktoberfest, tiếng nhạc vang khắp lều bia — "
                "và bạn có thể kể lại trải nghiệm ấy bằng tiếng Đức."
            ),
        },
    ],
}


# ---------------------------------------------------------------------------
# Main execution
# ---------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("vi-de Orchestrator — Creating collections and series")
    print("=" * 60)

    # Map collection letter to index for wiring
    collection_keys = ["A", "B", "C", "D"]
    collection_ids = {}
    series_ids = {}  # keyed by e.g. "A1", "B3", etc.

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
    print("\n--- Creating 20 series ---")
    for i, col_key in enumerate(collection_keys):
        series_list = SERIES[col_key]
        for j, ser_def in enumerate(series_list):
            ser_id = create_series(ser_def["title"], ser_def["description"])
            ser_label = f"{col_key}{j + 1}"
            series_ids[ser_label] = ser_id
            ser_tone = tones["collections"][i]["series"][j]["description_tone"]
            print(f"  Series {ser_label}: {ser_id}  (tone: {ser_tone})")
            print(f"    Title: {ser_def['title']}")

    # --- Step 3: Wire series to collections ---
    print("\n--- Wiring series to collections ---")
    for i, col_key in enumerate(collection_keys):
        col_id = collection_ids[col_key]
        for j in range(5):
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

    # --- Step 5: Set series display orders (1-5 within each collection) ---
    print("\n--- Setting series display orders ---")
    for col_key in collection_keys:
        for j in range(5):
            ser_label = f"{col_key}{j + 1}"
            ser_id = series_ids[ser_label]
            order = j + 1
            set_series_display_order(ser_id, order)
            print(f"  Series {ser_label} ({ser_id}) -> displayOrder {order}")

    # --- Summary ---
    print("\n" + "=" * 60)
    print("SUMMARY — vi-de Infrastructure")
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
        for j, ser_data in enumerate(col_data["series"]):
            ser_label = f"{col_key}{j + 1}"
            print(f"  Series {ser_label} (tone: {ser_data['description_tone']}):")
            for cur_data in ser_data["curriculums"]:
                cur_idx = cur_data["curriculum_index"] + 1
                print(
                    f"    Curriculum {cur_idx}: "
                    f"desc_tone={cur_data['description_tone']}, "
                    f"farewell_tone={cur_data['farewell_tone']}"
                )

    print("\n✅ vi-de orchestrator complete.")
    return collection_ids, series_ids


if __name__ == "__main__":
    main()
