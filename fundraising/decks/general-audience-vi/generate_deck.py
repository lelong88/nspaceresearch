"""Generate the Vietnamese-language pitch deck for the product Step.

This script produces a 7-slide `.pptx` file at
``decks/general-audience-vi/step-pitch-vi.pptx`` using the ``python-pptx``
library. The deck targets a general (non-technical) audience at a
technology exhibition.

Dependency
----------
- ``python-pptx`` (tested against 1.0.x). Install with::

    pip install python-pptx

How to run
----------
From the workspace root::

    python decks/general-audience-vi/generate_deck.py

The script builds the deck entirely in memory, uploads the resulting
``.pptx`` to the Cloudflare R2 bucket ``step-pitch-decks`` via the
``assets`` module, and prints the public URL on ``slides.nspace.is``.
It does NOT write the ``.pptx`` to local disk. Illustrations are generated
via Vertex Gemini on first run and cached under
``decks/general-audience-vi/.asset_cache/`` for subsequent runs.
All Vietnamese strings are UTF-8 literals in source; no external content
files are read.
"""

import io
import sys
from datetime import datetime, timezone
from pathlib import Path

from lxml import etree
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Inches, Pt

# Ensure the deck directory is on sys.path so the ``assets`` sibling module
# can be imported directly whether this file is run as a script or imported
# by the test suite.
_DECK_DIR = Path(__file__).resolve().parent
if str(_DECK_DIR) not in sys.path:
    sys.path.insert(0, str(_DECK_DIR))

# ---------------------------------------------------------------------------
# Palette (RGB hex). See design.md for the rationale behind each color.
# ---------------------------------------------------------------------------
ACCENT = RGBColor(0x0F, 0x5F, 0x5C)  # deep teal
BG = RGBColor(0xFA, 0xF7, 0xF2)  # warm neutral background
BODY = RGBColor(0x2B, 0x2B, 0x2B)  # near-black body text
MUTED = RGBColor(0x6B, 0x6B, 0x6B)  # secondary text
ON_ACCENT = RGBColor(0xFA, 0xF7, 0xF2)  # text on accent fills

# Toggle for emoji glyphs inside icon circles. If False, icon helpers
# substitute short ASCII letters (A, B, C, ...) instead of unicode glyphs.
USE_GLYPH_EMOJI = True

# ---------------------------------------------------------------------------
# Typography
# ---------------------------------------------------------------------------
HEADLINE_FONT = "Inter"
BODY_FONT = "Inter"
FALLBACK_FONT = "Calibri"

# Font sizes (points)
SIZE_TITLE_XL = 54  # slide 1 hook, slide 7 CTA headline
SIZE_TITLE_L = 44  # slides 2, 3, 5, 6
SIZE_TITLE_M = 40  # slide 4 (content-heavy slide; keep titles compact)
SIZE_TAGLINE = 32  # emphasized taglines on slide 3, slide 5
SIZE_BODY_L = 24  # primary body
SIZE_BODY_M = 20  # secondary body / bullets
SIZE_BODY_S = 18  # meta/footnote (e.g., CTA next-step line)

# ---------------------------------------------------------------------------
# Slide geometry (inches). Origin is top-left.
# ---------------------------------------------------------------------------
SLIDE_WIDTH_IN = 13.333
SLIDE_HEIGHT_IN = 7.5
MARGIN_IN = 0.6  # >= 0.5 required by the design; 0.6 gives breathing room

# ---------------------------------------------------------------------------
# Output: R2 object key template
# ---------------------------------------------------------------------------
# No local .pptx is written. Deck bytes are uploaded to R2 bucket
# ``step-pitch-decks`` and served via the ``slides.nspace.is`` CDN domain.
# Objects live at the bucket root (no per-feature prefix) per the deck
# pipeline steering rule, so the shareable URL is just
# ``https://slides.nspace.is/<name>.pptx``. Each run writes two keys: a
# timestamped snapshot (immutable) and a ``<name>.pptx`` alias that
# overwrites on every run.
_R2_KEY_TEMPLATE = "step-pitch-vi-{stamp}.pptx"
_R2_KEY_LATEST = "step-pitch-vi.pptx"

