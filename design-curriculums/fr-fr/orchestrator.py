"""
fr-fr orchestrator — Creates 2 collections, 6 series, wires them together,
and sets display orders for the French-French (single-language) pair.

All titles and descriptions are in French.
Vocabulary targets formal/literary French registers (soutenu, littéraire).
Upper-intermediate to advanced level.

Tone assignments are pre-computed via tone_assigner.assign_tones_for_language_pair(2, 3, 5).
Series descriptions are short persuasive French hooks (≤255 chars) using the assigned tone.
Collection descriptions are short informative French summaries (not persuasive copy).
"""

import sys
import logging

sys.path.insert(0, "/home/ubuntu/nspaceresearch2/design-curriculums")
sys.path.insert(0, "/home/ubuntu/nspaceresearch2/design-curriculums/fr-fr")
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
# Collection definitions — French titles, informative summaries
# ---------------------------------------------------------------------------
COLLECTIONS = [
    {
        "title": "Littérature et Culture Avancée",
        "description": (
            "Analyse littéraire, philosophie, histoire intellectuelle et critique culturelle. "
            "Chaque série approfondit un domaine du patrimoine culturel francophone, "
            "avec un vocabulaire issu des registres soutenu et littéraire."
        ),
    },
    {
        "title": "Maîtrise Professionnelle",
        "description": (
            "Droit des affaires, innovation scientifique, médias et discours public. "
            "Chaque série développe la maîtrise du français professionnel avancé, "
            "du vocabulaire juridique à la rhétorique journalistique."
        ),
    },
]

# ---------------------------------------------------------------------------
# Series definitions — 3 per collection, French titles
# Descriptions: short persuasive hooks ≤255 chars using assigned tone
# ---------------------------------------------------------------------------
SERIES = {
    # ===== Collection E: Littérature et Culture Avancée =====
    "E": [
        {
            # E1 — Analyse Littéraire
            "title": "Analyse Littéraire",
            "description": (
                "Pourquoi certains romans vous hantent des années après la dernière page ? "
                "Maîtrisez les techniques narratives, les formes poétiques et les procédés rhétoriques "
                "qui font la grandeur de la littérature française."
            ),
        },
        {
            # E2 — Philosophie et Histoire Intellectuelle
            "title": "Philosophie et Histoire Intellectuelle",
            "description": (
                "De Voltaire à Sartre, la pensée française a redessiné les frontières du possible. "
                "Plongez dans les Lumières, l'existentialisme et les débats contemporains "
                "avec le vocabulaire qui donne accès aux textes originaux."
            ),
        },
        {
            # E3 — Art, Cinéma et Critique Culturelle
            "title": "Art, Cinéma et Critique Culturelle",
            "description": (
                "Imaginez-vous devant une toile de Delacroix ou un film de Godard, "
                "capable d'articuler exactement ce que vous ressentez. "
                "Cette série vous donne les mots de la critique culturelle."
            ),
        },
    ],
    # ===== Collection F: Maîtrise Professionnelle =====
    "F": [
        {
            # F1 — Droit et Affaires Avancés
            "title": "Droit et Affaires Avancés",
            "description": (
                "Le droit des sociétés, l'analyse financière, le management stratégique : "
                "autant de domaines où la précision du vocabulaire fait la différence "
                "entre un professionnel compétent et un expert reconnu."
            ),
        },
        {
            # F2 — Science et Innovation
            "title": "Science et Innovation",
            "description": (
                "L'intelligence artificielle transforme déjà la médecine, le climat et la recherche. "
                "Acquérez le vocabulaire scientifique avancé pour comprendre — et participer — "
                "aux débats qui façonnent notre avenir."
            ),
        },
        {
            # F3 — Médias, Journalisme et Discours Public
            "title": "Médias, Journalisme et Discours Public",
            "description": (
                "Saviez-vous que la rhétorique d'un éditorial peut renverser l'opinion publique ? "
                "Du journalisme d'investigation à la prise de parole, "
                "maîtrisez l'art du discours en français."
            ),
        },
    ],
}


# ---------------------------------------------------------------------------
# Main execution
# ---------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("fr-fr Orchestrator — Creating collections and series")
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
    print("SUMMARY — fr-fr Infrastructure")
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

    print("\n✅ fr-fr orchestrator complete.")
    return collection_ids, series_ids


if __name__ == "__main__":
    main()
