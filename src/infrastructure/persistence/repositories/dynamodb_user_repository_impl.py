from typing import List

from domain import User, UserRepository, UserNotFoundException
from infrastructure.persistence.daos.user_dao import UserDAO


class DynamoDBUserRepositoryImpl(UserRepository):
    def __init__(self, dynamodb_table):
        self.table = dynamodb_table

    def get_all(self) -> List[User]:
        response = self.table.scan()
        items = response.get('Items', [])
        return [UserDAO.from_dynamo_item(item) for item in items]

    def get_by_id(self, user_id: int) -> User:
        response = self.table.get_item(Key={'id': user_id})
        item = response.get('Item')

        if not item:
            raise UserNotFoundException(user_id)

        return UserDAO.from_dynamo_item(item)
    
    def save(self, user: User):
        item = UserDAO.to_dynamo_item(user)
        self.table.put_item(Item=item)

    def update(self, user: User):
        item = UserDAO.to_dynamo_item(user)
        self.table.update_item(Item=item)