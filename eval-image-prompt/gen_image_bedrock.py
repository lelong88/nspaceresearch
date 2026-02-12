import boto3
import json
import os
import asyncio
from typing import Optional
from botocore.config import Config


async def generate_image_canvas(
    prompt: str,
    output_path: Optional[str] = None
) -> bytes:
    """Generate an image using Amazon Nova Canvas model."""
    config = Config(read_timeout=300, retries={"max_attempts": 0})
    client = boto3.client("bedrock-runtime", region_name="us-east-1", config=config)

    body = json.dumps({
        "taskType": "TEXT_IMAGE",
        "textToImageParams": {"text": prompt},
        "imageGenerationConfig": {"numberOfImages": 1, "quality": "standard"}
    })

    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(
        None, lambda: client.invoke_model(modelId="amazon.nova-canvas-v1:0", body=body)
    )

    result = json.loads(response["body"].read())
    import base64
    image_bytes = base64.b64decode(result["images"][0])

    if output_path:
        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
        with open(output_path, "wb") as f:
            f.write(image_bytes)

    return image_bytes


async def generate_image_bedrock(
    prompt: str,
    model_id: str = "us.amazon.nova-2-omni-v1:0",
    aspect_ratio: Optional[str] = "1:1",
    output_path: Optional[str] = None
) -> bytes:
    """Generate an image using Bedrock Nova 2 Omni model."""
    config = Config(read_timeout=300, retries={"max_attempts": 0})
    client = boto3.client("bedrock-runtime", region_name="us-east-1", config=config)

    full_prompt = f"{prompt} Make it {aspect_ratio}." if aspect_ratio else prompt

    request = {
        "modelId": model_id,
        "messages": [{"role": "user", "content": [{"text": full_prompt}]}],
        "inferenceConfig": {"temperature": 0, "topP": 1, "maxTokens": 10000}
    }

    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, lambda: client.converse(**request))

    if "output" in response and "message" in response["output"]:
        for block in response["output"]["message"].get("content", []):
            if "image" in block:
                image_bytes = block["image"]["source"]["bytes"]
                if output_path:
                    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
                    with open(output_path, "wb") as f:
                        f.write(image_bytes)
                return image_bytes

    raise ValueError("No image generated in response")


if __name__ == "__main__":
    result = asyncio.run(generate_image_canvas("create an image of a lion", output_path="test_lion_canvas.png"))
    print(f"Generated {len(result)} bytes")
