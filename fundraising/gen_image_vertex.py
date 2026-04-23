import asyncio
import json
import os
import random
from typing import Optional

from dotenv import load_dotenv
from google import genai as google_genai
from google.genai import types
from google.oauth2.service_account import Credentials

load_dotenv(override=False)

_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
_LOCATION = os.environ.get("VERTEX_LOCATION", "global")
_MODEL = "gemini-3.1-flash-image-preview"

# Service account key files to rotate between (1/3 chance each)
_SERVICE_ACCOUNT_FILES = [
    "quan_serviceAccountKey.json"
]

# Lazy-initialized client pool keyed by filename
_clients: dict[str, google_genai.Client] = {}


def _get_client() -> google_genai.Client:
    """Return a random client from the pool, creating it on first use."""
    sa_file = random.choice(_SERVICE_ACCOUNT_FILES)
    if sa_file not in _clients:
        path = os.path.join(_BASE_DIR, sa_file)
        with open(path) as f:
            project_id = json.load(f)["project_id"]
        scopes = ["https://www.googleapis.com/auth/cloud-platform"]
        credentials = Credentials.from_service_account_file(path, scopes=scopes)
        _clients[sa_file] = google_genai.Client(
            vertexai=True,
            project=project_id,
            location=_LOCATION,
            credentials=credentials,
        )
    return _clients[sa_file]


async def generate_image_vertex(
    prompt: str,
    aspect_ratio: Optional[str] = "1:1",
) -> bytes:
    """Generate an image using Gemini 3.1 Flash Image Preview on Vertex AI.

    Drop-in replacement for generate_image_bedrock — same signature, returns raw image bytes.
    """
    client = _get_client()

    # Vertex AI doesn't support image_config for this preview model,
    # so we embed the aspect ratio in the prompt (same approach as bedrock).
    full_prompt = prompt
    if aspect_ratio and aspect_ratio != "1:1":
        full_prompt = f"{prompt} Make it {aspect_ratio} aspect ratio."

    config = types.GenerateContentConfig(
        response_modalities=["IMAGE"],
    )

    # Run the synchronous SDK call in an executor so we don't block the event loop
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(
        None,
        lambda: client.models.generate_content(
            model=_MODEL,
            contents=[full_prompt],
            config=config,
        ),
    )

    # Extract image bytes from the response
    for part in response.parts:
        if part.inline_data is not None:
            return part.inline_data.data

    raise ValueError("No image generated in Vertex AI response")


if __name__ == "__main__":
    import time

    tick = time.time()
    result = asyncio.run(
        generate_image_vertex(
            "A cheerful stylized person sitting on a vintage suitcase, warm amber palette, editorial illustration style.",
            aspect_ratio="2:1",
        )
    )
    print(f"Generated {len(result)} bytes in {time.time() - tick:.1f}s")
