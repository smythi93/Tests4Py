import argparse
import json
import os.path
import time
import traceback

from sflkit.runners import Runner

import tests4py.api as t4p
from tests4py import sfl


def main(project_name, bug_id):
    report = dict()
    os.makedirs("mappings", exist_ok=True)
    for project in t4p.get_projects(project_name, bug_id):
        identifier = project.get_identifier()
        print(identifier)
        report[identifier] = dict()
        report[identifier]["time"] = dict()

        start = time.time()
        r = t4p.checkout(project)
        report[identifier]["time"]["checkout"] = time.time() - start
        if r.successful:
            report[identifier]["checkout"] = "successful"
        else:
            report[identifier]["checkout"] = "failed"
            report[identifier]["error"] = traceback.format_exception(r.raised)
            continue

        mapping = os.path.join("mappings", f"{project}.json")
        sfl_path = os.path.join("tmp", f"sfl_{identifier}")
        start = time.time()
        r = sfl.sflkit_instrument(sfl_path, project, mapping=mapping)
        report[identifier]["time"]["instrument"] = time.time() - start
        if r.successful:
            report[identifier]["build"] = "successful"
        else:
            report[identifier]["build"] = "failed"
            report[identifier]["error"] = traceback.format_exception(r.raised)
            continue

        with open(mapping, "r") as f:
            mapping_content = json.load(f)
        with open(mapping, "w") as f:
            json.dump(mapping_content, f, indent=2)

        start = time.time()
        r = sfl.sflkit_unittest(
            sfl_path, relevant_tests=True, all_tests=False, include_suffix=True
        )
        report[identifier]["time"]["test"] = time.time() - start
        if r.successful:
            report[identifier]["test"] = "successful"
        else:
            report[identifier]["test"] = "failed"
            report[identifier]["error"] = traceback.format_exception(r.raised)
            continue

        project.buggy = False
        start = time.time()
        r = t4p.checkout(project)
        report[identifier]["time"]["checkout_fixed"] = time.time() - start
        if r.successful:
            report[identifier]["checkout_fixed"] = "successful"
        else:
            report[identifier]["checkout_fixed"] = "failed"
            report[identifier]["error"] = traceback.format_exception(r.raised)
            continue

        mapping = os.path.join("mappings", f"{project}.json")
        start = time.time()
        r = sfl.sflkit_instrument(sfl_path, project, mapping=mapping)
        report[identifier]["time"]["instrument_fixed"] = time.time() - start
        if r.successful:
            report[identifier]["build_fixed"] = "successful"
        else:
            report[identifier]["build_fixed"] = "failed"
            report[identifier]["error"] = traceback.format_exception(r.raised)
            continue

        with open(mapping, "r") as f:
            mapping_content = json.load(f)
        with open(mapping, "w") as f:
            json.dump(mapping_content, f, indent=2)

        start = time.time()
        r = sfl.sflkit_unittest(
            sfl_path, relevant_tests=False, all_tests=False, include_suffix=True
        )
        report[identifier]["time"]["test_fixed"] = time.time() - start
        if r.successful:
            report[identifier]["test_fixed"] = "successful"
        else:
            report[identifier]["test_fixed"] = "failed"
            report[identifier]["error"] = traceback.format_exception(r.raised)
            continue

        checks = True
        events_base = os.path.join(
            "sflkit_events", project.project_name, str(project.bug_id)
        )
        bug_events = os.path.join(events_base, "bug")
        fix_events = os.path.join(events_base, "fix")
        for failing_test in project.test_cases:
            safe_test = Runner.safe(failing_test)
            if not os.path.exists(os.path.join(bug_events, "failing", safe_test)):
                report[identifier][f"bug:{failing_test}"] = "not_found"
                checks = False
            if not os.path.exists(os.path.join(fix_events, "passing", safe_test)):
                report[identifier][f"fix:{failing_test}"] = "not_found"
                checks = False
        if not os.listdir(os.path.join(bug_events, "passing")):
            report[identifier]["bug_passing"] = "empty"
            checks = False

        if checks:
            report[identifier]["check"] = "successful"
        else:
            report[identifier]["check"] = "failed"

    with open(f"report_{project_name}.json", "w") as f:
        json.dump(report, f, indent=2)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("-p", required=True, dest="project_name", help="project name")
    args.add_argument("-i", default=None, dest="bug_id", help="bug_id")

    arguments = args.parse_args()
    name = arguments.project_name
    id_ = arguments.bug_id
    if id_ is not None:
        id_ = int(id_)

    main(name, id_)
