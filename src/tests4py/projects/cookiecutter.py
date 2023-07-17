import abc
import ast
import os
import random
import re
import shutil
import string
import subprocess
import sys
from abc import abstractmethod, ABC
from os import PathLike
from pathlib import Path
from subprocess import Popen
from typing import List, Optional, Tuple, Dict, Union, Any

from fuzzingbook.Grammars import Grammar, srange, is_valid_grammar
from isla.derivation_tree import DerivationTree
from isla.fuzzer import GrammarFuzzer

from tests4py.constants import Environment
from tests4py.grammars.utils import GrammarVisitor
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult


class CookieCutter(Project):
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
            project_name="cookiecutter",
            github_url="https://github.com/cookiecutter/cookiecutter",
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
    CookieCutter(
        bug_id=1,
        python_version="3.6.9",
        darwin_python_version="3.6.15",  # version 3.6.9 do not work on mac os
        python_path="cookiecutter/build/lib/",
        buggy_commit_id="c15633745df6abdb24e02746b82aadb20b8cdf8c",
        fixed_commit_id="7f6804c4953a18386809f11faf4d86898570debc",
        test_file=[
            Path("tests", "test_generate_context.py"),
            Path("tests", "test-generate-context", "non_ascii.json"),
        ],
        test_cases=[
            "tests/test_generate_context.py::test_generate_context_decodes_non_ascii_chars"
        ],
        test_status_buggy=TestStatus.PASSING,
    )
    CookieCutter(
        bug_id=2,
        python_version="3.6.9",
        darwin_python_version="3.6.15",  # version 3.6.9 do not work on mac os
        python_path="cookiecutter/build/lib/",
        buggy_commit_id="d7e7b28811e474e14d1bed747115e47dcdd15ba3",
        fixed_commit_id="90434ff4ea4477941444f1e83313beb414838535",
        test_file=[Path("tests", "test_hooks.py")],
        test_cases=[
            "tests/test_hooks.py::TestFindHooks::test_find_hook",
            "tests/test_hooks.py::TestExternalHooks::test_run_hook",
        ],
        api=CookieCutter2API(),
        systemtests=CookieCutter2SystemtestGenerator(),
        unittests=CookieCutter2UnittestGenerator(),
    )
    CookieCutter(
        bug_id=3,
        python_version="3.6.9",
        darwin_python_version="3.6.15",  # version 3.6.9 do not work on mac os
        python_path="cookiecutter/build/lib/",
        buggy_commit_id="5c282f020a8db7e5e7c4e7b51b010556ca31fb7f",
        fixed_commit_id="7129d474206761a6156925db78eee4b62a0e3944",
        test_file=[Path("tests", "test_read_user_choice.py")],
        test_cases=["tests/test_read_user_choice.py::test_click_invocation"],
        api=CookieCutter3API(),
        systemtests=CookieCutter3SystemtestGenerator(),
        unittests=CookieCutter3UnittestGenerator(),
    )
    CookieCutter(
        bug_id=4,
        python_version="3.6.9",
        darwin_python_version="3.6.15",  # version 3.6.9 do not work on mac os
        python_path="cookiecutter/build/lib/",
        buggy_commit_id="9568ab6ecd2d6836646006c59473c4a4ac0dee04",
        fixed_commit_id="457a1a4e862aab4102b644ff1d2b2e2b5a766b3c",
        test_file=[Path("tests", "test_hooks.py")],
        test_cases=["tests/test_hooks.py::TestExternalHooks::test_run_failing_hook"],
        api=CookieCutter4API(),
        systemtests=CookieCutter4SystemtestGenerator(),
        unittests=CookieCutter4UnittestGenerator(),
    )


