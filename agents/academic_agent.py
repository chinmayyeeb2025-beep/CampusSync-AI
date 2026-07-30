from models.task import Task
from state import PlannerState


def academic_agent(state: PlannerState) -> PlannerState:

    print("\n========== Academic Agent ==========")

    state["timetable"] = """
Monday:
8:00-8:50 Machine Learning
9:00-9:50 Python for AI
10:00-10:50 Data Mining
11:00-11:50 Linear Algebra
2:00-2:50 Deep Learning
3:00-3:50 NLP
"""

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