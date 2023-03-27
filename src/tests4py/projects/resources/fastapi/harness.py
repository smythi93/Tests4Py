import argparse
import sys
from typing import List

from decimal import Decimal

# noinspection PyUnresolvedReferences
from fastapi import APIRouter, Depends, FastAPI, Form

# noinspection PyUnresolvedReferences
from fastapi.routing import APIRoute

try:
    # noinspection PyUnresolvedReferences
    from fastapi import WebSocket
except ImportError:
    # noinspection PyUnresolvedReferences
    from starlette.websockets import WebSocket

try:
    # noinspection PyUnresolvedReferences
    from fastapi.testclient import TestClient
except ImportError:
    # noinspection PyUnresolvedReferences
    from starlette.testclient import TestClient

# noinspection PyUnresolvedReferences
from pydantic import BaseModel, condecimal

try:
    # noinspection PyUnresolvedReferences
    from pydantic import Field
except ImportError:
    field_exists = False
else:
    field_exists = True


if __name__ == "__main__":
    arguments = argparse.ArgumentParser()

    arguments.add_argument("-p", dest="url", default="/")
    arguments.add_argument("-m", dest="mode", default="get")
    arguments.add_argument("-d", dest="data", default=None)
    arguments.add_argument("-a", dest="alias", default=False, action="store_true")
    arguments.add_argument("-o", dest="override", default=False, action="store_true")
    arguments.add_argument("-u", dest="users", default=False, action="store_true")

    args = arguments.parse_args()

    app = FastAPI()
    router = APIRouter()

    if args.alias and field_exists:

        class Item(BaseModel):
            name: str = Field(..., alias="aliased_name")
            price: float = None
            ids: List[int] = None
            age: condecimal(gt=Decimal(0.0))

    else:

        class Item(BaseModel):
            name: str = ...
            price: float = None
            ids: List[int] = None
            age: condecimal(gt=Decimal(0.0))

    if field_exists:

        class OtherItem(BaseModel):
            name: str = Field(..., alias="aliased_name")
            price: float = None
            ids: List[int] = None

    else:

        class OtherItem(BaseModel):
            name: str = ...
            price: float = None
            ids: List[int] = None

    class ModelB(BaseModel):
        username: str

    class ModelA(ModelB):
        password: str

    class ModelC(BaseModel):
        id_: int
        model_b: ModelB

    async def dependency():
        return "Dependency"

    async def overridden():
        return "Overridden"

    @app.get("/items/valid", response_model=Item)
    def get_valid():
        return (
            Item(aliased_name="valid", price=1.0, age=5)
            if args.alias
            else Item(name="valid", price=1.0, age=5)
        )

    @app.post("/items/")
    def save_item_no_body(item: Item):
        return {"item": item}

    @app.get("/items/valid_list", response_model=List[Item])
    def get_valid():
        return [
            Item(aliased_name="valid", price=1.0, age=5)
            if args.alias
            else Item(name="valid", price=1.0, age=5),
            Item(aliased_name="list", price=1.0, age=5, ids=[1, 2, 3])
            if args.alias
            else Item(name="list", price=1.0, age=5, ids=[1, 2, 3]),
        ]

    @app.get("/items/other", response_model=OtherItem)
    def get_other():
        return OtherItem(aliased_name="valid", price=1.0, age=5)

    if args.users:

        async def user_exists(user_id: int):
            return True

        @app.get("/user/{user_id}", dependencies=[Depends(user_exists)])
        async def read_users(user_id: int):
            return user_id

    @router.websocket("/")
    async def router_ws_decorator_depends(
        websocket: WebSocket, data=Depends(dependency)
    ):
        await websocket.accept()
        await websocket.send_text(data)
        await websocket.close()

    async def get_model_a() -> ModelA:
        return ModelA(username="test-user", password="test-password")

    @app.get("/model", response_model=ModelC)
    async def get_model_c(model_a=Depends(get_model_a)):
        return {"id_": 0, "model_b": model_a}

    @app.post("/form/python-set")
    def post_form_param_set(items: set = Form(...)):
        return items

    @app.post("/form/python-list")
    def post_form_param_tuple(items: tuple = Form(...)):
        return items

    class CustomAPIRoute(APIRoute):
        x_type = "test"

    custom_router = APIRouter(route_class=CustomAPIRoute)

    @custom_router.get("/")
    def get_custom():
        return {"msg": "test"}

    app.include_router(router=custom_router, prefix="/custom")
    app.include_router(router, prefix="/router")

    @app.get("/routes/")
    def get_routes():
        routes = dict()
        for r in app.router.routes:
            if r.path == "/custom/":
                routes[r.path] = r.x_type
            else:
                routes[r.path] = r.__class__.__name__
        return routes

    if args.override:
        app.dependency_overrides[dependency] = overridden

    client = TestClient(app)

    if args.mode == "websocket":
        with client.websocket_connect(args.url) as websocket:
            print(websocket.receive_text())
    elif args.data is not None:
        response = getattr(client, args.mode)(args.url, json=eval(args.data))
        print(response.json())
        sys.exit(response.status_code)
    else:
        response = getattr(client, args.mode)(args.url)
        print(response.json())
        sys.exit(response.status_code)
