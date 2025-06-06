from fastapi import FastAPI
from routers.shopify.customers import shopify_customers
from routers.shopify.orders import shopify_orders


app = FastAPI(title="Webhooks Use", version="1.0.0")

app.include_router(shopify_customers)
app.include_router(shopify_orders)
