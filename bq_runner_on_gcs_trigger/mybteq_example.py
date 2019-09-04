import os
from google.cloud import bigquery

# Variables
DATASET = os.environ.get('DATASET', 'Specified environment variable is not set.')

# GCP libraries
client = bigquery.Client()

def mybteq_example(data, context):
    print("Start processing.")

    # TODO just drop and recreate the table
    client.query("DELETE FROM " + DATASET + ".table WHERE true").result()

    mandants = [2, 23, 24]

    for mandant in mandants:
        client.query("SELECT " + str(mandant)).result() # API request

    print("Processing finished!")
