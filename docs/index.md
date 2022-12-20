# A Friendly Guide to integrate Airflow with BigQuery

[Airflow](https://airflow.apache.org/) is a popular workflow tool for scheduling and monitoring the ETL(Extract, Transform, Load) process in modern data engineering.
It allows users to create a data pipeline between various data sources such as RDBMS, API, spreadsheet, and data warehouse. 

[BigQuery](https://cloud.google.com/bigquery/), Google's managed data warehouse, is one of the most frequently used data warehouses for its flexibility and convenience.

This guide introduces how to create a simple batch ETL pipeline by integrating Airflow with BigQuery. 
The following tutorial is appropriate for users who have a basic experience with the ETL process, Bigquery, and writing Airflow DAG,

## Requirements
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Google Cloud Platform](https://cloud.google.com/) account and project

## Goals
- Create a simple DAG that writes a query result to a BigQuery table
- Create basic validation tasks using Airflow Operators

## Non-goals
* Deploy Airflow on a cloud environment
* Cover complicated data transformation process
* Integrate with external data sources other than BigQuery
