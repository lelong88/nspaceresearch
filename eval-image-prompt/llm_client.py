import os
import base64
import asyncio
from io import BytesIO
from openai import AsyncOpenAI
from PIL import Image


client = AsyncOpenAI(
    base_url="https://litellm.meomap.blog/v1",
    api_key=os.environ.get("MEOMAP_API_KEY", "")
)


def resize_image_if_needed(img_path: str, max_bytes: int = 4_000_000) -> str:
    """Resize image if it exceeds max_bytes, return base64."""
    img = Image.open(img_path)
    
    buf = BytesIO()
    img.save(buf, format="PNG")
    data = buf.getvalue()
    
    while len(data) > max_bytes:
        img = img.resize((int(img.width * 0.7), int(img.height * 0.7)), Image.LANCZOS)
        buf = BytesIO()
        img.save(buf, format="PNG")
        data = buf.getvalue()
    
    return base64.b64encode(data).decode()


async def chat(prompt: str, model: str = "opus", system: str = None, images: list = None) -> str:
    """Send a chat completion request and return the response text."""
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    
    if images:
        content = [{"type": "text", "text": prompt}]
        for img_path in images:
            b64 = resize_image_if_needed(img_path)
            content.append({"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64}"}})
        messages.append({"role": "user", "content": content})
    else:
        messages.append({"role": "user", "content": prompt})

    response = await client.chat.completions.create(model=model, messages=messages)
    return response.choices[0].message.content


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv(override=False)
    result = asyncio.run(chat("Say hello in 5 words"))
    print(result)
