from crewai import Agent
from tools.search_tool import SearchTool

def create_resource_agent():
    search_tool = SearchTool()  # Create an instance of the SearchTool
    return Agent(
        role="Resource Collector",
        goal="Collect datasets, articles, and resources for the generated use cases.",
        backstory="You are an expert in finding and organizing resources for AI projects.",
        tools=[search_tool],  # Use the search tool
        verbose=True
    )