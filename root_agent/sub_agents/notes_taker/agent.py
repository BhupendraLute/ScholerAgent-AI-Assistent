from . import prompt
from ...tools.pdf_writer import create_study_notes_pdf

from google.adk.agents import LlmAgent
from google.adk.tools.function_tool import FunctionTool

notes_taker_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='notes_taker_agent',
    description="An agent specialized in creating well structured study notes in PDF.",
    instruction=prompt.NOTES_TAKER_INSTRUCTION,
    tools=[FunctionTool(create_study_notes_pdf)]
)