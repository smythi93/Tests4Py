import abc
import ast
import os.path
import random
import string
import subprocess
from pathlib import Path
from typing import List, Optional, Any, Tuple

from tests4py.constants import PYTHON
from tests4py.grammars import python
from tests4py.grammars.default import clean_up
from tests4py.grammars.fuzzer import Grammar, is_valid_grammar, srange
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult

PROJECT_NAME = "ansible"


class Ansible(Project):
    def __init__(
        self,
        bug_id: int,
        buggy_commit_id: str,
        fixed_commit_id: str,
        test_files: List[Path],
        test_cases: List[str],
        test_status_fixed: TestStatus = TestStatus.PASSING,
        test_status_buggy: TestStatus = TestStatus.FAILING,
        unittests: Optional[UnittestGenerator] = None,
        systemtests: Optional[SystemtestGenerator] = None,
        api: Optional[API] = None,
        grammar: Optional[Grammar] = None,
        loc: int = 0,
        relevant_test_files: Optional[List[Path]] = None,
        skip_tests: Optional[List[str]] = None,
        included_packages: Optional[str] = None,
    ):
        super().__init__(
            bug_id=bug_id,
            project_name=PROJECT_NAME,
            github_url="https://github.com/ansible/ansible",
            status=Status.OK,
            python_version="3.6.15",
            python_path=os.path.join(PROJECT_NAME, "build", "lib"),
            buggy_commit_id=buggy_commit_id,
            fixed_commit_id=fixed_commit_id,
            testing_framework=TestingFramework.PYTEST,
            test_files=test_files,
            test_cases=test_cases,
            test_status_fixed=test_status_fixed,
            test_status_buggy=test_status_buggy,
            unittests=unittests,
            systemtests=systemtests,
            api=api,
            grammar=grammar,
            loc=loc,
            setup=[[PYTHON, "-m", "pip", "install", "-e", "."]],
            source_base=[Path("lib", "ansible")],
            test_base=Path("test", "units"),
            included_files=(
                [
                    os.path.join("lib", PROJECT_NAME, package)
                    for package in included_packages
                ]
                if included_packages
                else [os.path.join("lib", PROJECT_NAME)]
            ),
            relevant_test_files=relevant_test_files,
            skip_tests=skip_tests,
        )


# REGISTER BUGS


