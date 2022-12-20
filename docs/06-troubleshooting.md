# Troubleshooting

This page lists common problems you might face while following the guide. 

## docker-compose
### Cannot connect to the Docker daemon

> Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?

You need a docker engine running locally to deploy Airflow via docker-compose. Check if the docker is running.

## Running DAGs

### DAG Import Errors 

![dag-import-errors](/airflow-with-bigquery-guide/img/dag-import-errors.png)

In most cases, DAG import errors occur due to syntax errors in a DAG file.
For example, it might be missing dependencies or the wrong configuration of the import path. 
It is best to follow the logs and debug the problem cause.


### Error 403: Permission denied on resource project

> Error: googleapi: Error 403: Permission denied on resource project {project_id}., forbidden

Check if the service account has valid permissions on the target GCP project to perform the desired task. 
