# Tests4Py

[![Python Version](https://img.shields.io/pypi/pyversions/sflkit)](https://pypi.org/project/tests4py/)
[![GitHub release](https://img.shields.io/github/v/release/uds-se/sflkit)](https://img.shields.io/github/v/release/smythi93/tests4py)
[![PyPI](https://img.shields.io/pypi/v/sflkit)](https://pypi.org/project/tests4py/)
[![Build Status](https://img.shields.io/github/actions/workflow/status/smythi93/tests4py/test-tests4py.yml?branch=main)](https://img.shields.io/github/actions/workflow/status/smythi93/tests4py/test-tests4py.yml?branch=main)
[![Coverage Status](https://coveralls.io/repos/github/smythi93/tests4py/badge.svg?branch=main)](https://coveralls.io/github/smythi93/tests4py?branch=main)
[![Licence](https://img.shields.io/github/license/smythi93/tests4py)](https://img.shields.io/github/license/smythi93/tests4py)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Tests4Py is an easy-to-use benchmark inspired by (BugsInPy)[https://github.com/soarsmu/BugsInPy] for evaluating and analyzing all things testing and debugging related.
Each subject in Tests4Py comes with a testing oracle, predefined system and unit tests, and the possibility to generate new system and unit tests on demand.

## Installation

### Prerequisite

Tests4Py requires [pyenv](https://github.com/pyenv/pyenv) to leverage the correct Python version for each subject. 
Please follow the instructions at [https://github.com/pyenv/pyenv#installation](https://github.com/pyenv/pyenv#installation) to install pyenv.

### Getting Tests4Py

Installing Tests4Py is as easy as calling the Python package manager `pip`:
```sh
pip install tests4py
```
If you have separate Python 2 and Python 3 on your machine, you may need to run the following:
```sh
pip3 install tests4py
```

## Using the Benchmark

The API of Tests4Py provides several commands, making it easy to use the benchmark.
The API you can leverage by importing Tests4Py returns an instance of a report that provides the information about the executed command.
Furthermore, each of these commands is accessible via Tests4Py's CLI.
You can find a listing of Tests4Py's most important commands in the following.

### Getting the Information You Need

The `info` command provides all information about Tests4Py, its projects, and all its subjects.
It is accessible via the CLI with the following:
```
usage: t4p info [-h] [-p PROJECT_NAME] [-i BUG_ID]

options:
  -h, --help       show this help message and exit
  -p PROJECT_NAME  The id of the project for which the information shall be
                   printed
  -i BUG_ID        The bug number of the project_name for which the
                   information shall be printed
```

### Getting a Subject 

The `checkout` command retrieves the source code of a subject to a defined position. Test4Py provides built-in caching; as soon as you check out a subject, Tests4Py will store the project repository in your home directory and uses this version for further checkouts.

```
t4p checkout [-h] -p PROJECT_NAME -i BUG_ID [-r] [-w WORK_DIR] [-u] [-f]

options:
  -h, --help       show this help message and exit
  -p PROJECT_NAME  The name of the project for which a particular version shall be checked out. Run tests4py info to check
                   available project
  -i BUG_ID        The number of bug from project in tests4py. Run tests4py info to check bug id number
  -r, --repaired   Set the flag to checkout the repaired version, without the flag the buggy version will be checked out
  -w WORK_DIR      The working directory to which the buggy or fixed project version shall be checked out. The working
                   directory has to be either empty or a previously used working directory. Default will be
                   (cwd/tmp)
  -u               If set the project won't be checked out again if it already exists at the specified location but only the
                   tests4py data will be updated
  -f               If set the command won't use any cached version, even if the global cache flag is set
```

### Building a Subject

The `compile` command utilizes the correct Python version based on the subject and your machine leveraging [pyenv](https://github.com/pyenv/pyenv), establishes the virtual environment, including all dependencies, and installs the subject in this environment. Tests4Py will store the virtual environment in your home directory and uses this environment for further compiles of this installed subject.

```
t4p compile [-h] [-w WORK_DIR] [-r] [-f]

options:
  -h, --help   show this help message and exit
  -w WORK_DIR  The working directory to compile the project. Default will be the current directory
  -r           Set to recompile the project from scratch
  -f           If set the command won't use any cached version, even if the global cache flag is set
```
