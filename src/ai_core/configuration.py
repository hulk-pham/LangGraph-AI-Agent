"""Define the configurable parameters for the agent."""

from __future__ import annotations

from dataclasses import dataclass, field, fields
from typing import Annotated, Optional

from langchain_core.runnables import RunnableConfig, ensure_config

from ai_core import prompts


@dataclass(kw_only=True)
class Configuration:
    """The configuration for the agent."""

    system_prompt: str = field(
        default=prompts.SYSTEM_PROMPT,
        metadata={
            "description": "The system prompt to use for the agent's interactions. "
            "This prompt sets the context and behavior for the agent."
        },
    )

    model: Annotated[str, {"__template_metadata__": {"kind": "llm"}}] = field(
        default="anthropic/claude-3-5-sonnet-20240620",
        metadata={
            "description": "The name of the language model to use for the agent's main interactions. "
            "Should be in the form: provider/model-name."
        },
    )

    max_search_results: int = field(
        default=10,
        metadata={
            "description": "The maximum number of search results to return for each search query."
        },
    )

    database_host: str = field(
        default="127.0.0.1",
        metadata={
            "description": "The host of the database to use for the agent's interactions."
        },
    )

    database_port: int = field(
        default=3306,
        metadata={
            "description": "The port of the database to use for the agent's interactions."
        },
    )

    database_user: str = field(
        default="root",
        metadata={
            "description": "The user of the database to use for the agent's interactions."
        },
    )

    database_password: str = field(
        default="",
        metadata={
            "description": "The password of the database to use for the agent's interactions."
        },
    )

    database_name: str = field(
        default="",
        metadata={
            "description": "The name of the database to use for the agent's interactions."
        },
    )
    
    
    
