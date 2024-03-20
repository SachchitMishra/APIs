'''
from fastapi import APIRouter
from models.user import User
from config.db import conn
from bson import ObjectId
from schemas.user import userEntity,usersEntity

user=APIRouter()
@user.get('/')
async def find_all_sums():
    
    # print(conn.local.user.find())
    # print(usersEntity(conn.local.user.find()))
   

    return usersEntity(conn.local.user.find())
    

@user.post('/sum') 
async def do_the_calculations(user:User):
    conn.local.user.insert_one(dict(user))
    print(user.num1+user.num2)
    return usersEntity(conn.local.user.find())

@user.put('/{id}')
async def update_calc(id,user:User):
        a= conn.local.user.find_one({"_id":ObjectId(id)})
        b=a['num1']
        c=a['num2']
        print(b)
        print(c)
    

        
        conn.local.user.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(user)})
        conn.local.user.find_one_and_update({"_id":ObjectId(id)},{"$set":{"sums":b+c}})
        return userEntity(conn.local.user.find_one({"_id":ObjectId(id)}))
'''
'''
from fastapi import APIRouter
from models.user import User
from config.db import conn
from bson import ObjectId
from schemas.user import userEntity,usersEntity

user=APIRouter()
@user.get('/')
async def find_all_sums():
    
    # print(conn.local.user.find())
    # print(usersEntity(conn.local.user.find()))
   

    return usersEntity(conn.local.user.find())
    

@user.post('/sum') 
async def do_the_calculations(user:User):
    conn.local.user.insert_one(dict(user))
    print(user.num1+user.num2)
    return usersEntity(conn.local.user.find())

@user.put('/{id}')
async def add(id,user:User):
        a= conn.local.user.find_one({"_id":ObjectId(id)})
        b=a['num1']
        c=a['num2']
        print(b)
        print(c)
    
        conn.local.user.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(user)})
        conn.local.user.find_one_and_update({"_id":ObjectId(id)},{"$set":{"sums":b+c}})
        return userEntity(conn.local.user.find_one({"_id":ObjectId(id)})) 
# @user.put('/{id}')  
# async def sub(id,user:User):       
#     a = conn.local.user.find_one({"_id":ObjectId(id)})
#     b = a['num1']
#     c = a['num2']
    
#     print(b) # Remove later
#     print(c) # Remove later
#     conn.local.user.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(user)})
#     conn.local.user.find_one_and_update
@user.delete('/{id}')
async def dele(id,user:User):
    return  userEntity(conn.local.user.find_one_and_delete({"_id":ObjectId(id)}))
'''    
from fastapi import APIRouter
from models.user import User
from config.db import conn
from bson import ObjectId
from schemas.user import userEntity,usersEntity

user=APIRouter()
@user.get('/')
async def find_all_sums():
    
    # print(conn.local.user.find())
    # print(usersEntity(conn.local.user.find()))
   

    return usersEntity(conn.local.user.find())
    

@user.post('/sum') 
async def do_the_calculations(user:User):
    conn.local.user.insert_one(dict(user))
    print(user.num1+user.num2)
    return usersEntity(conn.local.user.find())

@user.put('/{id}')
async def add(id,user:User):
        a= conn.local.user.find_one({"_id":ObjectId(id)})
        b=a['num1']
        c=a['num2']
        print(b)
        print(c)
    
        conn.local.user.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(user)})
        conn.local.user.find_one_and_update({"_id":ObjectId(id)},{"$set":{"sums":b+c}})
        return userEntity(conn.local.user.find_one({"_id":ObjectId(id)})) 
@user.put('/{id}')  
async def sub(id,user:User):       
    a = conn.local.user.find_one({"_id":ObjectId(id)})
    b = a['num1']
    c = a['num2']
    print(b-c)
    
    print(b) # Remove later
    print(c) # Remove later
    conn.local.user.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(user)})
    conn.local.user.find_one_and_update({"_id":ObjectId(id)}, {"$set":{"sums":b-c}})
    return usersEntity(conn.local.user.find_one({"_id":ObjectId(id)}))
@user.put('/{id}')
async def mul(id,user:User):
    a = conn.local.user.find_one({"_id":ObjectId(id)})
    b = a['num1']
    c = a['num2']
    print(b*c)
    
    conn.local.user.find_one_and_update({"_id":ObjectId(id)}, {"$set":dict(user)})
    conn.local.user.find_one_and_update({"_id":ObjectId(id)}, {"$set":{"sums":b*c}})
    return usersEntity(conn.local.user.find_one({"_id":ObjectId(id)}))
@user.delete('/{id}')
async def dele(id,user:User):
    return  userEntity(conn.local.user.find_one_and_delete({"_id":ObjectId(id)}))  