from pydantic import BaseModel
from datetime import datetime

from application import FundDTO, SubscriptionDTO, TransactionDTO, UserDTO
from domain import Amount, PreferNotification, TransactionStatus, TransactionType

class SubscriptionSchema(BaseModel):
    user_id: int
    fund_id: int
    amount: float

    def to_domain(self) -> SubscriptionDTO:
        return SubscriptionDTO(
            user_id=self.user_id,
            fund_id=self.fund_id,
            amount=self.amount
        )

class UserSchema(BaseModel):
    user_id: int
    name: str
    email: str
    phone: str
    notification: str
    balance: int

    @classmethod
    def from_domain(cls, user: UserDTO):
        return cls(
            user_id=user.id,
            name=user.name,
            email=user.email,
            phone=user.phone,
            notification=user.notification.value,
            balance=user.balance.value
        )

    def to_domain(self) -> UserDTO:
        return UserDTO(
            id=self.user_id,
            name=self.name,
            email=self.email,
            phone=self.phone,
            notification=PreferNotification(self.notification),
            balance=self.balance
        )

class FundSchema(BaseModel):
    fund_id: int
    name: str
    min_amount: float
    category: str

    @classmethod
    def from_domain(cls, fund: FundDTO):
        return cls(
            fund_id=fund.id,
            name=fund.name,
            min_amount=fund.min_amount.value,
            category=fund.category,
        )

class TransactionSchema(BaseModel):
    transaction_id: int
    fund_id: int
    amount: float
    timestamp: str
    transaction_type: str
    status: str

    @classmethod
    def from_domain(cls, transaction: TransactionDTO):
        return cls(
            transaction_id=transaction.transaction_id,
            fund_id=transaction.fund_id,
            amount=transaction.amount.value,
            timestamp=transaction.timestamp.isoformat(),
            transaction_type=transaction.transaction_type.value,
            status=transaction.status.value,
        )
