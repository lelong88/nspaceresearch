"""
vi-fr orchestrator (bilingual-parity-expansion) — Creates 5 collections, 25 series,
wires them together, and sets display orders for the Vietnamese-French language pair.

NOTE: This orchestrator REPLACES the old multilingual-curriculum-expansion orchestrator
that created 4 collections with 20 series. Those old collections/series already exist
in the database. This script creates ENTIRELY NEW infrastructure for the
bilingual-parity-expansion spec.

Language pair: userLanguage=vi (Vietnamese speakers), language=fr (learning French)
User-facing text (titles, descriptions): Vietnamese
Reading passages: French
Session titles: Phần 1, Phần 2, Phần 3, Ôn tập, Đọc tổng hợp

Target: 141 curriculums (60 beginner, 55 preintermediate, 26 intermediate)

Distribution across 5 collections, 25 series:
  Collection A: Đời Sống & Du Lịch (Vie Quotidienne et Voyages) — 7 series, 40 curriculums
  Collection B: Kinh Doanh & Nghề Nghiệp (Affaires et Carrière) — 6 series, 34 curriculums
  Collection C: Học Thuật & Khoa Học (Sciences et Savoir) — 5 series, 28 curriculums
  Collection D: Văn Hóa & Xã Hội (Culture et Société) — 4 series, 20 curriculums
  Collection E: Thiên Nhiên & Đổi Mới (Nature et Innovation) — 3 series, 19 curriculums

Tone assignments are pre-computed via tone_assigner.assign_tones_for_language_pair(5, 7, 7),
which generates 245 tone slots across a uniform 5×7×7 grid. The orchestrator uses only the
slots needed for each collection's actual series count (A=7, B=6, C=5, D=4, E=3) and each
series' actual curriculum count (5, 6, or 7). Unused slots are simply not consumed.

All series descriptions are short persuasive Vietnamese hooks (≤255 chars) using the assigned tone.
Collection descriptions are short informative Vietnamese summaries (not persuasive copy).

Requirements: 6.1–6.8, 8.1–8.4, 8.7
"""

import sys
import logging

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums/vi-fr")
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
# counts. We request a 5 × 7 × 7 grid (245 tone slots) — enough to cover the maximum
# of 7 series per collection and 7 curriculums per series. Collections with fewer
# series (B=6, C=5, D=4, E=3) simply ignore extra series slots; series with fewer
# curriculums (5 or 6 instead of 7) ignore extra curriculum slots.
#
# The assigner already enforces:
#   - No adjacent duplicate description tones (curriculums within a series,
#     series within a collection)
#   - No adjacent duplicate farewell tones (curriculums within a series)
#   - No single description tone exceeds 30% across the whole pair
tones = tone_assigner.assign_tones_for_language_pair(5, 7, 7)

# ---------------------------------------------------------------------------
# Tone reference (from tone_assigner output, collections A–E):
# ---------------------------------------------------------------------------
#
# Collection A (Đời Sống & Du Lịch): description_tone = provocative_question
#   Series A1: bold_declaration       — 6 curriculums
#   Series A2: vivid_scenario         — 6 curriculums
#   Series A3: empathetic_observation — 6 curriculums
#   Series A4: surprising_fact        — 6 curriculums
#   Series A5: metaphor_led           — 5 curriculums
#   Series A6: provocative_question   — 5 curriculums
#   Series A7: bold_declaration       — 6 curriculums
#
# Collection B (Kinh Doanh & Nghề Nghiệp): description_tone = bold_declaration
#   Series B1: vivid_scenario         — 6 curriculums
#   Series B2: empathetic_observation — 6 curriculums
#   Series B3: surprising_fact        — 6 curriculums
#   Series B4: metaphor_led           — 6 curriculums
#   Series B5: provocative_question   — 5 curriculums
#   Series B6: bold_declaration       — 5 curriculums
#
# Collection C (Học Thuật & Khoa Học): description_tone = vivid_scenario
#   Series C1: empathetic_observation — 6 curriculums
#   Series C2: surprising_fact        — 6 curriculums
#   Series C3: metaphor_led           — 6 curriculums
#   Series C4: provocative_question   — 5 curriculums
#   Series C5: bold_declaration       — 5 curriculums
#
# Collection D (Văn Hóa & Xã Hội): description_tone = empathetic_observation
#   Series D1: surprising_fact        — 5 curriculums
#   Series D2: metaphor_led           — 5 curriculums
#   Series D3: provocative_question   — 5 curriculums
#   Series D4: bold_declaration       — 5 curriculums
#
# Collection E (Thiên Nhiên & Đổi Mới): description_tone = surprising_fact
#   Series E1: metaphor_led           — 7 curriculums
#   Series E2: provocative_question   — 6 curriculums
#   Series E3: bold_declaration       — 6 curriculums
#
# Per-curriculum description + farewell tones are printed to stdout at the end of
# this script (see the "Tone Assignments" section), and the curriculum create_*.py
# scripts (tasks 15.3–15.5) will reference that output.


