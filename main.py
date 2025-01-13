from fastapi import FastAPI
from enum import Enum


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


#  Define path parameters must precede general/variable path parameter
@app.get("/users/me")
async def read_user_me() -> dict[str, str]:
    return {"user_id": "the current user"}


#  Path Parameter "int" also function complete an operation and return new value
@app.get("/items/{item_id}")
async def read_item(item_id: str) -> dict[str, str]:
    return {"item_id": item_id}


#  Predefined values for path parameter
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName) -> dict[str, str]:
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


#  Path Parameter "str"
# @app.get("/items/{item_id}")
# async def read_item(item_id) -> dict[str, str]:
#     return {"item_id": item_id}


#
# # from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# async def root() -> dict[str, str]:
#     return {"message": "Hello World"}
