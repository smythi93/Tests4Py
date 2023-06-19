from tests4py.api.default import (
    checkout_project,
    compile_project,
    test_project,
    info_project,
)

from typing import List

from tests4py.framework.utils import __setup__
from tests4py.projects import get_number_of_bugs, Project, get_matching_projects

__setup__()


def get_bugs(project_name: str) -> int:
    project_name = project_name.lower()
    return get_number_of_bugs(project_name)


def get_projects(project_name: str = None, bug_id: int = None) -> List[Project]:
    return get_matching_projects(project_name=project_name, bug_id=bug_id)


__all__ = [
    "get_bugs",
    "get_projects",
    "checkout_project",
    "compile_project",
    "test_project",
    "info_project",
]
