from tkinter import Image
from typing import Annotated
from fastapi import FastAPI,Query,Path
from pydantic import BaseModel

app = FastAPI()

@app.get("/items/{item_id}")
def read_path(item_id : Annotated[int, Path(title="path parameter")], q : Annotated[str | None, Query(alias="item-query")] = None,):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated[int, Path(title="The ID of the item to get")],
#     q: Annotated[str | None, Query(alias="item-query")] = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results



@app.get("/itemss/{item_id}")
async def read_items(
    *,
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str,
    size: Annotated[float, Query(gt=0, lt=10.5)],
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if size:
        results.update({"size": size})
    return results




class Image(BaseModel):
    url: str
    name: str

class Items(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image: Image | None = None


@app.put("/itemsss/{item_id}")
async def update_item(item_id: int, item: Items):
    results = {"item_id": item_id, "item": item}
    return results