import os
import boto3
from dotenv import load_dotenv

load_dotenv()
def get_dynamodb_table(table_name: str):
    if os.getenv("ENVIRONMENT") == "develop":
        dynamodb_endpoint = os.getenv('DYNAMODB_ENDPOINT_URL', None)
        dynamodb = boto3.resource('dynamodb',
            endpoint_url=dynamodb_endpoint,
            region_name=os.getenv('AWS_DEFAULT_REGION', 'fakeRegion'),
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID', 'fakeMyKeyId'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY', 'fakeSecretAccessKey'))
    else:
        dynamodb = boto3.resource('dynamodb',
            region_name=os.getenv('AWS_DEFAULT_REGION', 'us-west-2'))

    
    return dynamodb.Table(table_name)
