import enum
import os
from abc import abstractmethod
from os import PathLike
from pathlib import Path
from typing import List, Tuple

from Tests4Py.framework.constants import Environment


class TestResult(enum.Enum):
    FAILING = 0
    PASSING = 1
    UNKNOWN = 2


class API:

    def __init__(self, default_timeout=5):
        self.default_timeout = default_timeout

    @abstractmethod
    def run(self, system_test_path: PathLike, environ: Environment) -> TestResult:
        return NotImplemented

    def runs(self, system_tests_path: PathLike, environ: Environment) -> List[Tuple[PathLike, TestResult]]:
        system_tests_path = Path(system_tests_path)
        if not system_tests_path.exists():
            raise ValueError(f'{system_tests_path} does not exist')
        if not system_tests_path.is_dir():
            raise ValueError(f'{system_tests_path} is not a directory')
        tests = list()
        for dir_path, _, files in os.walk(system_tests_path):
            for file in files:
                path = Path(dir_path, file)
                tests.append((path, self.run(path, environ)))
        return tests
