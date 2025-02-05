import os

from langchain_community.tools.google_jobs import GoogleJobsQueryRun
from langchain_community.utilities.google_jobs import GoogleJobsAPIWrapper

from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_openai import OpenAI
from ai_core.utils import load_chat_model
from ai_core.common import configuration, llm

google_jobs_tools = load_tools(["google-jobs"], llm=llm)