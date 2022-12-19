# Validation

There is a lot of ways to validate the ETL process and results. For example, [`dbt`](https://www.getdbt.com/) is one of the great way to validate the pipeline.

However, you can utilize Airflow Operators such as `BigQueryValuCheckOperator` or `BigQueryCheckOperator` to add a simple validation task to your dag. 

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
This will only fail if the count(*) == 0. 