# ---------------------------------------------------------------------------
# Slide content (data model)
#
# ``SLIDES`` is the single source of truth for every piece of Vietnamese text
# that appears in the 7 content slides. The brief calls for a minimalist,
# typography-forward deck: each slide carries a single phrase or image and
# the speaker delivers the narrative. Ten-word-per-slide ceiling, no
# bullets, one focal point per slide.
#
# Keys:
#   - ``index``     : 1..7 slide number.
#   - ``hero``      : the large centered phrase on the slide.
#   - ``sub``       : optional small line beneath ``hero``.
#   - ``notes``     : 2–3 sentence Vietnamese speaker notes.
# ---------------------------------------------------------------------------
SLIDES: list[dict] = [
    {
        "index": 1,
        "hero": "Heal the World",
        "sub": "Học tiếng Anh qua bài hát bạn yêu.",
        "notes": (
            "Hãy bắt đầu bằng một bài hát quen thuộc. "
            "Học tiếng Anh qua Heal the World là học qua chính điều bạn đã yêu. "
            "Ngôn ngữ không còn là môn học — nó trở thành một phần của bài hát."
        ),
    },
    {
        "index": 2,
        "hero": "Step",
        "sub": "Vừa học. Vừa dùng.",
        "notes": (
            "Step là nơi bạn học ngoại ngữ theo cách mới. "
            "Không mày mò nhiều năm rồi mới hi vọng dùng được — bạn vừa học vừa dùng ngay từ ngày đầu. "
            "Mỗi buổi học chỉ 5–10 phút, đủ để bạn bước vào nội dung bạn yêu."
        ),
    },
    {
        "index": 3,
        "hero": "Long Lê",
        "sub": "Ngoại ngữ là một cánh cửa.",
        "notes": (
            "Tôi tên là Long Lê. Tôi xây Step vì với tôi, ngoại ngữ không chỉ là một công cụ. "
            "Nó là cánh cửa ẩn giấu những câu chuyện và kiến thức sâu sắc. "
            "Nếu ai đó dịch sẵn cho tôi, tôi sẽ không bao giờ được nhìn thấy điều phía sau cánh cửa đó."
        ),
    },
    {
        "index": 4,
        "hero": "decision",
        "sub": "“cắt bỏ”",
        "notes": (
            "Một ví dụ: từ 'decision' gốc Latin, nghĩa đen là 'cắt bỏ'. "
            "Người ta chỉ thực sự quyết định khi sẵn sàng đánh mất một điều gì đó quan trọng. "
            "Bên trong chữ 'decision' là lòng can đảm, sự chịu đựng mất mát, và cảm xúc."
        ),
    },
    {
        "index": 5,
        "hero": "Câu chuyện là cánh cửa.",
        "sub": None,
        "notes": (
            "Nếu ai đó dịch từ 'decision' sang tiếng Việt cho tôi, tôi sẽ đánh mất câu chuyện. "
            "Câu chuyện chính là cánh cửa bước sang một thế giới quan khác — và đó là lý do tôi học ngoại ngữ."
        ),
    },
    {
        "index": 6,
        "hero": "Step không làm việc học dễ hơn.",
        "sub": "Step nuôi dưỡng sự tò mò của bạn.",
        "notes": (
            "Tôi không hứa Step làm việc học dễ dàng. "
            "Trong thời đại AI, học vẫn là một quá trình đầy khó khăn, cần nhiều nỗ lực và sự tự vận động. "
            "Điều Step hứa là luôn nuôi dưỡng sự tò mò và động lực tự thân — nền tảng cho tiến bộ lâu dài."
        ),
    },
    {
        "index": 7,
        "hero": "“Giáo dục là thắp lên một ngọn lửa.”",
        "sub": "Step — Long Lê",
        "notes": (
            "Câu nói tôi yêu thích trong giáo dục: giáo dục không phải là đổ đầy một cái bình, mà là thắp lên một ngọn lửa. "
            "Tôi hi vọng Step trở thành một phần của ngọn lửa đó bên trong bạn. "
            "Ghé https://step.is/vi để bắt đầu."
        ),
    },
]


# ---------------------------------------------------------------------------
# Helper functions
#
# Each helper mutates the given ``slide`` object in place and returns
# ``None``. Geometry is expressed in inches and converted via ``Inches(...)``.
# ---------------------------------------------------------------------------
def add_bg(slide, color: RGBColor) -> None:
    """Paint the full slide rectangle with the given solid fill color.

    Draws a full-bleed rectangle at (0, 0) covering the entire slide area
    (``SLIDE_WIDTH_IN`` x ``SLIDE_HEIGHT_IN``). The rectangle has no stroke
    so the fill reads as a clean background.
    """
    shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(0),
        Inches(0),
        Inches(SLIDE_WIDTH_IN),
        Inches(SLIDE_HEIGHT_IN),
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()


def add_accent_bar(
    slide,
    *,
    left_in: float,
    top_in: float,
    width_in: float = 0.1,
    height_in: float = 1.2,
    color: RGBColor = ACCENT,
) -> None:
    """Draw a thin decorative accent rectangle at the given inch-geometry.

    Used as a visual anchor next to titles (vertical bar) or above them
    (horizontal bar). The rectangle is filled with ``color`` (default:
    the module-level ``ACCENT``) and has no stroke.
    """
    shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(left_in),
        Inches(top_in),
        Inches(width_in),
        Inches(height_in),
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()


# ---------------------------------------------------------------------------
# Text helpers
# ---------------------------------------------------------------------------
_ALIGN_MAP: dict[str, PP_ALIGN] = {
    "left": PP_ALIGN.LEFT,
    "center": PP_ALIGN.CENTER,
    "right": PP_ALIGN.RIGHT,
}

