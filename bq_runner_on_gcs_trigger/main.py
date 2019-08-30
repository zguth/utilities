import os
from google.cloud import bigquery

# Variables
TARGET_DATASET = '[CHANGE_TO_TARGET_DATASET]'
TARGET_TABLE = '[CHANGE_TO_TARGET_TABLE]'

# GCP libraries
client = bigquery.Client()

def load_dapo(data, context):
    fileUri = getFileLink(data)
    print("Run triggered by file: {}.".format(fileUri))

    table_ref = client.dataset(TARGET_DATASET).table(TARGET_TABLE)
    job_config = bigquery.LoadJobConfig()
    job_config.write_disposition = bigquery.WriteDisposition.WRITE_EMPTY
    job_config.source_format = bigquery.SourceFormat.CSV
    job_config.field_delimiter = '|'
    load_job = client.load_table_from_uri(fileUri, table_ref, job_config=job_config)  # API request
    load_job.result()  # Waits for table load to complete.

    job_config = bigquery.LoadJobConfig()

    for sql in readFilesFromDir('sql'):
        query_job = client.query(sql)  # API request
        query_job.result()  # Waits for query to finish

    print("Processing finished for file: {}.".format(fileUri))

def getFileLink(data):
    return "gs://" + data['bucket'] + "/" + data['name']

def readFilesFromDir(dir):
    files = []
    for file in os.listdir(dir):
        filepath = os.path.join(dir, file)
        f = open(filepath, 'r')
        files += f.readlines()
        f.close()
    return files
