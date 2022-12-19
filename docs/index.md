# A Friendly Guide to integrate Airflow with BigQuery
Airflow is a great tool used for scheduling and executing ETL(Extract, Transform, Load) in modern data engineering. 
Also, BigQuery is one of the most frequently used data warehouses for ETL because of its flexibility and convenience.

This guide introduces how to create a simple batch ETL pipeline by integrating Airflow with BigQuery.
The following tutorial is appropriate for users who have a basic understanding of the ETL process, Airflow, and Bigquery.

## Requirements
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Google Cloud Platform](https://cloud.google.com/) account and project

## Goals
- Create a simple DAG that writes a BigQuery SQL result to a BigQuery table
- Create basic validation tasks using Airflow Operators

## Non-goals
* Deploy Airflow on a cloud environment
* Cover complicated data transformation process
* Integrate with external data sources other than BigQuery