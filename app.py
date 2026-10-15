# flask app for using ChatGPT to talk to a database
from flask import Flask, render_template, request, url_for, redirect
# now the libraries to do our chat
# need to get our env variables
import os
from dotenv import load_dotenv
# now start adding the bits to do the chat
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from sqlalchemy import create_engine


# let's get some results from the database
import sqlite3

# Access environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

app_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(app_dir, 'Chinook.db')
# read only access!
engine = create_engine(
    f"sqlite:///file:{db_path}?mode=ro&uri=true"
)
db = SQLDatabase(engine)

print(f"database uri = {db_path}")

# Create the agent executor for the chat
# in order to specify the version of ChatGPT, set model as below:
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

toolkit = SQLDatabaseToolkit(db=db, llm=llm)

agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    agent_type="tool-calling",
    verbose=False,
    agent_executor_kwargs={
        "return_intermediate_steps": True
    }
)

app = Flask(__name__)
# turn on debug mode.  set to "False" to turn off
# app.debug = False  # Enable debug mode

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text', '')

        # Execute the SQL agent and collect its results
        result_data = agent_executor.invoke({"input": text})

        # Extract the final answer
        response = result_data["output"]

        # Collect the SQL agent's intermediate steps
        steps = []

        for action, observation in result_data.get("intermediate_steps", []):
            steps.append({
                "tool": action.tool,
                "input": str(action.tool_input),
                "output": str(observation)
            })

        # Send everything to the HTML template
        return render_template(
            'index.html',
            text=text,
            response=response,
            steps=steps
        )

    return render_template('index.html')  
    
# now we add a route to our about page
@app.route('/about')
def about():
    return render_template('about.html')  
    
# now we add a route to our news page
@app.route('/news')
def news():
    return render_template('news.html')
    
# now we add a route to our contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')                
    
@app.route('/test')    
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(host='chat7.tikimojo.com', port=8007)


