# Set up

## Set Up Airflow
For test purposes, this guide uses quickstart installation to deploy airflow on local environment. 
If you already have airflow deployed on cloud environment, please skip this part.

Make sure you have Docker Desktop engine running on local environment before installation. 

```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml'
mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env
docker-compose up airflow-init
docker-compose up
```
Visit `localhost:8080` in the browser and login with default credentials.
```bash
id: airflow
password: airflow
```
Now, you will see the list of example dags.
![airflow-example-dags](/img/airflow-example-dags.png)

Refer to [the official document of apache airflow](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/pipeline.html) for more information.

## Create Raw BigQuery Table
You will need a BigQuery table as a raw data source in your GCP project.
We will use bigquery-public-data to create a dummy table.

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

## Create a Google Cloud Connection

You need a service account that contains following permissions.

* bigquery.jobs.create
* bigquery.tables.getData 
* bigquery.tables.create 

Visit IAM > Service Account > Create a Service Account and create a service account with the following role.

* BigQuery User 
* BigQuery Data Editor 

![add-sa](/img/add-sa.png)

Add a Key and download it on local as json format. 
![add-sa-key](/img/add-sa-key.png)

On Airflow UI, go to Admin > Connections. Create a connection with following configuration.

![add-connection](/img/add-connection.png)

* Connection Id : Your preferable connection id (ex. google-cloud-conn-id)
* Connection Type : Google Cloud
* Project Id : Your GCP project id
* Keyfile JSON : Full content of your service account key json file 


Now you're ready to write DAG! 