import argparse
import os
from pathlib import Path

import tests4py.api as t4p
from tests4py.projects import Project, TestStatus
from tests4py.tests.utils import TestResult


class FoundError(Exception):
    pass


def main(project: Project):
    if project.test_status_buggy != TestStatus.FAILING:
        return  # skip
    project.buggy = True
    report = t4p.checkout(project)
    if report.raised:
        raise RuntimeError(
            f"bug: checkout of {project.get_identifier()}", report.raised
        )

    report = t4p.build(project)
    if report.raised:
        raise RuntimeError(f"bug: build of {project.get_identifier()}", report.raised)

    xml_output = Path(f"{project.get_identifier()}.xml").absolute()
    report = t4p.test(project, xml_output=xml_output)
    if report.raised:
        raise RuntimeError(f"bug: test of {project.get_identifier()}", report.raised)

    os.remove(xml_output)

    failing_tests = {t[0] for t in report.results if t[1] == TestResult.FAILING}
    if (
        len(project.test_cases) != len(failing_tests)
        or len(failing_tests) != len(set(report.results))
        or any(t not in failing_tests for t in project.test_cases)
    ):
        raise FoundError(
            f"found different tests for {project.get_identifier()}: {list(failing_tests)}"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-p", required=True, dest="project_name", help="project name")
    parser.add_argument("-i", dest="bug_id", help="bug_id", type=int, default=None)

    args = parser.parse_args()

    projects = t4p.get_projects(args.project_name, args.bug_id)
    results = dict()
    if projects:
        for p in projects:
            try:
                main(p)
            except Exception as e:
                results[p.get_identifier()] = str(e)
            else:
                results[p.get_identifier()] = "OK"
        with open(f"results_{args.project_name}.txt", "w") as f:
            for k, v in results.items():
                f.write(f"{k}: {v}\n")
    else:
        raise RuntimeError(f"no project found {args.project_name}_{args.bug_id}")
