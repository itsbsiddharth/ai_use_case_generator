from crewai import Agent
from tools.search_tool import SearchTool

def create_research_agent():
    search_tool = SearchTool()  # Create an instance of the SearchTool
    return Agent(
        role="Industry Researcher",
        goal="Research the industry and company's key offerings and strategic focus areas.",
        backstory="You are an expert in market research and industry analysis.",
        tools=[search_tool],  # Use the search tool
        verbose=True
    )