class CookieCutterAPI(API, GrammarVisitor, abc.ABC):
    REPO_PATH = "tests4py_repo"

    def __init__(self, default_timeout: int = 5):
        API.__init__(self, default_timeout=default_timeout)
        GrammarVisitor.__init__(self, grammar=grammar)
        self.config = None
        self.pre_hooks = []
        self.post_hooks = []
        self.path = []
        self.pre_hook_crash = False
        self.post_hook_crash = False

    def visit_hooks(self, node: DerivationTree):
        self.pre_hooks = []
        self.post_hooks = []
        self.pre_hook_crash = False
        self.post_hook_crash = False
        for children in node.children:
            self.visit(children)

    def visit_config(self, node: DerivationTree):
        self.config = node.to_string()
        for child in node.children:
            self.visit(child)

    def visit_repo_name(self, node: DerivationTree):
        self.path = list(
            map(lambda x: x.replace('"', ""), node.children[1].to_string().split(","))
        )

    def _set_hook_crash(self, hook: str, pre: bool = True):
        c, v = hook.split(",")
        if c == "exit" and v != "0":
            if pre:
                self.pre_hook_crash = True
            else:
                self.post_hook_crash = True

    def visit_pre_hook(self, node: DerivationTree):
        hook = node.children[1].to_string()
        self._set_hook_crash(hook)
        self.pre_hooks.append(hook)

    def visit_post_hook(self, node: DerivationTree):
        hook = node.children[1].to_string()
        self._set_hook_crash(hook, pre=False)
        self.post_hooks.append(hook)

    @staticmethod
    def _write_hook(hooks_path, hooks, file):
        for i, hook in enumerate(hooks):
            c, v = hook.split(",")
            with open(os.path.join(hooks_path, f"{file}.{i}"), "w") as fp:
                if sys.platform.startswith("win"):
                    if c == "exit":
                        fp.write(f"exit \\b {v}\n")
                    else:
                        fp.write("@echo off\n")
                        fp.write(f"echo {v}\n")
                else:
                    fp.write("#!/bin/sh\n")
                    if c == "exit":
                        fp.write(f"exit {v}\n")
                    else:
                        fp.write(f'echo "{v}"\n')

    def _setup(self):
        if os.path.exists(self.REPO_PATH):
            if os.path.isdir(self.REPO_PATH):
                shutil.rmtree(self.REPO_PATH, ignore_errors=True)
            else:
                os.remove(self.REPO_PATH)

        os.makedirs(self.REPO_PATH)

        with open(os.path.join(self.REPO_PATH, "cookiecutter.json"), "w") as fp:
            fp.write(self.config)

        repo_path = os.path.join(self.REPO_PATH, "{{cookiecutter.repo_name}}")
        os.makedirs(repo_path)

        with open(os.path.join(repo_path, "README.rst"), "w") as fp:
            fp.write(
                "============\nFake Project\n============\n\n"
                "Project name: **{{ cookiecutter.project_name }}**\n\n"
                "Blah!!!!\n"
            )

        if self.pre_hooks or self.post_hooks:
            hooks_path = os.path.join(self.REPO_PATH, "hooks")
            os.makedirs(hooks_path)
            if self.pre_hooks:
                self._write_hook(hooks_path, self.pre_hooks, "pre_gen_project")
            if self.post_hooks:
                self._write_hook(hooks_path, self.post_hooks, "post_gen_project")

    @abstractmethod
    def _validate(self, process: subprocess.Popen, stdout, stderr) -> TestResult:
        pass

    @abstractmethod
    def _get_command_parameters(self) -> List[str]:
        return []

    def _communicate(self, process: Popen) -> Tuple[bytes, bytes] | Tuple[str, str]:
        return process.communicate(20 * b"\n", self.default_timeout)

    def get_test_arguments(self, system_test_path: PathLike) -> List[str]:
        with open(system_test_path, "r") as fp:
            content = fp.read()
        self.visit_source(content)
        self._setup()
        if self.path:
            for p in self.path:
                shutil.rmtree(p, ignore_errors=True)

    def oracle(self, args) -> TestResult:
        process, args = args
        stdout, stderr = args
        return self._validate(process, stdout, stderr)

    # noinspection PyBroadException
    def execute(self, system_test_path: PathLike, environ: Environment) -> Any:
        try:
            process = subprocess.Popen(
                ["cookiecutter"] + self._get_command_parameters() + [self.REPO_PATH],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env=environ,
            )
            return process, self._communicate(process)
        except subprocess.TimeoutExpired:
            return None
        except Exception:
            return None

    def clean_up(self):
        if self.path:
            for p in self.path:
                shutil.rmtree(p, ignore_errors=True)
        shutil.rmtree(self.REPO_PATH, ignore_errors=True)


