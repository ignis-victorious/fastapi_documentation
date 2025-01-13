from fastapi import FastAPI

app = FastAPI()


#  Define path parameters must precede general/variable path parameter
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


#  Path Parameter "int" also function complete an operation and return new value
@app.get("/items/{item_id}")
async def read_item(item_id: str) -> dict[str, str]:
    return {"item_id": item_id}


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
