import pytest
from unittest.mock import MagicMock

from domain import Amount, User, NotificationType, UserRepository, UserNotFoundException
from application import UserService

@pytest.fixture
def setup_mocks():
    user_repo = MagicMock(UserRepository)
    
    user = User(
        id=1,
        name="Usuario de Prueba",
        email="prueba@example.com",
        phone="+573107863381",
        notification=NotificationType.EMAIL,
        balance=Amount(200000)
    )
    
    user_repo.get_by_id.return_value = user
    
    user_service = UserService(user_repo)
    
    return {
        'user_service': user_service,
        'user_repo': user_repo,
        'user': user
    }

def test_get_user_profile(setup_mocks):
    user_service = setup_mocks['user_service']
    user_repo = setup_mocks['user_repo']
    user = setup_mocks['user']

    result = user_service.get_user_profile(user_id=1)
    
    user_repo.get_by_id.assert_called_once_with(1)
    assert result == user

def test_get_user_profile_not_found(setup_mocks):
    user_service = setup_mocks['user_service']
    user_repo = setup_mocks['user_repo']
    
    user_repo.get_by_id.return_value = None

    with pytest.raises(UserNotFoundException):
        user_service.get_user_profile(user_id=1)

def test_update_profile(setup_mocks):
    user_service = setup_mocks['user_service']
    user_repo = setup_mocks['user_repo']
    user = setup_mocks['user']
    
    updated_user = User(
        name="Nombre Completo",
        email="femonres@example.com",
        phone="+1789654323",
        notification=NotificationType.SMS,
    )

    result = user_service.update_profile(user_id=1, user=updated_user)
    
    user_repo.get_by_id.assert_called_once_with(1)
    user_repo.save.assert_called_once_with(result)
    
    assert user.name != updated_user.name
    assert user.email != updated_user.email
    assert user.phone != updated_user.phone
    assert user.notification != updated_user.notification

    assert result.name == updated_user.name
    assert result.email == updated_user.email
    assert result.phone == updated_user.phone
    assert result.notification == updated_user.notification

def test_update_profile_not_found(setup_mocks):
    user_service = setup_mocks['user_service']
    user_repo = setup_mocks['user_repo']
    
    user_repo.get_by_id.return_value = None

    updated_user = User(
        name="Nombre Completo",
        email="femonres@example.com",
        phone="+1789654323",
        notification=NotificationType.SMS,
    )

    with pytest.raises(UserNotFoundException):
        user_service.update_profile(user_id=1, user=updated_user)

def test_reset_balance(setup_mocks):
    user_service = setup_mocks['user_service']
    user_repo = setup_mocks['user_repo']
    user = setup_mocks['user']

    user_repo.get_by_id.return_value = None
    
    result = user_service.reset_balance(user_id=1)
    
    user_repo.get_by_id.assert_called_once_with(1)
    user_repo.save.assert_called_once_with(result)
    
    assert user.balance != Amount(500000)
    assert len(user.subscriptions) != 0

    assert result.balance == Amount(500000)
    assert len(result.subscriptions) == 0

def test_reset_balance_not_found(setup_mocks):
    user_service = setup_mocks['user_service']
    user_repo = setup_mocks['user_repo']
    
    user_repo.get_by_id.return_value = None

    with pytest.raises(UserNotFoundException):
        user_service.reset_balance(user_id=1)
