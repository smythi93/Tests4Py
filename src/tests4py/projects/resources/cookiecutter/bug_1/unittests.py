import os
import subprocess
import sys
import tempfile
import unittest
from abc import ABC


class DefaultTests(unittest.TestCase, ABC):
    @staticmethod
    def run_generate_context(content):
        """Write ``content`` to a JSON file and load it through
        ``cookiecutter.generate.generate_context`` in a subprocess forced to an
        ASCII locale. Returns the subprocess return code (0 on success)."""
        path = os.path.join(tempfile.mkdtemp(), "cc1_context.json")
        with open(path, "w", encoding="utf-8") as fp:
            fp.write(content)
        env = dict(os.environ)
        env["LC_ALL"] = "C"
        env["LANG"] = "C"
        env["LC_CTYPE"] = "C"
        env.pop("PYTHONUTF8", None)
        env.pop("PYTHONIOENCODING", None)
        code = (
            "from cookiecutter.generate import generate_context; "
            "generate_context(context_file=%r)" % path
        )
        proc = subprocess.run(
            [sys.executable, "-c", code],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=env,
        )
        return proc.returncode


class TestsFailing(DefaultTests):
    # Non-ASCII context: reading it under an ASCII locale fails on the buggy
    # build (return code != 0), so asserting success fails here.
    def test_diversity_1(self):
        self.assertEqual(0, self.run_generate_context('{"full_name":"café"}'))

    def test_diversity_2(self):
        self.assertEqual(0, self.run_generate_context('{"full_name":"résumé"}'))

    def test_diversity_3(self):
        self.assertEqual(0, self.run_generate_context('{"full_name":"Müller"}'))

    def test_diversity_4(self):
        self.assertEqual(0, self.run_generate_context('{"full_name":"José Niño"}'))

    def test_diversity_5(self):
        self.assertEqual(0, self.run_generate_context('{"full_name":"ångstrom"}'))

    def test_diversity_6(self):
        self.assertEqual(0, self.run_generate_context('{"full_name":"naïve"}'))

    def test_diversity_7(self):
        self.assertEqual(0, self.run_generate_context('{"full_name":"François"}'))

    def test_diversity_8(self):
        self.assertEqual(0, self.run_generate_context('{"full_name":"straße"}'))

    def test_diversity_9(self):
        self.assertEqual(0, self.run_generate_context('{"full_name":"øresund"}'))

    def test_diversity_10(self):
        self.assertEqual(0, self.run_generate_context('{"full_name":"zürich äöü"}'))


class TestsPassing(DefaultTests):
    # Pure-ASCII context reads correctly on the buggy build.
    def test_diversity_1(self):
        self.assertEqual(0, self.run_generate_context('{"full_name":"John Doe"}'))

    def test_diversity_2(self):
        self.assertEqual(0, self.run_generate_context('{"full_name":"Jane Smith"}'))

    def test_diversity_3(self):
        self.assertEqual(0, self.run_generate_context('{"full_name":"Marius"}'))

    def test_diversity_4(self):
        self.assertEqual(0, self.run_generate_context('{"full_name":"Alan Turing"}'))

    def test_diversity_5(self):
        self.assertEqual(0, self.run_generate_context('{"full_name":"Grace Hopper"}'))

    def test_diversity_6(self):
        self.assertEqual(0, self.run_generate_context('{"full_name":"Ada Lovelace"}'))

    def test_diversity_7(self):
        self.assertEqual(0, self.run_generate_context('{"full_name":"Linus T"}'))

    def test_diversity_8(self):
        self.assertEqual(0, self.run_generate_context('{"full_name":"Donald Knuth"}'))

    def test_diversity_9(self):
        self.assertEqual(0, self.run_generate_context('{"full_name":"Liskov"}'))

    def test_diversity_10(self):
        self.assertEqual(0, self.run_generate_context('{"full_name":"Dijkstra"}'))
