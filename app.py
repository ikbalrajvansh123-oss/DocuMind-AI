from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper

# Load environment variables
load_dotenv()

# Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    temperature=0.3
)

# Free Search Wrapper
search = DuckDuckGoSearchAPIWrapper()

tools = [
    Tool(
        name="Search",
        func=search.run,
        description="Useful for searching real-time information from the internet"
    )
]

# Create Agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Run Agent
response = agent.run("Latest AI research trends in 2026?")
print("\nFinal Answer:\n")
print(response)