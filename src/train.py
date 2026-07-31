from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import mlflow
from mlflow import MlflowClient
import mlflow.sklearn



def load_data():
    cancer= load_breast_cancer() # the dataset
    X=cancer.data  
    y=cancer.target
    return X,y

def train_model(X,y):
    X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    # Fixe le decoupage pour obtenir toujours les mêmes données de train et de test
    random_state=42
    ) 
    model=RandomForestClassifier()
    model.fit(X_train,y_train)

    return model, X_test,y_test

def evaluate_model(model, X_test,y_test):
    predictions=model.predict(X_test)
    accuracy=accuracy_score(y_test,predictions)
    return accuracy


def main():
    with mlflow.start_run():
        X,y = load_data()

        model, X_test, y_test =train_model(X,y)

        accuracy= evaluate_model(model,X_test,y_test)

        mlflow.log_metric("accuracy", accuracy)

        #mlflow.sklearn.log_model(model, "model")
        
        mlflow.sklearn.log_model(
            sk_model=model,
            artifact_path="model",
            registered_model_name="BreastCancerModel"
        )
        
        print(f"Accuracy:{accuracy:.2f}")

        print("Training completed successfully!")


if __name__== "__main__":
    main()