_ANCHOR_MAP: dict[str, MSO_ANCHOR] = {
    "top": MSO_ANCHOR.TOP,
    "middle": MSO_ANCHOR.MIDDLE,
    "bottom": MSO_ANCHOR.BOTTOM,
}


def _set_bullet(paragraph) -> None:
    """Enable a simple '•' bullet on the given paragraph via its pPr XML.

    ``python-pptx`` does not expose bullet formatting on the Python API, so we
    manipulate the underlying ``a:pPr`` element directly: appending an
    ``<a:buChar char="•"/>`` child marks the paragraph as bulleted with the
    given character. A matching ``<a:buFont typeface="Arial"/>`` keeps the
    glyph stable across renderers that otherwise fall back to a theme bullet.
    """
    pPr = paragraph._p.get_or_add_pPr()

    # Remove any pre-existing bullet children to avoid duplicates when the
    # helper is invoked twice on the same paragraph.
    for tag in ("a:buChar", "a:buAutoNum", "a:buNone", "a:buFont"):
        for existing in pPr.findall(qn(tag)):
            pPr.remove(existing)

    buFont = etree.SubElement(pPr, qn("a:buFont"))
    buFont.set("typeface", "Arial")
    buChar = etree.SubElement(pPr, qn("a:buChar"))
    buChar.set("char", "•")


