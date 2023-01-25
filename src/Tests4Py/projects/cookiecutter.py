import os
import shutil
import string
import subprocess
from abc import abstractmethod
from os import PathLike
from pathlib import Path
from typing import List, Optional

from fuzzingbook.Grammars import Grammar, srange, is_valid_grammar
from isla.derivation_tree import DerivationTree

from Tests4Py.framework.constants import Environment
from Tests4Py.grammars.utils import GrammarVisitor
from Tests4Py.projects import Project, Status, TestingFramework, TestStatus
from Tests4Py.tests.generator import UnittestGenerator, SystemtestGenerator
from Tests4Py.tests.utils import API, TestResult


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
            test_status_fixed=test_status_fixed,
            test_status_buggy=test_status_buggy,
            unittests=unittests,
            systemtests=systemtests,
            api=api,
            grammar=None,
        )  # TODO adjust parameters


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
        test_status_buggy=TestStatus.PASSING,  # It was just a missing test file
    )
    CookieCutter(
        bug_id=2,
        python_version="3.6.9",
        darwin_python_version="3.6.15",  # version 3.8.1-3 do not work on mac os
        python_path="cookiecutter/build/lib/",
        buggy_commit_id="d7e7b28811e474e14d1bed747115e47dcdd15ba3",
        fixed_commit_id="90434ff4ea4477941444f1e83313beb414838535",
        test_file=[Path("tests", "test_hooks.py")],
        test_cases=[
            "tests/test_hooks.py::TestFindHooks::test_find_hook",
            "tests/test_hooks.py::TestExternalHooks::test_run_hook",
        ],
        api=CookieCutter2API(),
        systemtests=None,  # Bug does not propagate
    )
    CookieCutter(
        bug_id=3,
        python_version="3.6.9",
        darwin_python_version="3.6.15",  # version 3.8.1-3 do not work on mac os
        python_path="cookiecutter/build/lib/",
        buggy_commit_id="5c282f020a8db7e5e7c4e7b51b010556ca31fb7f",
        fixed_commit_id="7129d474206761a6156925db78eee4b62a0e3944",
        test_file=[Path("tests", "test_read_user_choice.py")],
        test_cases=["tests/test_read_user_choice.py::test_click_invocation"],
        systemtests=None,  # Bug does not propagate
    )
    CookieCutter(
        bug_id=4,
        python_version="3.6.9",
        darwin_python_version="3.6.15",  # version 3.8.1-3 do not work on mac os
        python_path="cookiecutter/build/lib/",
        buggy_commit_id="9568ab6ecd2d6836646006c59473c4a4ac0dee04",
        fixed_commit_id="457a1a4e862aab4102b644ff1d2b2e2b5a766b3c",
        test_file=[Path("tests", "test_hooks.py")],
        test_cases=["tests/test_hooks.py::TestExternalHooks::test_run_failing_hook"],
        systemtests=None,  # Bug does not propagate
    )
    # TODO implement the 4 bugs of cookiecutter


