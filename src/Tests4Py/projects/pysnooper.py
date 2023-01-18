import ast
import os
import subprocess
import tempfile
from os import PathLike
from pathlib import Path
from typing import List, Optional, Tuple

from Tests4Py.grammars import python
from Tests4Py.projects import Project, Status, TestingFramework, TestStatus
from Tests4Py.tests.generator import UnittestGenerator, SystemtestGenerator
from Tests4Py.tests.utils import API, TestResult


class PySnooper(Project):

    def __init__(self, bug_id: int, python_version: str, python_path: str,
                 buggy_commit_id: str, fixed_commit_id: str, test_file: List[Path], test_cases: List[str],
                 darwin_python_version: Optional[str] = None,
                 test_status_fixed: TestStatus = TestStatus.PASSING,
                 test_status_buggy: TestStatus = TestStatus.FAILING,
                 unittests: Optional[UnittestGenerator] = None,
                 systemtests: Optional[SystemtestGenerator] = None,
                 api: Optional[API] = None):
        super().__init__(bug_id=bug_id, project_name='pysnooper', github_url='https://github.com/cool-RR/PySnooper',
                         status=Status.OK, cause='N.A.',
                         python_version=python_version, python_path=python_path, buggy_commit_id=buggy_commit_id,
                         fixed_commit_id=fixed_commit_id, testing_framework=TestingFramework.PYTEST,
                         test_file=test_file, test_cases=test_cases, darwin_python_version=darwin_python_version,
                         test_status_fixed=test_status_fixed, test_status_buggy=test_status_buggy,
                         unittests=unittests, systemtests=systemtests, api=api, grammar=python.GENERATIVE_GRAMMAR)


def register():
    PySnooper(
        bug_id=1,
        python_version='3.8.1',
        darwin_python_version='3.8.4',  # version 3.8.1-3 do not work on mac os
        python_path='',
        buggy_commit_id='e21a31162f4c54be693d8ca8260e42393b39abd3',
        fixed_commit_id='56f22f8ffe1c6b2be4d2cf3ad1987fdb66113da2',
        test_file=[Path('tests', 'test_chinese.py')],
        test_cases=['tests/test_chinese.py::test_chinese'],
        test_status_buggy=TestStatus.PASSING,
    )
    PySnooper(
        bug_id=2,
        python_version='3.8.1',
        darwin_python_version='3.8.4',  # version 3.8.1-3 do not work on mac os
        python_path='',
        buggy_commit_id='e21a31162f4c54be693d8ca8260e42393b39abd3',
        fixed_commit_id='814abc34a098c1b98cb327105ac396f985d2413e',
        test_file=[Path('tests', 'test_pysnooper.py'), Path('tests', 'mini_toolbox'), Path('pysnooper', 'pycompat.py'),
                   Path('pysnooper', 'utils.py')],
        test_cases=['tests/test_pysnooper.py::test_custom_repr_single', 'tests/test_pysnooper.py::test_custom_repr'],
        api=PySnooperAPI(b"TypeError: __init__() got an unexpected keyword argument 'custom_repr'"),
        unittests=PySnooper2UnittestGenerator(),
        systemtests=PySnooper2SystemtestGenerator(),
    )
    PySnooper(
        bug_id=3,
        python_version='3.8.1',
        darwin_python_version='3.8.10',  # version 3.8.1-3 do not work on mac os
        python_path='',
        buggy_commit_id='6e3d797be3fa0a746fb5b1b7c7fea78eb926c208',
        fixed_commit_id='15555ed760000b049aff8fecc79d29339c1224c3',
        test_file=[Path('tests', 'test_pysnooper.py')],
        test_cases=['tests/test_pysnooper.py::test_file_output'],
        api=PySnooperAPI(b"NameError: name 'output_path' is not defined"),
        unittests=PySnooper3UnittestGenerator(),
        systemtests=PySnooper3SystemtestGenerator(),
    )


