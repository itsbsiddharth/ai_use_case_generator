from crewai import Agent

def create_use_case_agent():
    return Agent(
        role="Use Case Generator",
        goal="Generate relevant AI and GenAI use cases for the company.",
        backstory="You are an AI expert specializing in identifying use cases for various industries.",
        verbose=True
    )