import argparse
import os.path
import subprocess

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("-p", required=True, dest="project_name", help="project name")
    args.add_argument("-i", required=True, dest="bug_id", help="bug_id")

    arguments = args.parse_args()
    project_name = arguments.project_name
    bug_id = arguments.bug_id
    identifier = f"{project_name}_{bug_id}"

    subprocess.check_call(
        ["t4p", "checkout", "-p", project_name, "-i", bug_id],
    )
    subprocess.check_call(
        [
            "t4p",
            "sfl",
            "instrument",
            "-w",
            os.path.join("tmp", identifier),
            "-d",
            os.path.join("tmp", f"sfl_{identifier}"),
        ]
    )
    subprocess.check_call(
        [
            "t4p",
            "sfl",
            "events",
            "-w",
            os.path.join("tmp", f"sfl_{identifier}"),
        ]
    )
