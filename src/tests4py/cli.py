import argparse
import logging
import os
import subprocess
import sys
from pathlib import Path

from tests4py.framework import (
    unittest,
    systemtest,
)
from tests4py.framework.cache import tests4py_cache
from tests4py.framework.config import tests4py_config_set
from tests4py.framework.default import (
    tests4py_checkout,
    tests4py_compile,
    tests4py_test,
    tests4py_info,
)
from tests4py.constants import (
    CHECKOUT,
    COMPILE,
    # COVERAGE,
    INFO,
    # MUTATION,
    TEST,
    UNITTEST,
    SYSTEMTEST,
    GENERATE,
    CONFIG,
    CACHE,
    GRAMMAR,
    DEFAULT_WORK_DIR,
    DEFAULT_SUB_PATH_SYSTEMTESTS,
    DEFAULT_SUB_PATH_UNITTESTS,
)
from tests4py.framework.grammar import tests4py_grammar


def check_pyenv():
    try:
        _ = subprocess.check_output(["pyenv", "--version"])
    except FileNotFoundError:
        logging.error("Pyenv is not installed! Exiting.")
        sys.exit(-1)

    try:
        os.environ["PYENV_ROOT"]
    except KeyError:
        logging.error("Environment Variable PYENV_ROOT not set! Exiting.")
        sys.exit(-1)


def str_to_bool(s):
    if isinstance(s, bool):
        return s
    s = s.lower()
    if s in ("yes", "true", "t", "y", "1"):
        return True
    elif s in ("no", "false", "f", "n", "0"):
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean value expected.")


