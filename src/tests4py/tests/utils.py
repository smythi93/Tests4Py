import enum
import os
import subprocess
from abc import abstractmethod
from os import PathLike
from pathlib import Path
from typing import List, Tuple, Collection

from tests4py.framework.constants import Environment, HARNESS_FILE


class TestResult(enum.Enum):
    FAILING = 0
    PASSING = 1
    UNDEFINED = 2


class API:
    def __init__(self, default_timeout=5):
        self.default_timeout = default_timeout

    @abstractmethod
    def run(self, system_test_path: PathLike, environ: Environment) -> TestResult:
        return NotImplemented

    def runs(
        self, system_tests_path: PathLike, environ: Environment
    ) -> List[Tuple[PathLike, TestResult]]:
        system_tests_path = Path(system_tests_path)
        if not system_tests_path.exists():
            raise ValueError(f"{system_tests_path} does not exist")
        if not system_tests_path.is_dir():
            raise ValueError(f"{system_tests_path} is not a directory")
        tests = list()
        for dir_path, _, files in os.walk(system_tests_path):
            for file in files:
                path = Path(dir_path, file)
                tests.append((path, self.run(path, environ)))
        return tests


class ExpectOutputAPI(API):
    def __init__(
        self,
        expected: bytes | Collection[bytes],
        executable: PathLike = HARNESS_FILE,
        expect_in: bool = False,
        is_stdout: bool = False,
        no_check: bool = False,
        is_or: bool = True,
        default_timeout: int = 5,
    ):
        self.expected = expected
        self.executable = executable
        self.is_stdout = is_stdout
        self.expect_in = expect_in
        self.no_check = no_check
        self.is_or = is_or
        super().__init__(default_timeout=default_timeout)

    # noinspection PyBroadException
    def run(self, system_test_path: PathLike, environ: Environment) -> TestResult:
        try:
            with open(system_test_path, "r") as fp:
                test = fp.read()
            if test:
                test = test.split("\n")
            else:
                test = []
            process = subprocess.run(
                ["python", HARNESS_FILE] + test,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=self.default_timeout,
                env=environ,
            )
            if self.no_check or process.returncode:
                if (any if self.is_or else all)(
                    map(
                        (
                            process.stdout if self.is_stdout else process.stderr
                        ).__contains__,
                        [self.expected]
                        if isinstance(self.expected, bytes)
                        else self.expected,
                    )
                ):
                    return TestResult.PASSING if self.expect_in else TestResult.FAILING
                elif self.no_check:
                    return TestResult.FAILING if self.expect_in else TestResult.PASSING
                else:
                    return TestResult.UNDEFINED
            else:
                return TestResult.PASSING
        except subprocess.TimeoutExpired:
            return TestResult.UNDEFINED
        except Exception:
            return TestResult.UNDEFINED


class ExpectErrAPI(ExpectOutputAPI):
    def __init__(
        self, expected: bytes | Collection[bytes], executable: PathLike = HARNESS_FILE
    ):
        super().__init__(expected, executable)


class ExpectOutAPI(ExpectOutputAPI):
    def __init__(
        self, expected: bytes | Collection[bytes], executable: PathLike = HARNESS_FILE
    ):
        super().__init__(expected, executable, is_stdout=True)


class ExpectNotErrAPI(ExpectOutputAPI):
    def __init__(
        self, expected: bytes | Collection[bytes], executable: PathLike = HARNESS_FILE
    ):
        super().__init__(expected, executable, expect_in=True)


class ExpectNotOutAPI(ExpectOutputAPI):
    def __init__(
        self, expected: bytes | Collection[bytes], executable: PathLike = HARNESS_FILE
    ):
        super().__init__(expected, executable, is_stdout=True, expect_in=True)
