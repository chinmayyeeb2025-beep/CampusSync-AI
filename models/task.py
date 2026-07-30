from pydantic import BaseModel


class Task(BaseModel):
    title: str
    subject: str
    platform: str
    deadline: str
    description: str = ""