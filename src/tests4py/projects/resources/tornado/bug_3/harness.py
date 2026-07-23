import subprocess
import sys

SNIPPETS = {
    "LAMBDA": "from tornado.httpclient import HTTPClient; f = lambda: None; c = HTTPClient()",
    "INT": "from tornado.httpclient import HTTPClient; f = 5; c = HTTPClient()",
}

if __name__ == "__main__":
    mode = sys.argv[1]
    proc = subprocess.run(
        [sys.executable, "-c", SNIPPETS[mode]],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    print("OUTPUT" if proc.stdout.strip() else "CLEAN")
