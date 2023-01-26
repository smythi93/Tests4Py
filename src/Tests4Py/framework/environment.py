import logging
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from Tests4Py.framework.constants import Environment

from Tests4Py.framework.logger import LOGGER
from Tests4Py.projects import Project

VERSION_PATTERN = re.compile(r"Installed Python-(?P<v>\d+.\d+.\d+)")
VENV = "tests4py_venv"


def __env_on__(project: Project, verbose=True) -> Environment:
    if verbose:
        LOGGER.setLevel(logging.INFO)
    else:
        LOGGER.setLevel(logging.WARNING)

    LOGGER.info(f"Checking for platform {sys.platform}")
    if sys.platform == "darwin":
        v = project.darwin_python_version
    else:
        v = project.python_version
    current_versions = (
        subprocess.check_output(["pyenv", "versions", "--bare"])
        .decode("utf-8")
        .splitlines()
    )
    if v not in current_versions:
        try:
            LOGGER.info(f"Try to install pyenv python {v}")
            subprocess.check_call(["pyenv", "install", v])
        except subprocess.CalledProcessError:
            LOGGER.info(f"Failed. Check for best alternative to pyenv python {v}")
            v = ".".join(project.python_version.split(".")[:-1])
            p, r, s = project.python_version.split(".")[:3]
            s = int(s)
            best_sub_version = None
            for candidate in current_versions:
                cp, cr, cs = candidate.split(".")[:3]
                if cp == p and cr == r:
                    cs = int(cs)
                    if cs >= s and best_sub_version is None or cs < best_sub_version:
                        best_sub_version = cs
            if best_sub_version is not None:
                v = f"{v}.{best_sub_version}"
                LOGGER.info(f"Found alternative to pyenv python {v}")
            else:
                LOGGER.info(f"Failed. Try to install fallback pyenv python {v}")
                output = subprocess.check_output(["pyenv", "install", v]).decode(
                    "utf-8"
                )
                match = VERSION_PATTERN.search(output)
                if match:
                    v = match.group("v")
                    LOGGER.info(f"Found pyenv python {v}")
                else:
                    LOGGER.info(f"Failed. Using current python version instead.")
    environ = dict(os.environ)
    environ[
        "PATH"
    ] = f'{Path(os.environ["PYENV_ROOT"], "versions", v, "bin")}:{os.environ["PATH"]}'
    LOGGER.info(f"Check for activated python version")
    output = (
        subprocess.check_output(["python", "--version"], env=environ)
        .decode("utf-8")
        .replace("\n", "")
    )
    if not output.endswith(v):
        raise OSError(
            f"Python version {v} not set, because current version is {output}"
        )
    LOGGER.info(f"Using pyenv python {v}")
    return environ


def __update_env__(environ: Environment):
    subprocess.check_call(
        ["python", "-m", "pip", "install", "--upgrade", "pip"], env=environ
    )
    subprocess.check_call(
        ["python", "-m", "pip", "install", "--upgrade", "setuptools"], env=environ
    )
    subprocess.check_call(
        ["python", "-m", "pip", "install", "--upgrade", "wheel"], env=environ
    )
    subprocess.check_call(
        ["python", "-m", "pip", "install", "--upgrade", "pytest"], env=environ
    )


def __activating_venv__(
    work_dir: Path, environ: Environment, verbose=True
) -> Environment:
    if verbose:
        LOGGER.setLevel(logging.INFO)
    else:
        LOGGER.setLevel(logging.WARNING)

    LOGGER.info("Activating virtual env")

    env_dir = work_dir / VENV
    environ["VIRTUAL_ENV"] = str(env_dir.absolute())
    environ["_OLD_VIRTUAL_PATH"] = environ["PATH"]
    environ["PATH"] = f'{(env_dir / "bin").absolute()}:{environ["PATH"]}'
    if "PYTHONHOME" in environ:
        environ["_OLD_VIRTUAL_PYTHONHOME"] = environ["PYTHONHOME"]
        del environ["PYTHONHOME"]
    if "VIRTUAL_ENV_DISABLE_PROMPT" not in environ:
        environ["_OLD_VIRTUAL_PS1"] = environ["PS1"] if "PS1" in environ else ""
        environ["PS1"] = f'({VENV}) {environ["PS1"] if "PS1" in environ else ""}'
        environ["VIRTUAL_ENV_PROMPT"] = f"({VENV})"
    return environ


def __create_venv__(work_dir, environ):
    env_dir = work_dir / VENV
    shutil.rmtree(env_dir, ignore_errors=True)
    LOGGER.info("Creating virtual env")
    subprocess.run(["python", "-m", "venv", env_dir], env=environ)