def register():
    Ansible(
        bug_id=1,
        buggy_commit_id="25c5388fdec9e56517a93feb5e8d485680946c25",
        fixed_commit_id="343ffaa18b63c92e182b16c3ad84b8d81ca4df69",
        test_files=[Path("test", "units", "galaxy", "test_collection.py")],
        test_cases=[
            os.path.join(
                "test",
                "units",
                "galaxy",
                "test_collection.py::test_verify_collections_no_version",
            ),
        ],
        included_packages=["galaxy"],
        loc=55990,
    )
    Ansible(
        bug_id=2,
        buggy_commit_id="de59b17c7f69d5cfb72479b71776cc8b97e29a6b",
        fixed_commit_id="5b9418c06ca6d51507468124250bb58046886be6",
        test_files=[Path("test", "units", "utils", "test_version.py")],
        test_cases=[
            os.path.join("test", "units", "utils", "test_version.py::test_alpha"),
            os.path.join("test", "units", "utils", "test_version.py::test_numeric"),
        ],
        included_packages=["utils"],
        api=Ansible2API(),
        unittests=Ansible2UnittestGenerator(),
        systemtests=Ansible2SystemtestGenerator(),
        grammar=grammar_2,
        loc=55936,
    )
    Ansible(
        bug_id=3,
        buggy_commit_id="70219df9056ffb1e2766f572fbe71f7a1800c9f5",
        fixed_commit_id="9d48884e36fb4fd9551f000b87d264383de74e75",
        test_files=[
            Path("test", "units", "module_utils", "test_distribution_version.py")
        ],
        test_cases=[
            os.path.join(
                "test",
                "units",
                "module_utils",
                "test_distribution_version.py::test_distribution_version[stdin29-Kali 2020.2]",
            ),
        ],
        included_packages=["module_utils"],
        api=Ansible3API(),
        unittests=Ansible3UnittestGenerator(),
        systemtests=Ansible3SystemtestGenerator(),
        grammar=grammar_3,
        loc=55902,
    )
    Ansible(
        bug_id=4,
        buggy_commit_id="d91658ec0c8434c82c3ef98bfe9eb4e1027a43a3",
        fixed_commit_id="18a66e291dad71128a32d662aa808213acefe0e9",
        test_files=[Path("test", "units", "playbook", "test_collectionsearch.py")],
        test_cases=[
            os.path.join(
                "test",
                "units",
                "playbook",
                "test_collectionsearch.py::test_collection_static_warning",
            ),
        ],
        relevant_test_files=[Path("test", "units", "playbook")],
        included_packages=["playbook"],
        api=Ansible4API(),
        unittests=Ansible4UnittestGenerator(),
        systemtests=Ansible4SystemtestGenerator(),
        grammar=grammar_4,
        loc=55805,
    )
    Ansible(
        bug_id=5,
        buggy_commit_id="2af76f16be8cf2239daaec4c2f31c3dcb4e3469e",
        fixed_commit_id="3c3ffc09c203d1b2262f6a319cceadd727749761",
        test_files=[
            Path(
                "test",
                "units",
                "module_utils",
                "common",
                "validation",
                "test_check_required_arguments.py",
            )
        ],
        test_cases=[
            os.path.join(
                "test",
                "units",
                "module_utils",
                "common",
                "validation",
                "test_check_required_arguments.py::test_check_required_arguments_missing_multiple",
            ),
        ],
        relevant_test_files=[
            Path(
                "test",
                "units",
                "module_utils",
                "common",
                "validation",
            )
        ],
        included_packages=["module_utils"],
        api=Ansible5API(),
        unittests=Ansible5UnittestGenerator(),
        systemtests=Ansible5SystemtestGenerator(),
        grammar=grammar_5,
        loc=55640,
    )
    Ansible(
        bug_id=6,
        buggy_commit_id="90898132e456ee1993db99a1531379f1b98ee915",
        fixed_commit_id="4881af2e7e0506ada0225fd764e874e20569d5b2",
        test_files=[Path("test", "units", "galaxy", "test_collection_install.py")],
        test_cases=[
            os.path.join(
                "test",
                "units",
                "galaxy",
                "test_collection_install.py::test_build_requirement_from_path_with_manifest[1.1]",
            ),
            os.path.join(
                "test",
                "units",
                "galaxy",
                "test_collection_install.py::test_build_requirement_from_path_with_manifest[1]",
            ),
            os.path.join(
                "test",
                "units",
                "galaxy",
                "test_collection_install.py::test_add_collection_requirement_to_unknown_installed_version",
            ),
        ],
        skip_tests=[
            "test_build_requirement_from_path_no_version",
        ],
        included_packages=["galaxy"],
        # test_status_fixed=TestStatus.FAILING,
        loc=718675,
    )
    Ansible(
        bug_id=7,
        buggy_commit_id="cd146b836e032df785ecd9eb711c6ef23c2228b8",
        fixed_commit_id="cd146b836e032df785ecd9eb711c6ef23c2228b8",
        test_files=[
            Path("test", "units", "modules", "network", "eos", "test_eos_vlans.py")
        ],
        test_cases=[
            os.path.join(
                "test",
                "units",
                "modules",
                "network",
                "eos",
                "test_eos_vlans.py::TestEosVlansModule::test_eos_vlan_replaced",
            ),
        ],
        included_packages=["module_utils"],
        test_status_buggy=TestStatus.PASSING,
        loc=718540,
    )
    Ansible(
        bug_id=8,
        buggy_commit_id="81378b3e744cd0d13b33d18a4f8a38aeb8a6e97a",
        fixed_commit_id="fc7980af9a42676913b4054163570ee438b82e9c",
        test_files=[Path("test", "units", "plugins", "shell", "test_powershell.py")],
        test_cases=[
            os.path.join(
                "test",
                "units",
                "plugins",
                "shell",
                "test_powershell.py::test_join_path_unc",
            ),
        ],
        relevant_test_files=[Path("test", "units", "plugins", "shell")],
        included_packages=["plugins"],
        api=Ansible8API(),
        unittests=Ansible8UnittestGenerator(),
        systemtests=Ansible8SystemtestGenerator(),
        grammar=grammar_8,
        loc=718558,
    )
    Ansible(
        bug_id=9,
        buggy_commit_id="9276dd2007a73172ed99ab5a56cded4298d3cd2b",
        fixed_commit_id="6f1bb37feb81acd99157f5ba0933fecd747015a2",
        test_files=[
            Path(
                "test",
                "units",
                "modules",
                "packaging",
                "os",
                "test_redhat_subscription.py",
            )
        ],
        test_cases=[
            os.path.join(
                "test",
                "units",
                "modules",
                "packaging",
                "os",
                "test_redhat_subscription.py::test_redhat_subscribtion[test_registeration_username_password_pool_ids]",
            ),
            os.path.join(
                "test",
                "units",
                "modules",
                "packaging",
                "os",
                "test_redhat_subscription.py::test_redhat_subscribtion"
                "[test_registeration_username_password_one_pool_id]",
            ),
        ],
        included_packages=["modules"],
        loc=718035,
    )
    Ansible(
        bug_id=10,
        buggy_commit_id="e368f788f71c338cd3f049d5d6bdc643a51c0514",
        fixed_commit_id="a4b59d021368285490f7cda50c11ac4f7a8030b5",
        test_files=[Path("test", "units", "modules", "system", "test_pamd.py")],
        test_cases=[
            os.path.join(
                "test",
                "units",
                "modules",
                "system",
                "test_pamd.py::PamdServiceTestCase::test_remove_first_rule",
            ),
            os.path.join(
                "test",
                "units",
                "modules",
                "system",
                "test_pamd.py::PamdServiceTestCase::test_remove_last_rule",
            ),
        ],
        included_packages=["modules"],
        api=Ansible10API(),
        unittests=Ansible10UnittestGenerator(),
        systemtests=Ansible10SystemtestGenerator(),
        grammar=grammar_10,
        loc=717990,
    )
    Ansible(
        bug_id=11,
        buggy_commit_id="da07b98b7a433493728ddb7ac7efbd20b8988776",
        fixed_commit_id="52f3ce8a808f943561803bd664e695fed1841fe8",
        test_files=[
            Path("test", "units", "modules", "network", "ios", "test_ios_banner.py")
        ],
        test_cases=[
            os.path.join(
                "test",
                "units",
                "modules",
                "network",
                "ios",
                "test_ios_banner.py::TestIosBannerModule::test_ios_banner_nochange",
            ),
            os.path.join(
                "test",
                "units",
                "modules",
                "network",
                "ios",
                "test_ios_banner.py::TestIosBannerIos12Module::test_ios_banner_nochange",
            ),
        ],
        relevant_test_files=[Path("test", "units", "modules", "network", "ios")],
        included_packages=["modules"],
        api=Ansible11API(),
        unittests=Ansible11UnittestGenerator(),
        systemtests=Ansible11SystemtestGenerator(),
        grammar=grammar_11,
        loc=714515,
    )
    Ansible(
        bug_id=12,
        buggy_commit_id="05e2e1806162393d76542a75c2520c7d61c2d855",
        fixed_commit_id="2fa8f9cfd80daf32c7d222190edf7cfc7234582a",
        test_files=[Path("test", "units", "plugins", "lookup", "test_env.py")],
        test_cases=[
            os.path.join(
                "test",
                "units",
                "plugins",
                "lookup",
                "test_env.py::test_env_var_value[foo-bar]",
            ),
            os.path.join(
                "test",
                "units",
                "plugins",
                "lookup",
                "test_env.py::test_env_var_value[equation-a=b*100]",
            ),
            os.path.join(
                "test",
                "units",
                "plugins",
                "lookup",
                "test_env.py::test_utf8_env_var_value[simple_var-alpha-\\u03b2-gamma]",
            ),
            os.path.join(
                "test",
                "units",
                "plugins",
                "lookup",
                "test_env.py::test_utf8_env_var_value[the_var-\\xe3n\\u02c8si\\u03b2le]",
            ),
        ],
        relevant_test_files=[Path("test", "units", "plugins", "lookup")],
        included_packages=["plugins"],
        api=Ansible12API(),
        unittests=Ansible12UnittestGenerator(),
        systemtests=Ansible12SystemtestGenerator(),
        grammar=grammar_12,
        loc=714514,
    )
    Ansible(
        bug_id=13,
        buggy_commit_id="41472ee3878be215af8b933b2b04b4a72b9165ca",
        fixed_commit_id="694ef5660d45fcb97c9beea5b2750f6eadcf5e93",
        test_files=[Path("test", "units", "cli", "test_galaxy.py")],
        test_cases=[
            os.path.join(
                "test",
                "units",
                "cli",
                "test_galaxy.py::test_collection_install_with_url",
            ),
        ],
        included_packages=["cli", "galaxy"],
        loc=711087,
    )
    Ansible(
        bug_id=14,
        buggy_commit_id="a1ab093ddbd32f1002cbf6d6f184c7d0041d890d",
        fixed_commit_id="7acae62fa849481b2a5e2e2d56961c5e1dcea96c",
        test_files=[Path("test", "units", "galaxy", "test_api.py")],
        test_cases=[
            os.path.join(
                "test",
                "units",
                "galaxy",
                "test_api.py::test_get_role_versions_pagination[responses1]",
            ),
        ],
        included_packages=["galaxy"],
        loc=705660,
    )
    Ansible(
        bug_id=15,
        buggy_commit_id="b1e8a6c1cbd2a668b462995487b819ef7dd8ba4b",
        fixed_commit_id="68de182555b185737353e780882159a3d213908c",
        test_files=[
            Path("test", "units", "modules", "network", "eos", "test_eos_eapi.py")
        ],
        test_cases=[
            os.path.join(
                "test",
                "units",
                "modules",
                "network",
                "eos",
                "test_eos_eapi.py::TestEosEapiModule::test_eos_eapi_vrf",
            ),
        ],
        included_packages=["modules"],
        api=Ansible15API(),
        unittests=Ansible15UnittestGenerator(),
        systemtests=Ansible15SystemtestGenerator(),
        grammar=grammar_15,
        loc=701141,
    )
    Ansible(
        bug_id=16,
        buggy_commit_id="2a9964ede8b2b77a62a005f6f5abc964b2819b0e",
        fixed_commit_id="93d9d640380252084855885ad27873b4377898ec",
        test_files=[
            Path(
                "test",
                "units",
                "module_utils",
                "facts",
                "hardware",
                "test_linux_get_cpu_info.py",
            )
        ],
        test_cases=[
            os.path.join(
                "test",
                "units",
                "module_utils",
                "facts",
                "hardware",
                "test_linux_get_cpu_info.py::test_get_cpu_info_missing_arch",
            ),
        ],
        relevant_test_files=[
            Path(
                "test",
                "units",
                "module_utils",
                "facts",
                "hardware",
            )
        ],
        included_packages=["module_utils"],
        api=Ansible16API(),
        unittests=Ansible16UnittestGenerator(),
        systemtests=Ansible16SystemtestGenerator(),
        grammar=grammar_16,
        loc=623199,
    )
    Ansible(
        bug_id=17,
        buggy_commit_id="9cb47832d15c61884b30d70f9d4e0f816b064b05",
        fixed_commit_id="b38cb37728df76e0529243bdce694b18ca0e1163",
        test_files=[Path("test", "units", "module_utils", "facts", "test_facts.py")],
        test_cases=[
            os.path.join(
                "test",
                "units",
                "module_utils",
                "facts",
                "test_facts.py::TestFactsLinuxHardwareGetMountFacts::test_get_mount_facts",
            ),
        ],
        included_packages=["module_utils"],
        api=Ansible17API(),
        unittests=Ansible17UnittestGenerator(),
        systemtests=Ansible17SystemtestGenerator(),
        grammar=grammar_17,
        loc=622794,
    )
    Ansible(
        bug_id=18,
        buggy_commit_id="70219df9056ffb1e2766f572fbe71f7a1800c9f5",
        fixed_commit_id="9d48884e36fb4fd9551f000b87d264383de74e75",
        test_files=[
            Path("test", "units", "module_utils", "test_distribution_version.py")
        ],
        test_cases=[
            os.path.join(
                "test",
                "units",
                "module_utils",
                "test_distribution_version.py::test_distribution_version[stdin29-Kali 2020.2]",
            ),
        ],
        included_packages=["module_utils"],
        api=Ansible3API(),
        unittests=Ansible3UnittestGenerator(),
        systemtests=Ansible3SystemtestGenerator(),
        grammar=grammar_3,
        loc=55902,
    )


