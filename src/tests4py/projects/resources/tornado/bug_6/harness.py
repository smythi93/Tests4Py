import asyncio
import sys

from tornado.ioloop import IOLoop
from tornado.platform.asyncio import AsyncIOLoop

if __name__ == "__main__":
    scenario = sys.argv[1]
    n = int(sys.argv[2])
    AsyncIOLoop().close()
    asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())
    orig = len(IOLoop._ioloop_for_asyncio)
    if scenario == "IOLOOP_CLOSE":
        for _ in range(n):
            loop = AsyncIOLoop()
            loop.close()
        print(len(IOLoop._ioloop_for_asyncio) - orig)
    elif scenario == "ASYNCIO_CLOSE":
        for _ in range(n):
            loop = asyncio.new_event_loop()
            loop.call_soon(IOLoop.current)
            loop.call_soon(loop.stop)
            loop.run_forever()
            loop.close()
        print(len(IOLoop._ioloop_for_asyncio) - orig)
    elif scenario == "KEEP":
        loops = []
        for _ in range(n):
            loops.append(AsyncIOLoop())
        print(len(IOLoop._ioloop_for_asyncio) - orig)
        for loop in loops:
            loop.close()