class CookieCutter2API(CookieCutterAPI):
    def _get_command_parameters(self) -> List[str]:
        return ["--no-input", "-v"]

    def _validate(
        self, process: subprocess.Popen, stdout: bytes | str, stderr: bytes | str
    ) -> TestResult:
        if process.returncode != 0:
            return TestResult.UNDEFINED
        if isinstance(stdout, str):
            output = stdout
        else:
            output = stdout.decode("utf-8")
        for hook in self.pre_hooks + self.post_hooks:
            command, hook = hook.split(",")
            if command == "echo":
                hook_repr = "\n" + hook + "\n"
                if hook_repr in output:
                    output = output.replace(hook_repr, "\n", 1)
                else:
                    return TestResult.FAILING
            else:
                return TestResult.UNDEFINED
        return TestResult.PASSING


class CookieCutter3API(CookieCutterAPI):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)
        self.choice_pattern = re.compile(r"Choose from \d+(, \d)+ \(\d+(, \d)+\)")

    def _get_command_parameters(self) -> List[str]:
        return []

    def _validate(
        self, process: subprocess.Popen, stdout: bytes | str, stderr: bytes | str
    ) -> TestResult:
        if process.returncode != 0:
            return TestResult.UNDEFINED
        if isinstance(stdout, str):
            output = stdout
        else:
            output = stdout.decode("utf-8")
        if self.choice_pattern.search(output):
            return TestResult.FAILING
        return TestResult.PASSING


class CookieCutter4API(CookieCutterAPI):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def _get_command_parameters(self) -> List[str]:
        return ["-v"]

    def _validate(
        self, process: subprocess.Popen, stdout: bytes | str, stderr: bytes | str
    ) -> TestResult:
        if isinstance(stderr, str):
            output = stderr
        else:
            output = stderr.decode("utf-8")
        if self.pre_hook_crash:
            if (
                "Stopping generation because pre_gen_project hook script didn't exit sucessfully"
                in output
            ):
                return TestResult.PASSING
            else:
                return TestResult.FAILING
        if self.post_hook_crash:
            if (
                "cookiecutter.exceptions.FailedHookException: Hook script failed"
                in output
            ):
                return TestResult.PASSING
            if self.post_hook_crash:
                return TestResult.FAILING
        return TestResult.PASSING


