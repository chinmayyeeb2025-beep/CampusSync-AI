from typing import TypedDict

from models.task import Task
from models.study_plan import StudyPlan


class PlannerState(TypedDict):

    registration_no: str

    mode: str

    timetable: str

    assignments: list[Task]

    classroom_tasks: list[Task]

    study_plan: StudyPlan