from typing import Annotated
from fastapi import FastAPI, Request, Response, Cookie
from pydantic import BaseModel

app = FastAPI()

# Cookie set karne ka endpoint
@app.get("/set-cookie/")
def set_cookie(response: Response):
    response.set_cookie(key="sample_cookie", value="loag")
    print(response)
    return {"message": "Cookie set successfully!"}

# Cookie read karne ka endpoint
@app.get("/read-cookie/")
def read_cookie(sample_cookie: Annotated[str | None ,Cookie()] = None ):
    return {"sample_cookie":sample_cookie}

@app.get("/readdcookie/")
def read_cookie(request : Request):
    cookies = request.cookies
    return {"samplecookie":cookies}




class Cookies(BaseModel):
    session_id: str
    fatebook_tracker: str | None = None
    googall_tracker: str | None = None


@app.get("/itemsssss/")
async def read_items(cookies: Annotated[Cookies, Cookie()]):
    return cookies