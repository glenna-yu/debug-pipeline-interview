# debug-pipeline-interview

This repo contains an Airflow dag to download data weather data from ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/. 
There is a Docker image with Airflow and the dag installed on it that you can use to run Airflow and trigger the dag. 
The Makefile provides a few helpful commands for interacting with the Docker image (building, running the container, ssh-ing, etc.)

The goal is eventually to be able to download all the `.dly` files from ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/all/ for stations from 
each state, starting with New York. However, the pipeline is incomplete and a little buggy. 

Take a look around the repo and feel free to ask your interviewer any questions you might have about Airflow or the data. 