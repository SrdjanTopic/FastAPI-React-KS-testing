from typing import List

from cruds.user import add_user, find_all_users
from fastapi import APIRouter, Depends, Security, status
from schemas.user import UserGet, UserRegister
from security.auth import check_user_has_role, get_current_user

router = APIRouter(prefix="/users",
                   tags=["users"],  responses={404: {"description": "Not found"}})


@router.get('/', response_model=List[UserGet])
async def get_all_users(current_user: UserGet = Security(check_user_has_role, scopes=["ADMIN"])):
    return find_all_users()


@router.post('/', response_model=UserGet, status_code=status.HTTP_201_CREATED)
async def register_user(user: UserRegister):
    return await add_user(user)


@router.get("/users/me", response_model=UserGet)
async def read_users_me(current_user: UserGet = Depends(get_current_user)):
    return current_user
