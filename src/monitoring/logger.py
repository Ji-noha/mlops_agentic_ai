import json
import os
import datetime
import csv


def log_prediction(features,prediction):

    os.makedirs("logs",exist_ok=True)

    csv_file= "logs/prediction.csv"
    file_exist= os.path.isfile("logs/predictions.csv")

    timestamp=datetime.datetime.now()

    with open('current_version.json','r') as f:
        data=json.load(f)
        model_version= data['current_version']

    
    with open("logs/predictions.csv","a",newline="") as file:
        writer=csv.writer(file)

        if not file_exist:
            writer.writerows(["timestamp", "model_version", "prediction", "features"])

        writer.writerow([timestamp,
            model_version,
            prediction,
            features])