def _apply_run_formatting(
    run,
    *,
    font_size: int,
    font_color: RGBColor,
    font_name: str,
    bold: bool,
    italic: bool,
) -> None:
    """Apply font formatting to a single run."""
    run.font.name = font_name
    run.font.size = Pt(font_size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = font_color


def add_paragraph(
    text_frame,
    text: str,
    *,
    font_size: int,
    font_color: RGBColor = BODY,
    font_name: str = BODY_FONT,
    bold: bool = False,
    italic: bool = False,
    align: str = "left",
    bullet: bool = False,
    space_before_pt: int = 0,
    space_after_pt: int = 6,
) -> None:
    """Append a paragraph to an existing text frame with explicit formatting.

    The paragraph is added via ``text_frame.add_paragraph()`` and populated
    with a single run carrying ``text``. Font name, size, color, weight, and
    italic styling are applied to that run; alignment, bullet flag, and
    before/after spacing are applied to the paragraph itself.
    """
    paragraph = text_frame.add_paragraph()
    paragraph.alignment = _ALIGN_MAP[align]
    paragraph.space_before = Pt(space_before_pt)
    paragraph.space_after = Pt(space_after_pt)

    run = paragraph.add_run()
    run.text = text
    _apply_run_formatting(
        run,
        font_size=font_size,
        font_color=font_color,
        font_name=font_name,
        bold=bold,
        italic=italic,
    )

    if bullet:
        _set_bullet(paragraph)


def add_text_box(
    slide,
    text: str | list[str],
    *,
    left_in: float,
    top_in: float,
    width_in: float,
    height_in: float,
    font_size: int,
    font_color: RGBColor = BODY,
    font_name: str = BODY_FONT,
    bold: bool = False,
    italic: bool = False,
    align: str = "left",
    anchor: str = "top",
    line_spacing: float = 1.15,
    bullets: bool = False,
) -> None:
    """Create a text frame at the given geometry and fill it with text.

    If ``text`` is a ``str``, it is rendered as a single paragraph. If it is
    a ``list[str]``, the first entry populates the text frame's default first
    paragraph and the remaining entries are appended via ``add_paragraph``.
    All paragraphs share the same formatting; when ``bullets`` is ``True``
    each paragraph is rendered with a ``•`` bullet.
    """
    textbox = slide.shapes.add_textbox(
        Inches(left_in),
        Inches(top_in),
        Inches(width_in),
        Inches(height_in),
    )
    text_frame = textbox.text_frame
    text_frame.word_wrap = True
    text_frame.vertical_anchor = _ANCHOR_MAP[anchor]

    if isinstance(text, str):
        items = [text]
    else:
        items = list(text)

    if not items:
        return

    # The text frame ships with a single empty paragraph. Reuse it for the
    # first item rather than appending a new one so we don't leave a blank
    # leading line.
    first_paragraph = text_frame.paragraphs[0]
    # Clear any default runs to populate the paragraph cleanly.
    for existing_run in list(first_paragraph.runs):
        existing_run._r.getparent().remove(existing_run._r)

    first_paragraph.alignment = _ALIGN_MAP[align]
    first_paragraph.line_spacing = line_spacing

    first_run = first_paragraph.add_run()
    first_run.text = items[0]
    _apply_run_formatting(
        first_run,
        font_size=font_size,
        font_color=font_color,
        font_name=font_name,
        bold=bold,
        italic=italic,
    )

    if bullets:
        _set_bullet(first_paragraph)

    for entry in items[1:]:
        add_paragraph(
            text_frame,
            entry,
            font_size=font_size,
            font_color=font_color,
            font_name=font_name,
            bold=bold,
            italic=italic,
            align=align,
            bullet=bullets,
        )
        # Match the configured line spacing on appended paragraphs as well.
        text_frame.paragraphs[-1].line_spacing = line_spacing


# ---------------------------------------------------------------------------
# Shape / icon helpers
# ---------------------------------------------------------------------------

# Fallback mapping used when ``USE_GLYPH_EMOJI`` is False and the requested
# glyph is non-ASCII or multi-character. Keys cover every glyph the deck
# intentionally renders (Slide 4 activity row icons and Slide 6 differentiator
# icons) plus a generic bullet fallback.
_GLYPH_ASCII_FALLBACK: dict[str, str] = {
    "♪": "A",
    "🎧": "B",
    "🌍": "C",
    "🃏": "D",
    "✎": "E",
    "AI": "AI",
    "♫": "M",
    "♥": "H",
    "✓": "V",
}


def _resolve_glyph(glyph: str) -> str:
    """Return the glyph to render inside an icon circle.

    If ``USE_GLYPH_EMOJI`` is True, the glyph is used as-is. Otherwise this
    picks a short ASCII-safe substitute: the explicit mapping entry if any,
    else the first ASCII character of the glyph, else ``"•"`` as a last
    resort.
    """
    if USE_GLYPH_EMOJI:
        return glyph
    if glyph in _GLYPH_ASCII_FALLBACK:
        return _GLYPH_ASCII_FALLBACK[glyph]
    for ch in glyph:
        if ch.isascii() and ch.isprintable() and not ch.isspace():
            return ch
    return "•"


def add_icon_circle(
    slide,
    *,
    left_in: float,
    top_in: float,
    diameter_in: float = 0.6,
    fill: RGBColor = ACCENT,
    glyph: str | None = None,
    glyph_color: RGBColor = ON_ACCENT,
    glyph_size: int = 20,
) -> None:
    """Draw a circular accent shape with an optional centered glyph.

    The oval is placed at ``(left_in, top_in)`` with side length
    ``diameter_in`` (inches). It is filled with ``fill`` (defaulting to the
    module-level ``ACCENT``) and renders without a stroke so the circle reads
    as a clean color disc. When ``glyph`` is provided, the oval's own text
    frame is used to center the glyph both horizontally (paragraph alignment)
    and vertically (``MSO_ANCHOR.MIDDLE``). Glyphs honor the module-level
    ``USE_GLYPH_EMOJI`` flag via ``_resolve_glyph``: with emoji disabled, a
    single ASCII letter is substituted so icons still render on hosts without
    emoji-capable fonts.
    """
    shape = slide.shapes.add_shape(
        MSO_SHAPE.OVAL,
        Inches(left_in),
        Inches(top_in),
        Inches(diameter_in),
        Inches(diameter_in),
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    shape.line.fill.background()

    if glyph is None:
        return

    text_frame = shape.text_frame
    text_frame.word_wrap = False
    text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
    # Tight insets keep the glyph visually centered inside a small oval.
    text_frame.margin_left = Inches(0)
    text_frame.margin_right = Inches(0)
    text_frame.margin_top = Inches(0)
    text_frame.margin_bottom = Inches(0)

    paragraph = text_frame.paragraphs[0]
    paragraph.alignment = PP_ALIGN.CENTER
    # Clear any default run so the glyph is the only content.
    for existing_run in list(paragraph.runs):
        existing_run._r.getparent().remove(existing_run._r)

    run = paragraph.add_run()
    run.text = _resolve_glyph(glyph)
    _apply_run_formatting(
        run,
        font_size=glyph_size,
        font_color=glyph_color,
        font_name=BODY_FONT,
        bold=True,
        italic=False,
    )


def add_lyric_motif(
    slide,
    *,
    left_in: float,
    top_in: float,
    width_in: float,
    height_in: float,
) -> None:
    """Compose the Slide 1 "listener with lyrics" motif from pure shapes.

    The motif fits inside the rectangle defined by ``(left_in, top_in)`` and
    ``(width_in, height_in)`` and uses only palette colors (``ACCENT`` and
    ``MUTED``). It is deliberately stylized rather than realistic: a head
    oval with two small headphone ovals flanking it, a rounded-rectangle
    torso below, and three floating lyric-line rectangles of varying widths
    drifting near the figure. No pictures, no extra accent colors.
    """
    # ------------------------------------------------------------------
    # Figure geometry (all values in inches, relative to the motif box)
    # ------------------------------------------------------------------
    head_diameter = min(width_in * 0.38, height_in * 0.28)
    head_left = left_in + (width_in - head_diameter) / 2.0
    head_top = top_in + height_in * 0.08

    head = slide.shapes.add_shape(
        MSO_SHAPE.OVAL,
        Inches(head_left),
        Inches(head_top),
        Inches(head_diameter),
        Inches(head_diameter),
    )
    head.fill.solid()
    head.fill.fore_color.rgb = ACCENT
    head.line.fill.background()

    # Headphone cups: small ovals on either side of the head, vertically
    # centered on the head.
    phone_diameter = head_diameter * 0.35
    phone_top = head_top + (head_diameter - phone_diameter) / 2.0
    phone_left_x = head_left - phone_diameter * 0.55
    phone_right_x = head_left + head_diameter - phone_diameter * 0.45

    for phone_left in (phone_left_x, phone_right_x):
        phone = slide.shapes.add_shape(
            MSO_SHAPE.OVAL,
            Inches(phone_left),
            Inches(phone_top),
            Inches(phone_diameter),
            Inches(phone_diameter),
        )
        phone.fill.solid()
        phone.fill.fore_color.rgb = ACCENT
        phone.line.fill.background()

    # Torso: a rounded rectangle centered horizontally below the head.
    torso_width = width_in * 0.55
    torso_height = height_in * 0.32
    torso_left = left_in + (width_in - torso_width) / 2.0
    torso_top = head_top + head_diameter + height_in * 0.04

    torso = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(torso_left),
        Inches(torso_top),
        Inches(torso_width),
        Inches(torso_height),
    )
    torso.fill.solid()
    torso.fill.fore_color.rgb = ACCENT
    torso.line.fill.background()

    # ------------------------------------------------------------------
    # Floating lyric-line rectangles
    # ------------------------------------------------------------------
    # Each tuple is (x_offset_frac, y_offset_frac, width_frac, color).
    # x_offset_frac/y_offset_frac are anchored to the top-left of the motif
    # box; width_frac is a fraction of the motif width. Line thickness stays
    # constant so the rectangles read as "lyric lines" rather than blocks.
    line_height = 0.08  # inches, thin horizontal bar
    lyric_lines = [
        (0.05, 0.18, 0.28, ACCENT),
        (0.62, 0.32, 0.32, MUTED),
        (0.08, 0.72, 0.42, ACCENT),
        (0.55, 0.86, 0.30, MUTED),
    ]

    for x_frac, y_frac, w_frac, color in lyric_lines:
        line_left = left_in + width_in * x_frac
        line_top = top_in + height_in * y_frac
        line_width = width_in * w_frac
        line_shape = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(line_left),
            Inches(line_top),
            Inches(line_width),
            Inches(line_height),
        )
        line_shape.fill.solid()
        line_shape.fill.fore_color.rgb = color
        line_shape.line.fill.background()


