from utils.formatters import format_currency


class InsufficientBalanceException(Exception):
    def __init__(self, fund_name: str, message="No tiene saldo disponible para vincularse al fondo"):
        self.message = f"{message}: {fund_name}"
        super().__init__(self.message)

class CanInvestException(Exception):
    def __init__(self, fund_name: str, min_amount, message="El monto con el cual desea vincularse al fondo"):
        self.message = f"{message}: {fund_name}, es inferior el minimo requerido: {format_currency(min_amount.value)}"
        super().__init__(self.message)

class FundNotFoundException(Exception):
    def __init__(self, fund_id: int, message="Fondo no encontrado."):
        self.message = f"{message} ID: {fund_id}"
        super().__init__(self.message)

class SubscriptionAlreadyException(Exception):
    def __init__(self, fund_name: str, message="El cliente ya está suscrito al fondo"):
        self.message = f"{message}: {fund_name}."
        super().__init__(self.message)

class SubscriptionNotFoundException(Exception):
    def __init__(self, fund_name: str, message="No hay suscripción activa para el fondo"):
        self.message = f"{message}: {fund_name}"
        super().__init__(self.message)

class UserNotFoundException(Exception):
    def __init__(self, user_id: int, message="Usuario no encontrado."):
        self.message = f"{message} ID: {user_id}"
        super().__init__(self.message)
