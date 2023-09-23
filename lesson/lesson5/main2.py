from fastapi import FastAPI, Request

from fastapi.responses import HTMLResponse

from fastapi.responses import JSONResponse

from fastapi.templating import Jinja2Templates

app = FastAPI()


# 1
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "<h1>Hello World</h1>"


# 2
@app.get("/message")
async def read_message():
    message = {"message": "Hello World"}
    return JSONResponse(content=message, status_code=200)


# 3
templates = Jinja2Templates(directory="templates")


@app.get("/{name}", response_class=HTMLResponse)
async def read_item(request: Request, name: str):
    return templates.TemplateResponse("item.html", {"request": request, "name": name})
