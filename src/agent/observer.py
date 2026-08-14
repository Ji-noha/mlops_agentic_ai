from mlflow.tracking import MlflowClient
import json
from .prometheus_client import get_prediction_count, get_model_version, get_errors_count, get_response_time 

client= MlflowClient()

def get_model_accuracy(version):

    model_version = client.get_model_version(
        "BreastCancerModel",
        str(version)
    )

    run = client.get_run(model_version.run_id)

    return run.data.metrics.get("accuracy")


def observe():

    latest_version = client.get_latest_versions(
        "BreastCancerModel"
    )[0].version

    with open("current_version.json", "r") as file:
        data = json.load(file)

    current_version = data["current_version"]

    prediction_count = get_prediction_count()
    error_count = get_errors_count()
    response_time = get_response_time()
    model_version = get_model_version()

    return {
        "latest_version": int(latest_version),
        "current_version": int(current_version),
        "prediction_count": prediction_count,
        "error_count": error_count,
        "response_time": response_time,
        "model_version": model_version,
        "accuracy": get_model_accuracy(latest_version)
    }

if __name__ == "__main__":

    state= observe()

    print(state)