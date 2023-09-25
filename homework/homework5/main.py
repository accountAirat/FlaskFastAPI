from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


class Task(BaseModel):
    task_name: str
    description: str
    # status: Optional[List["completed", "not_completed"]]