# ---------------------------------------------------------------------------
# Collection definitions — Vietnamese titles with French labels,
# informative summaries (not persuasive copy)
# ---------------------------------------------------------------------------
COLLECTIONS = [
    {
        "title": "Đời Sống & Du Lịch (Vie Quotidienne et Voyages)",
        "description": (
            "Tiếng Pháp cho các tình huống thường nhật: ẩm thực, di chuyển, mua sắm, "
            "giao tiếp xã hội, sức khỏe, nhà ở và du lịch. Mỗi chủ đề trang bị từ vựng "
            "và sự tự tin để bạn xử lý hội thoại thực tế khi sống hoặc du lịch tại các "
            "nước nói tiếng Pháp."
        ),
    },
    {
        "title": "Kinh Doanh & Nghề Nghiệp (Affaires et Carrière)",
        "description": (
            "Tiếng Pháp chuyên ngành cho môi trường công sở, tìm việc, thuật ngữ ngành, "
            "vận hành doanh nghiệp và thương mại quốc tế. Từ email và cuộc họp đến đàm "
            "phán hợp đồng — kỹ năng ngôn ngữ cần thiết để phát triển sự nghiệp trong "
            "thị trường Pháp ngữ."
        ),
    },
    {
        "title": "Học Thuật & Khoa Học (Sciences et Savoir)",
        "description": (
            "Tiếng Pháp học thuật qua các lĩnh vực khoa học, kinh tế, lịch sử, tâm lý "
            "học và triết học. Phù hợp cho người muốn đọc tài liệu chuyên sâu, tham gia "
            "thảo luận trí tuệ hoặc chuẩn bị du học tại các trường đại học Pháp ngữ."
        ),
    },
    {
        "title": "Văn Hóa & Xã Hội (Culture et Société)",
        "description": (
            "Tiếng Pháp về nghệ thuật, kiến trúc, truyền thông và truyền thống văn hóa. "
            "Mỗi series mở ra một góc nhìn khác về đời sống văn hóa Pháp ngữ, giúp bạn "
            "trò chuyện sâu sắc hơn vượt xa phạm vi giao tiếp thông thường."
        ),
    },
    {
        "title": "Thiên Nhiên & Đổi Mới (Nature et Innovation)",
        "description": (
            "Tiếng Pháp về môi trường, bền vững, công nghệ số và thể thao. Khám phá "
            "từ vựng cho những chủ đề đang định hình tương lai — từ năng lượng tái tạo "
            "đến trí tuệ nhân tạo trong bối cảnh Pháp ngữ."
        ),
    },
]

