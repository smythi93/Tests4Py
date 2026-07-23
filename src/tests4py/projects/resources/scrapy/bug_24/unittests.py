import unittest

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


def _t4p_tunnel_request_type(host, port):
    endpoint = TunnelingTCP4ClientEndpoint(
        reactor, host.encode("ascii"), port, ("proxy.example", 8080, None), None
    )
    protocol = _FakeProtocol()
    endpoint.requestTunnel(protocol)
    return type(protocol.transport.written).__name__


def _t4p_tunnel_port(host, port):
    endpoint = TunnelingTCP4ClientEndpoint(
        reactor, host.encode("ascii"), port, ("proxy.example", 8080, None), None
    )
    return endpoint._tunneledPort


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual("bytes", _t4p_tunnel_request_type("example.com", 443))

    def test_diversity_2(self):
        self.assertEqual("bytes", _t4p_tunnel_request_type("secure.host", 8443))

    def test_diversity_3(self):
        self.assertEqual("bytes", _t4p_tunnel_request_type("api.service.io", 9443))

    def test_diversity_4(self):
        self.assertEqual("bytes", _t4p_tunnel_request_type("data.node", 10443))

    def test_diversity_5(self):
        self.assertEqual("bytes", _t4p_tunnel_request_type("proxy.target", 4443))

    def test_diversity_6(self):
        self.assertEqual("bytes", _t4p_tunnel_request_type("cdn.assets", 2096))

    def test_diversity_7(self):
        self.assertEqual("bytes", _t4p_tunnel_request_type("mail.server", 993))

    def test_diversity_8(self):
        self.assertEqual("bytes", _t4p_tunnel_request_type("git.repo", 22443))

    def test_diversity_9(self):
        self.assertEqual("bytes", _t4p_tunnel_request_type("shop.store", 6443))

    def test_diversity_10(self):
        self.assertEqual("bytes", _t4p_tunnel_request_type("auth.gateway", 7443))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(443, _t4p_tunnel_port("example.com", 443))

    def test_diversity_2(self):
        self.assertEqual(8443, _t4p_tunnel_port("secure.host", 8443))

    def test_diversity_3(self):
        self.assertEqual(9443, _t4p_tunnel_port("api.service.io", 9443))

    def test_diversity_4(self):
        self.assertEqual(10443, _t4p_tunnel_port("data.node", 10443))

    def test_diversity_5(self):
        self.assertEqual(4443, _t4p_tunnel_port("proxy.target", 4443))

    def test_diversity_6(self):
        self.assertEqual(2096, _t4p_tunnel_port("cdn.assets", 2096))

    def test_diversity_7(self):
        self.assertEqual(993, _t4p_tunnel_port("mail.server", 993))

    def test_diversity_8(self):
        self.assertEqual(22443, _t4p_tunnel_port("git.repo", 22443))

    def test_diversity_9(self):
        self.assertEqual(6443, _t4p_tunnel_port("shop.store", 6443))

    def test_diversity_10(self):
        self.assertEqual(7443, _t4p_tunnel_port("auth.gateway", 7443))
