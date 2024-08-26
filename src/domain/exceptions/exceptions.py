class InsufficientBalanceException(Exception):
    def __init__(self, fund_name, message="No tiene saldo disponible para vincularse al fondo"):
        self.message = f"{message}: {fund_name}"
        super().__init__(self.message)

class CanInvestException(Exception):
    def __init__(self, fund_name, min_amount, message="El monto con el cual desea vincularse al fondo"):
        self.message = f"{message}: {fund_name}, es inferior el minimo requerido: {min_amount}"
        super().__init__(self.message)

class FundNotFoundException(Exception):
    def __init__(self, fund_id, message="Fondo no encontrado."):
        self.message = f"{message} ID: {fund_id}"
        super().__init__(self.message)

class SubscriptionNotFoundException(Exception):
    def __init__(self, fund_name, message="No hay suscripción activa para este fondo."):
        self.message = f"{message} Fondo: {fund_name}"
        super().__init__(self.message)
