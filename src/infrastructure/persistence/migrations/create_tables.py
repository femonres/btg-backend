import boto3

def create_tables():
    dynamodb = boto3.resource('dynamodb')

    # Crear tabla para Usuarios
    dynamodb.create_table(
        TableName='Users',
        KeySchema=[
            {'AttributeName': 'user_id', 'KeyType': 'HASH'},
        ],
        AttributeDefinitions=[
            {'AttributeName': 'user_id', 'AttributeType': 'N'},
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5,
        }
    )

    # Crear tabla para Fondos
    dynamodb.create_table(
        TableName='Funds',
        KeySchema=[
            {'AttributeName': 'fund_id', 'KeyType': 'HASH'},
        ],
        AttributeDefinitions=[
            {'AttributeName': 'fund_id', 'AttributeType': 'N'},
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5,
        }
    )

    print("Tablas creadas con éxito.")