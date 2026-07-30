from models.task import Task
from state import PlannerState
from models.timetable import Lecture

def academic_agent(state: PlannerState) -> PlannerState:

    print("\n========== Academic Agent ==========")

    state["timetable"] = [

    Lecture(
        day="Monday",
        start_time="08:00",
        end_time="08:50",
        subject="Machine Learning",
    ),

    Lecture(
        day="Monday",
        start_time="09:00",
        end_time="09:50",
        subject="Python for AI",
    ),

    Lecture(
        day="Monday",
        start_time="10:00",
        end_time="10:50",
        subject="Data Mining",
    ),

    Lecture(
        day="Monday",
        start_time="11:00",
        end_time="11:50",
        subject="Linear Algebra",
    ),

    Lecture(
        day="Monday",
        start_time="14:00",
        end_time="14:50",
        subject="Deep Learning",
    ),

    Lecture(
        day="Monday",
        start_time="15:00",
        end_time="15:50",
        subject="Natural Language Processing",
    ),
]

    state["assignments"] = [

    Task(
        title="Machine Learning Assignment",
        subject="Machine Learning",
        platform="MS Teams",
        deadline="Today",
        description="Complete and submit Assignment 1.",
    ),

    Task(
        title="Python Lab Record",
        subject="Python for AI",
        platform="LMS",
        deadline="Tomorrow",
        description="Complete Lab Experiment 5.",
    ),
    ]

    print("Academic data loaded.")

    return state