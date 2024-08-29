import os
import boto3
from dotenv import load_dotenv

load_dotenv()

def get_dynamodb_table(table_name: str):
    dynamodb_endpoint = os.getenv('DYNAMODB_ENDPOINT_URL', None)
    dynamodb = boto3.resource('dynamodb',
            endpoint_url=dynamodb_endpoint,
            region_name=os.getenv('AWS_DEFAULT_REGION', 'fakeRegion'),
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID', 'fakeMyKeyId'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY', 'fakeSecretAccessKey')
        )
    return dynamodb.Table(table_name)

def create_funds(table_name: str):
    table = get_dynamodb_table(table_name)

    fondos = [
        {"FundId": '1', "Name": "FPV_BTG_PACTUAL_RECAUDADORA", "MinAmount": 75000, "Category": "FPV"},
        {"FundId": '2', "Name": "FPV_BTG_PACTUAL_ECOPETROL", "MinAmount": 125000, "Category": "FPV"},
        {"FundId": '3', "Name": "DEUDAPRIVADA", "MinAmount": 50000, "Category": "FIC"},
        {"FundId": '4', "Name": "FDO-ACCIONES", "MinAmount": 250000, "Category": "FIC"},
        {"FundId": '5', "Name": "FPV_BTG_PACTUAL_DINAMICA", "MinAmount": 100000, "Category": "FPV"}
    ]

    for fondo in fondos:
        table.put_item(Item=fondo)

def create_test_user(table_name: str):
    table = get_dynamodb_table(table_name)

    user = {
        "ClientId": '1',
        "Name": "Test User",
        "Email": "femonres@gmail.com",
        "Phone": "+573107863381",
        "Notification": "email",  # Preferencia de notificación
        "Balance": 500000  # Saldo inicial
    }

    table.put_item(Item=user)

if __name__ == "__main__":
    create_funds("FundTable")
    create_test_user("ClientTable")