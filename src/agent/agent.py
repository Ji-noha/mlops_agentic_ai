from .observer import observe
from .decision import decide
from .action import update_model

def agent():
    state= observe()

    decision= decide(state)

    print(decision)

    if decision =="update_model" :
        update_model(state["latest_version"])

if __name__ == "__main__":

    agent()








