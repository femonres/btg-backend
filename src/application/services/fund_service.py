from typing import List

from domain import FundRepository, Fund

class FundService:
    def __init__(self, fund_repo: FundRepository):
        self.fund_repo = fund_repo

    def get_all_funds(self) -> List[Fund]:
        return self.fund_repo.get_all()