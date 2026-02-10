import boto3
import os
import asyncio
from botocore.config import Config


async def generate_image_bedrock(
    prompt: str,
    model_id: str = "us.amazon.nova-2-omni-v1:0",
    aspect_ratio: str = "1:1",
    output_path: str = None,
) -> bytes:
    """Generate an image using Bedrock Nova 2 Omni model. Returns raw image bytes."""
    config = Config(read_timeout=300, retries={"max_attempts": 0})
    client = boto3.client("bedrock-runtime", region_name="us-east-1", config=config)

    full_prompt = f"{prompt} Make it {aspect_ratio}." if aspect_ratio else prompt

    request = {
        "modelId": model_id,
        "messages": [{"role": "user", "content": [{"text": full_prompt}]}],
        "inferenceConfig": {"temperature": 0, "topP": 1, "maxTokens": 10000},
    }

    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, lambda: client.converse(**request))

    if "output" in response and "message" in response["output"]:
        for block in response["output"]["message"].get("content", []):
            if "image" in block:
                image_bytes = block["image"]["source"]["bytes"]
                if output_path:
                    path = f"{output_path}/generated_image.png" if os.path.isdir(output_path) else output_path
                    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
                    with open(path, "wb") as f:
                        f.write(image_bytes)
                    print(f"Saved image to {path}")
                return image_bytes

    raise ValueError("No image generated in response")


if __name__ == "__main__":
    import time

    tick = time.time()
    result = asyncio.run(
        generate_image_bedrock("create an image of a lion", output_path="output/test_lion.png")
    )
    print(f"Generated {len(result)} bytes in {time.time() - tick:.1f}s")
