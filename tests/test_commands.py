import json
import os
from typing import List

from tests4py.cli import framework
from tests4py.constants import (
    DEFAULT_WORK_DIR,
    INFO_FILE,
    REQUIREMENTS_FILE,
    DEFAULT_UNITTESTS_DIVERSITY_PATH,
    DEFAULT_SYSTEMTESTS_DIVERSITY_PATH,
    DEFAULT_SUB_PATH_UNITTESTS,
    DEFAULT_SUB_PATH_SYSTEMTESTS,
    GLOBAL_PROJECTS,
    GLOBAL_GIT,
)
from tests4py.grammars.fuzzer import is_valid_grammar
from tests4py.projects import load_bug_info
from tests4py.tests.utils import TestResult
from utils import BaseTest


class CommandTests(BaseTest):
    def _checkout(
        self,
        project_name: str,
        bug_id: int,
        has_tests: bool = False,
        fixed: bool = False,
    ):
        identifier = self.get_identifier(project_name, bug_id)
        report = framework.default.tests4py_checkout(project_name, bug_id, fixed=fixed)
        if report.raised:
            raise report.raised
        work_dir = DEFAULT_WORK_DIR / identifier
        self.assertTrue(work_dir.exists())
        self.assertTrue((work_dir / INFO_FILE).exists())
        self.assertTrue((work_dir / REQUIREMENTS_FILE).exists())
        if has_tests:
            self.assertTrue((work_dir / DEFAULT_UNITTESTS_DIVERSITY_PATH).exists())
            self.assertTrue((work_dir / DEFAULT_SYSTEMTESTS_DIVERSITY_PATH).exists())
            self.assertEqual(
                20,
                len(
                    os.listdir(
                        DEFAULT_WORK_DIR
                        / identifier
                        / DEFAULT_SYSTEMTESTS_DIVERSITY_PATH
                    )
                ),
            )

    def _compile(self, project_name: str, bug_id: int):
        identifier = self.get_identifier(project_name, bug_id)
        work_dir = DEFAULT_WORK_DIR / identifier
        project = load_bug_info(work_dir / INFO_FILE)
        self.assertFalse(project.compiled)
        report = framework.default.tests4py_build(work_dir)
        if report.raised:
            raise report.raised
        project = load_bug_info(work_dir / INFO_FILE)
        self.assertTrue(project.compiled)

    def _test(self, project_name: str, bug_id: int, fixed: bool = False):
        identifier = self.get_identifier(project_name, bug_id)
        work_dir = DEFAULT_WORK_DIR / identifier
        report = framework.default.tests4py_test(work_dir)
        if report.raised:
            raise report.raised
        self.assertEqual(1, report.total)
        if fixed:
            self.assertEqual(0, report.failing)
            self.assertEqual(1, report.passing)
        else:
            self.assertEqual(1, report.failing)
            self.assertEqual(0, report.passing)

    def _unittest(self, project_name: str, bug_id: int, fixed: bool = False):
        identifier = self.get_identifier(project_name, bug_id)
        work_dir = DEFAULT_WORK_DIR / identifier
        report = framework.unittest.tests4py_test(work_dir, diversity=True)
        if report.raised:
            raise report.raised
        self.assertEqual(20, report.total)
        if fixed:
            self.assertEqual(0, report.failing)
            self.assertEqual(20, report.passing)
        else:
            self.assertEqual(10, report.failing)
            self.assertEqual(10, report.passing)

    def _systemtest(self, project_name: str, bug_id: int, fixed: bool = False):
        identifier = self.get_identifier(project_name, bug_id)
        work_dir = DEFAULT_WORK_DIR / identifier
        report = framework.systemtest.tests4py_test(work_dir, diversity=True)
        if report.raised:
            raise report.raised
        if fixed:
            self.assertEqual(0, report.failing)
            self.assertEqual(20, report.passing)
        else:
            self.assertEqual(10, report.failing)
            self.assertEqual(10, report.passing)

    def _unittest_generate(self, project_name: str, bug_id: int, fixed: bool = False):
        identifier = self.get_identifier(project_name, bug_id)
        work_dir = DEFAULT_WORK_DIR / identifier
        report = framework.unittest.tests4py_generate(work_dir, n=6, p=0.5)
        if report.raised:
            raise report.raised
        self.assertTrue((work_dir / DEFAULT_SUB_PATH_UNITTESTS).exists())
        self.assertEqual(6, report.total)
        self.assertEqual(3, report.failing)
        self.assertEqual(3, report.passing)
        report = framework.unittest.tests4py_test(
            work_dir,
            path_or_str=work_dir / DEFAULT_SUB_PATH_UNITTESTS,
            diversity=False,
        )
        if report.raised:
            raise report.raised
        self.assertEqual(6, report.total)
        if fixed:
            self.assertEqual(0, report.failing)
            self.assertEqual(6, report.passing)
        else:
            self.assertEqual(3, report.failing)
            self.assertEqual(3, report.passing)

    def _systemtest_generate(self, project_name: str, bug_id: int, fixed: bool = False):
        identifier = self.get_identifier(project_name, bug_id)
        work_dir = DEFAULT_WORK_DIR / identifier
        report = framework.systemtest.tests4py_generate(work_dir, n=6, p=0.5)
        if report.raised:
            raise report.raised
        self.assertTrue((work_dir / DEFAULT_SUB_PATH_SYSTEMTESTS).exists())
        self.assertEqual(6, report.total)
        self.assertEqual(3, report.failing)
        self.assertEqual(3, report.passing)
        report = framework.systemtest.tests4py_test(
            work_dir,
            path_or_str=work_dir / DEFAULT_SUB_PATH_SYSTEMTESTS,
            diversity=False,
        )
        if report.raised:
            raise report.raised
        self.assertEqual(6, report.total)
        if fixed:
            self.assertEqual(0, report.failing)
            self.assertEqual(6, report.passing)
        else:
            self.assertEqual(3, report.failing)
            self.assertEqual(3, report.passing)

    def test_checkout_pysnooper_2(self):
        self._checkout("pysnooper", 2, has_tests=True)

    def test_compile_pysnooper_1(self):
        project = "pysnooper", 1
        self._checkout(*project)
        self._compile(*project)

    def _test_pysnooper_3(self, fixed: bool = False):
        project = "pysnooper", 3
        self._checkout(*project, has_tests=True, fixed=fixed)
        self._compile(*project)
        self._test(*project, fixed=fixed)
        self._unittest(*project, fixed=fixed)
        self._systemtest(*project, fixed=fixed)
        self._unittest_generate(*project, fixed=fixed)
        self._systemtest_generate(*project, fixed=fixed)

    def test_pysnooper_3(self):
        self._test_pysnooper_3()

    def test_pysnooper_3_fixed(self):
        self._test_pysnooper_3(fixed=True)

    def _direct_systemtest(
        self, project_name: str, bug_id: int, test: str, fixed: bool = False
    ):
        identifier = self.get_identifier(project_name, bug_id)
        work_dir = DEFAULT_WORK_DIR / identifier
        report = framework.systemtest.tests4py_test(work_dir, path_or_str=test)
        if report.raised:
            raise report.raised
        self.assertEqual(1, report.total)
        if fixed:
            self.assertEqual(0, report.failing)
            self.assertEqual(1, report.passing)
        else:
            self.assertEqual(1, report.failing)
            self.assertEqual(0, report.passing)

    def _run(
        self, project_name: str, bug_id: int, test: List[str], fixed: bool = False
    ):
        identifier = self.get_identifier(project_name, bug_id)
        work_dir = DEFAULT_WORK_DIR / identifier
        report = framework.systemtest.tests4py_run(work_dir, inputs=test)
        if report.raised:
            raise report.raised
        self.assertEqual(str(test), report.input)
        report = framework.systemtest.tests4py_run(
            work_dir, inputs=test, invoke_oracle=True
        )
        if report.raised:
            raise report.raised
        if fixed:
            self.assertEqual(TestResult.PASSING, report.test_result)
        else:
            self.assertEqual(TestResult.FAILING, report.test_result)

    def _test_middle_1(self, fixed: bool = False):
        project = "middle", 1
        self._checkout(*project, has_tests=True, fixed=fixed)
        self._compile(*project)
        self._test(*project, fixed=fixed)
        self._unittest(*project, fixed=fixed)
        self._direct_systemtest(*project, test="2 1 3", fixed=fixed)
        self._run(*project, test=["2", "1", "3"], fixed=fixed)

    def test_buggy_middle_1_direct(self):
        self._test_middle_1()

    def test_fixed_middle_1_direct(self):
        self._test_middle_1(fixed=True)

    def test_grammar_python(self):
        file = "grammar.py"
        framework.grammar.tests4py_grammar(
            "pysnooper", 2, grammar_format="python", output=file
        )
        with open(file, "r") as fp:
            exec(fp.read())
        self.assertTrue(is_valid_grammar(locals()["grammar"]))
        if os.path.exists(file):
            os.remove(file)

    def test_grammar_json(self):
        file = "grammar.json"
        framework.grammar.tests4py_grammar(
            "pysnooper", 2, grammar_format="json", output=file
        )
        with open(file, "r") as fp:
            grammar = json.load(fp)
        self.assertTrue(is_valid_grammar(grammar))
        if os.path.exists(file):
            os.remove(file)

    def test_grammar_antlr(self):
        file = "grammar.g4"
        # target = "test_antlr"
        framework.grammar.tests4py_grammar(
            "pysnooper", 2, grammar_format="antlr", output=file
        )
        self.assertTrue(os.path.exists(file))
        if os.path.exists(file):
            os.remove(file)

    def test_cache_clear(self):
        project_name = "middle"
        bug_id = 1
        identifier = self.get_identifier(project_name, bug_id)
        git = GLOBAL_PROJECTS / project_name / GLOBAL_GIT
        venv = GLOBAL_PROJECTS / project_name / f"venv_{bug_id}"
        report = framework.cache.tests4py_clear(
            project_name, bug_id, project_and_venv=True
        )
        if report.raised:
            raise report.raised
        self.assertFalse(git.exists())
        self.assertFalse(venv.exists())
        report = framework.cache.tests4py_cache(project_name, bug_id)
        if report.raised:
            raise report.raised
        for r in (report.checkout_reports, report.compile_reports):
            self.assertEqual(1, len(r))
            if r[identifier].raised:
                raise r[identifier].raised
        self.assertTrue(git.exists())
        self.assertTrue(venv.exists())
