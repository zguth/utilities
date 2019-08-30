<img src="https://avatars2.githubusercontent.com/u/2810941?v=3&s=96" alt="Google Cloud Platform logo" title="Google Cloud Platform" align="right" height="96" width="96"/>

# Run BigQuery Sqls on GCS trigger

Steps:

* Put your SQL script into the sql directory
* Create a GCS bucket which will be watched
* Deploy the Cloud Functions code with the following command:
`gcloud functions deploy run_sql_scripts --trigger-resource [bucket] --runtime python37 --timeout=540s --region=europe-west1 --trigger-event google.storage.object.finalize`

