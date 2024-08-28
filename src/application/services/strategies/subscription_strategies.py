from domain import ValidationStrategy, Amount, User, Fund, SubscriptionAlreadyException, InsufficientBalanceException, CanInvestException


class SubscriptionAlreadyValidation(ValidationStrategy):
    def validate(self, user: 'User', fund: 'Fund', amount: Amount):
        if user.is_subscribed(fund):
            raise SubscriptionAlreadyException(fund.name)

class InsufficientBalanceValidation(ValidationStrategy):
    def validate(self, user: 'User', fund: 'Fund', amount: Amount):
        if user.balance.value < amount.value:
            raise InsufficientBalanceException(fund.name)

class MinimumAmountValidation(ValidationStrategy):
    def validate(self, user: 'User', fund: 'Fund', amount: Amount):
        if not fund.can_invest(amount):
            raise CanInvestException(fund.name, fund.min_amount)