from application import FundService, UserService, SubscriptionService, NotificationService, GetFundsUsecase, FetchUsersUsecase, GetProfileUseCase, GetTransactionHistoryUseCase, ResetBalanceUseCase, SubscribeToFundUseCase, UnsubscribeOfFundUseCase, UpdateUserProfileUseCase
from domain import UserRepository, FundRepository, TransactionRepository
from infrastructure.messaging.sns_notification_service_impl import SNSNotificationServiceImpl
from infrastructure.persistence.repositories.dynamodb_fund_repository_impl import DynamoDBFundRepositoryImpl
from infrastructure.persistence.repositories.dynamodb_user_repository_impl import DynamoDBUserRepositoryImpl
from infrastructure.persistence.repositories.dynamodb_transaction_repository_impl import DynamoDBTrasacctionRepositoryImpl
from interfaces.api.controllers.fund_controller import FundController
from interfaces.api.controllers.user_controller import UserController

# Singleton
_fund_repository_instance = None
_user_repository_instance = None
_transaction_repository_instance = None
_notification_instance = None

# Database
def get_user_repository() -> UserRepository:
    global _user_repository_instance
    if _user_repository_instance is None:
        _user_repository_instance = DynamoDBUserRepositoryImpl('ClientTable')
    return _user_repository_instance

def get_fund_repository() -> FundRepository:
    global _fund_repository_instance
    if _fund_repository_instance is None:
        _fund_repository_instance = DynamoDBFundRepositoryImpl('FundTable')
    return _fund_repository_instance

def get_transaction_repository() -> TransactionRepository:
    global _transaction_repository_instance
    if _transaction_repository_instance is None:
        _transaction_repository_instance = DynamoDBTrasacctionRepositoryImpl('TransactionTable')
    return _transaction_repository_instance

# Servicios
def get_fund_service():
    fund_repo = get_fund_repository()
    return FundService(fund_repo)

def get_subscription_service():
    user_repo = get_user_repository()
    fund_repo = get_fund_repository()
    transaction_repo = get_transaction_repository()
    return SubscriptionService(user_repo, fund_repo, transaction_repo)

def get_user_service():
    user_repo = get_user_repository()
    return UserService(user_repo)

def get_notification_service() -> NotificationService:
    global _notification_instance
    if _notification_instance is None:
        _notification_instance = SNSNotificationServiceImpl()
    return _notification_instance

# Usecases
def get_funds_usecase():
    fund_service = get_fund_service()
    return GetFundsUsecase(fund_service)

def get_fetch_users_usecase():
    user_service = get_user_service()
    return FetchUsersUsecase(user_service)

def get_profile_usecase():
    user_service = get_user_service()
    return GetProfileUseCase(user_service)

def get_reset_balance_usecase():
    user_service = get_user_service()
    return ResetBalanceUseCase(user_service)

def get_update_profile_usecase():
    user_service = get_user_service()
    return UpdateUserProfileUseCase(user_service)

def get_transaction_history_usecase():
    subscription_service = get_subscription_service()
    return GetTransactionHistoryUseCase(subscription_service)

def get_subscribe_usecase():
    subscription_service = get_subscription_service()
    notification_service = get_notification_service()
    return SubscribeToFundUseCase(subscription_service, notification_service)

def get_unsubscribe_usecase():
    subscription_service = get_subscription_service()
    notification_service = get_notification_service()
    return UnsubscribeOfFundUseCase(subscription_service, notification_service)

# Controllers
def get_user_controller():
    all_users_usecase = get_fetch_users_usecase()
    profile_usecase = get_profile_usecase()
    update_profile_usecase = get_update_profile_usecase()
    reset_balance_usecase = get_reset_balance_usecase()
    transaction_history_usecase = get_transaction_history_usecase()
    return UserController(all_users_usecase, profile_usecase, update_profile_usecase, reset_balance_usecase, transaction_history_usecase)

def get_fund_controller():
    funds_usecase = get_funds_usecase()
    subscribe_usecase = get_subscribe_usecase()
    unsubscribe_usecase = get_unsubscribe_usecase()
    return FundController(funds_usecase, subscribe_usecase, unsubscribe_usecase)