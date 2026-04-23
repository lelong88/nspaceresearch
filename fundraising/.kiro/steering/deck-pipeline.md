# Deck pipeline — project rules

These rules apply to every pitch deck generated in this repo (starting with
`decks/general-audience-vi/`) and should be followed for any future deck
spec unless a deck's own spec explicitly overrides them.

## Output location: R2, not local disk

- **Do not save `.pptx` files to local disk.** Decks are built in memory
  and uploaded directly to the Cloudflare R2 bucket `step-pitch-decks`.
- **Do not commit `.pptx` files to the repository.** If one shows up in a
  working copy (e.g., from a past workflow), delete it; the canonical
  artifact lives in R2.
- Public access is served through the Cloudflare custom domain
  `slides.nspace.is` attached to `step-pitch-decks`. The shareable URL
  for any object `<key>` is `https://slides.nspace.is/<key>`.
- **Upload to the bucket root.** Do not use per-feature prefixes or
  subfolders — every deck's keys live at the top level of
  `step-pitch-decks`. Name each deck with a distinct `<name>` (e.g.,
  `step-pitch-vi` for Vietnamese, `step-pitch-en` for English) so keys
  don't collide.
- Each `main()` run uploads **two** objects at the bucket root:
  - `<name>-<UTC-timestamp>.pptx` — an immutable snapshot.
  - `<name>.pptx` — a mutable `latest` alias that overwrites on every
    run. This is the URL to share.
- R2 credentials live in `.env` at the workspace root (`R2_ACCESS_KEY_ID`,
  `R2_SECRET_ACCESS_KEY`, `R2_ENDPOINT_URL`). `decks/.../assets.py` reads
  them via `python-dotenv`. Do not hard-code or commit credentials.

## README per deck

- Every deck directory MUST contain a `README.md` alongside
  `generate_deck.py`. The README must document:
  - The **latest deck URL** (`https://slides.nspace.is/<name>.pptx`)
    prominently near the top.
  - A short "How to regenerate" section with the exact command.
  - A note that the pipeline rules in this steering doc apply.
- Update the README's URL if the deck's canonical name ever changes.
  The URL in the README is the single user-facing reference point.

## Image generation via Vertex AI

- Use `gen_image_vertex.generate_image_vertex(prompt, aspect_ratio=...)`
  (workspace root) for every illustration that can't be expressed cleanly
  as python-pptx shapes.
- Vertex credentials live in `quan_serviceAccountKey.json` at the
  workspace root. Do not move or duplicate that file; the image module
  resolves it relative to its own location.
- Cache generated images on disk under
  `decks/<feature>/.asset_cache/` keyed by a hash of
  `(prompt, aspect_ratio)`. Rerunning the generator must **not** re-bill
  Vertex unless a prompt or aspect ratio actually changed.
- Add `.asset_cache/` to `.gitignore` for each deck directory so cached
  bytes don't bloat the repo.
- Avoid stock-photo language-learning clichés (e.g., headset-in-front-of-
  flags). Prompts should bias toward warm, editorial, minimal flat-vector
  illustrations and explicitly state the slide's palette hex values.

## Real branding

- Use the real `step-logo.svg` at the workspace root for any Step brand
  mark; do not synthesize a logo from shapes or text.
- Rasterize the SVG to PNG at build time via `cairosvg.svg2png`; embed
  the resulting bytes via `python-pptx`'s `add_picture` API. Pick an
  `output_height` large enough to stay crisp at the embed size (256–512
  px is typical).

## Prefer real product assets over generated illustrations

- Before generating anything via Vertex, check whether a real asset on
  `https://step.is/assets/` already fits the slot. Canonical assets
  include `logo.svg`, `hero-image.png`, `appstore.png`, `playstore.png`,
  and `zalo.png`. If an asset fits, use it — don't re-imagine it.
- Download real assets once via `curl` and vendor them inside the deck
  directory at `decks/<feature>/vendor_assets/`. Commit the vendored
  copies so builds are reproducible without re-fetching on every run.
- Expose each vendored asset through a dedicated byte-loader in
  `assets.py` (e.g., `hero_image_png()`, `appstore_badge_png()`,
  `playstore_badge_png()`). Builders consume these helpers via
  `add_picture(slide, helper(), ...)`.
- On the CTA slide, always include both App Store and Google Play
  badges (stacked or side-by-side) alongside the product URL — the
  badges carry more recognition than the URL alone.
- Reserve Vertex generation for slots where no real asset exists (e.g.,
  a conceptual mood image for a worked example). Document the Vertex
  prompt and cache key in `assets.py` so re-runs don't re-bill.

## CTA on the closing slide

- **Never include a QR code** — decks ship with a text URL only.
- For Vietnamese decks the URL is `https://step.is/vi`. For future
  locales, use the matching `step.is/<locale>` URL. Render it in the
  slide's next-step line, not as a standalone shape.

## Module layout per deck

```
decks/<feature>/
├── README.md            # latest URL + how-to-regenerate (required)
├── instruction.md       # source brief (not generated)
├── generate_deck.py     # builds the Presentation, calls assets.upload_pptx
├── assets.py            # SVG rasterize, Vertex wrappers, R2 uploader
├── tests/               # pytest suite (see below)
├── vendor_assets/       # real assets downloaded from step.is, committed
└── .asset_cache/        # generated images (Vertex output), gitignored
```

`generate_deck.py` stays a pure composition layer — it imports from
`assets.py` for all network or SVG I/O. `main()` constructs the
`Presentation`, calls `build(prs)`, serializes to `BytesIO`, and uploads
via `assets.upload_pptx(bytes, key=...)`.

## Testing rules

- Tests must run offline. Add an `autouse` module-scoped fixture in
  `conftest.py` that stubs every `assets.slide_*_illustration` helper
  with a tiny valid PNG (a 1×1 transparent pixel is sufficient — see
  `decks/general-audience-vi/tests/conftest.py` for the canonical
  implementation).
- Integration tests must stub R2 at the `assets._r2_client` seam (a
  fake with a `put_object` method is enough). Required assertions:
  - `main()` performs exactly two uploads (snapshot + latest) against
    the `step-pitch-decks` bucket.
  - Both uploaded bodies reopen as a valid `Presentation` with the
    expected slide count.
  - The public URL printed on stdout points at
    `https://slides.nspace.is/`.
  - After `main()` returns, the deck directory contains no `.pptx`
    files (no-local-file rule).
- Per-slide content tests consume the in-memory `built_prs` fixture and
  assert Vietnamese literals verbatim (em dashes and smart quotes copied
  from the `SLIDES` data model, not retyped).

## When documenting a completed run

When the user asks for the current URL of a deck, return the `latest`
URL (e.g., `https://slides.nspace.is/step-pitch-vi.pptx` — bucket root,
no per-feature prefix) and note the snapshot URL is also available if
they want a frozen version. The deck's own `README.md` should already
carry this URL as its single source of truth; point users there when
they need a persistent reference. Do not mention QR codes, local file
paths, or internal spec file paths in user-facing summaries.
