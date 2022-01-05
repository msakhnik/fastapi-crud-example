from fastapi import FastAPI
from db import database
from api import users


app = FastAPI()
app.include_router(users.router, tags=["users"])


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
