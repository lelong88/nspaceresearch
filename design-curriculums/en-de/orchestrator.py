"""
en-de orchestrator — Creates 4 collections, 20 series, wires them together,
and sets display orders for the English-German language pair.

Tone assignments are pre-computed via tone_assigner.assign_tones_for_language_pair(4, 5, 5).
All series descriptions are short persuasive English hooks (≤255 chars) using the assigned tone.
Collection descriptions are short informative English summaries (not persuasive copy).
"""

import sys
import logging

sys.path.insert(0, "/home/ubuntu/nspaceresearch2/design-curriculums")
sys.path.insert(0, "/home/ubuntu/nspaceresearch2/design-curriculums/en-de")
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
        "title": "Daily Life and Travel (Alltag und Reisen)",
        "description": (
            "German for everyday situations: travel, dining, shopping, socializing, "
            "and health. Each topic equips you with the vocabulary and confidence to "
            "handle real conversations when living in or visiting German-speaking countries."
        ),
    },
    {
        "title": "Business and Professional (Geschäft und Beruf)",
        "description": (
            "Professional German for the workplace, job hunting, business operations, "
            "and international trade. From emails and meetings to contract negotiations, "
            "build the language skills you need to advance your career in German-speaking markets."
        ),
    },
    {
        "title": "Academic and Intellectual (Akademisch und Intellektuell)",
        "description": (
            "Academic German across science, economics, history, psychology, and philosophy. "
            "Ideal for anyone who wants to read specialized texts, join intellectual discussions, "
            "or prepare for study in a German-language university environment."
        ),
    },
    {
        "title": "Culture and Society (Kultur und Gesellschaft)",
        "description": (
            "German for arts, architecture, environment, sports, and cultural traditions. "
            "Each series opens a different window into German-speaking cultural life, helping you "
            "engage in deeper conversations that go well beyond everyday small talk."
        ),
    },
]

