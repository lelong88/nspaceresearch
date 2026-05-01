"""
en-fr orchestrator (bilingual-parity-expansion) — Creates 5 collections, 25 series,
wires them together, and sets display orders for the English-French language pair.

Language pair: userLanguage=en (English speakers), language=fr (learning French)
User-facing text (titles, descriptions): English
Reading passages: French
Session titles: Part 1, Part 2, Part 3, Review, Final Reading

Target: 138 curriculums (58 beginner, 51 preintermediate, 29 intermediate)

Distribution across 5 collections, 25 series:
  Collection A: Daily Life & Travel — 7 series, 40 curriculums
  Collection B: Business & Career — 6 series, 34 curriculums
  Collection C: Academic & Science — 5 series, 28 curriculums
  Collection D: Culture & Society — 4 series, 20 curriculums
  Collection E: Nature & Innovation — 3 series, 16 curriculums

Tone assignments are pre-computed via tone_assigner.assign_tones_for_language_pair(5, 7, 7),
which generates 245 tone slots across a uniform 5×7×7 grid. The orchestrator uses only the
slots needed for each collection's actual series count (A=7, B=6, C=5, D=4, E=3) and each
series' actual curriculum count (5 or 6). Unused slots are simply not consumed.

All series descriptions are short persuasive English hooks (≤255 chars) using the assigned tone.
Collection descriptions are short informative English summaries (not persuasive copy).

Requirements: 6.1–6.8, 8.1–8.4, 8.7
"""

import sys
import logging

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums/en-fr")
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
# curriculums (5 instead of 6) ignore extra curriculum slots.
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
# Collection A (Daily Life & Travel): description_tone = provocative_question
#   Series A1: bold_declaration       — 6 curriculums
#   Series A2: vivid_scenario         — 6 curriculums
#   Series A3: empathetic_observation — 6 curriculums
#   Series A4: surprising_fact        — 6 curriculums
#   Series A5: metaphor_led           — 5 curriculums
#   Series A6: provocative_question   — 5 curriculums
#   Series A7: bold_declaration       — 6 curriculums
#
# Collection B (Business & Career): description_tone = bold_declaration
#   Series B1: vivid_scenario         — 6 curriculums
#   Series B2: empathetic_observation — 6 curriculums
#   Series B3: surprising_fact        — 6 curriculums
#   Series B4: metaphor_led           — 6 curriculums
#   Series B5: provocative_question   — 5 curriculums
#   Series B6: bold_declaration       — 5 curriculums
#
# Collection C (Academic & Science): description_tone = vivid_scenario
#   Series C1: empathetic_observation — 6 curriculums
#   Series C2: surprising_fact        — 6 curriculums
#   Series C3: metaphor_led           — 6 curriculums
#   Series C4: provocative_question   — 5 curriculums
#   Series C5: bold_declaration       — 5 curriculums
#
# Collection D (Culture & Society): description_tone = empathetic_observation
#   Series D1: surprising_fact        — 5 curriculums
#   Series D2: metaphor_led           — 5 curriculums
#   Series D3: provocative_question   — 5 curriculums
#   Series D4: bold_declaration       — 5 curriculums
#
# Collection E (Nature & Innovation): description_tone = surprising_fact
#   Series E1: metaphor_led           — 6 curriculums
#   Series E2: provocative_question   — 5 curriculums
#   Series E3: bold_declaration       — 5 curriculums
#
# Per-curriculum description + farewell tones are printed to stdout at the end of
# this script (see the "Tone Assignments" section), and the curriculum create_*.py
# scripts (tasks 13.3–13.5) will reference that output.

