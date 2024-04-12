FROM apache/airflow:2.8.0

ENV AIRFLOW_HOME=/opt/airflow

USER root

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         vim \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

USER $AIRFLOW_UID

RUN pip install pandas sqlalchemy psycopg2-binary pyarrow fastparquet wget

WORKDIR $AIRFLOW_HOME

USER $AIRFLOW_UID
# docker run --network oluwaseyi covid19_image
# docker build -t covid19_image .
