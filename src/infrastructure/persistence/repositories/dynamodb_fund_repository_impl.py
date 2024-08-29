from domain import Fund, FundRepository, FundNotFoundException
from infrastructure.persistence.daos.fund_dao import FundDAO
from infrastructure.config.dynamodb_config import get_dynamodb_table


class DynamoDBFundRepositoryImpl(FundRepository):
    def __init__(self, table_name: str):
        self.table = get_dynamodb_table(table_name)

    def get_all(self) -> list[Fund]:
        response = self.table.scan()
        items = response.get('Items', [])
        return [FundDAO.from_dynamo_item(item) for item in items]

    def get_by_id(self, fund_id: int) -> Fund:
        response = self.table.get_item(
            Key={
                'PK': f'FUND#{fund_id}',
                'SK': f'#METADATA#{fund_id}'
            }
        )
        item = response.get('Item')

        if not item:
            raise FundNotFoundException(fund_id)

        return FundDAO.from_dynamo_item(item)