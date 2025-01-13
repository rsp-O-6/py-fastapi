from typing import Annotated

from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()


@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}


class FormData(BaseModel):
    username: str
    passwords: str
    model_config = {"extra": "forbid"}


@app.post("/logins/")
async def logins(data: Annotated[FormData, Form(description="A file read as bytes")]):
    return data

