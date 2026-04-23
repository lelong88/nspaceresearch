"""Asset pipeline for the general-audience-vi-pitch-deck.

Responsibilities:
  - Rasterize ``step-logo.svg`` (repo root) to a PNG byte string the
    ``python-pptx`` ``add_picture`` API can embed.
  - Generate illustrated slide images via ``gen_image_vertex`` (Vertex AI
    Gemini 3.1 Flash Image Preview). Generated images are cached on local
    disk under ``decks/general-audience-vi/.asset_cache/`` keyed by prompt
    hash so re-runs don't re-bill the model.
  - Upload a fully-built ``.pptx`` byte string to the Cloudflare R2 bucket
    ``step-pitch-decks`` and return its public URL on ``slides.nspace.is``.

All network I/O (Vertex generation, R2 upload) is intentionally quarantined
to this module so the slide builders in ``generate_deck.py`` can stay pure
and deterministic.
"""
from __future__ import annotations

import asyncio
import hashlib
import io
import os
import sys
from pathlib import Path
from typing import Optional

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

# R2 / public CDN
_BUCKET = "step-pitch-decks"
_PUBLIC_DOMAIN = "slides.nspace.is"

load_dotenv(_WORKSPACE_ROOT / ".env", override=False)


# ---------------------------------------------------------------------------
# Logo rasterization
# ---------------------------------------------------------------------------
def render_logo_png(height_px: int = 256) -> bytes:
    """Render ``step-logo.svg`` to a PNG byte string at the given pixel height.

    The source SVG has a viewBox of roughly 1280×1280 with centered glyphs;
    cairosvg preserves aspect ratio given only a height. Cached on first
    call and returned from memory thereafter.
    """
    cache_key = f"logo_h{height_px}.png"
    cached = _CACHE_DIR / cache_key
    if cached.exists():
        return cached.read_bytes()

    svg_bytes = _LOGO_SVG.read_bytes()
    png_bytes = cairosvg.svg2png(
        bytestring=svg_bytes,
        output_height=height_px,
    )
    cached.write_bytes(png_bytes)
    return png_bytes


# ---------------------------------------------------------------------------
# Vertex AI illustration generation (with disk cache)
# ---------------------------------------------------------------------------
def _prompt_cache_path(prompt: str, aspect_ratio: str) -> Path:
    """Return a deterministic cache path for a (prompt, aspect) pair."""
    key = hashlib.sha256(f"{aspect_ratio}\n{prompt}".encode("utf-8")).hexdigest()[:16]
    return _CACHE_DIR / f"img_{aspect_ratio.replace(':', 'x')}_{key}.png"


def generate_illustration(prompt: str, aspect_ratio: str = "4:3") -> bytes:
    """Generate an illustration via Vertex Gemini; cache the bytes on disk.

    Synchronous wrapper over ``gen_image_vertex.generate_image_vertex``.
    Returns raw image bytes (PNG). Safe to call repeatedly — the first call
    hits Vertex (~30s), subsequent calls with the same (prompt, aspect)
    pair return the cached bytes instantly.
    """
    cached = _prompt_cache_path(prompt, aspect_ratio)
    if cached.exists():
        return cached.read_bytes()

    # Lazy import so the deck builder module itself never needs the
    # google-genai SDK at import time.
    if str(_WORKSPACE_ROOT) not in sys.path:
        sys.path.insert(0, str(_WORKSPACE_ROOT))
    from gen_image_vertex import generate_image_vertex

    # ``generate_image_vertex`` is async; bridge to sync here.
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            # Running inside a live event loop (unlikely for the deck
            # builder, but guard defensively). Create a fresh loop.
            raise RuntimeError("reentrant event loop")
    except RuntimeError:
        loop = asyncio.new_event_loop()

    try:
        img_bytes = loop.run_until_complete(
            generate_image_vertex(prompt, aspect_ratio=aspect_ratio)
        )
    finally:
        # Don't close the default event loop if it was fetched via
        # get_event_loop(); only close loops we explicitly created.
        if loop is not asyncio.get_event_loop_policy().get_event_loop():
            loop.close()

    cached.write_bytes(img_bytes)
    return img_bytes


# ---------------------------------------------------------------------------
# Deck-specific illustration prompts
# ---------------------------------------------------------------------------
# Each prompt targets the warm neutral + deep-teal palette used in the deck
# and avoids stock-photo language-learning clichés (Req 11.6). Prompts are
# stable strings so the cache key stays consistent across runs.

_PROMPT_SLIDE_1 = (
    "Warm editorial illustration on a cream #FAF7F2 background. A young "
    "Vietnamese adult seen from the shoulders up, eyes softly closed, "
    "wearing simple over-ear headphones. Faint hand-drawn lyric lines in "
    "English drift around them like ribbons — not legible, just the shapes "
    "of typewritten lines. Muted deep-teal and soft coral accents, no logos, "
    "no text, no flags, no headsets-in-front-of-flags cliché. Minimal, "
    "contemplative mood. Flat vector look with subtle grain."
)

_PROMPT_SLIDE_4 = (
    "Warm editorial illustration on a cream #FAF7F2 background. A pair of "
    "open hands gently cradling a small glowing world with musical notes "
    "floating out of it, evoking the feeling of the song 'Heal the World'. "
    "Deep-teal and soft coral palette. No text, no logos, no photorealism. "
    "Minimal, hopeful, editorial flat-vector style."
)

_PROMPT_SLIDE_7 = (
    "Warm editorial illustration on a cream #FAF7F2 background. An open "
    "book transforming into a door of light, with a silhouette of a person "
    "stepping toward it. Soft coral and deep-teal accents. Minimal, "
    "inviting, no text, no logos, flat-vector illustration style."
)


def slide_1_illustration() -> bytes:
    """Lyric-listener illustration for Slide 1 (hook). Cached after first run."""
    return generate_illustration(_PROMPT_SLIDE_1, aspect_ratio="4:3")


def slide_4_illustration() -> bytes:
    """'Heal the World' mood image for Slide 4. Cached after first run."""
    return generate_illustration(_PROMPT_SLIDE_4, aspect_ratio="4:3")


def slide_7_illustration() -> bytes:
    """Closing-invitation image for Slide 7 (CTA). Cached after first run."""
    return generate_illustration(_PROMPT_SLIDE_7, aspect_ratio="1:1")


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
