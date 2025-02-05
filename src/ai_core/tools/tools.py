from typing import Any, Callable, List, Optional, cast

from ai_core.tools.search_tavily import search_tavily
from ai_core.tools.database import database_toolkit
from ai_core.tools.shell import shell_tool
from ai_core.tools.file import file_toolkit
from ai_core.tools.google_jobs import google_jobs_tools
from ai_core.tools.human_tool import human_tools
# Combine all tools into a single list
TOOLS: List[Callable[..., Any]] = [
    search_tavily,
    shell_tool,
    *database_toolkit.get_tools(),
    *file_toolkit.get_tools(),
    *google_jobs_tools,
    *human_tools,
]   