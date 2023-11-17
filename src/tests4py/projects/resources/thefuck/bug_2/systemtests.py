from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "C:\\Windows\\System32;C:\\Windows;C:\\Program Files\\Java\\jdk1.8.0_181\\bin;C:\\Program Files (x86)\\user1\\bin"

    def test_diversity_2(self):
        return "C:\\Windows\\System32;C:\\Windows;C:\\Program Files\\Java\\jdk1.8.0_181\\bin;C:\\Program Files (x86)\\user1\\bin"

    def test_diversity_3(self):
        return "C:\\Windows\\System32;C:\\Windows;C:\\Program Files\\Java\\jdk1.8.0_181\\bin;C:\\Program Files (x86)\\user1\\bin"

    def test_diversity_4(self):
        return "C:\\Windows\\System32;C:\\Windows;C:\\Program Files\\Java\\jdk1.8.0_181\\bin;C:\\Program Files (x86)\\user1\\bin"

    def test_diversity_5(self):
        return "C:\\Windows\\System32;C:\\Windows;C:\\Program Files\\Java\\jdk1.8.0_181\\bin;C:\\Program Files (x86)\\user1\\bin"

    def test_diversity_6(self):
        return "C:\\Windows\\System32;C:\\Windows;C:\\Program Files\\Java\\jdk1.8.0_181\\bin;C:\\Program Files (x86)\\user1\\bin"

    def test_diversity_7(self):
        return "C:\\Windows\\System32;C:\\Windows;C:\\Program Files\\Java\\jdk1.8.0_181\\bin;C:\\Program Files (x86)\\user1\\bin"

    def test_diversity_8(self):
        return "C:\\Windows\\System32;C:\\Windows;C:\\Program Files\\Java\\jdk1.8.0_181\\bin;C:\\Program Files (x86)\\user1\\bin"

    def test_diversity_9(self):
        return "C:\\Windows\\System32;C:\\Windows;C:\\Program Files\\Java\\jdk1.8.0_181\\bin;C:\\Program Files (x86)\\user1\\bin"

    def test_diversity_10(self):
        return "C:\\Windows\\System32;C:\\Windows;C:\\Program Files\\Java\\jdk1.8.0_181\\bin;C:\\Program Files (x86)\\user1\\bin"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "disktool"

    def test_diversity_2(self):
        return "t4p"

    def test_diversity_3(self):
        return "pip"

    def test_diversity_4(self):
        return "pip3"

    def test_diversity_5(self):
        return "screen"

    def test_diversity_6(self):
        return "heap"

    def test_diversity_7(self):
        return "jarsigner"

    def test_diversity_8(self):
        return "bundler"

    def test_diversity_9(self):
        return "libtool"

    def test_diversity_10(self):
        return "nl"
