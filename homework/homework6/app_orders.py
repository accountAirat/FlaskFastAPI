from fastapi import FastAPI
from typing import List
from models import orders, Order, OrderIn, database, OrderStatusEnum
from datetime import datetime as dt

app = FastAPI()


@app.post("/")
async def create_order(order: OrderIn):
    query = orders.insert().values(uid=order.uid, pid=order.pid, date=dt.now(), status=OrderStatusEnum.create)
    last_record_id = await database.execute(query)
    return {**order.model_dump(), "oid": last_record_id}


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
    return {**new_order.model_dump(), "oid": oid}


@app.delete("/{oid}")
async def delete_order(oid: int):
    query = orders.delete().where(orders.c.oid == oid)
    await database.execute(query)
    return {'message': f'Product №{oid} deleted'}

