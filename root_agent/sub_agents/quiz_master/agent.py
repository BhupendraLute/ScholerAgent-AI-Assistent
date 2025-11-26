from . import prompt

from google.adk.agents import LlmAgent

quiz_master_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="quiz_master_agent",
    description="An agent specialized in conducting quizzes and gathering information from various sources.",
    instruction=prompt.QUIZ_MASTER_AGENT_INSTRUCTIONS,
    tools=[]
)