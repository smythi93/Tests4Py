import os
import subprocess

import tests4py.api as t4p
from tests4py.projects import Project


def loc(project: Project):
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
    return project


def main():
    projects = list()
    t4p.logging.error()
    for project in t4p.get_projects():
        project.buggy = True
        try:
            project = loc(project)
        except:
            pass
        else:
            projects.append(project)
            print(f"{project.get_identifier():<40}: {project.loc:>10}")
    with open("cloc.txt", "w") as fp:
        for project in projects:
            fp.write(f"{project.get_identifier():<40}: {project.loc:>10}\n")


if __name__ == "__main__":
    main()
