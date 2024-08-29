from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from domain import FundNotFoundException, InsufficientBalanceException
from interfaces.api.controllers.fund_controller import FundController
from interfaces.api.dependency_injection import get_fund_controller
from interfaces.api.schemas.fund_schemas import FundResponse
from interfaces.api.schemas.transaction_schemas import TransactionResponse, CreateSubscription, CancelSubscription


router = APIRouter(prefix="/funds")

@router.get("", response_model=List[FundResponse])
async def get_funds(controller: FundController = Depends(get_fund_controller)):
    return controller.get_all_funds()

@router.post("/{fund_id}/subscribe", response_model=TransactionResponse)
async def subscribe_to_fund(fund_id: int, subscription: CreateSubscription, controller: FundController = Depends(get_fund_controller)):
    try:
        return controller.subscribe(fund_id, subscription)
    except FundNotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except InsufficientBalanceException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/{fund_id}/unsubscribe", response_model=TransactionResponse)
async def unsubscribe_from_fund(fund_id: int, subscription: CancelSubscription, controller: FundController = Depends(get_fund_controller)):
    try:
        return controller.unsubscribe(fund_id, subscription)
    except FundNotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