def add_qr_placeholder(
    slide,
    *,
    left_in: float,
    top_in: float,
    size_in: float = 1.8,
    stroke: RGBColor = ACCENT,
) -> None:
    """Draw a QR-code placeholder: a bordered square with a "QR" label and footnote.

    No real QR encoding is performed. The placeholder is a square rectangle at
    ``(left_in, top_in)`` with side length ``size_in`` (inches), filled with the
    background color and stroked with ``stroke`` at roughly 3 pt so the border
    reads clearly. The word "QR" is centered inside the square (both
    horizontally and vertically) in the stroke color at ~40 pt bold. A small
    muted italic footnote, "Mã QR sẽ được cập nhật", is placed directly below
    the square so reviewers understand the final QR will ship later.
    """
    # ------------------------------------------------------------------
    # Bordered square
    # ------------------------------------------------------------------
    square = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(left_in),
        Inches(top_in),
        Inches(size_in),
        Inches(size_in),
    )
    square.fill.solid()
    square.fill.fore_color.rgb = BG
    square.line.color.rgb = stroke
    square.line.width = Pt(3)

    # Centered "QR" label inside the square.
    text_frame = square.text_frame
    text_frame.word_wrap = False
    text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
    text_frame.margin_left = Inches(0)
    text_frame.margin_right = Inches(0)
    text_frame.margin_top = Inches(0)
    text_frame.margin_bottom = Inches(0)

    paragraph = text_frame.paragraphs[0]
    paragraph.alignment = PP_ALIGN.CENTER
    for existing_run in list(paragraph.runs):
        existing_run._r.getparent().remove(existing_run._r)

    run = paragraph.add_run()
    run.text = "QR"
    _apply_run_formatting(
        run,
        font_size=40,
        font_color=stroke,
        font_name=BODY_FONT,
        bold=True,
        italic=False,
    )

    # ------------------------------------------------------------------
    # Muted footnote directly below the square
    # ------------------------------------------------------------------
    footnote_top = top_in + size_in + 0.1
    footnote_height = 0.35
    add_text_box(
        slide,
        "Mã QR sẽ được cập nhật",
        left_in=left_in,
        top_in=footnote_top,
        width_in=size_in,
        height_in=footnote_height,
        font_size=12,
        font_color=MUTED,
        font_name=BODY_FONT,
        italic=True,
        align="center",
        anchor="top",
    )


