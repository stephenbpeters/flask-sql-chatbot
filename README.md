# Flask SQL Chatbot

A Flask-based web application that lets visitors ask questions about a SQLite database using everyday English.

Built with **Python, Flask, LangChain, OpenAI, and SQLite**, the application translates natural-language questions into SQL queries, executes them against a database, and returns answers in plain English.

The project also includes a command-line version of the chatbot.

## Live Demo

**[Try the SQL Chatbot](https://chat7.tikimojo.com)**

The demonstration uses the Chinook sample database, which contains information about a fictional digital music store, including artists, albums, tracks, customers, invoices, and playlists.

## Features

- **Natural-language database queries:** Ask questions without knowing SQL.
- **AI-generated SQL:** Uses LangChain and OpenAI to interpret questions and construct SQL queries.
- **Readable answers:** Converts database results into plain-English responses.
- **SQL agent activity viewer:** An expandable section displays the SQL agent's tool calls, generated queries, and database results.
- **Command-line interface:** Includes a standalone Python script for interacting with the database from a terminal.
- **Sample database:** Includes the Chinook SQLite database for experimentation.

## Example Questions

Try asking:

- How many artists are in the database?
- Which customer has spent the most money, and where do they live?
- What are the five best-selling albums?
- Which genres have the most tracks?
- What information is available in this database?

The SQL agent determines which database tables to examine, constructs queries, retrieves the results, and generates a response.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application programming language |
| Flask | Web application framework |
| LangChain | SQL agent and database tools |
| OpenAI (`gpt-4o-mini`) | Natural-language processing and SQL generation |
| SQLite | Database engine |
| Chinook | Sample music-store database |
| Bootstrap 5 | Web interface styling |
| Gunicorn | Production WSGI server |

## Project Structure

```text
chat-app/
├── app.py                 # Flask web application
├── cmd-chat.py            # Command-line chatbot
├── Chinook.db             # Sample SQLite database
├── requirements.txt       # Python dependencies
├── .env.example           # Example environment configuration
├── .gitignore             # Git exclusions
├── templates/
│   ├── base.html          # Shared page layout
│   ├── index.html         # Main chatbot interface
│   └── ...                # Additional site templates
└── README.md
```

Local environment files, logs, and Python cache directories are excluded from version control.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/flask-sql-chatbot.git
cd flask-sql-chatbot
```

Replace `YOUR_USERNAME` with the GitHub account that hosts the repository.

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows:

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your OpenAI API key

Copy the example environment file:

```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:

```dotenv
OPENAI_API_KEY=your_openai_api_key_here
```

An OpenAI API account with API access and available billing credits is required.

**Never commit your actual `.env` file or API keys to GitHub.**

### 5. Start the Flask application

With the virtual environment activated:

```bash
flask --app app run --debug
```

Open your browser at:

http://127.0.0.1:5000

The debug server is intended for local development, not public production hosting.

## Command-Line Version

The project includes `cmd-chat.py`, which allows you to interact with the Chinook database without running Flask.

Run:

```bash
python cmd-chat.py
```

Enter a question when prompted.

The command-line version uses the same LangChain SQL agent and OpenAI model as the web application.

## How the SQL Agent Works

When a visitor submits a question, the application:

1. Receives the natural-language question.
2. Passes it to a LangChain SQL agent powered by OpenAI.
3. Uses SQL database tools to inspect relevant database information.
4. Generates and executes SQL queries.
5. Interprets the database results.
6. Returns an English-language answer.

### Viewing SQL Agent Activity

The web interface includes an expandable **Show SQL Agent Activity** section.

Visitors can inspect the tool calls, SQL queries, and database results associated with their questions.

This makes the application useful as both a database exploration tool and an educational demonstration of AI-assisted SQL querying.

The activity viewer displays tool execution details, not the model's private internal reasoning.

## Deployment

The live demonstration is hosted on a DreamHost VPS using:

- Gunicorn as the WSGI application server.
- A systemd user service with linger enabled.
- DreamHost's HTTPS reverse proxy.

Gunicorn serves the Flask application behind the proxy. The production service is managed independently of Flask's development server.

## Security Considerations

This project is intended as a demonstration and learning tool.

LangChain SQL agents can generate and execute SQL statements. Depending on the database permissions, those statements may modify or delete data.

For deployments using real databases:

- Use a database account or connection with read-only permissions.
- Avoid exposing sensitive customer or business information.
- Never expose OpenAI API keys in templates, source code, or logs.
- Apply appropriate access controls, rate limits, and usage limits before allowing unrestricted public access.
- Review the SQL agent's permissions before connecting it to production data.

The included Chinook database is intended for demonstration purposes.

## Future Improvements

Potential enhancements include:

- Live streaming of SQL agent activity.
- Support for additional database engines.
- Improved error handling and user feedback.
- Additional database exploration features.
- Improved mobile interface and presentation.

## About

Created by **Stephen Peters — Tiki:Mojo Creative Services**.

This project demonstrates how large language models can provide a natural-language interface to a traditional relational database.

**Live demo:** https://chat7.tikimojo.com