class PySnooperAPI(API):

    def __init__(self, expected_error: bytes, default_timeout: int = 5):
        self.expected_error = expected_error
        self.translator = python.ToASTVisitor(python.GENERATIVE_GRAMMAR)
        super().__init__(default_timeout=default_timeout)

    # noinspection PyBroadException
    def run(self, system_test_path: PathLike) -> TestResult:
        try:
            with open(system_test_path, 'r') as fp:
                test = fp.read()
            test = ast.unparse(self.translator.visit_source(test))
            with tempfile.NamedTemporaryFile('w+', suffix='.py', delete=False) as fp:
                fp.write(test)
            process = subprocess.run(['python', fp.name], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                     timeout=self.default_timeout)
            os.remove(fp.name)
            if process.returncode:
                if self.expected_error in process.stderr:
                    return TestResult.FAILING
                else:
                    return TestResult.UNKNOWN
            else:
                return TestResult.PASSING
        except (subprocess.TimeoutExpired, SyntaxError):
            return TestResult.UNKNOWN
        except Exception:
            return TestResult.PASSING


class PySnooperTestGenerator(python.PythonGenerator):

    def __init__(self):
        python.PythonGenerator.__init__(self, limit_stmt_per_block=6, limit_stmt_depth=3, limit_expr_depth=2,
                                        limit_args_per_function=3)

    def _get_failing_args(self) -> List[ast.expr]:
        return []

    @staticmethod
    def _get_passing_args() -> List[ast.expr]:
        return []

    def _get_failing_keywords(self) -> List[ast.keyword]:
        return []

    @staticmethod
    def _get_passing_keywords() -> List[ast.keyword]:
        return []

    def _get_failing_prefix(self) -> List[ast.stmt]:
        return []

    def _get_passing_prefix(self) -> List[ast.stmt]:
        return []

    def _get_function_call(self, args: List[ast.expr] = None, keywords: List[ast.keyword] = None) -> ast.FunctionDef:
        function = self._generate_FunctionDef()
        function.decorator_list = [
            ast.Call(
                ast.Attribute(
                    value=ast.Name(id='pysnooper'),
                    attr='snoop',
                ),
                args=[] if args is None else args,
                keywords=[] if keywords is None else keywords,
            )
        ]
        return function

    def _get_failing_body(self, function: ast.FunctionDef, prefix: List[ast.stmt] = None) -> List[ast.stmt]:
        if prefix:
            return prefix + [function]
        return [function]

    def _get_passing_body(self, function: ast.FunctionDef, prefix: List[ast.stmt] = None) -> List[ast.stmt]:
        if prefix:
            return prefix + [function]
        return [function]


class PySnooperUnittestGenerator(UnittestGenerator, PySnooperTestGenerator):

    def __init__(self):
        UnittestGenerator.__init__(self)
        PySnooperTestGenerator.__init__(self)

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        self.reset()
        test = self.get_empty_test()
        prefix = self._get_failing_prefix()
        test.body = self._get_failing_body(self._get_function_call(self._get_failing_args(),
                                                                   self._get_failing_keywords()), prefix=prefix)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        self.reset()
        test = self.get_empty_test()
        prefix = self._get_passing_prefix()
        test.body = self._get_passing_body(self._get_function_call(self._get_passing_args(),
                                                                   self._get_passing_keywords()), prefix=prefix)
        return test, TestResult.PASSING


class PySnooperSystemtestGenerator(SystemtestGenerator, PySnooperTestGenerator):

    def __init__(self):
        self.translator = python.ToGrammarVisitor()
        UnittestGenerator.__init__(self)
        PySnooperTestGenerator.__init__(self)

    def _generate_test(self, module: ast.Module, function_name: str) -> str:
        # noinspection PyTypeChecker
        module.body = [
                          ast.Import(
                              names=[ast.alias(name='pysnooper')]
                          )
                      ] + module.body + [
                          ast.Expr(
                              value=self._generate_Call(function_name)
                          )
                      ]
        # noinspection PyTypeChecker
        return self.translator.visit(module)

    def generate_failing_test(self) -> Tuple[str, TestResult]:
        self.reset()
        test = ast.Module(
            body=[],
            type_ignores=[],
        )
        prefix = self._get_failing_prefix()
        function_call = self._get_function_call(self._get_failing_args(), self._get_failing_keywords())
        test.body = self._get_failing_body(function_call, prefix)
        return self._generate_test(test, function_call.name), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        self.reset()
        test = ast.Module(
            body=[],
            type_ignores=[],
        )
        prefix = self._get_passing_prefix()
        function_call = self._get_function_call(self._get_passing_args(), self._get_passing_keywords())
        test.body = self._get_passing_body(function_call, prefix)
        return self._generate_test(test, function_call.name), TestResult.PASSING


