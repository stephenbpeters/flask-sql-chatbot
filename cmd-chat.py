
#!/usr/bin/env python3

# Command-line SQL chatbot using LangChain and OpenAI

import os
from dotenv import load_dotenv

from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from sqlalchemy import create_engine

# Load the OpenAI API key from .env
load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError("OPENAI_API_KEY is not set")

# Find Chinook.db in the same directory as this script
app_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(app_dir, "Chinook.db")

if not os.path.isfile(db_path):
    raise FileNotFoundError(f"Database not found: {db_path}")

# Connect to the database, read only!
engine = create_engine(
    f"sqlite:///file:{db_path}?mode=ro&uri=true"
)
db = SQLDatabase(engine)

print(f"Connected to database: {db_path}")

# Initialize the language model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# Create the SQL toolkit
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# Create the SQL agent
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    agent_type="tool-calling",
    verbose=True
)

print("\nSQL Chatbot Ready!")
print("Type 'quit' or 'exit' to stop.\n")

# Interactive command-line loop
while True:
    query = input("Enter a question: ").strip()

    if query.lower() in ("quit", "exit"):
        print("Goodbye!")
        break

    if not query:
        continue

    try:
        response = agent_executor.invoke(
            {"input": query}
        )["output"]

        print("\n========== ANSWER ==========")
        print(response)
        print("============================\n")

    except Exception as e:
        print(f"\nError: {type(e).__name__}: {e}\n")
