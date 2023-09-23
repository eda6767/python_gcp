from google.cloud import bigquery
from KI_Predict_PKG import find_word, get_tagged_transactions, take_one_and_tag
import pandas as pd


# Construct a BigQuery client object.
client = bigquery.Client()
PROJECT="coral-mariner-396009"
query = """
    SELECT *
    FROM `coral-mariner-396009.kpr.crnt_acct_pkg_trx_fcd`
"""
query_job = client.query(query)  # Make an API request.

print(query_job)

df = client.query(query).to_dataframe()

print(df.head())


base_name=pd.DataFrame()
names=['Jack', 'Tom', 'Anna']
base_name['name']=imiona_lista


class PKGTransactionTagger():

    def __init__(self, dir_baza_imion=base_name, tagged=None):
        self.df_base_name = dir_baza_imion
        self.tagged = tagged

    def tag(self, data):

        taggedData = get_tagged_transactions(data, case_name=self.df_base_name,
                                             names='imie',
                                             receiver_name='receiver_nm_address',
                                             sender_name='sender_nm_address',
                                             receiver_acct='receiver_acct_id',
                                             sender_acct='acct_id',
                                             title_trx='title',
                                             trx_amount='trx_amt_pln')
        taggedData['tag_ind_ext_01']=taggedData['TAG01_ext']

        result=taggedData.drop(['TAG01_zew','pmt_classif','reverse_amount','internal'], axis=1)

        self.tagged = result
        
        return result


tagger=PKGTransactionTagger()
tagger.tag(df)

print(tagger.tagged.head())

PROJECT='coral-mariner-396009'
dpcrnt_acct_pkg_trx_fcd = "{}.agr.dpcrnt_acct_pkg_trx_fcd".format(PROJECT)

for i in tagger.tagged.columns:
    print(i)

print(tagger.tagged.dtypes)


# Since string columns use the "object" dtype, pass in a (partial) schema
# to ensure the correct BigQuery data type.
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
