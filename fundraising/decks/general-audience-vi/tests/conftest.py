"""Pytest fixtures for the general-audience-vi-pitch-deck deck tests.

Exposes three module-scoped fixtures and one autouse stub:
  - ``generator``: the loaded ``generate_deck`` module.
  - ``_stub_illustrations`` (autouse): replaces Vertex image helpers with a
    tiny placeholder PNG so the test suite runs offline and fast.
  - ``built_prs``: a ``Presentation`` with all 7 slides built (no disk I/O).
  - ``built_pptx_bytes``: serialized ``.pptx`` bytes for the built deck.
"""
from __future__ import annotations

import importlib.util
import io
import sys
from pathlib import Path
from unittest.mock import patch

import pytest
from pptx import Presentation
from pptx.util import Inches

# Resolve the generator module path relative to this conftest.py
_DECK_DIR = Path(__file__).resolve().parent.parent
_GENERATOR_PATH = _DECK_DIR / "generate_deck.py"

# Smallest valid PNG: 1×1 fully transparent pixel. Used as a placeholder
# for Vertex-generated illustrations during tests so no network calls are
# made and build time stays sub-second.
_TINY_PNG = bytes.fromhex(
    "89504e470d0a1a0a0000000d49484452000000010000000108060000001f15c489"
    "0000000d49444154789c6300010000000500010d0a2db40000000049454e44ae426082"
)


def _load_generator():
    """Load ``generate_deck.py`` as an importable module named ``generate_deck``.

    The generator lives outside any regular Python package, so we load it
    via ``importlib.util.spec_from_file_location`` and register the result
    in ``sys.modules`` so subsequent imports see the same module object.
    """
    deck_dir_str = str(_DECK_DIR)
    if deck_dir_str not in sys.path:
        sys.path.insert(0, deck_dir_str)

    spec = importlib.util.spec_from_file_location(
        "generate_deck", _GENERATOR_PATH
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules["generate_deck"] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def generator():
    """Load the ``generate_deck`` module once per test module."""
    return _load_generator()


@pytest.fixture(scope="module", autouse=True)
def _stub_illustrations(generator):
    """Auto-stub Vertex illustration helpers for every test module.

    The real ``assets.slide_*_illustration`` helpers call Vertex Gemini
    on cache miss, which costs time and money. Tests don't care about
    actual artwork — they care about deck structure, text content, and
    upload semantics. This fixture replaces each illustration helper
    with a tiny valid PNG so slide builds stay fast and offline.
    """
    import assets  # lazy import so the generator fixture can add to sys.path

    with (
        patch.object(assets, "slide_1_illustration", return_value=_TINY_PNG),
        patch.object(assets, "slide_4_illustration", return_value=_TINY_PNG),
        patch.object(assets, "slide_7_illustration", return_value=_TINY_PNG),
    ):
        yield


@pytest.fixture(scope="module")
def built_prs(generator):
    """Build all 7 slides onto a fresh ``Presentation`` without disk I/O.

    Mirrors what ``main()`` does, minus the upload step, so tests can
    inspect the in-memory ``Presentation`` directly.
    """
    prs = Presentation()
    prs.slide_width = Inches(generator.SLIDE_WIDTH_IN)
    prs.slide_height = Inches(generator.SLIDE_HEIGHT_IN)
    generator.build(prs)
    return prs


@pytest.fixture
def built_pptx_bytes(generator):
    """Build the deck fully in memory and return the serialized ``.pptx`` bytes.

    Mirrors ``main()`` without performing any network I/O (R2 upload): it
    builds the 7 slides, serializes the result to a ``BytesIO`` buffer, and
    returns ``buffer.getvalue()``.
    """
    prs = Presentation()
    prs.slide_width = Inches(generator.SLIDE_WIDTH_IN)
    prs.slide_height = Inches(generator.SLIDE_HEIGHT_IN)
    generator.build(prs)

    buf = io.BytesIO()
    prs.save(buf)
    return buf.getvalue()
