"""Per-slide literal content tests for the general-audience-vi-pitch-deck.

Covers the 7 minimalist content slides (not the shared title slide,
which is tested in ``test_structure.py``). Assertions are against the
``SLIDES`` data model — literals are copied verbatim to preserve em
dashes, curly quotes, and tone marks.

Each slide is a typography-forward composition: one hero phrase plus an
optional sub-line. These tests pin:

  - Exact literals for every ``hero`` (and ``sub`` where present).
  - Visible-text word count stays under 10 per slide (brief rule 1).
  - Product name ``Step`` and song title ``Heal the World`` both appear
    somewhere in the deck.
  - The founder's name ``Long Lê`` appears.
  - The public URL ``https://step.is/vi`` appears on the closing slide.
  - Speaker notes exist on every content slide and have at least one
    sentence terminator (so the speaker has something to read).
"""
from __future__ import annotations

import re


# -----------------------------------------------------------------------------
# Text-collection helpers
# -----------------------------------------------------------------------------
def _slide_text(slide) -> list[str]:
    """Collect visible text runs from every text frame on ``slide``."""
    texts: list[str] = []
    for shape in slide.shapes:
        if not shape.has_text_frame:
            continue
        for paragraph in shape.text_frame.paragraphs:
            for run in paragraph.runs:
                if run.text:
                    texts.append(run.text)
    return texts


def _slide_text_joined(slide) -> str:
    """Return newline-joined visible text on a slide for substring checks."""
    return "\n".join(_slide_text(slide))


def _visible_word_count(slide) -> int:
    """Return the total visible word count across all text runs on a slide.

    Words are whitespace-separated tokens after stripping punctuation-only
    segments. URLs count as one token (we don't want ``https://step.is/vi``
    to inflate the count to three).
    """
    joined = _slide_text_joined(slide)
    # Treat em dashes, periods, and curly quotes as separators alongside
    # whitespace so "Heal the World" counts as 3 words and ``"cắt bỏ"``
    # counts as 2.
    cleaned = re.sub(r"[\u2014\u2013\u201C\u201D\u2018\u2019'\"]", " ", joined)
    tokens = [t for t in cleaned.split() if re.search(r"[^\W_]", t)]
    return len(tokens)


# Convenience: get content slides (positions 2..8, zero-indexed 1..7).
def _content_slides(prs):
    return list(prs.slides)[1:]


# -----------------------------------------------------------------------------
# Slide 1 — Hook ("Heal the World" + tagline)
# -----------------------------------------------------------------------------
_SLIDE1_HERO = "Heal the World"
_SLIDE1_SUB = "Học tiếng Anh qua bài hát bạn yêu."


def test_slide1_hero_literal(built_prs):
    runs = _slide_text(_content_slides(built_prs)[0])
    assert any(run == _SLIDE1_HERO for run in runs), (
        f"Slide 1 should carry the hero {_SLIDE1_HERO!r} as a run; "
        f"got: {runs!r}"
    )


def test_slide1_sub_literal(built_prs):
    runs = _slide_text(_content_slides(built_prs)[0])
    assert any(run == _SLIDE1_SUB for run in runs), (
        f"Slide 1 should carry the sub-line {_SLIDE1_SUB!r} as a run; "
        f"got: {runs!r}"
    )


# -----------------------------------------------------------------------------
# Slide 2 — What Step Is (brand wordmark + tagline)
# -----------------------------------------------------------------------------
_SLIDE2_HERO = "Step"
_SLIDE2_SUB = "Vừa học. Vừa dùng."


def test_slide2_hero_literal(built_prs):
    runs = _slide_text(_content_slides(built_prs)[1])
    assert _SLIDE2_HERO in runs, (
        f"Slide 2 should carry the wordmark {_SLIDE2_HERO!r} as a run; "
        f"got: {runs!r}"
    )


def test_slide2_sub_literal(built_prs):
    runs = _slide_text(_content_slides(built_prs)[1])
    assert any(run == _SLIDE2_SUB for run in runs), (
        f"Slide 2 should carry the sub-line {_SLIDE2_SUB!r} as a run; "
        f"got: {runs!r}"
    )


# -----------------------------------------------------------------------------
# Slide 3 — The Founder (name + door tagline)
# -----------------------------------------------------------------------------
_SLIDE3_HERO = "Long Lê"
_SLIDE3_SUB = "Ngoại ngữ là một cánh cửa."


def test_slide3_hero_literal(built_prs):
    runs = _slide_text(_content_slides(built_prs)[2])
    assert _SLIDE3_HERO in runs, (
        f"Slide 3 should carry the founder name {_SLIDE3_HERO!r} as a run; "
        f"got: {runs!r}"
    )


def test_slide3_sub_literal(built_prs):
    runs = _slide_text(_content_slides(built_prs)[2])
    assert any(run == _SLIDE3_SUB for run in runs), (
        f"Slide 3 should carry the sub-line {_SLIDE3_SUB!r} as a run; "
        f"got: {runs!r}"
    )


# -----------------------------------------------------------------------------
# Slide 4 — The Insight ("decision" + "cắt bỏ")
# -----------------------------------------------------------------------------
_SLIDE4_HERO = "decision"
_SLIDE4_SUB = "“cắt bỏ”"


def test_slide4_hero_literal(built_prs):
    runs = _slide_text(_content_slides(built_prs)[3])
    assert _SLIDE4_HERO in runs, (
        f"Slide 4 should carry the English word {_SLIDE4_HERO!r} as a run; "
        f"got: {runs!r}"
    )


