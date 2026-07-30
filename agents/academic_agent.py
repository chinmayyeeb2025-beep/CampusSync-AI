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
            platform="MS Teams",
            deadline="Today",
            priority="High",
            estimated_duration=2,
        ),

        Task(
            title="Python Lab Record",
            platform="LMS",
            deadline="Tomorrow",
            priority="Medium",
            estimated_duration=1,
        ),
    ]

    print("Academic data loaded.")

    return state