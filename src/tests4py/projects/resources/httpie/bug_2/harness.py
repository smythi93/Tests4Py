import sys
import tempfile
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from httpie.context import Environment
from httpie.core import main


class _RedirectHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            n = int(self.path.rstrip("/").split("/")[-1])
        except ValueError:
            n = 0
        if n > 0:
            self.send_response(302)
            self.send_header("Location", "/redirect/%d" % (n - 1))
            self.end_headers()
        else:
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"done")

    def log_message(self, *args):
        pass


def run_redirects(max_redirects, chain_length):
    server = HTTPServer(("127.0.0.1", 0), _RedirectHandler)
    port = server.server_address[1]
    threading.Thread(target=server.serve_forever, daemon=True).start()
    env = Environment(
        stdout=tempfile.TemporaryFile("w+b"),
        stderr=tempfile.TemporaryFile("w+t"),
        stdin_isatty=True,
        stdout_isatty=False,
        colors=0,
        config_dir=tempfile.mkdtemp(),
    )
    try:
        return main(
            [
                "--max-redirects=%d" % max_redirects,
                "--follow",
                "http://127.0.0.1:%d/redirect/%d" % (port, chain_length),
            ],
            env=env,
        )
    finally:
        server.shutdown()


if __name__ == "__main__":
    # argv: max_redirects chain_length
    m = int(sys.argv[1])
    n = int(sys.argv[2])
    print(run_redirects(m, n))
