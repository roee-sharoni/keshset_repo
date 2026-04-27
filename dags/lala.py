from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime

with DAG(
    dag_id="lala_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    default_args={"owner": "data-guild"},
) as dag:

    def hello():
        print("Airflow 3 is running")

    PythonOperator(task_id="hello", python_callable=hello)
