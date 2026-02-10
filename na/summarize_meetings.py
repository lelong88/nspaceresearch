import os
from pathlib import Path
from dotenv import load_dotenv
import requests

load_dotenv()

API_URL = os.environ["OPENAI_COMPATIBLE_URL"]
API_KEY = os.environ["OPENAI_KEY"]
MODEL = "sonnet"

IN_DIR = Path("meeting-audio-transcripts-var")
OUT_DIR = Path("meeting-audio-transcript-summaries-var")
OUT_DIR.mkdir(exist_ok=True)

CONTEXT = Path("summary-mac.md").read_text()
GLOSSARY = Path("glossary.md").read_text()

SYSTEM_PROMPT = f"""You are a meeting summarizer for Manulife Vietnam's agency compensation team.
Use this background context to understand domain terms:

{CONTEXT}

Use this glossary for accurate terminology:

{GLOSSARY}

Given a Vietnamese meeting transcript, produce a structured summary in Vietnamese with:
1. **Tổng quan cuộc họp** - một đoạn ngắn về nội dung thảo luận
2. **Các điểm thảo luận chính** - bullet points các chủ đề chính
3. **Quyết định đã đưa ra** - các kết luận hoặc thỏa thuận
4. **Action Items** - các task cụ thể được giao, kèm người phụ trách nếu có
5. **Câu hỏi chưa giải quyết** - các vấn đề cần follow-up
6. **Số liệu/Dữ liệu quan trọng** - các con số, ngày tháng, metrics cụ thể được đề cập

Viết bằng tiếng Việt. Giữ nguyên các thuật ngữ tiếng Anh gốc (ví dụ: MAC, FYP, GTF, SM, office setup, monthly office allowance, catchup, recruitment bonus, etc.). Giữ nguyên tất cả số liệu cụ thể."""


def summarize(transcript: str) -> str:
    r = requests.post(
        f"{API_URL}/chat/completions",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={
            "model": MODEL,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Summarize this meeting transcript:\n\n{transcript}"},
            ],
        },
        timeout=120,
    )
    if not r.ok:
        raise Exception(f"{r.status_code}: {r.text[:300]}")
    return r.json()["choices"][0]["message"]["content"]


def main():
    files = sorted(IN_DIR.glob("*.txt"))
    if not files:
        print("No transcripts found in meeting-audio-transcripts/")
        return

    print(f"Found {len(files)} transcript(s)")
    for txt_path in files:
        out_path = OUT_DIR / (txt_path.stem + ".md")
        if out_path.exists():
            print(f"Skipping {txt_path.name} (already summarized)")
            continue
        print(f"Summarizing {txt_path.name}...", end=" ", flush=True)
        try:
            transcript = txt_path.read_text()
            summary = summarize(transcript)
            out_path.write_text(summary + "\n")
            print(f"OK ({len(summary)} chars)")
        except Exception as e:
            print(f"ERROR: {e}")

    print("Done.")


if __name__ == "__main__":
    main()
