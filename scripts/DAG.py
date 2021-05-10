from datetime import timedelta
from airflow import DAG
import shutil
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
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
def my_func():
    '''original = 'file.csv'
    target = '/tmp/file.csv'

    shutil.copyfile(original, target)'''
    print('Works')

with DAG(
    'Basic_DEMO',
    default_args=default_args,
    description='Airflow DEMO',
    schedule_interval= None, #timedelta(minutes=1),
    start_date=days_ago(1),
    tags=['DEMO'],
) as dag:


    task = BashOperator(
        task_id='create_file',
        bash_command='touch file.csv'
    )
    '''makedir = BashOperator(
        task_id='mkdir',
        bash_command='mkdir csvhandler '
    )'''
    task1 = BashOperator(
        task_id='copy_file',
        bash_command='python /usr/local/airflow/task.py '
    )


    #task1 = PythonOperator(task_id='copy_file', python_callable=my_func)


    task2 = BashOperator(
        task_id='remove_old',
        bash_command='rm /tmp/tst.csv '
    )

    

    task3 = BashOperator(
        task_id='move_file',
        bash_command='python /usr/local/airflow/moveFile.py -i /tmp/tst2.csv -o /tmp/renamed.csv '
    )

    task4 = BashOperator(
        task_id='copy_local',
        bash_command='cp /tmp/tst.csv /tmp/copy.csv '
    )

task >> task1 >> task2 >> task3 >> task4