# ---------------------------------------------------------------------------
# Series definitions — Vietnamese titles with French topic labels
# Descriptions: short persuasive hooks ≤255 chars using the series' assigned tone
# The "count" field records the number of curriculums planned per series, for
# total-count verification (should sum to 141).
# ---------------------------------------------------------------------------
SERIES = {
    # ===== Collection A: Đời Sống & Du Lịch — 7 series, 40 curriculums =====
    "A": [
        {
            # A1 — tone: bold_declaration
            "title": "Ẩm Thực & Nhà Hàng (Gastronomie et Restauration)",
            "description": (
                "Từ vựng ẩm thực Pháp không chỉ là từ ngữ — đó là chìa khóa mở ra cả "
                "một nền văn hóa. Từ gọi món tại brasserie đến trò chuyện ở marché, bạn "
                "sẽ tự tin bước vào bất kỳ nhà hàng Pháp nào."
            ),
            "count": 6,
        },
        {
            # A2 — tone: vivid_scenario
            "title": "Di Chuyển & Giao Thông (Transports et Navigation)",
            "description": (
                "Hãy tưởng tượng bạn đứng giữa ga Gare du Nord, dòng người cuồn cuộn — "
                "và bạn biết chính xác phải nói gì để tìm đúng quai. Đó là sức mạnh "
                "series này trao cho bạn."
            ),
            "count": 6,
        },
        {
            # A3 — tone: empathetic_observation
            "title": "Mua Sắm & Dịch Vụ (Achats et Services)",
            "description": (
                "Bạn đã bao giờ muốn hỏi đổi size, so sánh giá hay mở compte bancaire "
                "bằng tiếng Pháp mà không biết bắt đầu từ đâu? Series này sinh ra cho "
                "khoảnh khắc ấy."
            ),
            "count": 6,
        },
        {
            # A4 — tone: surprising_fact
            "title": "Đời Sống Xã Hội (Vie Sociale et Relations)",
            "description": (
                "Tiếng Pháp có cả một hệ thống ngữ pháp lịch sự — tu và vous có thể "
                "quyết định ấn tượng đầu tiên. Nắm vững giao tiếp xã hội giúp bạn kết "
                "nối thật sự thay vì chỉ tồn tại."
            ),
            "count": 6,
        },
        {
            # A5 — tone: metaphor_led
            "title": "Sức Khỏe & Thể Chất (Santé et Bien-être)",
            "description": (
                "Sức khỏe là tấm hộ chiếu thứ hai khi sống ở nước ngoài. Series này "
                "trang bị từ vựng y tế, thể dục và chăm sóc bản thân — chìa khóa mở "
                "mọi cánh cửa pharmacie và cabinet."
            ),
            "count": 5,
        },
        {
            # A6 — tone: provocative_question
            "title": "Nhà Ở & Sinh Hoạt (Logement et Vie Quotidienne)",
            "description": (
                "Bạn có thể thuê nhà, tranh luận hóa đơn charges locatives hay đăng ký "
                "tại mairie hoàn toàn bằng tiếng Pháp không? Nếu chưa, series này là "
                "con đường ngắn nhất."
            ),
            "count": 5,
        },
        {
            # A7 — tone: bold_declaration
            "title": "Du Lịch & Khám Phá (Voyages et Découvertes)",
            "description": (
                "Du lịch thật sự bắt đầu khi tiếng Pháp sách hướng dẫn kết thúc. Đặt "
                "chambre, tìm hành lý thất lạc hay tham gia randonnée — series này biến "
                "bạn thành lữ khách, không phải du khách."
            ),
            "count": 6,
        },
    ],
    # ===== Collection B: Kinh Doanh & Nghề Nghiệp — 6 series, 34 curriculums =====
    "B": [
        {
            # B1 — tone: vivid_scenario
            "title": "Giao Tiếp Công Sở (Communication au Bureau)",
            "description": (
                "Hình dung bạn đang trình bày trước phòng họp toàn đồng nghiệp Pháp — "
                "tự tin, mạch lạc, chuyên nghiệp. Series này đưa bạn từ email ngày đầu "
                "đến thuyết trình không vấp váp."
            ),
            "count": 6,
        },
        {
            # B2 — tone: empathetic_observation
            "title": "Tìm Việc & Sự Nghiệp (Recherche d'Emploi et Carrière)",
            "description": (
                "Viết CV bằng tiếng Pháp đã khó, phỏng vấn còn khó hơn. Nếu bạn đang "
                "theo đuổi cơ hội nghề nghiệp trong thị trường Pháp ngữ, đây là bước "
                "đệm bạn cần."
            ),
            "count": 6,
        },
        {
            # B3 — tone: surprising_fact
            "title": "Từ Vựng Chuyên Ngành (Vocabulaire Sectoriel)",
            "description": (
                "Mỗi ngành có một \"ngôn ngữ Pháp\" riêng — từ tech đến hôtellerie, từ "
                "luxe đến logistics toàn cầu. Nắm đúng thuật ngữ, bạn được tôn trọng "
                "ngay lập tức."
            ),
            "count": 6,
        },
        {
            # B4 — tone: metaphor_led
            "title": "Vận Hành Doanh Nghiệp (Gestion d'Entreprise)",
            "description": (
                "Doanh nghiệp như một cỗ máy — quản lý dự án là bánh răng, ngân sách "
                "là nhiên liệu, tuân thủ là phanh. Series này giúp bạn vận hành cỗ máy "
                "ấy bằng tiếng Pháp."
            ),
            "count": 6,
        },
        {
            # B5 — tone: provocative_question
            "title": "Kinh Doanh Quốc Tế (Commerce International)",
            "description": (
                "Bạn có thể đàm phán hợp đồng triệu euro bằng tiếng Pháp không? Từ "
                "Incoterms đến văn hóa kinh doanh, series này biến bạn thành đối tác "
                "đáng gờm trên bàn đàm phán."
            ),
            "count": 5,
        },
        {
            # B6 — tone: bold_declaration
            "title": "Khởi Nghiệp & Đổi Mới (Entrepreneuriat et Innovation)",
            "description": (
                "Paris, Lyon và Bruxelles là trung tâm startup Pháp ngữ. Nếu bạn đang "
                "sáng lập, gọi vốn hay gia nhập équipe fondatrice, tiếng Pháp là lợi "
                "thế không thể bỏ qua."
            ),
            "count": 5,
        },
    ],
    # ===== Collection C: Học Thuật & Khoa Học — 5 series, 28 curriculums =====
    "C": [
        {
            # C1 — tone: empathetic_observation
            "title": "Khoa Học & Công Nghệ (Sciences et Technologie)",
            "description": (
                "Đọc bài báo khoa học bằng tiếng Pháp mà cảm thấy lạc lõng? Bạn không "
                "đơn độc. Series này xây nền tảng từ vựng từ sinh học đến tin học để bạn "
                "tiếp cận tự tin."
            ),
            "count": 6,
        },
        {
            # C2 — tone: surprising_fact
            "title": "Kinh Tế & Tài Chính (Économie et Finance)",
            "description": (
                "Pháp là nền kinh tế lớn thứ 7 thế giới, nhưng hầu hết người học bỏ qua "
                "từ vựng tài chính. Từ vi mô đến vĩ mô, từ la Bourse đến ECB — series "
                "này lấp đầy khoảng trống."
            ),
            "count": 6,
        },
        {
            # C3 — tone: metaphor_led
            "title": "Lịch Sử & Chính Trị (Histoire et Politique)",
            "description": (
                "Lịch sử là tấm gương, chính trị là ánh sáng chiếu vào đó. Series này "
                "giúp bạn đọc hiểu và thảo luận về quá khứ lẫn hiện tại của thế giới "
                "Pháp ngữ."
            ),
            "count": 6,
        },
        {
            # C4 — tone: provocative_question
            "title": "Tâm Lý & Giáo Dục (Psychologie et Éducation)",
            "description": (
                "Tại sao trẻ em học ngôn ngữ nhanh hơn người lớn? Tâm lý học và giáo "
                "dục có câu trả lời — series này dạy bạn cách nói về điều đó bằng "
                "tiếng Pháp."
            ),
            "count": 5,
        },
        {
            # C5 — tone: bold_declaration
            "title": "Triết Học & Tư Duy Phản Biện (Philosophie et Pensée Critique)",
            "description": (
                "Triết học Pháp định hình tư tưởng phương Tây suốt nhiều thế kỷ — từ "
                "Descartes đến Foucault. Nắm vững từ vựng triết học là bước đầu tham "
                "gia những cuộc tranh luận sâu sắc nhất."
            ),
            "count": 5,
        },
    ],
    # ===== Collection D: Văn Hóa & Xã Hội — 4 series, 20 curriculums =====
    "D": [
        {
            # D1 — tone: surprising_fact
            "title": "Nghệ Thuật & Văn Học (Arts et Littérature)",
            "description": (
                "Các nhà văn Pháp ngữ đã giành nhiều giải Nobel Văn học hơn hầu hết mọi "
                "nhóm ngôn ngữ khác. Series này mở cánh cửa để bạn nói về nghệ thuật "
                "như người bản xứ."
            ),
            "count": 5,
        },
        {
            # D2 — tone: metaphor_led
            "title": "Kiến Trúc & Thiết Kế (Architecture et Design)",
            "description": (
                "Kiến trúc là ngôn ngữ thầm lặng của một thành phố. Từ Haussmann đến "
                "Le Corbusier, series này dạy bạn đọc và kể câu chuyện của thế giới "
                "xây dựng bằng tiếng Pháp."
            ),
            "count": 5,
        },
        {
            # D3 — tone: provocative_question
            "title": "Truyền Thông & Báo Chí (Médias et Journalisme)",
            "description": (
                "Bạn có thể hiểu bản tin France 24 sau mười giây đầu tiên không? Series "
                "này dẫn bạn qua ngôn ngữ tin tức, tranh luận và truyền thông số bằng "
                "tiếng Pháp."
            ),
            "count": 5,
        },
        {
            # D4 — tone: bold_declaration
            "title": "Truyền Thống & Lễ Hội (Traditions et Fêtes)",
            "description": (
                "Lễ hội Pháp không chỉ là Bastille — đó là cả một hệ thống văn hóa sống "
                "động. Series này giúp bạn mô tả mọi truyền thống, món ăn và lễ kỷ niệm "
                "bằng tiếng Pháp lưu loát."
            ),
            "count": 5,
        },
    ],
    # ===== Collection E: Thiên Nhiên & Đổi Mới — 3 series, 19 curriculums =====
    "E": [
        {
            # E1 — tone: metaphor_led
            "title": "Môi Trường & Bền Vững (Environnement et Durabilité)",
            "description": (
                "Trái đất là ngôi nhà chung, và tiếng Pháp là tiếng nói hàng đầu trong "
                "phong trào xanh toàn cầu. Từ transition énergétique đến lối sống "
                "zero-waste — từ vựng cho tương lai."
            ),
            "count": 7,
        },
        {
            # E2 — tone: provocative_question
            "title": "Công Nghệ Số & Trí Tuệ Nhân Tạo (Technologie Numérique et IA)",
            "description": (
                "Bạn có thể giải thích trí tuệ nhân tạo bằng tiếng Pháp không? Từ "
                "blockchain đến machine learning, series này đưa bạn vào cuộc trò chuyện "
                "công nghệ nóng nhất thế giới Pháp ngữ."
            ),
            "count": 6,
        },
        {
            # E3 — tone: bold_declaration
            "title": "Thể Thao & Giải Trí (Sports et Loisirs)",
            "description": (
                "Thể thao là ngôn ngữ chung của nhân loại — nhưng bình luận trận Ligue 1 "
                "bằng tiếng Pháp là một đẳng cấp khác. Series này đưa bạn từ stade đến "
                "salle de sport."
            ),
            "count": 6,
        },
    ],
}

