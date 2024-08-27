from application import FundService, UserService, GetFundsUsecase, GetProfileUseCase, GetTransactionHistoryUseCase, ResetBalanceUseCase, SubscribeToFundUseCase, UnsubscribeOfFundUseCase, UpdateUserProfileUseCase
from domain import UserRepository, FundRepository, EventPublisher
from infrastructure.messaging.event_publisher_impl import EventPublisherImpl
from infrastructure.persistence.repositories.dynamodb_fund_repository_impl import DynamoDBFundRepositoryImpl
from infrastructure.persistence.repositories.dynamodb_user_repository_impl import DynamoDBUserRepositoryImpl
from interfaces.api.controllers.fund_controller import FundController
from interfaces.api.controllers.user_controller import UserController


def get_user_repository() -> UserRepository:
    return DynamoDBUserRepositoryImpl('UsersTable')

def get_fund_repository() -> FundRepository:
    return DynamoDBFundRepositoryImpl('FundsTable')

def get_event_publisher() -> EventPublisher:
    return EventPublisherImpl()

def get_fund_service():
    user_repo = get_user_repository()
    fund_repo = get_fund_repository()
    event_publisher = get_event_publisher()
    return FundService(user_repo, fund_repo, event_publisher)

def get_user_service():
    user_repo = get_user_repository()
    return UserService(user_repo)

def get_funds_usecase():
    fund_service = get_fund_service()
    return GetFundsUsecase(fund_service)

def get_subscribe_usecase():
    fund_service = get_fund_service()
    return SubscribeToFundUseCase(fund_service)

def get_unsubscribe_usecase():
    fund_service = get_fund_service()
    return UnsubscribeOfFundUseCase(fund_service)

def get_profile_usecase():
    user_service = get_user_service()
    return GetProfileUseCase(user_service)

def get_update_profile_usecase():
    user_service = get_user_service()
    return UpdateUserProfileUseCase(user_service)

def get_reset_balance_usecase():
    user_service = get_user_service()
    return ResetBalanceUseCase(user_service)

def get_transaction_history_usecase():
    user_service = get_user_service()
    return GetTransactionHistoryUseCase(user_service)

def get_user_controller():
    profile_usecase = get_profile_usecase()
    update_profile_usecase = get_update_profile_usecase()
    reset_balance_usecase = get_reset_balance_usecase()
    transaction_history_usecase = get_transaction_history_usecase()
    return UserController(profile_usecase, update_profile_usecase, reset_balance_usecase, transaction_history_usecase)

def get_fund_controller():
    get_funds_usecase = get_funds_usecase()
    subscribe_usecase = get_subscribe_usecase()
    unsubscribe_usecase = get_unsubscribe_usecase()
    return FundController(get_funds_usecase, subscribe_usecase, unsubscribe_usecase)