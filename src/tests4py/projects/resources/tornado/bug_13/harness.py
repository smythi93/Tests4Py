import socket
import sys

import tornado.ioloop
from tornado.iostream import IOStream
from tornado.testing import bind_unused_port
from tornado.netutil import add_accept_handler
from tornado.http1connection import HTTP1Connection
from tornado.httputil import HTTPMessageDelegate
from tornado.locks import Event
from tornado import gen


def run_response(mode, body):
    io = tornado.ioloop.IOLoop()
    io.make_current()
    result = {}

    @gen.coroutine
    def _main():
        listener, port = bind_unused_port()
        ev = Event()
        holder = {}

        def _accept(conn, addr):
            holder["server"] = IOStream(conn)
            ev.set()

        add_accept_handler(listener, _accept, io_loop=io)
        client = IOStream(socket.socket())
        yield [client.connect(("127.0.0.1", port)), ev.wait()]
        io.remove_handler(listener)
        listener.close()
        server = holder["server"]
        conn = HTTP1Connection(client, True)
        b = body.encode()
        if mode == "HTTP10_NOCL":
            server.write(b"HTTP/1.0 200 OK\r\n\r\n" + b)
        elif mode == "HTTP11_CL":
            server.write(b"HTTP/1.1 200 OK\r\nContent-Length: %d\r\n\r\n" % len(b) + b)
        elif mode == "HTTP10_CL":
            server.write(b"HTTP/1.0 200 OK\r\nContent-Length: %d\r\n\r\n" % len(b) + b)
        server.close()
        code = [None]
        got = []
        done = Event()

        class _D(HTTPMessageDelegate):
            def headers_received(self, start_line, headers):
                code[0] = start_line.code

            def data_received(self, data):
                got.append(data)

            def finish(self):
                done.set()

        try:
            yield conn.read_response(_D())
            yield done.wait()
            result["out"] = "%s,%s" % (code[0], b"".join(got).decode())
        except Exception as e:
            result["out"] = "ERROR:%s" % type(e).__name__

    io.run_sync(_main)
    return result["out"]


if __name__ == "__main__":
    print(run_response(sys.argv[1], sys.argv[2]))
