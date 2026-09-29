from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from tavily import TavilyClient
from langchain_tavily import TavilySearch

load_dotenv()

tavily=TavilyClient()
@tool
def search(query:str)->str:
    """
    Tool that searches the internet and return the results
    Args:
    query: the query to search
    Returns:
    The search result
    """
    print(f"Searching :{query}")
    return tavily.search(query=query)

llm=ChatGoogleGenerativeAI(model="gemini-3.8-flash", temperature=0)
tools=[TavilySearch()]
agent=create_agent(model=llm, tools=tools)

def main():
    print("Welcome to the Search Agent!")
    result=agent.invoke({"messages":HumanMessage(content="search for 3 job posting on langchain for ai engineer in dhaka bangladesh")})
    print(f"Result: {result}")


if __name__=="__main__":
    main()