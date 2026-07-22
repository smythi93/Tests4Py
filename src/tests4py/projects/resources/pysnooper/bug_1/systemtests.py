from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    # A value with non-ASCII (Chinese) characters. When pysnooper writes the
    # trace to the log file, the buggy FileWriter uses the process default
    # encoding; under an ASCII locale this raises UnicodeEncodeError.
    def test_diversity_1(self):
        return "失败"

    def test_diversity_2(self):
        return "测试值"

    def test_diversity_3(self):
        return "abc中文"

    def test_diversity_4(self):
        return "你好 world"

    def test_diversity_5(self):
        return "变量输出"

    def test_diversity_6(self):
        return "data编码123"

    def test_diversity_7(self):
        return "世界字符"

    def test_diversity_8(self):
        return "x失败y测试"

    def test_diversity_9(self):
        return "中文编码变量"

    def test_diversity_10(self):
        return "log你好世界"


class TestsPassing(PassingSystemtests):
    # A pure-ASCII value: the trace is written correctly on the buggy build.
    def test_diversity_1(self):
        return "plain value"

    def test_diversity_2(self):
        return "hello world"

    def test_diversity_3(self):
        return "abc123"

    def test_diversity_4(self):
        return "test data"

    def test_diversity_5(self):
        return "variable output"

    def test_diversity_6(self):
        return "snoop log"

    def test_diversity_7(self):
        return "some_value"

    def test_diversity_8(self):
        return "another one"

    def test_diversity_9(self):
        return "final value"

    def test_diversity_10(self):
        return "ascii only text"
