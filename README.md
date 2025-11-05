# Task mAIstro: The Intelligent To-Do List

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

Task mAIstro is a next-generation task management application powered by AI. It goes beyond a simple To-Do list by learning your preferences and automating task creation, featuring a powerful **AI Email Assistant** to turn your inbox into an organized, actionable workflow.

## Overview

Traditional To-Do lists are passive; you have to manually add, manage, and prioritize every task. Task mAIstro changes that paradigm. At its core, it's an intelligent task manager that you can interact with using natural language.

Its killer feature is the **Email Assistant extension**, which connects directly to your Gmail inbox. It autonomously reads, triages, and even responds to your emails, but more importantly, it identifies actionable items and automatically creates structured tasks for you within Task mAIstro. It transforms your inbox from a source of stress into a source of organized productivity.

## Core Features

### Task mAIstro

-   **Intelligent Task Management:** A robust, AI-powered system for managing your To-Do list.
-   **Natural Language Interaction:** Create, update, and query your tasks by talking to the agent in plain English.
-   **Adaptive Learning:** Task mAIstro learns how you prefer to manage your tasks and personalizes its behavior over time based on your feedback.

### The Email Assistant Extension

-   **Automatic Task Creation from Emails:** This is where the magic happens. The assistant reads an email about a deadline or a request and automatically adds a corresponding item to your Task mAIstro list.
-   **Autonomous Inbox Triage:** It filters your inbox into `respond`, `notify`, or `ignore`, so you only focus on what matters.
-   **Automated Responses & Scheduling:** The assistant can draft and send email replies and schedule meetings on your Google Calendar, handling the administrative overhead for you.

## How It Works: An Agentic Architecture

Task mAIstro is built on a modular, multi-agent architecture using **LangGraph** to manage complex, stateful interactions.

1.  **The Core: Task mAIstro (`task_maistro.py`):** This is the heart of the application. It's an AI agent focused entirely on creating and managing your To-Do list, powered by a persistent memory.

2.  **The Extension: Email Assistant (`email_assistant_hitl_memory_gmail.py`):** This is a powerful sub-agent designed for inbox automation. It uses an LLM and tools to interact with Gmail and Google Calendar.

3.  **The Integrator: Unified Agent (`unified_agent.py`):** This master agent brings everything together. It acts as a smart router, directing user commands to the core Task mAIstro agent and activating the Email Assistant extension to process incoming emails.

4.  **The Bridge (`email_to_todo_bridge`):** This critical node is what makes the integration seamless. It takes the output from the Email Assistant (e.g., "Schedule a meeting with Bob on Friday") and translates it into a structured task ("Add 'Prepare for Bob meeting' to To-Do list") for the core Task mAIstro agent.

## Tech Stack

-   **Backend:** Python
-   **AI Orchestration:** LangChain & LangGraph
-   **LLMs:** OpenAI (GPT-4 and others)
-   **APIs:** Google Gmail API, Google Calendar API

## Getting Started

Follow these steps to set up and run your instance of Task mAIstro and its Email Assistant.

### 1. Prerequisites

-   Python 3.9+
-   An OpenAI API Key
-   A Google Cloud Project with the Gmail API and Calendar API enabled.

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/task-maistro.git
cd task-maistro
```

### 3. Install Dependencies

It's recommended to use a virtual environment.

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 4. Configure Google API Access

The Email Assistant extension needs credentials to access your Google account securely.

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

## Usage

You can interact with Task mAIstro directly or activate the Email Assistant to run in the background.

### Activating the Email Assistant Extension

To have Task mAIstro start processing your emails, you can run a one-time scan or set up an automated job.

**Manual Scan:**
```bash
python src/email_assistant/tools/gmail/run_ingest.py --email "your-email@gmail.com" --minutes-since 60
```

**Automated Background Operation (Cron Job):**
Set up a recurring job to have the assistant check your email every 10 minutes.
```bash
python src/email_assistant/tools/gmail/setup_cron.py --email "your-email@gmail.com" --url "http://127.0.0.1:2024" --schedule "*/10 * * * *"
```

## Contributing

Contributions are welcome! If you'd like to help improve Task mAIstro, please fork the repository and open a pull request.

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeature`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some feature'`).
5.  Push to the branch (`git push origin feature/YourFeature`).
6.  Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
