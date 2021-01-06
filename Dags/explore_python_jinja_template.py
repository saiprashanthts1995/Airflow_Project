from airflow import DAG
from datetime import datetime
from airflow.operators import BashOperator, DummyOperator, PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta


def hello_world(name, **kwargs):
    """
    Simple Python Function to print hello
    :return:
    """
    print('hello to {}'.format(name))


dag_arguments = {
    'Owner': 'Sai',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    dag_id='Hello_Python_Operator_With_Argument',
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
    python_callable=hello_world,
    op_kwargs={"name": 'Sai Prashanth T S'},
    dag=dag
)

templated_command = """
{% for i in range(7) %}
    echo "{{ ds }}"
    echo "{{ macros.ds_add(ds, 7)}}"
    echo "{{ params.Name }}"
{% endfor %}
"""

Jinja_task = BashOperator(
    task_id='Jinja_Template',
    depends_on_past=False,
    bash_command=templated_command,
    params={'Name': 'Sai Prashanth T S'},
    dag=dag,
)

dummy_task >> python_task >> Jinja_task