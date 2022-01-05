from db.users import UserDBHelper
from db import database
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_user_helper() -> UserDBHelper:
    return UserDBHelper(database)


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = token
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user
