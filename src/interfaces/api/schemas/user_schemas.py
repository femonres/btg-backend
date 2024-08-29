from pydantic import BaseModel, EmailStr

from domain import NotificationType

class SubscriptionResponse(BaseModel):
    fund_id: int
    amount: float

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    notification: NotificationType

class UserResponse(BaseModel):
    id: str
    name: str
    email: str
    phone: str
    balance: float
    notification: NotificationType
    subscriptions: list[SubscriptionResponse]

    class Config:
        from_attributes = True
