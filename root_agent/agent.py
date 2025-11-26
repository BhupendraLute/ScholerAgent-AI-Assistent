from . import prompt

from google.adk.agents import LlmAgent
from root_agent.sub_agents.researcher.agent import researcher_agent
from root_agent.sub_agents.quiz_master.agent import quiz_master_agent
from root_agent.sub_agents.notes_taker.agent import notes_taker_agent


root_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="The ",
    instruction=prompt.ROOT_AGENT_INSTRUCTIONS,
    sub_agents=[researcher_agent, quiz_master_agent, notes_taker_agent],
)