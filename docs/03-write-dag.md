# Write DAG with ETL Tasks

In this part, we will write a simple DAG that performs an ETL task with `BigQueryOperator`. 
BigQueryOperator executes BigQuery SQL query and saves the result to the destination table, a great way to create a pipeline that loads a data mart from another table. 

You will need two files under the `./dags` directory: 

* `tutorial_dags.py`: we will define the DAG that contains BigQueryOperator. 
* `query.sql`: we will write a query to load data.

## Create a Model Object with BigQueryOperator

First, create a DAG model with BigQueryOperator in `tutorial_dags.py`.  
```python

from airflow import models
from airflow.contrib.operators.bigquery_operator import BigQueryOperator

project_id = '{your_project_id}'
destination_table_id = '{your_dataset_id}.long_trips'

with models.DAG(
    dag_id="test_etl_dag",
    schedule="@once",
    start_date=datetime(2022, 12, 1),
    catchup=False,
    tags=["example", "bigquery"],
) as dag:

    run_etl = BigQueryOperator(
        task_id='run_etl',
        sql='query.sql',
        destination_dataset_table=destination_table_id,
        write_disposition='WRITE_TRUNCATE',
        gcp_conn_id='{your_custom_conn_id}', 
        use_legacy_sql=False
    )
```

Some of the basic parameters are like following: 

* `sql`: The SQL query to be executed. It can be either a file path or a raw string of SQL query.
* `destination_dataset_table`:  BigQuery table that will store the results of the query. (ex. `<dataset>.<table>`)
* `write_dispoistion`: Specifies the action that occurs if the destination table already exists.
     - `WRITE_EMPTY`: Write data if the destination table is empty.
     - `WRITE_TRUNCATE`: Overwrite the destination table data.
     - `WRITE_APPEND`: Append to the existing table data.
* `gcp_conn_id`: Reference to google cloud connection. 

For more information on `BigQueryOperator`, please refer to the [official documentation](https://airflow.apache.org/docs/apache-airflow/1.10.3/_api/airflow/contrib/operators/bigquery_operator/index.html).

## Write Query
In `query.sql`, we will define a simple query that filters row with duration_minutes of more than 100. 
```sql
SELECT *
FROM test_dataset.trips
WHERE duration_minutes > 100;
```

We will not cover complicated SQL syntax or transformation processes in this guide, but you can always look up more variations. 

Now that we have our DAG, let's run and test it! 
