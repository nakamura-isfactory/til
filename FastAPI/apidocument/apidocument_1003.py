#!python3
# :basenaem:apidocument_1003.py
# :$ make version/fastapi.txt

from typing import Union

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()

# :https://fastapi.tiangolo.com/ja/advanced/custom-response/#fileresponse
@app.get("/r1")
def r1():
    return """
    <h1>r1</h1>
    """

# :https://fastapi.tiangolo.com/ja/advanced/custom-response/#fileresponse


@app.get("/r2", response_class=HTMLResponse)
def r2():
    return """
    <h1>r2</h1>
    """

# :https://fastapi.tiangolo.com/ja/advanced/custom-response/#fileresponse


@app.get("/r3", response_class=FileResponse)
def r3():
    return """
    <h1>r3</h1>
    """
# :-------------------------------
# :https://fastapi.tiangolo.com/ja/advanced/additional-responses/


class Item(BaseModel):
    id: str
    value: str

responses = {
    404: {"description": "Item not found"},
    302: {"description": "The item was moved"},
    403: {"description": "Not enough privileges"},
}

@app.get(
    "/items/{item_id}",
    response_model=Item,
    responses={**responses, 200: {"content": {"image/png": {}}}},
)
async def read_item(item_id: str, img: Union[bool, None] = None):
    if img:
        return FileResponse("image.png", media_type="image/png")
    else:
        return {"id": "foo", "value": "there goes my hero"}

@app.get(
    "/images1/{item_id}",
    responses={**responses, 200: {"content": {"image/png": {}}}},
)
async def images1(item_id: str, img: Union[bool, None] = None):
    return FileResponse("image.png", media_type="image/png")

@app.get(
    "/images2/{item_id}",
    responses={**responses, 200: {"content": {"image/png": {}}}},
    response_class=FileResponse
)
async def images2(item_id: str, img: Union[bool, None] = None):
    return FileResponse("image.png", media_type="image/png")
