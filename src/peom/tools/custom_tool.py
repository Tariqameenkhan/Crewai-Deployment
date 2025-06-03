from crewai.tools import BaseTool

class CodeCheckerTool(BaseTool):
    name: str = "Python Code Checker"
    description: str = "Checks Python code for syntax errors and basic quality issues"

    def _run(self, code: str) -> str:
        """Check Python code syntax and basic structure"""
        # First check if this is a rejection case
        if "cannot generate" in code.lower() or "outside my scope" in code.lower():
            return "Rejection case detected - no need for further checking"
            
        if not any(kw in code.lower() for kw in ['def ', 'import ', 'class ', 'lambda ']):
            return "Error: This doesn't appear to be valid Python code"
        
        try:
            compile(code, "<string>", "exec")
            return "Code passed basic checks!"
        except Exception as e:
            return f"Error found: {str(e)}"

check_code = CodeCheckerTool()