class AnsibleAPI(API, abc.ABC):
    def __init__(self, default_timeout: int = 10):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        return TestResult.UNDEFINED, ""


# ======================================================================
# bug_2: ansible.utils.version._Alpha / _Numeric implemented ``__gt__``
# as ``not self.__lt__(other)``, so ``x > x`` (equal operands) wrongly
# returned True instead of False.  The fix redefines ``__gt__`` as
# ``not self.__le__(other)`` (and ``__ge__`` as ``not self.__lt__(other)``).
#
# System-test format:  ``<kind> <a> <b> <op>`` where ``<kind>`` is
#   ``alpha`` (operands are strings) or ``numeric`` (operands are ints),
#   and ``<op>`` is one of ``lt le gt ge eq ne``.  The harness builds the
#   two wrapper objects and prints the boolean of ``a <op> b``; the oracle
#   compares against the correct result computed with native comparison.
#   The ONLY distinguishing case is ``gt`` on equal operands.
# ======================================================================

_VERSION_OPS = ("lt", "le", "gt", "ge", "eq", "ne")


def _correct_version_cmp(kind: str, a: str, b: str, op: str) -> bool:
    if kind == "numeric":
        left, right = int(a), int(b)
    else:
        left, right = a, b
    return {
        "lt": left < right,
        "le": left <= right,
        "gt": left > right,
        "ge": left >= right,
        "eq": left == right,
        "ne": left != right,
    }[op]


