from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="model_pipeline",
    start_date=datetime(2026, 7, 31),
    schedule="@daily",
    catchup=False,
) as dag:

    train = BashOperator(
        task_id="train_model",
        bash_command="python -m src.train",
    )


    agent = BashOperator(
        task_id="deploy_model",
        bash_command="python -m src.agent.agent",
    )

    train >> agent