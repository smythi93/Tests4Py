"""Optional containerised backend for Tests4Py.

Everything here is *additive*: the default host/pyenv backend is untouched and
this module is only exercised through ``t4p docker ...`` or when
``config.mode == "docker"``. It drives a layered image build

    environment image  (tests4py-env)          -- OS + pyenv + Tests4Py
        -> project image (tests4py-project-<p>) -- one bug warmed, deps cached
            -> instance image (tests4py-instance-<p>-<b>) -- one bug ready to run

so that the expensive layers (toolchain, interpreter, dependencies) are built
once and reused by Docker's layer cache across bugs.

The functions shell out to the ``docker`` CLI; they never import a Docker SDK so
there is no new dependency. Each returns a :class:`DockerReport`.
"""

import os
import subprocess
from pathlib import Path
from typing import List, Optional, Sequence

from tests4py.api.config import config_set, load_config
from tests4py.api.report import DockerReport
from tests4py.constants import (
    DOCKER_ENV,
    DOCKER_INSTANCE,
    DOCKER_MODE,
    DOCKER_PROJECT,
    DOCKER_RUN,
)
from tests4py.logger import LOGGER

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ image naming ~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

ENV_IMAGE = "tests4py-env:latest"


def project_image(project_name: str) -> str:
    return f"tests4py-project-{project_name}:latest"


def instance_image(project_name: str, bug_id: int) -> str:
    return f"tests4py-instance-{project_name}-{bug_id}:latest"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ helpers ~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


def repo_root() -> Path:
    """Repository root (the Docker build context for the env image).

    Walks up from this package until a ``pyproject.toml`` is found. Works for an
    editable/source install; for a wheel install pass an explicit ``context``.
    """
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "pyproject.toml").exists():
            return parent
    # Fall back to <site-packages>/tests4py/.. two levels up from this file.
    return here.parent.parent.parent


