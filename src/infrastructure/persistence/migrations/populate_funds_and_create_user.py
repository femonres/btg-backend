import boto3

def create_funds(table_name: str):
    dynamo_db = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamo_db.Table(table_name)

    fondos = [
        {"id": 1, "name": "FPV_BTG_PACTUAL_RECAUDADORA", "min_amount": 75000, "category": "FPV"},
        {"id": 2, "name": "FPV_BTG_PACTUAL_ECOPETROL", "min_amount": 125000, "category": "FPV"},
        {"id": 3, "name": "DEUDAPRIVADA", "min_amount": 50000, "category": "FIC"},
        {"id": 4, "name": "FDO-ACCIONES", "min_amount": 250000, "category": "FIC"},
        {"id": 5, "name": "FPV_BTG_PACTUAL_DINAMICA", "min_amount": 100000, "category": "FPV"}
    ]

    for fondo in fondos:
        table.put_item(Item=fondo)

def create_test_user(table_name: str):
    dynamo_db = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamo_db.Table(table_name)

    user = {
        "id": 1,
        "name": "Test User",
        "email": "femonres@gmail.com",
        "phone": "+573107863381",
        "notification": "email",  # Preferencia de notificación
        "balance": 500000  # Saldo inicial
    }

    table.put_item(Item=user)

if __name__ == "__main__":
    create_funds("FundsTable")
    create_test_user("UsersTable")