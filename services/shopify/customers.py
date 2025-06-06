from config import SHOPIFY_TABLE_CUSTOMERS
from db.db_connection import BigQuery
from google.cloud import bigquery


class ShopifyCustomers:
    async def customers(shopify_topic, shopify_webhook_id, shopify_event_id, data):

        query = f"""
        INSERT INTO `{SHOPIFY_TABLE_CUSTOMERS}`
        (`x-shopify-webhook-id`, `x-shopify-topic`, `x-shopify-event-id`, `data`)
        VALUES (@shopify_webhook_id, @shopify_topic, @shopify_event_id, @data)
        """

        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter(
                    "shopify_webhook_id", "STRING", shopify_webhook_id),
                bigquery.ScalarQueryParameter(
                    "shopify_topic", "STRING", shopify_topic),
                bigquery.ScalarQueryParameter(
                    "shopify_event_id", "STRING", shopify_event_id),
                bigquery.ScalarQueryParameter(
                    "data", "JSON", data)
            ]
        )

        result = await BigQuery.run_query_and_return(
            query=query, job_config=job_config)

        return result
