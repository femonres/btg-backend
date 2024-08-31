from pydantic import BaseModel


class FundDTO(BaseModel):
    id: int
    name: str
    min_amount: int
    category: str