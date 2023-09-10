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
