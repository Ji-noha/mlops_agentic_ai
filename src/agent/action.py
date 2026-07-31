import mlflow
import joblib
import requests
import json

def update_model(version):

    model_uri = f"models:/BreastCancerModel/{version}"

    model= mlflow.sklearn.load_model(
        model_uri
    )

    joblib.dump(model, "models/random_forest.joblib")

    print("Local model updated successfully.")

    response=requests.post("http://localhost:8000/reload")

    if response.status_code ==200:
        with open("current_version.json","w") as file:
            json.dump(
                {"current_version":version} , 
                file
            )
        print("Model updated successfully")
    else:
        print("Reload failed")


if __name__ == "__main__":
    update_model()

