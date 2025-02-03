from tavily import TavilyClient

def test_tavily():
    tavily = TavilyClient(api_key="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")
    response = tavily.search(query="AI in steel industry", max_results=5)
    print(response)

if __name__ == "__main__":
    test_tavily()