import datetime
from domain import Amount, TransactionType, Transaction, TransactionRepository
from infrastructure.persistence.daos.transaction_dao import TransactionDAO
from infrastructure.config.dynamodb_config import get_dynamodb_table


class DynamoDBTrasacctionRepositoryImpl(TransactionRepository):
    def __init__(self, table_name: str):
        self.table = get_dynamodb_table(table_name)

    def save(self, transaction: Transaction):
        item = TransactionDAO.to_dynamo_item(transaction)
        self.table.put_item(Item=item)

    def find_by_user_id(self, client_id: int) -> list[Transaction]:
        response = self.table.query(
            KeyConditionExpression='PK = :pk and begins_with(SK, :sk)',
            ExpressionAttributeValues={
                ':pk': f'CLIENT#{client_id}',
                ':sk': 'TRANSACTION#'
            }
        )
        items = response.get('Items', [])
        transactions = []
        for item in items:
            transaction = TransactionDAO.from_dynamo_item(item)
            transactions.append(transaction)
        return transactions
