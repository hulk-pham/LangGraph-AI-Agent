import sqlite3

import requests
from langchain_community.utilities.sql_database import SQLDatabase
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from ai_core.common import configuration, llm
from ai_core.utils import load_chat_model
from urllib.parse import quote_plus

def get_mysql_url(user, password, host, database, port=3306):
    """Create MySQL connection URL with proper escaping"""
    return f"mysql+mysqlconnector://{user}:{quote_plus(password)}@{host}:{port}/{database}"

print(configuration)

DB_URL = get_mysql_url(
    user=configuration.database_user,
    password=configuration.database_password,
    host=configuration.database_host,
    database=configuration.database_name
)

engine = create_engine(DB_URL)
db = SQLDatabase(engine)

database_toolkit = SQLDatabaseToolkit(db=db, llm=llm)