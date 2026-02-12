import asyncio
import os
import random
from llm_client import chat

JUDGE_PROMPT = """You are judging which image better matches the given prompt.

Prompt: {prompt}

Image A and Image B are shown above. Which image better represents the prompt?
Reply with only "A" or "B"."""


async def judge_folder(folder: str, semaphore: asyncio.Semaphore):
    """Judge which image is better for a folder."""
    if os.path.exists(f"{folder}/winner.txt"):
        return
    
    prompt_file = f"{folder}/prompt.txt"
    if not os.path.exists(prompt_file):
        return
    
    with open(prompt_file) as f:
        prompt = f.read().strip()
    
    # Randomize order
    if random.random() < 0.5:
        images = [f"{folder}/omni.png", f"{folder}/canvas.png"]
        mapping = {"A": "omni", "B": "canvas"}
    else:
        images = [f"{folder}/canvas.png", f"{folder}/omni.png"]
        mapping = {"A": "canvas", "B": "omni"}
    
    async with semaphore:
        try:
            result = await chat(JUDGE_PROMPT.format(prompt=prompt), images=images)
            choice = result.strip().upper()
            winner = mapping.get(choice[0] if choice else "A", "omni")
            with open(f"{folder}/winner.txt", "w") as f:
                f.write(winner)
            print(f"{folder}: {winner}")
        except Exception as e:
            print(f"Failed {folder}: {e}")


async def main():
    semaphore = asyncio.Semaphore(5)
    tasks = []
    
    for lang in ["en", "zh"]:
        for i in range(1, 101):
            folder = f"generated-prompts/{lang}/{i}"
            if os.path.isdir(folder):
                tasks.append(judge_folder(folder, semaphore))
    
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv(override=True)
    asyncio.run(main())
