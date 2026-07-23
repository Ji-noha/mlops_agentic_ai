from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib


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


def save_model(model):
    joblib.dump(model,"models/random_forest.joblib")
    

def main():
    X,y = load_data()

    model, X_test, y_test =train_model(X,y)

    accuracy= evaluate_model(model,X_test,y_test)
    
    print(f"Accuracy:{accuracy:.2f}")

    save_model(model)

    print("Model  saved !!")


if __name__== "__main__":
    main()











"""
cancer= load_breast_cancer() # the dataset

X=cancer.data  # cancer.data ou lautre cancer["data"] 
y=cancer.target

# composer data
X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
) # with random Les données de test sont exactement les mêmes , La seule chose qui a changé est le modèle , 42 cest seulement une convention meme 10 ou 7 vont fonctionner

#creation du modele
model=RandomForestClassifier()

#Entrainer
model.fit(X_train,y_train)

#predire
predictions=model.predict(X_test)

#evaluer
accuracy=accuracy_score(y_test,predictions)

print(f"Accuracy:{accuracy:.2f}")

#save the model
joblib.dump(model,"models/random_forest.joblib")
==
def save_model(model):
    model_path=joblib.dump(model,"models/random_forest.joblib")
    return model_path

    model_path = save_model(model)

    print(f"Model saved in: {model_path}")

"""