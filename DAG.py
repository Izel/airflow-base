from datetime import timedelta
from airflow import DAG

from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['gloria.meneses@moveengineering-eu.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=20),    
}


with DAG(
    'Basic_DEMO',
    default_args=default_args,
    description='Airflow DEMO',
    schedule_interval= None, #timedelta(minutes=1),
    start_date=days_ago(1),
    tags=['DEMO'],
) as dag:

    task1 = BashOperator(
        task_id='copy_file',
        bash_command='cp /opt/file.csv /tmp/file.csv '
    )

    task2 = BashOperator(
        task_id='remove_old',
        bash_command='rm /opt/file.csv '
    )

    task3 = BashOperator(
        task_id='copy_renamed',
        bash_command='mv /tmp/file.csv /opt/renamed.csv '
    )

    task4 = BashOperator(
        task_id='copy_local',
        bash_command='cp /opt/renamed.csv /opt/file.csv '
    )

task1 >> task2 >> task3 >> task4
