import re
from pathlib import Path
from typing import Dict

# ~~~~~~ TYPES ~~~~~~ #

Environment = Dict[str, str]

# ~~~~~ COMMANDS ~~~~ #

CHECKOUT = "checkout"
COMPILE = "compile"
COVERAGE = "coverage"
INFO = "info"
MUTATION = "mutation"
TEST = "test"
UNITTEST = "unittest"
SYSTEMTEST = "systemtest"
GENERATE = "generate"
CACHE = "cache"
CONFIG = "config"
GRAMMAR = "grammar"

# ~~~~~~ FILES ~~~~~~ #

DEFAULT_WORK_DIR = Path(Path.cwd(), "tmp").absolute()
DEFAULT_UNITTESTS_DIVERSITY_PATH = "tests4py_unittests_diversity.py"
DEFAULT_SYSTEMTESTS_DIVERSITY_PATH = "tests4py_systemtest_diversity"

INFO_FILE = "tests4py_info.ini"
REQUIREMENTS_FILE = "tests4py_requirements.txt"
SETUP_FILE = "tests4py_setup.sh"
PATCH_FILE = "tests4py_fix.patch"
HARNESS_FILE = "tests4py_harness.py"
FIX_FILES = "tests4py_files.txt"
EXPLANATION_FILE = "tests4py_explanation.md"

# ~~ TEST PATTERN ~~ #

PYTEST_PATTERN = re.compile(
    rb"= ((((?P<f>\d+) failed)|((?P<p>\d+) passed)|(\d+ warnings?))(, )?)+ in "
)
UNITTEST_TOTAL_PATTERN = re.compile(rb"Ran (?P<t>\d+) tests? in")
UNITTEST_FAILED_PATTERN = re.compile(rb"FAILED (failures=(?P<f>\d+))")
SYSTEMTESTS_FAILING_CLASS = "TestsFailing"
SYSTEMTESTS_PASSING_CLASS = "TestsPassing"
DEFAULT_SUB_PATH_SYSTEMTESTS = "tests4py_systemtests"
DEFAULT_SUB_PATH_UNITTESTS = "tests4py_unittests.py"

# ~~~~~~ CONFIG ~~~~~~ #

GLOBAL_CONFIGS = Path.home() / ".t4p"
GLOBAL_CONFIG_FILE = GLOBAL_CONFIGS / "config.ini"
GLOBAL_PROJECTS = GLOBAL_CONFIGS / "projects"
GLOBAL_GIT = "project"

# ~~~~~~ VENV ~~~~~~ #

VERSION_PATTERN = re.compile(r"Installed Python-(?P<v>\d+.\d+.\d+)")
VENV = "tests4py_venv"

# ~~~~~~ TESTS ~~~~~~ #

NEWLINE_TOKEN = "TESTS4PYNEWLINETOKEN"
