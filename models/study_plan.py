from pydantic import BaseModel

from models.task import Task


class StudyPlan(BaseModel):
    registration_no: str
    mode: str
    tasks: list[Task]