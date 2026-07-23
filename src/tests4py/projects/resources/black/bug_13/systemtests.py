from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'aW55dHVvID0gW2p4bXNic24gYXN5bmMgZm9yIGp4bXNic24gaW4gY2psZGpzZHAoKV0K'

    def test_diversity_2(self):
        return 'ZGVmIG16bGEoKToKICAgIHJldHVybiAoeGVmZWJiIGFzeW5jIGZvciB4ZWZlYmIgaW4gZml5dXooKSkK'

    def test_diversity_3(self):
        return 'ZGVmIGtkcGFwZ28oKToKICAgIHJldHVybiAob2FvIGFzeW5jIGZvciBvYW8gaW4gZ2t2Z3NvZSgpKQo='

    def test_diversity_4(self):
        return 'ZGVmIGJ4dXN4digpOgogICAgcmV0dXJuIHtodXIgYXN5bmMgZm9yIGh1ciBpbiB4bGtndnJmYygpfQo='

    def test_diversity_5(self):
        return 'ZGVmIHZ1bXJsKCk6CiAgICByZXR1cm4gKGR6bHRnY3hzIGFzeW5jIGZvciBkemx0Z2N4cyBpbiB4d3koKSkK'

    def test_diversity_6(self):
        return 'ZGVmIHVic3ZweGwoKToKICAgIHJldHVybiAoc3BsIGFzeW5jIGZvciBzcGwgaW4gZHN1Z3FiZigpKQo='

    def test_diversity_7(self):
        return 'ZGVmIGdvdGx1KCk6CiAgICByZXR1cm4gKGFxdmpvbG4gYXN5bmMgZm9yIGFxdmpvbG4gaW4gZmthZHooKSkK'

    def test_diversity_8(self):
        return 'ZGVmIHRxdGUoKToKICAgIHJldHVybiBbb2RpZ2F6d3ggYXN5bmMgZm9yIG9kaWdhend4IGluIGJlcGgoKV0K'

    def test_diversity_9(self):
        return 'ZGVmIHFya2pzeGNzKCk6CiAgICByZXR1cm4gKG9vcHVjY2kgYXN5bmMgZm9yIG9vcHVjY2kgaW4gY3VheCgpKQo='

    def test_diversity_10(self):
        return 'ZGVmIGJobnRuKCk6CiAgICByZXR1cm4ge3pwbXJwZ3ppIGFzeW5jIGZvciB6cG1ycGd6aSBpbiBoeXcoKX0K'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'ZGVmIGx2dCgpOgogICAgcmV0dXJuIFtseHpicSBmb3IgbHh6YnEgaW4geHpjZHhodigpXQo='

    def test_diversity_2(self):
        return 'ZGVmIGdwYWJ2b3goKToKICAgIHJldHVybiBbbmFkeGdwIGZvciBuYWR4Z3AgaW4gdm1mb3N2bmYoKV0K'

    def test_diversity_3(self):
        return 'YXN5bmMgZGVmIG9obigpOgogICAgcmV0dXJuIFtqZmNvdmJzYyBhc3luYyBmb3IgamZjb3Zic2MgaW4gZmJseGwoKV0K'

    def test_diversity_4(self):
        return 'YXN5bmMgZGVmIGpucygpOgogICAgcmV0dXJuIFtseXZnYXJ2eSBhc3luYyBmb3IgbHl2Z2FydnkgaW4gaW9xd2MoKV0K'

    def test_diversity_5(self):
        return 'ZGVmIHpvaHhxbGYoKToKICAgIHJldHVybiBbdXJ0IGZvciB1cnQgaW4ga3dvKCldCg=='

    def test_diversity_6(self):
        return 'ZGVmIGlmdmMoKToKICAgIHJldHVybiBbdHhqemRlaCBmb3IgdHhqemRlaCBpbiBqcWNjKCldCg=='

    def test_diversity_7(self):
        return 'ZGVmIHljbWUoKToKICAgIHJldHVybiBbdHBndiBmb3IgdHBndiBpbiBrcnJ0aygpXQo='

    def test_diversity_8(self):
        return 'YXN5bmMgZGVmIHJtbG53YygpOgogICAgcmV0dXJuIFtwdHAgYXN5bmMgZm9yIHB0cCBpbiBiaG1neW56KCldCg=='

    def test_diversity_9(self):
        return 'ZGVmIGZoaGpnbygpOgogICAgcmV0dXJuIFt5c3pobHhyIGZvciB5c3pobHhyIGluIHZ5Z3IoKV0K'

    def test_diversity_10(self):
        return 'YXN5bmMgZGVmIHV4YWhnaCgpOgogICAgcmV0dXJuIFtsa2MgYXN5bmMgZm9yIGxrYyBpbiB6ZWVqYWEoKV0K'
