from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="agent_monitoring",
    start_date=datetime(2026, 7, 31),
    schedule="*/5 * * * *",
    catchup=False,
) as dag:

    run_agent = BashOperator(
        task_id="run_agent",
        bash_command=(
            "cd /workspaces/mlops_agentic_ai && "
            "/workspaces/mlops_agentic_ai/.venv/bin/python "
            "-m src.agent.agent"
        ),
    )