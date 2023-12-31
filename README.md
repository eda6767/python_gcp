# Python on Google Cloud Platform

<sub>
In this scenario we are gonna create pipeline with enrichment data in Python using Cloud Compute engine, Airflow and BigQuery. The task will indicate if given transaction is transaction - paying invoice, paying for renting a flat, salary etc. </sub> 

<br/> 
<sub>
Useful materials for this task:

<br/> 
</br> 
https://cloud.google.com/python/docs/setup#linux
<br/> 
https://cloud.google.com/bigquery/docs/reference/libraries#client-libraries-install-python 
<br/> 
https://cloud.google.com/appengine/docs/standard/python3/specifying-dependencies 
</sub> 


<br/> 
<br/> 

<sub>
In first step we will prepare and create virtual machine with python installed and other libraries required to our task.
</sub> 

<p align="center">
</p>


<sub>

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

</sub> 

<br/> 
</br> 

<sub> Compute Engine allows you to define commands to be executed when creating a machine. The list of commands has to be placed in Startup scripts window </sub> 

<br/> 
</br> 
<img width="500" alt="Zrzut ekranu 2023-10-11 o 21 08 57" src="https://github.com/eda6767/python_gcp/assets/102791467/ec1cd1ee-6a84-40a1-9d9e-fa5e4284fa43">

<br/> 
</br> 

<sub>
After creating Compute Engine, we are albe to test connection between out new VM and data on BigQuery, let's test with given code:
</sub> 


<sub>
    
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
</sub>



<sub> Unfortunatelly we optained an error: </sub>


<sub>
    
```
google.api_core.exceptions.Forbidden: 403 Access Denied: BigQuery BigQuery: Missing required OAuth scope. Need BigQuery or Cloud Platform read scope.
```

</sub>
<br/> 

<sub>
That is why now we have to give permission to service account and edit virtual machines. For this purpose we need a service account with permission: BigQuery Job User and BigQuery Data Viewer. After creating proper service account, we can stop and then edit VM substituting service account: </sub>

<p align="center">
<img width="500" alt="Zrzut ekranu 2023-09-10 o 16 37 53" src="https://github.com/eda6767/python_gcp/assets/102791467/79903a61-e972-4d39-9e1f-0a43a40d943b">
</p>

<br/> 
</br> 
<sub>
After changing the service account for a service with proper permissions we can run python script on Compute Engine after SSH: </sub>

<br/> 
</br> 

<sub>
    
```
python3 bg_client_test.py
```
</sub>


<br/> 
</br> 

<img width="500" alt="Zrzut ekranu 2023-10-11 o 21 17 38" src="https://github.com/eda6767/python_gcp/assets/102791467/dedbace2-43e3-49de-aa82-44dfc7bcecfd">

<br/> 
</br> 

<sub>
To save solution to BigQuery wee need to create a schema in LoadJobConfig, because columns with string values are represented in Python as an "object" dtype.
</sub>

<br/> 
</br> 

<sub>

```
job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("crnt_acct_pkg_trx_key", "STRING"),
        bigquery.SchemaField("sys_cd", "STRING"),
        bigquery.SchemaField("acct_key", "STRING"),
        bigquery.SchemaField("acct_id", "STRING"),
        bigquery.SchemaField("frst_acct_key", "STRING"),
        bigquery.SchemaField("main_acct_id", "STRING"),
        bigquery.SchemaField("title", "STRING"),
        bigquery.SchemaField("receiver_acct_key", "STRING"),
        bigquery.SchemaField("receiver_acct_id", "STRING"),
        bigquery.SchemaField("receiver_nm_address", "STRING"),
        bigquery.SchemaField("rejection_rsn_dsc", "STRING"),
        bigquery.SchemaField("sender_nm_address", "STRING"),
        bigquery.SchemaField("tech_etl_pkg_cd", "STRING")
    ]
)

job = client.load_table_from_dataframe(tagger.tagged, dpcrnt_acct_pkg_trx_fcd, job_config=job_config)

```
</sub>
