# import the libraries

from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks!
from airflow.operators.bash_operator import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago

#defining DAG arguments

# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'yosef',
    'start_date': days_ago(0),
    'email': ['yosef@somemail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# defining the DAG

# define the DAG
dag = DAG(
    'insert-to-database-dag',
    default_args=default_args,
    description='My first DAG',
    schedule_interval=timedelta(days=1),
)


insert_to_db = BashOperator(
    task_id='insert_to_db',
    bash_command='python ../scripts/inset_to_db.py',
    dag=dag,
)

insert_to_db