class CookieCutterSystemtestGenerator(SystemtestGenerator, ABC):
    def __init__(self):
        SystemtestGenerator.__init__(self)
        self.pre_hook_fuzzer = GrammarFuzzer(grammar, start_symbol="<pre_hook>")
        self.post_hook_fuzzer = GrammarFuzzer(grammar, start_symbol="<post_hook>")
        self.str_fuzzer = GrammarFuzzer(grammar, start_symbol="<str>")
        self.str_with_spaces_fuzzer = GrammarFuzzer(
            grammar, start_symbol="<str_with_spaces>"
        )
        self.email_fuzzer = GrammarFuzzer(grammar, start_symbol="<email_address>")
        self.date_fuzzer = GrammarFuzzer(grammar, start_symbol="<date>")
        self.int_fuzzer = GrammarFuzzer(grammar, start_symbol="<int>")
        self.version_fuzzer = GrammarFuzzer(grammar, start_symbol="<v>")

    def _generate_default_config(
        self,
        full_name=None,
        email=None,
        github_username=None,
        project_name=None,
        repo_name=None,
        project_short_description=None,
        release_date=None,
        year=None,
        version=None,
    ) -> str:
        full_name = (
            f'"{self.str_with_spaces_fuzzer.fuzz()}"'
            if full_name is None
            else full_name
        )
        email = f'"{self.email_fuzzer.fuzz()}"' if email is None else email
        github_username = (
            f'"{self.str_fuzzer.fuzz()}"'
            if github_username is None
            else github_username
        )
        project_name = (
            f'"{self.str_with_spaces_fuzzer.fuzz()}"'
            if project_name is None
            else project_name
        )
        repo_name = f'"{self.str_fuzzer.fuzz()}"' if repo_name is None else repo_name
        project_short_description = (
            f'"{self.str_with_spaces_fuzzer.fuzz()}"'
            if project_short_description is None
            else project_short_description
        )
        release_date = (
            f'"{self.date_fuzzer.fuzz()}"' if release_date is None else release_date
        )
        year = f'"{self.int_fuzzer.fuzz()}"' if year is None else year
        version = f'"{self.version_fuzzer.fuzz()}"' if version is None else version
        return (
            f'{{"full_name":{full_name},'
            f'"email":{email},'
            f'"github_username":{github_username},'
            f'"project_name":{project_name},'
            f'"repo_name":{repo_name},'
            f'"project_short_description":{project_short_description},'
            f'"release_date":{release_date},'
            f'"year":{year},'
            f'"version":{version}}}'
        )

    def _generate_config_with_choices(self, selection=None, n=4) -> str:
        choices = [
            "full_name",
            "email",
            "github_username",
            "project_name",
            "repo_name",
            "project_short_description",
            "release_date",
            "year",
            "version",
        ]
        if selection is None:
            n = max(1, min(n, len(choices)))
            selection = random.sample(
                choices,
                random.randint(1, n),
            )
        parameters = dict()
        for s in selection:
            if s in ["full_name", "project_name", "project_short_description"]:
                fuzzer = self.str_with_spaces_fuzzer
            elif s == "email":
                fuzzer = self.email_fuzzer
            elif s == "release_date":
                fuzzer = self.date_fuzzer
            elif s == "year":
                fuzzer = self.int_fuzzer
            elif s == "version":
                fuzzer = self.version_fuzzer
            else:
                fuzzer = self.str_fuzzer
            value = ",".join(f'"{fuzzer.fuzz()}"' for _ in range(random.randint(2, 5)))
            parameters[s] = f"[{value}]"
        return self._generate_default_config(**parameters)

    def _generate_hook(
        self, pre=True, echo=True, exit_=False, exit_codes: str | list = "0"
    ) -> str:
        hook_contents = []
        if exit_:
            hook_contents.append(lambda: f"exit,{random.choice(exit_codes)}")
        if echo:
            hook_contents.append(lambda: f"echo,{self.str_with_spaces_fuzzer.fuzz()}")
        if hook_contents:
            hook_content = random.choice(hook_contents)()
        else:
            hook_content = f"echo,{self.str_with_spaces_fuzzer.fuzz()}"
        if pre:
            return f"pre:{hook_content}"
        else:
            return f"post:{hook_content}"

    def _generate_hooks(
        self,
        pre=True,
        pre_min=0,
        pre_max=1,
        post_min=0,
        post_max=1,
        echo=True,
        exit_=False,
        exit_codes: str | list = "0",
    ) -> List[str]:
        hooks = [
            self._generate_hook(pre=pre, echo=echo, exit_=exit_, exit_codes=exit_codes)
            for _ in range(0, random.randint(pre_min, pre_max))
        ] + [
            self._generate_hook(
                pre=not pre, echo=echo, exit_=exit_, exit_codes=exit_codes
            )
            for _ in range(0, random.randint(post_min, post_max))
        ]
        if hooks:
            random.shuffle(hooks)
            return hooks
        else:
            return [""]


