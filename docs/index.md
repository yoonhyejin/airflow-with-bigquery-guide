# A Friendly Guide to integrate Airflow with BigQuery
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fyoonhyejin.github.io%2Fairflow-with-bigquery-guide%2F&count_bg=%233964C3&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

Airflow is a popular tool for scheduling and executing ETL(Extract, Transform, Load) in modern data engineering. 
Also, BigQuery is one of the most frequently used data warehouses for ETL because of its flexibility and convenience.

This guide introduces how to create a simple batch ETL pipeline by integrating Airflow with BigQuery.
The following tutorial is appropriate for users who understand the ETL process, Airflow, and Bigquery.

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
