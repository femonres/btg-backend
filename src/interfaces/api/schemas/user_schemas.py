from typing import List
from pydantic import BaseModel, EmailStr

from domain import NotificationType
from application import UserDTO

class SubscriptionResponse(BaseModel):
    id: str
    fund_id: int
    fund_name: str
    amount: int

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
    subscriptions: List[SubscriptionResponse] = []

    class Config:
        from_attributes = True

def convert_to_user_response(user_dto: UserDTO) -> UserResponse:
    subscriptions_response = [SubscriptionResponse(**sub.model_dump()) for sub in user_dto.subscriptions]
    
    return UserResponse(
        id=user_dto.id,
        name=user_dto.name,
        email=user_dto.email,
        phone=user_dto.phone,
        balance=user_dto.balance,
        notification=user_dto.notification,
        subscriptions=subscriptions_response
    )