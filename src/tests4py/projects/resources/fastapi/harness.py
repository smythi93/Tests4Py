import argparse
import sys
from decimal import Decimal
from typing import List, Union

# noinspection PyUnresolvedReferences,PyPackageRequirements
from fastapi import APIRouter, Body, Depends, FastAPI, Form

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
    arguments.add_argument(
        "-cr",
        dest="custom_routes",
        nargs=2,
        metavar=("prefix", "msg"),
        default=None,
    )
    arguments.add_argument(
        "-rp",
        dest="reused_param",
        default=None,
    )
    arguments.add_argument(
        "-fl",
        dest="form_list",
        default=None,
    )
    arguments.add_argument(
        "-mt",
        dest="media_type",
        default=None,
    )
    arguments.add_argument(
        "-sd",
        dest="skip_defaults",
        default=None,
    )
    arguments.add_argument(
        "-ub",
        dest="union_body",
        default=None,
    )
    arguments.add_argument(
        "-bs",
        dest="bearer_security",
        default=None,
    )
    arguments.add_argument(
        "-ah",
        dest="auth",
        nargs=2,
        metavar=("scheme", "credentials"),
        default=None,
    )
    arguments.add_argument(
        "-ar",
        dest="additional_responses",
        default=None,
    )
    arguments.add_argument(
        "-ap",
        dest="additional_properties",
        default=None,
    )
    arguments.add_argument(
        "-wr",
        dest="ws_router",
        nargs=2,
        metavar=("path", "message"),
        default=None,
    )
    arguments.add_argument(
        "-ce",
        dest="config_encoder",
        default=None,
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

    b_username = args.model_b[0] if isinstance(args.model_b, list) else args.model_b

    async def get_model_b() -> ModelB:
        return ModelB(username=b_username)

    class ModelA(ModelB):
        password: str

    a_username, a_password = args.model_a

    async def get_model_a() -> ModelA:
        return ModelA(username=a_username, password=a_password)

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
        elif response == "ModelA":
            responder = get_model_a
            type_ = ModelA
        elif response == "ModelB":
            responder = get_model_b
            type_ = ModelB
        elif response == "ModelCA":
            responder = get_model_c_a
            type_ = ModelC
        elif response == "ModelCB":
            responder = get_model_c_b
            type_ = ModelC

        if responder is not None:
            # Register the responder directly so FastAPI awaits async handlers
            # and resolves their dependencies (a plain wrapper would return an
            # un-awaited coroutine and skip Depends injection).
            app.get(url, response_model=type_)(responder)

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
        elif response == "ModelA":
            responder = get_model_a
            type_ = ModelA
        elif response == "ModelB":
            responder = get_model_b
            type_ = ModelB
        elif response == "ModelCA":
            responder = get_model_c_a
            type_ = ModelC
        elif response == "ModelCB":
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

    if args.custom_routes is not None:
        cr_prefix, cr_msg = args.custom_routes

        class RouteA(APIRoute):
            x_type = "A"

        class RouteB(APIRoute):
            x_type = "B"

        router_a = APIRouter(route_class=RouteA)
        router_b = APIRouter(route_class=RouteB)

        @router_b.get("/item")
        def get_cr_b():
            return {"msg": cr_msg}

        router_a.include_router(router=router_b, prefix="/" + cr_prefix)
        app.include_router(router=router_a, prefix="/root")

        @app.get("/routes/")
        def get_cr_routes():
            return [
                route.x_type
                for route in app.routes
                if isinstance(route, APIRoute) and route.path.startswith("/root")
            ]

    if args.reused_param is not None:

        async def check_reused_exists(item_id: int):
            return True

        @app.get(
            "/" + args.reused_param + "/{item_id}",
            dependencies=[Depends(check_reused_exists)],
        )
        async def read_reused(item_id: int):
            return {"item_id": item_id}

    if args.form_list is not None:

        @app.post("/form")
        def post_form(items: list = Form(...)):
            return items

    if args.skip_defaults is not None:

        class SkipSub(BaseModel):
            marker: str = "defaultmarker"

        class SkipModel(BaseModel):
            x: int = None
            sub: SkipSub

        @app.get(
            "/" + args.skip_defaults,
            response_model=SkipModel,
            response_model_skip_defaults=True,
        )
        def get_skip_defaults():
            return SkipModel(sub={})

    if args.config_encoder is not None:
        from enum import Enum

        class CERoleEnum(Enum):
            admin = "admin"
            normal = "normal"

        class CEModelWithConfig(BaseModel):
            role: CERoleEnum = None

            class Config:
                use_enum_values = True

        @app.get("/" + args.config_encoder, response_model=CEModelWithConfig)
        def ce_get():
            return CEModelWithConfig(role=CERoleEnum.admin)

    if args.ws_router is not None:
        wr_path, wr_message = args.ws_router
        wr_router = APIRouter()

        @wr_router.websocket_route(wr_path)
        async def wr_index(websocket: WebSocket):
            await websocket.accept()
            await websocket.send_text(wr_message)
            await websocket.close()

        app.include_router(wr_router)

    if args.additional_properties is not None:
        from typing import Dict

        class APItems(BaseModel):
            items: Dict[str, int]

        @app.post("/" + args.additional_properties)
        def ap_foo(items: APItems):
            return items.items

    if args.additional_responses is not None:
        ar_router = APIRouter()

        @ar_router.get(
            "/ar_a", responses={501: {"description": args.additional_responses}}
        )
        async def ar_a():
            return "a"

        @ar_router.get("/ar_b", responses={502: {"description": "second"}})
        async def ar_b():
            return "b"

        @ar_router.get("/ar_c", responses={503: {"description": "third"}})
        async def ar_c():
            return "c"

        app.include_router(ar_router)

    if args.bearer_security is not None:
        from typing import Optional

        # noinspection PyUnresolvedReferences,PyPackageRequirements
        from fastapi import Security

        # noinspection PyUnresolvedReferences,PyPackageRequirements
        from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

        bearer_scheme = HTTPBearer(auto_error=False)

        @app.get("/" + args.bearer_security)
        def read_current_user(
            credentials: Optional[HTTPAuthorizationCredentials] = Security(
                bearer_scheme
            )
        ):
            if credentials is None:
                return {"msg": "Create an account first"}
            return {
                "scheme": credentials.scheme,
                "credentials": credentials.credentials,
            }

    if args.union_body is not None:

        class UnionItemA(BaseModel):
            name: str = None

        class UnionItemB(BaseModel):
            price: int

        @app.post("/" + args.union_body)
        def save_union_body(item: Union[UnionItemB, UnionItemA]):
            return {"item": item}

    if args.media_type is not None:

        class MediaProduct(BaseModel):
            name: str
            price: float

        @app.post("/" + args.media_type)
        async def create_media_product(
            data: MediaProduct = Body(
                ..., media_type="application/vnd.api+json", embed=True
            )
        ):
            return data

    client = TestClient(app)

    if args.mode == "websocket":
        with client.websocket_connect(args.url) as ws:
            print(ws.receive_text())
    elif args.form_list is not None:
        response = client.post(args.url, data={"items": args.form_list.split(",")})
        print(response.json())
        sys.exit(response.status_code)
    else:
        kwargs = {}
        if args.data is not None:
            kwargs["json"] = eval(args.data)
        if args.auth is not None:
            kwargs["headers"] = {"Authorization": " ".join(args.auth)}
        response = getattr(client, args.mode)(args.url, **kwargs)
        print(response.json())
        sys.exit(response.status_code)
