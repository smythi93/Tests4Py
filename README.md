# Tests4Py

[![Python Version](https://img.shields.io/pypi/pyversions/tests4py)](https://pypi.org/project/tests4py/)
[![GitHub release](https://img.shields.io/github/v/release/smythi93/Tests4Py)](https://img.shields.io/github/v/release/smythi93/tests4py)
[![PyPI](https://img.shields.io/pypi/v/tests4py)](https://pypi.org/project/tests4py/)
[![Build Status](https://img.shields.io/github/actions/workflow/status/smythi93/Tests4Py/test-tests4py.yml?branch=main)](https://img.shields.io/github/actions/workflow/status/smythi93/Tests4Py/test-tests4py.yml?branch=main)
[![Coverage Status](https://coveralls.io/repos/github/smythi93/Tests4Py/badge.svg?branch=main)](https://coveralls.io/github/smythi93/Tests4Py?branch=main)
[![Licence](https://img.shields.io/github/license/smythi93/tests4py)](https://img.shields.io/github/license/smythi93/tests4py)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Tests4Py is an easy-to-use benchmark inspired by (BugsInPy)[https://github.com/soarsmu/BugsInPy] for evaluating and analyzing all things testing and debugging related.
Each subject in Tests4Py comes with a testing oracle, predefined system and unit tests, and the possibility to generate new system and unit tests on demand.

## Installation

### Prerequisite

Tests4Py requires [pyenv](https://github.com/pyenv/pyenv) to leverage the correct Python version for each subject. 
Tests4Py will automatically install pyenv if it is not installed on your machine. If this process fails, you can 
install pyenv manually by following the instructions at 
[https://github.com/pyenv/pyenv#installation](https://github.com/pyenv/pyenv#installation).


### Getting Tests4Py

Installing Tests4Py is as easy as calling the Python package manager `pip`:
```sh
pip install tests4py
```
If you have separate Python 2 and Python 3 on your machine, you may need to run the following:
```sh
pip3 install tests4py
```

If you want to install the latest development version, you can install Tests4Py directly from GitHub:
```sh
pip install git+https://github.com/smythi93/Tests4Py
```

## Using the Benchmark

The API of Tests4Py provides several commands, making it easy to use the benchmark.
You can leverage the API by importing Tests4Py in your program (see 
(this notebook)[https://github.com/smythi93/Tests4Py] for further information). Each call to the API returns an 
instance of a report that provides the information about the executed command.
Furthermore, each of these commands is accessible via Tests4Py's CLI.
You can find a listing of Tests4Py's most important commands in the following (additionally, you can try it yourself 
with (this notebook)[https://github.com/smythi93/Tests4Py]).

### T4P

`t4p` is Tests4Py's CLI. It provides all commands to interact with Tests4Py. You can get a list of all available 
commands by calling `t4p` without any arguments or `t4p --help` for a detailed list.

```
usage: t4p [-h] [--report REPORT] [--debug] [--version] {info,checkout,build,test,unittest,systemtest,config,cache,clear,grammar,sfl,run} ...

The access point to the tests4py framework

positional arguments:
  {info,checkout,build,test,unittest,systemtest,config,cache,clear,grammar,sfl,run}
                        The command of the tests4py framework to execute
    info                Get information of this benchmark and its projects
    checkout            Check out a project
    build               Build a project
    test                Run tests on a project that are included in the project
    unittest            Run or generate unittests
    systemtest          Run or generate system tests
    config              Edit the configuration of this benchmark
    cache               Cache a project to you local machine for faster access
    clear               Clear cached projects from your local machine
    grammar             Get the grammar of a project that specifies the input format
    sfl                 Conduct sfl (statistical fault localization) on a project
    run                 Run an input on a project and observe its result

options:
  -h, --help            show this help message and exit
  --report REPORT       Output the report to a file
  --debug               Activate debugging log
  --version             Show version number
```

### Getting the Information You Need

The `info` command provides all information about Tests4Py, its projects, and all its subjects.
It is accessible via the CLI with the following:
```
t4p info [-h] [-p PROJECT_NAME] [-i BUG_ID]

options:
  -h, --help       show this help message and exit
  -p PROJECT_NAME  The id of the project for which the information shall be printed
  -i BUG_ID        The bug number of the project_name for which the information shall be printed
```

### Retrieving a Subject 

The `checkout` command retrieves the source code of a subject to a defined position. Test4Py provides built-in caching; 
as soon as you check out a subject, Tests4Py will store the project repository in your home directory and uses this 
version for further checkouts.

```
t4p checkout [-h] -p PROJECT_NAME -i BUG_ID [-r] [-w WORK_DIR] [-u] [-f]

options:
  -h, --help       show this help message and exit
  -p PROJECT_NAME  The name of the project for which a particular version shall be checked out. Run tests4py info to 
                   check available project
  -i BUG_ID        The number of bug from project in tests4py. Run tests4py info to check bug id number
  -r, --repaired   Set the flag to checkout the repaired version, without the flag the buggy version will be checked out
  -w WORK_DIR      The working directory to which the buggy or fixed project version shall be checked out. The working 
                   directory has to be either empty or a previously used working directory. Default will be (./tmp)
  -u               If set the project won't be checked out again if it already exists at the specified location but 
                   only the tests4py data will be updated
  -f               If set the command won't use any cached version, even if the global cache flag is set
```

### Building a Subject

The `build` command utilizes the correct Python version based on the subject and your machine leveraging 
[pyenv](https://github.com/pyenv/pyenv), establishes the virtual environment, including all dependencies, and installs 
the subject in this environment. Tests4Py will store the virtual environment in your home directory and uses this 
environment for further compiles of this installed subject.

```
t4p build [-h] [-w WORK_DIR] [-r] [-f]

options:
  -h, --help   show this help message and exit
  -w WORK_DIR  The working directory to build the project. Default will be the current directory
  -r           Set to rebuild the project from scratch
  -f           If set the command won't use any cached version, even if the global cache flag is set
```

### Running the Original Tests

The `test` command executes the unit tests included in the project and outputs their results.

```
t4p test [-h] [-w WORK_DIR] [-t SINGLE_TEST] [-r] [-a] [-o OUTPUT]

options:
  -h, --help      show this help message and exit
  -w WORK_DIR     The working directory to run the test. Default will be the current directory
  -t SINGLE_TEST  Run single test from input. Default will run the test case that are failing for the bugs. Format for 
                  pytest: <test_file_path>::<test_method>. Format for unittest: 
                  <test_file_path_without.py>.<test_class>.<test_method>. Use tests4py info to get the information 
                  about the project
  -r              Run relevant test cases for the bug in the project. Default will run the test case that are failing 
                  for the bugs
  -a              Run all test cases in the project. Default will run the test case that are failing for the bugs
  -o OUTPUT       Output test results to file
```

### Running and Generating Unit Tests

To leverage the Tests4Py unit test capability, you must invoke the `unittest` with the two subcommands `test` that 
executes unit tests or `generate`. The generation can create an arbitrary number of failing and passing unit tests that 
can be investigated and executed.
```
t4p unittest [-h] {generate,test} ...

positional arguments:
  {generate,test}  The subcommand of the unittest to execute
    generate       Generate new unittests
    test           Run the unittests

options:
  -h, --help       show this help message and exit
```
```
t4p unittest test [-h] [-w WORK_DIR] [-p PATH] [-d] [-o OUTPUT]

options:
  -h, --help   show this help message and exit
  -w WORK_DIR  The working directory to run the test. Default will be the current directory
  -p PATH      The output path of the generated tests. Default will be (-w/tests4py_unittests.py) if -d is not set, 
               otherwise only the diversity tests are executed
  -d           Set to run diversity tests. When giving -p all tests in -p and the diversity tests are executed and
  -o OUTPUT    Output test results to file
```
```
t4p unittest generate [-h] [-w WORK_DIR] [-p PATH] [-n N] [-f P] [--passing] [--failing] [-a] [-v]

options:
  -h, --help   show this help message and exit
  -w WORK_DIR  The working directory to run the test. Default will be the current directory
  -p PATH      The output path of the generated tests. Default will be (tests4py_unittests.py)
  -n N         The number of generated tests. Default will be 1
  -f P         The number or probability of generated failing tests. If the number is a probability (<1) it will get 
               multiplied with -n to get the total number of failing tests. Default will be 1
  --passing    Set to generate only passing tests (<=> -p == 0). Cannot be set when --failing is set
  --failing    Set to generate only failing tests (<=> -p == -n). Cannot be set when --passing is set
  -a           Set to append the generated tests to the existing tests at -p
  -v           Set to verify the generated tests
```

### Running and Generating System Tests

You can also leverage the Tests4Py system test capability by invoking the `systemtest` command with the two subcommands 
`test` or `generate`. The generation can create an arbitrary number of failing and passing system tests that can be 
investigated and executed.

```
t4p systemtest [-h] {generate,test} ...

positional arguments:
  {generate,test}  The subcommand of the systemtest to execute
    generate       Generate new systemtests
    test           Run the systemtests

options:
  -h, --help       show this help message and exit
```

```
t4p systemtest test [-h] [-w WORK_DIR] [-p PATH] [-d] [-o OUTPUT]

options:
  -h, --help   show this help message and exit
  -w WORK_DIR  The working directory to run the test. Default will be the current directory
  -p PATH      The output path of the generated tests. Default will be (-w/tests4py_systemtests) if -d is not set, 
               otherwise only the diversity tests are executed
  -d           Set to run diversity tests. When giving -p all tests in -p and the diversity tests are executed and
  -o OUTPUT    Output test results to file
```

```
t4p systemtest generate [-h] [-w WORK_DIR] [-p PATH] [-n N] [-f P] [--passing] [--failing] [-a] [-v]

options:
  -h, --help   show this help message and exit
  -w WORK_DIR  The working directory to run the test. Default will be the current directory
  -p PATH      The output path of the generated tests. Default will be (tests4py_systemtests)
  -n N         The number of generated tests. Default will be 1
  -f P         The number or probability of generated failing tests. If the number is a probability (<1) it will get 
               multiplied with -n to get the total number of failing tests. Default will be 1
  --passing    Set to generate only passing tests (<=> -f == 0). Cannot be set when --failing is set
  --failing    Set to generate only failing tests (<=> -f == -n). Cannot be set when --passing is set
  -a           Set to append the generated tests to the existing tests at -p
  -v           Set to verify the generated tests

```

### Running an Input

The `run` command executes an input on the subject and outputs the result of the execution or when invoking the oracle 
consider it as a system test.

```
t4p run [-h] [-w WORK_DIR] [-o] test [test ...]

positional arguments:
  test         The path or string of the input

options:
  -h, --help   show this help message and exit
  -w WORK_DIR  The working directory to run the input. Default will be the current directory or last cached directory
  -o           Invoke the oracle to produce the result, if the input would be a test

```
### Configuring Tests4Py

To configure Tests4Py, you can use the `config` command. It allows you to set the global cache flag and the last 
working directory (which will be set automatically to the last used working directory).

```
t4p config [-h] flag value

positional arguments:
  flag        The flag for setting the value
  value       The value to set the flag

options:
  -h, --help  show this help message and exit
```

## Additional Information

We provide three notebooks that demonstrate the usage of Tests4Py and its capabilities on the example of statistical 
fault localization. You can find them in the `notebooks` folder.

Feel free to try them and experiment with them, since they provide easy access to Tests4Py.

## Citing Tests4Py

You can currently cite Tests4Py as follows:

```
@misc{smytzek2023tests4py,
      title={Tests4Py: A Benchmark for System Testing}, 
      author={Marius Smytzek and Martin Eberlein and Batuhan Serce and Lars Grunske and Andreas Zeller},
      year={2023},
      eprint={2307.05147},
      archivePrefix={arXiv},
      primaryClass={cs.SE}
}
```

## License

Tests4Py is licensed under the MIT License. See [LICENSE](LICENSE) for the full license text.