# ---------------------------------------------------------------------------
# Speaker notes helper
# ---------------------------------------------------------------------------
def add_speaker_notes(slide, notes_text: str) -> None:
    """Attach Vietnamese speaker notes to the slide, replacing any existing text.

    Uses the slide's ``notes_slide.notes_text_frame`` so the notes are
    accessible in PowerPoint's Notes pane and via ``python-pptx`` readers.
    Assigning ``notes_frame.text`` replaces any prior notes rather than
    appending.
    """
    notes_frame = slide.notes_slide.notes_text_frame
    notes_frame.text = notes_text


# ---------------------------------------------------------------------------
# Image helper
# ---------------------------------------------------------------------------
def add_picture(
    slide,
    image_bytes: bytes,
    *,
    left_in: float,
    top_in: float,
    width_in: float | None = None,
    height_in: float | None = None,
) -> None:
    """Embed a raster image (PNG/JPEG bytes) into the slide at the given geometry.

    Wraps ``slide.shapes.add_picture`` so builders can pass raw bytes (as
    returned by the ``assets`` module) without managing a ``BytesIO`` buffer
    themselves. Either ``width_in`` or ``height_in`` may be left ``None``;
    ``python-pptx`` preserves aspect ratio when only one dimension is given.
    """
    buf = io.BytesIO(image_bytes)
    kwargs = {}
    if width_in is not None:
        kwargs["width"] = Inches(width_in)
    if height_in is not None:
        kwargs["height"] = Inches(height_in)
    slide.shapes.add_picture(buf, Inches(left_in), Inches(top_in), **kwargs)


# ---------------------------------------------------------------------------
# Slide builders
#
# Minimalist, typography-forward layouts per the ``instruction.md`` brief:
# each slide has ONE focal point, ≤ 10 words of visible text, no bullets.
# The speaker carries the narrative; the slide is the punctuation.
#
# Every builder adds a blank-layout slide, paints the warm-neutral
# background, renders one ``hero`` phrase centered in accent color, renders
# an optional ``sub`` line in muted color beneath it, and attaches the
# Vietnamese speaker notes. Slides 1, 2, and 7 additionally embed real
# product assets (hero image, logo, app-store badges); Slide 4 embeds a
# small Vertex-generated motif.
# ---------------------------------------------------------------------------
def _build_typography_slide(
    prs,
    content: dict,
    *,
    hero_size: int,
    sub_size: int = SIZE_BODY_L,
    hero_italic: bool = False,
    sub_italic: bool = True,
):
    """Shared scaffold for a one-focal-point typography slide.

    Returns the slide so callers can add per-slide decoration (image,
    small motif) on top of the hero/sub text block.
    """
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_bg(slide, BG)

    # Hero phrase — centered both h/v inside the upper band of the slide.
    # Using anchor="middle" lets the text visually settle rather than
    # clamping to the top of the text frame.
    add_text_box(
        slide,
        content["hero"],
        left_in=1.0,
        top_in=2.6,
        width_in=11.333,
        height_in=1.8,
        font_size=hero_size,
        font_color=ACCENT,
        bold=True,
        italic=hero_italic,
        align="center",
        anchor="middle",
    )

    # Optional small sub-line in muted italic, breathing room beneath the hero.
    if content.get("sub"):
        add_text_box(
            slide,
            content["sub"],
            left_in=1.0,
            top_in=4.7,
            width_in=11.333,
            height_in=0.9,
            font_size=sub_size,
            font_color=MUTED,
            italic=sub_italic,
            align="center",
            anchor="top",
        )

    add_speaker_notes(slide, content["notes"])
    return slide


def build_slide_1_hook(prs) -> None:
    """Slide 1 (Hook): the song title as the focal anchor.

    Elegant "Heal the World" centered-left with the real app hero image
    tucked into the right-hand margin so the song-to-app bridge is
    visible at a glance.
    """
    slide = _build_typography_slide(prs, SLIDES[0], hero_size=SIZE_TITLE_XL)

    # Real app hero image vendored from https://step.is/assets/hero-image.png.
    # Kept small and right-aligned so the song title retains the focal point.
    from assets import hero_image_png

    add_picture(
        slide,
        hero_image_png(),
        left_in=10.5,
        top_in=1.0,
        width_in=2.2,
        height_in=2.2,
    )


