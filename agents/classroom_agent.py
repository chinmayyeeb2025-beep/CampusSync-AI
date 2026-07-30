from models.task import Task
from state import PlannerState


def classroom_agent(state: PlannerState) -> PlannerState:

    print("\n========== Classroom Agent ==========")

    state["classroom_tasks"] = [

    Task(
        title="Deep Learning Quiz",
        subject="Deep Learning",
        platform="Google Classroom",
        deadline="Friday",
        description="Prepare for Quiz 2.",
    )
]

    print("Google Classroom data loaded.")

    return state