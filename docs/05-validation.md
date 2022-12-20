# Validation

There is a lot of ways to validate the ETL process and results. For example, [`dbt`](https://www.getdbt.com/) is a great way to validate the pipeline.

However, you can utilize Airflow Operators such as `BigQueryValueCheckOperator` or `BigQueryCheckOperator` to add a simple validation task to your DAG. 

## `BigQueryValueCheckOperator`

```python
from airflow.providers.google.cloud.operators.bigquery import BigQueryValueCheckOperator

check_value = BigQueryValueCheckOperator(
    task_id="check_value",
    sql='validation_query.sql',
    pass_value=0,
    gcp_conn_id='google_cloud_conn_id',
    use_legacy_sql=False,
)
```
This operator checks if the result of the SQL query is equal to `pass_value`. 

For example, if you want to validate that none of the rows in target table has `duration_minutes` value less than 100, 
you could write following query and set `pass_value` to 0. 
```sql
-- validation_query.sql 

SELECT count(*)
FROM test_dataset.long_trips
WHERE duration_minutes < 100
```

## `BigQueryCheckOperator`

```python
from airflow.providers.google.cloud.operators.bigquery import BigQueryCheckOperator

check_value = BigQueryCheckOperator(
    task_id="check_value",
    sql='validation_query.sql',
    gcp_conn_id='google_cloud_conn_id',
    use_legacy_sql=False,
)
```
This operator checks if every row of the result of the SQL query is `true`. 

For example, if you want to validate that at least one row in the target table have `duration_minutes` bigger than 1000,
you can write the following query. 
```sql
-- validation_query.sql 

SELECT count(*)
FROM test_dataset.long_trips
WHERE duration_minutes > 1000
```
This validation will only fail if the count(*) == 

## Full Code
Following DAG executes ETL process with 2 validation tasks. 
```python
# tutorial_dag_with_validation.py

from __future__ import annotations

from datetime import datetime

from airflow import models
from airflow.contrib.operators.bigquery_operator import BigQueryOperator
from airflow.providers.google.cloud.operators.bigquery import \
    BigQueryValueCheckOperator, BigQueryCheckOperator

project_id = "starlit-sum-372013"
destination_table_id = "test_dataset.long_trips"

with models.DAG(
    dag_id="test_etl_dag_with_validation",
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

    validate_1 = BigQueryValueCheckOperator(
        task_id="validate_1",
        sql="bigquery_value_check.sql",
        pass_value=0,
        gcp_conn_id="google_cloud_conn_id",
        use_legacy_sql=False,
    )

    validate_2 = BigQueryCheckOperator(
        task_id="validate_2",
        sql="bigquery_check.sql",
        gcp_conn_id="google_cloud_conn_id",
        use_legacy_sql=False,
    )

    run_etl >> validate_1 >> validate_2
```
```sql
-- query.sql
SELECT *
FROM test_dataset.trips
WHERE duration_minutes > 100;
```
```sql
-- bigquery_value_check.sql
SELECT count(*)
FROM test_dataset.long_trips
WHERE duration_minutes < 100;
```

```sql
-- biquery_check.sql
SELECT count(*)
FROM test_dataset.long_trips
WHERE duration_minutes > 1000;
```

For more information, please refer to the [GitHub Repository](https://github.com/yoonhyejin/airflow-with-bigquery-guide/blob/main/dags/tutorial_dag_with_validation.py).  
