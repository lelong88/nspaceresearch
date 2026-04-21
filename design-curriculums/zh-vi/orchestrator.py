"""
zh-vi orchestrator — Creates 4 collections, 16 series, wires them together,
and sets display orders for the Chinese-Vietnamese language pair.

Language pair: userLanguage=zh, language=vi
Total gap: 79 curriculums (31 beginner, 22 preintermediate, 26 intermediate)
Layout: 4 collections × 4 series = 16 series, ~5 curriculums per series

Tone assignments are pre-computed via tone_assigner.assign_tones_for_language_pair(4, 4, 5).
All series descriptions are short persuasive Chinese hooks (≤255 chars) using the assigned tone.
Collection descriptions are short informative Chinese summaries (not persuasive copy).

Requirements: 6.1–6.8, 8.1–8.4, 8.7
"""

import sys
import logging

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums/zh-vi")
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
# Tone assignments from tone_assigner.assign_tones_for_language_pair(4, 4, 5)
# ---------------------------------------------------------------------------
tones = tone_assigner.assign_tones_for_language_pair(4, 4, 5)

# Collection 0 (A): description_tone = provocative_question
#   Series A1: bold_declaration
#     Curriculum 1: desc=vivid_scenario, farewell=introspective_guide
#     Curriculum 2: desc=empathetic_observation, farewell=warm_accountability
#     Curriculum 3: desc=surprising_fact, farewell=team_building_energy
#     Curriculum 4: desc=metaphor_led, farewell=quiet_awe
#     Curriculum 5: desc=provocative_question, farewell=practical_momentum
#   Series A2: vivid_scenario
#     Curriculum 1: desc=empathetic_observation, farewell=warm_accountability
#     Curriculum 2: desc=surprising_fact, farewell=team_building_energy
#     Curriculum 3: desc=metaphor_led, farewell=quiet_awe
#     Curriculum 4: desc=provocative_question, farewell=practical_momentum
#     Curriculum 5: desc=bold_declaration, farewell=introspective_guide
#   Series A3: empathetic_observation
#     Curriculum 1: desc=surprising_fact, farewell=team_building_energy
#     Curriculum 2: desc=metaphor_led, farewell=quiet_awe
#     Curriculum 3: desc=provocative_question, farewell=practical_momentum
#     Curriculum 4: desc=bold_declaration, farewell=introspective_guide
#     Curriculum 5: desc=vivid_scenario, farewell=warm_accountability
#   Series A4: surprising_fact
#     Curriculum 1: desc=metaphor_led, farewell=quiet_awe
#     Curriculum 2: desc=provocative_question, farewell=practical_momentum
#     Curriculum 3: desc=bold_declaration, farewell=introspective_guide
#     Curriculum 4: desc=vivid_scenario, farewell=warm_accountability
#     Curriculum 5: desc=empathetic_observation, farewell=team_building_energy
#
# Collection 1 (B): description_tone = bold_declaration
#   Series B1: vivid_scenario
#     Curriculum 1: desc=empathetic_observation, farewell=practical_momentum
#     Curriculum 2: desc=surprising_fact, farewell=introspective_guide
#     Curriculum 3: desc=metaphor_led, farewell=warm_accountability
#     Curriculum 4: desc=provocative_question, farewell=team_building_energy
#     Curriculum 5: desc=bold_declaration, farewell=quiet_awe
#   Series B2: empathetic_observation
#     Curriculum 1: desc=surprising_fact, farewell=introspective_guide
#     Curriculum 2: desc=metaphor_led, farewell=warm_accountability
#     Curriculum 3: desc=provocative_question, farewell=team_building_energy
#     Curriculum 4: desc=bold_declaration, farewell=quiet_awe
#     Curriculum 5: desc=vivid_scenario, farewell=practical_momentum
#   Series B3: surprising_fact
#     Curriculum 1: desc=metaphor_led, farewell=warm_accountability
#     Curriculum 2: desc=provocative_question, farewell=team_building_energy
#     Curriculum 3: desc=bold_declaration, farewell=quiet_awe
#     Curriculum 4: desc=vivid_scenario, farewell=practical_momentum
#     Curriculum 5: desc=empathetic_observation, farewell=introspective_guide
#   Series B4: metaphor_led
#     Curriculum 1: desc=provocative_question, farewell=team_building_energy
#     Curriculum 2: desc=bold_declaration, farewell=quiet_awe
#     Curriculum 3: desc=vivid_scenario, farewell=practical_momentum
#     Curriculum 4: desc=empathetic_observation, farewell=introspective_guide
#     Curriculum 5: desc=surprising_fact, farewell=warm_accountability
#
# Collection 2 (C): description_tone = vivid_scenario
#   Series C1: empathetic_observation
#     Curriculum 1: desc=surprising_fact, farewell=quiet_awe
#     Curriculum 2: desc=metaphor_led, farewell=practical_momentum
#     Curriculum 3: desc=provocative_question, farewell=introspective_guide
#     Curriculum 4: desc=bold_declaration, farewell=warm_accountability
#     Curriculum 5: desc=vivid_scenario, farewell=team_building_energy
#   Series C2: surprising_fact
#     Curriculum 1: desc=metaphor_led, farewell=practical_momentum
#     Curriculum 2: desc=provocative_question, farewell=introspective_guide
#     Curriculum 3: desc=bold_declaration, farewell=warm_accountability
#     Curriculum 4: desc=vivid_scenario, farewell=team_building_energy
#     Curriculum 5: desc=empathetic_observation, farewell=quiet_awe
#   Series C3: metaphor_led
#     Curriculum 1: desc=provocative_question, farewell=introspective_guide
#     Curriculum 2: desc=bold_declaration, farewell=warm_accountability
#     Curriculum 3: desc=vivid_scenario, farewell=team_building_energy
#     Curriculum 4: desc=empathetic_observation, farewell=quiet_awe
#     Curriculum 5: desc=surprising_fact, farewell=practical_momentum
#   Series C4: provocative_question
#     Curriculum 1: desc=bold_declaration, farewell=warm_accountability
#     Curriculum 2: desc=vivid_scenario, farewell=team_building_energy
#     Curriculum 3: desc=empathetic_observation, farewell=quiet_awe
#     Curriculum 4: desc=surprising_fact, farewell=practical_momentum
#     Curriculum 5: desc=metaphor_led, farewell=introspective_guide
#
# Collection 3 (D): description_tone = empathetic_observation
#   Series D1: surprising_fact
#     Curriculum 1: desc=metaphor_led, farewell=team_building_energy
#     Curriculum 2: desc=provocative_question, farewell=quiet_awe
#     Curriculum 3: desc=bold_declaration, farewell=practical_momentum
#     Curriculum 4: desc=vivid_scenario, farewell=introspective_guide
#     Curriculum 5: desc=empathetic_observation, farewell=warm_accountability
#   Series D2: metaphor_led
#     Curriculum 1: desc=provocative_question, farewell=quiet_awe
#     Curriculum 2: desc=bold_declaration, farewell=practical_momentum
#     Curriculum 3: desc=vivid_scenario, farewell=introspective_guide
#     Curriculum 4: desc=empathetic_observation, farewell=warm_accountability
#     Curriculum 5: desc=surprising_fact, farewell=team_building_energy
#   Series D3: provocative_question
#     Curriculum 1: desc=bold_declaration, farewell=practical_momentum
#     Curriculum 2: desc=vivid_scenario, farewell=introspective_guide
#     Curriculum 3: desc=empathetic_observation, farewell=warm_accountability
#     Curriculum 4: desc=surprising_fact, farewell=team_building_energy
#     Curriculum 5: desc=metaphor_led, farewell=quiet_awe
#   Series D4: bold_declaration
#     Curriculum 1: desc=vivid_scenario, farewell=introspective_guide
#     Curriculum 2: desc=empathetic_observation, farewell=warm_accountability
#     Curriculum 3: desc=surprising_fact, farewell=team_building_energy
#     Curriculum 4: desc=metaphor_led, farewell=quiet_awe
#     Curriculum 5: desc=provocative_question, farewell=practical_momentum

