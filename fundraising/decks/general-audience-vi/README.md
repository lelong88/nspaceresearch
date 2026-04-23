# General-audience Vietnamese pitch deck

Minimalist, typography-forward 8-slide pitch deck for **Step**, built by
`generate_deck.py`. The deck opens with the shared Vietnamese title
slide and is followed by 7 content slides, each a single focal point.
The speaker carries the narrative; the slides are the punctuation.

## Latest deck URL

**`https://slides.nspace.is/step-pitch-vi.pptx`**

This is the `latest` alias — it overwrites on every generator run. A
timestamped snapshot is also uploaded under
`https://slides.nspace.is/step-pitch-vi-<UTC-timestamp>.pptx` if you
need a frozen reference.

## Slide map

| # | Purpose            | What's on the slide                                   |
|---|--------------------|-------------------------------------------------------|
| 1 | Title (shared)     | STEP. wordmark + tagline + founder name               |
| 2 | Hook               | "Heal the World" + tagline + app hero image           |
| 3 | What Step Is       | Logo + "Step" wordmark + "Vừa học. Vừa dùng."         |
| 4 | The Founder        | "Long Lê" + "Ngoại ngữ là một cánh cửa."              |
| 5 | The Insight        | `decision` ↓ `"cắt bỏ"` — emotional centre            |
| 6 | Why It Matters     | "Câu chuyện là cánh cửa." + door motif                |
| 7 | The Promise        | "Step không làm việc học dễ hơn." + curiosity sub     |
| 8 | Closing            | Education-fire quote + signature + App Store / Play   |

## How to regenerate

From the workspace root:

```bash
python decks/general-audience-vi/generate_deck.py
```

The script opens the shared title slide from
`decks/title-slide-vi.pptx`, appends the 7 content slides in memory, and
uploads the merged `.pptx` directly to the Cloudflare R2 bucket
`step-pitch-decks`. No `.pptx` is written to local disk. The public
CDN-backed URL is printed on stdout.

## Tests

```bash
python -m pytest decks/general-audience-vi/tests -v
```

All tests run offline: the vendored-asset byte helpers are stubbed with
a 1×1 PNG, and the R2 client is stubbed at the `assets._r2_client`
seam. See `tests/conftest.py` for the fixtures.

## Project rules

The pipeline follows the rules in
[`.kiro/steering/deck-pipeline.md`](../../.kiro/steering/deck-pipeline.md):
every deck opens with the shared language-appropriate title slide
(`decks/title-slide-<lang>.pptx`), uploads to the bucket root (no
per-feature prefix), leaves no `.pptx` on local disk, and uses real
product assets (logo, hero image, app-store badges) in place of
synthesized illustrations where possible. No QR codes — the URL
`https://step.is/vi` is rendered as text on the closing slide.