class Ansible2API(AnsibleAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            kind = process.args[2]
            a = process.args[3]
            b = process.args[4]
            op = process.args[5]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        try:
            expected = _correct_version_cmp(kind, a, b, op)
        except (ValueError, KeyError):
            return TestResult.UNDEFINED, "Malformed test input"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == str(expected):
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Ansible2TestGenerator:
    @staticmethod
    def generate_word() -> str:
        return "".join(
            random.choices(string.ascii_lowercase, k=random.randint(1, 5))
        )

    @staticmethod
    def generate_number() -> int:
        return random.randint(0, 999)

    def generate_operands(self, kind: str) -> Tuple[str, str]:
        if kind == "numeric":
            return str(self.generate_number()), str(self.generate_number())
        return self.generate_word(), self.generate_word()

    def make_failing(self) -> str:
        # ``gt`` on EQUAL operands is the only case that distinguishes the
        # buggy (`x > x` -> True) from the fixed (`x > x` -> False) build.
        kind = random.choice(("alpha", "numeric"))
        if kind == "numeric":
            value = str(self.generate_number())
        else:
            value = self.generate_word()
        return f"{kind} {value} {value} gt"

    def make_passing(self) -> str:
        # Distinct operands with any operator never trigger the fault.
        kind = random.choice(("alpha", "numeric"))
        while True:
            a, b = self.generate_operands(kind)
            if a != b:
                break
        op = random.choice(_VERSION_OPS)
        return f"{kind} {a} {b} {op}"


class Ansible2SystemtestGenerator(SystemtestGenerator, Ansible2TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Ansible2UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Ansible2TestGenerator
):
    @staticmethod
    def _body(kind: str, a: str, b: str, op: str) -> List[ast.stmt]:
        expected = _correct_version_cmp(kind, a, b, op)
        src = (
            "from ansible.utils.version import _Alpha, _Numeric\n"
            "ops = {'lt': lambda x, y: x < y, 'le': lambda x, y: x <= y, "
            "'gt': lambda x, y: x > y, 'ge': lambda x, y: x >= y, "
            "'eq': lambda x, y: x == y, 'ne': lambda x, y: x != y}\n"
            f"kind, a, b, op = {kind!r}, {a!r}, {b!r}, {op!r}\n"
            "if kind == 'numeric':\n"
            "    left, right = _Numeric(int(a)), _Numeric(int(b))\n"
            "else:\n"
            "    left, right = _Alpha(a), _Alpha(b)\n"
            f"self.assertEqual({expected!r}, ops[op](left, right))\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        kind = random.choice(("alpha", "numeric"))
        value = (
            str(self.generate_number())
            if kind == "numeric"
            else self.generate_word()
        )
        test = self.get_empty_test()
        test.body = self._body(kind, value, value, "gt")
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        kind = random.choice(("alpha", "numeric"))
        while True:
            a, b = self.generate_operands(kind)
            if a != b:
                break
        op = random.choice(_VERSION_OPS)
        test = self.get_empty_test()
        test.body = self._body(kind, a, b, op)
        return test, TestResult.PASSING


grammar_2: Grammar = clean_up(
    {
        "<start>": ["<alpha_test>", "<numeric_test>"],
        "<alpha_test>": ["alpha <word> <word> <op>"],
        "<numeric_test>": ["numeric <number> <number> <op>"],
        "<word>": ["<letter><letters>"],
        "<letters>": ["", "<letter><letters>"],
        "<letter>": srange(string.ascii_lowercase),
        "<number>": ["<digit><digits>"],
        "<digits>": ["", "<digit><digits>"],
        "<digit>": srange(string.digits),
        "<op>": list(_VERSION_OPS),
    }
)

assert is_valid_grammar(grammar_2)


# ======================================================================
# bug_5: module_utils.common.validation.check_required_arguments built the
# "missing required arguments" error message from ``", ".join(missing)``
# using the argument_spec's insertion order.  The fix joins
# ``sorted(missing)`` so the message is deterministic (alphabetical).
#
# System-test format:  a space-separated list of REQUIRED argument names
#   (all missing).  The harness builds an ``OrderedDict`` spec from those
#   names, calls check_required_arguments with empty parameters and prints
#   the raised message.  The oracle compares against the SORTED message.
#   Names given in non-sorted order distinguish buggy from fixed.
# ======================================================================


class Ansible5API(AnsibleAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        names = [a for a in process.args[2:]]
        if not names:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "missing required arguments: " + ", ".join(sorted(names))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Ansible5TestGenerator:
    @staticmethod
    def generate_name() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(2, 6)))

    def generate_distinct_names(self, k: int) -> List[str]:
        names = set()
        while len(names) < k:
            names.add(self.generate_name())
        return list(names)

    def make_failing(self) -> str:
        # names in a NON-sorted order -> buggy keeps that order, fixed sorts
        k = random.randint(2, 4)
        names = self.generate_distinct_names(k)
        while names == sorted(names):
            random.shuffle(names)
        return " ".join(names)

    def make_passing(self) -> str:
        # names already sorted -> buggy and fixed both emit the same message
        k = random.randint(1, 4)
        return " ".join(sorted(self.generate_distinct_names(k)))


class Ansible5SystemtestGenerator(SystemtestGenerator, Ansible5TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Ansible5UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Ansible5TestGenerator
):
    @staticmethod
    def _body(names: List[str]) -> List[ast.stmt]:
        expected = "missing required arguments: " + ", ".join(sorted(names))
        src = (
            "from collections import OrderedDict\n"
            "from ansible.module_utils.common.validation import "
            "check_required_arguments\n"
            "from ansible.module_utils._text import to_native\n"
            f"names = {names!r}\n"
            "spec = OrderedDict((n, {'required': True}) for n in names)\n"
            "try:\n"
            "    check_required_arguments(spec, {})\n"
            "    msg = 'NO_ERROR'\n"
            "except TypeError as e:\n"
            "    msg = to_native(e)\n"
            f"self.assertEqual({expected!r}, msg)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        k = random.randint(2, 4)
        names = self.generate_distinct_names(k)
        while names == sorted(names):
            random.shuffle(names)
        test = self.get_empty_test()
        test.body = self._body(names)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        k = random.randint(1, 4)
        names = sorted(self.generate_distinct_names(k))
        test = self.get_empty_test()
        test.body = self._body(names)
        return test, TestResult.PASSING


grammar_5: Grammar = clean_up(
    {
        "<start>": ["<names>"],
        "<names>": ["<word>", "<word> <names>"],
        "<word>": ["<letter><letters>"],
        "<letters>": ["", "<letter><letters>"],
        "<letter>": srange(string.ascii_lowercase),
    }
)

assert is_valid_grammar(grammar_5)


# ======================================================================
# bug_8: plugins.shell.powershell.ShellModule.join_path split every part
# on backslash and dropped empty components, so a UNC path lost its
# leading ``\\`` (e.g. ``\\host\share\...`` became ``host\share\...``).
# The fix rebuilds the path with ``ntpath.normpath``/``ntpath.join``.
#
# System-test format:  a space-separated list of path components using
#   FORWARD slashes (shlex-safe).  A leading ``//host/share/...`` component
#   is a UNC path (the trigger); plain relative components are unaffected.
#   The harness prints ``ShellModule().join_path(*parts)`` and the oracle
#   compares it to the correct ntpath-based composition.
# ======================================================================


def _correct_join_path(parts: List[str]) -> str:
    import ntpath

    normed = [ntpath.normpath(p) for p in parts]
    return ntpath.join(normed[0], *[p.strip("\\") for p in normed[1:]])


class Ansible8API(AnsibleAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        parts = [a for a in process.args[2:]]
        if not parts:
            return TestResult.UNDEFINED, "Malformed test input"
        try:
            expected = _correct_join_path(parts)
        except Exception:
            return TestResult.UNDEFINED, "Malformed test input"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Ansible8TestGenerator:
    @staticmethod
    def _seg() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 6)))

    def _relative_arg(self) -> str:
        return "/".join(self._seg() for _ in range(random.randint(1, 3)))

    def make_failing_args(self) -> List[str]:
        host, share = self._seg(), self._seg()
        first = (
            "//"
            + host
            + "/"
            + share
            + "/"
            + "/".join(self._seg() for _ in range(random.randint(1, 2)))
        )
        rest = [self._relative_arg() for _ in range(random.randint(1, 3))]
        return [first] + rest

    def make_passing_args(self) -> List[str]:
        return [self._relative_arg() for _ in range(random.randint(2, 4))]