# ---------------------------------------------------------------------------
# Collection definitions — Chinese titles, informative category summaries
# ---------------------------------------------------------------------------
COLLECTIONS = [
    {
        "title": "日常生活与旅行 (Cuộc sống & Du lịch)",
        "description": (
            "越南语日常场景：旅行、餐饮、购物、社交与健康。"
            "每个主题帮助你掌握在越南生活或旅行时所需的核心词汇和表达方式。"
        ),
    },
    {
        "title": "商务与职场 (Kinh doanh & Nghề nghiệp)",
        "description": (
            "越南语职场沟通：求职、会议、商务运营与国际贸易。"
            "从邮件写作到合同谈判，构建在越南市场发展所需的语言能力。"
        ),
    },
    {
        "title": "学术与思想 (Học thuật & Tri thức)",
        "description": (
            "越南语学术领域：科学、经济、历史、心理学与哲学。"
            "适合希望阅读专业文献、参与学术讨论或准备留学的学习者。"
        ),
    },
    {
        "title": "文化与社会 (Văn hóa & Xã hội)",
        "description": (
            "越南语文化探索：艺术、建筑、环境、体育与传统节日。"
            "每个系列打开一扇了解越南文化生活的窗口，让你的对话超越日常寒暄。"
        ),
    },
]

