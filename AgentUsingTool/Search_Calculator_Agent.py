from langchain.agents import Tool,initialize_agent
from langchain.agents.agent_types import AgentType
from langchain_community.tools import DuckDuckGoSearchRun,Tool
from langchain_openai import ChatOpenAI
from langchain_experimental.tools.python.tool import PythonREPLTool
from dotenv import load_dotenv
import os

api_key = os.getenv("OPENAI_API_KEY")
load_dotenv()
llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=api_key, temperature=0.7)

search_tool = DuckDuckGoSearchRun() 
calc_tool = PythonREPLTool()

tools = [
    Tool(
        name="Search",
        func=search_tool.run,
        description="Useful for when you need to answer questions about current events. Input should be a search query."
    ),
    Tool(
        name="Calculator",
        func=calc_tool.run,
        description="Useful for when you need to perform calculations. Input should be a valid Python expression."
    )
]

# Initialize Agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Ask Question
question = "What is the square root of the population of Pakistan divided by 2?"
response = agent.invoke(question)
print("Response:", response)
