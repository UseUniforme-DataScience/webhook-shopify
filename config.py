import os
from dotenv import load_dotenv
from zoneinfo import ZoneInfo

load_dotenv(override=True)

SHOPIFY_TABLE_CUSTOMERS = os.getenv("SHOPIFY_TABLE_CUSTOMERS")
SHOPIFY_TABLE_ORDERS = os.getenv("SHOPIFY_TABLE_ORDERS")
TIMEZONE = ZoneInfo("America/Sao_Paulo")
