from pydantic import BaseModel


class FundResponse(BaseModel):
    id: int
    name: str
    min_amount: int
    category: str
