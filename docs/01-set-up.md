# Set Up 

## Set Up Airflow on Local Environment
This guide uses docker-compose to deploy Airflow on local environment. 
If you already have Airflow deployed on cloud environment, please skip this part.

Make sure you have Docker Desktop engine running on local environment before installation. 

```bash
# download docker-compose.yaml for Airflow 
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml'
mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env

# exeucte init process
docker-compose up airflow-init

# install all components
docker-compose up
```
Visit `localhost:8080` in the browser and login with default credentials.
```bash
id: airflow
password: airflow
```
Now, you will see the list of example dags.
![airflow-example-dags](/airflow-with-bigquery-guide/img/airflow-example-dags.png)

Refer to [the official document of apache airflow](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/pipeline.html) for more information.

## Create Raw BigQuery Table
You will need a BigQuery table as a raw data source in your GCP project.
We will use `bigquery-public-data.austin_bikeshare.bikeshare_trips` dataset to create a dummy table.

```sql
CREATE TABLE {your_dataset_name}.trips AS (
  SELECT
    bikeid,
    start_time,
    duration_minutes
  FROM
    bigquery-public-data.austin_bikeshare.bikeshare_trips
);
```