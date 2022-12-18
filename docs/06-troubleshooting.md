# Troubleshooting

### Cannot connect to the Docker daemon. Is the docker daemon running on this host?
You need docker engine running locally to deploy airflow via docker-compose. Check if the docker is running.

### Error 403: Permission denied on resource project
Check if the service account has valid permissions on target GCP project to perform desired task. 
