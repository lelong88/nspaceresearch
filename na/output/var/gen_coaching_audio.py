from dotenv import load_dotenv
load_dotenv()
import os, io, boto3

polly = boto3.client("polly", region_name="us-east-1")
CHUNK_SIZE = 2900  # stay under 3000 char limit

input_file = "output/var/var-report-3rd-draft-coaching.txt"
output_file = "output/var/var-report-3rd-draft-coaching.mp3"

text = open(input_file).read()

# Split on paragraph boundaries to stay under chunk size
paragraphs = text.split("\n\n")
chunks = []
current = ""
for p in paragraphs:
    if len(current) + len(p) + 2 > CHUNK_SIZE:
        if current:
            chunks.append(current.strip())
        current = p
    else:
        current = current + "\n\n" + p if current else p
if current.strip():
    chunks.append(current.strip())

print(f"Split into {len(chunks)} chunks")

audio_parts = []
for i, chunk in enumerate(chunks):
    print(f"Synthesizing chunk {i+1}/{len(chunks)} ({len(chunk)} chars)...")
    res = polly.synthesize_speech(
        Text=chunk, OutputFormat="mp3", VoiceId="Matthew", Engine="generative"
    )
    audio_parts.append(res["AudioStream"].read())

os.makedirs(os.path.dirname(output_file), exist_ok=True)
with open(output_file, "wb") as f:
    for part in audio_parts:
        f.write(part)

print(f"Saved: {output_file}")
