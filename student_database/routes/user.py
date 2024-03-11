from fastapi import APIRouter
from models.user import User
from config.db import conn
from schemas.user import userEntity, usersEntity

user = APIRouter()

@user.get('/')
async def show_value():
    return usersEntity(conn.local.user.find())
@user.post('/')
async def value(user:User):
    conn.local.user.insert_one(dict(user))
    return usersEntity(conn.local.user.find())