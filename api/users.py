from fastapi import APIRouter, Depends, HTTPException
from models.user import User, UserOut, UserIn
from typing import List
from db.users import UserDBHelper
from api.depends import get_user_helper, get_current_user
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter()


@router.get("/users/", response_model=List[User])
async def read_users(
    users: UserDBHelper = Depends(get_user_helper),
    limit: int = 100,
    skip: int = 0,
    current_user: User = Depends(get_current_user),
):
    return await users.get_all(limit=limit, skip=0)


@router.get("/users/me")
async def read_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.post("/users/", response_model=UserOut)
async def create_user(user: UserIn, users: UserDBHelper = Depends(get_user_helper)):
    return await users.create_user(user=user)


@router.post("/token")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    users: UserDBHelper = Depends(get_user_helper),
):
    user_from_db = await users.get_user_by_email(email=form_data.username)
    if not user_from_db:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    hashed_password = form_data.password
    if not hashed_password == user_from_db.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user_from_db.email, "token_type": "bearer"}
