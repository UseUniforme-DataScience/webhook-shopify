from fastapi import APIRouter, Request
from services.shopify.orders import ShopifyOrders


shopify_orders = APIRouter(prefix="/shopify")


@shopify_orders.post("/orders")
async def manage_orders(request: Request):
    headers = request.headers
    shopify_topic = headers.get("x-shopify-topic")
    shopify_webhook_id = headers.get("x-shopify-webhook-id")
    shopify_event_id = headers.get("x-shopify-event-id")

    body = await request.body()
    body = body.decode("utf-8")

    await ShopifyOrders.order(shopify_topic, shopify_webhook_id, shopify_event_id, body)

    return {"message": "OK"}
