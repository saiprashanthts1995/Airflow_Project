# Airflow_Project
Orchestrate Data Engineering activities using Airflow

## for the purpose of this project, I have provisioned Apache Airflow which is present in AWS as an serverless service. I have provisioned a server which is of small worker for practice purpose with only one worker. Below Image shows the Airflow environemnt created using AWS
![AWS_Airflow](https://github.com/saiprashanthts1995/Airflow_Project/blob/main/images/airflow.PNG)

## Below represents the list of task which I have accomplised using the Airflow environment which was created before

1. Basic Airflow DAG - to experience Bash, Python and Dummy operator.
![Basic](https://github.com/saiprashanthts1995/Airflow_Project/blob/main/images/basic.PNG)
2. Python Operator with arguments and Jinja Template using Bash Operator. Output of Jinja operator is shown below
![Jinja_Python_Argument](https://github.com/saiprashanthts1995/Airflow_Project/blob/main/images/Jinja.PNG)
3. S3_Key sensor to check if file is present
![S3_Key](https://github.com/saiprashanthts1995/Airflow_Project/blob/main/images/look_for_s3.PNG)
4. Cross Communication- helps to pass output fro one airflow operator to another
![Xcom](https://github.com/saiprashanthts1995/Airflow_Project/blob/main/images/xcom.PNG)
Below, I have represented how the XCOM tab looks, once we run the above dag of XCOM
![Xcom_Output](https://github.com/saiprashanthts1995/Airflow_Project/blob/main/images/xcom1.PNG)
5. List of Dags and storage of Dags in S3 for Apache Airflow( AWS serverless) to execute
![List_of_Dags](https://github.com/saiprashanthts1995/Airflow_Project/blob/main/images/list_of_Dags.PNG)
![Bucket_List](https://github.com/saiprashanthts1995/Airflow_Project/blob/main/images/s3.PNG)

## Created By Sai Prashanth T S
### Email : saiprashanthts@gmail.com
