ARG AIRFLOW_VERSION=3.0.3
ARG PYTHON_VERSION=3.11

FROM apache/airflow:${AIRFLOW_VERSION}-python${PYTHON_VERSION}

USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev git curl \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

USER airflow
COPY requirements.txt /requirements.txt
COPY constraints.txt /constraints.txt
RUN pip install --no-cache-dir -r /requirements.txt --constraint /constraints.txt
