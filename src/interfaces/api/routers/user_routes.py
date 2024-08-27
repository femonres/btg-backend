from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from domain import UserNotFoundException
from interfaces.api.controllers.user_controller import UserController
from interfaces.api.dependency_injection import get_user_controller
from interfaces.api.schemas.schemas import TransactionSchema, UserSchema


router = APIRouter(prefix="/users")

@router.get("", response_model=List[UserSchema])
async def get_users(controller: UserController = Depends(get_user_controller)):
    return controller.get_profile(user_id=1)

@router.get("/{user_id}", response_model=UserSchema)
async def get_user_by_id(user_id: int, controller: UserController = Depends(get_user_controller)):
    try:
        return controller.get_profile(user_id)
    except UserNotFoundException as e:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.put("/{user_id}", response_model=UserSchema)
async def update_user_profile(user_id: int, controller: UserController = Depends(get_user_controller)):
    try:
        return controller.update_profile(user_id)
    except UserNotFoundException as e:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.put("/{user_id}/reset", response_model=UserSchema)
async def reset_balance(user_id: int, controller: UserController = Depends(get_user_controller)):
    try:
        return controller.reset_balance(user_id)
    except UserNotFoundException as e:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    
@router.get("/{user_id}/history", response_model=List[TransactionSchema])
async def get_transaction_history(user_id: int, controller: UserController = Depends(get_user_controller)):
    return controller.get_transaction_history(user_id)