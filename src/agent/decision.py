def decide(state):
    
    if state["latest_version"] > state["current_version"]:
        return "update_model"

    if state["error_count"] >5:
        return "alert"
    if state["accuracy"] <0.90:
        return "retarin model"
    
    return "no_action"


if __name__ == "__main__":

    print(decide(test_state))




