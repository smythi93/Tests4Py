import ast
import hashlib
import os
import shutil
from abc import abstractmethod
from pathlib import Path
from typing import List, Tuple

from tests4py.constants import DEFAULT_SYSTEMTESTS_DIVERSITY_PATH
from tests4py.tests.utils import TestResult


class GenerationFailed(RuntimeWarning):
    pass


class GenerationResult:
    def __init__(self, passing: int = 0, failing: int = 0):
        self.passing = passing
        self.failing = failing


class TestGenerator:
    def __init__(self, failing_probability: float = 0.2):
        self.failing_probability = failing_probability

    def generate_only_passing_tests(
        self, n: int, path: Path, append: bool = False
    ) -> GenerationResult:
        tmp_probability = self.failing_probability
        self.failing_probability = 0
        self.generate_tests(n, path.with_suffix("_passing"), append)
        self.failing_probability = tmp_probability
        return GenerationResult(passing=n)

    def generate_only_failing_tests(
        self, n: int, path: Path, append: bool = False
    ) -> GenerationResult:
        tmp_probability = self.failing_probability
        self.failing_probability = 1
        self.generate_tests(n, path.with_suffix("_failing"), append)
        self.failing_probability = tmp_probability
        return GenerationResult(failing=n)

    def generate_tests(
        self, n: int, path: Path, append: bool = False
    ) -> GenerationResult:
        return NotImplemented


class UnittestGenerator(TestGenerator, ast.NodeVisitor):
    CLASS_NAME = "Tests4PyUnittests"

    @staticmethod
    def get_empty_test() -> ast.FunctionDef:
        return ast.FunctionDef(
            name="test",
            args=ast.arguments(
                args=[ast.arg(arg="self")],
                posonlyargs=[],
                kwonlyargs=[],
                kw_defaults=[],
                defaults=[],
            ),
            decorator_list=[],
            body=[],
            lineno=0,
        )

    @staticmethod
    def get_name(
        function: ast.FunctionDef, result: TestResult = TestResult.UNDEFINED
    ) -> ast.FunctionDef:
        hash_ = hashlib.md5(ast.unparse(function).encode("utf-8")).hexdigest()
        function.name = (
            f'test_{"failing" if result == TestResult.FAILING else "passing"}_{hash_}'
        )
        return function

    @abstractmethod
    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return NotImplemented

    @abstractmethod
    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return NotImplemented

    def get_utils(self) -> List[ast.stmt]:
        return list()

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

    def generate_tests(
        self, n: int, path: Path, append: bool = False
    ) -> GenerationResult:
        f = int(n * self.failing_probability)
        p = n - f
        body = (
            self.get_utils()
            + [self.get_name(*self.generate_passing_test()) for _ in range(p)]
            + [self.get_name(*self.generate_failing_test()) for _ in range(f)]
        )
        if path.exists() and path.is_dir():
            raise GenerationFailed(f"{path} is a directory")
        if append and path.exists() and path.is_file():
            with path.open("r") as fp:
                content = fp.read()
            try:
                tree = ast.parse(content)
            except SyntaxError:
                raise GenerationFailed(f"{path} is not a python file")
            body = self.visit(tree) + body
        tests = ast.unparse(
            ast.Module(
                body=[
                    ast.Import(names=[ast.alias(name="unittest")]),
                ]
                + self.get_imports()
                + [
                    ast.ClassDef(
                        name=self.CLASS_NAME,
                        bases=[
                            ast.Attribute(
                                value=ast.Name(id="unittest"), attr="TestCase"
                            )
                        ],
                        body=body,
                        keywords=[],
                        decorator_list=[],
                    ),
                ],
                type_ignores=[],
            )
        )

        with open(path, "w") as fp:
            fp.write(tests)
        return GenerationResult(passing=p, failing=f)

    def get_imports(self) -> List[ast.stmt]:
        return []


class SystemtestGenerator(TestGenerator):
    @staticmethod
    def get_name(
        test: str, result: TestResult = TestResult.UNDEFINED, directory: Path = None
    ) -> Path:
        directory = directory if directory else DEFAULT_SYSTEMTESTS_DIVERSITY_PATH
        hash_ = hashlib.md5(test.encode("utf-8")).hexdigest()
        return (
            directory
            / f'{"failing" if result == TestResult.FAILING else "passing"}_{hash_}'
        )

    @abstractmethod
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return NotImplemented

    @abstractmethod
    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return NotImplemented

    def generate_tests(
        self, n: int, path: Path, append: bool = False
    ) -> GenerationResult:
        if path.exists() and not path.is_dir():
            raise GenerationFailed(f"{path} is not a dir")
        elif path.exists() and not append:
            shutil.rmtree(path, ignore_errors=True)
            os.makedirs(path, exist_ok=True)
        elif not path.exists():
            os.makedirs(path, exist_ok=True)
        f = int(n * self.failing_probability)
        p = n - f
        tests = {None}
        for _ in range(p):
            test, result, name = "", TestResult.UNDEFINED, None
            while name in tests:
                test, result = self.generate_passing_test()
                name = self.get_name(test, result, path)
            tests.add(name)
            with open(name, "w") as fp:
                fp.write(test)
        for _ in range(f):
            test, result, name = "", TestResult.UNDEFINED, None
            while name in tests:
                test, result = self.generate_failing_test()
                name = self.get_name(test, result, path)
            tests.add(name)
            with open(self.get_name(test, result, path), "w") as fp:
                fp.write(test)
        return GenerationResult(passing=p, failing=f)
