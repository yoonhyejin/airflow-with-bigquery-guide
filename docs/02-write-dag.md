# Write DAG with ETL Tasks

We will use BigQueryOperator to load data. 

```bash
dags/
  query.sql
  tutorial_dags.py
```
You will need two files : 
In `tutorial_dags.py`, we will define the DAG that contains BigQueryOperator. 
In `query.sql`, we will write a SQL query to load data.

## Create a Model Object with BigQueryOperator

First, create a dag model with PythonOperator in `tutorial_dags.py`.  
```python

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
```
run_etl_processor function will trigger ETL process that we will define in the seperate file. 


## Full code

query.sql

```sql
SELECT *
FROM test_dataset.trips
WHERE duration_minutes > 100;
```

tutorial_dag.py 
```python

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
```