class CookieCutter2SystemtestGenerator(CookieCutterSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        pre = random.choice([True, False])
        hooks = self._generate_hooks(pre=pre, pre_min=2, pre_max=5, post_max=5)
        return "\n".join([self._generate_default_config()] + hooks), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        hooks = self._generate_hooks()
        return "\n".join([self._generate_default_config()] + hooks), TestResult.PASSING


class CookieCutter3SystemtestGenerator(CookieCutterSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        hooks = self._generate_hooks(pre_max=2, post_max=2, exit_=True)
        return (
            "\n".join(
                [self._generate_config_with_choices(n=random.randint(1, 5))] + hooks
            ),
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        hooks = self._generate_hooks(pre_max=2, post_max=2, exit_=True)
        return "\n".join([self._generate_default_config()] + hooks), TestResult.PASSING


class CookieCutter4SystemtestGenerator(CookieCutterSystemtestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        hooks = self._generate_hooks(
            pre_max=0,
            post_min=1,
            echo=False,
            exit_=True,
            exit_codes=list(range(1, 256)),
        )
        hooks += self._generate_hooks(post_max=0, exit_=True)
        if "" in hooks:
            hooks.remove("")
        random.shuffle(hooks)
        return (
            "\n".join(
                [self._generate_config_with_choices(n=random.randint(1, 5))] + hooks
            ),
            TestResult.FAILING,
        )

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        hooks = self._generate_hooks(post_max=0, exit_=True, exit_codes="001")
        hooks += self._generate_hooks(pre_max=0, post_max=1, exit_=True)
        if "" in hooks:
            hooks.remove("")
        random.shuffle(hooks)
        return "\n".join([self._generate_default_config()] + hooks), TestResult.PASSING


class CookieCutterUnittestGenerator(UnittestGenerator, ABC):
    pass


class CookieCutter2UnittestGenerator(CookieCutterUnittestGenerator):
    def __init__(
        self, failing_probability: float = 0.2, min_hooks: int = 0, max_hooks: int = 20
    ):
        super().__init__(failing_probability=failing_probability)
        self.min_hooks = min_hooks
        self.max_hooks = max(2, min_hooks + 1, max_hooks)

    def get_utils(self) -> List[ast.stmt]:
        module = ast.parse(
            """
@staticmethod
def get_hook(prefix, n):
    if sys.platform.startswith("win"):
        hook = "@echo off\\n"
        hook += "IF NOT EXIST test4py_tmp_tests mkdir test4py_tmp_tests\\n"
    else:
        hook = "#!/bin/sh\\n"
        hook += 'if [ ! -d "test4py_tmp_tests" ]; then\\n'
        hook += '    mkdir "test4py_tmp_tests"\\n'
        hook += "fi\\n"
    file = os.path.join("test4py_tmp_tests", f"{prefix}_{n}")
    hook += f"echo {n} > {file}\\n"
    return hook

def write_hooks(self, pre_gen_hooks=0, post_gen_hooks=0):
    if os.path.exists("hooks"):
        shutil.rmtree("hooks")
    os.makedirs("hooks")
    for i in range(pre_gen_hooks):
        with open(os.path.join("hooks", f"pre_gen_project.{i}"), "w") as fp:
            fp.write(self.get_hook("pre", i))
    for i in range(post_gen_hooks):
        with open(os.path.join("hooks", f"post_gen_project.{i}"), "w") as fp:
            fp.write(self.get_hook("post", i))

def tearDown(self) -> None:
    if os.path.exists("hooks"):
        shutil.rmtree("hooks")
    if os.path.exists("test4py_tmp_tests"):
        shutil.rmtree("test4py_tmp_tests")
"""
        )
        return module.body

    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.Import(names=[ast.alias(name="os")]),
            ast.Import(names=[ast.alias(name="sys")]),
            ast.Import(names=[ast.alias(name="shutil")]),
            ast.ImportFrom(
                module="cookiecutter.hooks",
                names=[ast.alias(name="find_hook"), ast.alias(name="run_hook")],
                level=0,
            ),
        ]

    @staticmethod
    def _get_write_hooks_call(pre: int, post: int) -> ast.Call:
        return ast.Expr(
            value=ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="write_hooks"),
                args=[ast.Constant(pre), ast.Constant(post)],
                keywords=[],
            )
        )

    @staticmethod
    def _get_expected_path(n: int, pre: bool = True) -> ast.Call:
        return ast.Call(
            func=ast.Name(id="os.path.abspath"),
            args=[
                ast.Call(
                    func=ast.Name(id="os.path.join"),
                    args=[
                        ast.Constant(value="hooks"),
                        ast.Constant(
                            value=f"{'pre' if pre else 'post'}_gen_project.{n}"
                        ),
                    ],
                    keywords=[],
                )
            ],
            keywords=[],
        )

    def _get_expected_paths(self, n, is_pre: bool = True):
        return ast.List(elts=[self._get_expected_path(i, is_pre) for i in range(n)])

    @staticmethod
    def _get_expected_runs(n, is_pre: bool = True):
        return ast.List(
            elts=[
                ast.Constant(value=f"{'pre' if is_pre else 'post'}_{n}")
                for i in range(n)
            ]
        )

    def _get_hook_assign(self, n, is_pre: bool = True):
        return ast.Assign(
            targets=[ast.Name(id=f"{'pre' if is_pre else 'post'}_expected")],
            value=self._get_expected_paths(n, is_pre=is_pre),
            type_comment=None,
            lineno=0,
        )

    def _get_run_assign(self, n, is_pre: bool = True):
        return ast.Assign(
            targets=[ast.Name(id=f"{'pre' if is_pre else 'post'}_expected")],
            value=self._get_expected_paths(n, is_pre=is_pre),
            type_comment=None,
            lineno=0,
        )

    @staticmethod
    def _get_find_hooks(is_pre: bool = True):
        return ast.parse(
            f"{'pre' if is_pre else 'post'}_hooks = find_hook('{'pre' if is_pre else 'post'}_gen_project')"
        )

    @staticmethod
    def _get_run_hooks(is_pre: bool = True):
        return ast.parse(
            f"run_hook('{'pre' if is_pre else 'post'}_gen_project', os.getcwd(), {{}})"
        )

    @staticmethod
    def _get_assertion_in(is_pre: bool = True, all_in: bool = False):
        if all_in:
            assertion = "all("
        else:
            assertion = f"not {'pre' if is_pre else 'post'}_expected or any("
        assertion += f"x in {'pre' if is_pre else 'post'}_hooks for x in {'pre' if is_pre else 'post'}_expected)"
        return ast.parse(f"self.assertTrue({assertion})").body[0]

    @staticmethod
    def _get_assertion_exist(is_pre: bool = True, all_exist: bool = False):
        if all_exist:
            assertion = "all("
        else:
            assertion = f"not {'pre' if is_pre else 'post'}_expected or any("
        assertion += (
            f"os.path.exists(os.path.join('test4py_tmp_tests', x)) "
            f"for x in {'pre' if is_pre else 'post'}_expected)"
        )
        return ast.parse(f"self.assertTrue({assertion})").body[0]

    def _generate_find_test(self, pre=0, post=0, all_in: bool = False):
        test = self.get_empty_test()
        test.body = [self._get_write_hooks_call(pre, post)] + sum(
            [
                [
                    self._get_hook_assign(pre if is_pre else post, is_pre=is_pre),
                    self._get_find_hooks(is_pre=is_pre),
                    self._get_assertion_in(is_pre=is_pre, all_in=all_in),
                ]
                for is_pre in (True, False)
            ],
            start=[],
        )
        return test

    def _generate_run_test(self, pre=0, post=0, all_exist=False):
        test = self.get_empty_test()
        test.body = [self._get_write_hooks_call(pre, post)] + sum(
            [
                [
                    self._get_run_hooks(is_pre=is_pre),
                    self._get_run_assign(pre if is_pre else post, is_pre=is_pre),
                    self._get_assertion_exist(is_pre=is_pre, all_exist=all_exist),
                ]
                for is_pre in (True, False)
            ],
            start=[],
        )
        return test

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        if random.getrandbits(1):
            pre_hooks = random.randint(2, self.max_hooks)
            post_hooks = random.randint(self.min_hooks, self.max_hooks)
        else:
            pre_hooks = random.randint(self.min_hooks, self.max_hooks)
            post_hooks = random.randint(2, self.max_hooks)

        if random.getrandbits(1):
            return (
                self._generate_find_test(pre_hooks, post_hooks, True),
                TestResult.FAILING,
            )
        else:
            return (
                self._generate_run_test(pre_hooks, post_hooks, True),
                TestResult.FAILING,
            )

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pre_hooks = random.randint(self.min_hooks, self.max_hooks)
        post_hooks = random.randint(self.min_hooks, self.max_hooks)

        if random.getrandbits(1):
            return (
                self._generate_find_test(pre_hooks, post_hooks, False),
                TestResult.PASSING,
            )
        else:
            return (
                self._generate_run_test(pre_hooks, post_hooks, False),
                TestResult.PASSING,
            )


class CookieCutter3UnittestGenerator(CookieCutterUnittestGenerator):
    def __init__(
        self,
        failing_probability: float = 0.2,
        min_choices: int = 1,
        max_choices: int = 20,
    ):
        super().__init__(failing_probability=failing_probability)
        self.min_choices = min_choices
        self.max_choices = max(min_choices, max_choices)

    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.Import(names=[ast.alias(name="click")]),
            ast.ImportFrom(
                module="cookiecutter.prompt",
                names=[ast.alias(name="read_user_choice")],
                level=0,
            ),
        ]

    def get_utils(self) -> List[ast.stmt]:
        module = ast.parse(
            """
def run_test(self, options, user_choice, name, with_args=True):
    expected = (
        f"Select {name}:\\n"
        + "\\n".join(f"{i} - {c}" for i, c in enumerate(options, 1))
        + f"\\nChoose from {', '.join(str(i) for i in range(1, len(options) + 1))}"
    )
    
    with unittest.mock.patch("click.Choice") as choice:
        choice.return_value = click.Choice(options)
    
        with unittest.mock.patch("click.prompt") as prompt:
            prompt.return_value = "{}".format(user_choice)
    
            self.assertEqual(
                read_user_choice(name, options), options[user_choice - 1]
            )
    
            if with_args:
                prompt.assert_called_once_with(
                    expected,
                    type=click.Choice(options),
                    default="1",
                    show_choices=False,
                )
            else:
                prompt.assert_called_once()
            """
        )
        return module.body

    @staticmethod
    def _generate_random_string() -> str:
        return "".join(
            random.sample(
                string.ascii_letters + string.digits + "_- ", random.randint(1, 20)
            )
        )

    def _generate_test(
        self, failing: bool = True
    ) -> Tuple[ast.FunctionDef, TestResult]:
        length = random.randint(self.min_choices, self.max_choices)
        choice = random.randint(1, length)
        choices = [self._generate_random_string() for _ in range(length)]
        test = self.get_empty_test()
        test.body = ast.parse(
            f"self.run_test({choices}, {choice}, '{self._generate_random_string()}', with_args={failing})"
        ).body
        return test, failing

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._generate_test(True)

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        return self._generate_test(False)


