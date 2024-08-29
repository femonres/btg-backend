from pydantic import BaseModel, EmailStr

from domain import NotificationType
from application import UserDTO

class SubscriptionResponse(BaseModel):
    id: str
    fund_id: int
    amount: float

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    notification: NotificationType

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    balance: int
    notification: str
    subscriptions: list[SubscriptionResponse] = []

    class Config:
        from_attributes = True