def build_slide_2_step(prs) -> None:
    """Slide 2 (What Step Is): brand wordmark + tagline.

    The real Step logo sits above the centered "Step" wordmark, with the
    ``Vừa học. Vừa dùng.`` tagline beneath. Clean, typographic,
    wordmark-forward.
    """
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_bg(slide, BG)

    # Real logo centered above the wordmark.
    from assets import render_logo_png

    # The Step logo rasterized from the vendored SVG. Centering a picture
    # requires knowing its rendered width; we fix height and derive the
    # left offset so the composition reads as a single centered block.
    logo_height_in = 1.3
    # The logo's rendered aspect ratio is roughly 1:1 in the source SVG.
    logo_width_in = 1.3
    logo_left = (SLIDE_WIDTH_IN - logo_width_in) / 2.0
    add_picture(
        slide,
        render_logo_png(height_px=512),
        left_in=logo_left,
        top_in=1.4,
        width_in=logo_width_in,
        height_in=logo_height_in,
    )

    # Wordmark ``Step`` in accent, large, centered below the logo.
    add_text_box(
        slide,
        SLIDES[1]["hero"],
        left_in=1.0,
        top_in=3.1,
        width_in=11.333,
        height_in=1.5,
        font_size=SIZE_TITLE_XL,
        font_color=ACCENT,
        bold=True,
        align="center",
        anchor="middle",
    )

    # Sub-line tagline in muted italic.
    add_text_box(
        slide,
        SLIDES[1]["sub"],
        left_in=1.0,
        top_in=4.8,
        width_in=11.333,
        height_in=0.9,
        font_size=SIZE_BODY_L,
        font_color=MUTED,
        italic=True,
        align="center",
        anchor="top",
    )

    add_speaker_notes(slide, SLIDES[1]["notes"])


def build_slide_3_founder(prs) -> None:
    """Slide 3 (The Founder): name-forward introduction.

    ``Long Lê`` large and centered, with the ``cánh cửa`` sub-line
    beneath. No decoration — the name is the focal point.
    """
    _build_typography_slide(prs, SLIDES[2], hero_size=SIZE_TITLE_XL)


def build_slide_4_insight(prs) -> None:
    """Slide 4 (The Insight): ``decision → "cắt bỏ"``.

    The emotional centre of the deck. The English word ``decision`` sits
    large on top, a thin vertical accent rule below it, and the Vietnamese
    gloss ``"cắt bỏ"`` in italic beneath — composed to hold a beat of
    silence while the speaker delivers the Latin origin.
    """
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_bg(slide, BG)

    # English word — large, accent, centered-upper.
    add_text_box(
        slide,
        SLIDES[3]["hero"],
        left_in=1.0,
        top_in=2.1,
        width_in=11.333,
        height_in=1.6,
        font_size=72,
        font_color=ACCENT,
        bold=True,
        italic=True,
        align="center",
        anchor="middle",
    )

    # Thin vertical accent rule in the middle — the "cut" visualized.
    rule_height_in = 0.7
    rule_left = SLIDE_WIDTH_IN / 2.0 - 0.02
    add_accent_bar(
        slide,
        left_in=rule_left,
        top_in=3.9,
        width_in=0.04,
        height_in=rule_height_in,
    )

    # Vietnamese gloss — muted italic, centered below the rule.
    add_text_box(
        slide,
        SLIDES[3]["sub"],
        left_in=1.0,
        top_in=4.8,
        width_in=11.333,
        height_in=1.2,
        font_size=44,
        font_color=BODY,
        italic=True,
        align="center",
        anchor="middle",
    )

    add_speaker_notes(slide, SLIDES[3]["notes"])


def build_slide_5_why(prs) -> None:
    """Slide 5 (Why It Matters): ``Câu chuyện là cánh cửa.``

    Single-line typography slide with a stylized door motif to the right
    of the text. The shape composition is kept minimal — a thin accent
    rectangle with a small arc on top — so the composition reads as a
    door silhouette without demanding attention from the phrase.
    """
    slide = _build_typography_slide(prs, SLIDES[4], hero_size=60, hero_italic=True)

    # Minimal door motif: a tall narrow rectangle (the door body) plus a
    # small square above it (the lintel/handle). Pure palette colors.
    door_left = 11.2
    door_top = 2.4
    door_width = 0.9
    door_height = 2.7

    door = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(door_left),
        Inches(door_top),
        Inches(door_width),
        Inches(door_height),
    )
    door.fill.solid()
    door.fill.fore_color.rgb = BG
    door.line.color.rgb = ACCENT
    door.line.width = Pt(3)

    # Door handle: small accent square near the right edge, centered vertically.
    handle_size = 0.12
    handle = slide.shapes.add_shape(
        MSO_SHAPE.OVAL,
        Inches(door_left + door_width - 0.25),
        Inches(door_top + door_height / 2.0 - handle_size / 2.0),
        Inches(handle_size),
        Inches(handle_size),
    )
    handle.fill.solid()
    handle.fill.fore_color.rgb = ACCENT
    handle.line.fill.background()


def build_slide_6_promise(prs) -> None:
    """Slide 6 (The Promise): two-line typography.

    Honest and quiet: "Step không làm việc học dễ hơn." as the hero, with
    "Step nuôi dưỡng sự tò mò của bạn." as the sub-line. Typography only.
    """
    _build_typography_slide(prs, SLIDES[5], hero_size=48, sub_size=SIZE_TITLE_M)


