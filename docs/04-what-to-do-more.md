# Validation

There is a lot of ways to validate the ETL process and results. For example, dbt is one of the great way to validate the pipeline.

However, you can use BigQueryValueCheckOperator to add a simple validation task to your dag. 
```python
check_value = BigQueryValueCheckOperator(
    task_id="check_value",
    sql=f"SELECT COUNT(*) FROM {DATASET}.{TABLE_1}",
    pass_value=4,
    use_legacy_sql=False,
    location=location,
)
```
'