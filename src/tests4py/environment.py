import importlib
import os
import shutil
import subprocess
import sys
from pathlib import Path

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


def install_version(project: Project):
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


def install_pyenv() -> str:
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


class ActivateShellPopen(DEFAULT_POPEN):
    @staticmethod
    def _replace_args(args):
        return [
            (
                arg.replace("<", "^<").replace(">", "^>")
                if isinstance(arg, str) and ("<" in arg or ">" in arg)
                else arg
            )
            for arg in args
        ]

    def __init__(self, *args, **kwargs):
        if "args" in kwargs:
            kwargs["args"] = self._replace_args(kwargs["args"])
        else:
            args = [self._replace_args(args[0])] + list(args[1:])
        kwargs["shell"] = True
        super().__init__(*args, **kwargs)


def env_on(project: Project, skip=False) -> Environment:
    if sys.platform.startswith("win"):
        LOGGER.debug("Activate chell for subprocess")
        importlib.reload(subprocess)
        subprocess.Popen = ActivateShellPopen

    environ = os.environ.copy()
    if skip:
        return environ
    LOGGER.debug(f"Before: {environ}")
    v = install_version(project)

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
    output = get_python_version(environ)
    LOGGER.debug(f"Version: {output}")
    if v not in output:
        raise OSError(
            f"Python version {v} not set, because current version is {output}"
        )
    LOGGER.info(f"Using pyenv python {v}")
    return environ


def get_python_version(environ: Environment):
    return (
        subprocess.check_output([PYTHON, "--version"], env=environ)
        .decode("utf-8")
        .replace("\n", "")
    )


def update_env(environ: Environment, force: bool = False):
    install = [PYTHON, "-m", "pip", "install"]
    # if force:
    install.append("--upgrade")
    subprocess.check_call(
        install + ["pip"],
        env=environ,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    subprocess.check_call(
        install + ["setuptools"],
        env=environ,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    subprocess.check_call(
        install + ["wheel"],
        env=environ,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    subprocess.check_call(
        install + ["pytest"],
        env=environ,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def sflkit_env(environ: Environment):
    subprocess.check_call(
        [PYTHON, "-m", "pip", "install", "sflkitlib>=0.0.5"],
        env=environ,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def activate_venv(work_dir: Path, environ: Environment) -> Environment:
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
    output = get_python_version(environ)
    LOGGER.debug(f"Venv version: {output}")
    return environ


def create_venv(work_dir, environ):
    env_dir = work_dir / VENV
    shutil.rmtree(env_dir, ignore_errors=True)
    LOGGER.info("Creating virtual env")
    subprocess.check_call([PYTHON, "-m", "venv", env_dir], env=environ)
