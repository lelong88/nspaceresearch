"""
Tone pre-assignment utility for multilingual curriculum expansion.

Assigns description tones (6-tone palette) and farewell tones (5-tone palette)
to all curriculums, series, and collections for a language pair, enforcing:
  - No two adjacent curriculums in a series share the same description tone
  - No two adjacent curriculums in a series share the same farewell tone
  - No two adjacent series in a collection share the same description tone
  - No single tone exceeds 30% of descriptions per language pair

Requirements: 8.1–8.7
"""

DESCRIPTION_TONES = [
    "provocative_question",
    "bold_declaration",
    "vivid_scenario",
    "empathetic_observation",
    "surprising_fact",
    "metaphor_led",
]

FAREWELL_TONES = [
    "introspective_guide",
    "warm_accountability",
    "team_building_energy",
    "quiet_awe",
    "practical_momentum",
]


def _assign_no_adjacent(palette, count, start_offset=0):
    """Assign tones from *palette* to *count* slots so no two adjacent are equal.

    Uses round-robin with an offset to spread usage evenly.  Returns a list of
    length *count*.
    """
    n = len(palette)
    result = []
    idx = start_offset % n
    for _ in range(count):
        result.append(palette[idx])
        idx = (idx + 1) % n
    return result


def _rebalance_descriptions(assignments, max_fraction=0.30):
    """Check and rebalance description tone assignments so no tone exceeds
    *max_fraction* of the total.

    *assignments* is the full flat list of description tones (curriculums +
    series + collections).  Mutates the list in-place and returns it.

    Strategy: identify over-represented tones, then swap excess occurrences
    with under-represented tones while preserving the no-adjacent constraint.
    """
    total = len(assignments)
    if total == 0:
        return assignments

    cap = int(total * max_fraction)
    # Allow at least 1 per tone to avoid impossible constraints on tiny inputs
    cap = max(cap, 1)

    from collections import Counter
    counts = Counter(assignments)

    over = {t for t, c in counts.items() if c > cap}
    if not over:
        return assignments

    under = [t for t in DESCRIPTION_TONES if counts.get(t, 0) < cap]

    for i in range(len(assignments)):
        if assignments[i] not in over:
            continue
        if counts[assignments[i]] <= cap:
            continue
        # Try to swap with an under-represented tone that doesn't violate adjacency
        prev_tone = assignments[i - 1] if i > 0 else None
        next_tone = assignments[i + 1] if i < len(assignments) - 1 else None
        for replacement in under:
            if replacement != prev_tone and replacement != next_tone:
                old = assignments[i]
                assignments[i] = replacement
                counts[old] -= 1
                counts[replacement] = counts.get(replacement, 0) + 1
                if counts[old] <= cap:
                    over.discard(old)
                if counts[replacement] >= cap:
                    under = [t for t in under if t != replacement]
                break

    return assignments


def assign_tones_for_language_pair(num_collections, series_per_collection, curriculums_per_series):
    """Assign description and farewell tones for an entire language pair.

    Parameters
    ----------
    num_collections : int
        Number of collections in this language pair.
    series_per_collection : int
        Number of series per collection (uniform).
    curriculums_per_series : int
        Number of curriculums per series (uniform).

    Returns
    -------
    dict with keys:
        "collections" : list of dicts, one per collection
            Each has:
                "collection_index": int
                "description_tone": str
                "series": list of dicts, one per series
                    Each has:
                        "series_index": int
                        "description_tone": str
                        "curriculums": list of dicts, one per curriculum
                            Each has:
                                "curriculum_index": int
                                "description_tone": str
                                "farewell_tone": str
    """
    total_series = num_collections * series_per_collection
    total_curriculums = total_series * curriculums_per_series

    # --- Step 1: assign collection description tones (rotate through palette) ---
    collection_tones = _assign_no_adjacent(DESCRIPTION_TONES, num_collections, start_offset=0)

    # --- Step 2: assign series description tones per collection ---
    # Offset each collection's series rotation so adjacent series across
    # collections also tend to differ.
    series_tones_flat = []
    series_offset = 0
    for c_idx in range(num_collections):
        # Start from a different palette position than the collection's own tone
        col_tone_idx = DESCRIPTION_TONES.index(collection_tones[c_idx])
        offset = (col_tone_idx + 1) % len(DESCRIPTION_TONES)
        tones = _assign_no_adjacent(DESCRIPTION_TONES, series_per_collection, start_offset=offset)
        series_tones_flat.extend(tones)
        series_offset += series_per_collection

    # --- Step 3: assign curriculum description tones per series ---
    curriculum_desc_tones_flat = []
    cur_offset = 0
    for s_idx in range(total_series):
        series_tone_idx = DESCRIPTION_TONES.index(series_tones_flat[s_idx])
        offset = (series_tone_idx + 1) % len(DESCRIPTION_TONES)
        tones = _assign_no_adjacent(DESCRIPTION_TONES, curriculums_per_series, start_offset=offset)
        curriculum_desc_tones_flat.extend(tones)
        cur_offset += curriculums_per_series

    # --- Step 4: assign farewell tones per series (no adjacent repeats) ---
    farewell_tones_flat = []
    for s_idx in range(total_series):
        offset = s_idx % len(FAREWELL_TONES)
        tones = _assign_no_adjacent(FAREWELL_TONES, curriculums_per_series, start_offset=offset)
        farewell_tones_flat.extend(tones)

    # --- Step 5: rebalance description tones for the 30% cap ---
    # Collect ALL description tones (collections + series + curriculums) into
    # one flat list, rebalance, then redistribute.
    all_desc = list(collection_tones) + list(series_tones_flat) + list(curriculum_desc_tones_flat)
    _rebalance_descriptions(all_desc, max_fraction=0.30)

    # Redistribute back
    collection_tones = all_desc[:num_collections]
    series_tones_flat = all_desc[num_collections:num_collections + total_series]
    curriculum_desc_tones_flat = all_desc[num_collections + total_series:]

    # --- Step 6: build output structure ---
    result = {"collections": []}
    cur_flat_idx = 0
    ser_flat_idx = 0

    for c_idx in range(num_collections):
        collection_entry = {
            "collection_index": c_idx,
            "description_tone": collection_tones[c_idx],
            "series": [],
        }
        for s_local in range(series_per_collection):
            series_entry = {
                "series_index": s_local,
                "description_tone": series_tones_flat[ser_flat_idx],
                "curriculums": [],
            }
            for cur_local in range(curriculums_per_series):
                fw_idx = ser_flat_idx * curriculums_per_series + cur_local
                series_entry["curriculums"].append({
                    "curriculum_index": cur_local,
                    "description_tone": curriculum_desc_tones_flat[cur_flat_idx],
                    "farewell_tone": farewell_tones_flat[fw_idx],
                })
                cur_flat_idx += 1
            collection_entry["series"].append(series_entry)
            ser_flat_idx += 1
        result["collections"].append(collection_entry)

    return result
