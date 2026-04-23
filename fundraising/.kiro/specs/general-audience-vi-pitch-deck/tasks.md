# Implementation Plan: general-audience-vi-pitch-deck

## Overview

This plan builds the Vietnamese-language, 7-slide pitch deck for the product **Step** as a single `python-pptx` generator script at `decks/general-audience-vi/generate_deck.py`, followed by the committed `.pptx` artifact at `decks/general-audience-vi/step-pitch-vi.pptx`.

The work proceeds bottom-up from constants and helper functions, then builds each slide one at a time with its property-based tests placed immediately next to the implementation (PBT-alongside pattern from the design). Slide 4 keeps its 5-activity exception to Requirement 3.5 per the documented design decision. The 14 correctness properties from the design are each implemented as a single `hypothesis`-based test with ≥100 iterations and tagged with the feature name and property number. A final checkpoint runs the generator end-to-end and verifies the committed `.pptx` is produced and valid.

Implementation language is Python (explicit in the design; the design does not use pseudocode). Test framework is `pytest` + `hypothesis`.

## Tasks

- [x] 1. Set up generator skeleton and constants
  - Create the target directory and file `decks/general-audience-vi/generate_deck.py`
  - Add module docstring documenting the `python-pptx` dependency and how to run the script
  - Add imports from `pptx`, `pptx.util`, `pptx.dml.color`, `pptx.enum.shapes`, `pptx.enum.text`, and `pathlib.Path`
  - Define palette constants (`ACCENT`, `BG`, `BODY`, `MUTED`, `ON_ACCENT`) as `RGBColor` values matching the hex literals in the design
  - Define typography constants (`HEADLINE_FONT`, `BODY_FONT`, `FALLBACK_FONT`) and size constants (`SIZE_TITLE_XL`, `SIZE_TITLE_L`, `SIZE_TITLE_M`, `SIZE_TAGLINE`, `SIZE_BODY_L`, `SIZE_BODY_M`, `SIZE_BODY_S`)
  - Define geometry constants (`SLIDE_WIDTH_IN = 13.333`, `SLIDE_HEIGHT_IN = 7.5`, `MARGIN_IN = 0.6`)
  - Define the `USE_GLYPH_EMOJI` toggle near the palette constants
  - Add a stub `main()` that constructs a `Presentation`, sets slide width/height, and writes to `decks/general-audience-vi/step-pitch-vi.pptx`
  - Add the `if __name__ == "__main__": main()` entrypoint
  - _Requirements: 1.3, 2.5, 11.1, 11.2, 13.1, 13.2, 13.5_

- [ ] 2. Create the `SLIDES` data model with Vietnamese content
  - [x] 2.1 Define the `SLIDES` module-level list with 7 entries
    - One dict per slide matching the `SlideContent` structure from the design (keys: `index`, `title`, `subtitle`, `body`, `emphasis`, `closing`, `visual`, `notes`)
    - Populate Slide 1 content: hook headline per Req 4.1 and one supporting line per Req 4.3
    - Populate Slide 2 content: title + exactly 3 bullets covering the three ideas in Req 5.3
    - Populate Slide 3 content: old→new reframe pair (Req 6.1), `Core_Message` tagline verbatim in `emphasis` (Req 2.4, Req 6.2), one-sentence explanation listing songs/novels/manga/podcasts/films (Req 6.3)
    - Populate Slide 4 content: title framing `Heal the World` (Req 7.1), five activity items (Req 7.2), closing line (Req 7.3)
    - Populate Slide 5 content: worldview paragraph (Req 8.1), heal-vs-cure paragraph (Req 8.2), `emphasis` one-liner *"Mỗi ngôn ngữ mới là một phiên bản mới của chính bạn."* (Req 8.3)
    - Populate Slide 6 content: exactly 4 differentiator cells, each with a short label and a body of ≤16 words (Req 9.1, Req 9.3)
    - Populate Slide 7 content: invitation headline (Req 10.1), sub-text (Req 10.2), `Step` brand + next-step line, QR visual kind (Req 10.3, Req 10.4)
    - Attach 2–3 sentence Vietnamese speaker notes on every slide (Req 3.3)
    - _Requirements: 1.2, 2.1, 2.2, 2.3, 2.4, 2.5, 3.1, 3.2, 3.3, 3.5, 4.1, 4.3, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3, 7.1, 7.2, 7.3, 8.1, 8.2, 8.3, 9.1, 9.3, 10.1, 10.2, 10.3, 10.4_

  - [ ]* 2.2 Write property test for `SLIDES` content data model
    - **Property 2: Every slide has a non-empty Vietnamese title and body**
    - **Validates: Requirements 2.1, 3.1, 3.2**
    - Iterate exhaustively over all 7 entries in `SLIDES`; assert non-empty `title`, non-empty `body` list, combined title+body+emphasis+closing contains at least one Vietnamese diacritic character
    - _Requirements: 2.1, 3.1, 3.2_

  - [ ]* 2.3 Write property test for speaker notes shape
    - **Property 3: Every slide has 2–3 sentence speaker notes**
    - **Validates: Requirement 3.3**
    - Exhaustive iteration over `SLIDES`; assert `notes` is non-empty and contains between 2 and 3 sentence-terminator characters from `{".", "!", "?"}`
    - _Requirements: 3.3_

  - [ ]* 2.4 Write property test for bullet count and word count bounds
    - **Property 5: Body bullet count and word count stay within bounds**
    - **Validates: Requirement 3.5 (with Slide 4 override from Requirement 7.2)**
    - Exhaustive iteration over `SLIDES`; assert body bullet count ≤ `max_bullets_for_slide` (4 default, 5 for Slide 4) and total body word count ≤ 60
    - _Requirements: 3.5, 7.2_

  - [ ]* 2.5 Write property test for deny-listed phrases
    - **Property 6: No deny-listed competitor or defensive-claim phrase appears**
    - **Validates: Requirements 5.4, 12.3, 12.4**
    - Define deny-list (competitor product names, defensive templates like "unlike", "better than", "we are better")
    - Exhaustive iteration over `SLIDES`; assert no deny-listed phrase appears as case-insensitive substring in combined slide text (title, body, emphasis, closing, notes)
    - _Requirements: 5.4, 12.3, 12.4_

