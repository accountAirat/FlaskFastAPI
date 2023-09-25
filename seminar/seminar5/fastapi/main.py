from fastapi import FastAPI
import uvicorn

from task1.app1 import app1
from task2.app2 import app2
from task3_4_5.app3 import app3
from task6.app6 import app6
from task7.app7 import app7
from task8.app8 import app8

app = FastAPI()
app.mount("/task1/", app1)
app.mount("/task2/", app2)
app.mount("/task3/", app3)
app.mount("/task6/", app6)
app.mount("/task7/", app7)
app.mount("/task8/", app8)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run("master:app", host='127.0.0.1', port=8000, reload=True)