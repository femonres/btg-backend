import uuid

class Identifier:
    def __init__(self, id: str):
        self.id = id

    @staticmethod
    def generate() -> 'Identifier':
        return Identifier(id=str(uuid.uuid4()))

    def __repr__(self):
        return f"Identifier(id={self.id!r})"

    def __eq__(self, other):
        if isinstance(other, Identifier):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)