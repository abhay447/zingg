from zingg.client import *
from zingg.pipes import *
import os 
from databricks_cli.sdk.api_client import ApiClient
from databricks_cli.jobs.api import JobsApi
from databricks_cli.runs.api import RunsApi 
from copy import deepcopy
import datetime
import time

nowTime = str(time.time_ns())
name = 'findTrainingData' + nowTime
task_key = nowTime
job_spec = {
  'new_cluster': {
      'spark_version': '7.3.x-scala2.12',
      'spark_conf': {
          'spark.databricks.delta.preview.enabled': 'true'
        },
      'node_type_id': 'm5.large',
      'spark_env_vars': {
          'PYSPARK_PYTHON': '/databricks/python3/bin/python3'
        },
      'enable_elastic_disk': 'true',
      'num_workers': 1
    },
  'timeout_seconds': 0,
  'email_notifications': {},
  'name': name,
  'max_concurrent_runs': 1,
  'tasks' : [{
      'task_key': task_key,
      'notebook_path': '/Users/sonal@zingg.ai/FebrlExample',
      "source": "WORKSPACE"
      }]
  }

print ('calling api client')
api_client = ApiClient(
  host  = os.getenv('DATABRICKS_HOST'),
  token = os.getenv('DATABRICKS_TOKEN')
)

jobs_api = JobsApi(api_client)
job = jobs_api.create_job(job_spec)
print(job)

job['notebook_params'] = {}
runs_api = RunsApi(api_client) 
jobs_api.run_now(job['job_id'], None, None, None, None)


