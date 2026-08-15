from .observer import observe
from .decision import decide
from .action import update_model ,alert, retrain_model

def agent():
    state= observe()

    decision= decide(state)

    print(decision)

    if decision =="update_model" :
        update_model(state["latest_version"])

    elif decision == "retrain_model":
        retrain_model()

    elif decision == "alert":
        alert()

    else:
        print("No action required.")

        
if __name__ == "__main__":

    agent()








