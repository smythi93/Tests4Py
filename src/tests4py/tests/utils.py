import abc
import enum
import os
import subprocess
import tempfile
from abc import abstractmethod
from os import PathLike
from pathlib import Path
from typing import List, Tuple, Collection, Any, Optional

from tests4py.constants import Environment, HARNESS_FILE, PYTHON
from tests4py.logger import LOGGER


class TestResult(enum.Enum):
    FAILING = "FAILING"
    PASSING = "PASSING"
    UNDEFINED = "UNDEFINED"


class API:
    def __init__(self, default_timeout=5):
        self.default_timeout = default_timeout

    @abstractmethod
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        raise NotImplementedError()

    def get_test_arguments(self, system_test_path: PathLike) -> List[str]:
        with open(system_test_path, "r") as fp:
            test = fp.read()
        parts = test.split("\n")
        if parts and parts[-1] == '':
            parts.pop()
        return parts if parts else []

    # noinspection PyBroadException
    def execute(
        self,
        system_test_path: PathLike,
        environ: Environment,
        work_dir: Optional[Path] = None,
    ) -> Any:
        try:
            process = subprocess.run(
                [PYTHON, HARNESS_FILE] + self.get_test_arguments(system_test_path),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=self.default_timeout,
                env=environ,
                cwd=Path.cwd() if work_dir is None else work_dir,
            )
            return process
        except subprocess.TimeoutExpired:
            return None
        except Exception:
            return None

    def run(
        self,
        system_test_path: PathLike,
        environ: Environment,
        work_dir: Optional[Path] = None,
    ) -> Tuple[PathLike, TestResult, str]:
        try:
            return system_test_path, *self.oracle(
                self.execute(system_test_path, environ, work_dir=work_dir)
            )
        finally:
            self.clean_up()

    def clean_up(self):
        pass

    def runs(
        self,
        system_tests: PathLike | str,
        environ: Environment,
        work_dir: Optional[Path] = None,
    ) -> List[Tuple[PathLike | str, TestResult, str]]:
        system_tests_path = Path(system_tests)
        tests = list()
        if len(str(system_tests_path)) > 265 or not system_tests_path.exists():
            LOGGER.info(
                f"Path {repr(system_tests)} does not exist, try to execute it as test case"
            )
            with tempfile.NamedTemporaryFile(mode="w") as tmp:
                tmp.write(system_tests)
                tmp.flush()
                _, test_result, feedback = self.run(
                    tmp.name, environ, work_dir=work_dir
                )
                tests.append((system_tests, test_result, feedback))
        elif not system_tests_path.is_dir():
            LOGGER.info(f"Path {system_tests_path} is a file")
            tests.append(self.run(system_tests_path, environ, work_dir=work_dir))
        else:
            for dir_path, _, files in os.walk(system_tests_path):
                for file in files:
                    path = Path(dir_path, file)
                    tests.append(self.run(path, environ, work_dir=work_dir))
        return tests


class CLIAPI(API, abc.ABC):
    def __init__(self, cli: List[str], default_timeout=5):
        super().__init__(default_timeout=default_timeout)
        self.cli = cli

    def execute(
        self,
        system_test_path: PathLike,
        environ: Environment,
        work_dir: Optional[Path] = None,
    ) -> Any:
        try:
            process = subprocess.run(
                self.cli + self.get_test_arguments(system_test_path),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=self.default_timeout,
                env=environ,
                cwd=Path.cwd() if work_dir is None else work_dir,
            )
            return process
        except subprocess.TimeoutExpired:
            return None
        except Exception:
            return None


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

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        process = args
        if process is None:
            return TestResult.UNDEFINED, "Cannot identify executed process"
        feedback = process.stdout if self.is_stdout else process.stderr
        if self.no_check or process.returncode:
            if (any if self.is_or else all)(
                map(
                    feedback.__contains__,
                    [self.expected]
                    if isinstance(self.expected, bytes)
                    else self.expected,
                )
            ):
                return (
                    TestResult.PASSING if self.expect_in else TestResult.FAILING,
                    feedback,
                )
            elif self.no_check:
                return (
                    TestResult.FAILING if self.expect_in else TestResult.PASSING,
                    feedback,
                )
            else:
                return TestResult.UNDEFINED, feedback
        else:
            return TestResult.PASSING, feedback


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
