# Run pipeline

## Trigger DAG 
Place `tutorial_dag.py` and `query.sql` under `/dags` directory like below. 
After slight delay, you can search the DAG on Web UI. 

Activate and trigger the DAG manually. 

## Check Data on BigQuery

After the DAG is finished successfully, check the BigQuery destination table to see the data mart that is just created.

![destination-table](/airflow-with-bigquery-guide/img/destination-table.png)