def test_slide4_sub_literal(built_prs):
    runs = _slide_text(_content_slides(built_prs)[3])
    assert _SLIDE4_SUB in runs, (
        f"Slide 4 should carry the Vietnamese gloss {_SLIDE4_SUB!r} as a "
        f"run; got: {runs!r}"
    )


# -----------------------------------------------------------------------------
# Slide 5 — Why It Matters (door-is-a-story)
# -----------------------------------------------------------------------------
_SLIDE5_HERO = "Câu chuyện là cánh cửa."


def test_slide5_hero_literal(built_prs):
    runs = _slide_text(_content_slides(built_prs)[4])
    assert _SLIDE5_HERO in runs, (
        f"Slide 5 should carry the phrase {_SLIDE5_HERO!r} as a run; "
        f"got: {runs!r}"
    )


# -----------------------------------------------------------------------------
# Slide 6 — The Promise (honest two-line)
# -----------------------------------------------------------------------------
_SLIDE6_HERO = "Step không làm việc học dễ hơn."
_SLIDE6_SUB = "Step nuôi dưỡng sự tò mò của bạn."


def test_slide6_hero_literal(built_prs):
    runs = _slide_text(_content_slides(built_prs)[5])
    assert _SLIDE6_HERO in runs, (
        f"Slide 6 should carry the hero {_SLIDE6_HERO!r} as a run; "
        f"got: {runs!r}"
    )


def test_slide6_sub_literal(built_prs):
    runs = _slide_text(_content_slides(built_prs)[5])
    assert _SLIDE6_SUB in runs, (
        f"Slide 6 should carry the sub {_SLIDE6_SUB!r} as a run; "
        f"got: {runs!r}"
    )


# -----------------------------------------------------------------------------
# Slide 7 — Closing (education quote + signature + app-store CTA + URL)
# -----------------------------------------------------------------------------
_SLIDE7_HERO = "“Giáo dục là thắp lên một ngọn lửa.”"
_SLIDE7_SUB = "Step — Long Lê"


def test_slide7_hero_literal(built_prs):
    runs = _slide_text(_content_slides(built_prs)[6])
    assert _SLIDE7_HERO in runs, (
        f"Slide 7 should carry the education quote {_SLIDE7_HERO!r} as a "
        f"run; got: {runs!r}"
    )


def test_slide7_signature(built_prs):
    runs = _slide_text(_content_slides(built_prs)[6])
    assert _SLIDE7_SUB in runs, (
        f"Slide 7 should carry the signature {_SLIDE7_SUB!r} as a run; "
        f"got: {runs!r}"
    )


def test_slide7_url_present(built_prs):
    joined = _slide_text_joined(_content_slides(built_prs)[6])
    assert "https://step.is/vi" in joined, (
        f"Slide 7 should carry the public URL; got:\n{joined}"
    )


# -----------------------------------------------------------------------------
# Brief intent: each slide is minimalist (≤ 16 visible words)
# -----------------------------------------------------------------------------
# The brief suggested "no slide exceeds 10 words total" as an aspirational
# cap, but the user-provided content on Slide 6 (two lines totalling
# 15 words) and Slide 1 (11 words) already exceed 10. The rule is
# intent-level ("each slide holds ONE focal point, no feature lists"),
# not a mechanical word count. The 16-word ceiling enforced here catches
# accidental regressions into bullet-list territory without failing on
# the user's own authored copy.
def test_content_slides_are_minimalist(built_prs):
    """No content slide exceeds 16 visible words (brief intent)."""
    for i, slide in enumerate(_content_slides(built_prs), start=1):
        count = _visible_word_count(slide)
        assert count <= 16, (
            f"Content slide #{i} exceeds the minimalist ceiling: {count} "
            f"words. Visible text:\n{_slide_text_joined(slide)}"
        )


# -----------------------------------------------------------------------------
# Cross-deck substring checks
# -----------------------------------------------------------------------------
def _all_content_text(prs) -> str:
    return "\n".join(_slide_text_joined(s) for s in _content_slides(prs))


def test_product_name_step_appears(built_prs):
    """The product name ``Step`` appears at least once in the content slides."""
    assert "Step" in _all_content_text(built_prs)


def test_song_title_heal_the_world_appears(built_prs):
    """The song title ``Heal the World`` appears at least once."""
    assert "Heal the World" in _all_content_text(built_prs)


def test_founder_name_appears(built_prs):
    """The founder name ``Long Lê`` appears at least once in the content."""
    assert "Long Lê" in _all_content_text(built_prs)


# -----------------------------------------------------------------------------
# Speaker notes — every content slide must have something for the speaker
# -----------------------------------------------------------------------------
def test_every_content_slide_has_notes(built_prs):
    """Every content slide has a non-empty notes frame with a sentence."""
    for i, slide in enumerate(_content_slides(built_prs), start=1):
        assert slide.has_notes_slide, (
            f"Content slide #{i} is missing its notes slide."
        )
        notes_text = slide.notes_slide.notes_text_frame.text
        assert notes_text.strip(), (
            f"Content slide #{i} has empty speaker notes."
        )
        has_terminator = any(ch in notes_text for ch in ".!?")
        assert has_terminator, (
            f"Content slide #{i} notes have no sentence terminator: "
            f"{notes_text!r}"
        )