def build_slide_7_closing(prs) -> None:
    """Slide 7 (Closing): the education quote + signature + download CTA.

    A single pulled quote ("Giáo dục là thắp lên một ngọn lửa.") occupies
    the upper two-thirds. "Step — Long Lê" appears as a signature beneath.
    A small flame accent motif punctuates the quote. The real App Store
    and Google Play badges anchor the lower-right as the functional CTA.
    """
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_bg(slide, BG)

    # The pulled quote — large, italic, accent, centered.
    add_text_box(
        slide,
        SLIDES[6]["hero"],
        left_in=1.0,
        top_in=1.8,
        width_in=11.333,
        height_in=2.4,
        font_size=46,
        font_color=ACCENT,
        bold=True,
        italic=True,
        align="center",
        anchor="middle",
    )

    # Small flame accent motif: a teardrop shape in accent color,
    # centered below the quote.
    flame_size = 0.5
    flame_left = SLIDE_WIDTH_IN / 2.0 - flame_size / 2.0
    flame = slide.shapes.add_shape(
        MSO_SHAPE.TEAR,
        Inches(flame_left),
        Inches(4.4),
        Inches(flame_size),
        Inches(flame_size * 1.4),
    )
    flame.fill.solid()
    flame.fill.fore_color.rgb = ACCENT
    flame.line.fill.background()
    # Rotate 180° so the teardrop's point faces up like a flame tip.
    flame.rotation = 180

    # Signature line: "Step — Long Lê" in muted body color, centered.
    add_text_box(
        slide,
        SLIDES[6]["sub"],
        left_in=1.0,
        top_in=5.4,
        width_in=11.333,
        height_in=0.6,
        font_size=SIZE_BODY_L,
        font_color=MUTED,
        italic=True,
        align="center",
        anchor="top",
    )

    # Public URL in muted body color below the signature, so the CTA
    # is reachable even without scanning a badge.
    add_text_box(
        slide,
        "https://step.is/vi",
        left_in=1.0,
        top_in=6.1,
        width_in=11.333,
        height_in=0.5,
        font_size=SIZE_BODY_M,
        font_color=MUTED,
        align="center",
        anchor="top",
    )

    # App-store badges — stacked on the lower-left corner so they don't
    # compete with the centered quote/signature column.
    from assets import appstore_badge_png, playstore_badge_png

    add_picture(
        slide,
        appstore_badge_png(),
        left_in=0.6,
        top_in=5.6,
        width_in=1.8,
    )
    add_picture(
        slide,
        playstore_badge_png(),
        left_in=0.6,
        top_in=6.4,
        width_in=1.8,
    )

    add_speaker_notes(slide, SLIDES[6]["notes"])


def build(prs) -> None:
    """Build all 7 content slides in order on the given ``Presentation``.

    Invokes each per-slide builder against ``prs`` in narrative order
    (Slide 1 hook → Slide 7 closing). Each builder appends exactly one
    slide and mutates ``prs`` in place. Does NOT include the title slide
    — that's merged in ``main()`` via ``assets.merge_title_slide``.
    """
    build_slide_1_hook(prs)
    build_slide_2_step(prs)
    build_slide_3_founder(prs)
    build_slide_4_insight(prs)
    build_slide_5_why(prs)
    build_slide_6_promise(prs)
    build_slide_7_closing(prs)


# Which language's title slide to prepend. This module is the Vietnamese
# deck, so the value is "vi". Future locales MUST set the matching
# language code so the correct ``decks/title-slide-<lang>.pptx`` is
# used as the opener (see ``.kiro/steering/deck-pipeline.md``).
DECK_LANGUAGE = "vi"


def main() -> None:
    """Build the deck in memory and upload the .pptx to Cloudflare R2.

    Assembles the deck in three stages and uploads the result without
    touching local disk:

      1. Open the language-appropriate title slide from
         ``decks/title-slide-<lang>.pptx`` as the starting
         ``Presentation``.
      2. Append the 7 minimalist content slides via ``build(prs)``.
      3. Serialize to bytes and upload to the ``step-pitch-decks`` R2
         bucket twice — once under a timestamped snapshot key and once
         under the ``<name>.pptx`` latest alias. The public URL (served
         via ``slides.nspace.is``) is printed on stdout.
    """
    from assets import open_title_slide_presentation, upload_pptx

    prs = open_title_slide_presentation(language=DECK_LANGUAGE)
    build(prs)

    buf = io.BytesIO()
    prs.save(buf)
    final_bytes = buf.getvalue()

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    snapshot_key = _R2_KEY_TEMPLATE.format(stamp=stamp)

    snapshot_url = upload_pptx(final_bytes, key=snapshot_key)
    latest_url = upload_pptx(final_bytes, key=_R2_KEY_LATEST)

    print(f"Uploaded snapshot: {snapshot_url}")
    print(f"Latest:            {latest_url}")


if __name__ == "__main__":
    main()
