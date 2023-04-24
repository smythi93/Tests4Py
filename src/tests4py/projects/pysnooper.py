import ast
import os
import random
import string
from _ast import Call
from abc import abstractmethod
from pathlib import Path
from typing import List, Optional, Tuple

from fuzzingbook.Grammars import Grammar, srange, is_valid_grammar
from isla.fuzzer import GrammarFuzzer

from tests4py.grammars import python
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult, ExpectErrAPI


class PySnooper(Project):
    def __init__(
        self,
        bug_id: int,
        python_version: str,
        python_path: str,
        buggy_commit_id: str,
        fixed_commit_id: str,
        test_file: List[Path],
        test_cases: List[str],
        darwin_python_version: Optional[str] = None,
        test_status_fixed: TestStatus = TestStatus.PASSING,
        test_status_buggy: TestStatus = TestStatus.FAILING,
        unittests: Optional[UnittestGenerator] = None,
        systemtests: Optional[SystemtestGenerator] = None,
        api: Optional[API] = None,
    ):
        super().__init__(
            bug_id=bug_id,
            project_name="pysnooper",
            github_url="https://github.com/cool-RR/PySnooper",
            status=Status.OK,
            cause="N.A.",
            python_version=python_version,
            python_path=python_path,
            buggy_commit_id=buggy_commit_id,
            fixed_commit_id=fixed_commit_id,
            testing_framework=TestingFramework.PYTEST,
            test_file=test_file,
            test_cases=test_cases,
            darwin_python_version=darwin_python_version,
            python_fallback_version=darwin_python_version,
            test_status_fixed=test_status_fixed,
            test_status_buggy=test_status_buggy,
            unittests=unittests,
            systemtests=systemtests,
            api=api,
            grammar=grammar,
        )


def register():
    PySnooper(
        bug_id=1,
        python_version="3.8.1",
        darwin_python_version="3.8.4",  # version 3.8.1-3 do not work on mac os
        python_path="",
        buggy_commit_id="e21a31162f4c54be693d8ca8260e42393b39abd3",
        fixed_commit_id="56f22f8ffe1c6b2be4d2cf3ad1987fdb66113da2",
        test_file=[Path("tests", "test_chinese.py")],
        test_cases=["tests/test_chinese.py::test_chinese"],
        test_status_buggy=TestStatus.PASSING,
    )
    PySnooper(
        bug_id=2,
        python_version="3.8.1",
        darwin_python_version="3.8.4",  # version 3.8.1-3 do not work on mac os
        python_path="",
        buggy_commit_id="e21a31162f4c54be693d8ca8260e42393b39abd3",
        fixed_commit_id="814abc34a098c1b98cb327105ac396f985d2413e",
        test_file=[
            Path("tests", "test_pysnooper.py"),
            Path("tests", "mini_toolbox"),
            Path("pysnooper", "pycompat.py"),
            Path("pysnooper", "utils.py"),
        ],
        test_cases=[
            "tests/test_pysnooper.py::test_custom_repr_single",
            "tests/test_pysnooper.py::test_custom_repr",
        ],
        api=PySnooperAPI(
            b"TypeError: __init__() got an unexpected keyword argument 'custom_repr'"
        ),
        unittests=PySnooper2UnittestGenerator(),
        systemtests=PySnooper2SystemtestGenerator(),
    )
    PySnooper(
        bug_id=3,
        python_version="3.8.1",
        darwin_python_version="3.8.4",  # version 3.8.1-3 do not work on mac os
        python_path="",
        buggy_commit_id="6e3d797be3fa0a746fb5b1b7c7fea78eb926c208",
        fixed_commit_id="15555ed760000b049aff8fecc79d29339c1224c3",
        test_file=[Path("tests", "test_pysnooper.py")],
        test_cases=["tests/test_pysnooper.py::test_file_output"],
        api=PySnooperAPI(b"NameError: name 'output_path' is not defined"),
        unittests=PySnooper3UnittestGenerator(),
        systemtests=PySnooper3SystemtestGenerator(),
    )


class PySnooperAPI(ExpectErrAPI):
    pass


