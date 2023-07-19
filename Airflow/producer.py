from airflow import DAG, Dataset
from airflow.decorators import task

from datetime import datetime

Data_set = Dataset("/Users/esakkimuthumurugan/Downloads/my_file.txt")
Data_set_2 = Dataset("/Users/esakkimuthumurugan/Downloads/my_file_2.txt")


with DAG(
    dag_id = "producer",
    schedule="@daily",
    start_date=datetime(2022,11,26),
    catchup=False
    ) as dag:

    @task(outlets=[Data_set])
    def update_dataset():
        with open(Data_set.uri,'a+') as f:
            f.write('Producer Update')

    @task(outlets=[Data_set_2])
    def update_dataset_2():
        with open(Data_set_2.uri,'a+') as f:
            f.write('Producer Update')

    update_dataset()
    update_dataset_2()
