from application import FundService, UserService, SubscriptionService, NotificationService, GetFundsUsecase, GetProfileUseCase, GetTransactionHistoryUseCase, ResetBalanceUseCase, SubscribeToFundUseCase, UnsubscribeOfFundUseCase, UpdateUserProfileUseCase
from domain import UserRepository, FundRepository, TransactionRepository
from infrastructure.messaging.sns_notification_service_impl import SNSNotificationServiceImpl
from infrastructure.persistence.repositories.dynamodb_fund_repository_impl import DynamoDBFundRepositoryImpl
from infrastructure.persistence.repositories.dynamodb_user_repository_impl import DynamoDBUserRepositoryImpl
from infrastructure.persistence.repositories.dynamodb_transaction_repository_impl import DynamoDBTrasacctionRepositoryImpl
from interfaces.api.controllers.fund_controller import FundController
from interfaces.api.controllers.user_controller import UserController

# Database
def get_user_repository() -> UserRepository:
    return DynamoDBUserRepositoryImpl('ClientTable')

def get_fund_repository() -> FundRepository:
    return DynamoDBFundRepositoryImpl('FundTable')

def get_transaction_repository() -> TransactionRepository:
    return DynamoDBTrasacctionRepositoryImpl('TransactionTable')

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
    return SNSNotificationServiceImpl()

# Usecases
def get_funds_usecase():
    fund_service = get_fund_service()
    return GetFundsUsecase(fund_service)

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
    profile_usecase = get_profile_usecase()
    update_profile_usecase = get_update_profile_usecase()
    reset_balance_usecase = get_reset_balance_usecase()
    transaction_history_usecase = get_transaction_history_usecase()
    return UserController(profile_usecase, update_profile_usecase, reset_balance_usecase, transaction_history_usecase)

def get_fund_controller():
    funds_usecase = get_funds_usecase()
    subscribe_usecase = get_subscribe_usecase()
    unsubscribe_usecase = get_unsubscribe_usecase()
    return FundController(funds_usecase, subscribe_usecase, unsubscribe_usecase)