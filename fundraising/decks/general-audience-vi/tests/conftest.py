"""Pytest fixtures for the general-audience-vi-pitch-deck deck tests.

Exposes three module-scoped fixtures and one autouse stub:
  - ``generator``: the loaded ``generate_deck`` module.
  - ``_stub_assets`` (autouse): replaces the vendored-asset byte helpers
    with a tiny placeholder PNG so the test suite runs fast and doesn't
    require the ``vendor_assets/`` files to be present on a CI checkout.
  - ``built_prs``: the merged ``Presentation`` with the title slide
    prepended and all 7 content slides appended (no disk I/O).
  - ``built_pptx_bytes``: serialized ``.pptx`` bytes for the merged deck.
"""
from __future__ import annotations

import importlib.util
import io
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

# Resolve the generator module path relative to this conftest.py
_DECK_DIR = Path(__file__).resolve().parent.parent
_GENERATOR_PATH = _DECK_DIR / "generate_deck.py"

# Smallest valid PNG: 1×1 fully transparent pixel. Used as a placeholder
# for vendored assets during tests so builds stay offline and fast.
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
def _stub_assets(generator):
    """Auto-stub the vendored-asset byte helpers for every test module.

    The real ``assets.hero_image_png`` / ``appstore_badge_png`` /
    ``playstore_badge_png`` functions read from files under
    ``vendor_assets/``. Tests don't care about the actual bytes — they
    care about deck structure, text content, and upload semantics. This
    fixture replaces each helper with a tiny valid PNG so slide builds
    stay fast and don't depend on vendored files being present on CI.

    ``render_logo_png`` is not stubbed because it reads directly from
    the workspace-root SVG (always present) and caches to disk.
    """
    import assets

    with (
        patch.object(assets, "hero_image_png", return_value=_TINY_PNG),
        patch.object(assets, "appstore_badge_png", return_value=_TINY_PNG),
        patch.object(assets, "playstore_badge_png", return_value=_TINY_PNG),
    ):
        yield


@pytest.fixture(scope="module")
def built_prs(generator):
    """Build the merged deck in memory (title slide + 7 content slides).

    Mirrors what ``main()`` does, minus the upload step. Returns the
    ``Presentation`` with 8 slides total.
    """
    import assets

    prs = assets.open_title_slide_presentation(language=generator.DECK_LANGUAGE)
    generator.build(prs)
    return prs


@pytest.fixture
def built_pptx_bytes(built_prs):
    """Serialize the merged deck to ``.pptx`` bytes for round-trip tests."""
    buf = io.BytesIO()
    built_prs.save(buf)
    return buf.getvalue()
