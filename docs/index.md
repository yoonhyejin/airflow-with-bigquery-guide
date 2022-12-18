# A Friendly Guide to integrate Airflow with BigQuery

ETL(Extract, Tranform, Load) is a core process of modern data engineering. 
Especially, BigQuery is one of the most frequently used data warehouse for ETL because of its flexibilty and convienience.

This guide introduces how to create simple batch ETL pipeline through integrating Airflow with BigQuery.
This guide is appropriate for users who have basic understanding of ETL process and basic experience of airflow and bigquery.

## Requirements
- Docker Desktop is installed on local environment
- Valid GCP project

## Goals
- Create a simple ETL pipeline that loads data mart from raw bigquery table.

## Non-goals
* Deploying Airflow on cloud environment
* Executing ETL pipeline on cloud environment
* Covering complicated data transformation process