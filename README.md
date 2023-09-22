# Python on Google Cloud Platform

<sub/>
In this scenario we are gonna create pipeline with enrichment data in Python using Cloud Compute engine, Airflow and BigQuery. The task will indicate if given transaction is transaction - paying invoice, paying for renting a flat, salary etc.

<br/> 
Useful materials for this task:

<br/> 
<br/>  https://cloud.google.com/python/docs/setup#linux <br/> 

<br/>  https://cloud.google.com/bigquery/docs/reference/libraries#client-libraries-install-python <br/> 

<br/>  https://cloud.google.com/appengine/docs/standard/python3/specifying-dependencies <br/> 


<br/> 
<br/> 
In first step we will prepare and create virtual machine with python installed.

<p align="center">
</p>




```
sudo apt update
sudo apt install python3 python3-dev python3-venv python3-distutils
sudo apt-get install python3-distutils
sudo apt-get install wget
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
bg_client_test.py
pip3 install --upgrade google-cloud-bigquery
pip3 install 'google-cloud-bigquery[pandas]'
pip3 install pandas-gbq
pip3 install pandas
pip3 install numpy
pip3 install pandas-gbq
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
That is why now we have to give permission to service account and edit virtual machines. <br/> 

For this purpose we need a service account with permission: BigQuery Job User and BigQuery Data Viewer. <br/> 

After creating proper service account, we can stop and then edit VM substituting service account:<br/> 

<p align="center">
<img width="500" alt="Zrzut ekranu 2023-09-10 o 16 37 53" src="https://github.com/eda6767/python_gcp/assets/102791467/79903a61-e972-4d39-9e1f-0a43a40d943b">
</p>


