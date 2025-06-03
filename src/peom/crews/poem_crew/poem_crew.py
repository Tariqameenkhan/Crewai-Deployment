from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from ...tools.custom_tool import check_code  # Import the custom tool



@CrewBase
class DevCrew:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def python_developer_expert_1(self) -> Agent:
        return Agent(
            config=self.agents_config["python_developer_expert_1"],
            tools=[check_code],
            function=lambda problem: (
                "I specialize exclusively in Python development. Please provide:\n"
                "- Python code to write\n"
                "- Python code to review\n"
                "- Python-related questions\n\n"
                "For your request: '{problem}', I can only help if it's Python-related."
                if not any(kw in problem.lower() for kw in ['python', 'def ', 'import ', 'class '])
                else problem
            )
        )
    
    @agent
    def python_developer_expert_2(self) -> Agent:
        return Agent(
            config=self.agents_config["python_developer_expert_2"],
            tools=[check_code],
            function=lambda problem: (
                "As a Python Code Reviewer, I only handle:\n"
                "- Python code optimization\n"
                "- Adding type hints\n"
                "- Writing docstrings\n"
                "- Creating pytest tests\n\n"
                "Your request doesn't appear to be Python-related."
                if not any(kw in problem.lower() for kw in ['python', 'def ', 'import ', 'class '])
                else problem
            )
        )

    @task
    def write_python_code(self) -> Task:
        return Task(
            config=self.tasks_config["write_python_code"],
            tools=[check_code],
            function=lambda problem: (
                "This task only writes Python code. Please provide a Python-related requirement."
                if not any(kw in problem.lower() for kw in ['python', 'def ', 'import ', 'class '])
                else problem
            )
        )
    
    @task
    def review_python_code(self) -> Task:
        return Task(
            config=self.tasks_config["review_python_code"],
            tools=[check_code],
            function=lambda problem: (
                "This task only reviews Python code. Please provide Python code to review."
                if not any(kw in problem.lower() for kw in ['python', 'def ', 'import ', 'class '])
                else problem
            )
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Development Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )