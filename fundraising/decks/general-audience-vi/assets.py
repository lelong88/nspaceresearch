"""Asset pipeline for the general-audience-vi-pitch-deck.

Responsibilities:
  - Rasterize ``step-logo.svg`` to PNG bytes for embedding via
    ``python-pptx``'s ``add_picture`` API (cached on disk).
  - Expose the real product assets vendored under ``vendor_assets/``
    (hero image, App Store badge, Google Play badge) as byte helpers.
  - Open the language-appropriate shared title slide from
    ``decks/title-slide-<lang>.pptx`` as a base ``Presentation`` so
    content builders can append their slides onto it.
  - Upload a fully-built ``.pptx`` byte string to the Cloudflare R2
    bucket ``step-pitch-decks`` and return its public URL on
    ``slides.nspace.is``.

All network I/O (R2 upload) is intentionally quarantined to this module
so the slide builders in ``generate_deck.py`` can stay pure and
deterministic. Vertex AI image generation was removed with the move to a
minimalist typography-forward design — every visible asset is now either
a vendored real product asset or a shape rendered inline by the builders.
"""
from __future__ import annotations

import os
from pathlib import Path

import boto3
import cairosvg
from botocore.config import Config as BotoConfig
from dotenv import load_dotenv

# ---------------------------------------------------------------------------
# Paths & config
# ---------------------------------------------------------------------------
_WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
_DECK_DIR = Path(__file__).resolve().parent
_CACHE_DIR = _DECK_DIR / ".asset_cache"
_CACHE_DIR.mkdir(exist_ok=True)

_LOGO_SVG = _WORKSPACE_ROOT / "step-logo.svg"

# Real product assets downloaded once from https://step.is/assets/ and
# committed under ``vendor_assets/`` so builds are reproducible without
# re-fetching on every run.
_VENDOR_DIR = _DECK_DIR / "vendor_assets"
_HERO_IMAGE = _VENDOR_DIR / "hero-image.png"
_APPSTORE_BADGE = _VENDOR_DIR / "appstore.png"
_PLAYSTORE_BADGE = _VENDOR_DIR / "playstore.png"
_VENDOR_LOGO_SVG = _VENDOR_DIR / "logo.svg"

# Shared title slides live at the root of ``decks/`` so every deck in
# this repo can pull from the same file. Language-aware — see
# ``.kiro/steering/deck-pipeline.md``.
_TITLE_SLIDES_DIR = _WORKSPACE_ROOT / "decks"

# R2 / public CDN
_BUCKET = "step-pitch-decks"
_PUBLIC_DOMAIN = "slides.nspace.is"

load_dotenv(_WORKSPACE_ROOT / ".env", override=False)


# ---------------------------------------------------------------------------
# Logo rasterization
# ---------------------------------------------------------------------------
def render_logo_png(height_px: int = 256) -> bytes:
    """Render the Step logo SVG to a PNG byte string at the given pixel height.

    Prefers ``decks/general-audience-vi/vendor_assets/logo.svg`` (the
    canonical brand asset downloaded from https://step.is/assets/logo.svg)
    and falls back to the workspace-root ``step-logo.svg`` if the vendor
    copy is missing. Cached on disk after the first call so subsequent
    calls return instantly.
    """
    cache_key = f"logo_h{height_px}.png"
    cached = _CACHE_DIR / cache_key
    if cached.exists():
        return cached.read_bytes()

    src = _VENDOR_LOGO_SVG if _VENDOR_LOGO_SVG.exists() else _LOGO_SVG
    svg_bytes = src.read_bytes()
    png_bytes = cairosvg.svg2png(
        bytestring=svg_bytes,
        output_height=height_px,
    )
    cached.write_bytes(png_bytes)
    return png_bytes


# ---------------------------------------------------------------------------
# Real product assets (vendored from https://step.is/assets/)
# ---------------------------------------------------------------------------
def hero_image_png() -> bytes:
    """Return the app hero/screenshot PNG as bytes. 512×512, RGBA."""
    return _HERO_IMAGE.read_bytes()


def appstore_badge_png() -> bytes:
    """Return the Apple App Store download badge as bytes. ~500×176 PNG."""
    return _APPSTORE_BADGE.read_bytes()


def playstore_badge_png() -> bytes:
    """Return the Google Play 'Get it on' badge as bytes. ~500×156 PNG."""
    return _PLAYSTORE_BADGE.read_bytes()


# ---------------------------------------------------------------------------
# Title slide prepend (language-aware)
# ---------------------------------------------------------------------------
def open_title_slide_presentation(*, language: str):
    """Open ``decks/title-slide-<language>.pptx`` as a fresh ``Presentation``.

    Content builders append their slides onto the returned presentation,
    so the resulting deck opens with the language-appropriate title slide
    and is followed by the content slides in narrative order. No XML
    surgery is involved — using the title-slide file as the base
    presentation preserves its masters, layouts, theme, fonts, and any
    embedded images.

    Args:
        language: Two-letter language code (``vi``, ``en``, ...). Must
            match the suffix of a file in ``decks/`` named
            ``title-slide-<language>.pptx``.

    Raises:
        FileNotFoundError: if the matching title-slide file is missing.
    """
    from pptx import Presentation

    path = _TITLE_SLIDES_DIR / f"title-slide-{language}.pptx"
    if not path.exists():
        raise FileNotFoundError(
            f"Title slide file not found at {path}. Expected a file named "
            f"'title-slide-{language}.pptx' under decks/. See "
            f".kiro/steering/deck-pipeline.md for the project rule."
        )
    return Presentation(str(path))


# ---------------------------------------------------------------------------
# R2 upload
# ---------------------------------------------------------------------------
def _r2_client():
    """Construct a boto3 S3 client pointed at Cloudflare R2."""
    return boto3.client(
        "s3",
        endpoint_url=os.environ["R2_ENDPOINT_URL"],
        aws_access_key_id=os.environ["R2_ACCESS_KEY_ID"],
        aws_secret_access_key=os.environ["R2_SECRET_ACCESS_KEY"],
        region_name="auto",
        config=BotoConfig(signature_version="s3v4"),
    )


def upload_pptx(data: bytes, *, key: str, bucket: str = _BUCKET) -> str:
    """Upload a ``.pptx`` byte string to R2 and return its public URL.

    Public access is served through the Cloudflare custom domain
    ``slides.nspace.is`` that is attached to the ``step-pitch-decks``
    bucket. The returned URL is directly shareable.
    """
    client = _r2_client()
    client.put_object(
        Bucket=bucket,
        Key=key,
        Body=data,
        ContentType=(
            "application/vnd.openxmlformats-officedocument.presentationml."
            "presentation"
        ),
    )
    return f"https://{_PUBLIC_DOMAIN}/{key}"


# ---------------------------------------------------------------------------
# Convenience
# ---------------------------------------------------------------------------
def public_url(key: str) -> str:
    """Return the public URL for a given object key under the CDN domain."""
    return f"https://{_PUBLIC_DOMAIN}/{key}"
