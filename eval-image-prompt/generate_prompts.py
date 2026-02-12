import asyncio
import json
import os
from llm_client import chat
from gen_word_domain_prompt import get_words_domain
from image_generation_prompt import IMAGE_GENERATE_PROMPT_V2


async def generate_prompt_for_word(word: str, lang: str, index: int, semaphore: asyncio.Semaphore):
    """Generate image prompt for a single word and save to file."""
    folder = f"generated-prompts/{lang}/{index}"
    if os.path.exists(f"{folder}/prompt.txt"):
        return  # Skip if already exists
    
    async with semaphore:
        # Get domain-prefixed word
        result = await get_words_domain([word], "")
        domain_word = f"{result[0]['domain']}:{word}" if result[0]['domain'] else word
        
        # Generate image prompt
        image_prompt = await chat(domain_word, system=IMAGE_GENERATE_PROMPT_V2)
        
        # Save to file
        os.makedirs(folder, exist_ok=True)
        with open(f"{folder}/prompt.txt", "w") as f:
            f.write(image_prompt)
        
        print(f"[{lang}/{index}] {word} -> {domain_word}")


async def main():
    with open("vocab_test_list.json") as f:
        vocab = json.load(f)
    
    semaphore = asyncio.Semaphore(10)  # Limit concurrent requests
    tasks = []
    for lang in ["en", "zh"]:
        for i, word in enumerate(vocab[lang], 1):
            tasks.append(generate_prompt_for_word(word, lang, i, semaphore))
    
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv(override=True)
    asyncio.run(main())
