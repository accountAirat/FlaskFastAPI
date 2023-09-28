from app_users import app as app_user
from app_products import app as app_product
from app_orders import app as app_orders
from fastapi import FastAPI
import uvicorn
from models import database


app = FastAPI()
app.mount("/users/", app_user)
app.mount("/products/", app_product)
app.mount("/orders/", app_orders)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
    # uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=False)