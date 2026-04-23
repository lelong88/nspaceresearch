# General-audience Vietnamese pitch deck

7-slide Vietnamese-language pitch deck for **Step**, produced by
`generate_deck.py`. Content lives in `SLIDES` (module constant) and
illustrations come from Vertex Gemini via `assets.py`.

## Latest deck URL

**`https://slides.nspace.is/step-pitch-vi.pptx`**

This is the `latest` alias — it overwrites on every generator run. A
timestamped snapshot is also uploaded on each run under
`https://slides.nspace.is/step-pitch-vi-<UTC-timestamp>.pptx` if you
need a frozen reference.

## How to regenerate

From the workspace root:

```bash
python decks/general-audience-vi/generate_deck.py
```

The script builds the deck entirely in memory, generates any missing
illustrations via Vertex (cached under `.asset_cache/` thereafter), and
uploads the `.pptx` directly to the Cloudflare R2 bucket
`step-pitch-decks`. No `.pptx` is written to local disk. The public
CDN-backed URL is printed on stdout.

## Tests

```bash
python -m pytest decks/general-audience-vi/tests -v
```

All tests run offline: illustration helpers are stubbed with a 1×1 PNG,
and the R2 client is stubbed at the `assets._r2_client` seam. See
`tests/conftest.py` for the fixtures.

## Project rules

The pipeline follows the rules in
[`.kiro/steering/deck-pipeline.md`](../../.kiro/steering/deck-pipeline.md):
decks upload to the bucket **root** (no per-feature prefix), no local
`.pptx` files, no QR codes on the CTA slide (the URL
`https://step.is/vi` carries the invitation instead), and the real
`step-logo.svg` is used as the brand mark.
