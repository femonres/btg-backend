import pytest
from domain import User, Amount, Fund, PreferNotification, FundCategory, InsufficientBalanceException
from application import SubscribeToFundUseCase, SubscriptionDTO


@pytest.fixture
def user():
    return User(
            id=1,
            name="John Doe",
            email="john.doe@example.com",
            phone="+573104567890",
            notification=PreferNotification.EMAIL,
            balance=Amount(500000)
        )

@pytest.fixture
def fund():
    return Fund(
            id=1,
            name="FPV_BTG_PACTUAL_RECAUDADORA",
            min_amount=Amount(75000),
            category=FundCategory(category='FPV')
        )

def test_subscribe_to_fund_success(mocker, user, fund):
    mock_fund_service = mocker.Mock()
    use_case = SubscribeToFundUseCase(mock_fund_service)

    subscription_dto = SubscriptionDTO(user_id=user.id, fund_id=fund.id, amount=Amount(50000))

    use_case.execute(subscription_dto=subscription_dto)
    
    assert user.balance.value == 500000
    assert len(user.transactions) == 0
