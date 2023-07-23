import importlib.resources
from typing import List

from sflkit.analysis.suggestion import Location
from whatthepatch import parse_patch, exceptions

from tests4py.api.default import (
    checkout_project,
    compile_project,
    test_project,
    info_project,
)
from tests4py.framework.utils import __setup__
from tests4py.projects import (
    get_number_of_bugs,
    Project,
    get_matching_projects,
    resources,
)

__setup__()


def load_projects():
    for project in get_matching_projects():
        globals()[project.get_identifier()] = project


load_projects()


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
                if diff.header.old_path.startswith("test"):
                    continue
                new_counter = None
                offset = 0
                new_location = None
                alternative = None
                last_line_not_empty = None
                for change in diff.changes:
                    location = None
                    if change.new is None and change.old is not None:
                        if not isinstance(change.line, str) or change.line.strip():
                            location = Location(diff.header.old_path, change.old)
                    elif change.old is None and change.new is not None:
                        if new_counter is None or new_counter + 1 != change.new:
                            new_location = Location(
                                diff.header.old_path, change.new - offset
                            )
                            if (
                                last_line_not_empty is not None
                                and last_line_not_empty == change.new - offset - 1
                            ):
                                alternative = Location(
                                    diff.header.old_path, last_line_not_empty
                                )
                        new_counter = change.new
                    if change.new is not None and change.old is not None:
                        offset = change.new - change.old
                    if (
                        new_location is not None
                        and change.old is not None
                        and new_location.line == change.old
                        and isinstance(change.line, str)
                        and change.line.strip()
                        and not change.line.strip().startswith("#")
                    ):
                        if new_location not in locations:
                            locations.append(new_location)
                        new_location = None
                        alternative = None
                    elif (
                        alternative is not None
                        and change.old is not None
                        and new_location.line >= change.old
                    ):
                        if alternative not in locations:
                            locations.append(alternative)
                        new_location = None
                        alternative = None

                    if location is not None and location not in locations:
                        locations.append(location)
                    if (
                        change.old
                        and change.line.strip()
                        and not change.line.strip().startswith("#")
                    ):
                        last_line_not_empty = change.old
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
