import os, base64, io
from pathlib import Path
from dotenv import load_dotenv
import requests
from PIL import Image

load_dotenv()

API_URL = os.environ["OPENAI_COMPATIBLE_URL"]
API_KEY = os.environ["OPENAI_KEY"]
MODEL = "sonnet"

IMAGES_DIR = Path("images")
SLIDES_DIR = Path("slides")
PROGRESS = SLIDES_DIR / "progress.txt"

CONTEXT = Path("summary.md").read_text()

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

def load_progress():
    lines = PROGRESS.read_text().strip().split("\n")
    status = {}
    for line in lines:
        parts = line.strip().split(None, 1)
        if len(parts) == 2 and parts[0] in ("DONE", "SKIP"):
            status[parts[1]] = parts[0]
        elif len(parts) == 2 and parts[0] == "ERROR":
            status[parts[1]] = "TODO"  # retry errors
        elif len(parts) == 1:
            status[parts[0]] = "TODO"
    return status

def save_progress(status):
    lines = []
    for fname, state in status.items():
        lines.append(fname if state == "TODO" else f"{state} {fname}")
    PROGRESS.write_text("\n".join(lines) + "\n")

def main():
    status = load_progress()
    todo = [f for f, s in status.items() if s == "TODO"]
    print(f"Total: {len(status)}, Done: {sum(1 for s in status.values() if s=='DONE')}, Todo: {len(todo)}")

    for fname in todo:
        img_path = IMAGES_DIR / fname
        md_path = SLIDES_DIR / fname.replace(".jpg", ".md")
        print(f"Processing {fname}...", end=" ", flush=True)
        try:
            content = ocr_image(img_path)
            md_path.write_text(content + "\n")
            status[fname] = "DONE"
            save_progress(status)
            print(f"OK ({len(content)} chars)")
        except Exception as e:
            print(f"ERROR: {e}")
            status[fname] = "ERROR"
            save_progress(status)

    done = sum(1 for s in status.values() if s == "DONE")
    print(f"\nFinished. Done: {done}/{len(status)}")

if __name__ == "__main__":
    main()
