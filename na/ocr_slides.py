import os, base64, io
from pathlib import Path
from dotenv import load_dotenv
import requests
from PIL import Image

load_dotenv()

API_URL = os.environ["OPENAI_COMPATIBLE_URL"]
API_KEY = os.environ["OPENAI_KEY"]
MODEL = "sonnet"

IMAGES_DIR = Path("images-var")
SLIDES_DIR = Path("slides-var")

CONTEXT = Path("summary-mac.md").read_text()

SYSTEM_PROMPT = f"""You are an OCR assistant. You will be given a photo of a presentation slide displayed on a laptop screen.
Extract ALL text content from the slide and format it as clean markdown.

Use this context about the presentation to improve accuracy of domain-specific terms:

{CONTEXT}

Rules:
- Output ONLY the markdown content, no preamble
- For tables, use markdown table syntax
- For diagrams/flowcharts, describe the structure with text and arrows
- Preserve Vietnamese diacritics accurately
- Note any visual elements (maps, charts, icons) in italics
- Start with the slide title as a # heading
- Add ![Source](../images/FILENAME) after the title
"""

MAX_BYTES = 4_500_000  # stay under 5MB

def encode_image(path):
    img = Image.open(path)
    # Resize if needed
    max_dim = 1600
    if max(img.size) > max_dim:
        img.thumbnail((max_dim, max_dim), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=85)
    if buf.tell() > MAX_BYTES:
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=60)
    return base64.b64encode(buf.getvalue()).decode()

def ocr_image(img_path):
    b64 = encode_image(img_path)
    resp = requests.post(
        f"{API_URL}/chat/completions",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={
            "model": MODEL,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": [
                    {"type": "text", "text": f"OCR this slide image. The source filename is {img_path.name}"},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}}
                ]}
            ]
        },
        timeout=120
    )
    if not resp.ok:
        raise Exception(f"{resp.status_code}: {resp.text[:300]}")
    return resp.json()["choices"][0]["message"]["content"]

def get_todo():
    """Compare source images dir to target slides dir to find unprocessed files."""
    done = {f.stem for f in SLIDES_DIR.glob("*.md")}
    return sorted(f for f in IMAGES_DIR.glob("*.jpg") if f.stem not in done)

def main():
    all_imgs = sorted(IMAGES_DIR.glob("*.jpg"))
    todo = get_todo()
    done = len(all_imgs) - len(todo)
    print(f"Total: {len(all_imgs)}, Done: {done}, Todo: {len(todo)}")

    for img_path in todo:
        md_path = SLIDES_DIR / (img_path.stem + ".md")
        print(f"Processing {img_path.name}...", end=" ", flush=True)
        try:
            content = ocr_image(img_path)
            md_path.write_text(content + "\n")
            print(f"OK ({len(content)} chars)")
        except Exception as e:
            print(f"ERROR: {e}")

    done = len(all_imgs) - len(get_todo())
    print(f"\nFinished. Done: {done}/{len(all_imgs)}")

if __name__ == "__main__":
    main()
