from mlflow.tracking import MlflowClient
import json

client= MlflowClient()

def observe():

    latest_version= client.get_latest_versions("BreastCancerModel")[0].version

    with open("current_version.json","r") as file:
        data= json.load(file)

    current_version= data["current_version"]

    return {
        "latest_version":int(latest_version),
        "current_version":int(current_version)
    } 

if __name__ == "__main__":

    state= observe()

    print(state)