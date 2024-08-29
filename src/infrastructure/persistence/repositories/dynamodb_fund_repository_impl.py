from domain import Fund, FundRepository, FundNotFoundException
from infrastructure.persistence.daos.fund_dao import FundDAO
from infrastructure.config.dynamodb_config import get_dynamodb_table
from utils.error_utils import handle_exception


class DynamoDBFundRepositoryImpl(FundRepository):
    def __init__(self, table_name: str):
        self.table = get_dynamodb_table(table_name)

    def get_all(self) -> list[Fund]:
        try:
            response = self.table.scan()
            items = response.get('Items', [])
            return [FundDAO.from_dynamo_item(item) for item in items]
        except Exception as err:
            handle_exception(err)
            return []

    def get_by_id(self, fund_id: int) -> Fund:
        try:
            response = self.table.get_item(Key={'FundId': str(fund_id)})
            item = response['Item']
            if not item:
                raise FundNotFoundException(fund_id)

            return FundDAO.from_dynamo_item(item)
        except Exception as err:
            handle_exception(err)
            raise FundNotFoundException(fund_id)