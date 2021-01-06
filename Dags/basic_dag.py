from airflow import dag
from airflow.models import Variable
from datetime import datetime
from airflow.operators import BashOperator, DummyOperator, PythonOperator


def hello_sai():
    '''
    Simple Python Function to print hello
    :return:
    '''
    print('hello to Sai')


dag_arguments = {
    'Owner': 'Sai',
    'depends_on_past': False,
    'start_date': datetime(2021, 1, 6)
}

dag = Dag(
    dag_id='Basic Airflow Check',
    default_args=dag_arguments
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
    task_id='print date',
    bash_command='date +%d%m%y',
    dag=dag
)

dummy_task >> python_task >> Bash_task