- [x] 3. Implement layout helper functions
  - [x] 3.1 Implement `add_bg(slide, color)` and `add_accent_bar(slide, ...)`
    - `add_bg` paints a full-bleed rectangle at `(0, 0, 13.333, 7.5)` with the given solid fill color
    - `add_accent_bar` draws a thin rectangle at the given geometry with the given fill color
    - _Requirements: 11.1, 11.2_

  - [x] 3.2 Implement text helpers `add_text_box(...)` and `add_paragraph(...)`
    - `add_text_box` creates a text frame at the given geometry and fills it with one or more paragraphs using the given font name, size, color, weight, alignment, and anchor; supports a `bullets` flag for rendering `list[str]` as bulleted paragraphs
    - `add_paragraph` appends a paragraph to an existing text frame with explicit formatting (size, color, font, bold/italic, alignment, bullet flag, spacing)
    - Ensure all text frames respect the 0.5-inch safe margin by construction when passed geometry matching the per-slide layout specs
    - _Requirements: 2.1, 2.5, 11.3, 11.4, 11.5_

  - [x] 3.3 Implement `add_icon_circle(...)` and `add_lyric_motif(...)`
    - `add_icon_circle` draws an oval of the given diameter at the given position, filled with accent color, optionally centering a 1–3 char glyph in `ON_ACCENT` at the given size; honors the `USE_GLYPH_EMOJI` toggle (substitutes a single ASCII letter if `False`)
    - `add_lyric_motif` composes the Slide 1 silhouette + floating lyric-line rectangles using only shapes (no images)
    - _Requirements: 3.4, 4.2, 11.6_

  - [x] 3.4 Implement `add_qr_placeholder(...)` and `add_speaker_notes(slide, notes_text)`
    - `add_qr_placeholder` draws a square with the accent stroke, centers the label `QR` in accent color, and adds a small `Mã QR sẽ được cập nhật` muted footnote below
    - `add_speaker_notes` attaches `notes_text` to `slide.notes_slide.notes_text_frame`
    - _Requirements: 3.3, 10.3_

