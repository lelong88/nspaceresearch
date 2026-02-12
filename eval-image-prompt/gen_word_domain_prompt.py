import asyncio
import json
from typing import List, Dict
from llm_client import chat
from word_domain_prompt import WORD_DOMAIN_PROMPT

async def get_words_domain(words: List[str], context: str) -> List[Dict[str, str]]:
    try:
        prompt = json.dumps({"terms": words, "context": context})
        output = await chat(prompt, system=WORD_DOMAIN_PROMPT)
        output = output.strip().removeprefix("```json").removesuffix("```").strip()
        result = json.loads(output)["result"]
        return [
            {"word": word, "domain": result[i].split(":")[0] if len(result) > i else None}
            for i, word in enumerate(words)
        ]
    except Exception as e:
        print(e)
        return [{"word": word, "domain": None} for word in words]


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv(override=True)
    from llm_client import client
    import os
    client.api_key = os.environ.get("MEOMAP_API_KEY", "")
    result = asyncio.run(
        get_words_domain(
            ["litter", "street", "apartment", "city"],
            "We have a cat and a dog, and we need to buy some litter for them.",
        )
    )
    print(result)
