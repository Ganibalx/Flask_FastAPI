from fastapi import FastAPI
from typing import List
from models_pydentic import User_get, User_create
from models_db import users, database

app = FastAPI()

@app.get('/users', response_model=List[User_get])
async def get_users():
    query = users.select()
    return await database.fetch_all(query)


@app.post('/create', response_model=User_create)
async def create_user(user: User_create):
    query = users.insert().values(**user.dict(), status='active')
    await database.execute(query)
    return {**user.dict()}


@app.get("/users/{user_id}", response_model=User_get)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.put("/users/{user_id}", response_model=User_create)
async def update_user(user_id: int, new_user: User_create):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict()}


@app.delete("/users/{user_id}", response_model=User_get)
async def delete_user(user_id: int):
    query = users.update().where(users.c.id == user_id).values(status='deactive')
    await database.execute(query)
    user = users.select().where(users.c.id == user_id)
    return await database.fetch_one(user)
