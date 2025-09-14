from datetime import datetime
from operator import add
from typing import Optional
from typing  import Annotated, TypedDict, Literal
from pydantic import BaseModel, Field
from langgraph.graph import MessagesState

# =========================
# Gmail Assistant Schemas
# =========================

class RouterSchema(BaseModel):
    """Analyze the unread email and route it according to its content."""

    reasoning: str = Field(
        description="Step-by-step reasoning behind the classification."
    )
    classification: Literal["ignore", "respond", "notify"] = Field(
        description=(
            "The classification of an email: "
            "'ignore' for irrelevant emails, "
            "'notify' for important information that doesn't need a response, "
            "'respond' for emails that need a reply"
        ),
    )


class StateInput(TypedDict):
    email_input: dict
    classification_decision: Literal["ignore", "respond", "notify"]
    task_input: str | None

class State(MessagesState):
    # This state class has the messages key built in
    email_input: dict
    task_messages:Annotated[list,add]
    classification_decision: Literal["ignore", "respond", "notify"]
    task_input: str | None


class EmailData(TypedDict):
    id: str
    thread_id: str
    from_email: str
    subject: str
    page_content: str
    send_time: str
    to_email: str


class UserPreferences(BaseModel):
    """Updated user preferences based on user's feedback."""
    chain_of_thought: str = Field(
        description="Reasoning about which user preferences need to add/update if required"
    )
    user_preferences: str = Field(
        description="Updated user preferences"
    )

# =========================
# ToDo App Schemas
# =========================

class Profile(BaseModel):
    """This is the profile of the user you are chatting with"""
    name: Optional[str] = Field(description="The user's name", default=None)
    location: Optional[str] = Field(description="The user's location", default=None)
    job: Optional[str] = Field(description="The user's job", default=None)
    connections: list[str] = Field(
        description="Personal connections of the user, such as family, friends, or coworkers",
        default_factory=list,
    )
    interests: list[str] = Field(
        description="Interests that the user has",
        default_factory=list,
    )


class ToDo(BaseModel):
    """A structured task extracted or created from an email or conversation."""
    task: str = Field(description="The task to be completed.")
    time_to_complete: Optional[int] = Field(
        description="Estimated time to complete the task (minutes)."
    )
    deadline: Optional[datetime] = Field(
        description="When the task needs to be completed by (if applicable)",
        default=None,
    )
    solutions: list[str] = Field(
        description=(
            "List of specific, actionable solutions (e.g., service providers or "
            "options relevant to completing the task)"
        ),
        min_items=1,
        default_factory=list,
    )
    status: Literal["not started", "in progress", "done", "archived"] = Field(
        description="Current status of the task",
        default="not started",
    )
