from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel, Field
from enum import Enum, IntEnum
import sqlalchemy
import databases

DATABASE_URL = "sqlite:///mydatabase.db"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

tasks = sqlalchemy.Table("tasks", metadata,
                         sqlalchemy.Column("task_id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("task_name", sqlalchemy.String(128)),
                         sqlalchemy.Column("description", sqlalchemy.String(1024)),
                         sqlalchemy.Column("status", sqlalchemy.String(16)),
                         )

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)

app = FastAPI()


class CompletedEnum(str, Enum):
    completed = 'completed'
    not_completed = 'not_completed'


class Task(BaseModel):
    task_id: int
    task_name: str = Field(min_length=3, max_length=32)
    description: str = Field(min_length=5, max_length=1024)
    status: Optional[CompletedEnum] = CompletedEnum.not_completed


class TaskIn(BaseModel):
    task_name: str = Field(min_length=3, max_length=32)
    description: str = Field(min_length=5, max_length=1024)
    status: Optional[CompletedEnum] = CompletedEnum.not_completed


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# CRUD
@app.post("/tasks/", response_model=Task)
async def create_task(task: TaskIn):
    query = tasks.insert().values(task_name=task.task_name, description=task.description, status=task.status)
    last_record_id = await database.execute(query)
    return {**task.dict(), "task_id": last_record_id}


@app.get("/tasks/", response_model=List[Task])
async def read_tasks():
    query = tasks.select()
    return await database.fetch_all(query)


@app.get("/tasks/{task_id}", response_model=List[Task])
async def get_task(task_id: int):
    query = tasks.select().where(tasks.c.task_id == task_id)
    return await database.fetch_all(query)


@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, new_task: TaskIn):
    query = tasks.update().where(tasks.c.task_id == task_id).values(**new_task.dict())
    await database.execute(query)
    return {**new_task.dict(), "task_id": task_id}


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    query = tasks.delete().where(tasks.c.task_id == task_id)
    await database.execute(query)
    return {'message': 'Task deleted'}