class PySnooper2UnittestGenerator(PySnooperUnittestGenerator):
    def _get_failing_keywords(self) -> List[ast.keyword]:
        return [
            ast.keyword(
                arg='custom_repr',
                value=ast.Tuple(
                    elts=[
                        ast.Tuple(
                            elts=[
                                ast.Name(id=self.scope.get_function()[0]),
                                ast.Name(id=self.scope.get_function()[0])
                            ]
                        )
                    ]
                )
            )
        ]

    def _get_failing_prefix(self) -> List[ast.stmt]:
        return [
            ast.Import(
                names=[ast.alias(name='pysnooper')]
            ),
            self._generate_FunctionDef(num_args=1),
            self._generate_FunctionDef(num_args=1),
        ]

    def _get_passing_prefix(self) -> List[ast.stmt]:
        return [
            ast.Import(
                names=[ast.alias(name='pysnooper')]
            )
        ]


class PySnooper2SystemtestGenerator(PySnooperSystemtestGenerator):

    def _get_failing_prefix(self) -> List[ast.stmt]:
        return [
            self._generate_FunctionDef(num_args=1),
            self._generate_FunctionDef(num_args=1),
        ]

    def _get_failing_keywords(self) -> List[ast.keyword]:
        return [
            ast.keyword(
                arg='custom_repr',
                value=ast.Tuple(
                    elts=[
                        ast.Tuple(
                            elts=[
                                ast.Name(id=self.scope.get_function()[0]),
                                ast.Name(id=self.scope.get_function()[0])
                            ]
                        )
                    ]
                )
            )
        ]


class PySnooper3UnittestGenerator(PySnooperUnittestGenerator):

    def _get_failing_args(self) -> List[ast.expr]:
        return [
            ast.Call(
                func=ast.Name(id='str'),
                args=[ast.Name(id='path')],
                keywords=[],
            )
        ]

    def _get_failing_prefix(self):
        return [
            ast.ImportFrom(
                module='python_toolbox',
                names=[ast.alias(name='temp_file_tools')],
                level=0,
            )
        ]

    def _get_failing_body(self, function: ast.FunctionDef, prefix: List[ast.stmt] = None) -> List[ast.stmt]:
        # noinspection SqlNoDataSourceInspection
        with_stmt = ast.parse("with temp_file_tools.create_temp_folder(prefix='pysnooper') as folder:\n"
                              "    path = folder / 'test.log'").body[0]
        assert isinstance(with_stmt, ast.With)
        with_stmt.body.append(ast.Import(
            names=[ast.alias(name='pysnooper')]
        ))
        with_stmt.body.append(function)
        with_stmt.body.append(ast.Expr(
            value=self._generate_Call(),
        ))
        with_stmt.body.append(ast.Expr(
            value=ast.Call(
                func=ast.Attribute(
                    value=ast.Name(id='self'),
                    attr='assertTrue'
                ),
                args=[
                    ast.Call(
                        func=ast.Attribute(
                            value=ast.Name(id='path'),
                            attr='exists'
                        ),
                        args=[],
                        keywords=[],
                    )
                ],
                keywords=[],
            ),
        ))
        return prefix + [with_stmt]

    def _get_passing_body(self, function: ast.FunctionDef, prefix: List[ast.stmt] = None) -> List[ast.stmt]:
        return [
            ast.Import(names=[ast.alias(name='pysnooper')]),
            function,
            ast.Expr(value=self._generate_Call()),
        ]


class PySnooper3SystemtestGenerator(PySnooperSystemtestGenerator):

    def _get_failing_args(self) -> List[ast.expr]:
        return [
            ast.Constant(constant='test.log')
        ]
