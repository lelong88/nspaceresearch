from dotenv import load_dotenv
load_dotenv()
import os, sys
from pathlib import Path
import boto3

polly = boto3.client("polly", region_name="us-east-1")


def generate_tts(text: str, output_path: str, voice_id: str = "Matthew", engine: str = "generative"):
    res = polly.synthesize_speech(Text=text, OutputFormat="mp3", VoiceId=voice_id, Engine=engine)
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "wb") as f:
        f.write(res["AudioStream"].read())
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python polly-tts.py <input_file.txt>")
        sys.exit(1)
    input_file = Path(sys.argv[1])
    text = input_file.read_text()
    output_path = os.path.join("output", input_file.with_suffix(".mp3").name)
    generate_tts(text, output_path)
