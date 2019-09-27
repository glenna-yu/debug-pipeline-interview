FROM python:3.7-slim-buster

WORKDIR /root

ENV AIRFLOW_HOME /root/airflow

ENV AIRFLOW__CORE__LOAD_EXAMPLES False

RUN apt-get update && apt-get install -y gcc nano vim

COPY requirements.txt /root/

RUN pip install --upgrade pip && pip install --trusted-host pypi.python.org -r /root/requirements.txt

COPY script/entrypoint /root/script/entrypoint

COPY dags/ /root/airflow/dags/

EXPOSE 8080

ENTRYPOINT [ "bash", "/root/script/entrypoint" ]