# ---------------------------------------------------------------------------
# Collection definitions — English titles with French labels,
# informative summaries (not persuasive copy)
# ---------------------------------------------------------------------------
COLLECTIONS = [
    {
        "title": "Daily Life & Travel (Vie Quotidienne et Voyages)",
        "description": (
            "French for everyday situations: dining, transportation, shopping, "
            "socializing, health, housing, and travel. Each topic builds the "
            "vocabulary and confidence you need for real conversations when "
            "living in or visiting French-speaking countries."
        ),
    },
    {
        "title": "Business & Career (Affaires et Carrière)",
        "description": (
            "Professional French for the workplace, job hunting, industry "
            "terminology, business operations, and international trade. From "
            "emails and meetings to contract negotiations — the language skills "
            "to advance your career in Francophone markets."
        ),
    },
    {
        "title": "Academic & Science (Sciences et Savoir)",
        "description": (
            "Academic French across science, economics, history, psychology, "
            "and philosophy. Designed for learners who want to read specialized "
            "texts, participate in intellectual discussions, or prepare for "
            "study at a French-language university."
        ),
    },
    {
        "title": "Culture & Society (Culture et Société)",
        "description": (
            "French for arts, architecture, media, and cultural traditions. "
            "Each series opens a different window into Francophone cultural "
            "life, helping you engage in richer conversations that go well "
            "beyond everyday small talk."
        ),
    },
    {
        "title": "Nature & Innovation (Nature et Innovation)",
        "description": (
            "French for environment, sustainability, digital technology, and "
            "sports. Explore the vocabulary for topics shaping the future — "
            "from renewable energy to artificial intelligence in the "
            "Francophone context."
        ),
    },
]

