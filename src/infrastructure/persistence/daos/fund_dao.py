from typing import Dict

from domain import Fund, Amount, FundCategory


class FundDAO:

    @staticmethod
    def to_dynamo_item(fund: Fund) -> Dict:
        return {
            'id': fund.id,
            'name': fund.name,
            'min_amount': fund.min_amount,
            'category': fund.category.category
        }
    
    @staticmethod
    def from_dynamo_item(item: Dict) -> Fund:
        return Fund(
            id=item['id'],
            name=item['name'],
            min_amount=Amount(item['min_amount']),
            category=FundCategory(item['category'])
        )