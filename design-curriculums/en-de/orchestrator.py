"""
en-de orchestrator — Creates 4 collections, 26 series, wires them together,
and sets display orders for the English-German language pair.

Language pair: userLanguage=en (English speakers), language=de (learning German)
User-facing text: English
Reading passages: German

Target: 149 curriculums (59 beginner, 52 preintermediate, 38 intermediate)

Distribution across 4 collections, 26 series:
  Collection A: Daily Life and Travel (Alltag und Reisen) — 7 series, 41 curriculums
  Collection B: Business and Professional (Geschäft und Beruf) — 6 series, 33 curriculums
  Collection C: Academic and Intellectual (Akademisch und Intellektuell) — 7 series, 42 curriculums
  Collection D: Culture and Society (Kultur und Gesellschaft) — 6 series, 33 curriculums

Tone assignments are pre-computed via tone_assigner.assign_tones_for_language_pair(4, 7, 6),
which generates 168 tone slots across a uniform 4x7x6 grid. The orchestrator uses only the
slots needed for each collection's actual series count (A=7, B=6, C=7, D=6) and each series'
actual curriculum count (5 or 6). Unused slots are simply not consumed.

All series descriptions are short persuasive English hooks (≤255 chars) using the assigned tone.
Collection descriptions are short informative English summaries (not persuasive copy).
"""

import sys
import logging

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums/en-de")
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
# counts. We request a 4 × 7 × 6 grid (168 tone slots) — enough to cover the maximum
# of 7 series per collection and 6 curriculums per series. Collections with fewer
# series (B, D = 6) simply ignore the 7th series slot; series with fewer curriculums
# (5 instead of 6) ignore the 6th curriculum slot.
#
# The assigner already enforces:
#   - No adjacent duplicate description tones (curriculums within a series,
#     series within a collection)
#   - No adjacent duplicate farewell tones (curriculums within a series)
#   - No single description tone exceeds 30% across the whole pair
tones = tone_assigner.assign_tones_for_language_pair(4, 7, 6)

# Tone reference (from tone_assigner output, collections A–D):
#
# Collection A (Daily Life and Travel): description_tone = provocative_question
#   Series A1: bold_declaration     — 6 curriculums
#   Series A2: vivid_scenario       — 6 curriculums
#   Series A3: empathetic_observation — 6 curriculums
#   Series A4: surprising_fact      — 6 curriculums
#   Series A5: metaphor_led         — 6 curriculums
#   Series A6: provocative_question — 6 curriculums
#   Series A7: bold_declaration     — 5 curriculums
#
# Collection B (Business and Professional): description_tone = bold_declaration
#   Series B1: vivid_scenario       — 6 curriculums
#   Series B2: empathetic_observation — 6 curriculums
#   Series B3: surprising_fact      — 6 curriculums
#   Series B4: metaphor_led         — 5 curriculums
#   Series B5: provocative_question — 5 curriculums
#   Series B6: bold_declaration     — 5 curriculums
#
# Collection C (Academic and Intellectual): description_tone = vivid_scenario
#   Series C1: empathetic_observation — 6 curriculums
#   Series C2: surprising_fact      — 6 curriculums
#   Series C3: metaphor_led         — 6 curriculums
#   Series C4: provocative_question — 6 curriculums
#   Series C5: bold_declaration     — 6 curriculums
#   Series C6: vivid_scenario       — 6 curriculums
#   Series C7: empathetic_observation — 6 curriculums
#
# Collection D (Culture and Society): description_tone = empathetic_observation
#   Series D1: surprising_fact      — 6 curriculums
#   Series D2: metaphor_led         — 6 curriculums
#   Series D3: provocative_question — 6 curriculums
#   Series D4: bold_declaration     — 5 curriculums
#   Series D5: vivid_scenario       — 5 curriculums
#   Series D6: empathetic_observation — 5 curriculums
#
# Per-curriculum description + farewell tones are printed to stdout at the end of
# this script (see the "Tone Assignments" section), and the curriculum create_*.py
# scripts (tasks 9.3–9.5) will reference that output.

