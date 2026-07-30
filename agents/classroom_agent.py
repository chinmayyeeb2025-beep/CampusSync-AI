from models.task import Task
from state import PlannerState


def classroom_agent(state: PlannerState) -> PlannerState:

    print("\n========== Classroom Agent ==========")

    state["classroom_tasks"] = [

        Task(
            title="Deep Learning Quiz",
            platform="Google Classroom",
            deadline="Friday",
            priority="Medium",
            estimated_duration=1,
        )
    ]

    print("Google Classroom data loaded.")

    return state