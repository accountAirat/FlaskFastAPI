from fastapi import FastAPI
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List
from models import *

app = FastAPI()


@app.post("/", response_model=Product)
async def create_product(product: ProductIn):
    query = products.insert().values(product_name=product.product_name, description=product.description, price=product.price)
    last_record_id = await database.execute(query)
    return {**product.dict(), "pid": last_record_id}


@app.get("/", response_model=List[Product])
async def read_products():
    query = products.select()
    return await database.fetch_all(query)


@app.get("/{pid}", response_model=List[Product])
async def read_product(pid: int):
    query = products.select().where(products.c.pid == pid)
    return await database.fetch_all(query)


@app.put("/{pid}", response_model=Product)
async def update_product(pid: int, new_product: ProductIn):
    query = products.update().where(products.c.pid == pid).values(**new_product.dict())
    await database.execute(query)
    return {**new_product.dict(), "pid": pid}


@app.delete("/{pid}")
async def delete_product(pid: int):
    query = products.delete().where(products.c.pid == pid)
    await database.execute(query)
    return {'message': f'Product №{pid} deleted'}

