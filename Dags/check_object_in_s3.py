from airflow import DAG
from airflow.operators import DummyOperator, BashOperator
from airflow.sensors import S3KeySensor
from airflow.utils.dates import days_ago

default_args = {
    'Owner': 'Sai Prashanth T S',
    'depends_on_past': False
}

dag = DAG(
    dag_id='Look_for_file_in_s3',
    start_date=days_ago(2),
    default_args=default_args,
    description='Check for a file in s3'
)

dummy_task = DummyOperator(
    task_id='Start',
    dag=dag
)

list_files_task = BashOperator(
    task_id='List_Files',
    bash_command='aws s3 ls s3://sai-learn-airflow/ --recursive',
    dag=dag
)

copy_file_task = BashOperator(
    task_id='Copy_file',
    bash_command='aws s3 cp s3://sai-learn-airflow/packages/requirement.txt s3://sai-learn-airflow/a/requirement.txt',
    dag=dag
)

s3_key_sensor = S3KeySensor(
    task_id='S3_Check_file_sensor',
    bucket_key='s3://sai-learn-airflow/dags/basic_dag.py',
    poke_interval=5,
    timeout=20,
    dag=dag
)

dummy_task >> list_files_task >> copy_file_task >> s3_key_sensor