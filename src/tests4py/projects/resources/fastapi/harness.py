import argparse
import sys

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

    arguments.add_argument(
        "-ws", dest="websockets", nargs=2, metavar=("url", "dependency")
    )
    arguments.add_argument("-ds", dest="dependencies", action="append")
    arguments.add_argument(
        "-os",
        dest="overrides",
        action="append",
        nargs=2,
        metavar=("dependency", "override"),
    )
    arguments.add_argument(
        "-c",
        dest="overrides",
        action="append",
        nargs=2,
        metavar=("dependency", "override"),
    )
    arguments.add_argument(
        "-m", dest="mode", required=True, choices=["websocket", "get", "post"]
    )
    arguments.add_argument("-u", dest="url", required=True)
    arguments.add_argument("-d", dest="data")

    args = arguments.parse_args()

    app = FastAPI()
    router = APIRouter()

    dependencies = dict()

    for dep in args.dependencies:

        async def dependency():
            return dep

        dependencies[dep] = dependency

    for dep, over in args.overrides:

        async def dependency():
            return dep

        async def override():
            return over

        dependencies[dep] = dependency
        app.dependency_overrides[dependency] = override

    for url, dep in args.websockets:

        @app.websocket(url)
        async def app_ws(websocket: WebSocket, data=Depends(dependencies[dep])):
            await websocket.accept()
            await websocket.send_text(data)
            await websocket.close()

    client = TestClient(app)

    if args.mode == "websocket":
        with client.websocket_connect(args.url) as websocket:
            print(websocket.receive_text())
    else:
        if args.data is None:
            response = getattr(client, args.mode)(args.url)
        else:
            response = getattr(client, args.mode)(args.url, json=eval(args.data))
        print(response.json())
        sys.exit(response.status_code)
