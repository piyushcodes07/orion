# Orion: Your Integrated AI Assistant

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

Orion is a sophisticated, autonomous AI assistant designed to manage your complete digital workflow. It seamlessly integrates email management and task creation, acting as a true partner to help you stay organized and productive.

## Overview

In today's fast-paced digital world, managing the constant flow of emails and the tasks that arise from them is a significant challenge. Orion solves this problem by providing a unified, intelligent system that not only triages and responds to your emails but also automatically creates and manages a corresponding To-Do list.

Built with a powerful multi-agent architecture, Orion learns from your feedback to adapt to your personal style and priorities, making it more than just a tool—it's a personalized assistant.

## Core Features

-   **Autonomous Email Management:** Orion connects to your Gmail inbox, automatically triaging emails into categories: `respond`, `notify`, or `ignore`.
-   **Intelligent Response Generation:** For emails that require a response, Orion can draft replies, schedule meetings using the Google Calendar API, and handle back-and-forth communication.
-   **Integrated Task Management:** Orion identifies actionable items from your emails and automatically creates tasks in a persistent To-Do list, bridging the gap between communication and action.
-   **Adaptive Learning (RAG + HITL):** Through a Human-in-the-Loop (HITL) interface, you can approve, edit, or reject Orion's actions. Every interaction teaches Orion, updating its "memory" to better match your preferences for communication and task management.

## How It Works: An Agentic Architecture

Orion is built using **LangGraph** to orchestrate a stateful, multi-agent system. This modular design allows for complex, multi-step reasoning and action.

1.  **Unified Agent (`unified_agent.py`):** This is the master router. It receives all incoming data (new emails or user commands) and directs it to the appropriate specialized agent.

2.  **Email Assistant (`email_assistant_hitl_memory_gmail.py`):** This sub-agent manages all email-related activities. It uses an LLM to understand email content, classify it, and use tools like `send_email_tool` and `schedule_meeting_tool` to interact with Google services.

3.  **Task Manager (`task_maistro.py`):** This sub-agent is the task management expert. It maintains the user's To-Do list, adding new tasks, updating their status, and storing them in a persistent memory.

4.  **The Bridge (`email_to_todo_bridge`):** This crucial node connects the two agents. After the Email Assistant processes an important email, the bridge extracts the context and transforms it into a structured command for the Task Manager, enabling seamless, automatic task creation.

5.  **Adaptive Memory (RAG):** User feedback from the HITL process is used to update a knowledge base of "user preferences." Before taking any action, Orion retrieves relevant preferences from this memory, allowing it to personalize its behavior over time.

## Tech Stack

-   **Backend:** Python
-   **AI Orchestration:** LangChain & LangGraph
-   **LLMs:** OpenAI (GPT-4 and others)
-   **APIs:** Google Gmail API, Google Calendar API

## Getting Started

Follow these steps to set up and run your own instance of Orion.

### 1. Prerequisites

-   Python 3.9+
-   An OpenAI API Key
-   A Google Cloud Project with the Gmail API and Calendar API enabled.

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/orion.git
cd orion
```

### 3. Install Dependencies

It's recommended to use a virtual environment.

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 4. Configure Google API Access

Orion needs credentials to access your Google account securely.

1.  From your Google Cloud Project, download your OAuth 2.0 Client ID credentials as a JSON file.
2.  Save this file in the project at the following path: `src/email_assistant/tools/gmail/.secrets/secrets.json`.
3.  Run the setup script. This will open a browser window for you to authenticate with your Google account and grant permissions.

    ```bash
    python src/email_assistant/tools/gmail/setup_gmail.py
    ```

    After successful authentication, a `token.json` file will be created in the `.secrets` directory.

### 5. Set Environment Variables

Create a `.env` file in the root of the project and add your OpenAI API key.

```
OPENAI_API_KEY="your-openai-api-key"
```

Orion will automatically load this key.

## Usage

### Manual Email Ingestion

You can trigger a one-time scan of your inbox to process recent emails.

```bash
python src/email_assistant/tools/gmail/run_ingest.py --email "your-email@gmail.com" --minutes-since 60
```

-   `--email`: The email address Orion should manage.
-   `--minutes-since`: How far back to look for emails (in minutes).

### Automated Email Ingestion (Cron Job)

For continuous, automated operation, you can set up a LangGraph cron job that periodically triggers the ingestion script.

```bash
python src/email_assistant/tools/gmail/setup_cron.py --email "your-email@gmail.com" --url "http://127.0.0.1:2024" --schedule "*/10 * * * *"
```

-   `--schedule`: The cron schedule (e.g., "every 10 minutes").

## Contributing

Contributions are welcome! If you'd like to help improve Orion, please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeature`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some feature'`).
5.  Push to the branch (`git push origin feature/YourFeature`).
6.  Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
