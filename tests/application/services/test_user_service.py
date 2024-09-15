import pytest
from unittest.mock import MagicMock

from domain import Amount, User, NotificationType, UserRepository, UserNotFoundException
from application import UserService

@pytest.fixture
def user_service():
    mock_repo = MagicMock(spec=UserRepository)
    return UserService(user_repo=mock_repo)

@pytest.fixture
def user():
    return User(
        id=1, 
        name="John Doe", 
        email="john@example.com", 
        phone="1234567890", 
        notification=NotificationType.EMAIL, 
        balance=Amount(100000))

class TestUserService:

    def test_fetch_all(self, user_service: UserService, user: User):
        # Configura el mock para devolver una lista de usuarios
        user_service.user_repo.get_all.return_value = [user]
        
        users = user_service.fetch_all()
        
        assert len(users) == 1
        assert users[0].name == "John Doe"
        user_service.user_repo.get_all.assert_called_once()

    def test_get_user_profile(self, user_service: UserService, user: User):
        # Configura el mock para devolver un usuario cuando se solicita por ID
        user_service.user_repo.get_by_id.return_value = user
        
        fetched_user = user_service.get_user_profile(user.id)
        
        assert fetched_user == user
        user_service.user_repo.get_by_id.assert_called_once_with(user.id)

    def test_get_user_profile_not_found(self, user_service: UserService):
        # Configura el mock para devolver None cuando el usuario no se encuentra
        user_service.user_repo.get_by_id.return_value = None
        
        with pytest.raises(UserNotFoundException):
            user_service.get_user_profile(999)
        
        user_service.user_repo.get_by_id.assert_called_once_with(999)

    def test_update_profile(self, user_service: UserService, user: User):
        # Configura el mock para devolver un usuario existente
        user_service.user_repo.get_by_id.return_value = user
        updated_user = User(
            id=1, 
            name="Jane Doe", 
            email="jane@example.com", 
            phone="0987654321", 
            notification=None, 
            balance=Amount(100000))
        
        updated_user_from_service = user_service.update_profile(user.id, updated_user)
        
        assert updated_user_from_service.name == "Jane Doe"
        assert updated_user_from_service.email == "jane@example.com"
        assert updated_user_from_service.phone == "0987654321"
        user_service.user_repo.save.assert_called_once_with(updated_user_from_service)

    def test_update_profile_not_found(self, user_service: UserService):
        # Configura el mock para devolver None cuando el usuario no se encuentra
        user_service.user_repo.get_by_id.return_value = None
        updated_user = User(
            id=1, 
            name="Jane Doe", 
            email="jane@example.com", 
            phone="0987654321", 
            notification=None, 
            balance=Amount(100000))
        
        with pytest.raises(UserNotFoundException):
            user_service.update_profile(999, updated_user)
        
        user_service.user_repo.get_by_id.assert_called_once_with(999)

    def test_reset_balance(self, user_service: UserService, user: User):
        # Configura el mock para devolver un usuario existente
        user_service.user_repo.get_by_id.return_value = user
        
        user_with_reset_balance = user_service.reset_balance(user.id)
        
        assert user_with_reset_balance.balance.value == 500000
        assert len(user_with_reset_balance.subscriptions) == 0
        user_service.user_repo.save.assert_called_once_with(user_with_reset_balance)

    def test_reset_balance_not_found(self, user_service: UserService):
        # Configura el mock para devolver None cuando el usuario no se encuentra
        user_service.user_repo.get_by_id.return_value = None
        
        with pytest.raises(UserNotFoundException):
            user_service.reset_balance(999)
        
        user_service.user_repo.get_by_id.assert_called_once_with(999)