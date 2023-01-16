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
        test_file=[Path('tests', 'test_pysnooper.py')],
        test_cases=['tests/test_pysnooper.py::test_custom_repr_single'],
        test_status_fixed=TestStatus.ERROR,
        test_status_buggy=TestStatus.ERROR,
    )
    PySnooper(
        bug_id=3,
        python_version='3.8.1',
        darwin_python_version='3.8.4',  # version 3.8.1-3 do not work on mac os
        python_path='',
        buggy_commit_id='6e3d797be3fa0a746fb5b1b7c7fea78eb926c208',
        fixed_commit_id='15555ed760000b049aff8fecc79d29339c1224c3',
        test_file=[Path('tests', 'test_pysnooper.py')],
        test_cases=['tests/test_pysnooper.py::test_file_output'],
        api=PySnooperAPI(),
        unittests=PySnooperUnittestGenerator(),
        systemtests=PySnooperSystemtestGenerator(),
    )


class PySnooperAPI(API):

    def __init__(self, default_timeout: int = 5):
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
                if b"NameError: name 'output_path' is not defined" in process.stderr:
                    return TestResult.FAILING
                else:
                    return TestResult.UNKNOWN
            else:
                return TestResult.PASSING
        except (subprocess.TimeoutExpired, SyntaxError):
            return TestResult.UNKNOWN
        except Exception:
            return TestResult.PASSING


class PySnooperUnittestGenerator(UnittestGenerator, python.PythonGenerator):

    def __init__(self):
        super().__init__()
        python.PythonGenerator.__init__(self, limit_stmt_per_block=6, limit_stmt_depth=3, limit_expr_depth=2,
                                        limit_args_per_function=3)

    # noinspection SqlNoDataSourceInspection
    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        self.reset()
        with_stmt = ast.parse("with temp_file_tools.create_temp_folder(prefix='pysnooper') as folder:\n"
                              "    path = folder / 'test.log'").body[0]
        assert isinstance(with_stmt, ast.With)
        function = self._generate_FunctionDef()
        function.decorator_list = [
            ast.Call(
                ast.Attribute(
                    value=ast.Name(id='pysnooper'),
                    attr='snoop',
                ),
                args=[
                    ast.Call(
                        func=ast.Name(id='str'),
                        args=[ast.Name(id='path')],
                        keywords=[],
                    )
                ],
                keywords=[],
            )
        ]
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
        test = self.get_empty_test()
        test.body.append(ast.ImportFrom(
            module='python_toolbox',
            names=[ast.alias(name='temp_file_tools')],
            level=0,
        ))
        test.body.append(with_stmt)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        self.reset()
        test = self.get_empty_test()
        function = self._generate_FunctionDef()
        function.decorator_list = [
            ast.Call(
                ast.Attribute(
                    value=ast.Name(id='pysnooper'),
                    attr='snoop',
                ),
                args=[],
                keywords=[]
            )
        ]
        test.body.append(ast.Import(
            names=[ast.alias(name='pysnooper')]
        ))
        test.body.append(function)
        test.body.append(ast.Expr(
            value=self._generate_Call(),
        ))
        return test, TestResult.PASSING


class PySnooperSystemtestGenerator(SystemtestGenerator, python.PythonGenerator):

    def __init__(self):
        self.translator = python.ToGrammarVisitor()
        super().__init__()
        python.PythonGenerator.__init__(self, limit_stmt_per_block=6, limit_stmt_depth=3, limit_expr_depth=2,
                                        limit_args_per_function=3)

    def _generate_test(self, function: ast.FunctionDef) -> str:
        # noinspection PyTypeChecker
        return self.translator.visit(ast.Module(
            body=[
                ast.Import(
                    names=[ast.alias(name='pysnooper')]
                ),
                function,
                ast.Expr(
                    value=self._generate_Call(),
                )
            ],
            type_ignores=[],
        ))

    def generate_failing_test(self) -> Tuple[str, TestResult]:
        self.reset()
        function = self._generate_FunctionDef()
        function.decorator_list = [
            ast.Call(
                ast.Attribute(
                    value=ast.Name(id='pysnooper'),
                    attr='snoop',
                ),
                args=[
                    ast.Constant('test.log'),
                ],
                keywords=[],
            )
        ]
        return self._generate_test(function), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        self.reset()
        function = self._generate_FunctionDef()
        function.decorator_list = [
            ast.Call(
                ast.Attribute(
                    value=ast.Name(id='pysnooper'),
                    attr='snoop',
                ),
                args=[],
                keywords=[],
            )
        ]
        return self._generate_test(function), TestResult.PASSING
