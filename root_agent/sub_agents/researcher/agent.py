from . import prompt
from ...tools import read_file_universal

from google.adk.agents import LlmAgent
from google.adk.tools.function_tool import FunctionTool

researcher_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='researcher_agent',
    description="An agent specialized in conducting research and gathering information on various study topics.",
    instruction=prompt.RESEARCHER_AGENT_INSTRUCTION,
    tools=[FunctionTool(read_file_universal)]
)