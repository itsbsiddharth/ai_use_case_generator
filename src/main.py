from crewai import Crew, Task
from agents.research_agent import create_research_agent
from agents.use_case_agent import create_use_case_agent
from agents.resource_agent import create_resource_agent

def crew(company_name: str, industry: str):
    # Create agents
    research_agent = create_research_agent()
    use_case_agent = create_use_case_agent()
    resource_agent = create_resource_agent()

    # Define tasks
    research_task = Task(
        description=f"Research the {industry} industry and {company_name}'s key offerings.",
        expected_output=f"A detailed report on the {industry} industry and {company_name}'s key offerings.",
        agent=research_agent
    )

    use_case_task = Task(
        description=f"Generate AI use cases for {company_name} based on the research.",
        expected_output=f"A list of relevant AI and GenAI use cases for {company_name}.",
        agent=use_case_agent,
        context=[research_task]  # Use the output of research_task as context
    )

    resource_task = Task(
        description=f"Collect resources for the generated use cases.",
        expected_output=f"A list of relevant datasets, articles, and resources for the use cases.",
        agent=resource_agent,
        context=[use_case_task]  # Use the output of use_case_task as context
    )

    # Create crew
    crew = Crew(
        agents=[research_agent, use_case_agent, resource_agent],
        tasks=[research_task, use_case_task, resource_task]
    )

    # Run the crew
    result = crew.kickoff()

    # Return structured output
    return {
        "tasks_output": [
            research_task.output,
            use_case_task.output,
            resource_task.output
        ]
    }