class PySnooperUnittestGenerator(python.PythonGenerator, UnittestGenerator):
    def __init__(self):
        python.PythonGenerator.__init__(
            self,
            limit_stmt_per_block=6,
            limit_stmt_depth=3,
            limit_expr_depth=2,
            limit_args_per_function=3,
        )
        UnittestGenerator.__init__(self)

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

    def _get_function_call(
        self, args: List[ast.expr] = None, keywords: List[ast.keyword] = None
    ) -> ast.FunctionDef:
        function = self._generate_FunctionDef()
        function.decorator_list = [
            ast.Call(
                ast.Attribute(
                    value=ast.Name(id="pysnooper"),
                    attr="snoop",
                ),
                args=[] if args is None else args,
                keywords=[] if keywords is None else keywords,
            )
        ]
        return function

    def _get_failing_body(
        self, function: ast.FunctionDef, prefix: List[ast.stmt] = None
    ) -> List[ast.stmt]:
        if prefix:
            return prefix + [function]
        return [function]

    def _get_passing_body(
        self, function: ast.FunctionDef, prefix: List[ast.stmt] = None
    ) -> List[ast.stmt]:
        if prefix:
            return prefix + [function]
        return [function]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        self.reset()
        test = self.get_empty_test()
        prefix = self._get_failing_prefix()
        test.body = self._get_failing_body(
            self._get_function_call(
                self._get_failing_args(), self._get_failing_keywords()
            ),
            prefix=prefix,
        )
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        self.reset()
        test = self.get_empty_test()
        prefix = self._get_passing_prefix()
        test.body = self._get_passing_body(
            self._get_function_call(
                self._get_passing_args(), self._get_passing_keywords()
            ),
            prefix=prefix,
        )
        return test, TestResult.PASSING


class PySnooperSystemtestGenerator(SystemtestGenerator):
    def __init__(self):
        super().__init__()
        self.variables_fuzzer = GrammarFuzzer(grammar, start_symbol="<variable_list>")
        self.predicate_fuzzer = GrammarFuzzer(grammar, start_symbol="<predicate_list>")
        self.str_fuzzer = GrammarFuzzer(grammar, start_symbol="<str>")

    def _generate_parameters(
        self, required: List[str], parameters: List[str], output_prob=0.5
    ):
        selection = required + random.sample(
            parameters, random.randint(0, len(parameters))
        )
        params = list()
        if "output" in selection:
            if random.random() < output_prob:
                params.append("-o")
            else:
                params.append("-otest.log")
        if "variables" in selection:
            params.append("-v" + self.variables_fuzzer.fuzz())
        if "depth" in selection:
            params.append(f"-d{random.randint(1, 5)}")
        if "prefix" in selection:
            params.append("-p" + self.str_fuzzer.fuzz())
        if "watch" in selection:
            params.append("-w" + self.variables_fuzzer.fuzz())
        if "custom_repr" in selection:
            params.append("-c" + self.predicate_fuzzer.fuzz())
        if "overwrite" in selection and "output" in selection and "-o" not in params:
            params.append("-O")
        if "thread_info" in selection:
            params.append("-T")
        return params

    @abstractmethod
    def _get_failing_params(self):
        return []

    @abstractmethod
    def _get_passing_params(self):
        return []

    def generate_failing_test(self) -> Tuple[str, TestResult]:
        params = self._get_failing_params()
        random.shuffle(params)
        return "\n".join(params), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        params = self._get_passing_params()
        random.shuffle(params)
        return "\n".join(params), TestResult.PASSING


class PySnooper2UnittestGenerator(PySnooperUnittestGenerator):
    def _get_failing_keywords(self) -> List[ast.keyword]:
        return [
            ast.keyword(
                arg="custom_repr",
                value=ast.Tuple(
                    elts=[
                        ast.Tuple(
                            elts=[
                                ast.Name(id=self.scope.get_function()[0]),
                                ast.Name(id=self.scope.get_function()[0]),
                            ]
                        )
                    ]
                ),
            )
        ]

    def _get_failing_prefix(self) -> List[ast.stmt]:
        return [
            ast.Import(names=[ast.alias(name="pysnooper")]),
            self._generate_FunctionDef(num_args=1),
            self._generate_FunctionDef(num_args=1),
        ]

    def _get_passing_prefix(self) -> List[ast.stmt]:
        # noinspection PyTypeChecker
        return [ast.Import(names=[ast.alias(name="pysnooper")])]