# ---------------------------------------------------------------------------
# Series definitions — English titles with French topic labels
# Descriptions: short persuasive hooks ≤255 chars using the series' assigned tone
# The "count" field records the number of curriculums planned per series, for
# total-count verification (should sum to 138).
# ---------------------------------------------------------------------------
SERIES = {
    # ===== Collection A: Daily Life & Travel — 7 series, 40 curriculums =====
    "A": [
        {
            # A1 — tone: bold_declaration
            "title": "Food & Dining (Gastronomie et Cuisine)",
            "description": (
                "French food vocabulary isn't just words — it's the key to an "
                "entire culture. From ordering at a brasserie to haggling at a "
                "marché, you'll walk into any French restaurant with confidence."
            ),
            "count": 6,
        },
        {
            # A2 — tone: vivid_scenario
            "title": "Transportation & Navigation (Transports et Navigation)",
            "description": (
                "Picture yourself at Gare du Nord, crowds rushing past — and you "
                "know exactly what to say to find your quai. That's the quiet "
                "power this series hands you."
            ),
            "count": 6,
        },
        {
            # A3 — tone: empathetic_observation
            "title": "Shopping & Services (Achats et Services)",
            "description": (
                "Ever wanted to ask for a different size, compare prices, or "
                "open a compte bancaire in French but didn't know where to "
                "start? This series was made for that exact moment."
            ),
            "count": 6,
        },
        {
            # A4 — tone: surprising_fact
            "title": "Social Life & Relationships (Vie Sociale et Relations)",
            "description": (
                "French has an entire grammar of politeness — tu versus vous "
                "can make or break a first impression. Master social French to "
                "truly connect rather than just get by."
            ),
            "count": 6,
        },
        {
            # A5 — tone: metaphor_led
            "title": "Health & Wellness (Santé et Bien-être)",
            "description": (
                "Your health is your second passport when living abroad. This "
                "series arms you with medical, fitness, and self-care French — "
                "vocabulary that opens every door at the pharmacie and cabinet."
            ),
            "count": 5,
        },
        {
            # A6 — tone: provocative_question
            "title": "Housing & Home Life (Logement et Vie Quotidienne)",
            "description": (
                "Could you rent an apartment, dispute a charges locatives bill, "
                "or register at the mairie entirely in French? If not, this "
                "series is the fastest path to yes."
            ),
            "count": 5,
        },
        {
            # A7 — tone: bold_declaration
            "title": "Travel & Exploration (Voyages et Découvertes)",
            "description": (
                "Real travel begins where guidebook French ends. Book a chambre, "
                "recover lost luggage, or join a randonnée — this series turns "
                "you into a traveler, not a tourist."
            ),
            "count": 6,
        },
    ],
    # ===== Collection B: Business & Career — 6 series, 34 curriculums =====
    "B": [
        {
            # B1 — tone: vivid_scenario
            "title": "Office Communication (Communication au Bureau)",
            "description": (
                "Imagine presenting to a boardroom of French colleagues — "
                "confident, clear, professional. This series takes you from "
                "first-day emails to polished presentations without a stumble."
            ),
            "count": 6,
        },
        {
            # B2 — tone: empathetic_observation
            "title": "Job Search & Career (Recherche d'Emploi et Carrière)",
            "description": (
                "Writing a CV in French is hard enough; interviewing is even "
                "harder. If you're chasing career opportunities in Francophone "
                "markets, this is the stepping stone you need."
            ),
            "count": 6,
        },
        {
            # B3 — tone: surprising_fact
            "title": "Industry Vocabulary (Vocabulaire Sectoriel)",
            "description": (
                "Every industry speaks its own French — from tech to hospitality, "
                "from luxury goods to global logistics. Nail the right terms and "
                "earn instant credibility."
            ),
            "count": 6,
        },
        {
            # B4 — tone: metaphor_led
            "title": "Business Operations (Gestion d'Entreprise)",
            "description": (
                "A business is a machine — project management is the gears, "
                "budgeting is the fuel, compliance is the brake. This series "
                "helps you run that machine fluently in French."
            ),
            "count": 6,
        },
        {
            # B5 — tone: provocative_question
            "title": "International Trade (Commerce International)",
            "description": (
                "Could you negotiate a million-euro contract in French? From "
                "Incoterms to cross-cultural etiquette, this series turns you "
                "into a formidable partner at the negotiation table."
            ),
            "count": 5,
        },
        {
            # B6 — tone: bold_declaration
            "title": "Entrepreneurship (Entrepreneuriat et Innovation)",
            "description": (
                "Paris, Lyon, and Brussels are powerhouses of Francophone "
                "startups. If you're founding, pitching, or joining an équipe "
                "fondatrice, French fluency is the edge you can't skip."
            ),
            "count": 5,
        },
    ],
    # ===== Collection C: Academic & Science — 5 series, 28 curriculums =====
    "C": [
        {
            # C1 — tone: empathetic_observation
            "title": "Science & Technology (Sciences et Technologie)",
            "description": (
                "Reading a scientific paper in French and feeling lost? You're "
                "not alone. This series builds your vocabulary from biology to "
                "computer science so you can engage with confidence."
            ),
            "count": 6,
        },
        {
            # C2 — tone: surprising_fact
            "title": "Economics & Finance (Économie et Finance)",
            "description": (
                "France is the world's seventh-largest economy, yet most "
                "learners skip financial vocabulary. From micro to macro, from "
                "la Bourse to the ECB — this series fills that gap."
            ),
            "count": 6,
        },
        {
            # C3 — tone: metaphor_led
            "title": "History & Politics (Histoire et Politique)",
            "description": (
                "History is the mirror; politics is the light cast upon it. "
                "This series helps you read, discuss, and debate the past and "
                "present of the Francophone world."
            ),
            "count": 6,
        },
        {
            # C4 — tone: provocative_question
            "title": "Psychology & Education (Psychologie et Éducation)",
            "description": (
                "Why do children learn languages faster than adults? Psychology "
                "and education research has answers — this series teaches you "
                "how to discuss them in French."
            ),
            "count": 5,
        },
        {
            # C5 — tone: bold_declaration
            "title": "Philosophy & Critical Thinking (Philosophie et Pensée Critique)",
            "description": (
                "French philosophy has shaped Western thought for centuries — "
                "from Descartes to Foucault to Derrida. Mastering philosophical "
                "vocabulary is the first step to joining the deepest debates."
            ),
            "count": 5,
        },
    ],
    # ===== Collection D: Culture & Society — 4 series, 20 curriculums =====
    "D": [
        {
            # D1 — tone: surprising_fact
            "title": "Arts & Literature (Arts et Littérature)",
            "description": (
                "French-speaking writers have won more Nobel Prizes in Literature "
                "than almost any other language group. This series opens the door "
                "to discussing art like a native speaker."
            ),
            "count": 5,
        },
        {
            # D2 — tone: metaphor_led
            "title": "Architecture & Design (Architecture et Design)",
            "description": (
                "Architecture is the silent language of a city. From Haussmann "
                "boulevards to Le Corbusier, this series teaches you to read "
                "and retell the story of the built world in French."
            ),
            "count": 5,
        },
        {
            # D3 — tone: provocative_question
            "title": "Media & Journalism (Médias et Journalisme)",
            "description": (
                "Can you follow a France 24 broadcast after the first ten "
                "seconds? This series walks you through the language of French "
                "news, debate, and digital media."
            ),
            "count": 5,
        },
        {
            # D4 — tone: bold_declaration
            "title": "Traditions & Festivals (Traditions et Fêtes)",
            "description": (
                "French festivals go far beyond Bastille Day — they are a living "
                "tapestry of regional culture. This series helps you describe "
                "every tradition, dish, and celebration in fluent French."
            ),
            "count": 5,
        },
    ],
    # ===== Collection E: Nature & Innovation — 3 series, 16 curriculums =====
    "E": [
        {
            # E1 — tone: metaphor_led
            "title": "Environment & Sustainability (Environnement et Durabilité)",
            "description": (
                "The Earth is our shared home, and French is a leading voice in "
                "the global green movement. From transition énergétique to "
                "zero-waste living — vocabulary for the future."
            ),
            "count": 6,
        },
        {
            # E2 — tone: provocative_question
            "title": "Digital Technology & AI (Technologie Numérique et IA)",
            "description": (
                "Can you explain artificial intelligence in French? From "
                "blockchain to machine learning, this series drops you into "
                "the hottest tech conversation in the Francophone world."
            ),
            "count": 5,
        },
        {
            # E3 — tone: bold_declaration
            "title": "Sports & Leisure (Sports et Loisirs)",
            "description": (
                "Sport is humanity's universal language — but commentating a "
                "Ligue 1 match in French is another league entirely. This "
                "series takes you from the stade to the salle de sport."
            ),
            "count": 5,
        },
    ],
}