# ---------------------------------------------------------------------------
# Series definitions — 4 per collection, Chinese titles with Vietnamese labels
# Descriptions: short persuasive hooks ≤255 chars using assigned tone
# ---------------------------------------------------------------------------
SERIES = {
    # ===== Collection A: 日常生活与旅行 =====
    "A": [
        {
            # A1 — tone: bold_declaration
            "title": "美食与餐饮 (Ẩm thực)",
            "description": (
                "越南美食不只是味觉体验——它是一整套文化密码。"
                "从街头小吃到高档餐厅，掌握点餐、食材和烹饪词汇，让你像本地人一样享受每一餐。"
            ),
        },
        {
            # A2 — tone: vivid_scenario
            "title": "城市出行与交通 (Giao thông)",
            "description": (
                "想象你站在胡志明市的十字路口，摩托车如潮水般涌来——"
                "而你能自信地用越南语问路、打车、买票。这个系列让你做到。"
            ),
        },
        {
            # A3 — tone: empathetic_observation
            "title": "购物与服务 (Mua sắm & Dịch vụ)",
            "description": (
                "想在越南市场讨价还价却不知从何开口？"
                "这个系列专为那些想要自如应对购物、银行和日常服务场景的学习者设计。"
            ),
        },
        {
            # A4 — tone: surprising_fact
            "title": "社交与人际关系 (Quan hệ xã hội)",
            "description": (
                "越南语中称呼系统的复杂程度远超你的想象——用错一个称谓就可能改变整段关系。"
                "掌握社交越南语，真正融入而非仅仅生存。"
            ),
        },
    ],
    # ===== Collection B: 商务与职场 =====
    "B": [
        {
            # B1 — tone: vivid_scenario
            "title": "职场沟通 (Giao tiếp công sở)",
            "description": (
                "想象你在河内的会议室里用流利的越南语做报告——自信、清晰、专业。"
                "这个系列带你从邮件到演示，一步步建立职场越南语能力。"
            ),
        },
        {
            # B2 — tone: empathetic_observation
            "title": "求职与职业发展 (Tìm việc & Sự nghiệp)",
            "description": (
                "用越南语写简历已经够难了，面试更是挑战。"
                "如果你正在越南市场寻找职业机会，这个系列是你最需要的起点。"
            ),
        },
        {
            # B3 — tone: surprising_fact
            "title": "行业专业词汇 (Từ vựng chuyên ngành)",
            "description": (
                "每个行业都有自己的语言——从科技到酒店、制造到物流。"
                "掌握精准的行业术语，立刻赢得越南同事的专业认可。"
            ),
        },
        {
            # B4 — tone: metaphor_led
            "title": "商务运营与贸易 (Vận hành & Thương mại)",
            "description": (
                "企业如同一台精密机器——项目管理是齿轮，预算是燃料。"
                "这个系列帮你用越南语驾驭这台机器，从运营到国际贸易。"
            ),
        },
    ],
    # ===== Collection C: 学术与思想 =====
    "C": [
        {
            # C1 — tone: empathetic_observation
            "title": "科学与技术 (Khoa học & Công nghệ)",
            "description": (
                "读越南语科学论文时感到迷茫？你不是一个人。"
                "这个系列从生物到计算机科学，帮你建立学术越南语的自信。"
            ),
        },
        {
            # C2 — tone: surprising_fact
            "title": "经济与金融 (Kinh tế & Tài chính)",
            "description": (
                "越南是东南亚增长最快的经济体之一，但大多数学习者忽略了金融词汇。"
                "从宏观到微观，这个系列填补这一空白。"
            ),
        },
        {
            # C3 — tone: metaphor_led
            "title": "历史与政治 (Lịch sử & Chính trị)",
            "description": (
                "历史是一面镜子，政治是照在镜上的光。"
                "这个系列帮你用越南语阅读、讨论和辩论过去与现在。"
            ),
        },
        {
            # C4 — tone: provocative_question
            "title": "心理学与教育 (Tâm lý học & Giáo dục)",
            "description": (
                "为什么孩子学语言比成人快？心理学有答案——"
                "这个系列教你如何用越南语谈论这些话题。"
            ),
        },
    ],
    # ===== Collection D: 文化与社会 =====
    "D": [
        {
            # D1 — tone: surprising_fact
            "title": "艺术与文学 (Nghệ thuật & Văn học)",
            "description": (
                "越南文学从口传史诗到现代小说，跨越千年历史。"
                "这个系列为你打开用越南语讨论艺术与文学的大门。"
            ),
        },
        {
            # D2 — tone: metaphor_led
            "title": "建筑与设计 (Kiến trúc & Thiết kế)",
            "description": (
                "建筑是城市无声的语言。"
                "从古老的皇城到现代摩天大楼，这个系列帮你用越南语读懂并讲述这些故事。"
            ),
        },
        {
            # D3 — tone: provocative_question
            "title": "环境与可持续发展 (Môi trường & Phát triển bền vững)",
            "description": (
                "你能用越南语解释气候变化吗？从可再生能源到绿色生活，"
                "这个系列为你装备当今最重要议题的语言工具。"
            ),
        },
        {
            # D4 — tone: bold_declaration
            "title": "体育与休闲 (Thể thao & Giải trí)",
            "description": (
                "体育是人类共通的语言——但用越南语解说比赛是另一个层次。"
                "这个系列带你从球场到健身房，掌握专业体育词汇。"
            ),
        },
    ],
}


# ---------------------------------------------------------------------------
# Main execution
# ---------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("zh-vi Orchestrator — Creating collections and series")
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
    print("\n--- Creating 16 series ---")
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
        for j in range(4):
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

    # --- Step 5: Set series display orders (1-4 within each collection) ---
    print("\n--- Setting series display orders ---")
    for col_key in collection_keys:
        for j in range(4):
            ser_label = f"{col_key}{j + 1}"
            ser_id = series_ids[ser_label]
            order = j + 1
            set_series_display_order(ser_id, order)
            print(f"  Series {ser_label} ({ser_id}) -> displayOrder {order}")

    # --- Summary ---
    print("\n" + "=" * 60)
    print("SUMMARY — zh-vi Infrastructure")
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

    print("\n✅ zh-vi orchestrator complete.")
    return collection_ids, series_ids


if __name__ == "__main__":
    main()