# Verify planned total:
# A: 6+6+6+6+5+5+6 = 40
# B: 6+6+6+6+5+5   = 34
# C: 6+6+6+5+5     = 28
# D: 5+5+5+5       = 20
# E: 7+6+6         = 19
# Grand total = 40 + 34 + 28 + 20 + 19 = 141 ✓
#
# Planned level distribution across all 25 series (60 beg / 55 preint / 26 inter):
# The per-series level split is finalized in tasks 15.3–15.5 when the individual
# create_*.py scripts are written. Each series respects the max-1-level-gap
# rule (curriculum_series_level_gap view).

# Series counts per collection for iteration
SERIES_COUNTS = {"A": 7, "B": 6, "C": 5, "D": 4, "E": 3}


# ---------------------------------------------------------------------------
# Main execution
# ---------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("vi-fr Orchestrator (bilingual-parity-expansion)")
    print("Creating collections and series")
    print("userLanguage=vi (Vietnamese), language=fr (French)")
    print("Target: 141 curriculums across 5 collections, 25 series")
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

    # --- Step 4: Set collection display orders (1–5) ---
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
    print("SUMMARY — vi-fr Infrastructure (bilingual-parity-expansion)")
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

    print("\n✅ vi-fr orchestrator (bilingual-parity-expansion) complete.")
    return collection_ids, series_ids


if __name__ == "__main__":
    main()
