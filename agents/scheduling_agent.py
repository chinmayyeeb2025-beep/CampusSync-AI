from models.study_plan import StudyPlan
from state import PlannerState


def scheduling_agent(state: PlannerState) -> PlannerState:

    print("\n========== Scheduling Agent ==========")

    all_tasks = []

    all_tasks.extend(state["assignments"])

    all_tasks.extend(state["classroom_tasks"])

    state["study_plan"] = StudyPlan(
        registration_no=state["registration_no"],
        mode=state["mode"],
        tasks=all_tasks,
    )

    print(f"Generated plan with {len(all_tasks)} task(s).")

    return state