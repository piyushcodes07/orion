from typing_extensions import Literal
from langgraph.graph import StateGraph, START, END
from langgraph.store.base import BaseStore

# Import Gmail Assistant + ToDo Agent
from email_assistant import configuration
from email_assistant.email_assistant_hitl_memory_gmail import email_assistant # compiled workflow
from email_assistant.task_maistro import graph as todo_agent  # compiled workflow
from email_assistant.schemas import State as GmailState        # Gmail schema (already extends MessagesState)

def entry_router(state: GmailState, store: BaseStore) -> Literal["email_assistant", "todo_agent"]:
    """Route based on the very first input"""
    if state.get("email_input"):
        return "email_assistant"
    elif len(state.get("task_messages"))>0:
        return "todo_agent"
    else:
        raise ValueError("Invalid entry: must contain either email_input or task_input/messages")


def email_to_todo_bridge(state: GmailState, store: BaseStore):
    """Convert a Gmail email into a user message for Task mAIstro"""
    email = state["email_input"]

    todo_message = f"create a New task from context of this  email:\n {email}"

    return {
        "task_messages": [{"role": "user", "content": todo_message}],
        "task_input": todo_message,
    }


builder = StateGraph(GmailState,config_schema=configuration.Configuration)

builder.add_conditional_edges(
    START,
    entry_router,
    {
        "email_assistant": "email_assistant",
        "todo_agent": "todo_agent",
    },
)

builder.add_node("email_assistant", email_assistant)
builder.add_node("email_to_todo_bridge", email_to_todo_bridge)
builder.add_edge("email_assistant", "email_to_todo_bridge")
builder.add_edge("email_to_todo_bridge", "todo_agent")

builder.add_node("todo_agent", todo_agent)

builder.add_edge("todo_agent", END)

unified_agent = builder.compile()
