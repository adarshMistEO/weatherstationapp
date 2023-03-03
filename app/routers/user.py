from fastapi import Depends, HTTPException, Security, status
from fastapi import APIRouter
from auth.utils import AuthHandler
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from models.user import User
from db.user import (
    fetch_user,
    fetch_all_user,
    create_user,
    update_user,
    delete_user,
)

router = APIRouter()
security = HTTPBearer()

auth_handler = AuthHandler()

@router.get("/user")
async def all_users(credentials: HTTPAuthorizationCredentials = Depends(security)):
    response = await fetch_all_user()
    return response

@router.get("/user{id}", response_model=User)
async def get_user_by_id(id: int,credentials: HTTPAuthorizationCredentials = Depends(security)):
    response = await fetch_user(id)
    if response:
      return response
    raise HTTPException(status_code=404, detail="User with id {id} not found")

@router.post('/user', status_code=200)
async def add_user(details: User):
    hashed_password = auth_handler.get_password_hash(details.password)
    user_dict = details.dict()
    user_dict['password'] = hashed_password
    response = await create_user(user_dict)
    if response:
        return {
            'code': 200,
            'message': 'User added successfully',
        } 
    raise HTTPException(status_code=200, detail="Bad Request")

@router.put('/user{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_user_by_id(id: int, details: User, credentials: HTTPAuthorizationCredentials = Depends(security)):
    response = await update_user(id, details.dict())
    if response:
        return {
            'code': 200,
            'message': 'User updated successfully',
        } 
    raise HTTPException(status_code=404, detail="User not found")

@router.delete('/user{id}')
async def delete_user_by_id(id: int, credentials: HTTPAuthorizationCredentials = Depends(security)):
    response = await delete_user(id)
    if response:
        return "Succesfully deleted"
    raise HTTPException(status_code=204, detail="User not found")
