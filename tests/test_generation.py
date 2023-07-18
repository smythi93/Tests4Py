import os
import random
import subprocess
import tempfile
import unittest

from tests4py.grammars import python


class TestPythonGeneration(unittest.TestCase):
    def setUp(self) -> None:
        self.generator = python.PythonGenerator(
            limit_stmt_per_block=3,
            limit_stmt_depth=3,
            limit_expr_depth=2,
            limit_args_per_function=2,
        )

    def test_fuzzing_50_syntax(self):
        self._test_fuzzing_syntax(50)

    def test_fuzzing_50_syntax_seed(self):
        self._test_fuzzing_syntax(50, seed=21)

    def test_fuzzing_50_semantic(self):
        self._test_fuzzing_semantic(50)

    def test_fuzzing_50_semantic_seed(self):
        self._test_fuzzing_semantic(50, seed=21)

    def _test_fuzzing_syntax(self, n, seed=42):
        random.seed(seed)
        for _ in range(n):
            self.generator.reset()
            self.assertIsNotNone(self.generator.generate())

    def _test_fuzzing_semantic(self, n, seed=42):
        random.seed(seed)
        for _ in range(n):
            self.generator.reset()
            p = self.generator.generate()
            self.assertIsNotNone(p)
            with tempfile.NamedTemporaryFile("w+", suffix=".py", delete=False) as fp:
                fp.write(p)
            process = subprocess.run(
                ["python3.10", fp.name], stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            os.remove(fp.name)
            self.assertEqual(0, process.returncode)
