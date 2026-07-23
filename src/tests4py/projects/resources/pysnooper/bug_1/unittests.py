import os
import subprocess
import sys
import tempfile
import unittest
from abc import ABC

SNOOP_PROGRAM = (
    "import os, tempfile, pysnooper\n"
    "value = open(os.environ['TESTS4PY_PS1_VALUE'], encoding='utf-8').read()\n"
    "log = os.path.join(tempfile.mkdtemp(), 'snoop.log')\n"
    "@pysnooper.snoop(log)\n"
    "def foo():\n"
    "    x = value\n"
    "    return x\n"
    "foo()\n"
    "open(log, encoding='utf-8').read()\n"
)


class DefaultTests(unittest.TestCase, ABC):
    @staticmethod
    def run_snoop(value):
        """Trace a function whose local variable holds ``value`` and write the
        trace to a log file, in a subprocess forced to an ASCII locale. Returns
        the subprocess return code (0 on success)."""
        d = tempfile.mkdtemp()
        value_path = os.path.join(d, "value.txt")
        with open(value_path, "w", encoding="utf-8") as fp:
            fp.write(value)
        env = dict(os.environ)
        env["TESTS4PY_PS1_VALUE"] = value_path
        env["LC_ALL"] = "C"
        env["LANG"] = "C"
        env["LC_CTYPE"] = "C"
        env["PYTHONCOERCECLOCALE"] = "0"
        env["PYTHONUTF8"] = "0"
        env.pop("PYTHONIOENCODING", None)
        proc = subprocess.run(
            [sys.executable, "-c", SNOOP_PROGRAM],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=env,
        )
        return proc.returncode


class TestsFailing(DefaultTests):
    # Non-ASCII values: writing the trace fails on the buggy build.
    def test_diversity_1(self):
        self.assertEqual(0, self.run_snoop("失败"))

    def test_diversity_2(self):
        self.assertEqual(0, self.run_snoop("测试值"))

    def test_diversity_3(self):
        self.assertEqual(0, self.run_snoop("abc中文"))

    def test_diversity_4(self):
        self.assertEqual(0, self.run_snoop("你好 world"))

    def test_diversity_5(self):
        self.assertEqual(0, self.run_snoop("变量输出"))

    def test_diversity_6(self):
        self.assertEqual(0, self.run_snoop("data编码123"))

    def test_diversity_7(self):
        self.assertEqual(0, self.run_snoop("世界字符"))

    def test_diversity_8(self):
        self.assertEqual(0, self.run_snoop("x失败y测试"))

    def test_diversity_9(self):
        self.assertEqual(0, self.run_snoop("中文编码变量"))

    def test_diversity_10(self):
        self.assertEqual(0, self.run_snoop("log你好世界"))


class TestsPassing(DefaultTests):
    # Pure-ASCII values: the trace is written correctly on the buggy build.
    def test_diversity_1(self):
        self.assertEqual(0, self.run_snoop("plain value"))

    def test_diversity_2(self):
        self.assertEqual(0, self.run_snoop("hello world"))

    def test_diversity_3(self):
        self.assertEqual(0, self.run_snoop("abc123"))

    def test_diversity_4(self):
        self.assertEqual(0, self.run_snoop("test data"))

    def test_diversity_5(self):
        self.assertEqual(0, self.run_snoop("variable output"))

    def test_diversity_6(self):
        self.assertEqual(0, self.run_snoop("snoop log"))

    def test_diversity_7(self):
        self.assertEqual(0, self.run_snoop("some_value"))

    def test_diversity_8(self):
        self.assertEqual(0, self.run_snoop("another one"))

    def test_diversity_9(self):
        self.assertEqual(0, self.run_snoop("final value"))

    def test_diversity_10(self):
        self.assertEqual(0, self.run_snoop("ascii only text"))