- [x] 4. Implement slide builders — part 1 (Slides 1–3)
  - [x] 4.1 Implement `build_slide_1_hook(prs)`
    - Add blank slide, background, left accent bar, headline text box at the geometry from the Slide 1 layout spec
    - Add the supporting italic line in muted color
    - Call `add_lyric_motif(...)` at the right-hand geometry
    - Attach speaker notes from `SLIDES[0]["notes"]`
    - _Requirements: 1.2, 4.1, 4.2, 4.3, 11.1, 11.2, 11.3, 11.4, 11.5_

  - [x] 4.2 Implement `build_slide_2_gap(prs)`
    - Add blank slide, background, top accent bar, title in accent color
    - Render the 3 body bullets at the three geometries from the Slide 2 layout spec
    - Attach speaker notes from `SLIDES[1]["notes"]`
    - _Requirements: 1.2, 5.1, 5.2, 5.3, 5.4, 11.1, 11.2, 11.3, 11.4, 11.5_

  - [x] 4.3 Implement `build_slide_3_intro(prs)`
    - Add blank slide, background, old (muted italic) and new (bold body) reframe question text boxes with the accent arrow shape between them
    - Render the accent rule, then the `Core_Message` tagline in accent color at `SIZE_TAGLINE`+, centered
    - Render the one-sentence explanation line
    - Attach speaker notes from `SLIDES[2]["notes"]`
    - _Requirements: 1.2, 2.4, 6.1, 6.2, 6.3, 11.1, 11.2, 11.3, 11.4, 11.5_

- [x] 5. Implement slide builders — part 2 (Slides 4–5)
  - [x] 5.1 Implement `build_slide_4_heal(prs)`
    - Add blank slide, background, title, italic subtitle framing the song
    - Render 5 activity rows, each composed of `add_icon_circle(...)` + row text box at the geometries from the Slide 4 layout spec; glyphs in order: ♪, 🎧, 🌍, 🃏, ✎ (honoring `USE_GLYPH_EMOJI`)
    - Render the closing line in accent bold-italic
    - Attach speaker notes from `SLIDES[3]["notes"]`
    - _Requirements: 1.2, 7.1, 7.2, 7.3, 11.1, 11.2, 11.3, 11.4, 11.5_

  - [x] 5.2 Implement `build_slide_5_why(prs)`
    - Add blank slide, background, top accent bar, title
    - Render insight paragraph 1 (worldview) and paragraph 2 (heal vs cure)
    - Render divider rule, then the `emphasis` one-liner centered in accent at `SIZE_TAGLINE` italic bold
    - Attach speaker notes from `SLIDES[4]["notes"]`
    - _Requirements: 1.2, 8.1, 8.2, 8.3, 11.1, 11.2, 11.3, 11.4, 11.5_

- [x] 6. Implement slide builders — part 3 (Slides 6–7) and orchestration
  - [x] 6.1 Implement `build_slide_6_diff(prs)`
    - Add blank slide, background, title
    - Render the 2×2 differentiator grid: for each of the 4 cells, call `add_icon_circle(...)` with the cell's glyph (`AI`, ♫, ♥, ✓) then the label and body text boxes at the geometries from the Slide 6 layout spec
    - Attach speaker notes from `SLIDES[5]["notes"]`
    - _Requirements: 1.2, 9.1, 9.2, 9.3, 11.1, 11.2, 11.3, 11.4, 11.5_

  - [x] 6.2 Implement `build_slide_7_cta(prs)`
    - Add blank slide, background, centered invitation headline in accent at `SIZE_TITLE_XL`
    - Render the italic sub-text centered, brand mark `Step` left-aligned, next-step line below brand
    - Call `add_qr_placeholder(...)` at the right-hand position
    - Attach speaker notes from `SLIDES[6]["notes"]`
    - _Requirements: 1.2, 10.1, 10.2, 10.3, 10.4, 11.1, 11.2, 11.3, 11.4, 11.5_

  - [x] 6.3 Implement `build(prs)` orchestrator and finalize `main()`
    - `build(prs)` invokes the 7 builders in order (Slide 1 → Slide 7)
    - `main()` constructs `Presentation()`, sets 16:9 widescreen slide size, calls `build(prs)`, and saves to `decks/general-audience-vi/step-pitch-vi.pptx` (overwriting if present)
    - _Requirements: 1.1, 1.2, 1.3, 13.1, 13.2, 13.3, 13.4_

- [x] 7. Checkpoint — generator runs clean
  - Run `python decks/general-audience-vi/generate_deck.py` from the workspace root; confirm exit code 0 and that `decks/general-audience-vi/step-pitch-vi.pptx` is written
  - Ensure all tests implemented so far pass, ask the user if questions arise.

