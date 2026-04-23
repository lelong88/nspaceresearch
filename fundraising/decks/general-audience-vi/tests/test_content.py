"""Per-slide literal content tests for the general-audience-vi-pitch-deck.

Example-based assertions that pin the Vietnamese copy produced by
``generate_deck.py`` against the requirements document. Each test reaches
into the built ``Presentation`` via the ``built_prs`` fixture and checks
either an exact run-text match or a substring appearance in the joined
slide text.

Validates:
  - 2.2, 2.3, 2.4: product name ``Step`` and song title ``Heal the World``
    appear; Core_Message tagline is verbatim.
  - 4.1, 4.3: Slide 1 headline literal and at most one supporting line.
  - 5.1, 5.2, 5.3: Slide 2 title literal, ≤ 3 body bullets, three-idea
    keyword coverage.
  - 6.1, 6.3: Slide 3 reframe pair literal and content-type noun coverage.
  - 7.1, 7.2, 7.3: Slide 4 Heal-the-World title, five activity rows with
    keyword coverage, closing sentence literal.
  - 8.1, 8.2, 8.3: Slide 5 worldview, heal/cure motif, emphasis literal.
  - 9.1: Slide 6 four differentiator cells with label + body per cell and
    per-cell keyword coverage.
  - 10.1, 10.2, 10.3, 10.4: Slide 7 headline, sub-text, brand + URL + next
    step line.

Note on literals: every "exact" string below is copied verbatim from
``SLIDES`` in ``generate_deck.py`` to avoid smart-quote/dash mismatches
(e.g., the em dash ``—`` vs a hyphen-minus ``-``).
"""
from __future__ import annotations


