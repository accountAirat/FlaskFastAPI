from fastapi import FastAPI
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List
from models import users, User, UserIn, database

app = FastAPI()


@app.post("/", response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(username=user.username, surname=user.surname, email=user.email,
                                  password=generate_password_hash(user.password))
    last_record_id = await database.execute(query)
    return {**user.model_dump(), "uid": last_record_id}


@app.get("/", response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get("/{uid}", response_model=List[User])
async def read_user(uid: int):
    query = users.select().where(users.c.uid == uid)
    return await database.fetch_all(query)


@app.put("/{uid}", response_model=User)
async def update_user(uid: int, new_user: UserIn):
    query = users.update().where(users.c.uid == uid).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.model_dump(), "uid": uid}


@app.delete("/{uid}")
async def delete_user(uid: int):
    query = users.delete().where(users.c.uid == uid)
    await database.execute(query)
    return {'message': f'User №{uid} deleted'}

