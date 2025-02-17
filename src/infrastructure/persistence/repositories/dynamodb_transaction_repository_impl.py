from boto3.dynamodb.conditions import Key

from domain import Transaction, TransactionRepository
from infrastructure.persistence.daos.transaction_dao import TransactionDAO
from infrastructure.config.dynamodb_config import get_dynamodb_table
from utils.singleton import singleton
from utils.error_utils import handle_exception

@singleton
class DynamoDBTrasacctionRepositoryImpl(TransactionRepository):
    def __init__(self, table_name: str):
        self.table = get_dynamodb_table(table_name)

    def save(self, transaction: Transaction):
        item = TransactionDAO.to_dynamo_item(transaction)
        self.table.put_item(Item=item)

    def find_by_user_id(self, user_id: int) -> list[Transaction]:
        try:
            response = self.table.query(IndexName='ClientIDIndex', KeyConditionExpression = Key('ClientID').eq(str(user_id)))

            items = response.get('Items', [])
            transactions = []
            for item in items:
                transaction = TransactionDAO.from_dynamo_item(item)
                transactions.append(transaction)
            return transactions
        except Exception as err:
            handle_exception(err)
            return []

