from typing import Dict

from domain import Fund, Amount, FundCategory


class FundDAO:

    @staticmethod
    def to_dynamo_item(fund: Fund) -> Dict:
        return {
            'PK': f'CLIENT#{fund.id}',
            'SK': f'#METADATA#{fund.id}',
            'Name': fund.name,
            'MinAmount': fund.min_amount.value,
            'Category': fund.category.category
        }
    
    @staticmethod
    def from_dynamo_item(item: Dict) -> Fund:
        return Fund(
            id=int(item['PK'].split('#')[1]),
            name=item['Name'],
            min_amount=Amount(item['MinAmount']),
            category=FundCategory(category=item['Category'])
        )