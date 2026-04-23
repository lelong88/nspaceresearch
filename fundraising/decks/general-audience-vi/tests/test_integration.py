"""Integration tests for the general-audience-vi-pitch-deck generator.

These tests cover the end-to-end path from title-slide open → content
build → serialization → R2 upload, with R2 network calls stubbed so the
suite runs offline. They verify:

  - ``main()`` opens the shared Vietnamese title slide, appends 7
    content slides, and uploads the merged 8-slide deck to R2.
  - Both uploaded bodies reopen as a valid 8-slide ``Presentation``.
  - The ``<name>.pptx`` latest alias is overwritten on every run while
    the timestamped snapshot key is new each time.
  - ``main()`` prints the public ``slides.nspace.is`` URL on stdout.
  - The generator completes in under 30 seconds.
  - No ``.pptx`` is written to local disk.

The R2 client is stubbed at the ``assets._r2_client`` seam so no real
network traffic leaves the test machine. The vendored-asset byte helpers
are stubbed via the module-scoped autouse fixture in ``conftest.py``.
"""
from __future__ import annotations

import io
import time
from pathlib import Path

import pytest
from pptx import Presentation


_DECK_DIR = Path(__file__).resolve().parent.parent


class _FakeR2:
    """In-memory stub for the R2 boto3 client.

    Captures every ``put_object`` call so tests can inspect bucket, key,
    body bytes, and content type without touching the network.
    """

    def __init__(self) -> None:
        self.calls: list[dict] = []

    def put_object(self, *, Bucket: str, Key: str, Body: bytes, ContentType: str):
        self.calls.append(
            {
                "bucket": Bucket,
                "key": Key,
                "body": Body,
                "content_type": ContentType,
            }
        )
        return {"ETag": '"stub"'}


@pytest.fixture
def stubbed_r2(monkeypatch):
    """Stub the R2 client seam so ``main()`` uploads go in-memory only."""
    import assets

    fake = _FakeR2()
    monkeypatch.setattr(assets, "_r2_client", lambda: fake)
    return fake


# -----------------------------------------------------------------------------
# Tests
# -----------------------------------------------------------------------------
def test_main_uploads_merged_deck(generator, stubbed_r2, capsys):
    """``main()`` uploads a merged 8-slide deck (title + 7 content)."""
    generator.main()

    assert len(stubbed_r2.calls) == 2, (
        f"Expected 2 R2 uploads (snapshot + latest); got "
        f"{len(stubbed_r2.calls)}: {[c['key'] for c in stubbed_r2.calls]}"
    )

    buckets = {call["bucket"] for call in stubbed_r2.calls}
    assert buckets == {"step-pitch-decks"}, (
        f"Uploads must target ``step-pitch-decks``; got {buckets!r}."
    )

    keys = [call["key"] for call in stubbed_r2.calls]
    assert any(k == "step-pitch-vi.pptx" for k in keys), (
        f"Expected the ``.../latest`` alias key; got {keys!r}"
    )
    assert any(
        k.startswith("step-pitch-vi-") and k.endswith(".pptx") for k in keys
    ), f"Expected a timestamped snapshot key; got {keys!r}"

    # Both bodies must be valid 8-slide .pptx files.
    for call in stubbed_r2.calls:
        prs = Presentation(io.BytesIO(call["body"]))
        assert len(prs.slides) == 8, (
            f"Uploaded body under key {call['key']!r} has "
            f"{len(prs.slides)} slides (expected 8 = 1 title + 7 content)."
        )

    out = capsys.readouterr().out
    assert "https://slides.nspace.is/" in out, (
        f"Expected public URL on stdout; got:\n{out}"
    )


def test_main_overwrites_latest_alias(generator, stubbed_r2):
    """Repeated ``main()`` runs overwrite the same ``step-pitch-vi.pptx`` key."""
    generator.main()
    generator.main()

    latest_calls = [c for c in stubbed_r2.calls if c["key"] == "step-pitch-vi.pptx"]
    assert len(latest_calls) == 2, (
        f"Expected 2 writes to the latest alias across 2 main() "
        f"invocations; got {len(latest_calls)}."
    )


def test_main_does_not_write_local_pptx(generator, stubbed_r2):
    """``main()`` MUST NOT write a ``.pptx`` to local disk."""
    before = {p for p in _DECK_DIR.rglob("*.pptx")}
    generator.main()
    after = {p for p in _DECK_DIR.rglob("*.pptx")}
    new_pptx = after - before
    assert not new_pptx, (
        f"main() wrote .pptx files to local disk (should upload to R2 "
        f"only): {sorted(new_pptx)!r}"
    )


def test_merged_build_completes_within_30s(generator, stubbed_r2):
    """Opening the title slide + building 7 content slides finishes quickly."""
    import assets

    start = time.monotonic()
    prs = assets.open_title_slide_presentation(language=generator.DECK_LANGUAGE)
    generator.build(prs)
    buf = io.BytesIO()
    prs.save(buf)
    duration_s = time.monotonic() - start

    assert duration_s < 30.0, (
        f"Building the merged deck took {duration_s:.2f}s, exceeding "
        f"the 30s budget."
    )
    assert buf.getvalue(), "Expected non-empty .pptx bytes."
