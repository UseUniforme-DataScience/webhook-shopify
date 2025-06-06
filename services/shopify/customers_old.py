
import json


class ShopifyCustomers:
    @staticmethod
    def get_person_fields(data: json):
        formatted_json = {
            "id": data.get("id") or None,
            "email": data.get("email") or None,
            "created_at": data.get("created_at") or None,
            "updated_at": data.get("updated_at") or None,
            "first_name": data.get("first_name") or None,
            "last_name": data.get("last_name") or None,
            "orders_count": data.get("orders_count") or None,
            "state": data.get("state") or None,
            "total_spent": data.get("total_spent") or None,
            "last_order_id": data.get("last_order_id") or None,
            "note": data.get("note") or None,
            "verified_email": data.get("verified_email") or None,
            "multipass_identifier": data.get("multipass_identifier") or None,
            "tax_exempt": data.get("tax_exempt") or None,
            "tags": data.get("tags") or None,
            "last_order_name": data.get("last_order_name") or None,
            "currency": data.get("currency") or None,
            "phone": data.get("phone") or None,
            "tax_exemptions": data.get("tax_exemptions") or None,
            "email_marketing_consent": data.get("email_marketing_consent", {}).get("state") or None,
            "sms_marketing_consent": data.get("sms_marketing_consent", {}).get("state") or None,
            "admin_graphql_api_id": data.get("admin_graphql_api_id") or None,
            "admin_graphql_api_id": data.get("admin_graphql_api_id") or None,
        }

        return formatted_json

    def customers_create(content: json):
        data = ShopifyCustomers.get_person_fields(content)
        print(content)
        print("---------------------------------")
        print(json.dumps(data, indent=4))

    def customers_delete(content: json):
        print(content)

    def customers_disable(content: json):
        print(content)

    def customers_enable(content: json):
        print(content)

    def customers_update(content: json):
        print(content)