def main(*args: str, stdout=sys.stdout, stderr=sys.stderr):
    if "-O" in sys.argv:
        sys.argv.remove("-O")
        os.execl(sys.executable, sys.executable, "-O", *sys.argv)
        sys.exit(0)

    if stdout is not None:
        sys.stdout = stdout
    if stderr is not None:
        sys.stderr = stderr

    check_pyenv()

    arguments = argparse.ArgumentParser(
        description="The access point to the tests4py framework"
    )

    arguments.add_argument(
        "--report", dest="report", default=None, help="Output the report to a file"
    )

    # The subparsers
    commands = arguments.add_subparsers(
        help="The command of the tests4py framework to execute",
        dest="command",
        required=True,
    )
    checkout_parser = commands.add_parser(CHECKOUT, help="Check out a project")
    compile_parser = commands.add_parser(COMPILE, help="Compile a project")
    # coverage_parser = commands.add_parser(
    #    COVERAGE, help="Measure coverage of a project"
    # )
    info_parser = commands.add_parser(INFO, help="Get information of a project")
    # mutation_parser = commands.add_parser(MUTATION, help="Mutate a project")
    test_parser = commands.add_parser(TEST, help="Run tests on a project")
    unittest_parser = commands.add_parser(UNITTEST, help="The unittest subcommand")
    systemtest_parser = commands.add_parser(
        SYSTEMTEST, help="The systemtest subcommand"
    )
    config_parser = commands.add_parser(CONFIG, help="The config subcommand")
    cache_parser = commands.add_parser(CACHE, help="The cache subcommand")
    grammar_parser = commands.add_parser(GRAMMAR, help="The grammar subcommand")

    # Checkout
    checkout_parser.add_argument(
        "-p",
        dest="project_name",
        required=True,
        help="The name of the project for which a particular version shall be checked out. "
        "Run tests4py info to check available project",
    )
    checkout_parser.add_argument(
        "-i",
        dest="bug_id",
        type=int,
        required=True,
        help="The number of bug from project in tests4py. "
        "Run tests4py info to check bug id number",
    )
    checkout_parser.add_argument(
        "-r",
        "--repaired",
        dest="fixed",
        action="store_true",
        default=False,
        help="Set the flag to checkout the repaired version, without the flag the buggy version will be checked out",
    )
    checkout_parser.add_argument(
        "-w",
        dest="work_dir",
        default=DEFAULT_WORK_DIR,
        help="The working directory to which the buggy or fixed project version shall be checked out. The working "
        "directory has to be either empty or a previously used working directory. Default will be "
        f"({DEFAULT_WORK_DIR})",
    )
    checkout_parser.add_argument(
        "-u",
        dest="update",
        default=False,
        action="store_true",
        help="If set the project won't be checked out again if it already exists at the specified location but only "
        "the tests4py data will be updated",
    )
    checkout_parser.add_argument(
        "-f",
        dest="force",
        default=False,
        action="store_true",
        help="If set the command won't use any cached version, even if the global cache flag is set",
    )

    # Compile
    compile_parser.add_argument(
        "-w",
        dest="work_dir",
        default=None,
        help="The working directory to compile the project. "
        "Default will be the current directory",
    )
    compile_parser.add_argument(
        "-r",
        dest="recompile",
        default=False,
        action="store_true",
        help="Set to recompile the project from scratch",
    )
    compile_parser.add_argument(
        "-f",
        dest="force",
        default=False,
        action="store_true",
        help="If set the command won't use any cached version, even if the global cache flag is set",
    )

    # Coverage
    # coverage_parser.add_argument(
    #     "-w",
    #     dest="work_dir",
    #     required=True,
    #     help="The working directory to run the test. Default will be the current directory",
    # )
    # coverage_parser.add_argument(
    #     "-t",
    #     dest="single_test",
    #     default=None,
    #     help="Run coverage from single test case by input. "
    #     "Default will run coverage from test cases that relevant from bugs. "
    #     "Format for pytest: <test_file_path>::<test_method>. "
    #     "Format for unittest: <test_file_path_without.py>.<test_class>.<test_method> . "
    #     "Use tests4py info to get the information about the project",
    # )
    # coverage_parser.add_argument(
    #     "-a",
    #     dest="all_tests",
    #     default=False,
    #     action="store_true",
    #     help="Run coverage from all test cases in the project. "
    #     "Default will run coverage from test cases that relevant from bugs",
    # )
    # coverage_parser.add_argument(
    #     "-r",
    #     dest="relevant_tests",
    #     default=False,
    #     action="store_true",
    #     help="Run coverage from test cases that relevant from bugs (Default)",
    # )

    # Info
    info_parser.add_argument(
        "-p",
        dest="project_name",
        default=None,
        help="The id of the project for which the information shall be printed",
    )
    info_parser.add_argument(
        "-i",
        dest="bug_id",
        type=int,
        default=None,
        help="The bug number of the project_name for which the information shall be printed",
    )

    # Mutation
    # mutation_parser.add_argument(
    #     "-w",
    #     dest="work_dir",
    #     required=True,
    #     help="The working directory to run the test. Default will be the current directory",
    # )
    # mutation_parser.add_argument(
    #     "-t",
    #     dest="target",
    #     default=None,
    #     help="Target module or package to mutate. "
    #     "Default will be run mutation from test case and target that relevant from bugs",
    # )
    # mutation_parser.add_argument(
    #     "-u",
    #     dest="unit_test",
    #     default=None,
    #     help="Test class, test method, module or package with unit tests. "
    #     "Default will be run mutation from test case and target that relevant from bugs",
    # )
    # mutation_parser.add_argument(
    #     "-r",
    #     dest="relevant_tests",
    #     default=False,
    #     action="store_true",
    #     help="Run mutation from test case and target that relevant from bugs (Default)",
    # )

    # Test
    test_parser.add_argument(
        "-w",
        dest="work_dir",
        default=None,
        help="The working directory to run the test. Default will be the current directory",
    )
    test_parser.add_argument(
        "-t",
        dest="single_test",
        default=None,
        help="Run single test from input. Default will run the test case that are relevant for the bugs. "
        "Format for pytest: <test_file_path>::<test_method>. "
        "Format for unittest: <test_file_path_without.py>.<test_class>.<test_method>. "
        "Use tests4py info to get the information about the project",
    )
    test_parser.add_argument(
        "-a",
        dest="all_tests",
        default=False,
        action="store_true",
        help="Run all test case in the project. "
        "Default will run the test case that are relevant for the bugs",
    )
    test_parser.add_argument(
        "-o", dest="output", default=None, help="Output test results to file"
    )

    # unittest
    unittest_commands = unittest_parser.add_subparsers(
        help="The subcommand of the unittest to execute",
        dest="subcommand",
        required=True,
    )
    unittest_generate = unittest_commands.add_parser(
        GENERATE, help="Generate new unittests"
    )
    unittest_test = unittest_commands.add_parser(TEST, help="Run the unittests")

    # systemtest
    systemtest_commands = systemtest_parser.add_subparsers(
        help="The subcommand of the systemtest to execute",
        dest="subcommand",
        required=True,
    )
    systemtest_generate = systemtest_commands.add_parser(
        GENERATE, help="Generate new systemtests"
    )
    systemtest_test = systemtest_commands.add_parser(TEST, help="Run the systemtests")

    for is_systemtest, generate in enumerate((unittest_generate, systemtest_generate)):
        generate.add_argument(
            "-w",
            dest="work_dir",
            default=None,
            help="The working directory to run the test. Default will be the current directory",
        )
        default = (
            DEFAULT_SUB_PATH_SYSTEMTESTS
            if is_systemtest
            else DEFAULT_SUB_PATH_UNITTESTS
        )
        generate.add_argument(
            "-p",
            dest="path",
            default=None,
            help=f"The output path of the generated tests. Default will be ({default})",
        )
        generate.add_argument(
            "-n",
            dest="n",
            default=1,
            type=int,
            help="The number of generated tests. Default will be 1",
        )
        generate.add_argument(
            "-f",
            dest="p",
            default=1,
            type=float,
            help="The number or probability of generated failing tests. If the number is a "
            "probability (<1) it will get multiplied with -n to get the total number of "
            "failing tests. Default will be 1",
        )
        generate.add_argument(
            "--passing",
            dest="is_only_passing",
            default=False,
            action="store_true",
            help="Set to generate only passing tests (<=> -p == 0). Cannot be set when "
            "--failing is set",
        )
        generate.add_argument(
            "--failing",
            dest="is_only_failing",
            default=False,
            action="store_true",
            help="Set to generate only failing tests (<=> -p == -n). Cannot be set when "
            "--passing is set",
        )
        generate.add_argument(
            "-a",
            dest="append",
            default=False,
            action="store_true",
            help="Set to append the generated tests to the existing tests at -p",
        )
        generate.add_argument(
            "-v",
            dest="verify",
            default=False,
            action="store_true",
            help="Set to verify the generated tests",
        )

    for is_systemtest, test in enumerate((unittest_test, systemtest_test)):
        test.add_argument(
            "-w",
            dest="work_dir",
            default=None,
            help="The working directory to run the test. Default will be the current directory",
        )
        default = (
            DEFAULT_SUB_PATH_SYSTEMTESTS
            if is_systemtest
            else DEFAULT_SUB_PATH_UNITTESTS
        )
        test.add_argument(
            "-p",
            dest="path",
            default=None,
            help=f"The output path of the generated tests. Default will be (-w/"
            f"{default}) if -d is not set, otherwise only the diversity tests are executed",
        )
        test.add_argument(
            "-d",
            dest="diversity",
            default=False,
            action="store_true",
            help="Set to run diversity tests. When giving -p all tests in -p and the diversity tests are "
            "executed and",
        )
        test.add_argument(
            "-o", dest="output", default=None, help="Output test results to file"
        )

    # Config
    config_parser.add_argument("flag", help="The flag for setting the value")
    config_parser.add_argument(
        "value", type=str_to_bool, help="The value to set the flag"
    )

    # Cache
    cache_parser.add_argument(
        "-p",
        dest="project_name",
        default=None,
        help="The name of the project for which a particular version shall be cached. "
        "If no project name is given, the command will consider all projects for caching that have the specified "
        "bug_id",
    )
    cache_parser.add_argument(
        "-i",
        dest="bug_id",
        type=int,
        default=None,
        help="The id of a bug from the project in tests4py to cache. "
        "If no id is given all projects are considered for caching that have the specified project name",
    )
    cache_parser.add_argument(
        "-f",
        dest="force",
        default=False,
        action="store_true",
        help="If set the command won't use any cached version, even if the global cache flag is set",
    )

    # Grammar
    grammar_parser.add_argument(
        "-p",
        dest="project_name",
        required=True,
        help="The id of the project for which the grammar shall be given",
    )
    grammar_parser.add_argument(
        "-i",
        dest="bug_id",
        type=int,
        required=True,
        help="The bug number of the project_name for which the grammar shall be given",
    )
    grammar_parser.add_argument(
        "-g",
        dest="grammar_format",
        default="python",
        help="The output format for the grammar. Can be python, json, or antlr (default: python)",
    )
    grammar_parser.add_argument(
        "-o",
        dest="output",
        default=None,
        help="Output the grammar to the given file (default: grammar.[py|json|g4])",
    )

    args = arguments.parse_args(args or sys.argv[1:])

    if args.command == CHECKOUT:
        report = tests4py_checkout(
            project_name=args.project_name,
            bug_id=args.bug_id,
            fixed=args.fixed,
            work_dir=Path(args.work_dir).absolute(),
            update=args.update,
            force=args.force,
        )
    elif args.command == COMPILE:
        report = tests4py_compile(
            work_dir=Path(args.work_dir).absolute() if args.work_dir else None,
            recompile=args.recompile,
            force=args.force,
        )
    elif args.command == INFO:
        report = tests4py_info(
            project_name=args.project_name,
            bug_id=args.bug_id,
        )
    elif args.command == TEST:
        report = tests4py_test(
            work_dir=Path(args.work_dir).absolute() if args.work_dir else None,
            single_test=args.single_test,
            all_tests=args.all_tests,
            output=Path(args.output).absolute() if args.output else None,
        )
    elif args.command == UNITTEST or args.command == SYSTEMTEST:
        if args.command == UNITTEST:
            command = unittest
        else:
            command = systemtest
        if args.subcommand == TEST:
            report = command.tests4py_test(
                work_dir=Path(args.work_dir).absolute() if args.work_dir else None,
                path=Path(args.path).absolute() if args.path else None,
                diversity=args.diversity,
                output=Path(args.output).absolute() if args.output else None,
            )
        elif args.subcommand == GENERATE:
            report = command.tests4py_generate(
                work_dir=Path(args.work_dir).absolute() if args.work_dir else None,
                path=Path(args.path).absolute() if args.path else None,
                n=args.n,
                p=args.p,
                is_only_passing=args.is_only_passing,
                is_only_failing=args.is_only_failing,
                append=args.append,
                verify=args.verify,
            )
        else:
            raise NotImplementedError(
                f"Subcommand {args.subcommand} not implemented for command {args.command}"
            )
    elif args.command == CONFIG:
        report = tests4py_config_set(name=args.flag, value=args.value)
    elif args.command == CACHE:
        report = tests4py_cache(
            project_name=args.project_name, bug_id=args.bug_id, force=args.force
        )
    elif args.command == GRAMMAR:
        report = tests4py_grammar(
            project_name=args.project_name,
            bug_id=args.bug_id,
            grammar_format=args.grammar_format,
            output=Path(args.output).absolute() if args.output else None,
        )
    else:
        raise NotImplementedError(f"Command {args.command} not implemented")

    if report.raised:
        raise report.raised


if __name__ == "__main__":
    if "-O" in sys.argv:
        sys.argv.remove("-O")
        os.execl(sys.executable, sys.executable, "-O", *sys.argv)
    else:
        main()
