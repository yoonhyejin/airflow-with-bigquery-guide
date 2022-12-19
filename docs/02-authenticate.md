# Authenticate Google Cloud Connection

To integrate Airflow with BigQuery, you need to set up a connection between GCP and Airflow.

## Create a GCP Service Account 

First, you need a GCP service account with specific permissions such as `bigquery.jobs.create`, 
`bigquery.tables.getData ` and `bigquery.tables.create `. 

Visit `IAM & Admin > Service Accounts` on GCP console and create a service account with the following role.

* BigQuery User 
* BigQuery Data Editor 

![add-sa](/airflow-with-bigquery-guide/img/add-sa.png)

After saving the service account, navigate to `Actions > Mnanage Keys `. 

![manage-keys](/airflow-with-bigquery-guide/img/manage-keys.png)


Go to `ADD KEY > Create new key` and select the key type as `JSON`. 
It will automatically download json file on local device. 

![add-sa-key](/airflow-with-bigquery-guide/img/add-sa-key.png)

## Add an Airflow Connection

On Airflow UI, go to `Admin > Connections`. Create a connection with following configuration.

![add-connection](/airflow-with-bigquery-guide/img/add-connection.png)

* Connection Id : Your preferable connection id (ex. google-cloud-conn-id)
* Connection Type : `Google Cloud`
* Project Id : Your GCP project id
* Keyfile JSON : Full content of your service account key json file 


Now you're ready to write DAG! 