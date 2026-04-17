"""
Property-based tests for tone_assigner.py

# Feature: multilingual-curriculum-expansion
# Properties 10, 11, 12: Tone palette validity, adjacency constraint, distribution cap

**Validates: Requirements 8.1, 8.2, 8.3, 8.4, 8.5, 8.6**
"""

from hypothesis import given, settings
from hypothesis import strategies as st

from tone_assigner import (
    DESCRIPTION_TONES,
    FAREWELL_TONES,
    assign_tones_for_language_pair,
)

# Valid tone sets for quick membership checks
VALID_DESCRIPTION_TONES = set(DESCRIPTION_TONES)
VALID_FAREWELL_TONES = set(FAREWELL_TONES)

# ---------------------------------------------------------------------------
# Shared strategy: random language-pair configuration
# ---------------------------------------------------------------------------
config_strategy = st.fixed_dictionaries({
    "num_collections": st.integers(min_value=1, max_value=6),
    "series_per_collection": st.integers(min_value=1, max_value=8),
    "curriculums_per_series": st.integers(min_value=2, max_value=10),
})


# ---------------------------------------------------------------------------
# Helper: flatten all tones from the assignment result
# ---------------------------------------------------------------------------

def _collect_all_tones(result):
    """Return lists of all description tones and farewell tones from the result."""
    desc_tones = []
    farewell_tones = []
    for coll in result["collections"]:
        desc_tones.append(coll["description_tone"])
        for series in coll["series"]:
            desc_tones.append(series["description_tone"])
            for cur in series["curriculums"]:
                desc_tones.append(cur["description_tone"])
                farewell_tones.append(cur["farewell_tone"])
    return desc_tones, farewell_tones


# ===========================================================================
# Property 10: Tone palette validity
# Feature: multilingual-curriculum-expansion, Property 10: Tone palette validity
# ===========================================================================


@given(cfg=config_strategy)
@settings(max_examples=100)
def test_tone_palette_validity(cfg):
    """Every description tone must be one of the 6 valid Tone_Palette types and
    every farewell tone must be one of the 5 valid Farewell_Palette registers.

    **Validates: Requirements 8.1, 8.5**
    """
    result = assign_tones_for_language_pair(
        num_collections=cfg["num_collections"],
        series_per_collection=cfg["series_per_collection"],
        curriculums_per_series=cfg["curriculums_per_series"],
    )

    desc_tones, farewell_tones = _collect_all_tones(result)

    for tone in desc_tones:
        assert tone in VALID_DESCRIPTION_TONES, (
            f"Invalid description tone '{tone}'; "
            f"expected one of {VALID_DESCRIPTION_TONES}"
        )

    for tone in farewell_tones:
        assert tone in VALID_FAREWELL_TONES, (
            f"Invalid farewell tone '{tone}'; "
            f"expected one of {VALID_FAREWELL_TONES}"
        )


# ===========================================================================
# Property 11: Tone adjacency constraint
# Feature: multilingual-curriculum-expansion, Property 11: Tone adjacency constraint
# ===========================================================================


@given(cfg=config_strategy)
@settings(max_examples=100)
def test_tone_adjacency_constraint(cfg):
    """No two adjacent curriculums in a series share the same description tone
    or farewell tone, and no two adjacent series in a collection share the same
    description tone.

    **Validates: Requirements 8.2, 8.3, 8.6**
    """
    result = assign_tones_for_language_pair(
        num_collections=cfg["num_collections"],
        series_per_collection=cfg["series_per_collection"],
        curriculums_per_series=cfg["curriculums_per_series"],
    )

    for coll in result["collections"]:
        # --- Adjacent series description tones within a collection ---
        series_desc_tones = [s["description_tone"] for s in coll["series"]]
        for i in range(len(series_desc_tones) - 1):
            assert series_desc_tones[i] != series_desc_tones[i + 1], (
                f"Adjacent series {i} and {i+1} in collection "
                f"{coll['collection_index']} share description tone "
                f"'{series_desc_tones[i]}'"
            )

        # --- Adjacent curriculum tones within each series ---
        for series in coll["series"]:
            cur_desc = [c["description_tone"] for c in series["curriculums"]]
            cur_fare = [c["farewell_tone"] for c in series["curriculums"]]

            for i in range(len(cur_desc) - 1):
                assert cur_desc[i] != cur_desc[i + 1], (
                    f"Adjacent curriculums {i} and {i+1} in series "
                    f"{series['series_index']} share description tone "
                    f"'{cur_desc[i]}'"
                )
                assert cur_fare[i] != cur_fare[i + 1], (
                    f"Adjacent curriculums {i} and {i+1} in series "
                    f"{series['series_index']} share farewell tone "
                    f"'{cur_fare[i]}'"
                )


# ===========================================================================
# Property 12: Tone distribution cap
# Feature: multilingual-curriculum-expansion, Property 12: Tone distribution cap
# ===========================================================================


@given(cfg=config_strategy)
@settings(max_examples=100)
def test_tone_distribution_cap(cfg):
    """No single Tone_Palette type exceeds 30% of the total description tone
    assignments within a language pair.

    **Validates: Requirements 8.4**
    """
    result = assign_tones_for_language_pair(
        num_collections=cfg["num_collections"],
        series_per_collection=cfg["series_per_collection"],
        curriculums_per_series=cfg["curriculums_per_series"],
    )

    desc_tones, _ = _collect_all_tones(result)
    total = len(desc_tones)

    if total == 0:
        return  # nothing to check

    from collections import Counter
    counts = Counter(desc_tones)

    for tone, count in counts.items():
        fraction = count / total
        assert fraction <= 0.30, (
            f"Description tone '{tone}' accounts for {count}/{total} "
            f"({fraction:.1%}) of assignments, exceeding the 30% cap"
        )