- [x] 8. Set up test scaffolding
  - [x] 8.1 Create test package layout
    - Create `decks/general-audience-vi/tests/__init__.py`
    - Create `decks/general-audience-vi/tests/conftest.py` with a module-scoped `built_prs` fixture that imports the generator and returns `build(Presentation())`, and a `built_pptx_path` fixture that calls `main()` with the output path redirected into `tmp_path`
    - _Requirements: 13.1, 13.3_

  - [ ]* 8.2 Write smoke tests
    - Add `test_smoke.py` covering: generator source file exists at the required path (Req 13.1), source decodes cleanly as UTF-8 (Req 13.5), `import pptx` succeeds (Req 13.2)
    - _Requirements: 13.1, 13.2, 13.5_

- [x] 9. Example-based structural and content tests
  - [x] 9.1 Write structural tests
    - Add `test_structure.py`: assert slide count == 7, slide order matches Req 1.2 (by title), slide width == 13.333 in, slide height == 7.5 in
    - _Requirements: 1.1, 1.2, 1.3_

  - [x] 9.2 Write per-slide literal content tests
    - Add `test_content.py` with example-based assertions: Slide 1 headline literal (Req 4.1) and supporting-line cap (Req 4.3); Slide 2 title literal and ≤3 bullets with three-idea keyword coverage (Req 5.1, 5.2, 5.3); Slide 3 reframe pair literals, `Core_Message` tagline verbatim, content-type noun coverage (Req 2.4, 6.1, 6.3); Slide 4 Heal-the-World framing, exactly 5 activity rows with keyword coverage, closing literal (Req 7.1, 7.2, 7.3); Slide 5 worldview literal, heal/cure motif, emphasis one-liner literal (Req 8.1, 8.2, 8.3); Slide 6 4-cell count and per-cell keyword coverage (Req 9.1); Slide 7 headline literal, sub-text literal, `Step` + QR placeholder + next-step line presence (Req 10.1, 10.2, 10.3, 10.4); product name and song title substring checks (Req 2.2, 2.3)
    - _Requirements: 2.2, 2.3, 2.4, 4.1, 4.3, 5.1, 5.2, 5.3, 6.1, 6.3, 7.1, 7.2, 7.3, 8.1, 8.2, 8.3, 9.1, 10.1, 10.2, 10.3, 10.4_

- [ ] 10. Structural property-based tests (Properties 4, 7, 8, 14)
  - [ ]* 10.1 Write property test for visual element presence and no pictures
    - **Property 4: Every slide has a visual element and no picture shapes**
    - **Validates: Requirements 3.4, 11.6**
    - Exhaustive iteration over the 7 built slides; assert at least one non-text decorative shape exists per slide (in addition to background) and zero shapes of type `PICTURE`
    - _Requirements: 3.4, 11.6_

  - [ ]* 10.2 Write property test for emphasis visual distinction
    - **Property 7: Emphasis elements are visually distinct from body**
    - **Validates: Requirements 6.2, 8.3, 10.3**
    - Exhaustive iteration over slides that declare `emphasis` (Slide 3 tagline, Slide 5 one-liner, Slide 7 brand `Step`); assert the emphasis run's font size is strictly greater than every non-title body run on the same slide AND its font color equals `ACCENT`
    - _Requirements: 6.2, 8.3, 10.3_

  - [ ]* 10.3 Write property test for Slide 6 icon adjacency
    - **Property 8: Every Slide 6 differentiator cell has an adjacent icon**
    - **Validates: Requirement 9.2**
    - Exhaustive iteration over the 4 Slide 6 cells; assert an icon-circle shape exists within 0.5 in horizontally and 0.3 in vertically of each cell's label text frame
    - _Requirements: 9.2_

  - [ ]* 10.4 Write property test for safe margin
    - **Property 14: Every text frame respects the 0.5-inch safe margin**
    - **Validates: Requirement 11.5**
    - Iterate over all text frames on all 7 slides; assert `left ≥ 0.5`, `top ≥ 0.5`, `left + width ≤ 13.333 - 0.5`, `top + height ≤ 7.5 - 0.5`
    - _Requirements: 11.5_

