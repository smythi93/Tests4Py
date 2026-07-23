from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'QGl0eQojIHp5c2Z0cQpAYWJzdHJhY3RtZXRob2QKZGVmIHdxdGtzZWpiKCk6CiAgICBwYXNzCg=='

    def test_diversity_2(self):
        return 'QGFic3RyYWN0bWV0aG9kCiMgYmluY2ltdAojIGFpd2JxaAojIFRPRE86IGxvdGFuCkBhYnN0cmFjdG1ldGhvZApkZWYgZGdhZmhnKCk6CiAgICBwYXNzCg=='

    def test_diversity_3(self):
        return 'QGNhY2hlZAojIE5PVEUgcG9vamdmCiMgaGFuZGxlcyB6ZGVrCiMgRklYTUUgcHNjdmpjYm4KQGJ3d3l1awpkZWYgaHNyKCk6CiAgICBwYXNzCg=='

    def test_diversity_4(self):
        return 'QHpkemEKIyBpdWduCiMgTk9URSB3dXd6eXJ1CkB1bmF1bGNqcApkZWYgYXd1enF4YmgoKToKICAgIHBhc3MK'

    def test_diversity_5(self):
        return 'QGZ1bmN0b29scy5scnVfY2FjaGUKIyBGSVhNRSBnZGwKQHBuaXdkbwpkZWYgY3d6eGN3KCk6CiAgICBwYXNzCg=='

    def test_diversity_6(self):
        return 'QGNhY2hlZAojIFRPRE86IGhwaGZwcnQKIyBUT0RPOiBxYncKQGF4dXZhCmRlZiBxbWVsZHR4bCgpOgogICAgcGFzcwo='

    def test_diversity_7(self):
        return 'QGhqZWJtZAojIE5PVEUgaXN0cmMKIyBOT1RFIHhkeWdkb2NmCiMgYnZsaGp1ZQpAdHdhZm5hdgpkZWYgcWhqbGh4YSgpOgogICAgcGFzcwo='

    def test_diversity_8(self):
        return 'QGNjeGN5bmsKIyBOT1RFIHVkcHcKIyBoYW5kbGVzIHpmcXoKQGFwcC5yb3V0ZQpkZWYgaHdvcHMoKToKICAgIHBhc3MK'

    def test_diversity_9(self):
        return 'QHNtcnRicmwKIyBrZGx0bwpAbGVreApkZWYgend2KCk6CiAgICBwYXNzCg=='

    def test_diversity_10(self):
        return 'QHN0YXRpY21ldGhvZAojIEZJWE1FIHpnYWpxaHcKQHZtdm9qZGMKZGVmIGx3a3NsZSgpOgogICAgcGFzcwo='


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'QHdyYXBzCmRlZiBlb3koKToKICAgICMgZnl3YW1ndXUKICAgIHJldHVybiAzMwo='

    def test_diversity_2(self):
        return 'ZGVmIGh6dXl1cCh4ZGl0LCBpa2d2bik6CiAgICByZXR1cm4gMzAK'

    def test_diversity_3(self):
        return 'ZGVmIHJ5a3NsaXFsKGJtenhzLCB5enVjKToKICAgIHJldHVybiA0NQo='

    def test_diversity_4(self):
        return 'QHRkeHVtYwpAcHl0ZXN0LmZpeHR1cmUKZGVmIGJkdWpxc3IoKToKICAgIHBhc3MK'

    def test_diversity_5(self):
        return 'QHFpZXZ1CkBsZmxrdQpkZWYgZWJ1ZmkoKToKICAgIHBhc3MK'

    def test_diversity_6(self):
        return 'QHB5dGVzdC5maXh0dXJlCkBjZ3UKZGVmIHphdSgpOgogICAgcGFzcwo='

    def test_diversity_7(self):
        return 'QGNhY2hlZApAa3pueHcKZGVmIHZ3Y3goKToKICAgIHBhc3MK'

    def test_diversity_8(self):
        return 'QHRvbW8KQGt4eGFtdWdyCmRlZiB3ZWJ2eGRlKCk6CiAgICBwYXNzCg=='

    def test_diversity_9(self):
        return 'ZGVmIG1kYihpaWZhbG1tLCB0YmdmZyk6CiAgICByZXR1cm4gNDAK'

    def test_diversity_10(self):
        return 'QHB5dGVzdC5maXh0dXJlCmRlZiBtcnpxcmZxZygpOgogICAgIyB0YXRmd2VsCiAgICByZXR1cm4gNzEK'
