import argparse
import os
import subprocess

import tests4py.api as t4p
from tests4py.projects import Project


def main(project: Project):
    project.buggy = True
    report = t4p.checkout(project)
    if report.raised:
        raise RuntimeError(
            f"bug: checkout of {project.get_identifier()}", report.raised
        )
    cloc = (
        ["cloc", "--include-lang=Python"]
        + (
            [
                "--fullpath",
                "--not-match-d="
                + "|".join(
                    [os.path.join(report.location, s) for s in project.excluded_files]
                ),
            ]
            if project.excluded_files
            else []
        )
        + [os.path.join(report.location, s) for s in project.source_base]
    )
    lines = subprocess.run(
        cloc,
        stdout=subprocess.PIPE,
    )
    if lines.returncode != 0:
        raise RuntimeError(f"bug: cloc of {project.get_identifier()}")
    if b"SUM" not in lines.stdout:
        project.loc = int(
            lines.stdout.split(b"Python")[1].split(b"\n")[0].split(b" ")[-1].strip()
        )
    else:
        project.loc = int(
            lines.stdout.split(b"SUM")[1].split(b"\n")[0].split(b" ")[-1].strip()
        )
    print(f"loc: {project.loc}")
    report = t4p.build(project)
    if report.raised:
        raise RuntimeError(f"bug: build of {project.get_identifier()}", report.raised)
    report = t4p.test(project, relevant_tests=True)
    if report.raised:
        raise RuntimeError(f"bug: test of {project.get_identifier()}", report.raised)
    if not report.failing:
        raise RuntimeError(f"bug: no failing tests for {project.get_identifier()}")
    if not report.passing:
        raise RuntimeError(f"bug: no passing tests for {project.get_identifier()}")

    project.buggy = False
    report = t4p.checkout(project)
    if report.raised:
        raise RuntimeError(
            f"fix: checkout of {project.get_identifier()}", report.raised
        )
    report = t4p.build(project)
    if report.raised:
        raise RuntimeError(f"fix: build of {project.get_identifier()}", report.raised)
    report = t4p.test(project, relevant_tests=True)
    if report.raised:
        raise RuntimeError(f"fix: test of {project.get_identifier()}", report.raised)
    if report.failing:
        raise RuntimeError(f"fix: failing tests for {project.get_identifier()}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-p", required=True, dest="project_name", help="project name")
    parser.add_argument("-i", required=True, dest="bug_id", help="bug_id", type=int)

    args = parser.parse_args()

    projects = t4p.get_projects(args.project_name, args.bug_id)
    if projects and len(projects) == 1:
        main(projects[0])
    else:
        raise RuntimeError(f"no project found {args.project_name}_{args.bug_id}")