class Ansible8SystemtestGenerator(SystemtestGenerator, Ansible8TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return " ".join(self.make_failing_args()), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return " ".join(self.make_passing_args()), TestResult.PASSING


class Ansible8UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Ansible8TestGenerator
):
    @staticmethod
    def _body(args: List[str]) -> List[ast.stmt]:
        src = (
            "import ntpath\n"
            "from ansible.plugins.shell.powershell import ShellModule\n"
            f"args = {args!r}\n"
            "normed = [ntpath.normpath(a) for a in args]\n"
            "expected = ntpath.join(normed[0], "
            "*[p.strip(chr(92)) for p in normed[1:]])\n"
            "self.assertEqual(expected, ShellModule().join_path(*args))\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body(self.make_failing_args())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body(self.make_passing_args())
        return test, TestResult.PASSING


grammar_8: Grammar = clean_up(
    {
        "<start>": ["<tokens>"],
        "<tokens>": ["<token>", "<token> <tokens>"],
        "<token>": ["<char><chars>"],
        "<chars>": ["", "<char><chars>"],
        "<char>": srange(string.ascii_lowercase) + ["/"],
    }
)

assert is_valid_grammar(grammar_8)


# ======================================================================
# bug_10: modules.system.pamd.PamdService.remove crashed when deleting the
# LAST rule in the linked list: it unconditionally executed
# ``current_line.next.prev = current_line.prev`` even when ``next`` was
# ``None`` -> AttributeError.  The fix guards ``if current_line.next is not
# None`` (and initialises ``prev``/``next`` on PamdRule).
#
# System-test format:  ``<idx> <rule> <rule> ...`` where each ``<rule>`` is
#   ``type:control:path`` (colon-separated, no spaces) and ``<idx>`` is the
#   index of the rule to remove.  The harness builds a PamdService, removes
#   that rule, and prints ``OK`` on success or ``ERROR:<Exc>``.  Removing
#   the LAST rule triggers the fault; the oracle expects ``OK``.
# ======================================================================


class Ansible10API(AnsibleAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        if len(process.args) < 4:
            return TestResult.UNDEFINED, "Malformed test input"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == "OK":
            return TestResult.PASSING, "Rule removed successfully"
        return TestResult.FAILING, f"Expected 'OK', but was {out!r}"


class Ansible10TestGenerator:
    _TYPES = ("auth", "account", "session", "password")
    _CONTROLS = ("required", "sufficient", "optional", "requisite")

    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 6)))

    def _rules(self, n: int) -> List[Tuple[str, str, str]]:
        used = set()
        rules = []
        while len(rules) < n:
            path = "pam" + self._word() + ".so"
            if path in used:
                continue
            used.add(path)
            rules.append(
                (random.choice(self._TYPES), random.choice(self._CONTROLS), path)
            )
        return rules

    def make_failing(self) -> Tuple[int, List[Tuple[str, str, str]]]:
        n = random.randint(2, 5)
        rules = self._rules(n)
        return n - 1, rules  # remove the LAST rule -> triggers the fault

    def make_passing(self) -> Tuple[int, List[Tuple[str, str, str]]]:
        n = random.randint(3, 6)
        rules = self._rules(n)
        return random.randint(1, n - 2), rules  # remove a MIDDLE rule


def _format_pamd_system(idx: int, rules: List[Tuple[str, str, str]]) -> str:
    return f"{idx} " + " ".join(":".join(r) for r in rules)


