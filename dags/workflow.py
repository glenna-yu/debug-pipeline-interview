from datetime import datetime

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from tasks.download_data import download_data
from tasks.join_stations_and_states import get_station_data, join_stations_and_states


default_args = {
    "owner": "Enigma",
    "depends_on_past": False,
    "start_date": datetime(2019, 1, 1),
    "retries": 0,
}

dag = DAG("debug_pipeline", default_args=default_args, schedule_interval=None)

download_data_task = PythonOperator(
    task_id="download_stations_data",
    python_callable=download_data,
    dag=dag,
)

join_stations_and_states_task = PythonOperator(
    task_id="join_stations_and_states",
    python_callable=join_stations_and_states,
    op_kwargs={
        "stations_path": "ghcnd-stations.txt",
        "states_path": "ghcnd-states.txt",
        "output_path": "/root/data/stations-and-states.csv",
    },
    dag=dag,
)

get_station_data_task = PythonOperator(
    task_id="get_station_data",
    python_callable=get_station_data,
    dag=dag,

)

download_data_task.set_downstream(join_stations_and_states_task)
join_stations_and_states_task.set_downstream(get_station_data_task)
