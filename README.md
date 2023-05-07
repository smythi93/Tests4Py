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
```sh
usage: t4p info [-h] [-p PROJECT_NAME] [-i BUG_ID]

options:
  -h, --help       show this help message and exit
  -p PROJECT_NAME  The id of the project for which the information shall be
                   printed
  -i BUG_ID        The bug number of the project_name for which the
                   information shall be printed
```


