import datetime
from pydantic import BaseModel


class DomainEvent(BaseModel):
    occurred_on: datetime