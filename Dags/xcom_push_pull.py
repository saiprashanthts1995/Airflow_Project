from airflow import DAG
from datetime import datetime
from airflow.operators import BashOperator, DummyOperator, PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta


def push_function(ti, **kwargs):
    """
    Simple Python Function to push value
    :return:
    """
    a = 1
    b = 2
    c = a + b
    ti.xcom_push(key='c', value=c)
    return a+b


def receive_function(ti, **kwargs):
    """
    to receive the value from XCOM
    :param ti: cross function element
    :return:
    """
    output = ti.xcom_pull(key='c', task_ids=['Xcom_Push'])
    print(output)


dag_arguments = {
    'Owner': 'Sai',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    dag_id='Xcom_Push_Pull',
    default_args=dag_arguments,
    description='A simple tutorial DAG',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2)
)

dummy_task = DummyOperator(
    task_id='Start',
    dag=dag
)

push_task = PythonOperator(
    task_id='Xcom_Push',
    python_callable=push_function,
    provide_context=True,
    dag=dag
)

pull_task = PythonOperator(
    task_id='Xcom_Pull',
    python_callable=receive_function,
    provide_context=True,
    dag=dag
)

dummy_task >> push_task >> pull_task