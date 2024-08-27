from typing import List

from domain import Fund, FundRepository, FundNotFoundException
from infrastructure.persistence.daos.fund_dao import FundDAO


class DynamoDBFundRepositoryImpl(FundRepository):
    def __init__(self, dynamodb_table):
        self.table = dynamodb_table

    def get_all(self) -> List[Fund]:
        response = self.table.scan()
        items = response.get('Items', [])
        return [FundDAO.from_dynamo_item(item) for item in items]

    def find_by_id(self, fund_id: int) -> Fund:
        response = self.table.get_item(Key={'fund_id': fund_id})
        item = response.get('Item')

        if not item:
            raise FundNotFoundException(fund_id)

        return FundDAO.from_dynamo_item(item)

    def update(self, fund: Fund):
        item = FundDAO.to_dynamo_item(fund)
        self.table.put_item(Item=item)