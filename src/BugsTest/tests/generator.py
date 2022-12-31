import ast
import hashlib
import os
import random
import shutil
from pathlib import Path
from typing import List, Tuple

from BugsTest.tests.utils import TestResult


class GenerationFailed(RuntimeWarning):
    pass


class TestGenerator:

    def __init__(self, failing_probability: float = 0.2):
        self.failing_probability = failing_probability

    def generate_only_passing_tests(self, n: int, path: Path, append: bool = False):
        tmp_probability = self.failing_probability
        self.failing_probability = 0
        self.generate_tests(n, path.with_suffix('_passing'), append)
        self.failing_probability = tmp_probability

    def generate_only_failing_tests(self, n: int, path: Path, append: bool = False):
        tmp_probability = self.failing_probability
        self.failing_probability = 1
        self.generate_tests(n, path.with_suffix('_failing'), append)
        self.failing_probability = tmp_probability

    def generate_tests(self, n: int, path: Path, append: bool = False):
        return NotImplemented


class UnitTestGenerator(TestGenerator, ast.NodeVisitor):
    CLASS_NAME = 'BugsTestsUnittests'

    @staticmethod
    def get_name(function: ast.FunctionDef, result: TestResult = TestResult.UNKNOWN) -> ast.FunctionDef:
        hash_ = hashlib.md5(ast.unparse(function).encode("utf-8")).hexdigest()
        function.name = f'test_{"failing" if result == TestResult.FAILING else "passing"}_{hash_}'
        return function

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return NotImplemented

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return NotImplemented

    def generic_visit(self, node: ast.AST) -> List[ast.AST]:
        result = list()
        for field, value in ast.iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, ast.AST):
                        result += self.visit(item)
            elif isinstance(value, ast.AST):
                result += self.visit(value)
        return result

    def visit_ClassDef(self, node: ast.ClassDef) -> List[ast.AST]:
        if node.name == self.CLASS_NAME:
            return node.body
        else:
            return self.generic_visit(node)

    def generate_tests(self, n: int, path: Path, append: bool = False):
        body = list(map(lambda f: self.get_name(*f()),
                        random.choices([self.generate_failing_test, self.generate_passing_test],
                                       weights=[self.failing_probability, 1], k=n)))
        if path.exists() and path.is_dir():
            raise GenerationFailed(f'{path} is a directory')
        if append and path.exists() and path.is_file():
            with path.open('r') as fp:
                content = fp.read()
            try:
                tree = ast.parse(content)
            except SyntaxError:
                raise GenerationFailed(f'{path} is not a python file')
            body = self.visit(tree) + body
        tests = ast.unparse(
            ast.Module(
                body=[
                    ast.Import(
                        names=[ast.alias(name='unittest')]
                    ),
                    ast.ClassDef(
                        name=self.CLASS_NAME,
                        bases=[
                            ast.Attribute(
                                value=ast.Name(id='unittest'),
                                attr='TestCase'
                            )
                        ],
                        body=body,
                    )
                ],
                type_ignores=[],
            )
        )

        with open(path, 'w') as fp:
            fp.write(tests)


class SystemTestGenerator(TestGenerator):
    DIR = Path('BugsTestsSystemTests')

    @staticmethod
    def get_name(test: str, result: TestResult = TestResult.UNKNOWN, directory: Path = None) -> Path:
        directory = directory if directory else SystemTestGenerator.DIR
        hash_ = hashlib.md5(test.encode("utf-8")).hexdigest()
        return directory / f'{"failing" if result == TestResult.FAILING else "passing"}_{hash_}'

    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return NotImplemented

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return NotImplemented

    def generate_tests(self, n: int, path: Path, append: bool = False):
        if path.exists() and not path.is_dir():
            raise GenerationFailed(f'{path} is not a dir')
        if path.exists() and not append:
            shutil.rmtree(path, ignore_errors=True)
            os.makedirs(path, exist_ok=True)
        for _ in range(n):
            choice = random.choices([self.generate_failing_test, self.generate_passing_test],
                                    weights=[self.failing_probability, 1])[0]
            test, result = choice()
            with open(self.get_name(test, result, path), 'w') as fp:
                fp.write(test)
