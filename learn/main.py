from enum import Enum
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/path-name")
def dataretrieve(name: Optional[str | None] = None):
    return {name}

@app.get("/items/{name}")
def path(name:int):
    return {"item_id":name}



class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"



@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "resnet":
        print(model_name.value)
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


    


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    a = {"skip" : skip + limit }
    fake_items_db.append(a)
    return fake_items_db



@app.get("/itemss/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}