import asyncio
import os
from dotenv import load_dotenv
from browser_use import Agent
from browser_use.llm.openai.like import ChatOpenAILike

load_dotenv()

llm = ChatOpenAILike(
    model="sonnet",
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

agent = Agent(
    task="Go to https://news.ycombinator.com and find the top 3 stories. Return their titles and links.",
    llm=llm,
)

asyncio.run(agent.run())
