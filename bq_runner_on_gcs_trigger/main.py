import os
from google.cloud import bigquery

# GCP libraries
client = bigquery.Client()

def run_sql_scripts(data, context):
    print("Run triggered by file: {}.".format(data['objectId']))

    for sql in readFilesFromDir('sql'):
        query_job = client.query(sql)  # API request
        query_job.result()  # Waits for query to finish

    print("Processing finished for file: {}.".format(data['objectId']))

def readFilesFromDir(dir):
    files = []
    for file in os.listdir(dir):
        filepath = os.path.join(dir, file)
        f = open(filepath, 'r')
        files += f.readlines()
        f.close()
    return files
