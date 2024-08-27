from pydantic import BaseModel

from domain import Amount, FundCategory, PreferNotification, TransactionStatus, TransactionType


class SubscriptionDTO(BaseModel):
    user_id: int
    fund_id: int
    amount: Amount

    class Config:
        arbitrary_types_allowed = True

class CancellationDTO(BaseModel):
    user_id: int
    fund_id: int

class UserDTO(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    notification: PreferNotification
    balance: Amount

    class Config:
        arbitrary_types_allowed = True

class FundDTO(BaseModel):
    id: int
    name: str
    min_amount: Amount
    category: FundCategory

    class Config:
        arbitrary_types_allowed = True

class TransactionDTO(BaseModel):
    transaction_id: str
    fund_id: int
    amount: Amount
    timestamp: str
    transaction_type: TransactionType
    status: TransactionStatus

    class Config:
        arbitrary_types_allowed = True