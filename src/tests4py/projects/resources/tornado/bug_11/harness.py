import socket
import sys
import threading

import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado.testing import bind_unused_port
from tornado.web import RequestHandler
from tornado.escape import recursive_unicode


class EchoHandler(RequestHandler):
    def post(self):
        self.write(recursive_unicode(self.request.arguments))


def run_chunked(te_casing, key, value):
    holder = {}
    started = threading.Event()

    def _serve():
        io = tornado.ioloop.IOLoop()
        io.make_current()
        app = tornado.web.Application([("/echo", EchoHandler)])
        sock, port = bind_unused_port()
        server = tornado.httpserver.HTTPServer(app)
        server.add_socket(sock)
        holder["port"] = port
        holder["io"] = io
        started.set()
        io.start()

    t = threading.Thread(target=_serve, daemon=True)
    t.start()
    started.wait(10)
    try:
        body = "%s=%s" % (key, value)
        chunk = "%x\r\n%s\r\n0\r\n\r\n" % (len(body), body)
        req = (
            "POST /echo HTTP/1.1\r\nTransfer-Encoding: %s\r\n"
            "Content-Type: application/x-www-form-urlencoded\r\n\r\n%s"
            % (te_casing, chunk)
        )
        s = socket.create_connection(("127.0.0.1", holder["port"]), timeout=10)
        s.settimeout(10)
        s.sendall(req.encode())
        data = b""
        while b"\r\n\r\n" not in data:
            data += s.recv(4096)
        header, _, rest = data.partition(b"\r\n\r\n")
        cl = 0
        for line in header.split(b"\r\n"):
            if line.lower().startswith(b"content-length:"):
                cl = int(line.split(b":")[1].strip())
        body_bytes = rest
        while len(body_bytes) < cl:
            body_bytes += s.recv(4096)
        s.close()
        return body_bytes[:cl].decode()
    finally:
        holder["io"].add_callback(holder["io"].stop)
        t.join(10)


if __name__ == "__main__":
    te_casing = sys.argv[1]
    key = sys.argv[2]
    value = sys.argv[3]
    print(run_chunked(te_casing, key, value))
