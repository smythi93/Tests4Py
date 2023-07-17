import argparse
import configparser
import os

if __name__ == "__main__":
    arguments = argparse.ArgumentParser()

    arguments.add_argument("-w", dest="working_dir", required=True)
    arguments.add_argument("-c", dest="project_class", required=True)
    arguments.add_argument("-n", dest="number_of_bugs", required=True)

    args = arguments.parse_args()
    subjects = ""
    for i in range(int(args.number_of_bugs)):
        bug = i + 1
        if not os.path.exists(os.path.join(args.working_dir, f"{bug}")):
            continue
        print(f"Bug {bug}")
        subjects += f"    {args.project_class}(bug_id={bug},"
        config = configparser.ConfigParser()
        config.read(os.path.join(args.working_dir, f"{bug}", "bug.ini"))
        bug_section = config["bug"]
        subjects += f"buggy_commit_id={repr(bug_section['buggy_commit_id'])},"
        subjects += f"fixed_commit_id={repr(bug_section['fixed_commit_id'])},"
        test_file = list()
        for t in bug_section["test_file"].split(";"):
            test_file.append(f"Path({', '.join(map(repr, t.split('/')))})")
        subjects += f"test_file=[{', '.join(test_file)}],"
        tests = list()
        with open(os.path.join(args.working_dir, f"{bug}", "run_test.sh"), "r") as fp:
            for line in fp:
                tests.append(
                    line.replace("pytest ", "")
                    .replace("python -m unittest -q ", "")
                    .replace("\n", "")
                    .replace(" ", "")
                )
        subjects += f"test_cases={tests},)\n"
    print(subjects)