# ---------------------------------------------------------------------------
# Collection definitions — English titles, informative summaries
# ---------------------------------------------------------------------------
COLLECTIONS = [
    {
        "title": "Daily Life and Travel (Alltag und Reisen)",
        "description": (
            "German for everyday situations: travel, dining, shopping, socializing, "
            "health, and home life. Each topic equips you with the vocabulary and "
            "confidence to handle real conversations when living in or visiting "
            "German-speaking countries."
        ),
    },
    {
        "title": "Business and Professional (Geschäft und Beruf)",
        "description": (
            "Professional German for the workplace, job hunting, business operations, "
            "and international trade. From emails and meetings to contract negotiations, "
            "build the language skills you need to advance your career in German-speaking "
            "markets."
        ),
    },
    {
        "title": "Academic and Intellectual (Akademisch und Intellektuell)",
        "description": (
            "Academic German across science, economics, history, psychology, philosophy, "
            "and the humanities. Ideal for learners who want to read specialized texts, "
            "join intellectual discussions, or prepare for study at a German-language "
            "university."
        ),
    },
    {
        "title": "Culture and Society (Kultur und Gesellschaft)",
        "description": (
            "German for arts, architecture, media, environment, sports, and cultural "
            "traditions. Each series opens a different window into German-speaking "
            "cultural life, helping you engage in deeper conversations that go well "
            "beyond everyday small talk."
        ),
    },
]