def docker_available(timeout: float = 8.0) -> bool:
    """True iff the ``docker`` CLI exists and its daemon answers quickly."""
    from shutil import which

    if which("docker") is None:
        return False
    try:
        subprocess.run(
            ["docker", "version", "--format", "{{.Server.Version}}"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=timeout,
            check=True,
        )
        return True
    except (subprocess.SubprocessError, OSError):
        return False


def image_exists(tag: str) -> bool:
    try:
        return (
            subprocess.run(
                ["docker", "image", "inspect", tag],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            ).returncode
            == 0
        )
    except OSError:
        return False


def _dockerfile(name: str) -> Path:
    from tests4py.docker import (
        DOCKERFILE_ENV,
        DOCKERFILE_INSTANCE,
        DOCKERFILE_PROJECT,
    )

    return {
        "env": DOCKERFILE_ENV,
        "project": DOCKERFILE_PROJECT,
        "instance": DOCKERFILE_INSTANCE,
    }[name]


def _run(
    cmd: Sequence[str], report: DockerReport, verbose: bool = False
) -> DockerReport:
    LOGGER.info("docker: %s", " ".join(str(c) for c in cmd))
    try:
        proc = subprocess.run(
            list(cmd),
            stdout=None if verbose else subprocess.DEVNULL,
            stderr=None if verbose else subprocess.STDOUT,
        )
        report.returncode = proc.returncode
        report.successful = proc.returncode == 0
        if not report.successful:
            report.raised = RuntimeError(
                f"`{' '.join(str(c) for c in cmd[:3])} ...` exited with "
                f"{proc.returncode}"
            )
    except BaseException as e:  # noqa: BLE001 -- surfaced via report.raised
        report.raised = e
        report.successful = False
    return report


def _guard_available(report: DockerReport) -> bool:
    if docker_available():
        return True
    report.successful = False
    report.raised = RuntimeError(
        "Docker is not available (the `docker` CLI is missing or its daemon is "
        "not running). Start Docker and retry, or use the default pyenv backend."
    )
    return False


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ image builds ~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


def build_env(
    tag: str = ENV_IMAGE,
    context: Optional[os.PathLike] = None,
    default_python: str = "3.10.9",
    verbose: bool = False,
    report: Optional[DockerReport] = None,
) -> DockerReport:
    """Build the reusable environment image (OS + pyenv + Tests4Py)."""
    report = report or DockerReport(DOCKER_ENV)
    if not _guard_available(report):
        return report
    context = Path(context) if context else repo_root()
    cmd = [
        "docker",
        "build",
        "-f",
        str(_dockerfile("env")),
        "--build-arg",
        f"DEFAULT_PYTHON={default_python}",
        "-t",
        tag,
        str(context),
    ]
    _run(cmd, report, verbose=verbose)
    report.image = tag if report.successful else None
    return report


def build_project(
    project_name: str,
    warm_bug: int = 1,
    env_image: str = ENV_IMAGE,
    tag: Optional[str] = None,
    context: Optional[os.PathLike] = None,
    build_env_if_missing: bool = True,
    verbose: bool = False,
    report: Optional[DockerReport] = None,
) -> DockerReport:
    """Build a project image warmed by one representative bug."""
    report = report or DockerReport(DOCKER_PROJECT)
    if not _guard_available(report):
        return report
    if build_env_if_missing and not image_exists(env_image):
        env_report = build_env(tag=env_image, context=context, verbose=verbose)
        if not env_report.successful:
            report.successful = False
            report.raised = env_report.raised
            return report
    tag = tag or project_image(project_name)
    context = Path(context) if context else repo_root()
    cmd = [
        "docker",
        "build",
        "-f",
        str(_dockerfile("project")),
        "--build-arg",
        f"ENV_IMAGE={env_image}",
        "--build-arg",
        f"PROJECT={project_name}",
        "--build-arg",
        f"WARM_BUG={warm_bug}",
        "-t",
        tag,
        str(context),
    ]
    _run(cmd, report, verbose=verbose)
    report.image = tag if report.successful else None
    return report


def build_instance(
    project_name: str,
    bug_id: int,
    project_img: Optional[str] = None,
    tag: Optional[str] = None,
    context: Optional[os.PathLike] = None,
    build_project_if_missing: bool = True,
    warm_bug: int = 1,
    verbose: bool = False,
    report: Optional[DockerReport] = None,
) -> DockerReport:
    """Build an instance image for one specific bug, ready to run."""
    report = report or DockerReport(DOCKER_INSTANCE)
    if not _guard_available(report):
        return report
    project_img = project_img or project_image(project_name)
    if build_project_if_missing and not image_exists(project_img):
        proj_report = build_project(
            project_name,
            warm_bug=warm_bug,
            tag=project_img,
            context=context,
            verbose=verbose,
        )
        if not proj_report.successful:
            report.successful = False
            report.raised = proj_report.raised
            return report
    tag = tag or instance_image(project_name, bug_id)
    context = Path(context) if context else repo_root()
    cmd = [
        "docker",
        "build",
        "-f",
        str(_dockerfile("instance")),
        "--build-arg",
        f"PROJECT_IMAGE={project_img}",
        "--build-arg",
        f"PROJECT={project_name}",
        "--build-arg",
        f"BUG={bug_id}",
        "-t",
        tag,
        str(context),
    ]
    _run(cmd, report, verbose=verbose)
    report.image = tag if report.successful else None
    return report


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ run a slice ~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


def run_slice(
    project_name: str,
    bug_id: int,
    command: Optional[List[str]] = None,
    build_if_missing: bool = True,
    docker_run_args: Optional[List[str]] = None,
    verbose: bool = True,
    report: Optional[DockerReport] = None,
) -> DockerReport:
    """Run a Tests4Py command inside a bug's instance container.

    ``command`` is the ``t4p`` argument vector (default: run the failing tests).
    Example: ``run_slice("middle", 1, ["systemtest", "generate", "-n", "4"])``.
    """
    report = report or DockerReport(DOCKER_RUN)
    if not _guard_available(report):
        return report
    tag = instance_image(project_name, bug_id)
    if not image_exists(tag):
        if not build_if_missing:
            report.successful = False
            report.raised = RuntimeError(
                f"Instance image {tag} not found (build it first with "
                f"`t4p docker instance -p {project_name} -i {bug_id}`)."
            )
            return report
        inst = build_instance(project_name, bug_id, verbose=verbose)
        if not inst.successful:
            report.successful = False
            report.raised = inst.raised
            return report
    work = f"/work/{project_name}_{bug_id}"
    t4p_cmd = command or ["test", "-w", work]
    cmd = (
        ["docker", "run", "--rm"]
        + (docker_run_args or [])
        + [tag, "t4p"]
        + t4p_cmd
    )
    _run(cmd, report, verbose=verbose)
    report.image = tag
    return report


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ mode toggle ~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


def set_mode(mode: str, report: Optional[DockerReport] = None) -> DockerReport:
    """Persist the execution backend (``pyenv`` or ``docker``)."""
    report = report or DockerReport(DOCKER_MODE)
    if mode not in ("pyenv", "docker"):
        report.successful = False
        report.raised = ValueError(f"mode must be 'pyenv' or 'docker', got {mode!r}")
        return report
    config_set("mode", mode)
    report.successful = True
    return report


def current_mode() -> str:
    return load_config().mode