class CookieCutter4UnittestGenerator(CookieCutterUnittestGenerator):
    def __init__(
        self,
        failing_probability: float = 0.2,
        min_hooks: int = 0,
        max_hooks: int = 20,
        max_errors: int = 5,
    ):
        super().__init__(failing_probability=failing_probability)
        self.min_hooks = min_hooks
        self.max_hooks = max(1, min_hooks + 1, max_hooks)
        self.max_errors = max(1, max_errors)

    def get_utils(self) -> List[ast.stmt]:
        return ast.parse(
            """
@staticmethod
def get_hook(n):
    if sys.platform.startswith("win"):
        hook = f"exit \\\\b {n}\\n"
    else:
        hook = "#!/bin/sh\\n"
        hook += f"exit {n}\\n"
    return hook

def write_hooks(self, exits_pre: list = None, exits_post: list = None):
    exits_pre = exits_pre or []
    exits_post = exits_post or []
    if os.path.exists("hooks"):
        shutil.rmtree("hooks")
    os.makedirs("hooks")
    for i, e in enumerate(exits_pre):
        with open(os.path.join("hooks", f"pre_gen_project.{i}"), "w") as fp:
            fp.write(self.get_hook(e))
    for i, e in enumerate(exits_post):
        with open(os.path.join("hooks", f"post_gen_project.{i}"), "w") as fp:
            fp.write(self.get_hook(e))

def tearDown(self) -> None:
    if os.path.exists("hooks"):
        shutil.rmtree("hooks")"""
        ).body

    def get_imports(self) -> List[ast.stmt]:
        return [
            ast.Import(names=[ast.alias(name="os")]),
            ast.Import(names=[ast.alias(name="sys")]),
            ast.Import(names=[ast.alias(name="shutil")]),
            ast.ImportFrom(
                module="cookiecutter",
                names=[ast.alias(name="hooks"), ast.alias(name="exceptions")],
                level=0,
            ),
        ]

    def _check_exit_code(self, exits):
        return exits and all(map(bool, exits))

    def _generate_test(
        self, pre_hooks: List[int] = None, post_hooks: List[int] = None
    ) -> ast.FunctionDef:
        pre_hooks = pre_hooks or []
        post_hooks = post_hooks or []
        test = self.get_empty_test()
        test.body = ast.parse(
            f"self.write_hooks({pre_hooks}, {post_hooks})\n"
            + (
                "self.assertRaises(exceptions.FailedHookException, hooks.run_hook, "
                "'pre_gen_project', os.getcwd(), {})\n"
                if self._check_exit_code(pre_hooks)
                else ""
            )
            + (
                "self.assertRaises(exceptions.FailedHookException, hooks.run_hook, "
                "'post_gen_project', os.getcwd(), {})\n"
                if self._check_exit_code(post_hooks)
                else ""
            )
        ).body
        return test

    def _get_exit_codes_for_hooks(self, error: bool = True):
        relevant_hooks = [0] * random.randint(
            1 if error else self.min_hooks, self.max_hooks
        )
        irrelevant_hooks = [0] * random.randint(self.min_hooks, self.max_hooks)
        if error:
            for i in range(len(relevant_hooks)):
                relevant_hooks[i] = random.randint(1, 1000)
            if irrelevant_hooks and random.getrandbits(1):
                for i in range(random.randint(1, self.max_errors)):
                    irrelevant_hooks[i] = random.randint(1, 1000)
        return relevant_hooks, irrelevant_hooks

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        if random.getrandbits(1):
            pre_hooks, post_hooks = self._get_exit_codes_for_hooks()
        else:
            post_hooks, pre_hooks = self._get_exit_codes_for_hooks()
        return self._generate_test(pre_hooks, post_hooks), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        if random.getrandbits(1):
            pre_hooks, post_hooks = self._get_exit_codes_for_hooks(error=False)
        else:
            post_hooks, pre_hooks = self._get_exit_codes_for_hooks(error=False)
        return self._generate_test(pre_hooks, post_hooks), TestResult.PASSING


