import datetime
import sys

from tornado.ioloop import IOLoop
from tornado import gen

if __name__ == "__main__":
    scenario = sys.argv[1]
    io = IOLoop()
    io.make_current()

    @gen.coroutine
    def _main():
        try:
            if scenario == "WAIT_NOREF":
                yield gen.with_timeout(
                    datetime.timedelta(seconds=0.5),
                    gen.WaitIterator(gen.sleep(0)).next(),
                )
            else:
                wi = gen.WaitIterator(gen.sleep(0))
                yield gen.with_timeout(datetime.timedelta(seconds=0.5), wi.next())
            raise gen.Return("OK")
        except gen.TimeoutError:
            raise gen.Return("TIMEOUT")

    try:
        print(io.run_sync(_main))
    finally:
        io.close()
