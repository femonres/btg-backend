from pydantic import BaseModel


class TransactionDTO(BaseModel):
    transaction_id: str
    user_id: int
    fund_id: int
    fund_name: str
    amount: int
    timestamp: str
    transaction_type: str