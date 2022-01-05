from typing import Optional
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: Optional[str] = None
    name: str
    email: EmailStr
    hashed_password: str


class UserIn(BaseModel):
    name: str
    email: EmailStr
    password: str
    password2: str


class UserOut(BaseModel):
    id: Optional[str] = None
    name: str
    email: EmailStr


class UserLogin(BaseModel):
    username: str
    hashed_password: str


class UserLoginOut(BaseModel):
    username: str