# Verify planned total:
# A: 6+6+6+6+5+5+6 = 40
# B: 6+6+6+6+5+5   = 34
# C: 6+6+6+5+5     = 28
# D: 5+5+5+5        = 20
# E: 6+5+5          = 16
# Grand total = 40 + 34 + 28 + 20 + 16 = 138 ✓
#
# Planned level distribution across all 25 series (58 beg / 51 preint / 29 inter):
# The per-series level split is finalized in tasks 13.3–13.5 when the individual
# create_*.py scripts are written. Each series respects the max-1-level-gap
# rule (curriculum_series_level_gap view).

# Series counts per collection for iteration
SERIES_COUNTS = {"A": 7, "B": 6, "C": 5, "D": 4, "E": 3}


# ---------------------------------------------------------------------------
# Main execution
# ---------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("en-fr Orchestrator (bilingual-parity-expansion)")
    print("Creating collections and series")
    print("userLanguage=en (English), language=fr (French)")
    print("Target: 138 curriculums across 5 collections, 25 series")
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
    print("SUMMARY — en-fr Infrastructure (bilingual-parity-expansion)")
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

    print("\n✅ en-fr orchestrator (bilingual-parity-expansion) complete.")
    return collection_ids, series_ids


if __name__ == "__main__":
    main()
