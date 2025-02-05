from langchain_community.agent_toolkits.load_tools import load_tools
from ai_core.common import llm

human_tools = load_tools(
    ["human"],
    llm=llm,
)