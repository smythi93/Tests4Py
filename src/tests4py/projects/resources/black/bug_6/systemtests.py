from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'ZGVmIGFzeW5jKCk6CiAgICB4dGd3c29iID0gMjY5CiAgICByZXR1cm4geHRnd3NvYgo= err'

    def test_diversity_2(self):
        return 'YXdhaXQgPSA3NjgKYXdhaXQoKQo= err'

    def test_diversity_3(self):
        return 'YXN5bmMgPSA4NTgKYXN5bmMoKQo= err'

    def test_diversity_4(self):
        return 'YXN5bmMgPSBsYW1iZGE6IDYyNQphc3luYygpCg== err'

    def test_diversity_5(self):
        return 'ZGVmIHJxYXZhamsoKToKICAgIGFzeW5jID0gMTQ0CiAgICByZXR1cm4gYXN5bmMK err'

    def test_diversity_6(self):
        return 'YXdhaXQgPSA1MjEKYXdhaXQoKQo= err'

    def test_diversity_7(self):
        return 'YXdhaXQgPSBsYW1iZGE6IDEzNgphd2FpdCgpCg== err'

    def test_diversity_8(self):
        return 'YXdhaXQgPSA3MjIKYXdhaXQoKQo= err'

    def test_diversity_9(self):
        return 'YXN5bmMgPSBsYW1iZGE6IDg1Nwphc3luYygpCg== err'

    def test_diversity_10(self):
        return 'YXN5bmMgPSBsYW1iZGE6IDQwNwphc3luYygpCg== err'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'bWJoID0gMAo= ok'

    def test_diversity_2(self):
        return 'ZGVmIGJ0em5oKHhxZmtoKToKICAgIHJldHVybiA0Cg== ok'

    def test_diversity_3(self):
        return 'YXN5bmMgZGVmIHFpcXooKToKICAgIGF3YWl0IHVkZXBjKCkK ok'

    def test_diversity_4(self):
        return 'ZGVmIHdjZmZ1KHJmcXh1bSk6CiAgICByZXR1cm4gMQo= ok'

    def test_diversity_5(self):
        return 'ZGVmIHd2bGgob3doKToKICAgIHJldHVybiA1Cg== ok'

    def test_diversity_6(self):
        return 'YXN5bmMgZGVmIHllaG5wbG92KCk6CiAgICBhd2FpdCB3bnd0cnZzdCgpCg== ok'

    def test_diversity_7(self):
        return 'YXN5bmMgZGVmIG9yYWQoKToKICAgIGF3YWl0IHdycW10eWwoKQo= ok'

    def test_diversity_8(self):
        return 'YXN5bmMgZGVmIGp6dW1rcWooKToKICAgIGF3YWl0IGJpdGZucHB4KCkK ok'

    def test_diversity_9(self):
        return 'ZGVmIGFxcChiZHFkY3NxZyk6CiAgICByZXR1cm4gMwo= ok'

    def test_diversity_10(self):
        return 'ZGVmIGh3cXhuZnVnKG9zaHVkbmxxKToKICAgIHJldHVybiAxCg== ok'
