from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items")
def items(age : int, name : Annotated[str | None,Query(max_length=25,title="Query string",min_length=2,pattern="^fixedquery$")] = None):
# async def read_items(q: str | None = Query(default=None, max_length=50)): withput annotation
    items_datas= {"name" : ["ritesh","lucky","krishan"], "class":"final year"}
    if name:
        items_datas.update({"name2" : name})
    return items_datas
