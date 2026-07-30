from pydantic import BaseModel


class Task(BaseModel):
    title: str
    platform: str
    deadline: str
    priority: str
    estimated_duration: int