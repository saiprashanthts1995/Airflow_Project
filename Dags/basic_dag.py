from airflow import DAG
from datetime import datetime
from airflow.operators import BashOperator, DummyOperator, PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta


def hello_sai():
    '''
    Simple Python Function to print hello
    :return:
    '''
    print('hello to Sai')


dag_arguments = {
    'Owner': 'Sai',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    dag_id='Basic_Airflow_Check',
    default_args=dag_arguments,
    description='A simple tutorial DAG',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2)
)

dummy_task = DummyOperator(
    task_id='Start',
    dag=dag
)

python_task = PythonOperator(
    task_id='Python_Hello_Word',
    python_callable=hello_sai,
    dag=dag
)

Bash_task = BashOperator(
    task_id='print_date',
    bash_command='date +%d%m%y',
    dag=dag
)

dummy_task >> python_task >> Bash_task