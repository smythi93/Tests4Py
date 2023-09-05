import importlib
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Callable

from tests4py.constants import (
    Environment,
    VERSION_PATTERN,
    VENV,
    PYENV,
    PYENV_ROOT,
    PYENV_TMP,
    PYTHON,
)
from tests4py.logger import LOGGER
from tests4py.projects import Project

DEFAULT_RUN = subprocess.run
DEFAULT_CHECK_CALL = subprocess.check_call
DEFAULT_CHECK_OUTPUT = subprocess.check_output
DEFAULT_POPEN = subprocess.Popen


def __install_version__(project: Project):
    LOGGER.info(f"Checking for platform {sys.platform}")
    if sys.platform == "darwin":
        v = project.darwin_python_version
    else:
        v = project.python_version
    current_versions = (
        subprocess.check_output([PYENV, "versions", "--bare"])
        .decode("utf-8")
        .splitlines()
    )
    LOGGER.debug(f"Versions: {current_versions}")
    if v not in current_versions:
        try:
            LOGGER.info(f"Try to install pyenv python {v}")
            subprocess.check_output([PYENV, "install", v], input=b"\n" * 10)
            return v
        except subprocess.CalledProcessError:  #
            pass
        if project.python_version and v != project.python_fallback_version:
            LOGGER.info(f"Failed. Check for fallback version to pyenv python {v}")
            try:
                LOGGER.info(
                    f"Try to install pyenv python {project.python_fallback_version}"
                )
                subprocess.check_output(
                    ["pyenv", "install", project.python_fallback_version],
                    input=b"\n" * 10,
                )
                return v
            except subprocess.CalledProcessError:
                pass
        LOGGER.info(f"Failed. Check for best alternative to pyenv python {v}")
        p, r, s = project.python_version.split(".")[:3]
        r = int(r)
        s = int(s)
        best_r = None
        best_s = None
        for candidate in current_versions:
            cp, cr, cs = candidate.split(".")[:3]
            if cp == p:
                cr = int(cr)
                if cr > r:
                    if best_r is None or cr < best_r or (cr == best_r and cs < best_s):
                        best_r = cr
                        best_s = cs
                elif cr == r:
                    cs = int(cs)
                    if cs >= s and (best_s is None or cs < best_s):
                        best_r = cr
                        best_s = cs
        if best_r and best_s:
            v = f"{p}.{best_r}.{best_s}"
            LOGGER.info(f"Found alternative to pyenv python {v}")
            return v
        v = f"{p}.{r}"
        LOGGER.info(f"Failed. Try to install fallback pyenv python {v}")
        try:
            output = subprocess.check_output(
                [PYENV, "install", v], input=b"\n" * 10
            ).decode("utf-8")
            match = VERSION_PATTERN.search(output)
            if match:
                v = match.group("v")
                LOGGER.info(f"Found pyenv python {v}")
                return v
            else:
                LOGGER.info(f"Failed. Using latest python version instead.")
                return current_versions[-1]
        except subprocess.CalledProcessError:
            LOGGER.info(f"Failed. Using latest python version instead.")
            return current_versions[-1]
    else:
        return v


def __install_pyenv__() -> str:
    if sys.platform.startswith("win"):
        shutil.rmtree(PYENV_TMP, ignore_errors=True)
        subprocess.check_call(
            [
                "git",
                "clone",
                "https://github.com/pyenv-win/pyenv-win.git",
                PYENV_TMP,
            ]
        )
        shutil.rmtree(PYENV_ROOT, ignore_errors=True)
        shutil.move(PYENV_TMP / "pyenv-win", PYENV_ROOT, copy_function=shutil.copytree)
        shutil.rmtree(PYENV_TMP, ignore_errors=True)
    else:
        process = subprocess.check_output(["curl", "https://pyenv.run"])
        subprocess.check_call(["bash"], stdin=process)


# Windows stuff


def set_shell(call: Callable, *args, **kwargs):
    kwargs["shell"] = True
    return call(*args, **kwargs)


def activate_shell_run(*args, **kwargs):
    return set_shell(DEFAULT_RUN, *args, **kwargs)


def activate_shell_check_call(*args, **kwargs):
    return set_shell(DEFAULT_CHECK_CALL, *args, **kwargs)


