from crewai.tools import BaseTool
from tavily import TavilyClient
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

class SearchTool(BaseTool):
    name: str = "Search Tool"  # Add type annotation
    description: str = "A tool to search the web for information about a company or industry."  # Add type annotation

    def _run(self, query: str) -> str:
        # Get the Tavily API key from the environment
        tavily_api_key = os.getenv("TAVILY_API_KEY")
        if not tavily_api_key:
            raise ValueError("Tavily API key not found in environment variables.")

        tavily = TavilyClient(api_key=tavily_api_key)
        response = tavily.search(query=query, max_results=5)
        return str(response["results"])  # Ensure the result is a string