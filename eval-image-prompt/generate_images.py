import asyncio
import os
from gen_image_bedrock import generate_image_bedrock, generate_image_canvas


async def generate_images_for_prompt(folder: str, semaphore: asyncio.Semaphore):
    """Generate omni and canvas images for a prompt folder."""
    prompt_file = f"{folder}/prompt.txt"
    if not os.path.exists(prompt_file):
        return
    
    with open(prompt_file) as f:
        prompt = f.read().strip()
    
    async with semaphore:
        if not os.path.exists(f"{folder}/omni.png"):
            try:
                await generate_image_bedrock(prompt, output_path=f"{folder}/omni.png")
            except Exception as e:
                print(f"Failed omni for {folder}: {e}")
        
        if not os.path.exists(f"{folder}/canvas.png"):
            try:
                await generate_image_canvas(prompt, output_path=f"{folder}/canvas.png")
            except Exception as e:
                print(f"Failed canvas for {folder}: {e}")
        
        print(f"Done {folder}")


async def main():
    semaphore = asyncio.Semaphore(5)
    tasks = []
    
    for lang in ["en", "zh"]:
        for i in range(1, 101):
            folder = f"generated-prompts/{lang}/{i}"
            tasks.append(generate_images_for_prompt(folder, semaphore))
    
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
