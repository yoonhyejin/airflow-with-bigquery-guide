from __future__ import annotations

from datetime import datetime

from airflow import models
from airflow.contrib.operators.bigquery_operator import BigQueryOperator

project_id = "starlit-sum-372013"
destination_table_id = "test_dataset.long_trips"

with models.DAG(
    dag_id="test_etl_dag",
    schedule="@once",
    start_date=datetime(2022, 12, 1),
    catchup=False,
    tags=["example", "bigquery"],
) as dag:

    run_etl = BigQueryOperator(
        task_id="run_etl",
        sql="query.sql",
        destination_dataset_table=destination_table_id,
        write_disposition="WRITE_TRUNCATE",
        gcp_conn_id="google_cloud_conn_id",
        use_legacy_sql=False,
    )
