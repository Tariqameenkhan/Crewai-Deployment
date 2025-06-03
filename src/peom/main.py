from crewai.flow import Flow, start
from peom.crews.poem_crew.poem_crew import DevCrew  # Fixed import path


class DevFlow(Flow):
    @start()
    def run_dev_crew(self) -> str:
        """Execute the development crew workflow with user input."""
        print("\n** Python Development Assistant **")
        user_problem = input("Please describe your Python coding problem or requirement:\n> ").strip()
        
        # Enhanced validation with more specific Python indicators
        python_indicators = [
            'python', 'def ', 'import ', 'class ', 'lambda ', 
            'django', 'fastapi', 'flask', 'pandas', 'numpy'
        ]
        
        if not any(indicator in user_problem.lower() for indicator in python_indicators):
            return (
                "🚫 I specialize exclusively in Python development. I cannot help with:\n"
                "- Java/JavaScript/C++/other languages\n"
                "- System administration\n"
                "- Non-Python frameworks\n\n"
                "Please provide a Python-specific request or ask about:\n"
                "- Python code generation\n"
                "- Python code review\n"
                "- Python debugging\n"
                "- Python framework help (Django, FastAPI, etc)"
            )
            
        return DevCrew().crew().kickoff(
            inputs={"problem": user_problem}
        )

def kickoff() -> str:
    """Entry point for the development flow."""
    dev_flow = DevFlow()
    return dev_flow.kickoff()