"""Structural tests for the general-audience-vi-pitch-deck.

Validates Requirements 1.1, 1.2, and 1.3:
  - 1.1: The deck contains exactly 7 slides.
  - 1.2: Slide order matches the fixed narrative sequence (Hook → Gap → Intro
         → Heal-the-World → Why it works → Differentiators → CTA), verified
         against the `SLIDES` data module (source of truth for titles).
  - 1.3: Slide size is 16:9 widescreen (13.333 in × 7.5 in).

Design note on Slide 3 title verification:
    The deck data model stores a `title` for every slide, but the Slide 3
    builder intentionally does not render the ``title`` field on the slide
    (only the reframe question pair, accent tagline, and explanation are
    rendered). To still pin the Slide 3 ordering against the narrative, this
    module falls back to checking for ``body[0]`` (the reframe question) or
    the ``emphasis`` tagline, both of which are rendered by the Slide 3
    builder and both uniquely identify Slide 3 in the deck.
"""
from __future__ import annotations

import pytest


# -----------------------------------------------------------------------------
# Slide geometry tolerance
# -----------------------------------------------------------------------------
# ``Inches(13.333)`` does not round-trip exactly through EMU, so compare with
# a small tolerance instead of asserting strict equality.
_DIM_TOLERANCE_IN = 0.01


def _slide_text(slide) -> list[str]:
    """Collect visible text strings from every text frame on ``slide``.

    Iterates shapes that expose a ``text_frame`` and gathers non-empty run
    text. Notes are deliberately excluded — this function returns only text
    that is visible on the slide itself.
    """
    texts: list[str] = []
    for shape in slide.shapes:
        if not shape.has_text_frame:
            continue
        for paragraph in shape.text_frame.paragraphs:
            for run in paragraph.runs:
                if run.text:
                    texts.append(run.text)
    return texts


# -----------------------------------------------------------------------------
# Requirement 1.1 — exactly 7 slides
# -----------------------------------------------------------------------------
def test_slide_count(built_prs):
    """The built deck contains exactly 7 slides (Requirement 1.1)."""
    assert len(built_prs.slides) == 7


# -----------------------------------------------------------------------------
# Requirement 1.3 — 16:9 widescreen at 13.333 in × 7.5 in
# -----------------------------------------------------------------------------
def test_slide_dimensions(built_prs):
    """Slide width and height match the 16:9 spec within EMU tolerance (Req 1.3)."""
    assert abs(built_prs.slide_width.inches - 13.333) < _DIM_TOLERANCE_IN
    assert abs(built_prs.slide_height.inches - 7.5) < _DIM_TOLERANCE_IN


# -----------------------------------------------------------------------------
# Requirement 1.2 — slide order matches the 7-step narrative
# -----------------------------------------------------------------------------
def test_slide_order_matches_narrative(built_prs, generator):
    """Each built slide carries the expected narrative marker in order (Req 1.2).

    For slides 1, 2, 4, 5, 6, 7 the marker is ``SLIDES[i]["title"]`` (the
    title as authored in the data model). For slide 3 the marker falls back
    to the reframe question (``body[0]``) or the tagline emphasis because the
    Slide 3 builder intentionally does not render the ``title`` field.
    """
    slides_data = generator.SLIDES
    assert len(slides_data) == 7, (
        "Sanity check: SLIDES must contain 7 entries to validate ordering."
    )

    rendered_slides = list(built_prs.slides)
    assert len(rendered_slides) == 7

    for i, (slide, content) in enumerate(zip(rendered_slides, slides_data)):
        texts = _slide_text(slide)
        joined = "\n".join(texts)

        if i == 2:
            # Slide 3 exception: title is not rendered on the slide; look for
            # the reframe question or the tagline emphasis instead.
            reframe_question = content["body"][0]
            tagline = content["emphasis"]
            found = any(
                (reframe_question and reframe_question in t)
                or (tagline and tagline in t)
                for t in texts
            ) or (
                (reframe_question and reframe_question in joined)
                or (tagline and tagline in joined)
            )
            assert found, (
                f"Slide {i + 1} (index {i}) should carry the reframe question "
                f"or tagline. Got text runs: {texts!r}"
            )
        else:
            expected_title = content["title"]
            assert expected_title, (
                f"SLIDES[{i}]['title'] must be a non-empty string to anchor "
                f"ordering for slide {i + 1}."
            )
            found = any(expected_title in t for t in texts) or (
                expected_title in joined
            )
            assert found, (
                f"Slide {i + 1} (index {i}) should carry the narrative title "
                f"{expected_title!r}. Got text runs: {texts!r}"
            )
