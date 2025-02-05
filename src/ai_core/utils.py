"""Utility & helper functions."""

from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import BaseMessage
import asyncio
from IPython.display import Image


def get_message_text(msg: BaseMessage) -> str:
    """Get the text content of a message."""
    content = msg.content
    if isinstance(content, str):
        return content
    elif isinstance(content, dict):
        return content.get("text", "")
    else:
        txts = [c if isinstance(c, str) else (c.get("text") or "") for c in content]
        return "".join(txts).strip()


def load_chat_model(fully_specified_name: str) -> BaseChatModel:
    """Load a chat model from a fully specified name.

    Args:
        fully_specified_name (str): String in the format 'provider/model'.
    """
    provider, model = fully_specified_name.split("/", maxsplit=1)
    return init_chat_model(model, model_provider=provider)


async def run_graph(graph, inputs):
    """Run a LangGraph asynchronously"""
    return await graph.ainvoke(inputs)


def run_graph_sync(graph, inputs):
    """Run a LangGraph synchronously"""
    return asyncio.run(run_graph(graph, inputs))


async def beautiful_print(message: BaseMessage):
    """Beautifully print a message"""
    print(f"{message.type}: {get_message_text(message)}")


def visualize_graph(graph, filename="workflow.png"):
    """Save and display the graph visualization"""
    img = Image(graph.get_graph().draw_mermaid_png())
    with open(filename, "wb") as f:
        f.write(img.data)
