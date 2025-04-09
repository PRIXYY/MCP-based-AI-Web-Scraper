from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
from pydantic import SecretStr
import os
from dotenv import load_dotenv

load_dotenv()
import asyncio
api_key = os.getenv("GEMINI_API_KEY")

# Initialize the model
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(os.getenv('GEMINI_API_KEY')))

# Create agent with the model

async def main():
    agent = Agent(
        task="search for a white shirt on amazon.in and get me an average price",
        llm=llm
    )
    result = await agent.run()
    print(result)

asyncio.run(main())