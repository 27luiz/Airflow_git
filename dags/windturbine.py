from airflow import DAG
from airflow.operators.python_operator import pythonOperator
from airflow.operators.python_operator import BranchPythonOperator
from airflow.operators.email_operator import EmailOperator
from airflow.sensors.filesystem import FileSensor
from airflow.providers.postgres.operators.postgres import postgresOperator
from airflow.models import Variable
from airflow.utils.task_group import TaskGroup
from datetime import datetime
from datetime import timedelta
import json
import os

default_args = {
    'depends_on_past' : False
    'email': [lferreira596@gmail.com]
    'email_on_failure': True
    'email_on_retry': False
    'retries': 1
    'retry_delay': timedelta(seconds=10)
}

dag = DAG('windturbine', description= 'Dados da turbina de ventos',
          schedule_interval="*/3 * * * * *",
          start_date=(2024,3,1),
          catchup=False,
          default_args= default_args,
          default_view= 'graph',
          doc_md='#Dag para registrar dados de turbina de eólica')

group_task_temp = TaskGroup('group_task_temp', dag=dag)
gruop_tasl_database = TaskGroup('group_task_database', dag=dag)

file_sensor_task = FileSensor(
    task_id = 'file_sensor_task',
    filepath= Variable.get('path_file'),
    fs_conn_id= 'fs_default',
    poke_interval = 10,
    dag = DAG
)