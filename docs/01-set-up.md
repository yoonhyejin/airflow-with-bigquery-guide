# Set Up 

## Deploy Airflow on Local Environment
This guide uses [docker-compose](https://github.com/docker/compose) to deploy Airflow on the local environment to help you start from scratch. 
If you already have Airflow deployed on a cloud environment, please skip this part.

> Make sure you have [Docker Desktop](https://www.docker.com/products/docker-desktop/) engine running on the local environment before installation. 

```bash
# download docker-compose.yaml for Airflow 
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml'
mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env

# execute init process
docker-compose up airflow-init

# install all components
docker-compose up
```
Visit `localhost:8080` in the browser and log in with default credentials.
```bash
id: airflow
password: airflow
```
Now, you will see the list of example DAGs.
![airflow-example-dags](/airflow-with-bigquery-guide/img/airflow-example-dags.png)

Refer to [the official document of apache airflow](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/pipeline.html) for more information.

## Create Raw BigQuery Table
You will need a BigQuery table as a raw data source in your GCP project.
We will use the `bigquery-public-data.austin_bikeshare.bikeshare_trips` dataset to create a dummy table.

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
