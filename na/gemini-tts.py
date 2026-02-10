from dotenv import load_dotenv
load_dotenv()
import os, sys, subprocess, tempfile, base64
from pathlib import Path
import requests

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

def generate_tts(text: str, output_path: str):
    prompt = f"Read this text at normal speed, speaking Vietnamese, and English words in their original languages:\n{text}"

    res = requests.post(
        f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-pro-preview-tts:generateContent?key={GEMINI_API_KEY}",
        headers={"Content-Type": "application/json"},
        json={
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {
                "responseModalities": ["AUDIO"],
                "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": "Kore"}}},
            },
        },
    )

    data = res.json()
    if "error" in data:
        raise Exception(data["error"]["message"])

    audio_data = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("inlineData", {}).get("data")
    if not audio_data:
        raise Exception("No audio data received")

    tmp = tempfile.mktemp()
    pcm_path = f"{tmp}.pcm"
    with open(pcm_path, "wb") as f:
        f.write(base64.b64decode(audio_data))
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    subprocess.run(["ffmpeg", "-y", "-f", "s16le", "-ar", "24000", "-ac", "1", "-i", pcm_path, output_path], capture_output=True)
    os.unlink(pcm_path)
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python gemini-tts.py <input_file.txt>")
        sys.exit(1)
    input_file = Path(sys.argv[1])
    text = input_file.read_text()
    output_path = os.path.join("output", input_file.with_suffix(".mp3").name)
    generate_tts(text, output_path)
