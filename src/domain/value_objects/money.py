from pydantic import BaseModel, Field, field_validator


class Money(BaseModel):
    amount: int = Field(gt=0)

    def add(self, other: 'Money') -> 'Money':
        return Money(amount=self.amount + other.amount)

    def subtract(self, other: 'Money') -> 'Money':
        return Money(amount=self.amount - other.amount)