class CookieCutterAPI(API, GrammarVisitor):
    REPO_PATH = "tests4py_repo"

    def __init__(self, default_timeout: int = 5):
        API.__init__(self, default_timeout=default_timeout)
        GrammarVisitor.__init__(self, grammar=grammar)
        self.config = None
        self.pre_hooks = []
        self.post_hooks = []

    def visit_hooks(self, node: DerivationTree):
        self.pre_hooks = []
        self.post_hooks = []
        for children in node.children:
            self.visit(children)

    def visit_config(self, node: DerivationTree):
        self.config = node.value

    def visit_pre_hook(self, node: DerivationTree):
        self.pre_hooks.append(node.children[1])

    def visit_post_hook(self, node: DerivationTree):
        self.post_hooks.append(node.children[1])

    def _setup(self):
        if os.path.exists(self.REPO_PATH):
            if os.path.isdir(self.REPO_PATH):
                shutil.rmtree(self.REPO_PATH, ignore_errors=True)
            else:
                os.remove(self.REPO_PATH)

        os.makedirs(self.REPO_PATH)

        with open("cookiecutter.json", "w") as fp:
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
                for i, pre_hook in enumerate(self.pre_hooks):
                    with open(
                        os.path.join(hooks_path, f"pre_gen_project.{i}.py"), "w"
                    ) as fp:
                        fp.write(f'print("{pre_hook}")')
            if self.post_hooks:
                for i, post_hook in enumerate(self.post_hooks):
                    with open(
                        os.path.join(hooks_path, f"post_gen_project.{i}.py"), "w"
                    ) as fp:
                        fp.write(f'print("{post_hook}")')

    @abstractmethod
    def _validate(self, process: subprocess.CompletedProcess) -> TestResult:
        pass

    # noinspection PyBroadException
    def run(self, system_test_path: PathLike, environ: Environment) -> TestResult:
        try:
            with open(system_test_path, "r") as fp:
                content = fp.read()
            self.visit_source(content)
            self._setup()
            process = subprocess.run(
                ["cookiecutter", self.REPO_PATH],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=self.default_timeout,
                env=environ,
            )
            return self._validate(process)
        except subprocess.TimeoutExpired:
            return TestResult.UNKNOWN
        except Exception:
            return TestResult.UNKNOWN
        finally:
            shutil.rmtree(self.REPO_PATH, ignore_errors=True)


class CookieCutter2API(CookieCutterAPI):
    def _validate(self, process: subprocess.CompletedProcess) -> TestResult:
        output: str = process.stdout.decode("utf-8")
        for hook in self.pre_hooks + self.post_hooks:
            if hook in output:
                output = output.replace(hook, "", 1)
            else:
                return TestResult.FAILING
        return TestResult.PASSING


grammar: Grammar = {
    "<start>": ["<config>\n<hooks>"],
    "<config>": ["{<pairs>}", "{}"],
    "<hooks>": ["", "<hook_list>"],
    "<hook_list>": ["<hook>", "<hook_list>\n<hook>"],
    "<hook>": ["<pre_hook>", "<post_hook>"],
    "<pre_hook>": ["pre:<str_with_space>"],
    "<post_hook>": ["post:<str_with_space>"],
    "<pairs>": ["<pair>", "<pairs>,<pair>"],
    "<pair>": [
        "<full_name>",
        "<email>",
        "<github_username>",
        "<project_name>",
        "<repo_name>",
        "<project_short_description>",
        "<release_date>",
        "<version>",
    ],
    "<full_name>": [
        '"full_name":"str_with_space"',
        '"full_name":[<str_with_space_list>]',
    ],
    "<email>": ['"email":"<email>"', '"email":[<email_list>]'],
    "<github_username>": [
        '"github_username":"<str>"',
        '"github_username":[<str_list>]',
    ],
    "<project_name>": [
        '"project_name":"<str_with_space>"',
        '"project_name":[<str_with_space_list>]',
    ],
    "<repo_name>": ['"repo_name":"<str>"', '"repo_name":[<str_list>]'],
    "<project_short_description>": [
        '"project_name":"<str_with_space>"',
        '"project_name":[<str_with_space_list>]',
    ],
    "<release_date>": ['"release_date":"<date>"', '"release_date":[<date_list>]'],
    "<year>": ['"year":"<int>"', '"year":[<int_list>]'],
    "<version>": ['"version":"<v>"', '"version":[<version_list>]'],
    "<str_with_space_list>": [
        "<str_with_space>",
        "<str_with_space_list>,<str_with_space>",
    ],
    "<email_list>": ["<email_address>", "<email_list>,<email_address>"],
    "<str_list>": ["<str>", "<str_list>,<str>"],
    "<int_list>": ["<int>", "<int_list>,<int>"],
    "<date_list>": ["<date>", "<date_list>,<date>"],
    "<version_list>": ["<v>", "<version_list>,<v>"],
    "<chars>": ["", "<chars><char>"],
    "<char>": srange(string.ascii_letters + string.digits + "_"),
    "<chars_with_space>": ["", "<chars_with_space><char_with_space>"],
    "<char_with_space>": srange(string.ascii_letters + string.digits + "_ "),
    "<str>": ["<char><chars>"],
    "<str_with_space>": ["<char_with_space><chars_with_space>"],
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