- [ ] 11. Visual design property-based tests (Properties 10, 11, 12, 13)
  - [ ]* 11.1 Write property test for background fill
    - **Property 10: Background fill is exactly the warm neutral on every slide**
    - **Validates: Requirement 11.1**
    - Exhaustive iteration over the 7 built slides; assert a full-bleed rectangle with solid fill RGB `#FAF7F2` exists on each
    - _Requirements: 11.1_

  - [ ]* 11.2 Write property test for palette-only colors
    - **Property 11: Only palette colors are used**
    - **Validates: Requirement 11.2**
    - Iterate over every shape solid fill and every text run font color across all 7 slides; assert each RGB belongs to `{ACCENT, BG, BODY, MUTED, ON_ACCENT}`
    - _Requirements: 11.2_

  - [ ]* 11.3 Write property test for title font size
    - **Property 12: Every slide title is rendered at 40 pt or larger**
    - **Validates: Requirement 11.3**
    - Exhaustive iteration over the 7 slides; assert the title text run's font size ≥ 40 pt
    - _Requirements: 11.3_

  - [ ]* 11.4 Write property test for body font size bounds
    - **Property 13: Body text font size stays within 18–28 pt**
    - **Validates: Requirement 11.4**
    - Iterate over every body text run (excluding title and emphasis runs) across all 7 slides; assert each font size is between 18 and 28 pt inclusive
    - _Requirements: 11.4_

- [ ] 12. Content integrity property-based tests (Properties 1, 9)
  - [ ]* 12.1 Write property test for Slide 6 cell word count
    - **Property 9: Every Slide 6 differentiator body is at most 16 words**
    - **Validates: Requirement 9.3**
    - Exhaustive iteration over the 4 Slide 6 cells; assert each cell body word count ≤ 16
    - _Requirements: 9.3_

  - [ ]* 12.2 Write property test for UTF-8 round trip
    - **Property 1: Text content survives UTF-8 round trip**
    - **Validates: Requirements 2.5, 2.1, 2.2, 2.3, 2.4**
    - Use `hypothesis.strategies.text(alphabet=VIETNAMESE_ALPHABET)` to generate ≥100 random Vietnamese strings; for each, run a write-string → save `.pptx` → read `.pptx` → compare harness and assert byte-exact equality; additionally assert every string field in `SLIDES` (title, subtitle, body items, emphasis, closing, notes) round-trips unchanged via the built pptx
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5_

- [x] 13. Integration tests
  - [x] 13.1 Write end-to-end, overwrite, and timing integration tests
    - Add `test_integration.py` with `test_generator_runs_end_to_end` (subprocess `python decks/general-audience-vi/generate_deck.py`; assert exit 0, file exists, size > 0, opens as valid `Presentation`), `test_generator_overwrites_existing_file` (pre-write a dummy file at the output path; assert post-run file is valid and differs), and `test_generator_completes_within_30s` (assert subprocess duration < 30 s)
    - _Requirements: 13.3, 13.4, 13.6_

- [x] 14. Generate and commit the output artifact
  - Run the generator script: `python decks/general-audience-vi/generate_deck.py`
  - Confirm `decks/general-audience-vi/step-pitch-vi.pptx` is produced, is non-empty, and opens via `python-pptx` as a valid `Presentation`
  - Confirm the committed artifact is present at the required path in the repository
  - _Requirements: 13.3, 13.4, 13.7_

- [x] 15. Final checkpoint — full test suite green
  - Run `pytest decks/general-audience-vi/tests --run` (single-execution mode; no watch) and confirm all non-optional tests pass
  - If any optional `*` property tests were implemented, run them as well and confirm they pass
  - Ensure all tests pass, ask the user if questions arise.

## Notes

- Tasks marked with `*` are optional and can be skipped for a faster MVP. In this plan the optional tasks are the property-based tests and the smoke tests; the example-based structural/content tests and integration tests are non-optional because they directly verify the requirements that define the deliverable.
- Property tests follow the PBT-alongside pattern from the design: structural properties about the `SLIDES` data (Properties 2, 3, 5, 6) are placed next to the data-model task so they catch errors the moment content is authored. Properties about the built `Presentation` are grouped by concern (structural, visual design, content integrity) and placed after the full build is in place so the `built_prs` fixture is meaningful.
- Each property-based test uses `hypothesis`, runs with ≥100 iterations or exhaustive enumeration over fixed populations, and carries a tag comment of the form `# Feature: general-audience-vi-pitch-deck, Property N: <title>`.
- Slide 4 intentionally carries 5 body items rather than the default cap of 4; this is the documented design override of Req 3.5 by Req 7.2 and is reflected in Property 5's `max_bullets_for_slide` parameter.
- The output `.pptx` is a committed artifact (Req 13.7); Task 14 is the explicit generate-and-commit step.

---

**Workflow complete.** This spec's design and planning artifacts are now in place (`requirements.md`, `design.md`, `tasks.md`). You can begin executing tasks by opening `tasks.md` and clicking **Start task** next to each item.