class Ansible10SystemtestGenerator(SystemtestGenerator, Ansible10TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        idx, rules = self.make_failing()
        return _format_pamd_system(idx, rules), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        idx, rules = self.make_passing()
        return _format_pamd_system(idx, rules), TestResult.PASSING


class Ansible10UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Ansible10TestGenerator
):
    @staticmethod
    def _body(idx: int, rules: List[Tuple[str, str, str]]) -> List[ast.stmt]:
        rules_list = [list(r) for r in rules]
        src = (
            "from ansible.modules.system.pamd import PamdService\n"
            f"rules = {rules_list!r}\n"
            f"idx = {idx}\n"
            "content = chr(10).join(' '.join(r) for r in rules)\n"
            "svc = PamdService(content)\n"
            "t, c, p = rules[idx]\n"
            "try:\n"
            "    changed = svc.remove(t, c, p)\n"
            "    result = 'OK' if (changed and not svc.has_rule(t, c, p)) "
            "else 'FAIL'\n"
            "except Exception as e:\n"
            "    result = 'ERROR:' + type(e).__name__\n"
            "self.assertEqual('OK', result)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        idx, rules = self.make_failing()
        test = self.get_empty_test()
        test.body = self._body(idx, rules)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        idx, rules = self.make_passing()
        test = self.get_empty_test()
        test.body = self._body(idx, rules)
        return test, TestResult.PASSING


grammar_10: Grammar = clean_up(
    {
        "<start>": ["<chars>"],
        "<chars>": ["", "<char><chars>"],
        "<char>": srange(string.ascii_lowercase + string.digits + " :._"),
    }
)

assert is_valid_grammar(grammar_10)


# ======================================================================
# bug_3 / bug_18 (same commit): module_utils.facts.system.distribution
# .DistributionFiles.parse_distribution_file_Debian only recognised Kali
# from ``/etc/lsb-release`` (``elif path == '/etc/lsb-release' and 'Kali'
# in data``).  Kali 2020.2 ships its identity in ``/etc/os-release``, so
# detection failed.  The fix accepts both ``/etc/lsb-release`` and
# ``/etc/os-release``.
#
# System-test format:  ``<distro> <path> <version>`` where ``<distro>`` is
#   ``kali``/``ubuntu``/``steamos``, ``<path>`` is ``os``/``lsb`` and
#   ``<version>`` is a version string.  The harness builds a minimal
#   os-/lsb-release blob, calls the parser and prints ``<matched>
#   <distribution>``.  ``kali os`` distinguishes buggy (``False None``)
#   from fixed (``True Kali``); the oracle expects the fixed result.
# ======================================================================

_DISTRO_NAMES = {"kali": "Kali", "ubuntu": "Ubuntu", "steamos": "SteamOS"}


class Ansible3API(AnsibleAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            distro = process.args[2]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        if distro not in _DISTRO_NAMES:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = f"True {_DISTRO_NAMES[distro]}"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Ansible3TestGenerator:
    @staticmethod
    def generate_version() -> str:
        return f"{random.randint(2000, 2099)}.{random.randint(0, 9)}"

    def make_failing(self) -> str:
        # kali advertised via /etc/os-release: buggy fails to detect it
        return f"kali os {self.generate_version()}"

    def make_passing(self) -> str:
        # every other combination detects identically on both builds
        distro = random.choice(("kali", "ubuntu", "steamos"))
        if distro == "kali":
            path = "lsb"
        else:
            path = random.choice(("os", "lsb"))
        return f"{distro} {path} {self.generate_version()}"


class Ansible3SystemtestGenerator(SystemtestGenerator, Ansible3TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Ansible3UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Ansible3TestGenerator
):
    @staticmethod
    def _body(distro: str, path_kind: str, version: str) -> List[ast.stmt]:
        expected = f"True {_DISTRO_NAMES[distro]}"
        src = (
            "from ansible.module_utils.facts.system.distribution import "
            "DistributionFiles\n"
            f"distro, path_kind, version = {distro!r}, {path_kind!r}, {version!r}\n"
            "if distro == 'kali':\n"
            "    data = 'NAME=\"Kali GNU/Linux Rolling\" VERSION=\"' + version + '\"'\n"
            "elif distro == 'ubuntu':\n"
            "    data = 'NAME=\"Ubuntu\" VERSION=\"' + version + '\"'\n"
            "else:\n"
            "    data = 'NAME=\"SteamOS\" VERSION=\"' + version + '\"'\n"
            "path = '/etc/os-release' if path_kind == 'os' else '/etc/lsb-release'\n"
            "df = DistributionFiles(module=None)\n"
            "matched, facts = df.parse_distribution_file_Debian("
            "distro, data, path, {'distribution_release': 'NA'})\n"
            "result = '%s %s' % (matched, facts.get('distribution'))\n"
            f"self.assertEqual({expected!r}, result)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("kali", "os", self.generate_version())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        distro = random.choice(("kali", "ubuntu", "steamos"))
        path_kind = "lsb" if distro == "kali" else random.choice(("os", "lsb"))
        test = self.get_empty_test()
        test.body = self._body(distro, path_kind, self.generate_version())
        return test, TestResult.PASSING


grammar_3: Grammar = clean_up(
    {
        "<start>": ["<distro> <path> <version>"],
        "<distro>": ["kali", "ubuntu", "steamos"],
        "<path>": ["os", "lsb"],
        "<version>": ["<vchar><vchars>"],
        "<vchars>": ["", "<vchar><vchars>"],
        "<vchar>": srange(string.digits) + ["."],
    }
)

assert is_valid_grammar(grammar_3)


# ======================================================================
# bug_16: module_utils.facts.hardware.linux.LinuxHardware.get_cpu_facts
# only forced the ``processor`` count for ARM systems
# (``startswith(('armv', 'aarch'))``).  On Power (ppc) cpuinfo lists both
# ``processor`` and ``cpu`` entries, so the processor count was doubled.
# The fix adds ``'ppc'`` to the prefix tuple.
#
# System-test format:  ``<arch> <n>`` where ``<arch>`` is a CPU
#   architecture and ``<n>`` the number of processors.  The harness builds
#   a synthetic cpuinfo (Power-style for ppc, Intel-style otherwise),
#   patches the file readers, and prints ``processor_count``.  A ``ppc*``
#   architecture doubles the count on the buggy build; the oracle expects
#   the correct value ``n``.
# ======================================================================


class Ansible16API(AnsibleAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            n = int(process.args[3])
        except (IndexError, ValueError):
            return TestResult.UNDEFINED, "Malformed test input"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == str(n):
            return TestResult.PASSING, f"Expected processor_count={n}"
        return TestResult.FAILING, f"Expected processor_count={n}, but was {out!r}"


class Ansible16TestGenerator:
    _PPC = ("ppc64", "ppc64le", "ppc")
    _OTHER = ("x86_64", "i386", "amd64")

    @staticmethod
    def generate_n() -> int:
        return random.randint(2, 8)

    def make_failing(self) -> str:
        return f"{random.choice(self._PPC)} {self.generate_n()}"

    def make_passing(self) -> str:
        return f"{random.choice(self._OTHER)} {self.generate_n()}"


class Ansible16SystemtestGenerator(SystemtestGenerator, Ansible16TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Ansible16UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Ansible16TestGenerator
):
    @staticmethod
    def _body(arch: str, n: int) -> List[ast.stmt]:
        src = (
            "from unittest import mock\n"
            "from ansible.module_utils.facts.hardware import linux\n"
            f"arch, n = {arch!r}, {n}\n"
            "lines = []\n"
            "if arch.startswith(('ppc', 'powerpc')):\n"
            "    for k in range(n):\n"
            "        lines.append('processor : %d' % k)\n"
            "        lines.append('cpu : POWER8 (architected), altivec supported')\n"
            "    lines.append('timebase : 512000000')\n"
            "else:\n"
            "    for k in range(n):\n"
            "        lines.append('processor : %d' % k)\n"
            "        lines.append('vendor_id : GenuineIntel')\n"
            "        lines.append('model name : Intel(R) Xeon(R) CPU')\n"
            "inst = linux.LinuxHardware(mock.Mock())\n"
            "with mock.patch('os.path.exists', return_value=False), "
            "mock.patch('os.access', return_value=True), "
            "mock.patch('ansible.module_utils.facts.hardware.linux."
            "get_file_lines', side_effect=[[], lines]):\n"
            "    facts = inst.get_cpu_facts("
            "collected_facts={'ansible_architecture': arch})\n"
            "self.assertEqual(n, facts.get('processor_count'))\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        arch = random.choice(self._PPC)
        test = self.get_empty_test()
        test.body = self._body(arch, self.generate_n())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        arch = random.choice(self._OTHER)
        test = self.get_empty_test()
        test.body = self._body(arch, self.generate_n())
        return test, TestResult.PASSING


grammar_16: Grammar = clean_up(
    {
        "<start>": ["<arch> <n>"],
        "<arch>": ["ppc64", "ppc64le", "ppc", "x86_64", "i386", "amd64"],
        "<n>": ["<digit><digits>"],
        "<digits>": ["", "<digit><digits>"],
        "<digit>": srange(string.digits),
    }
)

assert is_valid_grammar(grammar_16)


# ======================================================================
# bug_15: modules.network.eos.eos_eapi.map_obj_to_commands guarded the
# state (shutdown / no shutdown) command with ``if needs_update('state')
# and not needs_update('vrf')``.  When BOTH state and vrf changed, the
# state command was dropped.  The fix uses ``if needs_update('state')``.
#
# System-test format:  ``<want_state> <want_vrf> <have_state> <have_vrf>``
#   where each field is ``started``/``stopped``/``none`` (states) or a vrf
#   name / ``none``.  The harness builds want/have dicts (all protocol keys
#   None) and prints the ``|``-joined command list.  A case where state and
#   vrf both need updating distinguishes buggy from fixed; the oracle
#   compares against the correct command list.
# ======================================================================

_EOS_KEYS = (
    "http",
    "http_port",
    "https",
    "https_port",
    "local_http",
    "local_http_port",
    "socket",
)


def _eos_val(token: str) -> Optional[str]:
    return None if token == "none" else token


def _correct_eos_commands(ws, wv, hs, hv) -> List[str]:
    commands: List[str] = []

    def needs(w, h):
        return w is not None and w != h

    def add(cmd):
        if "management api http-commands" not in commands:
            commands.insert(0, "management api http-commands")
        commands.append(cmd)

    if needs(ws, hs):  # fixed: guarded on state only
        if ws == "stopped":
            add("shutdown")
        elif ws == "started":
            add("no shutdown")
    if needs(wv, hv):
        add("vrf %s" % wv)
        if ws == "stopped":
            add("shutdown")
        elif ws == "started":
            add("no shutdown")
    return commands


class Ansible15API(AnsibleAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            ws, wv, hs, hv = (_eos_val(process.args[i]) for i in range(2, 6))
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "|".join(_correct_eos_commands(ws, wv, hs, hv))
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Ansible15TestGenerator:
    @staticmethod
    def _vrf_word() -> str:
        while True:
            w = "".join(
                random.choices(string.ascii_lowercase, k=random.randint(3, 6))
            )
            if w not in ("none", "started", "stopped"):
                return w

    def make_failing(self) -> str:
        # both state and vrf need updating -> buggy drops the state command
        ws = random.choice(("started", "stopped"))
        hs = "stopped" if ws == "started" else "started"
        return f"{ws} {self._vrf_word()} {hs} none"

    def make_passing(self) -> str:
        if random.random() < 0.5:
            # state-only change (vrf unchanged)
            ws = random.choice(("started", "stopped"))
            hs = "stopped" if ws == "started" else "started"
            return f"{ws} none {hs} none"
        # vrf-only change (state not updated)
        wv = self._vrf_word()
        hs = random.choice(("started", "stopped"))
        return f"none {wv} {hs} none"


class Ansible15SystemtestGenerator(SystemtestGenerator, Ansible15TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Ansible15UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Ansible15TestGenerator
):
    @staticmethod
    def _body(ws, wv, hs, hv) -> List[ast.stmt]:
        expected = "|".join(
            _correct_eos_commands(_eos_val(ws), _eos_val(wv), _eos_val(hs), _eos_val(hv))
        )
        src = (
            "from ansible.modules.network.eos.eos_eapi import map_obj_to_commands\n"
            f"keys = {list(_EOS_KEYS)!r}\n"
            f"ws, wv, hs, hv = {ws!r}, {wv!r}, {hs!r}, {hv!r}\n"
            "def val(x):\n"
            "    return None if x == 'none' else x\n"
            "want = {k: None for k in keys}\n"
            "want['state'], want['vrf'] = val(ws), val(wv)\n"
            "have = {k: None for k in keys}\n"
            "have['state'], have['vrf'] = val(hs), val(hv)\n"
            "commands = map_obj_to_commands((want, have), None, [])\n"
            f"self.assertEqual({expected!r}, '|'.join(commands))\n"
        )
        return ast.parse(src).body

    def _fields_failing(self):
        ws = random.choice(("started", "stopped"))
        hs = "stopped" if ws == "started" else "started"
        return ws, self._vrf_word(), hs, "none"

    def _fields_passing(self):
        if random.random() < 0.5:
            ws = random.choice(("started", "stopped"))
            hs = "stopped" if ws == "started" else "started"
            return ws, "none", hs, "none"
        return "none", self._vrf_word(), random.choice(("started", "stopped")), "none"

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body(*self._fields_failing())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body(*self._fields_passing())
        return test, TestResult.PASSING


grammar_15: Grammar = clean_up(
    {
        "<start>": ["<state> <vrf> <state> <vrf>"],
        "<state>": ["started", "stopped", "none"],
        "<vrf>": ["none", "<word>"],
        "<word>": ["<letter><letters>"],
        "<letters>": ["", "<letter><letters>"],
        "<letter>": srange(string.ascii_lowercase),
    }
)

assert is_valid_grammar(grammar_15)


# ======================================================================
# bug_17: module_utils.facts.hardware.linux.LinuxHardware.get_mount_facts
# used the raw mtab fields, so octal escape sequences (e.g. a space
# encoded as ``\040`` in a mount path) were never decoded.  The fix adds
# ``_replace_octal_escapes`` and applies it to every mtab field.
#
# System-test format:  ``<mode> <name1> <name2>`` where ``<mode>`` is
#   ``esc`` (mount path ``/mnt/<name1>\040<name2>`` -- the trigger) or
#   ``plain`` (``/mnt/<name1><name2>``).  The harness mocks the mtab/uuid
#   helpers, runs get_mount_facts and prints the resulting mount path.
#   The oracle expects the decoded path (space for ``esc``).
# ======================================================================


class Ansible17API(AnsibleAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
            name1 = process.args[3]
            name2 = process.args[4]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        if mode == "esc":
            expected = f"/mnt/{name1} {name2}"
        else:
            expected = f"/mnt/{name1}{name2}"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected!r}"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Ansible17TestGenerator:
    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 6)))

    def make_failing(self) -> str:
        return f"esc {self._word()} {self._word()}"

    def make_passing(self) -> str:
        return f"plain {self._word()} {self._word()}"


class Ansible17SystemtestGenerator(SystemtestGenerator, Ansible17TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Ansible17UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Ansible17TestGenerator
):
    @staticmethod
    def _body(mode: str, name1: str, name2: str) -> List[ast.stmt]:
        if mode == "esc":
            expected = f"/mnt/{name1} {name2}"
        else:
            expected = f"/mnt/{name1}{name2}"
        src = (
            "from unittest import mock\n"
            "from ansible.module_utils.facts.hardware import linux\n"
            f"mode, name1, name2 = {mode!r}, {name1!r}, {name2!r}\n"
            "if mode == 'esc':\n"
            "    mount_raw = '/mnt/' + name1 + chr(92) + '040' + name2\n"
            "else:\n"
            "    mount_raw = '/mnt/' + name1 + name2\n"
            "entries = [['/dev/sdz', mount_raw, 'ext4', 'rw,relatime', '0', '0']]\n"
            "lh = linux.LinuxHardware(module=mock.Mock(), load_on_init=False)\n"
            "with mock.patch.object(linux.LinuxHardware, '_mtab_entries', "
            "return_value=entries), mock.patch.object(linux.LinuxHardware, "
            "'_find_bind_mounts', return_value=[]), mock.patch.object("
            "linux.LinuxHardware, '_lsblk_uuid', return_value={}), "
            "mock.patch.object(linux.LinuxHardware, '_udevadm_uuid', "
            "return_value=''):\n"
            "    result = lh.get_mount_facts()\n"
            "mounts = result['mounts']\n"
            "actual = mounts[0]['mount'] if mounts else 'NO_MOUNT'\n"
            f"self.assertEqual({expected!r}, actual)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("esc", self._word(), self._word())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("plain", self._word(), self._word())
        return test, TestResult.PASSING


grammar_17: Grammar = clean_up(
    {
        "<start>": ["<mode> <word> <word>"],
        "<mode>": ["esc", "plain"],
        "<word>": ["<letter><letters>"],
        "<letters>": ["", "<letter><letters>"],
        "<letter>": srange(string.ascii_lowercase),
    }
)

assert is_valid_grammar(grammar_17)


# ======================================================================
# bug_4: playbook.collectionsearch.CollectionSearch._load_collections did
# not warn when a collection name was actually a Jinja template (which is
# not supported).  The fix iterates the collection names and emits a
# ``display.warning('"collections" is not templatable ...')`` for each
# templated entry.
#
# System-test format:  a single collection name token.  A templated name
#   (contains ``{{ }}``) must produce the warning; a plain name must not.
#   The harness calls ``_load_collections`` capturing stderr and prints
#   ``WARN``/``NOWARN``.  The oracle expects ``WARN`` iff the name is a
#   template.
# ======================================================================


class Ansible4API(AnsibleAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            name = process.args[2]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        expected = "WARN" if ("{{" in name and "}}" in name) else "NOWARN"
        out = process.stdout.decode("utf8").strip()
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, f"Expected {expected}"
        return TestResult.FAILING, f"Expected {expected}, but was {out!r}"


class Ansible4TestGenerator:
    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 6)))

    def make_failing(self) -> str:
        if random.random() < 0.5:
            return f"{self._word()}.{{{{{self._word()}}}}}"
        return f"{{{{{self._word()}}}}}"

    def make_passing(self) -> str:
        if random.random() < 0.5:
            return f"{self._word()}.{self._word()}"
        return self._word()


class Ansible4SystemtestGenerator(SystemtestGenerator, Ansible4TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Ansible4UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Ansible4TestGenerator
):
    @staticmethod
    def _body(name: str) -> List[ast.stmt]:
        expected = "WARN" if ("{{" in name and "}}" in name) else "NOWARN"
        src = (
            "import io, contextlib\n"
            "from ansible.playbook.collectionsearch import CollectionSearch\n"
            f"name = {name!r}\n"
            "cs = CollectionSearch()\n"
            "buf = io.StringIO()\n"
            "with contextlib.redirect_stderr(buf):\n"
            "    result = cs._load_collections(None, [name])\n"
            "err = buf.getvalue()\n"
            "actual = 'WARN' if (('is not templatable' in err) and "
            "(name in err)) else 'NOWARN'\n"
            f"self.assertEqual({expected!r}, actual)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body(self.make_failing())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body(self.make_passing())
        return test, TestResult.PASSING


grammar_4: Grammar = clean_up(
    {
        "<start>": ["<word>.{{<word>}}", "{{<word>}}", "<word>.<word>", "<word>"],
        "<word>": ["<letter><letters>"],
        "<letters>": ["", "<letter><letters>"],
        "<letter>": srange(string.ascii_lowercase),
    }
)

assert is_valid_grammar(grammar_4)


# ======================================================================
# bug_11: modules.network.ios.ios_banner.map_obj_to_commands built the
# banner command with ``want['text'].strip()``, stripping ALL surrounding
# whitespace (including significant leading/trailing spaces).  The fix uses
# ``want['text'].strip('\n')`` so only newlines are removed.
#
# System-test format:  ``<mode> <word>`` where ``<mode>`` is ``pad``
#   (text = ``"  <word>  "`` -- the trigger), ``nl`` (newline padded) or
#   ``plain``.  The harness calls map_obj_to_commands and prints the banner
#   command.  The oracle expects the command built with ``strip('\n')``.
# ======================================================================


def _ios_build_text(mode: str, word: str) -> str:
    if mode == "pad":
        return "  " + word + "  "
    if mode == "nl":
        return "\n" + word + "\n"
    return word


class Ansible11API(AnsibleAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            mode = process.args[2]
            word = process.args[3]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        text = _ios_build_text(mode, word)
        expected = "banner login @\n" + text.strip("\n") + "\n@"
        out = process.stdout.decode("utf8").rstrip("\n")
        if process.returncode == 0 and out == expected:
            return TestResult.PASSING, "Banner command matches"
        return TestResult.FAILING, f"Expected {expected!r}, but was {out!r}"


class Ansible11TestGenerator:
    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 6)))

    def make_failing(self) -> str:
        return f"pad {self._word()}"

    def make_passing(self) -> str:
        return f"{random.choice(('nl', 'plain'))} {self._word()}"


class Ansible11SystemtestGenerator(SystemtestGenerator, Ansible11TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Ansible11UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Ansible11TestGenerator
):
    @staticmethod
    def _body(mode: str, word: str) -> List[ast.stmt]:
        text = _ios_build_text(mode, word)
        expected = "banner login @\n" + text.strip("\n") + "\n@"
        src = (
            "from types import SimpleNamespace\n"
            "from ansible.modules.network.ios.ios_banner import "
            "map_obj_to_commands\n"
            f"mode, word = {mode!r}, {word!r}\n"
            "if mode == 'pad':\n"
            "    text = '  ' + word + '  '\n"
            "elif mode == 'nl':\n"
            "    text = chr(10) + word + chr(10)\n"
            "else:\n"
            "    text = word\n"
            "module = SimpleNamespace(params={'state': 'present', "
            "'banner': 'login'})\n"
            "cmds = map_obj_to_commands(({'text': text}, {'text': None}), module)\n"
            "actual = cmds[0] if cmds else 'NONE'\n"
            f"self.assertEqual({expected!r}, actual)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("pad", self._word())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body(random.choice(("nl", "plain")), self._word())
        return test, TestResult.PASSING


grammar_11: Grammar = clean_up(
    {
        "<start>": ["<mode> <word>"],
        "<mode>": ["pad", "nl", "plain"],
        "<word>": ["<letter><letters>"],
        "<letters>": ["", "<letter><letters>"],
        "<letter>": srange(string.ascii_lowercase),
    }
)

assert is_valid_grammar(grammar_11)


# ======================================================================
# bug_12: plugins.lookup.env.LookupModule.run read variables with
# ``os.getenv(var, '')`` instead of the encoding-aware
# ``py3compat.environ.get(var, '')``.  The fix routes the lookup through
# ``ansible.utils.py3compat.environ``.
#
# System-test format:  ``<mode> <var> <value>`` where ``<mode>`` is
#   ``patch`` (patch ``py3compat.environ.get`` to return ``<value>`` with
#   ``<var>`` absent from os.environ -- buggy still reads os.getenv and
#   returns '') or ``real`` (set the real env var).  The harness runs the
#   env lookup and prints the value; the oracle expects ``<value>``.
# ======================================================================


class Ansible12API(AnsibleAPI):
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        try:
            value = process.args[4]
        except IndexError:
            return TestResult.UNDEFINED, "Malformed test input"
        out = process.stdout.decode("utf8").rstrip("\n")
        if process.returncode == 0 and out == value:
            return TestResult.PASSING, f"Expected {value!r}"
        return TestResult.FAILING, f"Expected {value!r}, but was {out!r}"


class Ansible12TestGenerator:
    @staticmethod
    def _word() -> str:
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 7)))

    def make_failing(self) -> str:
        return f"patch {self._word()} {self._word()}"

    def make_passing(self) -> str:
        return f"real {self._word()} {self._word()}"


