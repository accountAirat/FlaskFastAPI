from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, Field
import sqlalchemy
import databases

DATABASE_URL = "sqlite:///mydatabase.db"
# DATABASE_URL = "postgresql://user:password@localhost/dbname"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table("users", metadata,
                         sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("name", sqlalchemy.String(32)),
                         sqlalchemy.Column("email", sqlalchemy.String(128)),
                         )

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)


class Item(BaseModel):
    name: str = Field(title="Name", max_length=50)
    price: float = Field(title="Price", gt=0, le=100000)
    description: str = Field(default=None, title="Description", max_length=1000)
    tax: float = Field(0, title="Tax", ge=0, le=10)


# class User(BaseModel):
#     id: int
#     username: str = Field(title="Username", max_length=50)
#     full_name: str = Field(None, title="Full Name", max_length=100)
#     age: int = Field(default=0)
#     email: str = Field(max_length=128)

class UserIn(BaseModel):
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


class User(BaseModel):
    id: int
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


class Order(BaseModel):
    items: List[Item]
    user: User


"""
Field:
● default: значение по умолчанию для поля
● alias: альтернативное имя для поля (используется при сериализации и десериализации)
● title: заголовок поля для генерации документации API
● description: описание поля для генерации документации API
● gt: ограничение на значение поля (больше указанного значения)
● ge: ограничение на значение поля (больше или равно указанному значению)
● lt: ограничение на значение поля (меньше указанного значения)
● le: ограничение на значение поля (меньше или равно указанному значению)
● multiple_of: ограничение на значение поля (должно быть кратно указанному значению)
● max_length: ограничение на максимальную длину значения поля
● min_length: ограничение на минимальную длину значения поля
● regex: регулярное выражение, которому должно соответствовать значение поля
"""