# ---------------------------------------------------------------------------
# Series definitions — 5 per collection, English titles with German labels
# Descriptions: short persuasive hooks ≤255 chars using assigned tone
# ---------------------------------------------------------------------------
SERIES = {
    # ===== Collection A: Daily Life and Travel =====
    "A": [
        {
            # A1 — tone: bold_declaration
            "title": "Food and Dining (Essen und Gastronomie)",
            "description": (
                "German food vocabulary isn't just words — it's the key to an entire culture. "
                "From ordering at a Gasthaus to chatting at a Wochenmarkt, you'll walk into any German restaurant with confidence."
            ),
        },
        {
            # A2 — tone: vivid_scenario
            "title": "City Navigation and Transport (Stadtnavigation und Verkehr)",
            "description": (
                "Picture yourself at Berlin Hauptbahnhof, crowds rushing past — and you know exactly what to say "
                "to find your platform. That's the power of this series."
            ),
        },
        {
            # A3 — tone: empathetic_observation
            "title": "Shopping and Services (Einkaufen und Dienstleistungen)",
            "description": (
                "Ever wanted to ask for a different size, compare prices, or open a Girokonto in German "
                "but didn't know where to start? This series was made for that moment."
            ),
        },
        {
            # A4 — tone: surprising_fact
            "title": "Social Life and Relationships (Sozialleben und Beziehungen)",
            "description": (
                "Germans distinguish sharply between 'du' and 'Sie' — one wrong choice can reshape a relationship. "
                "Master social German to truly belong, not just survive."
            ),
        },
        {
            # A5 — tone: metaphor_led
            "title": "Health and Wellness (Gesundheit und Wohlbefinden)",
            "description": (
                "Your health is your second passport when living abroad. "
                "This series arms you with medical, fitness, and self-care vocabulary in German."
            ),
        },
    ],
    # ===== Collection B: Business and Professional =====
    "B": [
        {
            # B1 — tone: vivid_scenario
            "title": "Workplace Communication (Kommunikation am Arbeitsplatz)",
            "description": (
                "Imagine presenting to a boardroom full of German colleagues — confident, clear, professional. "
                "This series takes you from emails to presentations without a stumble."
            ),
        },
        {
            # B2 — tone: empathetic_observation
            "title": "Job Search and Career (Jobsuche und Karriere)",
            "description": (
                "Writing a Lebenslauf in German is hard enough; interviewing is even harder. If you're chasing career "
                "opportunities in the DACH region, this is the stepping stone you need."
            ),
        },
        {
            # B3 — tone: surprising_fact
            "title": "Industry-Specific Vocabulary (Branchenspezifischer Wortschatz)",
            "description": (
                "Every industry speaks its own language — from tech to hospitality, manufacturing to logistics. "
                "Nail the right terminology and earn instant respect from German colleagues."
            ),
        },
        {
            # B4 — tone: metaphor_led
            "title": "Business Operations (Geschäftsbetrieb)",
            "description": (
                "A business is a machine — project management is the gears, budgeting is the fuel. "
                "This series helps you run that machine in German."
            ),
        },
        {
            # B5 — tone: provocative_question
            "title": "International Business (Internationaler Handel)",
            "description": (
                "Could you negotiate a million-euro contract in German? From trade terms to business law, "
                "this series turns you into a formidable partner at the international table."
            ),
        },
    ],
    # ===== Collection C: Academic and Intellectual =====
    "C": [
        {
            # C1 — tone: empathetic_observation
            "title": "Science and Technology (Wissenschaft und Technologie)",
            "description": (
                "Reading a scientific paper in German and feeling lost? You're not alone. "
                "This series builds your vocabulary from biology to computer science so you can engage with confidence."
            ),
        },
        {
            # C2 — tone: surprising_fact
            "title": "Economics and Finance (Wirtschaft und Finanzen)",
            "description": (
                "Germany is the world's 3rd largest economy, yet most learners skip financial vocabulary. "
                "From micro to macro, this series fills that gap."
            ),
        },
        {
            # C3 — tone: metaphor_led
            "title": "History and Politics (Geschichte und Politik)",
            "description": (
                "History is the mirror; politics is the light cast upon it. "
                "This series helps you read, discuss, and debate the past and present in German."
            ),
        },
        {
            # C4 — tone: provocative_question
            "title": "Psychology and Education (Psychologie und Bildung)",
            "description": (
                "Why do children learn languages faster than adults? Psychology has the answer — "
                "and this series teaches you how to talk about it in German."
            ),
        },
        {
            # C5 — tone: bold_declaration
            "title": "Philosophy and Critical Thinking (Philosophie und kritisches Denken)",
            "description": (
                "German philosophy has shaped Western thought for centuries — from Kant to Heidegger. "
                "Mastering philosophical vocabulary is the first step to joining the deepest debates."
            ),
        },
    ],
    # ===== Collection D: Culture and Society =====
    "D": [
        {
            # D1 — tone: surprising_fact
            "title": "Arts and Literature (Kunst und Literatur)",
            "description": (
                "Germany has produced more Nobel laureates in literature than almost any other country. "
                "This series opens the door to discussing art and literature like a native speaker."
            ),
        },
        {
            # D2 — tone: metaphor_led
            "title": "Architecture and Design (Architektur und Design)",
            "description": (
                "Architecture is the silent language of a city. "
                "From Bauhaus to sustainable design, this series helps you read and tell that story in German."
            ),
        },
        {
            # D3 — tone: provocative_question
            "title": "Environment and Sustainability (Umwelt und Nachhaltigkeit)",
            "description": (
                "Can you explain the Energiewende in German? From renewable energy to green living, "
                "this series equips you with the language for the most important conversation of our time."
            ),
        },
        {
            # D4 — tone: bold_declaration
            "title": "Sports and Recreation (Sport und Freizeit)",
            "description": (
                "Sport is humanity's universal language — but commentating in German is a different league. "
                "This series takes you from the Fußballplatz to the gym with specialized vocabulary."
            ),
        },
        {
            # D5 — tone: vivid_scenario
            "title": "Traditions and Festivals (Traditionen und Feste)",
            "description": (
                "Imagine standing in the middle of Oktoberfest, the crowd singing in unison — "
                "and you can describe every moment in German."
            ),
        },
    ],
}


# ---------------------------------------------------------------------------
# Main execution
# ---------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("en-de Orchestrator — Creating collections and series")
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
    print("SUMMARY — en-de Infrastructure")
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

    print("\n✅ en-de orchestrator complete.")
    return collection_ids, series_ids


if __name__ == "__main__":
    main()
