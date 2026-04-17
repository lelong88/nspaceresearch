"""
de-de orchestrator — Creates 2 collections, 6 series, wires them together,
and sets display orders for the German-German (single-language) pair.

All titles and descriptions are in German.
Vocabulary targets formal/academic German registers (Bildungssprache, Fachsprache).
Upper-intermediate to advanced level.

Tone assignments are pre-computed via tone_assigner.assign_tones_for_language_pair(2, 3, 5).
Series descriptions are short persuasive German hooks (≤255 chars) using the assigned tone.
Collection descriptions are short informative German summaries (not persuasive copy).
"""

import sys
import logging

sys.path.insert(0, "/home/ubuntu/nspaceresearch2/design-curriculums")
sys.path.insert(0, "/home/ubuntu/nspaceresearch2/design-curriculums/de-de")
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
# Tone assignments from tone_assigner.assign_tones_for_language_pair(2, 3, 5)
# ---------------------------------------------------------------------------
tones = tone_assigner.assign_tones_for_language_pair(2, 3, 5)

# Collection 0 (E): description_tone = tones["collections"][0]["description_tone"]
#   Series E1: tones["collections"][0]["series"][0]["description_tone"]
#   Series E2: tones["collections"][0]["series"][1]["description_tone"]
#   Series E3: tones["collections"][0]["series"][2]["description_tone"]
#
# Collection 1 (F): description_tone = tones["collections"][1]["description_tone"]
#   Series F1: tones["collections"][1]["series"][0]["description_tone"]
#   Series F2: tones["collections"][1]["series"][1]["description_tone"]
#   Series F3: tones["collections"][1]["series"][2]["description_tone"]

# ---------------------------------------------------------------------------
# Collection definitions — German titles, informative summaries
# ---------------------------------------------------------------------------
COLLECTIONS = [
    {
        "title": "Literatur und Fortgeschrittene Kultur",
        "description": (
            "Literarische Analyse, Philosophie, Geistesgeschichte und Kulturkritik. "
            "Jede Serie vertieft einen Bereich des deutschsprachigen Kulturerbes "
            "mit Vokabular aus Bildungssprache und gehobener Fachsprache."
        ),
    },
    {
        "title": "Professionelle Meisterschaft",
        "description": (
            "Wirtschaftsrecht, wissenschaftliche Innovation, Medien und öffentlicher Diskurs. "
            "Jede Serie entwickelt die Beherrschung des fortgeschrittenen Fachdeutsch — "
            "von juristischer Terminologie bis zur journalistischen Rhetorik."
        ),
    },
]

# ---------------------------------------------------------------------------
# Series definitions — 3 per collection, German titles
# Descriptions: short persuasive hooks ≤255 chars using assigned tone
# ---------------------------------------------------------------------------
SERIES = {
    # ===== Collection E: Literatur und Fortgeschrittene Kultur =====
    "E": [
        {
            # E1 — Literarische Analyse
            "title": "Literarische Analyse",
            "description": (
                "Warum verfolgen manche Romane Sie noch Jahre nach der letzten Seite? "
                "Meistern Sie Erzähltechniken, poetische Formen und rhetorische Mittel, "
                "die große deutschsprachige Literatur ausmachen."
            ),
        },
        {
            # E2 — Philosophie und Geistesgeschichte
            "title": "Philosophie und Geistesgeschichte",
            "description": (
                "Von Kant bis Habermas hat deutsches Denken die Grenzen des Möglichen neu gezogen. "
                "Tauchen Sie ein in Aufklärung, Existenzialismus und aktuelle Debatten "
                "mit dem Vokabular der Originaltexte."
            ),
        },
        {
            # E3 — Kunst, Film und Kulturkritik
            "title": "Kunst, Film und Kulturkritik",
            "description": (
                "Stellen Sie sich vor einem Gemälde von Richter oder einem Film von Wenders vor — "
                "und können genau artikulieren, was Sie empfinden. "
                "Diese Serie gibt Ihnen die Sprache der Kulturkritik."
            ),
        },
    ],
    # ===== Collection F: Professionelle Meisterschaft =====
    "F": [
        {
            # F1 — Fortgeschrittenes Wirtschaftsrecht
            "title": "Fortgeschrittenes Wirtschaftsrecht",
            "description": (
                "Gesellschaftsrecht, Finanzanalyse, strategisches Management: "
                "In diesen Bereichen macht die Präzision des Vokabulars den Unterschied "
                "zwischen Kompetenz und anerkannter Expertise."
            ),
        },
        {
            # F2 — Wissenschaft und Innovation
            "title": "Wissenschaft und Innovation",
            "description": (
                "Künstliche Intelligenz verändert bereits Medizin, Klimaforschung und Wissenschaft. "
                "Erwerben Sie das fortgeschrittene Fachvokabular, um die Debatten zu verstehen — "
                "und mitzugestalten."
            ),
        },
        {
            # F3 — Medien, Journalismus und öffentlicher Diskurs
            "title": "Medien, Journalismus und öffentlicher Diskurs",
            "description": (
                "Wussten Sie, dass die Rhetorik eines Leitartikels die öffentliche Meinung kippen kann? "
                "Vom investigativen Journalismus bis zur Redekunst — "
                "meistern Sie die Kunst des Diskurses auf Deutsch."
            ),
        },
    ],
}


# ---------------------------------------------------------------------------
# Main execution
# ---------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("de-de Orchestrator — Creating collections and series")
    print("=" * 60)

    collection_keys = ["E", "F"]
    collection_ids = {}
    series_ids = {}  # keyed by e.g. "E1", "F3"

    # --- Step 1: Create collections ---
    print("\n--- Creating 2 collections ---")
    for i, col_def in enumerate(COLLECTIONS):
        col_id = create_collection(col_def["title"], col_def["description"])
        col_key = collection_keys[i]
        collection_ids[col_key] = col_id
        col_tone = tones["collections"][i]["description_tone"]
        print(f"  Collection {col_key}: {col_id}  (tone: {col_tone})")
        print(f"    Title: {col_def['title']}")

    # --- Step 2: Create series ---
    print("\n--- Creating 6 series ---")
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
        for j in range(3):
            ser_label = f"{col_key}{j + 1}"
            ser_id = series_ids[ser_label]
            add_series_to_collection(col_id, ser_id)
            print(f"  Wired {ser_label} ({ser_id}) -> Collection {col_key} ({col_id})")

    # --- Step 4: Set collection display orders (1-2) ---
    print("\n--- Setting collection display orders ---")
    for i, col_key in enumerate(collection_keys):
        col_id = collection_ids[col_key]
        order = i + 1
        set_collection_display_order(col_id, order)
        print(f"  Collection {col_key} ({col_id}) -> displayOrder {order}")

    # --- Step 5: Set series display orders (1-3 within each collection) ---
    print("\n--- Setting series display orders ---")
    for col_key in collection_keys:
        for j in range(3):
            ser_label = f"{col_key}{j + 1}"
            ser_id = series_ids[ser_label]
            order = j + 1
            set_series_display_order(ser_id, order)
            print(f"  Series {ser_label} ({ser_id}) -> displayOrder {order}")

    # --- Summary ---
    print("\n" + "=" * 60)
    print("SUMMARY — de-de Infrastructure")
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

    print("\n✅ de-de orchestrator complete.")
    return collection_ids, series_ids


if __name__ == "__main__":
    main()
