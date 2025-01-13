from fastapi import FastAPI

app = FastAPI()


#  Path Parameter "int" also function complete an operation and return new value
@app.get("/items/{item_id}")
async def read_item(item_id: int) -> dict[str, int]:
    return {"item_id": item_id * 50}


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
