from enum import Enum
from datetime import datetime as dt

import sqlalchemy
import databases
from typing import Optional
from pydantic import BaseModel, Field

DATABASE_URL = "sqlite:///mydatabase.db"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table("users", metadata,
                         sqlalchemy.Column("uid", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("username", sqlalchemy.String(64)),
                         sqlalchemy.Column("surname", sqlalchemy.String(128), default=None),
                         sqlalchemy.Column("email", sqlalchemy.String(128)),
                         sqlalchemy.Column("password", sqlalchemy.String(128)),
                         )

products = sqlalchemy.Table("products", metadata,
                            sqlalchemy.Column("pid", sqlalchemy.Integer, primary_key=True),
                            sqlalchemy.Column("product_name", sqlalchemy.String(128)),
                            sqlalchemy.Column("description", sqlalchemy.String(1024)),
                            sqlalchemy.Column("price", sqlalchemy.Float()),
                            )

orders = sqlalchemy.Table("orders", metadata,
                          sqlalchemy.Column("oid", sqlalchemy.Integer, primary_key=True),
                          sqlalchemy.Column("uid", sqlalchemy.Integer, sqlalchemy.ForeignKey('users.uid')),
                          sqlalchemy.Column("pid", sqlalchemy.Integer, sqlalchemy.ForeignKey('products.pid')),
                          sqlalchemy.Column("date", sqlalchemy.DateTime),
                          sqlalchemy.Column("status", sqlalchemy.String(16)),
                          )

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)


class UserIn(BaseModel):
    username: str = Field(title="Username", min_length=3, max_length=50)
    surname: str = Field(None, title="Surname", min_length=2, max_length=100)
    email: str = Field(max_length=128)
    password: str = Field(max_length=128)


class User(UserIn):
    uid: int


class ProductIn(BaseModel):
    product_name: str = Field(title="Product name", max_length=32)
    description: str = Field(default=None, title="Description", max_length=1024)
    price: float = Field(title="Price", gt=0)


class Product(ProductIn):
    pid: int


class OrderStatusEnum(str, Enum):
    create = 'create'
    paid = 'paid'


class OrderIn(BaseModel):
    uid: int
    pid: int
    date: Optional[dt] = None
    status: Optional[OrderStatusEnum] = None


class Order(OrderIn):
    oid: int


