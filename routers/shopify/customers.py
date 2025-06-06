from fastapi import APIRouter, Request, Response
from services.shopify.customers import ShopifyCustomers

shopify_customers = APIRouter(prefix="/shopify")


@shopify_customers.post("/customers")
async def manage_customers(request: Request):
    headers = request.headers
    shopify_topic = headers.get("x-shopify-topic")
    shopify_webhook_id = headers.get("x-shopify-webhook-id")
    shopify_event_id = headers.get("x-shopify-event-id")

    body = await request.body()
    body = body.decode("utf-8")

    await ShopifyCustomers.customers_create(shopify_topic, shopify_webhook_id, shopify_event_id, body)

    return {"message": "OK"}
