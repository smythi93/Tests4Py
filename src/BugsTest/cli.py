import argparse
import os
import sys
from pathlib import Path

from BugsTest import framework

CHECKOUT = 'checkout'
COMPILE = 'compile'
COVERAGE = 'coverage'
FUZZ = 'fuzz'
INFO = 'info'
MUTATION = 'mutation'
TEST = 'test'


def main(*args: str, stdout=sys.stdout, stderr=sys.stderr):
    if "-O" in sys.argv:
        sys.argv.remove("-O")
        os.execl(sys.executable, sys.executable, "-O", *sys.argv)
        sys.exit(0)

    arguments = argparse.ArgumentParser(description='The access point to the BugsTest framework')

    # The subparsers
    commands = arguments.add_subparsers(help='The command of the BugsTest framework to execute',
                                        dest='command', required=True)
    checkout_parser = commands.add_parser(CHECKOUT, help='Check out a project')
    compile_parser = commands.add_parser(COMPILE, help='Compile a project')
    coverage_parser = commands.add_parser(COVERAGE, help='Measure coverage of a project')
    fuzz_parser = commands.add_parser(FUZZ, help='Fuzz a project')
    info_parser = commands.add_parser(INFO, help='Get information of a project')
    mutation_parser = commands.add_parser(MUTATION, help='Mutate a project')
    test_parser = commands.add_parser(TEST, help='Run tests on a project')

    # Checkout
    checkout_parser.add_argument('-p', dest='project_name', required=True,
                                 help='The name of the project for which a particular version shall be checked out. '
                                      'Run bugstest info to check available project')
    checkout_parser.add_argument('-i', dest='bug_id', type=int, required=True,
                                 help='The number of bug from project in bugstest. '
                                      'Run bugstest info to check bug id number')
    checkout_parser.add_argument('-v', dest='version_id', type=int, default=1,
                                 help='The version id that shall be checked out (1 fixed, 0 buggy, default will be 1)')
    checkout_parser.add_argument('-w', dest='work_dir', default=framework.DEFAULT_WORK_DIR,
                                 help='The working directory to which the buggy or fixed project version shall be '
                                      'checked out. The working directory has to be either empty or a previously used '
                                      f'working directory. Default will be ({framework.DEFAULT_WORK_DIR})')

    # Compile
    compile_parser.add_argument('-w', dest='work_dir', required=True,
                                help='The working directory to compile the project. '
                                     'Default will be the current directory')

    # Coverage
    coverage_parser.add_argument('-w', dest='work_dir', required=True,
                                 help='The working directory to run the test. Default will be the current directory')
    coverage_parser.add_argument('-t', dest='single_test', default=None,
                                 help='Run coverage from single test case by input. '
                                      'Default will run coverage from test cases that relevant from bugs. '
                                      'Format for pytest: <test_file_path>::<test_method>. '
                                      'Format for unittest: <test_file_path_without.py>.<test_class>.<test_method> . '
                                      'Use bugstest info to get the information about the project')
    coverage_parser.add_argument('-a', dest='all_tests', default=False, action='store_true',
                                 help='Run coverage from all test cases in the project. '
                                      'Default will run coverage from test cases that relevant from bugs')
    coverage_parser.add_argument('-r', dest='relevant_tests', default=False, action='store_true',
                                 help='Run coverage from test cases that relevant from bugs (Default)')

    # Fuzz
    fuzz_parser.add_argument('-p', dest='project_name', required=True,
                             help='The name of the project from BugsTest')
    fuzz_parser.add_argument('-i', dest='bug_id', type=int, required=True,
                             help='The bug number from project in BugsTest')
    fuzz_parser.add_argument('-w', dest='work_dir', default='',
                             help='The working directory that the project has been checked out. '
                                  'Default will be the current directory.')

    # Info
    info_parser.add_argument('-p', dest='project_name', required=True,
                             help='The id of the project for which the information shall be printed')
    info_parser.add_argument('-i', dest='bug_id', type=int, required=True,
                             help='The bug number of the project_name for which the information shall be printed')

    # Mutation
    mutation_parser.add_argument('-w', dest='work_dir', required=True,
                                 help='The working directory to run the test. Default will be the current directory')
    mutation_parser.add_argument('-t', dest='target', default=None,
                                 help='Target module or package to mutate. '
                                      'Default will be run mutation from test case and target that relevant from bugs')
    mutation_parser.add_argument('-u', dest='unit_test', default=None,
                                 help='Test class, test method, module or package with unit tests. '
                                      'Default will be run mutation from test case and target that relevant from bugs')
    mutation_parser.add_argument('-r', dest='relevant_tests', default=False, action='store_true',
                                 help='Run mutation from test case and target that relevant from bugs (Default)')

    # Test
    test_parser.add_argument('-w', dest='work_dir', required=True,
                             help='The working directory to run the test. Default will be the current directory')
    test_parser.add_argument('-t', dest='single_test', default=None,
                             help='Run single test from input. Default will run the test case that relevant from bugs. '
                                  'Format for pytest: <test_file_path>::<test_method>. '
                                  'Format for unittest: <test_file_path_without.py>.<test_class>.<test_method> . '
                                  'Use bugstest info to get the information about the project')
    test_parser.add_argument('-a', dest='all_tests', default=False, action='store_true',
                             help='Run all test case in the project. '
                                  'Default will run the test case that relevant from bugs')
    test_parser.add_argument('-o', dest='output', default=None, help='Output test results to file')

    args = arguments.parse_args(args or sys.argv[1:])

    if args.command == CHECKOUT:
        framework.bugstest_checkout(project_name=args.project_name,
                                    bug_id=args.bug_id,
                                    version_id=args.version_id,
                                    work_dir=Path(args.work_dir).absolute())
    elif args.command == COMPILE:
        framework.bugstest_compile(work_dir=Path(args.work_dir).absolute())
    elif args.command == TEST:
        framework.bugstest_test(work_dir=Path(args.work_dir).absolute(),
                                single_test=args.single_test,
                                all_tests=args.all_tests,
                                output=Path(args.output) if args.output else None)
    else:
        raise NotImplementedError(f'Command {args.command} not implemented')


if __name__ == '__main__':
    if '-O' in sys.argv:
        sys.argv.remove('-O')
        os.execl(sys.executable, sys.executable, '-O', *sys.argv)
    else:
        main()
