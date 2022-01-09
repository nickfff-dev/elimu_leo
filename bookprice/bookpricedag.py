# bookpricedag.py in 'dags' folder
import datetime as dt
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
# start_date argument is used to tell scheduler when the DAG instance to be scheduled
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 10, 5, 23, 00),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
# schedule_interval argument is used to tell scheduler how frequently a specific task to be executed
dag = DAG(dag_id='bookpricedag', default_args=default_args,
          schedule_interval=timedelta(days=1))
# tasks are defined with the BashOperator
# actual tasks to be defined in a seperate python file
t1 = BashOperator(
    task_id='booksTbc',
    bash_command='run_Tbc_spider',
    dag=dag
)
t2 = BashOperator(
    task_id='booksNuria',
    bash_command='run_Nuria_spider',
    dag=dag
)
t3 = BashOperator(
    task_id='booksPrestige',
    bash_command='run_Prestige_spider',
    dag=dag
)

# this tells the scheduler in which order the tasks to be executed.
# in our case, t2 will start after t1 finished
# same applys for the others
t1 >> t2 >> t3 
