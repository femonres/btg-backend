
from pydantic import BaseModel

class DomainEvent(BaseModel):
    occurred_on: str

    class Config:
        arbitrary_types_allowed = True