class PySnooper2SystemtestGenerator(PySnooperSystemtestGenerator):
    def _get_failing_params(self):
        return self._generate_parameters(
            ["custom_repr"],
            ["output", "depth", "watch", "prefix", "overwrite", "thread_info"],
        )

    def _get_passing_params(self):
        return self._generate_parameters(
            [], ["output", "depth", "watch", "prefix", "overwrite", "thread_info"]
        )


class PySnooper3UnittestGenerator(PySnooperUnittestGenerator):
    def _get_failing_args(self) -> list[Call]:
        return [
            ast.Call(
                func=ast.Name(id="str"),
                args=[ast.Name(id="path")],
                keywords=[],
            )
        ]

    def _get_failing_prefix(self):
        return [
            ast.ImportFrom(
                module="python_toolbox",
                names=[ast.alias(name="temp_file_tools")],
                level=0,
            )
        ]

    def _get_failing_body(
        self, function: ast.FunctionDef, prefix: List[ast.stmt] = None
    ) -> List[ast.stmt]:
        # noinspection SqlNoDataSourceInspection
        with_stmt = ast.parse(
            "with temp_file_tools.create_temp_folder(prefix='pysnooper') as folder:\n"
            "    path = folder / 'test.log'"
        ).body[0]
        assert isinstance(with_stmt, ast.With)
        with_stmt.body.append(ast.Import(names=[ast.alias(name="pysnooper")]))
        # noinspection PyTypeChecker
        with_stmt.body.append(function)
        with_stmt.body.append(
            ast.Expr(
                value=self._generate_Call(),
            )
        )
        with_stmt.body.append(
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertTrue"),
                    args=[
                        ast.Call(
                            func=ast.Attribute(
                                value=ast.Name(id="path"), attr="exists"
                            ),
                            args=[],
                            keywords=[],
                        )
                    ],
                    keywords=[],
                ),
            )
        )
        # noinspection PyTypeChecker
        return prefix + [with_stmt]

    def _get_passing_body(
        self, function: ast.FunctionDef, prefix: List[ast.stmt] = None
    ) -> List[ast.stmt]:
        return [
            ast.Import(names=[ast.alias(name="pysnooper")]),
            function,
            ast.Expr(value=self._generate_Call()),
        ]


class PySnooper3SystemtestGenerator(PySnooperSystemtestGenerator):
    def _get_failing_params(self):
        return self._generate_parameters(
            ["output"], ["depth", "variables", "prefix"], output_prob=-1
        )

    def _get_passing_params(self):
        return self._generate_parameters(
            [], ["output", "depth", "variables", "prefix"], output_prob=2
        )


grammar: Grammar = {
    "<start>": ["<options>"],
    "<options>": ["", "<option_list>"],
    "<option_list>": ["<option>", "<option_list>\n<option>"],
    "<option>": [
        "<output>",
        "<variables>",
        "<depth>",
        "<prefix>",
        "<watch>",
        "<custom_repr>",
        "<overwrite>",
        "<thread_info>",
    ],
    "<output>": ["-o", "-o<path>"],
    "<variables>": ["-v<variable_list>"],
    "<depth>": ["-d<int>"],
    "<prefix>": ["-p<str>"],
    "<watch>": ["-w<variable_list>"],
    "<custom_repr>": ["-c<predicate_list>"],
    "<overwrite>": ["-O"],
    "<thread_info>": ["-T"],
    "<path>": ["<location>", "<location>.<str>"],
    "<location>": ["<str>", os.path.join("<path>", "<str>")],
    "<variable_list>": ["<variable>", "<variable_list>,<variable>"],
    "<variable>": ["<name>", "<variable>.<name>"],
    "<name>": ["<letter><chars>"],
    "<chars>": ["", "<chars><char>"],
    "<letter>": srange(string.ascii_letters),
    "<digit>": srange(string.digits),
    "<char>": ["<letter>", "<digit>", "_"],
    "<int>": ["<nonzero><digits>", "0"],
    "<digits>": ["", "<digits><digit>"],
    "<nonzero>": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "<str>": ["<char><chars>"],
    "<predicate_list>": ["<predicate>", "<predicate_list>,<predicate>"],
    "<predicate>": ["<p_function>=<t_function>"],
    "<p_function>": ["int", "str", "float", "bool"],
    "<t_function>": ["repr", "str", "int"],
}

assert is_valid_grammar(grammar)