grammar: Grammar = {
    "<start>": ["<config>\n<hooks>"],
    "<config>": ["{<pairs>}", "{}"],
    "<hooks>": ["", "<hook_list>"],
    "<hook_list>": ["<hook>", "<hook_list>\n<hook>"],
    "<hook>": ["<pre_hook>", "<post_hook>"],
    "<pre_hook>": ["pre:<hook_content>"],
    "<post_hook>": ["post:<hook_content>"],
    "<hook_content>": ["echo,<str_with_spaces>", "exit,<int>"],
    "<pairs>": ["<pair>", "<pairs>,<pair>"],
    "<pair>": [
        "<full_name>",
        "<email>",
        "<github_username>",
        "<project_name>",
        "<repo_name>",
        "<project_short_description>",
        "<release_date>",
        "<year>",
        "<version>",
    ],
    "<full_name>": [
        '"full_name":"<str_with_spaces>"',
        '"full_name":[<str_with_spaces_list>]',
    ],
    "<email>": ['"email":"<email_address>"', '"email":[<email_list>]'],
    "<github_username>": [
        '"github_username":"<str>"',
        '"github_username":[<str_list>]',
    ],
    "<project_name>": [
        '"project_name":"<str_with_spaces>"',
        '"project_name":[<str_with_spaces_list>]',
    ],
    "<repo_name>": ['"repo_name":"<str>"', '"repo_name":[<str_list>]'],
    "<project_short_description>": [
        '"project_short_description":"<str_with_spaces>"',
        '"project_short_description":[<str_with_spaces_list>]',
    ],
    "<release_date>": ['"release_date":"<date>"', '"release_date":[<date_list>]'],
    "<year>": ['"year":"<int>"', '"year":[<int_list>]'],
    "<version>": ['"version":"<v>"', '"version":[<version_list>]'],
    "<str_with_spaces_list>": [
        '"<str_with_spaces>"',
        '<str_with_spaces_list>,"<str_with_spaces>"',
    ],
    "<email_list>": ['"<email_address>"', '<email_list>,"<email_address>"'],
    "<str_list>": ['"<str>"', '<str_list>,"<str>"'],
    "<int_list>": ['"<int>"', '<int_list>,"<int>"'],
    "<date_list>": ['"<date>"', '<date_list>,"<date>"'],
    "<version_list>": ['"<v>"', '<version_list>,"<v>"'],
    "<chars>": ["", "<chars><char>"],
    "<char>": srange(string.ascii_letters + string.digits + "_"),
    "<chars_with_spaces>": ["", "<chars_with_spaces><char_with_spaces>"],
    "<char_with_spaces>": srange(string.ascii_letters + string.digits + "_ "),
    "<str>": ["<char><chars>"],
    "<str_with_spaces>": ["<char_with_spaces><chars_with_spaces>"],
    "<email_address>": ["<str>@<str>.<str>"],
    "<date>": ["<day>.<month>.<int>", "<int>-<month>-<day>"],
    "<month>": ["0<nonzero>", "<nonzero>", "10", "11", "12"],
    "<day>": [
        "0<nonzero>",
        "<nonzero>",
        "10",
        "1<nonzero>",
        "20",
        "2<nonzero>",
        "30",
        "31",
    ],
    "<v>": ["<digit><digits>", "<v>.<digit><digits>"],
    "<int>": ["<nonzero><digits>", "0"],
    "<digits>": ["", "<digits><digit>"],
    "<nonzero>": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "<digit>": srange(string.digits),
}

assert is_valid_grammar(grammar)
