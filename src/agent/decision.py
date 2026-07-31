def decide(state):
    
    if state["latest_version"] > state["current_version"]:
        return "update_model"

    return "no_action"


if __name__ == "__main__":

    test_state ={
        "current_state": 1,
        "latest_version": 2
    }

    print(decide(test_state))




