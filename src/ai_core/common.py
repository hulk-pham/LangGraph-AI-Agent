from langchain_core.runnables import RunnableConfig
from ai_core.configuration import Configuration
from ai_core.utils import load_chat_model
import os
from dotenv import load_dotenv

load_dotenv()

configuration = Configuration(
    model=os.getenv("MODEL"),
    database_host=os.getenv("DATABASE_HOST"),
    database_port=os.getenv("DATABASE_PORT"),
    database_user=os.getenv("DATABASE_USER"),
    database_password=os.getenv("DATABASE_PASSWORD"),
    database_name=os.getenv("DATABASE_NAME"),
)

llm = load_chat_model(configuration.model)