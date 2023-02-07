from airflow import DAG
from datetime import datetime
from airflow.sensors.http_sensor import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python_operator import PythonOperator
from pandas import json_normalize
import json
import os

os.environ["no_proxy"]="*"


def _process_user(ti):
        user = ti.xcom_pull(task_ids='extract_user')
        user = user['results'][0]
        processed_user = json_normalize({'firstname': user['name']['first'],
                'lastname': user['name']['last'],
                'country':user['location']['country'],
                'username': user['login']['username'],
                'email': user['email']
        })
        print(processed_user)
        processed_user.to_csv('/tmp/prograssed_user.csv')

with DAG('user_processing',start_date = datetime(2022,11,11),
        schedule_interval='@daily',catchup=False) as Dag:
        
        is_api_available = HttpSensor(
                task_id = 'is_api_available',
                http_conn_id = 'user_api',
                endpoint='api/')

        extract_user = SimpleHttpOperator(
                task_id = 'extract_user',
                http_conn_id = 'user_api',
                endpoint='api/',
                method='GET',
                response_filter=lambda response: json.loads(response.text),
                log_response =True)

        process_user = PythonOperator(
                task_id ='process_user',
                python_callable = _process_user)
        
is_api_available >> extract_user >> process_user

