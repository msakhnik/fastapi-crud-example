import sqlalchemy
from db.base import BaseDBHelper
from db import metadata
from typing import List, Optional
from models.user import User, UserIn


users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, unique=True),
    sqlalchemy.Column("email", sqlalchemy.String, unique=True),
    sqlalchemy.Column("hashed_password", sqlalchemy.String),
    sqlalchemy.Column("name", sqlalchemy.String),
)


class UserDBHelper(BaseDBHelper):
    async def get_all(self, limit: int = 100, skip: int = 0) -> List[User]:
        query = users.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def get_user_by_email(self, email: str) -> Optional[User]:
        query = users.select().where(users.c.email == email)
        user = await self.database.fetch_one(query=query)
        if user is None:
            return None
        return User.parse_obj(user)

    async def create_user(self, user: UserIn) -> User:
        new_user = User(name=user.name, email=user.email, hashed_password=user.password)
        values = {**new_user.dict()}
        values.pop("id")
        query = users.insert().values(**values)
        new_user.id = await self.database.execute(query=query)
        return new_user
