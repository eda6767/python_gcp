# Python on Google Cloud Platform

<sub/>
In this scenario we are gonna create pipeline with enrichment data in Python using Cloud Compute engine, Airflow and BigQuery. The task will indicate if given transaction is transaction - paying invoice, paying for renting a flat, salary etc.

<br/> 
<br/> 
In first step we will prepare and create virtual machine with python installed.

<p align="center">
</p>




```
sudo apt update
sudo apt install python3 python3-dev python3-venv
sudo apt-get install python3-distutils
sudo apt-get install wget
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
pip3 --version

```


```
pip install --upgrade google-cloud-bigquery
```

To test connection between out new VM and data on BigQuery, let's test with given code:

```
from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

query = """
    SELECT *
    FROM `coral-mariner-396009.data.table`
"""
query_job = client.query(query)  # Make an API request.

print(query_job)

df = client.query(query).to_dataframe()

print(df.head())
```

Unfortunatelly we optained an error:
```
google.api_core.exceptions.Forbidden: 403 Access Denied: BigQuery BigQuery: Missing required OAuth scope. Need BigQuery or Cloud Platform read scope.
```
That is why now we have to give permission to service account
