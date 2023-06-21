import os
import shutil
import subprocess
import sys
from pathlib import Path

from tests4py.constants import Environment, VERSION_PATTERN, VENV
from tests4py.framework.logger import LOGGER
from tests4py.projects import Project


def __install_version__(project: Project):
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
            return v
        except subprocess.CalledProcessError:  #
            pass
        if project.python_version and v != project.python_fallback_version:
            LOGGER.info(f"Failed. Check for fallback version to pyenv python {v}")
            try:
                LOGGER.info(
                    f"Try to install pyenv python {project.python_fallback_version}"
                )
                subprocess.check_call(
                    ["pyenv", "install", project.python_fallback_version]
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
            output = subprocess.check_output(["pyenv", "install", v]).decode("utf-8")
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


def __env_on__(project: Project, skip=False) -> Environment:
    environ = dict(os.environ)
    if skip:
        return environ

    v = __install_version__(project)

    environ[
        "PATH"
    ] = f'{Path(os.environ["PYENV_ROOT"], "versions", v, "bin")}:{os.environ["PATH"]}'
    LOGGER.info(f"Check for activated python version")
    output = (
        subprocess.check_output(["python", "--version"], env=environ)
        .decode("utf-8")
        .replace("\n", "")
    )
    if v not in output:
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
        ["python", "-m", "pip", "install", "--upgrade", "setuptools"],
        env=environ,
    )
    subprocess.check_call(
        ["python", "-m", "pip", "install", "--upgrade", "wheel"], env=environ
    )
    subprocess.check_call(
        ["python", "-m", "pip", "install", "--upgrade", "pytest"],
        env=environ,
    )


def __activate_venv__(work_dir: Path, environ: Environment) -> Environment:
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
