import argparse
import sys
from decimal import Decimal
from typing import List

# noinspection PyUnresolvedReferences,PyPackageRequirements
from fastapi import APIRouter, Depends, FastAPI, Form

# noinspection PyUnresolvedReferences,PyPackageRequirements
from fastapi.routing import APIRoute

try:
    # noinspection PyUnresolvedReferences,PyPackageRequirements
    from fastapi import WebSocket
except ImportError:
    # noinspection PyUnresolvedReferences,PyPackageRequirements
    from starlette.websockets import WebSocket

try:
    # noinspection PyUnresolvedReferences,PyPackageRequirements
    from fastapi.testclient import TestClient
except ImportError:
    # noinspection PyUnresolvedReferences,PyPackageRequirements
    from starlette.testclient import TestClient

# noinspection PyUnresolvedReferences,PyPackageRequirements
from pydantic import BaseModel, condecimal

try:
    # noinspection PyUnresolvedReferences,PyPackageRequirements
    from pydantic import Field
except ImportError:
    field_exists = False
else:
    field_exists = True


if __name__ == "__main__":
    arguments = argparse.ArgumentParser()

    arguments.add_argument(
        "-ws",
        dest="websockets",
        action="append",
        default=[],
        nargs=2,
        metavar=("url", "dependency"),
    )
    arguments.add_argument("-ds", dest="dependencies", action="append", default=[])
    arguments.add_argument(
        "-os",
        dest="overrides",
        action="append",
        default=[],
        nargs=2,
        metavar=("dependency", "override"),
    )
    arguments.add_argument(
        "-a",
        dest="alias",
        default=None,
    )
    arguments.add_argument(
        "-m", dest="mode", required=True, choices=["websocket", "get", "post"]
    )
    arguments.add_argument("-u", dest="url", required=True)
    arguments.add_argument("-d", dest="data")
    arguments.add_argument(
        "-item",
        dest="item",
        nargs=3,
        metavar=("name", "price", "age"),
        default=("valid", "1.0", "5"),
    )
    arguments.add_argument(
        "-mb", dest="model_b", nargs=1, metavar="username", default="username"
    )
    arguments.add_argument(
        "-ma",
        dest="model_a",
        nargs=2,
        metavar=("username", "password"),
        default=("username", "password"),
    )
    arguments.add_argument(
        "-gs",
        dest="gets",
        action="append",
        default=[],
        nargs=2,
        metavar=("url", "response"),
    )
    arguments.add_argument(
        "-ps",
        dest="posts",
        action="append",
        default=[],
        nargs=2,
        metavar=("url", "response"),
    )

    args = arguments.parse_args()

    app = FastAPI()
    router = APIRouter()

    dependencies = dict()

    def get_dependency(d):
        async def dependency():
            return d

        return dependency

    for dep in args.dependencies:
        dependencies[dep] = get_dependency(dep)

    for dep, over in args.overrides:
        dependencies[dep] = get_dependency(dep)
        app.dependency_overrides[dependencies[dep]] = lambda: over

    if args.alias and field_exists:

        class Item(BaseModel):
            name: str = Field(..., alias=args.alias)
            price: float = None
            ids: List[int] = None
            age: condecimal(gt=Decimal(0.0))

    else:

        class Item(BaseModel):
            name: str = ...
            price: float = None
            ids: List[int] = None
            age: condecimal(gt=Decimal(0.0))

    item_name, item_price, item_age = args.item

    def get_item():
        return Item(
            **{
                args.alias or "name": item_name,
                "price": float(item_price),
                "age": int(item_age),
            }
        )

    def save_item_no_body(item: Item):
        return {"item": item}

    def get_item_list():
        return [
            Item(
                **{
                    args.alias or "name": item_name,
                    "price": float(item_price),
                    "age": int(item_age),
                }
            ),
            Item(
                **{
                    args.alias or "name": item_name,
                    "price": float(item_price),
                    "age": int(item_age),
                }
            ),
        ]

    if field_exists:

        class OtherItem(BaseModel):
            name: str = Field(..., alias=args.alias or "aliased_name")
            price: float = None
            ids: List[int] = None

    else:

        class OtherItem(BaseModel):
            name: str = ...
            price: float = None
            ids: List[int] = None

    def get_other():
        return OtherItem(
            **{
                args.alias or ("aliased_name" if field_exists else "name"): item_name,
                "price": float(item_price),
                "age": int(item_age),
            }
        )

    def get_other_list():
        return [
            OtherItem(
                **{
                    args.alias
                    or ("aliased_name" if field_exists else "name"): item_name,
                    "price": float(item_price),
                    "age": int(item_age),
                }
            ),
            OtherItem(
                **{
                    args.alias
                    or ("aliased_name" if field_exists else "name"): item_name,
                    "price": float(item_price),
                    "age": int(item_age),
                }
            ),
        ]

    class ModelB(BaseModel):
        username: str

    b_username = args.model_b

    async def get_model_b() -> ModelB:
        return ModelB(username=b_username)

    class ModelA(ModelB):
        password: str

    a_username, a_password = args.model_a

    async def get_model_a() -> ModelA:
        return ModelA(username=a_username, passord=a_password)

    class ModelC(BaseModel):
        id_: int
        model_b: ModelB

    async def get_model_c_a(model_a=Depends(get_model_a)):
        return {"id_": 0, "model_b": model_a}

    async def get_model_c_b(model_b=Depends(get_model_b)):
        return {"id_": 0, "model_b": model_b}

    for url, response in args.gets:
        responder = None
        type_ = None
        if response == "Item":
            responder = get_item
            type_ = Item
        elif response == "List[Item]":
            responder = get_item_list
            type_ = List[Item]
        elif response == "OtherIterm":
            responder = get_other
            type_ = OtherItem
        elif response == "List[OtherIterm]":
            responder = get_other_list
            type_ = List[OtherItem]
        elif responder == "ModelA":
            responder = get_model_a
            type_ = ModelA
        elif responder == "ModelB":
            responder = get_model_b
            type_ = ModelB
        elif responder == "ModelCA":
            responder = get_model_c_a
            type_ = ModelC
        elif responder == "ModelCB":
            responder = get_model_c_b
            type_ = ModelC

        if responder is not None:

            @app.get(url, response_model=type_)
            def get():
                return responder()

    for url, response in args.posts:
        responder = None
        type_ = None
        no_response = False
        if response == "Item":
            responder = save_item_no_body
            type_ = Item
            no_response = True
        elif response == "List[Item]":
            responder = get_item_list
            type_ = List[Item]
        elif response == "OtherIterm":
            responder = get_other
            type_ = OtherItem
        elif response == "List[OtherIterm]":
            responder = get_other_list
            type_ = List[OtherItem]
        elif responder == "ModelA":
            responder = get_model_a
            type_ = ModelA
        elif responder == "ModelB":
            responder = get_model_b
            type_ = ModelB
        elif responder == "ModelCA":
            responder = get_model_c_a
            type_ = ModelC
        elif responder == "ModelCB":
            responder = get_model_c_b
            type_ = ModelC

        if responder is not None:
            if no_response:

                @app.post(url)
                def post(m: type_):
                    return responder(m)

            else:

                @app.post(url, response_model=type_)
                def post():
                    return responder()

    for url, dep in args.websockets:

        @app.websocket(url)
        async def app_ws(websocket: WebSocket, data=Depends(dependencies[dep])):
            await websocket.accept()
            await websocket.send_text(data)
            await websocket.close()

    client = TestClient(app)

    if args.mode == "websocket":
        with client.websocket_connect(args.url) as ws:
            print(ws.receive_text())
    else:
        if args.data is None:
            response = getattr(client, args.mode)(args.url)
        else:
            response = getattr(client, args.mode)(args.url, json=eval(args.data))
        print(response.json())
        sys.exit(response.status_code)
