import pandas as pd
import pyarrow
import pyarrow.parquet as pq
import wget
from sqlalchemy import create_engine
from time import time
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


dag = DAG(dag_id='yellow_cabs_dag', start_date=datetime(2024, 2, 12))

def yellow_cabs_upload():

    conn_string = 'postgresql://oluwaseyi:root@postgres_seyi:5432/yellow_cabs_db'
    db = create_engine(conn_string)
    final_df = []
    for month in ['%0.2d' % i for i in range(1, 2)]:
        result = wget.download(f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-{month}.parquet')
        table = pq.read_table(result)
        new_table = table.to_pandas()
        final_df.append(new_table)

        new_df = pd.concat(final_df)
    print(new_df.head())
    new_df.to_csv('yellow_cabs_report.csv')


with dag:
    download_upload_data = PythonOperator(task_id='yellow_cabs_upload',python_callable=yellow_cabs_upload)

download_upload_data
