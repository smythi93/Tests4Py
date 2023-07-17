import importlib.resources

from whatthepatch import parse_patch, exceptions
from sflkit.analysis.suggestion import Location

from tests4py.api.default import (
    checkout_project,
    compile_project,
    test_project,
    info_project,
)

from typing import List

from tests4py.framework.utils import __setup__
from tests4py.projects import (
    get_number_of_bugs,
    Project,
    get_matching_projects,
    resources,
)

__setup__()


def get_bugs(project_name: str) -> int:
    project_name = project_name.lower()
    return get_number_of_bugs(project_name)


def get_projects(project_name: str = None, bug_id: int = None) -> List[Project]:
    return get_matching_projects(project_name=project_name, bug_id=bug_id)


def get_faulty_lines(project: Project):
    locations = list()
    with importlib.resources.path(
        getattr(getattr(resources, project.project_name), f"bug_{project.bug_id}"),
        "fix.patch",
    ) as resource:
        try:
            with open(resource, "r") as fp:
                s = fp.read()
            for diff in parse_patch(s):
                last = None
                for change in diff.changes:
                    if change.old is None:
                        if last is None:
                            last = change.new
                    else:
                        last = change.old
                    location = Location(diff.header.old_path, last)
                    if location not in locations:
                        locations.append(location)
        except (IOError, exceptions.WhatThePatchException):
            pass
    return locations


__all__ = [
    "get_bugs",
    "get_projects",
    "get_faulty_lines",
    "checkout_project",
    "compile_project",
    "test_project",
    "info_project",
]
