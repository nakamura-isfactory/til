#!python3
# :basenaem:apidocument_1004.py
# :$ make version/fastapi.txt
# :https://github.com/tiangolo/fastapi/issues/4700 #{Query parameters from Depends do not show description in docs · Issue #4700 · tiangolo/fastapi}

from fastapi import Depends, FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI(description="API の 説明")


class CommonParams:
    def __init__(
        self,
        b: int = Query(2, description="Using query changes nothing"),
        a: int = Query(5, description="This description shows up"),
    ):
        self.b = b
        self.a = a

@app.get("/")
async def get_root(
    params: CommonParams = Depends(),
    q: int = Query(5, description="This description shows up"),
):
    return {
        "a": params.a,
        "b": params.b,
        "q": q,
    }

#:https://fastapi.tiangolo.com/ja/tutorial/query-params-str-validations/?h=query#query_1
@app.get("/items/")
async def read_items(q: str = Query(min_length=3, description="This parameter is requreid")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#:https://fastapi.tiangolo.com/ja/tutorial/path-operation-configuration/?h=description#summary-and-description
@app.post(
    "/items/",
    response_model=Item,
    summary="Create an item",
    description="Create an item with all the information, name, description, price, tax and a set of unique tags",
)
async def create_item(item: Item):
    return item
