from fastapi import APIRouter
from schemas.user import userEntity, usersEntity
from models.user import User
from config.db import conn

user = APIRouter()

@user.get('/')
async def main():
    return usersEntity(conn.local.user.find())
@user.post('/')
async def post(user:User):
    conn.local.user.insert_one(dict(user))
    return usersEntity(conn.local.user.find())


