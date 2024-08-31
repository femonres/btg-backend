from pydantic import BaseModel

from domain import Amount


class TransactionResponse(BaseModel):
    transaction_id: str
    fund_id: int
    fund_name: str
    amount: int
    timestamp: str
    transaction_type: str

    class Config:
        from_attributes = True

class SubscriptionSchema(BaseModel):
    user_id: int
    fund_id: int
    amount: float

class CreateSubscription(BaseModel):
    user_id: int
    amount: int

class CancelSubscription(BaseModel):
    user_id: int