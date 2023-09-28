from fastapi import FastAPI
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List
from models import *

app = FastAPI()


@app.post("/", response_model=Order)
async def create_order(order: OrderIn):
    query = orders.insert().values(uid=order.uid, pid=order.pid)
    last_record_id = await database.execute(query)
    return read_order(last_record_id)


@app.get("/", response_model=List[Order])
async def read_order():
    query = orders.select()
    return await database.fetch_all(query)


@app.get("/{oid}", response_model=List[Order])
async def read_order(oid: int):
    query = orders.select().where(orders.c.oid == oid)
    return await database.fetch_all(query)


@app.put("/{oid}", response_model=Order)
async def update_order(oid: int, new_order: OrderIn):
    query = orders.update().where(orders.c.oid == oid).values(**new_order.dict())
    await database.execute(query)
    return {**new_order.dict(), "oid": oid}


@app.delete("/{oid}")
async def delete_order(oid: int):
    query = orders.delete().where(orders.c.oid == oid)
    await database.execute(query)
    return {'message': f'Product №{oid} deleted'}

#dict

