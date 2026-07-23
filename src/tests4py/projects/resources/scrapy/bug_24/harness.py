import sys

# noinspection PyUnresolvedReferences
from scrapy.core.downloader.handlers.http11 import TunnelingTCP4ClientEndpoint

# noinspection PyUnresolvedReferences
from twisted.internet import reactor


class _FakeTransport(object):
    def __init__(self):
        self.written = None

    def write(self, data):
        self.written = data


class _FakeProtocol(object):
    def __init__(self):
        self.transport = _FakeTransport()
        self.dataReceived = None


def _make_endpoint(host, port):
    return TunnelingTCP4ClientEndpoint(
        reactor,
        host.encode("ascii"),
        port,
        ("proxy.example", 8080, None),
        None,
    )


if __name__ == "__main__":
    mode = sys.argv[1]
    host = sys.argv[2]
    port = int(sys.argv[3])
    try:
        endpoint = _make_endpoint(host, port)
        if mode == "request":
            protocol = _FakeProtocol()
            endpoint.requestTunnel(protocol)
            written = protocol.transport.written
            print("RESULT:" + type(written).__name__)
        else:
            print("RESULT:" + str(endpoint._tunneledPort))
    except Exception as exception:  # noqa: BLE001
        print("RESULT:ERR:" + type(exception).__name__)