# ---------------------------------------------------------------------------
# Series definitions — English titles with German topic labels
# Descriptions: short persuasive hooks ≤255 chars using the series' assigned tone
# The "count" field records the number of curriculums planned per series, for
# total-count verification (should sum to 149).
# ---------------------------------------------------------------------------
SERIES = {
    # ===== Collection A: Daily Life and Travel — 7 series, 41 curriculums =====
    "A": [
        {
            # A1 — tone: bold_declaration
            "title": "Food and Dining (Essen und Gastronomie)",
            "description": (
                "German food vocabulary isn't just words — it's the key to an entire "
                "culture. From ordering at a Gasthaus to chatting at a Wochenmarkt, "
                "you'll walk into any German restaurant with confidence."
            ),
            "count": 6,
        },
        {
            # A2 — tone: vivid_scenario
            "title": "City Navigation and Transport (Stadtnavigation und Verkehr)",
            "description": (
                "Picture yourself at Berlin Hauptbahnhof, crowds rushing past — and you "
                "know exactly what to say to find your platform. That's the quiet power "
                "this series hands you."
            ),
            "count": 6,
        },
        {
            # A3 — tone: empathetic_observation
            "title": "Shopping and Services (Einkaufen und Dienstleistungen)",
            "description": (
                "Ever wanted to ask for a different size, compare prices, or open a "
                "Girokonto in German but didn't know where to start? This series was "
                "made for that exact moment."
            ),
            "count": 6,
        },
        {
            # A4 — tone: surprising_fact
            "title": "Social Life and Relationships (Sozialleben und Beziehungen)",
            "description": (
                "Germans distinguish sharply between du and Sie — one wrong choice can "
                "reshape a relationship. Master social German to truly belong rather "
                "than just survive."
            ),
            "count": 6,
        },
        {
            # A5 — tone: metaphor_led
            "title": "Health and Wellness (Gesundheit und Wohlbefinden)",
            "description": (
                "Your health is your second passport when living abroad. This series "
                "arms you with medical, fitness, and self-care German — the vocabulary "
                "that unlocks doors in every clinic and Apotheke."
            ),
            "count": 6,
        },
        {
            # A6 — tone: provocative_question
            "title": "Home and Housing (Zuhause und Wohnen)",
            "description": (
                "Could you rent an apartment, argue a Nebenkosten bill, or register at "
                "the Bürgeramt entirely in German? If the answer is no, this series is "
                "the fastest path to yes."
            ),
            "count": 6,
        },
        {
            # A7 — tone: bold_declaration
            "title": "Travel and Tourism (Reisen und Tourismus)",
            "description": (
                "Real travel begins where guidebook German ends. Book a room, recover a "
                "lost bag, or join a Wanderung conversation — this series turns you "
                "into a traveler, not a tourist."
            ),
            "count": 5,
        },
    ],
    # ===== Collection B: Business and Professional — 6 series, 33 curriculums =====
    "B": [
        {
            # B1 — tone: vivid_scenario
            "title": "Workplace Communication (Kommunikation am Arbeitsplatz)",
            "description": (
                "Imagine presenting to a boardroom full of German colleagues — confident, "
                "clear, professional. This series takes you from first-day emails to "
                "flawless presentations without a stumble."
            ),
            "count": 6,
        },
        {
            # B2 — tone: empathetic_observation
            "title": "Job Search and Career (Jobsuche und Karriere)",
            "description": (
                "Writing a Lebenslauf in German is hard enough; interviewing is even "
                "harder. If you're chasing career opportunities in the DACH region, "
                "this is the stepping stone you need."
            ),
            "count": 6,
        },
        {
            # B3 — tone: surprising_fact
            "title": "Industry-Specific Vocabulary (Branchenspezifischer Wortschatz)",
            "description": (
                "Every industry speaks its own German — from IT to hospitality, from "
                "Mittelstand manufacturing to global logistics. Nail the right terms "
                "and earn instant respect."
            ),
            "count": 6,
        },
        {
            # B4 — tone: metaphor_led
            "title": "Business Operations (Geschäftsbetrieb)",
            "description": (
                "A business is a machine — project management is the gears, budgeting "
                "is the fuel, compliance is the brake. This series helps you run that "
                "machine fluently in German."
            ),
            "count": 5,
        },
        {
            # B5 — tone: provocative_question
            "title": "International Business (Internationaler Handel)",
            "description": (
                "Could you negotiate a million-euro contract in German? From Incoterms "
                "to cross-cultural etiquette, this series turns you into a formidable "
                "partner at the international table."
            ),
            "count": 5,
        },
        {
            # B6 — tone: bold_declaration
            "title": "Entrepreneurship and Innovation (Unternehmertum und Innovation)",
            "description": (
                "Berlin, Munich, and Vienna are powerhouses of European startups. If "
                "you're founding, pitching, or joining a Gründerteam, German fluency "
                "is the unfair advantage you cannot afford to skip."
            ),
            "count": 5,
        },
    ],
    # ===== Collection C: Academic and Intellectual — 7 series, 42 curriculums =====
    "C": [
        {
            # C1 — tone: empathetic_observation
            "title": "Science and Technology (Wissenschaft und Technologie)",
            "description": (
                "Reading a scientific paper in German and feeling lost? You're not "
                "alone. This series builds your vocabulary from biology to computer "
                "science so you can engage with confidence."
            ),
            "count": 6,
        },
        {
            # C2 — tone: surprising_fact
            "title": "Economics and Finance (Wirtschaft und Finanzen)",
            "description": (
                "Germany is the world's third-largest economy, yet most learners skip "
                "financial vocabulary. From micro to macro, from Sparkasse to DAX, "
                "this series fills that gap."
            ),
            "count": 6,
        },
        {
            # C3 — tone: metaphor_led
            "title": "History and Politics (Geschichte und Politik)",
            "description": (
                "History is the mirror; politics is the light cast upon it. This series "
                "helps you read, discuss, and debate the past and the present of "
                "German-speaking Europe."
            ),
            "count": 6,
        },
        {
            # C4 — tone: provocative_question
            "title": "Psychology and Education (Psychologie und Bildung)",
            "description": (
                "Why do children learn languages faster than adults? Psychology and "
                "education research has answers — and this series teaches you how to "
                "talk about them in German."
            ),
            "count": 6,
        },
        {
            # C5 — tone: bold_declaration
            "title": "Philosophy and Critical Thinking (Philosophie und kritisches Denken)",
            "description": (
                "German philosophy has shaped Western thought for centuries — from Kant "
                "to Heidegger to Habermas. Mastering philosophical vocabulary is the "
                "first step to joining the deepest debates."
            ),
            "count": 6,
        },
        {
            # C6 — tone: vivid_scenario
            "title": "Humanities and Literary Studies (Geisteswissenschaften und Literaturwissenschaft)",
            "description": (
                "Picture yourself in a Seminar at Heidelberg, analysing a Goethe poem "
                "line by line in German. This series equips you with the textual and "
                "critical vocabulary to be part of that conversation."
            ),
            "count": 6,
        },
        {
            # C7 — tone: empathetic_observation
            "title": "Research and Academic Writing (Forschung und wissenschaftliches Schreiben)",
            "description": (
                "Writing a Hausarbeit or thesis in German can feel overwhelming when "
                "your vocabulary stalls on the first sentence. This series walks with "
                "you through every academic register you need."
            ),
            "count": 6,
        },
    ],
    # ===== Collection D: Culture and Society — 6 series, 33 curriculums =====
    "D": [
        {
            # D1 — tone: surprising_fact
            "title": "Arts and Literature (Kunst und Literatur)",
            "description": (
                "German-speaking writers have won more Nobel Prizes in Literature than "
                "almost any other language group. This series opens the door to "
                "discussing art and literature like a native speaker."
            ),
            "count": 6,
        },
        {
            # D2 — tone: metaphor_led
            "title": "Architecture and Design (Architektur und Design)",
            "description": (
                "Architecture is the silent language of a city. From Bauhaus to "
                "Passivhaus, this series teaches you to read and retell the story of "
                "the built world in German."
            ),
            "count": 6,
        },
        {
            # D3 — tone: provocative_question
            "title": "Environment and Sustainability (Umwelt und Nachhaltigkeit)",
            "description": (
                "Can you explain the Energiewende in German? From renewable energy to "
                "zero-waste living, this series equips you with the language for the "
                "most important conversation of our time."
            ),
            "count": 6,
        },
        {
            # D4 — tone: bold_declaration
            "title": "Sports and Recreation (Sport und Freizeit)",
            "description": (
                "Sport is humanity's universal language — but commentating a "
                "Bundesliga match in German is another league entirely. This series "
                "takes you from the Fußballplatz to the gym with specialized vocabulary."
            ),
            "count": 5,
        },
        {
            # D5 — tone: vivid_scenario
            "title": "Traditions and Festivals (Traditionen und Feste)",
            "description": (
                "Imagine standing at Oktoberfest, the crowd singing in unison — and "
                "you can describe every moment, every dish, every Tracht in fluent "
                "German. That is the promise of this series."
            ),
            "count": 5,
        },
        {
            # D6 — tone: empathetic_observation
            "title": "Media and Journalism (Medien und Journalismus)",
            "description": (
                "Switching on a Tagesschau broadcast and feeling lost after ten seconds "
                "is a shared rite of passage. This series gently walks you through the "
                "language of German news, debate, and digital media."
            ),
            "count": 5,
        },
    ],
}

# Verify planned total:
# A: 6+6+6+6+6+6+5 = 41
# B: 6+6+6+5+5+5   = 33
# C: 6+6+6+6+6+6+6 = 42
# D: 6+6+6+5+5+5   = 33
# Grand total = 149 ✓
#
# Planned level distribution across all 26 series (59 beg / 52 preint / 38 inter):
# The per-series level split is finalized in tasks 9.3–9.5 when the individual
# create_*.py scripts are written. Each series respects the max-1-level-gap
# rule (curriculum_series_level_gap view).

# Series counts per collection for iteration
SERIES_COUNTS = {"A": 7, "B": 6, "C": 7, "D": 6}


# ---------------------------------------------------------------------------
# Main execution
# ---------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("en-de Orchestrator — Creating collections and series")
    print("userLanguage=en (English), language=de (German)")
    print("Target: 149 curriculums across 4 collections, 26 series")
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

    print("\n✅ en-de orchestrator complete.")
    return collection_ids, series_ids


if __name__ == "__main__":
    main()
