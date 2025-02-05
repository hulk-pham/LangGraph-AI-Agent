"""Define a custom Reasoning and Action agent.

Works with a chat model with tool calling support.
"""

from datetime import datetime, timezone
from typing import Dict, List, Literal, cast

from langchain_core.messages import AIMessage
from langchain_core.runnables import RunnableConfig
from langgraph.graph import StateGraph
from langgraph.prebuilt import ToolNode

from ai_core.configuration import Configuration
from ai_core.common import configuration, llm
from ai_core.state import InputState, State
from ai_core.tools import TOOLS
from IPython.display import Image, display
from ai_core.utils import load_chat_model, run_graph_sync

async def call_model(
    state: State
) -> Dict[str, List[AIMessage]]:
    """Call the LLM powering our "agent".

    This function prepares the prompt, initializes the model, and processes the response.

    Args:
        state (State): The current state of the conversation.

    Returns:
        dict: A dictionary containing the model's response message.
    """

    system_message = configuration.system_prompt.format(
        system_time=datetime.now(tz=timezone.utc).isoformat()
    )

    response = cast(
        AIMessage,
        await llm.ainvoke(
            [{"role": "system", "content": system_message}, *state.messages]
        ),
    )

    if state.is_last_step and response.tool_calls:
        return {
            "messages": [
                AIMessage(
                    id=response.id,
                    content="Sorry, I could not find an answer to your question in the specified number of steps.",
                )
            ]
        }

    return {"messages": [response]}

def route_model_output(state: State) -> Literal["__end__", "tools"]:
    """Determine the next node based on the model's output.

    This function checks if the model's last message contains tool calls.

    Args:
        state (State): The current state of the conversation.

    Returns:
        str: The name of the next node to call ("__end__" or "tools").
    """
    last_message = state.messages[-1]
    if not isinstance(last_message, AIMessage):
        raise ValueError(
            f"Expected AIMessage in output edges, but got {type(last_message).__name__}"
        )
    if not last_message.tool_calls:
        return "__end__"
    return "tools"


builder = StateGraph(State, input=InputState, config_schema=Configuration)

builder.add_node(call_model)
builder.add_node("tools", ToolNode(TOOLS))

builder.add_edge("__start__", "call_model")

builder.add_conditional_edges(
    "call_model",
    route_model_output,
)

builder.add_edge("tools", "call_model")

# Compile the builder into an executable graph
# You can customize this by adding interrupt points for state updates
graph = builder.compile(
    interrupt_before=[],  # Add node names here to update state before they're called
    interrupt_after=[],  # Add node names here to update state after they're called
)
graph.name = "AI Core Agent"  # This customizes the name in LangSmith