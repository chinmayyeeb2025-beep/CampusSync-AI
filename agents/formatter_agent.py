from state import PlannerState


def formatter_agent(state: PlannerState) -> PlannerState:

    print("\n========== Formatter Agent ==========")

    print(state["study_plan"].model_dump())

    return state