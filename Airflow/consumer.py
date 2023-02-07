from airflow import DAG, Dataset 
from airflow.decorators import task

from datetime import datetime

Data_set = Dataset("/Users/esakkimuthumurugan/Downloads/my_file.txt")
Data_set_2 = Dataset("/Users/esakkimuthumurugan/Downloads/my_file_2.txt")


with DAG(
    dag_id="consumer",
    schedule=[Data_set,Data_set_2],
    start_date=datetime(2022,11,26),
    catchup=False
    ) as dag:

    @task
    def read_dataset():
        with open(Data_set.uri,'r') as f:
            print(f.read())
    @task
    def read_dataset_2():
        with open(Data_set_2.uri,'r') as f:
            print(f.read())
    read_dataset()
    read_dataset_2()