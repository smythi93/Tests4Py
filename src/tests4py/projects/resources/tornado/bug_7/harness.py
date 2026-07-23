import sys

from tornado.ioloop import IOLoop

if __name__ == "__main__":
    mode = sys.argv[1]
    word = sys.argv[2]
    io = IOLoop()
    io.make_current()

    async def _run():
        if mode == "EXECUTOR":
            return str(await io.run_in_executor(None, len, word))
        return word

    try:
        print(io.run_sync(_run))
    except Exception as e:
        print("ERROR:%s" % type(e).__name__)
    finally:
        io.close()