# -----------------------------------------------------------------------------
# Text-collection helpers
# -----------------------------------------------------------------------------
def _slide_text(slide) -> list[str]:
    """Collect visible text runs from every text frame on ``slide``.

    Notes are deliberately excluded — this returns only text that is
    visible on the slide itself.
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


def _slide_text_joined(slide) -> str:
    """Return the newline-joined visible text on a slide for substring checks."""
    return "\n".join(_slide_text(slide))


def _all_text(prs) -> str:
    """Return the newline-joined visible text across every slide in the deck."""
    return "\n".join(_slide_text_joined(s) for s in prs.slides)


def _slide_text_frames(slide):
    """Iterate text-frame-bearing shapes on the slide."""
    return [shape for shape in slide.shapes if shape.has_text_frame]


# -----------------------------------------------------------------------------
# Slide 1 — Hook
# -----------------------------------------------------------------------------
# Copied verbatim from SLIDES[0]["title"] to preserve em dash and quote style.
_SLIDE1_HEADLINE = (
    "Bạn đã học tiếng Anh nhiều năm — nhưng vẫn chưa thực sự 'chạm' vào nó?"
)


def test_slide1_headline_literal(built_prs):
    """Slide 1 carries the exact hook headline (Req 4.1)."""
    runs = _slide_text(built_prs.slides[0])
    assert any(run == _SLIDE1_HEADLINE for run in runs), (
        f"Slide 1 should contain the headline {_SLIDE1_HEADLINE!r} as a run. "
        f"Got runs: {runs!r}"
    )


def test_slide1_supporting_line_cap(built_prs):
    """Slide 1 body has at most one supporting text line beyond the headline (Req 4.3)."""
    slide = built_prs.slides[0]
    supporting_frames = 0
    for shape in _slide_text_frames(slide):
        frame_text = shape.text_frame.text
        if not frame_text.strip():
            continue
        if frame_text == _SLIDE1_HEADLINE:
            continue
        supporting_frames += 1
    assert supporting_frames <= 1, (
        f"Slide 1 should have at most one supporting line beyond the "
        f"headline; found {supporting_frames}."
    )


# -----------------------------------------------------------------------------
# Slide 2 — Why Traditional Methods Fail
# -----------------------------------------------------------------------------
_SLIDE2_TITLE = "Vì sao cách học cũ không còn đủ?"


def test_slide2_title_literal(built_prs):
    """Slide 2 carries the literal framing title (Req 5.1)."""
    runs = _slide_text(built_prs.slides[1])
    assert any(run == _SLIDE2_TITLE for run in runs), (
        f"Slide 2 should contain the title {_SLIDE2_TITLE!r} as a run. "
        f"Got runs: {runs!r}"
    )


def test_slide2_bullet_count_max_3(built_prs):
    """Slide 2 has exactly 3 body bullet text frames (Req 5.2)."""
    slide = built_prs.slides[1]
    body_frames = 0
    for shape in _slide_text_frames(slide):
        frame_text = shape.text_frame.text
        if not frame_text.strip():
            continue
        if frame_text == _SLIDE2_TITLE:
            continue
        body_frames += 1
    assert body_frames == 3, (
        f"Slide 2 should have exactly 3 body bullet text frames; "
        f"found {body_frames}."
    )


def test_slide2_three_ideas_covered(built_prs):
    """Slide 2 body covers the three ideas from Req 5.3.

    Disconnect from loved content, irrelevant vocabulary topics, and
    motivation fading are each signalled by at least one keyword.
    """
    joined = _slide_text_joined(built_prs.slides[1])

    disconnect_keywords = ("truyền thống", "tách")
    irrelevant_keywords = ("sân bay", "thời tiết", "sở thích")
    motivation_keywords = ("động lực", "nghĩa vụ")

    assert any(k in joined for k in disconnect_keywords), (
        f"Slide 2 should mention the disconnect from loved content "
        f"(one of {disconnect_keywords!r}); got:\n{joined}"
    )
    assert any(k in joined for k in irrelevant_keywords), (
        f"Slide 2 should mention irrelevant vocabulary topics "
        f"(one of {irrelevant_keywords!r}); got:\n{joined}"
    )
    assert any(k in joined for k in motivation_keywords), (
        f"Slide 2 should mention motivation fading / chore "
        f"(one of {motivation_keywords!r}); got:\n{joined}"
    )


# -----------------------------------------------------------------------------
# Slide 3 — Introducing Step
# -----------------------------------------------------------------------------
_SLIDE3_REFRAME_OLD = "Phương pháp nào để học tiếng Anh?"
_SLIDE3_REFRAME_NEW = "Nội dung nào bạn muốn sống cùng trong tiếng Anh?"
_SLIDE3_TAGLINE = "Step — Học ngoại ngữ qua những điều bạn thực sự yêu thích."


def test_slide3_reframe_pair(built_prs):
    """Slide 3 shows both reframe questions (Req 6.1)."""
    joined = _slide_text_joined(built_prs.slides[2])
    assert _SLIDE3_REFRAME_OLD in joined, (
        f"Slide 3 should contain the old reframe question "
        f"{_SLIDE3_REFRAME_OLD!r}; got:\n{joined}"
    )
    assert _SLIDE3_REFRAME_NEW in joined, (
        f"Slide 3 should contain the new reframe question "
        f"{_SLIDE3_REFRAME_NEW!r}; got:\n{joined}"
    )


def test_slide3_tagline_verbatim(built_prs):
    """Slide 3 renders the Core_Message tagline verbatim (Req 2.4, 6.2)."""
    runs = _slide_text(built_prs.slides[2])
    assert any(run == _SLIDE3_TAGLINE for run in runs), (
        f"Slide 3 should contain the tagline {_SLIDE3_TAGLINE!r} as an "
        f"exact run. Got runs: {runs!r}"
    )


def test_slide3_content_type_nouns(built_prs):
    """Slide 3 explanation lists every content-type noun (Req 6.3)."""
    joined = _slide_text_joined(built_prs.slides[2])
    expected_nouns = ("bài hát", "tiểu thuyết", "truyện tranh", "podcast", "phim")
    missing = [noun for noun in expected_nouns if noun not in joined]
    assert not missing, (
        f"Slide 3 should mention every content type; missing {missing!r} "
        f"in:\n{joined}"
    )


# -----------------------------------------------------------------------------
# Slide 4 — Heal the World
# -----------------------------------------------------------------------------
_SLIDE4_CLOSING = (
    "Bạn không chỉ học tiếng Anh — bạn đang sống cùng bài hát mình yêu."
)


def test_slide4_heal_world_title(built_prs):
    """Slide 4 title frames the ``Heal the World`` song (Req 7.1, 2.3)."""
    joined = _slide_text_joined(built_prs.slides[3])
    assert "Heal the World" in joined, (
        f"Slide 4 should reference the song literal ``Heal the World``; "
        f"got:\n{joined}"
    )


def test_slide4_five_activities(built_prs):
    """Slide 4 shows five activity rows with the expected per-row keywords (Req 7.2).

    Each keyword uniquely identifies one of the five activities: reading
    lyrics, listening/pronunciation, cultural exploration, flashcards, and
    writing to restate the song. Matching is case-insensitive because
    Vietnamese activity sentences start with capitalized words (e.g.,
    ``Nghe...``, ``Viết...``).
    """
    activity_keywords = ("lời", "nghe", "văn hóa", "flashcards", "viết")
    frame_texts = [
        shape.text_frame.text.lower()
        for shape in _slide_text_frames(built_prs.slides[3])
        if shape.text_frame.text.strip()
    ]

    matches = 0
    for keyword in activity_keywords:
        if any(keyword in text for text in frame_texts):
            matches += 1
    assert matches == 5, (
        f"Slide 4 should contain five activity rows covering "
        f"{activity_keywords!r}; matched {matches} of 5."
    )


def test_slide4_closing_literal(built_prs):
    """Slide 4 ends with the exact closing sentence (Req 7.3)."""
    runs = _slide_text(built_prs.slides[3])
    assert any(run == _SLIDE4_CLOSING for run in runs), (
        f"Slide 4 should contain the closing sentence {_SLIDE4_CLOSING!r} "
        f"as a run. Got runs: {runs!r}"
    )


# -----------------------------------------------------------------------------
# Slide 5 — Why This Works
# -----------------------------------------------------------------------------
_SLIDE5_EMPHASIS = "Mỗi ngôn ngữ mới là một phiên bản mới của chính bạn."


def test_slide5_worldview_statement(built_prs):
    """Slide 5 body contains the ``thế giới quan`` (worldview) phrase (Req 8.1)."""
    joined = _slide_text_joined(built_prs.slides[4])
    assert "thế giới quan" in joined, (
        f"Slide 5 should contain the worldview phrase 'thế giới quan'; "
        f"got:\n{joined}"
    )


def test_slide5_heal_cure_motif(built_prs):
    """Slide 5 contrasts ``heal`` with ``cure`` (Req 8.2)."""
    joined_lower = _slide_text_joined(built_prs.slides[4]).lower()
    assert "heal" in joined_lower, (
        "Slide 5 should reference the word 'heal' (case-insensitive) "
        "as part of the heal-vs-cure contrast."
    )
    assert "cure" in joined_lower, (
        "Slide 5 should reference the word 'cure' (case-insensitive) "
        "as part of the heal-vs-cure contrast."
    )


def test_slide5_emphasis_literal(built_prs):
    """Slide 5 carries the exact emphasis one-liner (Req 8.3)."""
    runs = _slide_text(built_prs.slides[4])
    assert any(run == _SLIDE5_EMPHASIS for run in runs), (
        f"Slide 5 should contain the emphasis line {_SLIDE5_EMPHASIS!r} "
        f"as a run. Got runs: {runs!r}"
    )


# -----------------------------------------------------------------------------
# Slide 6 — What Makes Step Different
# -----------------------------------------------------------------------------
def test_slide6_four_differentiators(built_prs, generator):
    """Slide 6 renders all 4 cell labels and bodies (Req 9.1).

    Each of the 4 cells defined in ``SLIDES[5]["body"]`` contributes a
    ``label`` and a ``text`` string; both strings must appear on the slide.
    """
    cells = generator.SLIDES[5]["body"]
    assert len(cells) == 4, (
        f"Sanity check: Slide 6 data should define exactly 4 cells; "
        f"got {len(cells)}."
    )

    runs = _slide_text(built_prs.slides[5])
    for cell in cells:
        assert cell["label"] in runs, (
            f"Slide 6 should contain the cell label {cell['label']!r} as "
            f"an exact run. Got runs: {runs!r}"
        )
        assert cell["text"] in runs, (
            f"Slide 6 should contain the cell body {cell['text']!r} as an "
            f"exact run. Got runs: {runs!r}"
        )


def test_slide6_per_cell_keyword_coverage(built_prs, generator):
    """Slide 6 covers the 4 differentiator themes via per-cell keywords.

    Cell 1: AI + level-adaptation (độ khó or trình độ).
    Cell 2: diverse content types.
    Cell 3: deep connection keyword.
    Cell 4: rejection of empty gamification (Req 9.1).
    """
    cells = generator.SLIDES[5]["body"]
    assert len(cells) == 4

    def _cell_text(i: int) -> str:
        return f"{cells[i]['label']} {cells[i]['text']}"

    cell1 = _cell_text(0)
    assert "AI" in cell1, f"Cell 1 should mention 'AI'; got: {cell1!r}"
    assert ("độ khó" in cell1) or ("trình độ" in cell1), (
        f"Cell 1 should mention level adaptation ('độ khó' or 'trình độ'); "
        f"got: {cell1!r}"
    )

    cell2 = _cell_text(1)
    cell2_keywords = ("Bài hát", "tiểu thuyết", "podcast")
    assert any(k in cell2 for k in cell2_keywords), (
        f"Cell 2 should mention at least one content type "
        f"(one of {cell2_keywords!r}); got: {cell2!r}"
    )

    cell3 = _cell_text(2)
    cell3_keywords = ("kết nối", "Kết nối", "gắn")
    assert any(k in cell3 for k in cell3_keywords), (
        f"Cell 3 should mention deep connection "
        f"(one of {cell3_keywords!r}); got: {cell3!r}"
    )

    cell4 = _cell_text(3)
    cell4_keywords = ("gamification", "điểm số ảo", "streak")
    assert any(k in cell4 for k in cell4_keywords), (
        f"Cell 4 should reject empty gamification "
        f"(one of {cell4_keywords!r}); got: {cell4!r}"
    )


# -----------------------------------------------------------------------------
# Slide 7 — Call to Action
# -----------------------------------------------------------------------------
_SLIDE7_HEADLINE = "Bắt đầu với bài hát, cuốn sách, bộ phim bạn yêu nhất."
_SLIDE7_SUBTEXT = (
    "Ngôn ngữ không phải là môn học. Nó là cánh cửa vào một thế giới mới "
    "— và một phiên bản mới của chính bạn."
)


def test_slide7_headline_literal(built_prs):
    """Slide 7 carries the exact invitation headline (Req 10.1)."""
    runs = _slide_text(built_prs.slides[6])
    assert any(run == _SLIDE7_HEADLINE for run in runs), (
        f"Slide 7 should contain the headline {_SLIDE7_HEADLINE!r} as a "
        f"run. Got runs: {runs!r}"
    )


def test_slide7_subtext_literal(built_prs):
    """Slide 7 carries the exact sub-text (Req 10.2)."""
    runs = _slide_text(built_prs.slides[6])
    assert any(run == _SLIDE7_SUBTEXT for run in runs), (
        f"Slide 7 should contain the sub-text {_SLIDE7_SUBTEXT!r} as a "
        f"run. Got runs: {runs!r}"
    )


def test_slide7_brand_and_url_and_next_step(built_prs):
    """Slide 7 renders brand, public URL, and next-step line (Req 10.3, 10.4)."""
    slide = built_prs.slides[6]
    runs = _slide_text(slide)
    joined = _slide_text_joined(slide)

    # Brand mark ``Step`` appears as its own run on the slide.
    assert "Step" in runs, (
        f"Slide 7 should render the brand ``Step`` as a run; got: {runs!r}"
    )

    # Public URL replaces the earlier QR placeholder; must appear verbatim.
    assert "https://step.is/vi" in joined, (
        f"Slide 7 should render the public URL ``https://step.is/vi``; "
        f"got:\n{joined}"
    )

    # Next-step line must cover at least one of the download / sign-up /
    # learn-more verbs.
    next_step_keywords = ("tải", "Đăng ký", "tìm hiểu")
    assert any(k in joined for k in next_step_keywords), (
        f"Slide 7 should include a next-step line covering one of "
        f"{next_step_keywords!r}; got:\n{joined}"
    )


# -----------------------------------------------------------------------------
# Cross-deck substring checks (Req 2.2, 2.3)
# -----------------------------------------------------------------------------
def test_product_name_step_appears(built_prs):
    """The product name ``Step`` appears at least once across the deck (Req 2.2)."""
    assert "Step" in _all_text(built_prs), (
        "The literal product name ``Step`` should appear at least once "
        "across the deck."
    )


def test_song_title_heal_the_world_appears(built_prs):
    """The song title ``Heal the World`` appears at least once (Req 2.3)."""
    assert "Heal the World" in _all_text(built_prs), (
        "The literal song title ``Heal the World`` should appear at least "
        "once across the deck."
    )