def activate_shell_check_output(*args, **kwargs):
    return set_shell(DEFAULT_CHECK_OUTPUT, *args, **kwargs)


class ActivateShellPopen(DEFAULT_POPEN):
    def __init__(self, *args, **kwargs):
        kwargs["shell"] = True
        super().__init__(*args, **kwargs)


def __env_on__(project: Project, skip=False) -> Environment:
    if sys.platform.startswith("win") or (
        sys.platform.startswith("darwin") and platform.processor().startswith("arm")
    ):
        LOGGER.debug("Activate chell for subprocess")
        importlib.reload(subprocess)
        subprocess.run = activate_shell_run
        subprocess.check_call = activate_shell_check_call
        subprocess.check_output = activate_shell_check_output
        subprocess.Popen = ActivateShellPopen

    environ = os.environ.copy()
    if skip:
        return environ
    LOGGER.debug(f"Before: {environ}")
    v = __install_version__(project)

    python_root = PYENV_ROOT / "versions" / v
    if sys.platform.startswith("win"):
        sep = ";"
    else:
        python_root /= "bin"
        sep = ":"
    environ["PATH"] = f'{python_root}{sep}{environ["PATH"]}'
    LOGGER.info(f"Check for activated python version")
    LOGGER.debug(f"Dir: {python_root}")
    LOGGER.debug(f"Dir: {os.listdir(PYENV_ROOT / 'versions')}")
    LOGGER.debug(f"Dir: {python_root}")
    LOGGER.debug(f"After: {environ}")
    output = __get_python_version__(environ)
    LOGGER.debug(f"Version: {output}")
    if v not in output:
        raise OSError(
            f"Python version {v} not set, because current version is {output}"
        )
    LOGGER.info(f"Using pyenv python {v}")
    return environ


def __get_python_version__(environ: Environment):
    return (
        subprocess.check_output([PYTHON, "--version"], env=environ)
        .decode("utf-8")
        .replace("\n", "")
    )


def __update_env__(environ: Environment):
    subprocess.check_call(
        [PYTHON, "-m", "pip", "install", "--upgrade", "pip"], env=environ
    )
    subprocess.check_call(
        [PYTHON, "-m", "pip", "install", "--upgrade", "setuptools"],
        env=environ,
    )
    subprocess.check_call(
        [PYTHON, "-m", "pip", "install", "--upgrade", "wheel"], env=environ
    )
    subprocess.check_call(
        [PYTHON, "-m", "pip", "install", "--upgrade", "pytest"],
        env=environ,
    )


def __sflkit_env__(environ: Environment):
    subprocess.check_call(
        [PYTHON, "-m", "pip", "install", "sflkitlib==0.0.1"],
        env=environ,
    )


def __activate_venv__(work_dir: Path, environ: Environment) -> Environment:
    LOGGER.info("Activating virtual env")

    env_dir = work_dir / VENV
    environ["VIRTUAL_ENV"] = str(env_dir.absolute())
    environ["_OLD_VIRTUAL_PATH"] = environ["PATH"]
    if sys.platform.startswith("win"):
        environ["PATH"] = f'{(env_dir / "Scripts").absolute()};{environ["PATH"]}'
    else:
        environ["PATH"] = f'{(env_dir / "bin").absolute()}:{environ["PATH"]}'
    if "PYTHONHOME" in environ:
        environ["_OLD_VIRTUAL_PYTHONHOME"] = environ["PYTHONHOME"]
        del environ["PYTHONHOME"]
    if "VIRTUAL_ENV_DISABLE_PROMPT" not in environ:
        environ["_OLD_VIRTUAL_PS1"] = environ["PS1"] if "PS1" in environ else ""
        environ["PS1"] = f'({VENV}) {environ["PS1"] if "PS1" in environ else ""}'
        environ["VIRTUAL_ENV_PROMPT"] = f"({VENV})"
    output = __get_python_version__(environ)
    LOGGER.debug(f"Venv version: {output}")
    return environ


def __create_venv__(work_dir, environ):
    env_dir = work_dir / VENV
    shutil.rmtree(env_dir, ignore_errors=True)
    LOGGER.info("Creating virtual env")
    subprocess.check_call([PYTHON, "-m", "venv", env_dir], env=environ)
