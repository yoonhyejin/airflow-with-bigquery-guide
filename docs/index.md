# A Friendly Guide to integrate Airflow with BigQuery
Airflow is a great tool used for scheduling and executing ETL(Extract, Tranform, Load) in modern data engineering. 
Also, BigQuery is one of the most frequently used data warehouse for ETL because of its flexibilty and convienience.

This guide introduces how to create simple batch ETL pipeline through integrating Airflow with BigQuery.
Following tutorial is appropriate for users who have basic understanding of ETL process, Airflow and Bigquery.

## Requirements
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Google Cloud Platform](https://cloud.google.com/) account and project

## Goals
- Create a simple DAG that writes a BigQuery SQL result to a BigQuery table
- Create a basic validation tasks using Airflow Operators

## Non-goals
* Deploy Airflow on cloud environment
* Cover complicated data transformation process
* Integrate with external data sources other than BigQuery