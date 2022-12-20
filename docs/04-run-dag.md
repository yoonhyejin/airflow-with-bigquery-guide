# Run pipeline

## Trigger DAG 
Place `tutorial_dag.py` and `query.sql` under the `./dags` directory like below. 
```tree
├── dags
│   ├── tutorial_dag.py
│   └── query.sql
```
After a slight delay, you can search the DAG by `dag_id` on Airflow UI. 

![trigger-dag](/airflow-with-bigquery-guide/img/trigger-dag.png)
Activate and trigger the DAG manually. 

## Check Data on BigQuery

After the DAG finishes successfully, check the BigQuery destination table to see the data mart as a result.

![destination-table](/airflow-with-bigquery-guide/img/destination-table.png)
