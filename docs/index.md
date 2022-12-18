# A Friendly Guide to integrate Airflow with BigQuery

ETL(Extract, Tranform, Load) is a core processes of modern data engineering. Especially, BigQuery is one of the most frequently used data warehouse because of its flexibilty and convienience.

This guide introduces how to create simple batch ETL pipeline through integrating Airflow with BigQuery.
This guide is appropriate for users who have basic understanding of ETL process and basic experience of airflow and bigquery.

## Requirements

- Airflow is deployed on cloud environment
- Valid GCP account and project

## Goals
- Create a simple ETL pipeline that loads data mart from raw bigquery table.

## Non-goals
* Building Airflow from zero-base 
* Network, Infra-related issues
* Complicated data transformation process