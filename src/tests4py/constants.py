import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict

import psutil

# ~~~~~~ TYPES ~~~~~~ #

Environment = Dict[str, str]

# ~~~~~ COMMANDS ~~~~ #

CHECKOUT = "checkout"
BUILD = "build"
COVERAGE = "coverage"
INFO = "info"
MUTATION = "mutation"
TEST = "test"
UNITTEST = "unittest"
SYSTEMTEST = "systemtest"
GENERATE = "generate"
CACHE = "cache"
CLEAR = "clear"
CONFIG = "config"
GRAMMAR = "grammar"
GET_TESTS = "get"
RUN = "run"

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
TMP_FILE = "tests4py_tmp"
SRC_FILE = "tests4py_src"

# ~~ TEST PATTERN ~~ #

PYTEST_PATTERN = re.compile(
    rb"=( |\x1b\[\d+m)+(("
    rb"((?P<f>\d+) failed)|"
    rb"((?P<p>\d+) passed)|"
    rb"(\d+ (skipped|warning(s?)|"
    rb"(error(s?)))))"
    rb"(( |\x1b\[\d+m)*,( |\x1b\[\d+m)+)?)+( |\x1b\[\d+m)+in( |\x1b\[\d+m)+"
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

# ~~~~~~ PYENV ~~~~~~ #

PYTHON = "python"


def check_pyenv(pyenv):
    try:
        _ = subprocess.check_output([pyenv, "--version"])
    except FileNotFoundError:
        return False
    return True


PYENV_ROOT = Path.home() / ".pyenv"
PYENV_TMP = Path.home() / "pyenv_tmp"

if sys.platform.startswith("win"):
    IS_POWER_SHELL = bool(
        re.fullmatch(
            "pwsh|pwsh.exe|powershell.exe", psutil.Process(os.getppid()).name()
        )
    )
else:
    IS_POWER_SHELL = False

PYENV = "pyenv"

if check_pyenv(PYENV):
    PYENV_EXISTS = True
else:
    if sys.platform.startswith("win"):
        if IS_POWER_SHELL:
            PYENV = (PYENV_ROOT / "bin" / "pyenv.ps1").absolute()
        else:
            PYENV = (PYENV_ROOT / "bin" / "pyenv.bat").absolute()
    else:
        PYENV = (PYENV_ROOT / "bin" / "pyenv").absolute()
    PYENV_EXISTS = PYENV.exists()
    PYENV = str(PYENV)

os.environ["PYENV_ROOT"] = str(PYENV_ROOT)
