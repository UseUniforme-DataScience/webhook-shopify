import asyncio
from datetime import datetime
import json
from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd

with open("config.json") as f:
    service_account_info = json.load(f)

credentials = service_account.Credentials.from_service_account_info(
    service_account_info
)

bq_client = bigquery.Client(credentials=credentials,
                            project=credentials.project_id)


class BigQuery:
    @staticmethod
    async def run_query_and_return(
        query: str, job_config: bigquery.QueryJobConfig = None
    ) -> pd.DataFrame:
        def run_query():
            start_time = datetime.now()
            job = bq_client.query(query=query, job_config=job_config).result()
            
            end_time = datetime.now()
            total_time = (end_time - start_time).microseconds / 1000
            print(f"Total time: {total_time} ms")

            return job

        return await asyncio.to_thread(run_query)