class Ansible12SystemtestGenerator(SystemtestGenerator, Ansible12TestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        return self.make_failing(), TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        return self.make_passing(), TestResult.PASSING


class Ansible12UnittestGenerator(
    python.PythonGenerator, UnittestGenerator, Ansible12TestGenerator
):
    @staticmethod
    def _body(mode: str, var: str, value: str) -> List[ast.stmt]:
        src = (
            "import os\n"
            "from unittest import mock\n"
            "import ansible.utils.py3compat as py3compat\n"
            "from ansible.plugins.loader import lookup_loader\n"
            f"mode, var, value = {mode!r}, {var!r}, {value!r}\n"
            "env_lookup = lookup_loader.get('env')\n"
            "if mode == 'patch':\n"
            "    os.environ.pop(var, None)\n"
            "    with mock.patch.object(py3compat.environ, 'get', "
            "lambda x, y=None: value):\n"
            "        retval = env_lookup.run([var], None)\n"
            "else:\n"
            "    os.environ[var] = value\n"
            "    retval = env_lookup.run([var], None)\n"
            "actual = retval[0] if retval else 'EMPTY'\n"
            "self.assertEqual(value, actual)\n"
        )
        return ast.parse(src).body

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("patch", self._word(), self._word())
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        test = self.get_empty_test()
        test.body = self._body("real", self._word(), self._word())
        return test, TestResult.PASSING


grammar_12: Grammar = clean_up(
    {
        "<start>": ["<mode> <word> <word>"],
        "<mode>": ["patch", "real"],
        "<word>": ["<letter><letters>"],
        "<letters>": ["", "<letter><letters>"],
        "<letter>": srange(string.ascii_lowercase),
    }
)

assert is_valid_grammar(grammar_12)
