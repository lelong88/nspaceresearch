import os, time, glob
from pathlib import Path
from dotenv import load_dotenv
import requests

load_dotenv()

API = "https://api.soniox.com"
KEY = os.environ["SONIOX_API_KEY"]
HDR = {"Authorization": f"Bearer {KEY}"}

AUDIO_DIR = Path("meeting-audios")
OUT_DIR = Path("meeting-audio-transcripts")
OUT_DIR.mkdir(exist_ok=True)

CONTEXT_TEXT = Path("summary.md").read_text()
CONTEXT_TERMS = [
    "MAC", "Manulife Agency Center", "Branch Model", "General Agency",
    "SM", "SSM", "Sales Manager", "Senior Sales Manager",
    "UM", "Unit Manager", "RH", "Regional Head",
    "DRD", "AVP", "GTF", "Growth Task Force",
    "FYP", "First Year Premium", "MOC", "maintenance of contract",
    "CE", "controllable expenses", "PRE", "production-related expense",
    "MAA", "monthly active agent", "1mAA",
    "office setup", "monthly office allowance",
    "big MAC", "small MAC", "internal MAC", "GTF MAC",
    "EMT", "pilot phase", "recruitment bonus",
]

EXTENSIONS = {".m4a", ".mp3", ".mp4", ".wav", ".flac", ".ogg", ".aac", ".webm", ".amr", ".aiff", ".asf"}


def transcribe(audio_path: Path) -> str:
    name = audio_path.stem
    print(f"\n[{name}] Uploading...")
    with open(audio_path, "rb") as f:
        r = requests.post(f"{API}/v1/files", headers=HDR, files={"file": f})
    r.raise_for_status()
    file_id = r.json()["id"]

    print(f"[{name}] Creating transcription...")
    r = requests.post(f"{API}/v1/transcriptions", headers=HDR, json={
        "model": "stt-async-v3",
        "language_hints": ["vi"],
        "file_id": file_id,
        "context": {
            "general": [
                {"key": "domain", "value": "Insurance"},
                {"key": "topic", "value": "Manulife Agency Center (MAC) scheme"},
                {"key": "organization", "value": "Manulife Vietnam"},
            ],
            "text": CONTEXT_TEXT,
            "terms": CONTEXT_TERMS,
        },
    })
    r.raise_for_status()
    tid = r.json()["id"]

    print(f"[{name}] Waiting...", end="", flush=True)
    while True:
        r = requests.get(f"{API}/v1/transcriptions/{tid}", headers=HDR)
        r.raise_for_status()
        status = r.json()["status"]
        if status == "completed":
            break
        if status == "error":
            raise Exception(r.json().get("error_message", "Unknown error"))
        print(".", end="", flush=True)
        time.sleep(2)
    print(" done")

    r = requests.get(f"{API}/v1/transcriptions/{tid}/transcript", headers=HDR)
    r.raise_for_status()
    text = "".join(t["text"] for t in r.json()["tokens"]).strip()

    # cleanup
    requests.delete(f"{API}/v1/transcriptions/{tid}", headers=HDR)
    requests.delete(f"{API}/v1/files/{file_id}", headers=HDR)

    return text


def main():
    files = sorted(f for f in AUDIO_DIR.iterdir() if f.suffix.lower() in EXTENSIONS)
    if not files:
        print("No audio files found in meeting-audios/")
        return

    print(f"Found {len(files)} audio file(s)")
    for audio_path in files:
        out_path = OUT_DIR / (audio_path.stem + ".txt")
        if out_path.exists():
            print(f"Skipping {audio_path.name} (already transcribed)")
            continue
        try:
            text = transcribe(audio_path)
            out_path.write_text(text)
            print(f"[{audio_path.stem}] Saved ({len(text)} chars)")
        except Exception as e:
            print(f"[{audio_path.stem}] ERROR: {e}")

    print("\nDone.")


if __name__ == "__main__":
    main()
