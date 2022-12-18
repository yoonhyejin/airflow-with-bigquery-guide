from __future__ import annotations
from datetime import datetime

from airflow import models
from airflow.contrib.operators.bigquery_operator import BigQueryOperator

project_id = 'starlit-sum-372013'
source_table_id = 'test_dataset.trips'
destination_table_id = 'test_dataset.long_trips'

with models.DAG(
    dag_id="test_etl_dag",
    schedule="@once",
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["example", "bigquery"],
) as dag:

    bq_extract_one_day = BigQueryOperator(
        task_id='bq_extract_one_day',
        sql='query.sql',
        destination_dataset_table=destination_table_id,
        write_disposition='WRITE_TRUNCATE',
        gcp_conn_id='google_cloud_conn_id',
        use_legacy_sql=False
    )