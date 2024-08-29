from fastapi import APIRouter, Depends, HTTPException, status

from domain import UserNotFoundException
from interfaces.api.controllers.user_controller import UserController
from interfaces.dependency_injection import get_user_controller
from interfaces.api.schemas.user_schemas import UserResponse, UserCreate
from interfaces.api.schemas.transaction_schemas import TransactionResponse


router = APIRouter(prefix="/users")

@router.get("", response_model=list[UserResponse])
async def get_users(controller: UserController = Depends(get_user_controller)):
    return controller.fetch_all()

@router.get("/{user_id}", response_model=UserResponse)
async def get_user_by_id(user_id: int, controller: UserController = Depends(get_user_controller)):
    try:
        return controller.get_profile(user_id)
    except UserNotFoundException as e:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.put("/{user_id}", response_model=UserResponse)
async def update_user_profile(user_id: int, user: UserCreate, controller: UserController = Depends(get_user_controller)):
    try:
        return controller.update_profile(user_id, user)
    except UserNotFoundException as e:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.put("/{user_id}/reset", response_model=UserResponse)
async def reset_balance(user_id: int, controller: UserController = Depends(get_user_controller)):
    try:
        return controller.reset_balance(user_id)
    except UserNotFoundException as e:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    
@router.get("/{user_id}/history", response_model=list[TransactionResponse])
async def get_transaction_history(user_id: int, controller: UserController = Depends(get_user_controller)):
    return controller.get_transaction_history(user_id)