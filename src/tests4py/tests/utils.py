import enum
import os
import subprocess
from abc import abstractmethod
from os import PathLike
from pathlib import Path
from typing import List, Tuple, Collection, Union, Any, Dict

from tests4py.constants import Environment, HARNESS_FILE


class TestResult(enum.Enum):
    FAILING = "FAILING"
    PASSING = "PASSING"
    UNDEFINED = "UNDEFINED"


class API:
    def __init__(self, default_timeout=5):
        self.default_timeout = default_timeout

    @abstractmethod
    def oracle(self, args: Any) -> TestResult:
        raise NotImplementedError()

    def get_test_arguments(self, system_test_path: PathLike) -> List[str]:
        with open(system_test_path, "r") as fp:
            test = fp.read()
        return test.split("\n") if test else []

    # noinspection PyBroadException
    def execute(self, system_test_path: PathLike, environ: Environment) -> Any:
        try:
            process = subprocess.run(
                ["python", HARNESS_FILE] + self.get_test_arguments(system_test_path),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=self.default_timeout,
                env=environ,
            )
            return process
        except subprocess.TimeoutExpired:
            return None
        except Exception:
            return None

    def run(self, system_test_path: PathLike, environ: Environment):
        try:
            return system_test_path, self.oracle(
                self.execute(system_test_path, environ)
            )
        finally:
            self.clean_up()

    def clean_up(self):
        pass

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
                tests.append(self.run(path, environ))
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

    def oracle(self, args: Any) -> TestResult:
        process = args
        if process is None:
            return TestResult.UNDEFINED
        if self.no_check or process.returncode:
            if (any if self.is_or else all)(
                map(
                    (process.stdout if self.is_stdout else process.stderr).__contains__,
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
