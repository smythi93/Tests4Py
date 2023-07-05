import json
import traceback
from pathlib import Path

from tests4py.api import get_projects
from tests4py.api.default import checkout_project, compile_project, test_project
from tests4py.constants import DEFAULT_WORK_DIR
from tests4py.tests.utils import TestResult


def write(res):
    with open("tests.json", "w") as fp:
        json.dump(res, fp, indent=2)


if __name__ == "__main__":
    results = dict()
    projects = get_projects()
    for project in projects:
        project.buggy = True
        print(f"\n\n\n================ {project} ================")
        report = checkout_project(project)
        if not report.successful:
            print(f"Checkout failed:")
            traceback.print_exception(report.raised)
            input()
            results[project.get_identifier()] = None
            continue
        report = compile_project(DEFAULT_WORK_DIR / project.get_identifier())
        if not report.successful:
            print(f"Compile failed:")
            traceback.print_exception(report.raised)
            input()
            results[project.get_identifier()] = None
            continue
        report = test_project(
            DEFAULT_WORK_DIR / project.get_identifier(),
            xml_output=Path("tmp.xml"),
            single_test=[str(tf) for tf in project.test_file],
        )
        if not report.successful:
            print(f"Test failed:")
            traceback.print_exception(report.raised)
            input()
            results[project.get_identifier()] = None
            continue
        if report.results:
            results[project.get_identifier()] = {
                TestResult.PASSING.value: [],
                TestResult.FAILING.value: [],
                TestResult.UNDEFINED.value: [],
            }
            for test, result in report.results:
                results[project.get_identifier()][result.value].append(test)
        else:
            results[project.get_identifier()] = None
        write(results)
