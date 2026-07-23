"""CLI handlers for the optional Docker backend (``t4p docker ...``)."""

from typing import List, Optional

from tests4py.api import docker
from tests4py.api.report import DockerReport


def tests4py_docker_env(
    default_python: str = "3.10.9", verbose: bool = True
) -> DockerReport:
    return docker.build_env(default_python=default_python, verbose=verbose)


def tests4py_docker_project(
    project_name: str, warm_bug: int = 1, verbose: bool = True
) -> DockerReport:
    return docker.build_project(project_name, warm_bug=warm_bug, verbose=verbose)


def tests4py_docker_instance(
    project_name: str, bug_id: int, verbose: bool = True
) -> DockerReport:
    return docker.build_instance(project_name, bug_id, verbose=verbose)


def tests4py_docker_run(
    project_name: str,
    bug_id: int,
    command: Optional[List[str]] = None,
    verbose: bool = True,
) -> DockerReport:
    return docker.run_slice(project_name, bug_id, command=command, verbose=verbose)


def tests4py_docker_mode(mode: str) -> DockerReport:
    return docker.set_mode(mode)
