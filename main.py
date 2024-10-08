import json 
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'airscholar',
    'start_date': datetime(2023, 9, 3, 10, 00)
}

def get_data():
    import requests

    res=requests.get('')
    res=res.json()
    res=res['results'][0]

def format_data():
    data={}

def stream_data():
    import requests

    res=requests.get("https://randomuser.me/api/")
    res=res.json()
    res=res['results'][0]

    print(res)

with DAG('user_automation',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    streaming_task = PythonOperator(
        task_id='stream_data_from_api',
        python_callable=stream_data
    )