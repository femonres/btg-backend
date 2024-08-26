import uuid

from pydantic import BaseModel

class Identifier(BaseModel):
    id: str

    @staticmethod
    def generate() -> 'Identifier':
        return Identifier(id=str(uuid.uuid4()))