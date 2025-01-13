from typing import Annotated
from fastapi import FastAPI, Header, Request
from pydantic import BaseModel

app = FastAPI()

@app.get("/read-header/")
def read_header(user_agent: str = Header(None)):
    return {"User-Agent": user_agent}

@app.get("/reader-allheader")
def all_header(request:Request):
    head = request.headers
    print(head)
    return head



class CommonHeaders(BaseModel):
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []


@app.get("/iteems/")
async def read_items(headers: Annotated[CommonHeaders, Header()]):
    return headers