from typing import List, Optional

from domain import User, UserRepository, UserNotFoundException
from infrastructure.persistence.daos.user_dao import UserDAO
from infrastructure.config.dynamodb_config import get_dynamodb_table


class DynamoDBUserRepositoryImpl(UserRepository):
    def __init__(self, table_name: str):
        self.table = get_dynamodb_table(table_name)

    def get_all(self) -> list[User]:
        response = self.table.scan()
        items = response.get('Items', [])
        return [UserDAO.from_dynamo_item(item) for item in items]

    def get_by_id(self, user_id: int) -> Optional[User]:
        response = self.table.get_item(
            Key={
                'PK': f'CLIENT#{user_id}',
                'SK': f'#METADATA#{user_id}'
            }
        )
        item = response.get('Item')
        if item:
            return UserDAO.from_dynamo_item(item)
        return None

    def save(self, user: User):
        item = UserDAO.to_dynamo_item(user)
        self.table.put_item(Item=item)
