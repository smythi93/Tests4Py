"""
This module provides the API for the Tests4Py package. The API provides the following functionalities:

checkout: Checkout the source code of a project.
build: Build the environment of a project.
test: Test a project with provided unit tests.
info: Get the information of a project.
run: Run a system test from a file or as a string.
systemtest_generate: Generate a system test for a project.
systemtest_test: Test a project with a system test.
unittest_generate: Generate a unit test for a project.
unittest_test: Test a project with a unit test.

Besides, the API provides the following utility functions:

get_bugs: Get the number of bugs in a project.
get_projects: Get the projects that match the provided criteria.
get_faulty_lines: Get the faulty lines in a project.
get_loc: Get the lines of code in a project.
get_tests: Get the tests of a project.
"""

import importlib.resources
from typing import List, Optional

from sflkit.analysis.suggestion import Location
from unidiff import PatchSet

from tests4py.api import logging
from tests4py.api.default import (
    checkout,
    build,
    test,
    info,
)
from tests4py.api.test import (
    run,
    get_tests,
    systemtest_generate,
    systemtest_test,
    unittest_generate,
    unittest_test,
)
from tests4py.api.utils import setup
from tests4py.projects import (
    get_number_of_bugs,
    Project,
    get_matching_projects,
    resources,
)

setup()


def load_projects():
    """
    Load all the projects.
    :return: None
    """
    for project in get_matching_projects():
        globals()[project.get_identifier()] = project


load_projects()


def get_bugs(project_name: str) -> int:
    """
    Get the number of bugs in a project.
    :param str project_name: The name of the project.
    :return int: The number of bugs in the project.
    """
    project_name = project_name.lower()
    return get_number_of_bugs(project_name)


def get_projects(
    project_name: Optional[str] = None, bug_id: Optional[int] = None
) -> List[Project]:
    """
    Get the projects that match the provided criteria.
    :param Optional[str] project_name: The name of the project.
    :param Optional[int] bug_id: The id of the bug.
    :return List[Project]: The projects that match the provided criteria.
    """
    return get_matching_projects(project_name=project_name, bug_id=bug_id)


def get_loc(project: Project) -> int:
    """
    Get the lines of code in a project.
    :param Project project: The project.
    :return int: The lines of code in the project.
    """
    return project.loc


class _BlankLine:
    """
    A utility class to represent a blank line.
    """

    def __init__(self):
        """
        Initialize the blank line.
        """
        self.is_added = False
        self.is_context = False
        self.is_removed = False
        self.source_line_no = 1


def get_faulty_lines(project: Project) -> List[Location]:
    """
    Get the faulty lines in a project.
    :param Project project: The project.
    :return List[Location]: The faulty lines in the project.
    """
    locations = list()
    project_resources = importlib.resources.files(
        getattr(getattr(resources, project.project_name), f"bug_{project.bug_id}")
    )
    with importlib.resources.as_file(
        project_resources.joinpath(
            "fix.patch",
        )
    ) as resource:
        try:
            with open(resource, "r") as fp:
                s = fp.read()
            for diff in PatchSet(s):
                if project.test_base:
                    if diff.path.startswith(str(project.test_base)):
                        continue
                for change in diff:
                    last_line_to_add = False
                    last_line = _BlankLine()
                    last_line_not_empty = _BlankLine()
                    for line in change:
                        if line.is_context:
                            if line.value.strip():
                                if last_line_to_add:
                                    locations.append(
                                        Location(diff.path, line.source_line_no)
                                    )
                                last_line_not_empty = line
                                last_line_to_add = False
                            elif last_line_to_add:
                                locations.append(
                                    Location(
                                        diff.path,
                                        last_line_not_empty.source_line_no,
                                    )
                                )
                                last_line_to_add = False
                        elif line.is_added:
                            if line.value.strip():
                                if last_line.is_removed:
                                    last_line_to_add = False
                                    if not last_line.value.strip():
                                        locations.append(
                                            Location(
                                                diff.path, last_line.source_line_no
                                            )
                                        )
                                elif last_line_not_empty.is_removed:
                                    last_line_to_add = False
                                else:
                                    last_line_to_add = True
                        elif line.is_removed:
                            if line.value.strip():
                                if last_line_not_empty.is_added:
                                    locations.append(
                                        Location(diff.path, line.source_line_no)
                                    )
                                last_line_to_add = False
                                last_line_not_empty = line
                                locations.append(
                                    Location(diff.path, line.source_line_no)
                                )
                        last_line = line
                    if last_line_to_add:
                        locations.append(
                            Location(diff.path, last_line_not_empty.source_line_no)
                        )
        except IOError:
            pass
    return locations


__all__ = [
    "get_bugs",
    "get_projects",
    "get_faulty_lines",
    "checkout",
    "build",
    "test",
    "info",
    "run",
    "systemtest_generate",
    "systemtest_test",
    "unittest_generate",
    "unittest_test",
    "logging",
    "get_tests",
]
