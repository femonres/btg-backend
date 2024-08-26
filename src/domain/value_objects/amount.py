class Amount:
    def __init__(self, value: int):
        if value < 0:
            raise ValueError("El monto no puede ser negativo")
        self.value = value

    def __eq__(self, other):
        if isinstance(other, Amount):
            return self.value == other.value
        return False

    def __add__(self, other):
        if isinstance(other, Amount):
            return Amount(self.value + other.value)
        raise ValueError("Operación inválida")

    def __sub__(self, other):
        if isinstance(other, Amount):
            return Amount(self.value - other.value)
        raise ValueError("Operación inválida")

    def __repr__(self):
        return f"Amount({self.value})"
